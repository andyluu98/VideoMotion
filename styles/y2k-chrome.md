# Y2K Chrome (bạc bóng, ánh xà cừ, bong bóng năm 2000)

> Chữ và vật như kim loại bạc bóng loáng phản chiếu bầu trời, viền sáng, ánh cầu vồng xà cừ, bong bóng nhựa trong và ngôi sao lấp lánh trên nền xanh trời hoặc tím đêm, đặt trong cửa sổ bo tròn.

**Hợp:** ra mắt sản phẩm công nghệ trẻ, âm nhạc và thời trang, hoài niệm đầu những năm 2000, sự kiện giới trẻ, trailer app, tổng kết năm vui.
**Không hợp:** báo cáo tài chính, nội dung trang nghiêm, y tế, bài giảng dày chữ, thương hiệu truyền thống.
**Cảm xúc:** lạc quan, bóng bẩy, mơ về tương lai, hoài niệm, lấp lánh.

## Hình dung
Màn hình máy tính bỏ túi thời đĩa CD: nền trời xanh nhạt có mây trắng, một cửa sổ bo tròn viền bạc nổi lên, trong đó chữ khối bạc phản chiếu đường chân trời, một quả cầu chrome xoay chậm và vài bong bóng trong suốt trôi lên. Mọi mặt phẳng đều như vừa được đánh bóng. Người xem muốn chạm vào nút bấm.

## Bảng màu
```css
--sky: #BFE3FF;      /* xanh trời, nền sáng */
--sky-hi: #EAF6FF;   /* trắng xanh, mây */
--night: #1B1040;    /* tím đêm, nền tối */
--chrome-1: #F7FAFF; /* bạc sáng nhất */
--chrome-2: #AEB9CC; /* bạc trung */
--chrome-3: #5C6784; /* bạc tối, đáy dải */
--ink: #232B45;      /* chữ trên nền sáng */
--pearl-pink: #FF9ED8;
--pearl-lilac: #B9A2FF;
--pearl-mint: #8FF0D6;
--pearl-lemon: #FFF2A0;
--pop: #2E7CFF;      /* xanh nút bấm */
```
- Kim loại là gradient nhiều dải: sáng, tối, sáng, tối, sáng (đường chân trời giả), không phải một màu bạc phẳng.
- Xà cừ chỉ dùng như ánh cầu vồng pastel (hồng, tím, bạc hà, vàng chanh) trượt trên mặt bóng, mờ vừa, không thành mảng sặc sỡ.
- Một nền chính mỗi cảnh: xanh trời hoặc tím đêm, không trộn.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@1,800&family=Lexend:wght@400;600&display=swap" rel="stylesheet">
```
- Tiêu đề: Exo 2 800 (có tiếng Việt, đã kiểm đủ dấu), nghiêng nhẹ, IN HOA hoặc chữ thường to, tô gradient bạc nhiều dải kèm viền sáng và bóng đổ tối phía dưới.
- Thân và nhãn: Lexend 400 và 600 (có tiếng Việt, đã kiểm đủ dấu), tròn, thoáng, dễ đọc trên nền bóng.
- Dòng nhỏ giãn 0,12em, màu bạc tối hoặc xanh nút bấm.

## Bề mặt
Nền trời gradient xanh lên trắng ở chân trời, vài đám mây elip mờ. Cửa sổ bo tròn bán kính lớn, viền bạc hai lớp, thanh tiêu đề gradient bạc với ba nút tròn bóng. Mọi khối có một vệt sáng cong ở nửa trên (highlight) và một viền sáng mảnh.
```css
.chrome-text { background: linear-gradient(180deg, #fff 0%, #cfd8e8 28%, #5c6784 48%, #e9f0fb 52%, #9aa6c0 78%, #f7faff 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  -webkit-text-stroke: 2px rgba(255,255,255,.9); filter: drop-shadow(0 6px 0 rgba(35,43,69,.35)); }
```
(`filter` chỉ để tĩnh, không tween.)

## Ngôn ngữ minh họa
- **Quả cầu chrome:** đường tròn với gradient xuyên tâm lệch, một dải ngang tối giả đường chân trời, vệt sáng trắng cong ở trên, viền sáng.
- **Bong bóng trong:** vòng tròn viền xà cừ, ruột gần như trong suốt, hai chấm sáng đối diện.
- **Ngôi sao bốn cánh:** đa giác lõm bốn đỉnh, trắng lõi, tỏa tia mảnh; rải thưa.
- **Cửa sổ bo tròn:** thanh tiêu đề bạc, ba nút bóng (hồng, vàng chanh, bạc hà), thanh cuộn tròn.
- **Nút bấm viên thuốc:** gradient xanh, viền trắng, vệt sáng nửa trên.
- Biểu tượng nên có: đĩa CD, bướm, tim nhựa, mũi tên bóng, dấu hoa thị, vòng quay chữ.
- Mọi vật có một hướng sáng (trên trái) và highlight cong; không nét tay.

## Chữ ký chuyển động
- **Vệt sáng lướt mặt chrome:** một dải xiên trắng mờ trượt ngang qua chữ hoặc quả cầu, mỗi lần một lần.
- **Xoay khoe ánh kim:** vật xoay chậm, gradient bên trong đổi phía nên ánh kim đổi theo.
- **Nảy đàn hồi:** vật rơi vào chỗ với `elastic.out` hoặc `back.out`, rồi đứng yên.
- **Sao lấp lánh:** ngôi sao nở rồi thu (scale và opacity), lệch pha nhau.
- **Bong bóng trôi lên:** bay chậm, lắc ngang nhẹ, vỡ thành ngôi sao nhỏ.
- Nhịp: vui, bóng, có độ nảy; mỗi cú nảy dừng dứt khoát, không rung kéo dài.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** cửa sổ bo tròn bật lên với độ nảy, tiêu đề chrome bị vệt sáng quét qua, quả cầu chrome xoay bên cạnh.
- **Tính năng mới:** nút viên thuốc phồng lên, bong bóng mang biểu tượng trôi quanh.
- **Số liệu:** con số chrome lớn trong ô kính, ngôi sao lấp lánh ở góc.
- **Kết:** nền đổi sang tím đêm, quả cầu chrome xoay chậm, một dòng cảm ơn dưới thanh trượt.

## Nên tránh
Bạc một màu phẳng, cầu vồng sặc sỡ phủ cả khung, quá nhiều hiệu ứng lấp lánh cùng lúc, bóng chữ nhòe làm mất nét, nền xám xỉn, bố cục tối giản trống trải, tên và logo hệ điều hành hay hãng có thật.

## Họ hàng
`retro-windows` (cùng giao diện cửa sổ nhưng xám vát cạnh kiểu 1995, phẳng và tếu), `aurora` (cũng ánh màu chuyển trên nền tối nhưng mềm, không kim loại), `cel-anime-80s` (cùng hoài niệm neon nhưng thập niên 80, nét cel).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/y2k-chrome.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một cửa sổ bo tròn lơ lửng trên bầu trời xanh, bên trong là sân khấu tím đêm nhỏ. Vật chính là một quả cầu chrome lớn và một dòng tiêu đề chữ khối bạc; quanh đó vài bong bóng nhựa trong, ngôi sao bốn cánh, một đĩa CD cầu vồng. Nếu cần nhân vật thì là một con robot bạc tròn trĩnh, mắt ngọc, khoảng 3 đầu cao, tay cầm bong bóng; nhân vật phải cùng chất liệu chrome với phông nền.
- **Chất liệu và ánh sáng:** gradient nhiều dải cho mọi mặt kim loại (sáng, tối, sáng, tối, sáng), viền sáng 2 đến 3px, highlight cong nửa trên, xà cừ là lớp elip gradient hồng, tím, bạc hà, vàng chanh mờ trên mặt bóng. Một hướng sáng duy nhất (trên trái). Bóng đổ elip tím mờ dưới vật. Không dùng `mix-blend-mode`; vệt sáng là hình xiên trắng mờ. Chỉ tween transform, opacity, màu, clipPath.
- **Máy quay và khung:** ngang tầm mắt, hơi chếch lên, vật chính đặt trên trục giữa hoặc lệch một phần ba, đủ chỗ cho tiêu đề. Di máy rất chậm bằng scale và translate các lớp: trời xa, cửa sổ, vật chính, bong bóng gần mỗi lớp một tốc độ. Khung dọc: xếp quả cầu trên, tiêu đề dưới.
- **Chuyển động:** vật xoay và trôi mượt, đổi chỗ có độ nảy đàn hồi ngắn rồi đứng yên. Vệt sáng quét một lần mỗi vật. Sao lấp lánh lệch pha. Ease `back.out`, `elastic.out(1, 0.5)`, `sine.inOut`.
- **Chữ trên hình:** tiêu đề Exo 2 800 gradient bạc có viền sáng; phụ đề là thanh kính mờ bo tròn viền bạc, chữ Lexend 600 màu mực, có thể có ngôi sao nhỏ đầu dòng. Phải đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Cửa sổ bật lên với độ nảy, thanh tiêu đề trượt xuống (hợp mở màn, giới thiệu).
  - Vệt sáng lướt qua chữ chrome đúng nhịp từ khóa (hợp nhấn mạnh, công bố).
  - Bong bóng phồng lên mang biểu tượng rồi vỡ thành sao (hợp liệt kê tính năng).
  - Quả cầu chrome xoay, ánh kim đổi phía theo lời nói (hợp chuyển ý, khoe sản phẩm).
  - Nền đổi từ xanh trời sang tím đêm khi sang chương cuối.
- **Bẫy:** gradient bạc ít dải trông như xám phẳng. Quá nhiều sao và bong bóng làm rối vật chính. Chữ chrome nền sáng cần viền tối mỏng hoặc bóng đổ để không chìm. Highlight không bám theo hình cầu nên trông dán. Cầu vồng phủ cả khung làm mất chất kim loại.

*Phỏng theo thẩm mỹ chung của thập niên 2000, tự vẽ bằng HTML, SVG, CSS và GSAP.*

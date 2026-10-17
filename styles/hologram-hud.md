# HUD hologram (màn hình quét khung dây ánh sáng)

> Sân khấu gần đen, một sắc xanh ngọc lạnh đổi độ mờ để tạo chiều sâu, vật thể là khung dây vừa được quét, và màu cam chỉ xuất hiện khi một con số đã được khóa.

**Hợp:** giới thiệu sản phẩm công nghệ, thông số kỹ thuật, gọi vốn, màn hình trình diễn hội chợ, phần cứng, hàng không, an ninh hệ thống.
**Không hợp:** văn hóa truyền thống, nội dung ấm áp, trẻ em, tài liệu để in.
**Cảm xúc:** viễn tưởng, chính xác, lạnh, công nghệ.

## Hình dung
Người xem như đứng trước bàn chiếu hologram trong phòng điều khiển: một bệ chiếu phát nón sáng, vật thể hiện lên bằng nét ánh sáng mảnh, xung quanh là đồ nghề đo đạc (vòng đồng hồ, thước chia, khung góc màn hình, bóng đánh số). Mọi thứ trông như dữ liệu vừa được quét. Không phải neon rực rỡ: lạnh, kỷ luật, như dụng cụ đo.

## Bảng màu
```css
--bg: #04111a;       /* sân khấu gần đen */
--fg: #dffcf8; --muted: #86d4cd;   /* chữ */
--line: #3be8d9;     /* cạnh chính, vật gần */
--line-soft: rgba(59, 232, 217, 0.6);  /* cạnh phụ, đường dẫn */
--hair: rgba(59, 232, 217, 0.24);      /* vật xa, lưới */
--face: rgba(59, 232, 217, 0.09);      /* mặt trong suốt */
--hot: #eafffd;      /* cạnh "nóng": vừa quét tới, đang khóa */
--lock: #ff9a2e;     /* cam số liệu đã khóa: chỉ ở chữ, số lớn */
--plate: rgba(3, 14, 22, 0.84);        /* tấm nền tối dưới mọi nhãn */
--accent: #7ff3e8;
```
Một sắc lạnh duy nhất; vật xa chìm còn 25 đến 30 phần trăm. Trắng ngà chỉ cho thứ đang nóng. Cam là phần thưởng: chỉ cho số liệu đã khóa (số lớn, mốc thời gian) và nằm ở chữ của slide, không đưa vào hình SVG.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
```
- Tiêu đề, nhãn trong hình: Chakra Petch 500, IN HOA, giãn 0,05 đến 0,1em.
- Thân: Barlow 400 đến 500.
- Số, mã, bóng đánh số, "QUÉT 03": IBM Plex Mono 500 đến 600.
Cả ba font có tiếng Việt (đã kiểm ngày 16/10/2026).

## Bề mặt
Nền gần đen, lưới chấm xanh ngọc 48px, vạch quét ngang rất mờ cách 4px, quầng sáng chiếu ở nửa phải, tối dần bốn góc.
```css
background-image:
  radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 52%, rgba(0,0,0,.62) 100%),
  radial-gradient(circle, rgba(59,232,217,.34) 1.3px, transparent 1.9px),
  repeating-linear-gradient(0deg, rgba(59,232,217,.04) 0 1px, transparent 1px 4px),
  radial-gradient(ellipse at 76% 54%, rgba(22,120,130,.34) 0%, rgba(22,120,130,0) 56%);
background-size: 100% 100%, 48px 48px, 100% 100%, 100% 100%;
```

## Ngôn ngữ minh họa
- **Vật là khung dây ánh sáng**, không tô đặc: cạnh chính 2,5px, cạnh nóng 3px, đường dẫn 1,8 đến 2px, đầu và góc tròn.
- **Khối chiếu đẳng cự** (trục nghiêng 30 độ) trên một bệ chiếu, bóng in xuống bệ bằng hai elip mờ.
- **Tầng nổ theo trục:** các tầng chồng nhau tách ra dọc một trục đứt `22 6 4 6`; tầng đang xét sáng nóng, tầng dưới chìm dần.
- **Khóa mục tiêu:** bốn góc chữ L dài 20 đến 30px ôm chi tiết.
- **Đồng hồ cung bảy đoạn**, **thanh vạch** (vạch đứng cách 22px, số vạch sáng nói mức độ), **thước chia** dưới trục.
- **Tấm nền nhãn:** hộp tối có bốn tick góc sáng, đánh số mono; chữ không bao giờ đè lên nét khung dây.
- Hai tư thế một vật: tư thế cũ nét khuất `8 7`, tư thế mới nóng, nối bằng đường phantom `26 6 6 6`.
- Không vẽ người, logo, sản phẩm có thật; vật là ẩn dụ của chủ đề.

## Chữ ký chuyển động
- **Dải quét lộ hình:** một mặt phẳng quét sáng chạy dọc khung (`data-loop="scan"` hoặc lớp `data-scene`), vật hiện dần theo đúng chỗ dải đi qua (`wipe` từ trên xuống).
- **Cạnh nóng trước, phần còn lại sau:** cạnh `--hot` `draw` đầu tiên, rồi đường dẫn, rồi tấm nền nhãn `fade`, như máy quét khóa đường viền trước khi đọc chi tiết.
- **Khóa mục tiêu và đếm số:** bốn góc L từ rộng co lại ôm vật (`zoom` ngược, nhanh, dừng gắt), ngay sau đó số cam chạy `data-count` và đứng yên.
- **Nón sáng bật từ bệ:** nón chiếu dâng lên bằng `rise-wipe` khi vào slide có vật mới.
- **Vòng đồng hồ quay chậm:** vòng đo ngoài cùng `spin` rất chậm (`data-loop-dur` 30 đến 60 giây), thứ lặp duy nhất.
- Nhịp: nhanh, gắt, tuyến tính, không nảy, không nhấp nháy; cả hình xong trong khoảng 2 giây.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** bệ chiếu bên phải, nón sáng dâng, ba tầng của vật nổ theo trục, khung khóa ôm tầng trên cùng, dải quét cắt ngang; tên deck trên tấm nền tối bên trái.
- **Thông số:** đồng hồ cung và thanh vạch, mỗi thông số một tấm nền nhãn; con số chính khóa xong mới chuyển cam.
- **Quy trình:** trục sáng có thước chia, mỗi bước một trạm vuông tối có tick góc; đoạn nối giữa hai trạm chạy sáng lần lượt; trạm cuối bị khóa mục tiêu.
- **Trước và sau:** tư thế cũ nét khuất, tư thế mới nhấc khỏi bóng, đường phantom có mũi tên nối hai tư thế.

## Nên tránh
Màu ngoài bảng (nhất là cam trong hình), gradient màu, bóng đổ màu, glow neon, mặt đặc che hết khung dây; chữ nằm trên nét; số đo bịa trên nhãn và đồng hồ; logo, sản phẩm có thật, giao diện của phim cụ thể; nhấp nháy, rung.

## Họ hàng
`neon-cyber` (neon phát sáng, có hồng tím, năng lượng cao; hud thì một sắc lạnh, không glow, là đồ nghề đo), `terminal-green` (giao diện chữ dòng lệnh; hud là khung dây và đồng hồ), `blueprint` (bản vẽ kỹ thuật nét trắng trên giấy xanh, cổ điển; hud là màn chiếu tương lai trên nền đen).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/hologram-hud.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Phòng điều khiển tối với một bệ chiếu tròn ở nửa dưới, nón sáng mờ dựng lên phía trên. Trên bệ là một vật thể khung dây ánh sáng (ví dụ một chiếc xe đạp điện đẳng cự, nghiêng 3/4) chiếm khoảng 60% chiều cao khung; vật là ẩn dụ của chủ đề, mọi bộ phận nối liền nhau. Bên trái là ba tấm nhãn tối xếp dọc, mỗi tấm một số đo màu cam. Bốn góc là khung HUD.
- **Chất liệu và ánh sáng:** Nền gần đen xanh thẫm, lưới chấm xanh ngọc, quầng sáng sau vật, tối góc. Cạnh khung dây bằng stroke 1,5 đến 2,5px, ba mức độ mờ theo độ xa (gần sáng, xa chìm 25 đến 30%); một lớp stroke dày hơn, mờ, đặt dưới để giả glow, không dùng filter động. Mặt trong suốt rất nhạt. Bệ là các elip đồng tâm, một vòng đứt nét, vài vạch chia. Nón sáng là gradient dọc mờ dần. Cam chỉ ở chữ số đã khóa.
- **Máy quay và khung dọc 9:16:** Hơi nhìn từ trên xuống, 3/4. Máy đẩy vào rất chậm hoặc quay nhẹ bằng cách scale/translate lớp vật, lớp bệ và lớp HUD với tốc độ khác nhau (HUD nhanh hơn, lưới chậm nhất). Khung dọc: vật ở nửa trên, các tấm nhãn xếp chồng ở nửa dưới, không đè lên nét khung dây.
- **Chuyển động:** Nhanh, gắt, tuyến tính, không nảy, không nhấp nháy. Dải quét chạy qua vật, vật lộ dần theo đường dải đi qua (`clipPath`). Cạnh nóng vẽ trước, tấm nhãn hiện sau. Vòng đồng hồ ngoài cùng quay rất chậm.
- **Chữ trên hình:** Nhãn IN HOA Chakra Petch, số Plex Mono (đơn cách để không nhảy khi đếm). Mỗi khối chữ có tấm nền tối viền 1px và tick góc, có số thứ tự nhỏ. Chữ không bao giờ nằm trên nét khung dây. Phụ đề là tấm HUD tối có góc ngoặc ở giữa đáy. Phải đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Dải quét lộ hình: mặt phẳng sáng quét xuống, vật hiện theo (hợp giới thiệu sản phẩm).
  - Khóa mục tiêu: bốn góc L từ rộng co lại ôm chi tiết, rồi số cam chạy và đứng yên (hợp thông số chính).
  - Tầng nổ theo trục: các lớp tách dọc trục đứt, lớp đang xét sáng nóng (hợp cấu tạo, bóc tách).
  - Chip nạp dần: số đã khóa trượt vào dải bên và ở lại (hợp 3 đến 5 ý phải đọc hết).
- **Bẫy:** Dùng cam trong hình vẽ làm hỏng luật màu. Mặt đặc che khung dây thành khối nhựa. Bộ phận trôi lơ lửng không nối nên bị nhìn ra ngay. Số đo bịa trên nhãn. Glow nặng hoặc nhấp nháy làm mất vẻ dụng cụ đo.

Phỏng theo `styles/hologram-hud/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

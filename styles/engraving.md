# Tranh khắc đồng (tờ minh họa sách khoa học thế kỷ 19)

> Cả deck là một tờ in từ bản đồng trên giấy kem có vân: một màu mực nâu đen, độ đậm nhạt chỉ làm bằng nét phình thon đan chéo, một lớp màu nước hổ phách đặt tay lem ra ngoài nét.

**Hợp:** bảo tàng, giải thích khoa học, lịch sử tự nhiên, di sản thương hiệu, bài giảng lịch sử, y học, thực vật học.
**Không hợp:** công nghệ hiện đại, thời trang trẻ, sự kiện sôi động, số liệu kinh doanh dày.
**Cảm xúc:** cổ điển, tinh xảo, học thuật, di sản.

## Hình dung
Người xem như lật một tập bản khắc trong thư viện cổ: mỗi slide là "HÌNH n", chủ thể đặt giữa vòng kính lúp, bóng số gọi tên từng bộ phận, chú thích chữ nghiêng bên dưới, góc tờ có dấu ép bản đồng. Chậm, kỹ, đáng tin: cảm giác của tri thức được người thợ đục từng nét.

## Bảng màu
```css
--paper: #f1e8d2;    /* giấy kem có vân, quầng quanh chủ thể */
--paper-2: #f8f1de;  /* tờ giấy rời */
--ink: #1c1510;      /* mực duy nhất: nét, chữ */
--line-soft: rgba(28, 21, 16, 0.6);  /* nét mảnh, đường dẫn */
--hair: rgba(28, 21, 16, 0.3);       /* nét rất mảnh, kẻ dòng */
--wash: #c98a2e;     /* màu nước hổ phách, fill-opacity 0,4 */
--rose: #7f3023;     /* đỏ nâu: chỉ cho nhãn chữ, không vào hình */
--muted: #5a4a38;
```
Một mực, một lớp màu nước hổ phách mỗi slide, một sắc đỏ nâu cho nhãn chữ. Màu nước đến sau, trong, lem nhẹ ra ngoài nét, mực luôn nằm trên. Không tô mảng xám hay đen đặc.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@400;700;900&family=Newsreader:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
```
- Tiêu đề, nhãn "HÌNH n": Playfair Display SC 700, chữ hoa nhỏ kiểu La Mã, giãn 0,03 đến 0,1em.
- Thân, chú thích, số bóng: Newsreader 400 đến 500, chữ nghiêng cho chú thích.
Cả hai font có tiếng Việt (đã kiểm ngày 16/10/2026). Bản gốc ghi rõ Bodoni Moda và Pinyon Script không dùng vì thiếu tiếng Việt.

## Bề mặt
Giấy kem có sợi, đường xích dọc mờ cách 38px, đường kẻ ngang rất mảnh cách 5px, vài đốm ố vàng, tối dần về mép. Khung kẻ viền tờ in và dấu ép bản đồng lõm nhẹ quanh vùng hình.
```css
background-image:
  repeating-linear-gradient(90deg, rgba(120,92,50,.05) 0 2px, transparent 2px 38px),
  repeating-linear-gradient(0deg, rgba(120,92,50,.04) 0 1px, transparent 1px 5px),
  radial-gradient(ellipse at 50% 50%, rgba(150,110,55,0) 62%, rgba(150,110,55,.2) 100%),
  radial-gradient(120% 100% at 40% 35%, #f5edd9 0%, #f1e8d2 55%, #e9dcbd 100%);
```

## Ngôn ngữ minh họa
- **Nét đục phình thon:** mỗi nét là một hình thoi dài, mảnh hai đầu, dày ở giữa; đường dài cắt thành đoạn 70 đến 190px chồng nhẹ nhau như tay thợ nhấc đục. Nét đều như vector trông sai chất.
- **Ba họ nét:** nửa tối một họ song song theo chiều mặt; bóng đổ thêm họ chéo lệch 50 đến 70 độ; khe sâu nhất thêm họ thứ ba. Chỗ sáng để giấy trống.
- **Ánh sáng từ trên trái** cho cả deck; đường bao dày hơn ở phía xa nguồn sáng.
- **Quầng giấy** bao quanh chủ thể 12 đến 16px để nền kẻ dòng không chạm nét.
- **Bóng số:** vòng tròn giấy, số chữ nghiêng, đường dẫn mảnh kết thúc bằng chấm.
- **Vòng kính lúp:** vòng tròn nền kẻ dòng mang chủ thể; vòng nhỏ phóng to một chi tiết, nối bằng đường dẫn.
- **Quả cầu khắc** làm trạm, điểm nhấn; **chấm khắc (stipple)** cho vệt bay, bụi.

## Chữ ký chuyển động
- **Khắc ba lượt:** hình hiện đúng như thợ khắc làm: họ nét thứ nhất `fade`, họ chéo `fade` trễ, họ tối nhất trễ hơn, đường bao sau cùng (`data-stagger` giữa các nhóm). Người xem thấy hình đậm dần như được đục.
- **Màu nước đặt tay:** lớp hổ phách hiện một lần bằng `blur` mềm, lem nhẹ ra ngoài nét, trước khi mực phủ lên.
- **Phóng qua kính lúp:** đi sâu vào chi tiết bằng `data-transition="zoom"`; đường dẫn `draw` từ chi tiết tới vòng nhỏ, vòng nhỏ `zoom` mở ra.
- **Gọi tên bộ phận:** bóng số lần lượt `pop` nhỏ, đường dẫn `draw`, chú thích chữ nghiêng `fade`, theo thứ tự số.
- **Lật sang hình kế:** khung "HÌNH n" giữ nguyên (`data-morph`), chỉ số hình và chủ thể đổi, như lật trang trong cùng một tập.
- Nhịp: chậm, trang nghiêm, không nảy, không lặp; cả hình xong trong khoảng 2 giây.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** vòng kính lúp lớn bên phải mang chủ thể khắc đầy đủ ba họ nét, màu nước hổ phách lem phía sau, vòng nhỏ phóng một chi tiết ở góc dưới; tên deck chữ hoa nhỏ bên trái, dòng chú thích chữ nghiêng.
- **Giải phẫu một khái niệm:** chủ thể giữa slide, bóng số 1 đến 5 gọi tên từng phần, bảng kê khung đôi bên cạnh.
- **Quy trình:** năm quả cầu trên trục, mỗi quả khắc thêm một lượt (chỉ viền, một họ nét, nét chéo, nét tối, thêm màu nước): tiến trình hiện ngay trong độ đậm.
- **Kết:** dấu ép bản đồng và một dòng chữ nghiêng như chú thích cuối sách.

## Nên tránh
Tô mảng xám hay đen đặc, gradient, bóng đổ mờ, render 3D, ánh kim, glow; màu nước đục hay phủ lên chữ, quá một sắc nước mỗi slide; nét đều như vẽ máy; số đo bịa trong hình; sao chép một tờ minh họa có thật hay chữ ký người khắc.

## Họ hàng
`woodcut` (khắc gỗ: mảng đen lớn, nét dao thô, kịch tính; khắc đồng thì nét mảnh đan chéo, tinh và học thuật), `vintage-editorial` (báo ảnh kem với chữ lớn, dí dỏm; khắc đồng là hình nét đan chéo có khung in và bóng số), `blueprint` (bản vẽ kỹ thuật nét đều trên giấy xanh; khắc đồng nét phình thon trên giấy kem).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/engraving.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một tấm bản khắc đồng trên giấy kem, khung in có viền kép, ở giữa là một con ong mật nhìn từ trên, cánh xòe, râu và chân có đốt, thân đan nét ngang và chéo, hai cụm phấn hoa cam ở chân. Quanh nó là ba vòng tròn phóng to (mắt kép, móc cánh, giỏ phấn) nối bằng đường dẫn mảnh, một hình nhỏ đúng cỡ thật ở góc. Tiêu đề chữ in hoa lớn, tên khoa học in nghiêng bên dưới, nhãn hình đánh số. Con ong chiếm khoảng 60 % chiều cao khung.
- **Chất liệu và ánh sáng:** nền kem `#f1e8d2` có vân sợi tĩnh, khung nổi bằng hai đường viền và một bóng khe mảnh. Mực một màu nâu đen `#1c1510`. Độ đậm nhạt chỉ làm bằng mật độ nét: lớp nét song song cho nửa tối, lớp nét chéo cho bóng, không tô xám. Nét thắt thon hai đầu: mỗi nét là `path` dạng thoi (tự dựng đa giác, không dùng `stroke` đều). Một hướng sáng cố định phía trên bên trái, nét viền dày hơn ở phía khuất. Màu nước chỉ là lớp `multiply` mờ đặt dưới mực, tràn nhẹ ra ngoài nét.
- **Máy quay và khung dọc 9:16:** như kính lúp trên một tờ giấy, gần như tĩnh. Dọc 9:16 thì con ong ở giữa, các vòng phóng to xếp dọc ở dưới. Di máy rất nhẹ: đẩy vào dưới 2 %, hoặc tiến vào một vòng tròn cùng lúc nó bay ra lề.
- **Chuyển động:** thứ tự khắc là hoạt họa: nét viền, rồi nét song song quét qua từng phần, rồi nét chéo, rồi chỗ tối nhất. Nét chạy tốc độ đều bằng `stroke-dashoffset`, nhiều nét cùng lúc. Vòng tròn bay theo cung ease nhẹ, to dần khi tới lề. Màu nước nở từ một điểm bằng `clipPath` hình tròn lớn dần. Không mờ dần hay trượt kiểu giao diện.
- **Chữ trên hình:** tiêu đề Playfair Display SC (đủ dấu tiếng Việt), tên khoa học và chú thích Newsreader nghiêng. Chữ khắc hiện từng ký tự, không fade. Phụ đề là mảnh giấy ở đáy, chữ Newsreader.
- **Nước đi đặc trưng:**
  - Ba lượt khắc: khung, nét song song, nét chéo; hợp một vật được dựng dần.
  - Vòng phóng to: vẽ vòng, phình ra, bay ra lề kèm đường dẫn rồi khắc nhãn; hợp chi tiết không thấy bằng mắt.
  - Màu nước nở sau khi in; hợp nhấn một bộ phận.
  - Hình đúng cỡ thật ở góc; hợp so sánh kích thước.
- **Bẫy:** nét đều như bút bi thì mất chất khắc, phải thắt thon hai đầu; tô xám thay vì đan nét; đường dẫn chạy xuyên qua con ong thay vì chừa khoảng; tạo vòng phóng to ở bán kính nhỏ rồi scale lên thì nét vỡ, hãy vẽ lớn rồi thu vào.

Phỏng theo `styles/engraving/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

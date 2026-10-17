# Whiteboard (bảng trắng bút lông)

> Như người thuyết trình vừa nói vừa vẽ lên bảng: nét bút lông một mạch, hơi run, ba màu bút mỗi màu một nghĩa.

**Hợp:** giải thích khái niệm, quy trình, bài giảng đào tạo, workshop, onboarding, nội dung "vừa nói vừa vẽ".
**Không hợp:** ra mắt sản phẩm cao cấp, báo cáo tài chính trang trọng, sự kiện lễ hội.
**Cảm xúc:** thân thiện, dễ hiểu, nét tay, gần gũi.

## Hình dung
Cả deck là một tấm bảng trắng bóng: vết xước nhỏ, bóng mờ của bài giảng cũ chưa xóa sạch, vệt sáng cửa sổ trôi ngang. Mọi thứ người xem học được đều là nét bút lông. Bút và nam châm tự bay, không vẽ tay người.

## Bảng màu
```css
--bg: #F4F4EF;        /* bảng */
--ink: #23262c;       /* bút đen: vật, cấu trúc */
--blue: #2a5cb3;      /* bút xanh: tín hiệu, mũi tên, nối kết */
--orange: #d97757;    /* bút cam: điều quan trọng nhất, mỗi slide một chỗ */
--orange-d: #b5502b;  /* chữ cam đủ tương phản */
--muted: #4A505A;
```

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Playpen+Sans:wght@500;700;800&family=Patrick+Hand&display=swap" rel="stylesheet">
```
- Tiêu đề và thân: Playpen Sans (có tiếng Việt), 700 đến 800 cho tiêu đề.
- Chữ viết tay ngắn trong hình: Patrick Hand 32 đến 62px, một hai chữ ("tách!", "đây rồi").

## Bề mặt
Nền trắng ấm, vết xước rất mờ, vùng sáng như ánh cửa sổ ở góc trên trái, bóng mờ của nét cũ (đen 8%, nét đứt).

## Ngôn ngữ minh họa
- Một độ dày: nét chính 7px, nét phụ 5px; đầu nét tròn.
- **Nét tay:** đường hơi lệch 1 đến 3px; hộp là bốn nét rời vượt qua góc 4 đến 7px; vòng tròn vẽ quá điểm đầu, không khép kín.
- Mũi tên: thân cong một nét, đầu mở hai nét, màu xanh.
- Vòng khoanh cam quanh câu trả lời. Chấm vệt (đứt 1 rồi 20) cho đường đi.
- Hình đơn giản nhất mà vẫn mang ý: hộp, vòng, mũi tên, thước, nam châm. Không đổ bóng, không tả thực.
- **Mẹo:** vòng khoanh quanh chữ nên đo vị trí chữ thật sau khi font tải xong (xem hàm `around` trong `examples/02_ai-agent-xay-dung-whiteboard.html`), đừng đoán tọa độ, chữ xuống dòng là lệch.

## Chữ ký chuyển động
- **Nét được viết ra:** mọi hình hiện bằng `draw`, theo thứ tự người vẽ thật (hộp trước, mũi tên sau, khoanh cam cuối).
- **Chữ viết tay hiện bằng `wipe`** từ trái sang như đang viết.
- **Nam châm dập** (`drop` có nảy) ghim tờ giấy, thẻ lên bảng.
- **Khăn lau quét** qua để xóa trạng thái cũ (một dải trắng `wipe`), rồi vẽ trạng thái mới.
- **Bút lơ lửng** (`float`) ở góc, như vừa đặt xuống.
- Nhịp: vừa phải, như đang giảng.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** tên bài viết tay, một vòng khoanh cam quanh từ khóa, nam châm ghim tờ đề cương.
- **Quy trình:** các hộp nối bằng mũi tên xanh, vẽ lần lượt theo cú bấm.
- **Trước và sau:** vẽ trạng thái cũ, khăn lau quét qua, vẽ trạng thái mới.
- **Kết:** một câu được khoanh cam, dấu tích lớn.

## Nên tránh
Nét thẳng tắp như máy, gradient, bóng đổ, icon phẳng, quá ba màu bút, vẽ bàn tay người.

## Họ hàng
`notebook-tabs` (giấy kẻ, tab màu), `crayon-book` (sáp màu trẻ em), `scatterbrain` (bừa có chủ ý, brainstorm).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/whiteboard.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một tấm bảng trắng bóng, khung quay chỉ thấy một vùng của nó. Không có người, không có tay. Nhân vật là hình vẽ nét đơn: hai chiếc đồng hồ tròn (đen và cam) đặt cạnh nhau, dưới là hai thước đo có vạch chia, nhãn viết tay dưới mỗi hình. Hai cây bút lông nổi ở mép phải khung, thân trắng, dải màu và nắp đúng màu mực, đổ bóng xuống bảng. Hình chính chiếm khoảng 1/3 chiều cao khung; còn lại là mặt bảng trống.
- **Chất liệu và ánh sáng:** nền SVG gradient trắng ấm, thêm vài dấu vết cũ (chữ, vòng tròn mờ 5 đến 10 % xám hoặc xanh nhạt) và một vệt sáng chéo trắng 10 đến 16 % trôi chậm hơn bảng. Nét mực là `path` bo đầu, `stroke-linecap: round`, độ rộng 6 đến 11 px, hai màu bút (đen than, cam đất), `mix-blend-mode: multiply` để chỗ chồng nét đậm hơn. Đầu và cuối nét hơi chồng lên nhau, vòng tròn không khép kín tuyệt đối. Bút là nhóm SVG tĩnh, bóng là ellipse mờ tĩnh. Filter chỉ để tĩnh.
- **Máy quay và khung dọc 9:16:** cận trung, nhìn thẳng vào bảng. Dọc 9:16 thì xếp hai đồng hồ chồng trên dưới, thước đo nằm dưới. Di máy bằng scale và translate cả lớp bảng, trượt theo đường bút đang vẽ; không cắt cảnh, chuyển vùng bằng một cú quét nhanh.
- **Chuyển động:** nét vẽ bằng `stroke-dashoffset`, ease chậm nhanh chậm, mỗi nét 0,3 đến 0,8 giây, xong đúng lúc lời đọc nói tới từ đó. Bút trượt tới đầu nét tiếp theo, bóng to ra khi bút nhấc. Vạch chia thước hiện từng vạch theo nhịp. Hai bút vẽ song song khi so sánh hai đại lượng.
- **Chữ trên hình:** nhãn viết tay bằng nét, dùng Playpen Sans (đủ dấu tiếng Việt), đúng màu mực của hình đi kèm, viết bằng `clipPath` quét trái sang phải. Phụ đề là nhãn tròn trắng ngà ở đáy, Patrick Hand.
- **Nước đi đặc trưng:**
  - Vẽ công thức hoặc nhãn từng nét đúng lúc nói; hợp giải thích khái niệm.
  - Hai bút cùng vẽ hai đồng hồ hoặc hai thước để so sánh; hợp trước và sau, hai kế hoạch.
  - Bút dẫn máy quay theo một đường kẻ sang vùng mới; hợp quy trình, chuỗi bước.
  - Cục tẩy quét ngược để xóa nét; hợp hoàn tác, đảo ngược.
  - Vệt mờ của bài cũ hiện rõ lại khi cần; hợp thay thế lý thuyết, gọi lại ý trước.
- **Bẫy:** nét gạch rời quá ngắn thì cho thời lượng tối thiểu, đừng để cả đường nét đứt kéo dài nhiều giây; mực đều đặn như vector thì mất chất bảng, phải có rung tay và chồng nét; vẽ chữ bằng khối hiện mờ thay vì nét thì hỏng cảm giác viết tay; nhãn bị cắt dở khi máy đẩy vào.

Phỏng theo `styles/whiteboard/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

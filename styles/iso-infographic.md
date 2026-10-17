# Infographic isometric (sa bàn hệ thống)

> Cả hệ thống đặt trên một sa bàn nhìn nghiêng 30 độ: khối phẳng ba tông không viền, luồng nét đứt có mũi tên, ghim nhãn như bản đồ chỉ dẫn.

**Hợp:** giải thích hệ thống, quy trình, chuỗi cung ứng, kiến trúc phần mềm cho người không chuyên, báo cáo năm, logistics.
**Không hợp:** cảm xúc, văn hóa truyền thống, thời trang, nội dung cần chất thủ công.
**Cảm xúc:** rõ ràng, hệ thống, tươi sáng, hiện đại.

## Hình dung
Người xem như đang cúi nhìn một mô hình thu nhỏ trên bàn: tấm nền nổi có lớp đất nâu ở mép, tòa tháp xanh có cửa sổ, vài khối màu đứng thành trạm, dòng dữ liệu chạy giữa chúng như xe trên đường. Góc nhìn không bao giờ đổi: mọi thứ chỉ trượt, lớn lên, nhỏ lại. Cảm giác: "à, hóa ra nó chạy như vậy".

## Bảng màu
Mỗi màu có ba tông: mặt trên sáng (`-t`), mặt trái vừa (`-l`), mặt phải tối (`-r`).
```css
--ground: #F4F2EC; --paper: #FFFFFF; --ink: #22263A;  /* nền, thẻ trạm, mực đồ nghề */
--plate-side: #D3D8E2; --plate-line: #A3ABBB;          /* cạnh và viền đứt của tấm trạm */
--blue-t: #8DBCE8; --blue-l: #4A88C8; --blue-r: #2F619A;   /* dữ liệu, nước, hệ thống */
--coral-t: #F59A86; --coral-l: #E0644F; --coral-r: #B0473A; /* chủ thể đang kể */
--amber-t: #F7CF6E; --amber-l: #E5A93A; --amber-r: #B8842A; /* nhóm phụ, bước giữa */
--mint-t: #9EDBB4; --mint-l: #55B37F; --mint-r: #3C8A60;    /* kết quả, hoàn tất */
--slate-t: #E3E7EE; --slate-l: #BCC4D2; --slate-r: #939CAF; /* trung tính: máy, giấy */
--muted: #565C72; --accent: #2B67AD;
```
Màu là chú giải bản đồ: một màu một nghĩa, không dùng một màu cho hai nghĩa. Dữ liệu luôn xanh dương; san hô chỉ dành cho chủ thể của slide. Mực chỉ dùng cho đồ nghề (luồng, ghim, đường kích thước).

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
```
- Tiêu đề: Lexend 600, IN HOA, giãn 0,04em, như biển chỉ dẫn.
- Thân, nhãn ghim, tên trạm: Be Vietnam Pro 400 đến 600.
- Số lớn: Lexend 600 đến 700.
Cả hai font có tiếng Việt (đã kiểm ngày 16/10/2026).

## Bề mặt
Nền kem nhạt có lưới isometric mờ (đường chéo 30 độ, chấm ở mắt lưới, ô 69,282 x 40px). Thẻ trạm trắng bo 14px, viền đứt xám, cạnh dày lệch phải dưới như tấm bìa cứng.
```css
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='69.282' height='40'%3E%3Cpath d='M0 0L69.282 40M0 40L69.282 0' stroke='%23C9CFDA' stroke-opacity='.55' fill='none'/%3E%3C/svg%3E");
background-size: 69.282px 40px;
```

## Ngôn ngữ minh họa
- **Phép chiếu cố định:** `x = ox + 0.866·k·(u − v)`, `y = oy + 0.5·k·(u + v) − k·z`. Vẽ xa trước gần sau. Không phối cảnh, không xoay trục.
- **Khối hộp ba đa giác** (trái, phải, trên), không viền, không gradient, không bóng mềm.
- **Tấm nền nổi:** mặt cỏ nhạt, mép là 3 đến 4 dải đất nâu phẳng, có thể có một ao nước xanh.
- **Luồng dữ liệu:** nét đứt 4px (14/10) đi dọc trục u hoặc v, mũi tên là tam giác ép dẹt theo mặt đất.
- **Gói dữ liệu Isotype:** khối xanh nhỏ cạnh 20 đến 24px; muốn nói số lượng thì lặp đúng số khối.
- **Ghim nhãn:** vòng tròn ở tâm mặt trên của vật, cần đứng, gạch ngang, nhãn HTML là thẻ giấy viền mực.
- **Vòng theo dõi:** nửa trước của elip quanh chân vật. **Bóng ma:** viền lục giác nét đứt nơi vật vừa rời đi.

## Chữ ký chuyển động
- **Đường trước, khối sau:** luồng nét đứt hiện trước (`wipe` theo hướng luồng), rồi khối mới `drop` xuống đúng ô, không có gì di chuyển khi chưa có đường.
- **Dòng kiến chạy:** gói dữ liệu đi dọc luồng bằng `<animateMotion>`, nhịp đều, như băng chuyền; đây là thứ lặp duy nhất của slide.
- **Khối trượt trên trục:** giữa hai slide, cùng một khối `data-morph` trượt sang trạm khác và đổi chiều cao, không bao giờ xoay.
- **Tòa tháp mọc tầng:** cột tiến độ dâng bằng `rise-wipe`, cao dần qua từng bước.
- **Ghim cắm xuống:** vòng ghim `pop`, cần và gạch ngang `draw`, nhãn `fade` sau cùng; bóng ma để lại chỗ cũ.
- Nhịp: gọn, máy móc vui vẻ, nảy rất nhẹ khi khối đáp.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** sa bàn bên phải, tháp xanh và ba khối màu đứng trên tấm nền; luồng nối thành vòng, gói dữ liệu bắt đầu chạy; một vòng theo dõi quanh khối san hô.
- **Kiến trúc hệ thống:** các trạm zíc zắc dọc trục, mỗi trạm mang một vật tượng trưng (chồng tấm mỏng là tệp, cụm khối là thành phần), luồng đi đúng trục.
- **Quy trình:** ba đến năm cột cao dần, luồng nhảy cong từ mặt cột này sang cột sau, chủ thể san hô nhảy theo.
- **So sánh trước và sau:** hai tấm trạm cạnh nhau cùng góc nhìn, chỉ khác số khối Isotype, đếm được bằng mắt.

## Nên tránh
Phối cảnh hay nghiêng phép chiếu, khối xoay lệch trục, low poly có ánh sáng, bóng đổ mềm, viền quanh khối đặc; tô san hô cho thứ không phải chủ thể; biểu đồ 3D có trục; đếm Isotype sai số; chữ vẽ trong SVG.

## Họ hàng
`blueprint` (bản vẽ kỹ thuật nét trắng trên giấy xanh, chính xác và cổ điển; iso thì màu tươi, dễ hiểu cho người ngoài ngành), `clay-3d` (khối đất sét bo tròn có ánh sáng, vui cho trẻ em; iso phẳng ba tông, không ánh sáng), `bento-light` (thẻ phẳng chính diện, tối giản; iso có chiều sâu sa bàn).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/iso-infographic.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một sa bàn isometric thật: bến cảng với tàu container chất nhiều thùng nhiều màu, hai cần cẩu giàn vàng, xe tải xanh nhỏ, dãy nhà thấp màu pastel và cây tròn, mặt nước xanh có vài gợn. Mép sa bàn lộ mặt cắt đất nâu ở góc dưới trái. Không có người, vật chính là tàu và cần cẩu, chiếm hơn 1/3 chiều cao khung. Một đường đứt nét mực chạy xuyên cảnh như tuyến di chuyển.
- **Chất liệu và ánh sáng:** không có ánh sáng điện ảnh, chỉ có ba tông cố định cho mỗi khối: mặt trên sáng, mặt trái vừa, mặt phải tối (đa polygon SVG, không viền). Chiếu isometric 30 độ: `sx = (x - y)·cos30°·k`, `sy = ((x + y)/2 - z)·k`, sắp theo độ sâu x + y + z. Tông tối pha hơi lạnh. Một màu một nghĩa như chú giải. Mực mảnh 2 px chỉ cho nét hạ tầng: đường dẫn, ghim, đường đứt.
- **Máy quay và khung dọc 9:16:** góc isometric cố định, không xoay, không phối cảnh; máy chỉ pan và zoom (scale và translate cả nhóm, zoom nội suy theo log). Cỡ từ toàn cảnh tới cận một trạm. Khung dọc: xếp sa bàn chéo từ trên xuống, nước ở trên, đất và mặt cắt ở dưới; nhãn ghim hướng lên hoặc xuống.
- **Chuyển động:** không gì chuyển động mà không có đường dẫn đi trước: đường tuyến vẽ trước, ghim mọc trước khi khung phụ mở. Khối đến bằng chuyển động chứ không bằng alpha. Hạ cánh có squash khoảng 18% và nảy nhẹ. Xe đi theo polyline, quay theo hướng tiếp tuyến. Ease `power2.inOut`, `back.out` cho biểu tượng nảy lên.
- **Chữ trên hình:** tiêu đề Lexend IN HOA giãn rộng; nhãn ghim Be Vietnam Pro (chấm, đường dọc, đường ngang, chữ) có viền sáng quanh chữ; số lớn dựng bằng biểu tượng giống nhau (Isotype); phụ đề như nhãn bản đồ, thẻ sáng bo nhẹ có viền mực. Đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Cắt mở (cutaway): đường cắt vẽ, lớp vỏ trượt khỏi sa bàn, lộ ruột có vạch sọc (cấu tạo, bên trong hệ thống).
  - Số Isotype: biểu tượng giống nhau nảy lên từng cái, số đếm chạy cùng lúc (con số cần cảm nhận).
  - Tập trung và bối cảnh: mọi thứ xám đi, chỉ chủ thể giữ màu (một thứ giữa nhiều thứ).
  - Khung tròn trong khung: đường dẫn mọc thành ô tròn cận cảnh (chi tiết nhỏ).
  - Lùi xa theo log thành một infographic hoàn chỉnh (tổng quan cuối).
- **Bẫy:** semi-transparent trên khối đang chuyển động trông như ma (chỉ dùng chuyển động); sắp độ sâu sai ở vật ghép như cần cẩu trên tàu (vẽ thành một nhóm có thứ tự); tàu hoặc bánh xe chạm sai mặt thành tai nạn (chừa khe); lặp một màu cho hai nghĩa; thêm bóng mềm hoặc gradient phá chất phẳng ba tông.

Phỏng theo `styles/iso-infographic/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

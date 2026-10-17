# HD-2D (sprite pixel trong mô hình thu nhỏ có đèn)

> Nhân vật pixel phẳng đứng giữa một diorama về đêm: sương chàm, đèn lồng ấm, vầng sáng trên đá lát. Cái chuyển động mượt là ánh sáng, không phải nhân vật.

**Hợp:** trailer game, kể chuyện, giới thiệu thương hiệu, nội dung giả tưởng và hoài niệm, mở màn sự kiện có không khí.
**Không hợp:** số liệu dày, bảng biểu kỹ thuật, nội dung cần đọc nhanh nhiều chữ.
**Cảm xúc:** ấm áp, huyền ảo, ánh sáng, diorama.

## Hình dung
Người xem nhìn từ trên xuống và hơi xéo vào một sa bàn thu nhỏ: bầu trời chàm lúc chạng vạng có viền tối, hai dãy núi bậc thang, ngôi làng có cửa sổ sáng, cây thông, một cột đèn đường đổ vũng sáng ấm. Người lữ hành áo choàng đỏ san hô đứng như tấm bìa cắt. Mỗi slide đổi một màu sương, như máy quay lia sang góc khác của cùng một thế giới.

## Bảng màu
```css
--sky: #2b2a66;     /* sương nền, đổi theo slide */
--ink: #14102e;     /* tối nhất, không dùng đen thuần */
--fg: #F6ECD6;      /* chữ kem */
--muted: #D8CFB6;
--gold: #E8C27A;    /* kim loại duy nhất: khung giao diện, nhãn */
--card-bg: rgba(14,10,36,.82);  /* tấm giao diện tối trong mờ */
/* sương mỗi slide: #2b2a66 #1e2554 #4a2c66 #1d2f5c #322868 #2a3a5e #23204d #1f3355 #3a2148 #4a2f5e
   đá #4a3f78 sáng #5a4e90 tối #2b2554 khe #221d48
   đèn ấm #ffb347 lõi #fff3c4
   nhân vật chính: áo #e8553a, bóng áo #b13e2e, da #f2c9a0 */
```
Một tông lạnh lớn đối lập vài nguồn sáng ấm nhỏ. Mỗi hình có đúng một nguồn sáng dẫn mắt (tối đa hai). Màu san hô chỉ dành cho nhân vật chính.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant:wght@600;700&family=Cormorant+Garamond:wght@500;600;700&display=swap" rel="stylesheet">
```
- Tiêu đề: Cormorant 700, IN HOA, giãn 0,06em (nhãn trong hình giãn 0,2em), màu kem hoặc vàng. Có tiếng Việt (đã kiểm).
- Thân: Cormorant Garamond 500 đến 600. Có tiếng Việt. Nét serif mảnh, nên giữ cỡ chữ thân lớn và nền tấm tối đủ đặc.

## Bề mặt
Trời chạng vạng có quầng sáng chân trời và viền tối bốn góc, sương nhạt dần lên trên, bụi sáng và sao rải thưa. Đáy là phiến đá lát.
```css
background: radial-gradient(120% 90% at 50% 100%, transparent 50%, rgba(20,16,46,.7)),
            linear-gradient(to top, #4a3f78, var(--sky) 45%, #14102e);
```

## Ngôn ngữ minh họa
- **Hai mức độ nét:** sprite và đồ vật là ô pixel vuông (ô 4, 6 hoặc 8 đơn vị, `crispEdges`), vầng sáng, bóng và sương là tròn, elip trong suốt, mềm. Không trộn nét mềm vào sprite.
- **Vầng sáng** là các vòng tròn đồng tâm cùng màu ấm, độ mờ 0,07 đến 0,2, lõi đậm nhất; không dùng `filter`.
- **Bóng** là elip `#05030f` mờ 0,4, lệch ra xa nguồn sáng; **vũng sáng** là elip ấm chồng hai lớp trên mặt đất.
- Đế diorama là ba đa giác (mặt trên, mặt trái đậm, mặt phải đậm nhất), khe lát đá song song hai trục.
- Hình mẫu: đèn lồng giấy kem viền vàng lơ lửng, căn nhà pixel cửa sổ sáng, thông pixel, đèn đường, bảng kê viền vàng có viên thoi số, tia lấp lánh chữ thập, hạt sáng ba lớp.
- Nhân vật không cao hơn 1/8 khung hình.

## Chữ ký chuyển động
- **Thắp nguồn sáng:** cảnh hiện tối trước, rồi đèn bật: lõi `pop`, các vòng sáng nở ra từ trong ra ngoài (`zoom` + `data-stagger`), vũng sáng trên đất hiện sau cùng. Ánh sáng kể chuyện.
- **Lia máy qua các lớp:** núi xa, làng, phiến đá là lớp cố định xuyên deck (`data-scene`), chuyển slide thì mỗi lớp trượt một quãng khác nhau (xa ít, gần nhiều), tạo thị sai.
- **Sương đổi màu:** màu trời chuyển êm sang màu sương mới của slide (chuyển `--sky` có `transition` dài), không cắt.
- **Bụi và đom đóm bay:** vài hạt sáng `data-loop="float"`, đèn lồng giấy lơ lửng nghiêng nhẹ; tối đa hai thứ lặp mỗi slide.
- **Ngó vào chi tiết:** đi sâu vào một ý bằng `data-transition="zoom"`, như máy quay hạ xuống sa bàn.
- **Nhân vật bước chậm:** người lữ hành di chuyển theo bậc pixel, ngắn, rồi đứng yên; phần mượt để dành cho ánh sáng.
- Nhịp: chậm, êm, có khoảng lặng; mọi thứ như đang thở.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** trời chàm, làng xa lên đèn từng ô cửa, đèn đường bật sáng giữa khung, người lữ hành đứng trong vũng sáng; tên deck chữ vàng IN HOA.
- **Chương mới:** máy quay lia ngang qua núi, sương đổi từ chàm sang tím, một đèn lồng giấy lơ lửng mang tên chương.
- **Danh sách:** bảng kê viền vàng như menu nhập vai, mỗi hàng một viên thoi số sáng lên theo cú bấm.
- **Kết:** các đèn tắt dần, chỉ còn đèn lồng và lời cảm ơn, tia lấp lánh rơi quanh.

## Nên tránh
Bloom thật, `filter` mờ, gradient trên sprite; nhân vật dáng mềm cuốn tròn; nhiều hơn hai nguồn sáng ấm trong một hình; màu san hô trên vật khác; cảnh ban ngày không đèn; tên, nhân vật, hoa văn khung của game HD-2D có thật; số liệu bịa; câu dài trong hình.

## Họ hàng
`pixel-rpg` (cùng sprite pixel nhưng phẳng, tươi, có hộp thoại và thanh HP, nhịp giật kiểu 16-bit), `den-long-giay` (cũng đêm và đèn ấm, nhưng là bìa cắt, không có pixel), `stained-glass` (huyền ảo bằng ánh sáng xuyên kính màu, trang nghiêm hơn).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/hd-2d.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một sa bàn đêm nhìn từ trên cao xéo: đỉnh hải đăng với mái chóp tối, buồng kính sáng vàng, lan can sắt vòng quanh, nền gạch pixel, biển chàm tối và mây bậc thang ở xa. Một nhân vật pixel nhỏ (áo choàng đỏ, tay cầm đèn) đứng trong buồng sáng, cao khoảng 1/8 khung, phẳng như bìa cắt. Nhân vật phải có mặt trong cảnh.
- **Chất liệu và ánh sáng:** sprite và gạch vẽ bằng ô vuông `crispEdges` trong SVG hoặc Canvas 2D; đế, mái, lan can là đa giác phẳng tối. Nguồn sáng là cụm hình chữ nhật vàng cam xếp lớp, quanh nó là các vòng tròn đồng tâm mờ dần, thêm chùm sáng hình thang quét ra mặt biển. Lan can đổ bóng chéo dài lên nền gạch (đa giác `#05030f` mờ 0,4). Vignette bằng radial-gradient. Mờ nét trên và dưới khung là lớp gradient chồng, không dùng `filter` động.
- **Máy quay và khung dọc 9:16:** nhìn xuống từ cao, góc xéo khoảng 3/4, không bao giờ ngang mắt. Cỡ trung, dải nét ở giữa. Đi máy bằng scale và translate các lớp: trời và biển trượt ít, đế và lan can trượt nhiều. Khung dọc: xếp chồng đỉnh tháp ở giữa, trời trên, biển dưới.
- **Chuyển động:** sprite bước nấc (đổi hai khung, 6 đến 10 fps); ánh sáng, chùm tia, bụi và máy quay mượt. Đèn thở: opacity vầng sáng dao động tổng vài sine, quanh ±20%. Ease `sine.inOut` hoặc `power1.inOut`, chậm.
- **Chữ trên hình:** thẻ chương chữ Cormorant IN HOA giãn rộng màu vàng trên tấm tối; lời thoại trong hộp tối viền vàng mảnh, gõ chữ dần, kèm con trỏ nhấp nháy; phụ đề serif nghiêng kem. Đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Đèn bật: cảnh tối rồi lõi sáng nở vòng ra ngoài, bóng lan can quét qua nền (mở màn, khởi động hệ thống).
  - Đèn cầm tay như đồng hồ cảm xúc: sáng, lụi, gần tắt, bật lại (hành trình dài, kiên trì).
  - Pull-back từ nhân vật lên toàn bộ sa bàn, dải nét chuyển từ người sang công trình (hệ quả lan rộng).
  - Đèn bật lần lượt từng ô trên bản đồ (người dùng gia nhập, làng có điện).
- **Bẫy:** dither hoặc ô vuông quá dày thành caro; vầng sáng làm cháy sprite cầm đèn (dịch nguồn sáng ra phía trước một chút); cảnh tối quá không đọc được (nâng tông trung ở mọi chỗ trừ nhịp phải tối); quên bóng đổ nên sprite trôi khỏi nền; làm mờ nét bằng `filter` động gây giật.

Phỏng theo `styles/hd-2d/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

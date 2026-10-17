# Từ điển động từ: câu nói gì, hình làm nấy

Chuyển động có nghĩa khi nó làm đúng **động từ** của câu đang đọc. Nghe câu, tìm động từ, tra bảng, rồi biến tấu theo chữ ký chuyển động của thẻ style. Bảng là gợi ý, không phải luật: nghĩ ra cách hay hơn thì dùng.

Mọi mốc thời gian lấy bằng `A("key")` (neo theo từ khóa trong lời đọc). Plugin GSAP đã nạp sẵn: SplitText, DrawSVGPlugin, MotionPathPlugin, MorphSVGPlugin, ScrambleTextPlugin, CustomEase.

## 1. Vật xuất hiện

| Động từ trong câu | Cách làm bằng GSAP | Hợp với |
|---|---|---|
| xuất hiện, có | `from(el, {opacity:0, y:30})` ngắn, `power3.out` | vật phụ |
| mọc, tăng, đi lên | `from(bar, {scaleY:0, transformOrigin:'50% 100%'})` | cột, cây, tòa nhà |
| rơi vào chỗ, được giao | `from(el, {y:-400})` với `bounce.out` hoặc `back.out(2)` | thẻ, hộp, vật nặng |
| bật ra, nhấn mạnh | `from(el, {scale:0})` với `back.out(3)` | huy hiệu, con số |
| vẽ, phác, dựng | `from(path, {drawSVG:'0%'})`, nhiều nét thì `stagger` | sơ đồ, bản vẽ, nét tay |
| viết ra, gõ | SplitText `chars`, `from(chars, {opacity:0, stagger:.03})` | câu thoại, terminal |
| hiện rõ dần, lộ diện | `from(el, {opacity:0, scale:1.08})` chậm | tiêu đề lớn, câu chốt |
| giải mã, đổi nhãn | `to(el, {scrambleText:{text:'...'}})` | tên, mã, số liệu |
| đếm tới | `from(el, {textContent:0, snap:{textContent:1}})` | con số có nguồn |

## 2. Vật làm việc

| Động từ | Cách làm | Hợp với |
|---|---|---|
| gom lại, tổng hợp | các mảnh `to(..., {x:cx, y:cy, scale:.4})` về tâm, `stagger` | dữ liệu, ý kiến |
| tách ra, cắt | `SplitText` rồi tách khoảng cách `x`, một đường cắt `drawSVG` | câu, token, chi phí |
| lọc, chọn | vật rơi qua phễu, vật hỏng bật sang bên | lọc dữ liệu, kiểm hàng |
| kiểm tra, soi | vạch quét `x` qua vật, vật đổi màu khi vạch đi qua | kiểm thử, QA |
| chạy theo, đi tới | `motionPath:{path, align}` | dòng chảy, đơn hàng, xe |
| kết nối | đường `drawSVG` nối hai nút, chấm sáng chạy theo đường | mạng, API, đội nhóm |
| biến thành, trở thành | `morphSVG` từ hình này sang hình kia | trước và sau, ẩn dụ |
| sắp xếp lại | tính vị trí mới, `to(items, {x, y, stagger})` | lịch, thứ tự, ưu tiên |
| đóng dấu, chốt | `from(stamp, {scale:3, opacity:0})` nhanh, `power4.in`, rồi rung nhẹ | duyệt, kết luận |
| sụp, giảm, mất | `to(el, {scaleY:.2})` hoặc vỡ thành mảnh rơi | rủi ro, chi phí |

## 3. Sống suốt cảnh (sau khi hiện xong)

Không dùng `repeat:-1`: tính số lần lặp theo độ dài cảnh, ví dụ `repeat: Math.floor(dur / 1.2)`.

| Ý | Cách làm |
|---|---|
| đang chạy, vận hành | bánh răng `rotation`, băng chuyền dịch `x` |
| tín hiệu, sống | nhịp đập `scale` 1 đến 1.06, `yoyo` |
| lơ lửng, nhẹ | `y` lên xuống vài px, `sine.inOut` |
| dòng chảy | chấm sáng chạy theo `motionPath`, `stagger` |
| chờ, cảnh báo | nhấp nháy `opacity` theo `steps(1)` |

## 4. Giữa các cảnh

| Ý | Cách làm |
|---|---|
| cùng một vật đi tiếp | vật nằm cùng chỗ ở cuối cảnh trước và đầu cảnh sau, hoặc đặt trong lớp nền chung `_nen` |
| sang chương mới | màn che quét ngang bằng `clipPath: inset(...)` |
| đi sâu vào chi tiết | phóng to vào một vật rồi cắt sang cảnh chi tiết |
| cắt dứt khoát | không chuyển, cảnh sau bắt đầu ngay ở trạng thái mạnh |

## 5. Nhịp

- Hình chính vào xong trong khoảng 1 giây kể từ từ khóa.
- `back.out`, `bounce.out`, `elastic.out` cho vật có cá tính; `power3.inOut` cho máy quay lia; `steps(n)` cho style pixel, rối bóng, phim câm.
- Cuối cảnh để hình đọng lại khoảng 0,3 giây trước khi cắt.

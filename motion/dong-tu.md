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

## Kỹ thuật lớn: dùng với mọi style

Năm kỹ thuật này không thuộc style nào. Lời đọc có động từ đúng thì dùng, đổi màu và nét vẽ cho hợp style. Mọi đoạn code giả định đã có `tl` (một `gsap.timeline` paused) và `A("key")` trả về mốc giây. Mọi giá trị ngẫu nhiên phải đến từ hàm có hạt giống, cùng một khung hình luôn cho cùng một kết quả:

```js
const rnd = (i) => ((Math.sin(i * 12.9898) * 43758.5453) % 1 + 1) % 1;
```

### 1. Particles (hạt)

**Khi nào dùng:** lời đọc nói "lan ra", "tỏa ra", "bùng nổ", "tản", "hội tụ", "thu về".

**Cách làm:**
- Vẽ sẵn 30 đến 80 hình nhỏ (`circle`, `rect`) trong một nhóm. Không sinh hạt lúc chạy.
- Hướng, bán kính, độ trễ, kích cỡ của hạt thứ `i` đều tính từ `rnd(i)`, mỗi thuộc tính dùng một độ lệch khác (`i`, `i + 99`, `i + 7`) để không trùng nhau.
- Chỉ tween `x`, `y`, `scale`, `opacity`. Hội tụ thì đảo `fromTo`: bắt đầu ở vị trí xa, kết thúc ở 0.
- Hạt tắt dần ở cuối, không để hạt đứng yên chiếm hình.

```js
const t0 = A("lan-ra");
gsap.utils.toArray("#hat circle").forEach((d, i) => {
  const ang = rnd(i) * Math.PI * 2;
  const r = 80 + rnd(i + 99) * 320;
  const at = t0 + rnd(i + 3) * 0.2;
  tl.fromTo(d, { x: 0, y: 0, opacity: 0, scale: 0.4 },
    { x: Math.cos(ang) * r, y: Math.sin(ang) * r, opacity: 1, scale: 1,
      duration: 0.9 + rnd(i + 7) * 0.5, ease: "power3.out" }, at);
  tl.to(d, { opacity: 0, duration: 0.4, ease: "power1.in" }, at + 1.1);
});
```

### 2. Liquid morph (hình lỏng biến dạng)

**Khi nào dùng:** lời đọc nói "biến thành", "chuyển hóa", "hòa vào", "tách ra", "chảy sang".

**Cách làm:**
- Hai cách, chọn một hoặc dùng cả hai:
  - **Morph path:** vẽ các path blob (hoặc biểu tượng) có đường nét mềm, rồi `MorphSVGPlugin` đưa path này về path kia. Hai path nên có số điểm gần nhau để không bị xoắn.
  - **Goo:** bọc các hình tròn trong một nhóm có bộ lọc SVG `feGaussianBlur` rồi `feColorMatrix`. Bộ lọc này **tĩnh**, khai báo trong `defs` và không bao giờ tween. Chỉ tween `x`, `y`, `scale` của các hình con, chúng sẽ dính vào nhau rồi tách ra như giọt nước.
- Màu của blob tween bằng `fill`, cùng nhịp với morph.

```html
<filter id="goo"><feGaussianBlur in="SourceGraphic" stdDeviation="12" result="b"/>
  <feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9"/></filter>
<g id="giot" filter="url(#goo)"><circle id="g1" r="60"/><circle id="g2" r="60"/></g>
```

```js
const t0 = A("bien-thanh");
tl.to("#blob-a", { morphSVG: "#blob-b", fill: "#2f80ed", duration: 1.2, ease: "power2.inOut" }, t0);
tl.fromTo("#g2", { x: 260 }, { x: 0, duration: 0.9, ease: "power2.inOut" }, t0);
tl.to("#g2", { x: 200, scale: 0.6, duration: 0.8, ease: "power2.inOut" }, t0 + 1.4);
```

### 3. Kinetic type (chữ chuyển động là nhân vật chính)

**Khi nào dùng:** câu đọc ngắn, mạnh, là khẩu hiệu hoặc con số gây sốc: "chỉ một", "gấp ba", "dừng lại". Chữ là hình chính, không cần minh họa thêm.

**Cách làm:**
- Tách chữ bằng `SplitText` (`type: "chars,words"`). Mỗi từ khóa vào đúng mốc `A("key")` của từ đó, không vào cả câu một lượt.
- Từ nhấn: phóng to, đổi màu, hoặc tách khỏi dòng. Từ phụ: nhỏ và mờ.
- Đổi nghĩa bằng chuyển động: "tăng" thì chữ trượt lên, "giảm" thì chữ rơi xuống, "xáo trộn" thì dùng `ScrambleTextPlugin` rồi chốt đúng chữ.
- Chữ có dấu tiếng Việt: đặt `line-height` từ 1.2 trở lên và đừng cắt `clipPath` sát thân chữ, kẻo mất dấu.

```js
const s = new SplitText("#khau-hieu", { type: "chars,words" });
const t0 = A("khau-hieu");
tl.from(s.chars, { y: 120, rotation: (i) => (rnd(i) - 0.5) * 30, opacity: 0,
  duration: 0.5, ease: "back.out(1.7)", stagger: 0.03 }, t0);
tl.to(s.words[1], { scale: 1.35, color: "#ff5a36", duration: 0.35, ease: "power4.out" }, A("nhan"));
tl.to("#phu-de", { scrambleText: { text: "Chốt trong một ngày", chars: "01" }, duration: 0.8 }, A("phu-de"));
```

### 4. Split-flap (bảng lật chữ kiểu nhà ga)

**Khi nào dùng:** lời đọc nói "đổi", "cập nhật", "chuyển sang", "thay bằng", "đếm lên", nhất là với số, giờ, trạng thái.

**Cách làm:**
- Mỗi ký tự là một ô gồm **bốn lớp**: nửa trên tĩnh (hiện ký tự mới), nửa dưới tĩnh (hiện ký tự cũ), lá lật trên (ký tự cũ, `rotationX` từ 0 đến -90), lá lật dưới (ký tự mới, `rotationX` từ 90 về 0). Đặt `transform-origin` ở đường giữa ô, `backface-visibility: hidden`.
- Đổi ký tự theo **bước**: mỗi lần lật mất khoảng 0,12 giây, đi qua vài ký tự trung gian rồi dừng ở ký tự đích. Chuỗi trung gian lấy bằng `rnd`, không ngẫu nhiên thật. Không đổi chữ bằng `tl.call` (callback không tự hoàn tác khi HyperFrames tua ngược hoặc nhảy khung): dựng sẵn mỗi bước một lá có chữ riêng, chỉ bật tắt bằng `tl.set` opacity và lật bằng `rotationX`.
- Ô cần **đủ cao** cho chữ tiếng Việt có dấu (Ấ, Ệ, Ữ): chiều cao ô bằng khoảng 1,5 lần cỡ chữ, chữ căn giữa đường lật. Mỗi nửa chỉ cắt đúng một nửa ô, không cắt theo thân chữ.
- Các ô vào lệch nhau bằng `stagger` nhỏ để nghe như tiếng lách cách.

```js
const t0 = A("cap-nhat"), pool = "ABCDEGHKLMNPRSTVX0123456789";
gsap.utils.toArray(".flap").forEach((cell, c) => {
  const steps = [0, 1, 2].map(k => pool[Math.floor(rnd(c * 10 + k) * pool.length)]).concat(cell.dataset.to);
  steps.forEach((ch, k) => {
    const leaf = document.createElement("div");          // một lá cho mỗi bước, dựng lúc khởi tạo
    leaf.className = "la"; leaf.textContent = ch; cell.appendChild(leaf);
    const at = t0 + c * 0.05 + k * 0.12;
    tl.set(leaf, { opacity: 0 }, 0);                       // ẩn từ đầu
    tl.set(leaf, { opacity: 1 }, at);                      // hiện đúng bước của nó
    tl.fromTo(leaf, { rotationX: 90 }, { rotationX: 0, duration: 0.1, ease: "power1.out" }, at);
    if (k < steps.length - 1) tl.set(leaf, { opacity: 0 }, at + 0.12);  // nhường lá sau
  });
});
```

### 5. Physics (vật rơi, nảy, va chạm, con lắc)

**Khi nào dùng:** lời đọc nói "rơi", "va", "đổ", "nảy", "lắc", "đập vào", "sụp".

**Cách làm:**
- **Không mô phỏng theo khung.** Tính trước quỹ đạo bằng công thức rồi xếp thành các tween, hoặc dùng ease `bounce.out`, `elastic.out`, `CustomEase`.
- Rơi và nảy: một tween `y` với `bounce.out`. Muốn mỗi lần nảy thấp dần theo ý mình thì lặp trong vòng `for`, biên độ nhân 0,5 mỗi lần.
- Va chạm: tính mốc chạm từ công thức (khoảng cách chia vận tốc), đặt tween của vật bị đụng đúng mốc đó. Thêm `scaleY` ép dẹt ngắn và hạt bụi theo mục 1.
- Con lắc: chuỗi tween `rotation` dạng `sine.inOut`, biên độ giảm theo `exp(-k * n)`. Đặt `transformOrigin` ở điểm treo.
- Đổ hoặc sụp: mỗi mảnh rơi với độ trễ và góc xoay từ `rnd(i)`.

```js
const t0 = A("roi");
tl.fromTo("#qua-bong", { y: -500 }, { y: 0, duration: 1.1, ease: "bounce.out" }, t0);
tl.to("#qua-bong", { scaleY: 0.8, scaleX: 1.15, transformOrigin: "50% 100%", duration: 0.08, yoyo: true, repeat: 1 }, t0 + 0.4);
let amp = 40, at = A("lac");
for (let n = 0; n < 6; n++) {
  tl.to("#con-lac", { rotation: n % 2 ? -amp : amp, transformOrigin: "50% 0%", duration: 0.5, ease: "sine.inOut" }, at);
  amp *= 0.65; at += 0.5;
}
```

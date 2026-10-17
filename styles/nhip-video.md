# Dùng thẻ style cho video

86 thẻ style ở thư mục này dùng chung với SlideMotion (skill làm slide). Thẻ tả **gu**: hình dung, bảng màu, chữ, bề mặt, ngôn ngữ minh họa, chữ ký chuyển động, khoảnh khắc đáng nhớ. Giữ những thứ đó; bố cục và hình từng cảnh do người dựng tự nghĩ.

Thẻ viết cho slide nên có vài từ của runtime slide. Đổi sang video như sau:

| Thẻ nói | Trong video |
|---|---|
| `data-anim="wipe"`, `pop`, `drop`, `rise`, `draw`, `stamp`... | hiệu ứng vào cùng tên, viết bằng GSAP (tra `motion/dong-tu.md`) |
| `data-loop="blink"`, `pulse`, `float`, `spin` | chuyển động sống suốt cảnh, đếm số lần lặp theo độ dài cảnh |
| `data-step`, "bấm để hiện" | hiện đúng lúc từ khóa được đọc: neo `A("key")` |
| `data-stagger="80"` | `stagger: 0.08` |
| `data-transition="cut"`, `wipe`, `zoom` | cách cảnh vào và ra (`in`, `out` trong storyboard) |
| lớp cố định xuyên deck, `data-scene`, `data-morph` | lớp nền chung `compositions/_nen.html` hoặc vật xuyên suốt đặt cùng chỗ giữa hai cảnh |
| dòng `<link href="https://fonts.googleapis.com/...">` | chạy `tools/fonts.py <du-an> "Tên phông:400,700"` rồi dán `fonts.css` vào từng cảnh |
| "slide", "deck" | "cảnh", "video" |
| "chữ thân từ 28px" | khung 1080 x 1920 dọc: chữ chính từ 56px; khung 1920 x 1080 ngang: từ 40px |

## Khác biệt của video so với slide
- **Lời đọc dẫn hình.** Trên slide người xem tự đọc chữ; trong video họ nghe. Chữ trên hình chỉ để nhấn: một từ khóa lớn, một con số, một nhãn. Phụ đề đã có ở đáy khung.
- **Thời gian là của giọng.** Mỗi câu làm một thứ trên hình đổi trạng thái, đúng lúc từ khóa vang lên.
- **Không có cú bấm.** Thứ slide giấu chờ bấm, video cho hiện theo lời.
- **Khung dọc 9:16** (mặc định cho mạng xã hội): bố cục xếp theo chiều đứng, vật chính to và nằm giữa khung (điện thoại nhỏ, vật bé thì mất), chừa 14 phần trăm đáy cho phụ đề. Đừng để cả nửa khung trống không có lý do.

## Gợi ý chọn style theo nhu cầu
Bảng đầy đủ ở `INDEX.md`. Nhanh:

| Nhu cầu | Style hợp |
|---|---|
| Đào tạo, giải thích khái niệm | whiteboard, iso-infographic, midcentury-toon, blueprint, pixel-rpg |
| Số liệu, báo cáo, tin tức | dataviz, swiss-modern, broadside, game-show |
| Sản phẩm, công nghệ | dark-keynote, terminal-green, hologram-hud, neon-cyber, claude-ivory |
| Marketing, kể chuyện | paper-popup, risograph, crayon-book, mau-nuoc, one-line |
| Văn hóa Á Đông | thuy-mac, cat-giay-do, den-long-giay, roi-bong, ukiyoe, son-mai |
| Giải trí, hoài niệm | pixel-rpg, cel-anime-80s, rubber-hose, silent-film, 8-bit-orbit |

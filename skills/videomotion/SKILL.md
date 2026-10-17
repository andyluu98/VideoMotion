---
name: videomotion
description: Làm video tiếng Việt từ một yêu cầu, AI làm đạo diễn, không khung dựng sẵn: ý tưởng lớn, kịch bản, giọng VieNeu, phân cảnh theo lời, nhạc nền, dựng từng cảnh bằng agent Sonnet chạy song song (HyperFrames + GSAP), phụ đề, xuất MP4. Dùng khi người dùng gõ "/videomotion", "làm video", "video giải thích", "clip ngắn về X", "biến bài này thành video".
---

# VideoMotion: AI làm đạo diễn cho video

Khung dựng sẵn làm video nào cũng một dáng. VideoMotion đưa cho AI thứ nó thật sự cần: **gu** (86 thẻ style), **vốn từ chuyển động** (`motion/dong-tu.md`) và **một câu chuyện** do đạo diễn viết. Bạn (phiên chính) là đạo diễn; từng cảnh giao cho agent `vm-canh` (Sonnet mới nhất, effort medium) dựng song song.

```bash
VV="${CLAUDE_PLUGIN_ROOT}"
PY="$HOME/.motionfly/venv/Scripts/python.exe"; [ -x "$PY" ] || PY="$HOME/.motionfly/venv/bin/python"
export PYTHONUTF8=1 HF_HUB_DISABLE_PROGRESS_BARS=1
```

Lần đầu trong phiên chạy `python "$VV/tools/setup/doctor.py"`; chưa `SAN SANG` thì theo skill `vm-cai-dat`. Mỗi video là thư mục `videos/<slug>/` (slug không dấu, gạch nối).

## Luật không đổi
- **Số liệu, tên, ngày có nguồn.** Tin tức và số phải tra; ví dụ tự đặt thì nói "ví dụ". Ghi nguồn vào `brief.json`.
- **Tiếng Việt đủ dấu**, không gạch ngang dài, không emoji trong lời đọc.
- **Chữ là chữ HTML**, không vẽ chữ vào ảnh.

Mọi thứ khác là gợi ý nghề.

## 1. Brief
Ghi `brief.json`: `topic`, `audience`, `message` (một câu thông điệp lõi), `aspect` (mặc định `9:16`), `duration_s` (mặc định 60), `style`, `voice` (mặc định `Ngọc Huyền`), `music` (mặc định `synth:<mood>`), `sources`, `auto`. Chỉ hỏi thứ không đoán được, một câu một lần, phương án đề xuất đặt đầu. Người dùng nói "tự làm hết" thì `auto: true`.

## 2. Style
- Người dùng nêu tên thì dùng (tra `styles/INDEX.md` theo tên Việt hoặc slug).
- Chưa nêu thì gợi ý 3 style: một **hợp** chủ đề, một **khác nền**, một **bất ngờ** (bảng nhanh trong `styles/nhip-video.md`). Với `auto` thì tự chọn style hợp.
- Đọc kỹ `styles/<slug>.md` và `styles/nhip-video.md` (cách dùng thẻ slide cho video).

## 3. Ý tưởng lớn và kịch bản (cổng duyệt duy nhất)
**Ý tưởng lớn trước.** Một câu: video diễn ra trong *thế giới* nào, theo *trục* nào, với *nhân vật hoặc vật xuyên suốt* nào. Ví dụ: "Nhà máy là bàn cờ: mỗi lãng phí là một quân địch, AI là quân hậu đi một nước ăn ba quân." Câu chuyện làm video có hồn; style chỉ quyết định vẻ ngoài.

Viết `script.json`:
```json
{"title": "...", "voice": "Ngọc Huyền", "aspect": "9:16",
 "scenes": [{"id": "s1", "say": "Câu nói. | Câu sau khoảng nghỉ.", "intent": "ý cảnh"}], "pron": {}}
```
- 1 phút khoảng 150 đến 170 từ, 5 đến 9 cảnh. 3 giây đầu là câu móc.
- Mỗi cảnh 1 đến 3 câu, câu dưới 25 từ, văn nói. `|` tạo khoảng nghỉ 0,55 giây.
- Giọng VieNeu: câu có chủ ngữ tiếng Việt, tránh câu dưới 5 từ và câu mở đầu bằng tên tiếng Anh; số viết chữ số.

Gửi người dùng bảng ngắn: cảnh, lời đọc, hình ẩn dụ dự kiến. Chờ duyệt (bỏ qua nếu `auto`).

## 4. Giọng
Theo skill `vm-giong`. Xong khi có `voice.wav`, `words.json`.

## 5. Phân cảnh
Viết `storyboard.json` dựa trên mốc giọng thật trong `words.json`:
```json
{"title": "...", "aspect": "9:16", "style": "pixel-rpg",
 "idea": "câu ý tưởng lớn",
 "look": "giọng hình chung trong 2 đến 4 câu: vật xuyên suốt trông thế nào, nghĩa của màu nhấn, cách cảnh vào ra",
 "scenes": [{"id": "s1", "visual": "vật gì, đang làm gì, chuyển động theo động từ nào",
             "anchors": [{"id": "hook", "kw": "từ đúng như lời đọc", "nth": 1, "off": -0.1}],
             "in": "cách vào cảnh", "out": "cách sang cảnh sau"}]}
```
- `visual` tả **ý và vật**, không tả bố cục pixel: để agent tự thiết kế.
- **Trạng thái nối cảnh:** vật đi qua nhiều cảnh (thanh tiến độ, nhân vật, con số) thì ghi rõ trạng thái lúc vào và lúc ra trong `visual` của từng cảnh (ví dụ "HP vào 9/10, ra 3/10"). Các agent chạy song song không thấy cảnh của nhau.
- **Vật dùng chung** (nhân vật, khung giao diện, lớp nền) thì tả kích thước và vị trí cụ thể trong `look`, hoặc vẽ sẵn vào `compositions/_nen.html`.
- Mỗi câu có ít nhất một neo; `kw` viết đúng như trong `say`.
- Xen cảnh dày và cảnh thở; không để ba cảnh liền cùng một kiểu hình. Chọn 2 đến 3 khoảnh khắc "ồ" và tả kỹ hơn.
- Chạy `"$PY" "$VV/tools/timeline.py" <du-an>`; sửa đến khi không còn `KW miss`.

## 6. Nhạc nền
Theo skill `vm-nhac`: ra `mix.wav`.

## 7. Dựng, render, giao
Theo skill `vm-dung`: phông, màu, giao cảnh song song cho `vm-canh`, ghép, `hyperframes check`, render, ghép âm, phụ đề.

Báo cáo cuối: đường dẫn tuyệt đối MP4 và SRT, độ dài, style, giọng, nguồn nhạc, chỗ nào là ví dụ tự đặt, nguồn tư liệu.

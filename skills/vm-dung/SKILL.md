---
name: vm-dung
description: Dựng hình cho dự án VideoMotion đã có giọng và phân cảnh: tải phông của style, viết màu, giao từng cảnh cho agent vm-canh chạy song song, ghép, kiểm tra kỹ thuật, render, ghép âm thanh và phụ đề. Dùng ở bước 7 của /videomotion, hoặc khi người dùng nói "dựng lại cảnh", "render", "xuất video", "sửa hình cảnh X".
---

# Dựng và xuất video

Biến `VV`, `PY` như trong skill `videomotion`. HF là `npx -y hyperframes@0.8.145`. Đầu vào trong `<du-an>`: `storyboard.json`, `words.json`, `timeline.json`, `mix.wav`.

## 1. Chuẩn bị theo style
1. Phông của thẻ style (dòng Google Fonts trong thẻ):
   `"$PY" "$VV/tools/fonts.py" <du-an> "VT323" "Be Vietnam Pro:400,700"` ra `fonts/` và `fonts.css`.
2. `theme.css`: biến `:root` từ bảng màu thẻ: `--bg`, `--ink`, `--accent`, màu phụ, `--cap-bg`, `--cap-ink` (phụ đề đạt tương phản 4,5:1).
3. Style có nền liền suốt video (bản đồ, giấy, bảng, lưới): viết `compositions/_nen.html` (id `_nen`), các cảnh để nền trong suốt.
4. `"$PY" "$VV/tools/assemble.py" <du-an>`: tạo `index.html`, chép phông, tạo file chờ cho cảnh chưa có.
5. `"$PY" "$VV/tools/packets.py" <du-an>`: gói giao việc `checks/packets/<id>.md` cho từng cảnh.

## 2. Giao cảnh song song
Phát **tất cả trong cùng một tin nhắn**, mỗi cảnh một agent, agent type `videomotion:vm-canh` (đã khai `model: sonnet`, `effort: medium`: luôn là Sonnet mới nhất). Lời giao ngắn:

> Dựng cảnh `<id>`. Gói giao việc: `<du-an>/checks/packets/<id>.md`. Khuôn: `$VV/templates/scene.html`. Viết đúng file `<du-an>/compositions/<id>.html`.

Phiên chưa có agent `vm-canh` (cài skill không qua plugin, hoặc công cụ khác): dùng agent đa năng với `model: "sonnet"`, `effort: "medium"`, dặn đọc `$VV/agents/vm-canh.md` trước. Công cụ không có agent con thì tự dựng lần lượt theo file đó.

Dưới 3 cảnh thì tự dựng, khỏi giao.

## 3. Ghép và kiểm tra kỹ thuật
```bash
"$PY" "$VV/tools/assemble.py" <du-an>
cd <du-an> && npx -y hyperframes@0.8.145 check
```
Sửa đến khi `Check passed`, 0 error (lỗi ở file cảnh nào thì sửa file đó). Cảnh báo `timeline_track_too_dense` của phụ đề là bình thường. Không cần tờ duyệt hay người chấm; người dùng muốn xem trước thì `npx -y hyperframes@0.8.145 preview --background`.

## 4. Render và ghép âm
```bash
"$PY" "$VV/tools/assemble.py" <du-an> --no-audio
cd <du-an> && npx -y hyperframes@0.8.145 render --output renders/raw.mp4 > renders/render.log 2>&1
"$PY" "$VV/tools/audio/mix.py" srt <du-an>
"$PY" "$VV/tools/audio/mix.py" final <du-an> --video <du-an>/renders/raw.mp4 --name <slug>-<ddmmyyyy>
"$PY" "$VV/tools/assemble.py" <du-an>
```
Render chạy nền (khoảng 2 giây máy cho mỗi giây video). `--no-audio` là bắt buộc: `mix.py final` ghép `mix.wav` nguyên vẹn. Lệnh assemble cuối trả `index.html` về bản có tiếng để xem trước.

## 5. Kiểm một lần
`ffprobe renders/<ten>.mp4`: đúng kích thước, có luồng âm thanh, thời lượng bằng `total` trong `words.json`. Trích một khung giữa video bằng ffmpeg và nhìn qua. Giao `renders/<ten>.mp4` và `phude.srt`.

# Ghi nguồn (NOTICE)

VideoMotion tách từ [MotionFly](https://github.com/andyluu98/MotionFly) (cùng tác giả, MIT): giữ phần máy (giọng, mốc từng từ, nhạc, ghép, render, phụ đề), thay phần đạo diễn và style. Code và tài liệu chép từ dự án khác giữ nguyên giấy phép gốc; văn bản giấy phép nằm trong `vendor/licenses/`.

## Chép vào repo

| Thành phần | Nguồn | Giấy phép | Đã sửa gì |
|---|---|---|---|
| `tools/` (voice, timeline, assemble, packets, audio, music, setup) | MotionFly 0.4.0 (commit a97b643) | MIT | `assemble.py` nạp thêm plugin GSAP và phông của dự án; `packets.py` viết lại gói giao việc; thêm `tools/fonts.py`; bỏ `sheet.py` |
| `styles/*.md` (86 thẻ) | [SlideMotion](https://github.com/andyluu98/slidemotion) (cùng tác giả, MIT); nhiều thẻ phỏng theo [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) (MIT) và frontend-slides (MIT), ghi công ở cuối từng thẻ | MIT | Không sửa; thêm `styles/nhip-video.md` |
| `vendor/bestagentkits/fit-beat-grid.py` | [bestagentkits/motion-video-skill](https://github.com/bestagentkits/motion-video-skill) commit a73702b | MIT | Không sửa |
| `templates/fonts/BeVietnamPro-*.ttf`, `JetBrainsMono-Variable.ttf` | [google/fonts](https://github.com/google/fonts) | SIL OFL 1.1 | Đổi tên file JetBrains Mono |
| `reference/vn-short-video-tts/` | dự án cũ của chủ repo | của chủ repo | Không sửa |

## Phụ thuộc cài khi chạy (không chép vào repo)

| Phụ thuộc | Vai trò | Giấy phép |
|---|---|---|
| [HyperFrames](https://github.com/heygen-com/hyperframes) 0.8.145 (npx) | Dựng HTML thành MP4, kiểm tra | Apache-2.0 |
| [GSAP](https://gsap.com) 3.14.2 và plugin (CDN jsDelivr) | Chuyển động trong cảnh | GSAP Standard "no charge" license (https://gsap.com/standard-license), không thuộc MIT của repo |
| Phông Google Fonts (tải bằng `tools/fonts.py` vào từng dự án) | Chữ theo style | Giấy phép của từng phông, phần lớn SIL OFL 1.1 |
| [VieNeu-TTS](https://github.com/pnnbao97/VieNeu-TTS) (pip `vieneu`) | Giọng đọc tiếng Việt | Apache-2.0 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Mốc từng từ, chấm phát âm | MIT |
| numpy, scipy, soundfile, Pillow | Xử lý âm thanh, ảnh | BSD, MIT-CMU |
| ffmpeg (người dùng tự cài) | Đọc ghi âm thanh, video | LGPL/GPL tùy bản |

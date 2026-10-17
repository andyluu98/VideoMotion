"""Write one hand-off packet per scene for the vm-canh agents.

Reads timeline.json, storyboard.json (top-level "idea" and "look" written by the
director), theme.css and fonts.css. Writes checks/packets/<scene>.md with local word
times and A("key") anchors. The packet carries the story, not layout rules: each
agent designs its own scene.

Usage: python packets.py <project_dir>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]


def read(p: Path, fallback: str = "") -> str:
    return p.read_text(encoding="utf-8") if p.exists() else fallback


def main() -> None:
    p = Path(sys.argv[1]).resolve()
    tl = json.loads((p / "timeline.json").read_text(encoding="utf-8"))
    sb_all = json.loads((p / "storyboard.json").read_text(encoding="utf-8"))
    sb = {s["id"]: s for s in sb_all["scenes"]}
    theme = read(p / "theme.css", "(chưa có theme.css)")
    fonts = read(p / "fonts.css", "(chỉ có Be Vietnam Pro và JetBrains Mono của khuôn)")
    style = sb_all.get("style", "")
    has_bg = (p / "compositions" / "_nen.html").exists()
    order = [s["id"] for s in tl["scenes"]]
    out = p / "checks" / "packets"
    out.mkdir(parents=True, exist_ok=True)
    for i, s in enumerate(tl["scenes"]):
        sid, dur = s["id"], s["end"] - s["start"]
        words = "\n".join(f"  {w['start'] - s['start']:6.2f} - {w['end'] - s['start']:6.2f}  {w['w']}"
                          for w in tl["words"] if w["scene"] == sid)
        anchors = "\n".join(f'  A("{k}") = {v - s["start"]:.2f} s' for k, v in s["anchors"].items())
        prev = sb[order[i - 1]].get("visual", "") if i else "(không, đây là cảnh mở đầu)"
        nxt = sb[order[i + 1]].get("visual", "") if i + 1 < len(order) else "(không, cảnh cuối: để hình đọng lại ở cuối)"
        bg = ("Nền: cảnh để background trong suốt, đã có lớp nền chung `_nen` chạy suốt video."
              if has_bg else "Nền: tự vẽ nền theo style ngay trong cảnh.")
        text = f"""# Gói giao việc cảnh {sid}

File cần viết: {(p / 'compositions' / f'{sid}.html').as_posix()}
Khung {tl['width']}x{tl['height']}, cảnh dài {dur:.2f} s (thời gian cục bộ 0 đến {dur:.2f}).
Thẻ style: {(PLUGIN / 'styles' / f'{style}.md').as_posix()}
{bg}

## Câu chuyện của cả video
Ý tưởng lớn: {sb_all.get('idea', '')}
Giọng hình chung: {sb_all.get('look', '')}

## Cảnh này
Ý hình: {sb[sid].get('visual', '')}
Vào: {sb[sid].get('in', '')}   Ra: {sb[sid].get('out', '')}
Cảnh trước: {prev}
Cảnh sau: {nxt}

Lời đọc (thời gian cục bộ, giây):
{words}

Neo có sẵn:
{anchors}

## Màu (theme.css, dùng var(--...))
{theme}
## Phông (dán nguyên các dòng này vào <style> của cảnh)
{fonts}
"""
        (out / f"{sid}.md").write_text(text, encoding="utf-8")
    print(f"PACKETS {len(order)} -> {out}")


if __name__ == "__main__":
    main()

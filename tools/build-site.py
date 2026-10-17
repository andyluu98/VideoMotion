"""Build the style gallery data for the GitHub Pages site (docs/).

Reads styles/INDEX.md, copies one preview image per style into docs/assets/styles/,
writes docs/styles.js (window.STYLES = [...]). Preview sources, in order:
  1. a MotionFly style frame (same style family, video look), from a MotionFly checkout
  2. a SlideFly slide shot, already collected in a SlideMotion checkout

Usage: python tools/build-site.py <motionfly_dir> <slidemotion_dir>
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# MotionFly slug -> VideoMotion slug when the names differ
MF_ALIAS = {"ink-wash": "thuy-mac", "paper-lantern": "den-long-giay", "papercut-red": "cat-giay-do",
            "shadow-puppet": "roi-bong", "watercolor": "mau-nuoc", "pictogram-motion": "pictogram"}


def main() -> None:
    mf, sm = Path(sys.argv[1]), Path(sys.argv[2])
    mf_imgs = {MF_ALIAS.get(p.stem, p.stem): p for p in (mf / "site" / "media" / "styles").glob("*.jpg")}
    out_dir = ROOT / "docs" / "assets" / "styles"
    out_dir.mkdir(parents=True, exist_ok=True)
    styles, group = [], ""
    for line in (ROOT / "styles" / "INDEX.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"## (.+?) \(\d+\)", line)
        if m:
            group = m.group(1)
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not cells[1].startswith("`"):
            continue
        slug = cells[1].strip("`")
        own = ROOT / "site" / "media" / "mau" / f"{slug}.jpg"
        src, origin = (own, "VideoMotion") if own.exists() else (mf_imgs.get(slug), "MotionFly")
        if not src:
            src, origin = sm / "docs" / "assets" / "styles" / f"{slug}-1.jpg", "SlideFly"
        img = ""
        if src.exists():
            shutil.copy2(src, out_dir / f"{slug}.jpg")
            img = f"assets/styles/{slug}.jpg"
        styles.append({"name": cells[0], "slug": slug, "group": group, "mood": cells[2], "use": cells[3],
                       "fonts": cells[4], "img": img, "from": origin if img else ""})
    js = "window.STYLES=" + json.dumps(styles, ensure_ascii=False) + ";"
    (ROOT / "docs" / "styles.js").write_text(js, encoding="utf-8")
    n = {k: sum(s["from"] == k for s in styles) for k in ("VideoMotion", "MotionFly", "SlideFly")}
    print(f"{len(styles)} style: {n}, thiếu ảnh: "
          f"{[s['slug'] for s in styles if not s['img']]}")


if __name__ == "__main__":
    main()

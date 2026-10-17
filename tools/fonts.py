"""Download Google Fonts as local TTF files for one project, so scenes can use the
style's own typefaces while rendering offline.

Writes <project>/fonts/<Family>-<weight>.ttf and <project>/fonts.css (@font-face
lines). assemble.py inlines fonts.css into index.html; packets.py hands it to every
scene agent, who pastes it into the scene's <style> (HyperFrames lint wants each
scene to declare its fonts).

Usage: python fonts.py <project_dir> "VT323" "Be Vietnam Pro:400,700"
"""

from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/4.0"  # an old user agent makes Google Fonts answer with plain TTF files


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def css_for(family: str, weights: list[str]) -> str:
    base = "https://fonts.googleapis.com/css2?family=" + urllib.parse.quote_plus(family)
    if weights:
        try:
            return fetch(base + ":wght@" + ";".join(weights)).decode()
        except Exception:
            pass  # family has no such weight axis: fall back to its default face
    return fetch(base).decode()


def main() -> None:
    p = Path(sys.argv[1]).resolve()
    out = p / "fonts"
    out.mkdir(parents=True, exist_ok=True)
    faces = []
    for spec in sys.argv[2:]:
        family, _, w = spec.partition(":")
        weights = [x.strip() for x in w.split(",") if x.strip()]
        for block in re.findall(r"@font-face\s*{[^}]*}", css_for(family.strip(), weights)):
            weight = (re.search(r"font-weight:\s*(\d+)", block) or [None, "400"])[1]
            style = (re.search(r"font-style:\s*(\w+)", block) or [None, "normal"])[1]
            url = re.search(r"url\((https://[^)]+)\)", block)[1]
            name = f"{family.strip().replace(' ', '')}-{weight}{'i' if style == 'italic' else ''}.ttf"
            if not (out / name).exists():
                (out / name).write_bytes(fetch(url))
            faces.append(f'@font-face {{ font-family: "{family.strip()}"; src: url("fonts/{name}"); '
                         f'font-weight: {weight}; font-style: {style}; }}')
            print(f"FONT {family.strip()} {weight} -> fonts/{name}")
    css = p / "fonts.css"
    old = css.read_text(encoding="utf-8").splitlines() if css.exists() else []
    css.write_text("\n".join(dict.fromkeys(old + faces)) + "\n", encoding="utf-8")
    print(f"FONTS {len(faces)} -> {css}")


if __name__ == "__main__":
    main()

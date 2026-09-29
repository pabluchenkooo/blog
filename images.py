#!/usr/bin/env python3
"""
Converts Obsidian image embeds in content/ into Hugo-friendly links.

  ![[photo.jpeg]]          -> ![photo.jpeg](/images/photo.jpeg)
  ![alt](some/photo.jpeg)  -> ![alt](/images/photo.jpeg)

Images are looked up next to the note, then in static/images/, then anywhere
in the repo, and copied into static/images/ if they aren't there yet.

Runs in GitHub Actions before `hugo`, so the notes in git keep their Obsidian
syntax. Running it locally rewrites your notes in place (fine, just noisy).

Usage:
    python3 images.py
"""

import re
import shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
STATIC_IMAGES = ROOT / "static" / "images"
IMAGES_URL = "/images"
SKIP_DIRS = {".git", ".obsidian", "public", "_vendor", "resources"}

IMAGE_EXT = r"\.(?:png|jpg|jpeg|webp|gif|svg)"

# Matches ![[any-image.png]] and ![[any-image.png|300]]
WIKI_EMBED = re.compile(r'!\[\[([^\]|]+' + IMAGE_EXT + r')(?:\|[^\]]*)?\]\]', re.IGNORECASE)
# Matches ![alt](any-image.png) — skips already-converted URLs (starting with / or http)
MD_EMBED = re.compile(r'!\[([^\]]*)\]\((?!(?:/|https?://))([^)]+' + IMAGE_EXT + r')\)', re.IGNORECASE)


def find_image_file(filename, md_file):
    """Search next to the note, then static/images/, then the whole repo."""
    for d in [md_file.parent, STATIC_IMAGES]:
        candidate = d / filename
        if candidate.exists():
            return candidate
    for candidate in ROOT.rglob(filename):
        if not SKIP_DIRS.intersection(candidate.relative_to(ROOT).parts):
            return candidate
    return None


def copy_image(src, stats):
    """Make sure the image is in static/images/ and return its Hugo URL."""
    STATIC_IMAGES.mkdir(parents=True, exist_ok=True)
    dest = STATIC_IMAGES / src.name
    if not dest.exists():
        shutil.copy2(src, dest)
        print(f"    copied  : {src.relative_to(ROOT)}")
        stats["copied"] += 1
    return f"{IMAGES_URL}/{quote(src.name)}"


def process_file(md_file, stats):
    text = md_file.read_text(encoding="utf-8")
    original = text

    def replace(m, alt, path):
        filename = Path(path.replace("%20", " ")).name
        src = find_image_file(filename, md_file)
        if src:
            return f"![{alt}]({copy_image(src, stats)})"
        print(f"    WARNING : image not found — {filename} (in {md_file.relative_to(ROOT)})")
        stats["warnings"] += 1
        return m.group(0)

    text = WIKI_EMBED.sub(lambda m: replace(m, Path(m.group(1)).name, m.group(1)), text)
    text = MD_EMBED.sub(lambda m: replace(m, m.group(1), m.group(2)), text)

    if text != original:
        md_file.write_text(text, encoding="utf-8")
        print(f"    updated : {md_file.relative_to(ROOT)}")
        stats["files_updated"] += 1


def main():
    md_files = list(CONTENT.rglob("*.md"))
    stats = {"copied": 0, "warnings": 0, "files_updated": 0}

    print(f"Scanning {len(md_files)} markdown file(s) in content/\n")
    for md_file in md_files:
        process_file(md_file, stats)

    print(f"\n  files updated : {stats['files_updated']}")
    print(f"  images copied : {stats['copied']}")
    print(f"  warnings      : {stats['warnings']}")


if __name__ == "__main__":
    main()

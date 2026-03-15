#!/usr/bin/env python3
"""
Finds image references in Obsidian markdown posts, copies the images
to Hugo's static/images/, and rewrites the links with proper %20-encoded URLs.

Usage:
    python images.py
"""

import re
import shutil
from pathlib import Path
from urllib.parse import quote

OBSIDIAN_POSTS = Path("/Users/pablo/Documents/Obsidian Vault/blog/content/posts")
HUGO_STATIC_IMAGES = Path("/Users/pablo/pablo/pabloblog/static/images")
HUGO_IMAGES_URL = "/images"

IMAGE_EXT = r"\.(?:png|jpg|jpeg|webp|gif|svg)"

# Matches ![[any-image.png]]
WIKI_EMBED = re.compile(r'!\[\[([^\]]+' + IMAGE_EXT + r')\]\]', re.IGNORECASE)
# Matches ![alt](any-image.png) — skips already-converted URLs (starting with / or http)
MD_EMBED = re.compile(r'!\[([^\]]*)\]\((?!(?:/|https?://))([^)]+' + IMAGE_EXT + r')\)', re.IGNORECASE)


def find_image_file(filename, md_file):
    """Search next to the note, then walk up to vault root."""
    for d in [md_file.parent] + list(md_file.parents):
        candidate = d / filename
        if candidate.exists():
            return candidate
    return None


def copy_image(src, stats):
    """Copy image to static/images/ and return its Hugo URL."""
    HUGO_STATIC_IMAGES.mkdir(parents=True, exist_ok=True)
    dest = HUGO_STATIC_IMAGES / src.name
    if not dest.exists():
        shutil.copy2(src, dest)
        print(f"    copied  : {src.name}")
        stats["copied"] += 1
    else:
        print(f"    exists  : {src.name} (skipped)")
        stats["skipped"] += 1
    return f"{HUGO_IMAGES_URL}/{quote(src.name)}"


def process_file(md_file, stats):
    text = md_file.read_text(encoding="utf-8")
    original = text

    def replace_wiki(m):
        filename = Path(m.group(1)).name
        src = find_image_file(filename, md_file)
        if src:
            return f"![{filename}]({copy_image(src, stats)})"
        print(f"    WARNING : image not found — {filename}")
        stats["warnings"] += 1
        return m.group(0)

    def replace_md(m):
        alt, filename = m.group(1), Path(m.group(2)).name
        src = find_image_file(filename, md_file)
        if src:
            return f"![{alt}]({copy_image(src, stats)})"
        print(f"    WARNING : image not found — {filename}")
        stats["warnings"] += 1
        return m.group(0)

    text = WIKI_EMBED.sub(replace_wiki, text)
    text = MD_EMBED.sub(replace_md, text)

    if text != original:
        md_file.write_text(text, encoding="utf-8")
        print(f"    updated : {md_file.relative_to(OBSIDIAN_POSTS)}")
        stats["files_updated"] += 1


def main():
    md_files = list(OBSIDIAN_POSTS.rglob("*.md"))
    stats = {"copied": 0, "skipped": 0, "warnings": 0, "files_updated": 0}

    print(f"Scanning {len(md_files)} markdown file(s) in posts/\n")
    for md_file in md_files:
        process_file(md_file, stats)

    print(f"\n{'='*40}")
    if stats["copied"] == 0 and stats["skipped"] == 0 and stats["warnings"] == 0:
        print("  No image references found.")
    else:
        print(f"  files updated : {stats['files_updated']}")
        print(f"  images copied : {stats['copied']}")
        print(f"  already exist : {stats['skipped']}")
        if stats["warnings"]:
            print(f"  warnings      : {stats['warnings']} image(s) not found on disk")
        else:
            print("  status        : OK")
    print('='*40)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Video embeds for Hugo. Videos are not in git: .githooks/pre-push uploads them
to engram, and the image render hook links them there
(docs/adr/0001-videos-on-engram.md).

  ![[clip.mp4]]               -> ![](clip.mp4)
  ![[clip.mp4|wide|Caption]]  -> ![wide|Caption](clip.mp4)

Then checks that every video linked from a published (non-draft) post exists
on engram, and exits non-zero if one is missing, so the build fails instead of
publishing a broken video (e.g. pushed from the phone, where hooks don't run).

Runs in GitHub Actions before `hugo`, like images.py.

Usage:
    python3 videos.py
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"

VIDEO_EXT = r"\.(?:mp4|mov|webm|m4v)"

# Matches ![[clip.mp4]] and ![[clip.mp4|right|Caption]]
WIKI_EMBED = re.compile(r'!\[\[([^\]|]+' + VIDEO_EXT + r')(?:\|([^\]]*))?\]\]', re.IGNORECASE)
# Matches ![alt](any/path/clip.mp4)
MD_EMBED = re.compile(r'!\[[^\]]*\]\(([^)]+' + VIDEO_EXT + r')\)', re.IGNORECASE)
FRONT_MATTER = re.compile(r'---\s*\n(.*?)\n---', re.DOTALL)
DRAFT = re.compile(r'^draft:\s*true\s*$', re.MULTILINE | re.IGNORECASE)


def engram_url():
    m = re.search(r'^\s*engram\s*=\s*"([^"]+)"', (ROOT / "hugo.toml").read_text(), re.MULTILINE)
    return m.group(1).rstrip("/")


def is_draft(text):
    fm = FRONT_MATTER.match(text)
    return bool(fm and DRAFT.search(fm.group(1)))


def wiki_alt(m):
    # keep position/caption (|right|Caption); a bare number is an Obsidian size, not alt text
    extra = (m.group(2) or "").strip()
    return "" if extra.isdigit() else extra


def exists(url):
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except urllib.error.URLError:
        return False


def main():
    base = engram_url()
    missing = []
    checked = 0

    for md_file in CONTENT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        new = WIKI_EMBED.sub(lambda m: f"![{wiki_alt(m)}]({quote(m.group(1).strip())})", text)
        if new != text:
            md_file.write_text(new, encoding="utf-8")
            print(f"    updated : {md_file.relative_to(ROOT)}")

        if is_draft(new):
            continue
        for path in MD_EMBED.findall(new):
            name = Path(unquote(path)).name
            url = f"{base}/{quote(name)}"
            checked += 1
            if not exists(url):
                missing.append((md_file.relative_to(ROOT), url))

    print(f"\n  videos checked : {checked}")
    for md_file, url in missing:
        print(f"  MISSING        : {url} (in {md_file}) — push from the laptop to upload it")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()

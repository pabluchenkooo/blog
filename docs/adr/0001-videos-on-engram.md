# 1. Videos live on engram, not in git

- Status: accepted
- Date: 2026-10-11

## Context

Posts are written in Obsidian; the vault is this repo, committed and pushed by
obsidian-git, built by GitHub Actions and served from GitHub Pages. That works
for photos, but videos don't fit:

- GitHub rejects files over 100 MB and warns from 50 MB; a repo full of video
  gets slow to clone and can't be cleaned without rewriting history.
- Pages sites have a soft 1 GB limit.
- Expected volume: hundreds of GB of video, eventually TB with photos.

Writing must stay the same: drop the file into the note in Obsidian, commit,
push. Nothing extra to remember.

## Options

| | Option | Why not (now) |
| --- | --- | --- |
| A | Videos in the repo | size limits above |
| B | Git LFS | GitHub LFS quota is small and paid; Pages doesn't serve LFS files |
| C | YouTube / Vimeo | ads, tracking, third-party player, files leave our hands |
| D | Object storage (S3-style) on the VPS (MinIO/Garage) | overkill: an API, keys and a service to run for a few static files |
| D′ | **Static folder on the VPS, uploaded on push** | chosen |
| E | Animated WebP/GIF in the repo | huge files, no sound, poor quality |

## Decision

Videos are served from **engram** (`https://engram.pabluchenko.de/videos/`): a
static nginx on the hum0labs VPS, behind the shared Traefik, with its files on
a Hetzner Volume.
The flow:

1. In Obsidian, drop or link a video like an image:
   `![wide|Caption](static/images/some-video.mp4)`. It previews locally.
2. `.gitignore` ignores video files (`*.mp4`, `*.mov`, `*.webm`, `*.m4v`)
   anywhere in the vault, so they never reach git.
3. `.githooks/pre-push` rsyncs every video in the vault to
   `engram@engram.pabluchenko.de:videos/` before each push. If the upload
   fails, the push is aborted, so a post never goes live without its video.
4. `layouts/_markup/render-image.html` turns a video "image" into a `<video>`
   pointing at `params.engram` + the file name.
5. CI (`videos.py`) checks that every video linked from a published post
   exists on engram, and fails the build if not (e.g. pushed from the phone,
   where hooks don't run).

Rules that follow from this:

- Video **file names must be unique** across the vault: engram is one flat
  folder. The hook refuses to upload two videos with the same name.
- Uploads only add or replace; deleting a video locally does not delete it on
  engram. Clean up by hand (`ssh root@... rm /srv/engram/videos/x.mp4`).
- Replacing a file under the same name can take up to a day to show
  (`Cache-Control: max-age=86400`). Use a new name for a new version.
- Each machine that pushes needs the `engram` SSH host entry (see below).
  Obsidian on the phone can push text, but not videos.

Per-machine setup (`~/.ssh/config`):

```
Host engram.pabluchenko.de
  User engram
  IdentityFile ~/.ssh/ssh-pabluchenko-key
  IdentitiesOnly yes
  AddKeysToAgent yes
  UseKeychain yes
```

plus once: `ssh-add --apple-use-keychain ~/.ssh/ssh-pabluchenko-key`, so the
hook also works from Obsidian without a terminal.

## Consequences

- The blog now depends on the VPS for videos; if it's down, pages load but
  videos don't. Photos stay in git and on Pages.
- Storage scales with the Hetzner Volume (resize online, billed per GB per month;
  check current Hetzner pricing). Fine for tens to low hundreds of GB.

## Open question: TB scale

At hundreds of GB to TB, a volume gets expensive compared to object storage
(Hetzner Object Storage, Cloudflare R2 with free egress, Backblaze B2). That
decision is postponed. The flow is built so a move only changes two things:
the upload target in `.githooks/pre-push` and `params.engram` in
`hugo.toml`. Posts don't change. Revisit when the volume passes ~200 GB or
traffic costs show up.

# Rules for this repo

- **No AI attribution in git.** Never add `Co-Authored-By` trailers, "Generated with Claude Code" lines, session links, or any other AI/assistant attribution to commit messages or PR descriptions. Commits are authored by Pablo only.
- Commit identity for this repo is `Pablo <pabluchenkooo@gmail.com>` (set in the repo's local git config). Never commit with another email.

These are enforced by `.claude/settings.json` (attribution disabled) and `.githooks/commit-msg` (rejects co-author trailers). Enable the hook on a fresh clone with `git config core.hooksPath .githooks`.

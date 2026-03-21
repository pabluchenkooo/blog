---
title: Hostinger Deployment Flow (Subtree + Public Build)
date: 2026-03-21
draft: false
tags: ["tech", "blog"]
---

## Overview

This project deploys to **Hostinger** using a dedicated branch (`hostinger`) that contains only the static output from the `public/` folder.

The flow:

1. Sync content from Obsidian
2. Ensure `public/` is up to date (build step if needed)
3. Extract `public/` into a temporary branch
4. Force push to `hostinger` (deploy branch)
5. Clean up

---

## 🔁 Full Deployment Script

```bash

rsync -av --delete /Users/pablo/Documents/Obsidian\ Vault/blog/content /Users/pablo/pablo/pabloblog/

git subtree split --prefix public -b hostinger-deploy

git push origin hostinger-deploy:hostinger --force

git branch -D hostinger-deploy
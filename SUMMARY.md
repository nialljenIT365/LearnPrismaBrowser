# Prisma Access Browser docs extraction — status & runbook

**Date:** 2026-06-26
**Goal:** Extract `https://docs.paloaltonetworks.com/prisma-access-browser` and **all** child pages into a single Markdown file in this folder.

---

## Status: ✅ COMPLETE — full crawl finished & verified (2026-06-26)

The crawl ran successfully and produced the final deliverable:

```
C:\Users\blink\OneDrive\Documents\PrismaBrowser\prisma-access-browser-docs.md
```

**Verified result** (~855k chars):

| Check | Result |
|---|---|
| Pages extracted | **133 / 133** |
| Pages with substantial article body | 131 |
| Section-cover/landing pages (heading only, no article body — expected) | 2 (doc-set root, Administration guide landing) |
| In-page links | **all 154 resolve** (132 TOC + 22 in-body); 0 dangling, 0 duplicate anchors |
| Headings | clean `## Title` (anchor `<a id>` on its own line above each heading) |
| Wrapped titles / double-spaces | none (source whitespace collapsed) |
| HTML leakage (`<div`/`<script`/`book-pdf-content`) | none |
| Guide breakdown | administration 64 · deployment 22 · integrations 20 · getting-started 14 · activation-and-onboarding 8 · user-guide 4 · root 1 |

**Heading format (2026-06-27 cleanup):** each section heading is plain Markdown
(`## Activate New Prisma Browser …`) with the TOC anchor moved to its own line just
above it (`<a id="…"></a>`), so headings stay clean while the in-document TOC links
keep working in every renderer.

**In-body cross-reference links (2026-06-27):** DITA in-page jump-links (e.g. the
"Use the Prisma Browser Dashboards" page's Web security / Data leakage prevention /
Assets / Policy / User behavior links) are now resolved. The crawler re-injects an
explicit `<a id>` anchor for every referenced fragment — on the target subsection's
heading, or, for headingless targets (procedure steps), on the nearest enclosing
section heading. A final safety-net pass remaps any still-unresolvable fragment to
its own page anchor, so **no in-page link dangles**.

Nothing further is required. To **regenerate** with current doc content later, re-run
`run.ps1` (see below) — it re-fetches every page and overwrites the file.
*(2026-06-27 note: after several full crawls the live docs site began throttling, so
the final safety-net remap was applied directly to the finished file rather than via
a fresh crawl; the same logic is built into the crawler for future clean re-runs.)*

---

## How to finish (after relaunch)

A new Claude Code session starts in `bypassPermissions` mode (per your user settings),
so it will run with **zero prompts**.

**Option A — let Claude run it.** In the new session, say:

> Run `C:\Users\blink\AppData\Local\Temp\prisma-extract\run.ps1` to finish the Prisma Access Browser docs extraction.

**Option B — run it yourself** (no Claude needed). In any PowerShell window:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\blink\AppData\Local\Temp\prisma-extract\run.ps1"
```

Either way it takes ~2–3 minutes and writes:

```
C:\Users\blink\OneDrive\Documents\PrismaBrowser\prisma-access-browser-docs.md
```

When done it prints a summary (pages extracted, any failures, output size).

---

## What gets produced

- **One Markdown file**, `prisma-access-browser-docs.md` (~0.7–1 MB).
- A generated **Table of Contents** with in-document anchor links.
- **133 pages** across the 6 guides, in authored order with heading depth matching
  the doc hierarchy:
  | Guide | Pages |
  |---|---|
  | Activation & Onboarding | 8 |
  | Getting Started | 14 |
  | Deployment | 22 |
  | Administration | 64 |
  | Integrations | 20 |
  | User Guide | 4 |
  | (doc-set root / section covers) | rest |
- Each page section includes a `*Source: <url>*` line back to the live doc.
- **Images and links are kept as absolute URLs** on `docs.paloaltonetworks.com`
  (images are referenced, not downloaded — the deliverable is a single `.md`).

---

## How it works (for reference / re-running later)

- Source platform is Adobe AEM/FrameMaker TechDocs — **server-rendered HTML**, no
  JavaScript needed.
- Discovery: a breadth-first crawl from the doc-set root following every
  `/content/techdocs/en_US/prisma-access-browser/...` link (the book landing pages
  only list direct children, so a full BFS is required to reach the deep topics).
- Per page: parse with BeautifulSoup, take `<h1>` as the title and the
  `div.book-pdf-content` element as the clean article body (this is the printable
  view — no nav/TOC/footer chrome), strip pagination/feedback, rewrite relative
  URLs to absolute, convert to Markdown with `markdownify`.
- Re-running `run.ps1` any time will re-fetch and regenerate the file with current
  content (useful when the docs are updated).

## Tooling locations

- Crawler script: `C:\Users\blink\AppData\Local\Temp\prisma-extract\crawl_prisma.py`
- Runner:         `C:\Users\blink\AppData\Local\Temp\prisma-extract\run.ps1`
- Isolated venv:  `C:\Users\blink\AppData\Local\Temp\prisma-extract\venv` (Python 3.14, `beautifulsoup4` + `markdownify`)

> These live under `%LOCALAPPDATA%\Temp`, which survives a Claude relaunch but may be
> cleared by Windows disk cleanup. If the venv is gone, `run.ps1` rebuilds it
> automatically (needs internet for the two pip packages).

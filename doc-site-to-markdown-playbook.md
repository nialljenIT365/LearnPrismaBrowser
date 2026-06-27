# Playbook: Crawling a Documentation Site into Accurate Markdown

A reproducible method for turning a **published documentation site** (a doc portal /
knowledge base built on a CMS such as Adobe AEM, ReadMe, Docusaurus, GitBook, MkDocs,
etc.) into clean, complete, well-linked Markdown — one file per doc-set, with a Table
of Contents and source links. Written to hand to another agent. No vendor names are
required; substitute your target site's specifics where indicated by `<…>`.

---

## Core principles

1. **Program the analysis; keep raw bytes out of context.** Never read whole HTML
   pages or full crawl dumps into your working context to "eyeball" them. Fetch and
   parse in a script/subprocess and surface only derived findings (counts, page lists,
   sample tokens). The raw bytes stay in the sandbox.
2. **Discovery and extraction are two separate problems.** *Discovery* = "what is the
   complete set of pages?" *Extraction* = "what is the clean content of one page?"
   They fail independently and must be measured independently.
3. **Trust the site's own table of contents, not the rendered nav.** Modern doc sites
   render the left-hand navigation client-side (JavaScript), so a naive link-follow
   crawl sees almost nothing. Find the machine-readable TOC the site uses to build that
   nav and drive discovery from it.
4. **Deterministic, resumable scripts — not ad-hoc fetches.** Every fetch is cached to
   disk; every transform lives in a re-runnable script. A blocked or killed run resumes
   from cache instead of re-hitting the site.
5. **Verify completeness with a detector; iterate to zero.** "Done" means a coverage
   audit shows every in-corpus link resolves to a captured page (minus a documented
   allowlist of out-of-scope cross-references), not "looks complete".
6. **Be a polite client.** One request at a time, spaced, with exponential-backoff
   retries. Assume the site will throttle you; design so throttling only slows you down,
   never corrupts output.

---

## Stage 0 — Reconnaissance (do this before writing the crawler)

Fetch **one** representative content page and **one** section/landing page and inspect:

- **Is the article body in the server-rendered HTML?** Search the raw HTML for a
  distinctive sentence you can see on the page. If present → server-rendered, no
  headless browser needed. If absent → the body is JS-hydrated; you'll need the site's
  data API or a headless browser (heavier — avoid if any server-rendered view exists).
- **Find the clean "article" container.** Doc CMSs wrap the real content in a single
  element (e.g. a printable/PDF view, `<main>`, `<article>`, or a class like
  `book-pdf-content` / `content-body` / `md-content`). Extract *that* element, not the
  whole page — it excludes nav, header, footer, feedback widgets, and breadcrumbs.
- **Does the landing/section page expose child links in server HTML?** Often **no** —
  the nav tree is JS-only. This is the trap that makes link-follow crawls under-collect.
- **Hunt for the TOC/data endpoint.** Try sibling URLs next to a page URL:
  `<page>.toc.json`, `<page>.nav.json`, `/toc.json`, `<section>.json`, a `sitemap.xml`,
  or an obvious `/api/...` the page's JS calls (check the HTML for `fetch(`/`.json`).
  A TOC endpoint that returns the nested page tree is the single most valuable find.
- Record: the article container selector, the TOC endpoint pattern, the URL→path
  convention (e.g. trailing `.html`), and how a doc-set decomposes into *books*
  (top-level sections, usually the direct children of the doc-set root page).

## Stage 1 — Discovery: TOC-driven, with a BFS union as a safety net

**Primary: parse the TOC tree.**
- Enumerate the **books** (top-level sections) — usually the in-prefix links on the
  doc-set root's server HTML.
- For each book, fetch its TOC endpoint (e.g. `<book>.toc.json`) and walk the nested
  entries recursively, collecting `(url, title, depth)` in document order.

**Always union with a bounded BFS — do not rely on the TOC alone.**
> **Critical gotcha:** some books' TOC endpoints return errors (e.g. HTTP 400) or
> partial trees. If you take "the TOC returned *some* pages" as success, you silently
> ship a doc-set missing entire sections. **Always also run a link-follow BFS** (start
> from the root/seeds, enqueue only in-scope links found in each page's server HTML)
> and **union** its results with the TOC's. The two methods are complementary: TOC wins
> where nav is JS-only; BFS wins where the TOC endpoint 400s but pages cross-link.

**Scoped vs full crawls.** A *full* crawl takes the whole doc-set prefix. A *scoped*
crawl takes a set of **seed sub-tree prefixes** and accepts a page only if it lives
under one of them — use this to extract a few relevant sub-trees from a huge doc-set
without pulling the entire thing.

## Stage 2 — Extraction: one page → clean Markdown

For each discovered page:
1. Fetch (cache-first — see Stage 4).
2. Parse HTML; take `<h1>` as the title (collapse internal whitespace so titles never
   wrap: `re.sub(r"\s+", " ", title)`).
3. Select the **article container** found in Stage 0; **decompose** chrome inside it
   (pagination, feedback, toolbar, scripts, styles).
4. **Absolutize** relative URLs (`/foo` → `https://<host>/foo`) for `href` and `src`
   so links/images work out of context.
5. Convert that element to Markdown (a library like `markdownify` with ATX headings).
6. Remove the duplicated page-title line the converter emits at the top of the body.
7. **Shift heading levels** by the page's depth so the merged doc nests correctly
   (a page at tree-depth *d* starts at heading level `min(2+d, 6)`).

## Stage 3 — Markdown hygiene (the details that make it usable)

- **Clean headings + own-line anchors.** Emit `## Title` (plain), and put the TOC
  anchor on its **own line above** it: `<a id="slug"></a>\n\n## Title`. This keeps
  headings clean while in-document TOC links resolve in every renderer. (Inline
  `## <a id>Title` is ugly in raw Markdown; relying on auto-generated heading IDs is
  fragile when heading text repeats.)
- **Re-inject in-body cross-reference anchors.** Doc CMSs use intra-page `#fragment`
  links whose target element IDs the Markdown converter drops. For each `#fragment` a
  page links to, find the target element and emit an explicit `<a id="fragment"></a>`
  on the heading it belongs to (or, for a heading-less target like a procedure step,
  on the nearest enclosing section heading). Otherwise those links dangle.
- **Dead-link safety net.** After assembly, rewrite any remaining in-page link whose
  target was never anchored to point at its own page's anchor — so no in-page link ever
  dangles, now or for future edge cases.
- **Assemble** one file per doc-set: title + provenance line, a generated **Table of
  Contents** (`- [Title](#slug)` indented by depth), then each page as
  `<anchor> / heading / *Source: <url>* / body / ---`.

## Stage 4 — Resumability & politeness (survive throttling)

- **On-disk page cache.** Key each fetch by a hash of its path; write the response to
  `cache/<hash>.html`. `fetch()` returns the cache hit instantly. Re-running after a
  kill/block re-discovers from cache and only hits the network for *new* pages.
- **Gentle rate-limit + backoff retries.** Sleep ~0.5 s between *network* fetches (not
  cache hits). On failure, retry 4–6× with exponential backoff (e.g. `min(4*(n+1), 30)`
  seconds). This rides out rate-limiting; the cache makes a hard block recoverable.
- **Long jobs run in the background**, resumable across sessions. Phase large work
  (one doc-set at a time), smallest first, and report after each.

## Stage 5 — Verify completeness (the coverage audit)

This is how you answer "are we missing anything?":
1. **captured** = the set of every `*Source:` URL across all output files (normalize:
   strip host, strip a `content/.../` infix if present, strip `.html`, strip `#…`).
2. **referenced** = every in-corpus link to the doc host, normalized the same way.
3. **missing = referenced − captured.** Group by doc-set and by keyword
   (`license|activate|onboard|configure|install|deploy|prerequisite|...`).
4. **Triage the missing list** into: (a) genuine in-scope gaps → crawl them;
   (b) duplicate URL-forms of pages you already have (same leaf, different root) →
   not missing; (c) adjacent-product cross-references → out of scope, document and
   exclude. Most of a large "missing" count is usually (c).

Also run cheap quality detectors over each output: count raw HTML leakage
(`<div`, `<script`, the article-container class — want 0), unresolved `](#…)` anchors
(want 0), and replacement chars `�` (want 0).

## Stage 6 — Synthesis (optional, high-value)

Over the raw per-doc-set library, write a **map document** that ties the corpus to the
question the user actually has (an architecture, a setup journey, a feature). For each
concept: one-line definition + the authoritative source URL + which local file(s) cover
it + a status (covered / partial / gap). This is what makes a dump into a usable
reference.

---

## Anti-patterns (don't)

- ❌ Drive discovery from the rendered left-nav or a link-follow crawl alone — JS nav
  is invisible to it; you'll silently miss whole sections.
- ❌ Treat "the TOC returned some pages" as complete — union with BFS and *measure*.
- ❌ Spin up a headless browser when a server-rendered printable view exists.
- ❌ Read raw HTML or full crawl output into context to inspect it — run detectors.
- ❌ Hammer the site in parallel with no backoff — you'll get blocked and corrupt
  partial output. One stream, spaced, cached, resumable.
- ❌ Inline `<a id>` inside heading text, or trust renderer auto-anchors when heading
  text repeats — TOC links break.
- ❌ Ship without a coverage audit — "looks complete" is not complete.

## Minimal pipeline at a glance

```
recon (article container? TOC endpoint? JS nav?)
  └► discover = TOC-tree ∪ bounded BFS   (scoped: filter to seed sub-trees)
       └► per page: fetch(cache) ▸ select article ▸ strip chrome ▸ absolutize
                    ▸ markdownify ▸ shift headings ▸ re-inject fragment anchors
            └► assemble: TOC + own-line anchors + *Source* links + dead-link safety net
                 └► verify: coverage audit (captured vs referenced) + quality detectors → 0
                      └► (optional) synthesis map tying corpus to the user's question
```

## Suggested script/file layout

```
crawl_docset.py     # one parameterized crawler: --root <prefix> [--seeds a,b,…] --out f.md --name "…"
                    #   TOC∪BFS discovery, on-disk cache, gentle retries, anchors+TOC+safety-net
cache/              # <hash>.html per fetched page  (resume; never re-fetch)
<doc-set>.md        # one output per doc-set (full or scoped)
audit.py            # coverage audit: captured Source URLs vs referenced links → missing, triaged
<map>.md            # optional synthesis tying the corpus to the user's architecture/journey
PLAYBOOK.md         # this method
```

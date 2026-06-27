# LearnPrismaBrowser

A curated, offline **Markdown knowledge base for Palo Alto Networks Prisma Access
Browser (Prisma Browser)** — built to be queried by an LLM so you can ask
setup/configuration questions and get answers **grounded in the official docs**, each
with a citation to the exact file, section, and source URL.

It covers the product end-to-end — **license → activate → onboard → deploy → configure**
— plus identity/Entra ID integration, the routing model, and tenant/sub-tenant setup.

- ~935 documentation pages across 22 Markdown files (~11 MB)
- Every extracted page carries a `*Source:` link back to the live Palo Alto documentation
- **Start with [INDEX.md](INDEX.md)** — the catalog of every document with a summary

---

## What's in here

See **[INDEX.md](INDEX.md)** for the full catalogue. In short:

| Area | Where |
|---|---|
| Core product docs | `prisma-access-browser-docs.md`, `prisma-browser-routing-model.md`, the converted `sec-int-…` / `secure-browser-for-dummies` PDFs |
| Setup & lifecycle | `prisma-browser-licensing-onboarding.md`, `prisma-tenants-and-sub-tenants.md` |
| Identity / Entra ID | `prisma-browser-entra-id-references.md`, `strata-cloud-manager-entra-id-integration.md` |
| Dependency library | `cloud-identity.md`, `common-services.md`, `prisma-access-scoped.md`, `strata-logging-service.md` |
| How it was built | `doc-site-to-markdown-playbook.md`, `scanned-pdf-to-markdown-playbook.md` |

---

## How to use it with an LLM (the point of this repo)

This repo ships a ready-made **grounded Q&A system prompt** designed to stop the model
inventing answers: it responds **only** from these files and **cites the file +
section + source URL** for every claim. If the answer isn't in the docs, it says so
instead of guessing.

> **The system prompt lives in [LLM-PROMPT.md](LLM-PROMPT.md).**
> Copy the text **between the `=== BEGIN SYSTEM PROMPT ===` and `=== END SYSTEM PROMPT ===`
> markers** — that block is what you paste into the LLM. Everything else in that file is
> usage notes, a worked example, and tuning tips.

### Quick start

1. Copy the prompt (between the BEGIN/END markers) into your LLM's **System** /
   **Custom Instructions** field.
2. Give the LLM access to the documents — pick one option below.
3. **Always include [INDEX.md](INDEX.md)** — the prompt uses it to route to the right file.
4. Ask your question. You'll get an **Answer** plus a **Sources** list.

### Three ways to give the LLM the documents

**Option A — Connector / RAG (recommended, most reliable).**
Use a tool that ingests the whole repo: ChatGPT's *“Connect GitHub”*, a Claude
**Project** with this repo added, **NotebookLM**, or any RAG setup. It indexes all
files; the prompt + `INDEX.md` find the right ones. Best for the full corpus — it's
too big to paste.

**Option B — Browsing / Git-aware model (e.g. ChatGPT with web access).**
The repo's raw base URL is already baked into [LLM-PROMPT.md](LLM-PROMPT.md), and the
prompt tells the model to **bootstrap from `INDEX.md`** automatically. So:

1. Paste the prompt (the BEGIN/END block) into the system / instructions field.
2. Ask your question — the model fetches `…/main/INDEX.md`, picks the relevant file(s),
   fetches their raw URLs, and answers with **Sources**.

> **Gotcha (common):** just pasting the *repo link* into a chat usually makes the model
> read only this README and stop. Paste the **prompt**, not just the link, so it knows to
> go fetch `INDEX.md` and the right file. If it still doesn't fetch, tell it:
> *“Fetch `https://raw.githubusercontent.com/nialljenIT365/LearnPrismaBrowser/main/INDEX.md`,
> choose the relevant file, fetch its raw URL, then answer with sources.”*
> The ~6 MB `strata-logging-service.md` may be too big to fetch in full — for
> logging-heavy questions, prefer **Option A**.

**Option C — Paste a subset.**
For a focused question, paste **`INDEX.md` + the one or two relevant files** (chosen
from INDEX's tables) into the chat. Don't paste everything — the corpus is ~11 MB and
one file alone (`strata-logging-service.md`) is ~6 MB.

### Example

> **Q:** *Which identity providers can I use for Prisma Browser SSO, and where do I configure Entra ID?*

The model answers from `strata-cloud-manager-entra-id-integration.md` /
`cloud-identity.md` and lists those files + sections + the live doc URLs as its
**Sources** — so you can click through and verify.

---

## Good to know

- **Grounded, with citations.** The prompt requires a `Sources:` block on every answer
  (file → section → `*Source:` URL). A *“not covered in the documentation”* reply is
  treated as a **success**, not a failure — that's the anti-hallucination design. If an
  answer comes back with **no Sources**, treat that turn as failed and re-ask.
- **Traceable.** Every `*Source:` URL points to the live page on
  `docs.paloaltonetworks.com`, so any answer can be checked against the original.
- **Settings.** Keep temperature low (≈0–0.3) for factual retrieval.

## Sources & disclaimer

All content is derived from **public Palo Alto Networks documentation** (crawled from
`docs.paloaltonetworks.com`) and public product PDFs, converted to Markdown for
offline/LLM use. This is an **unofficial learning aid**, not affiliated with or endorsed
by Palo Alto Networks. For production decisions, always confirm against the official
documentation linked in each page's `*Source:` line.

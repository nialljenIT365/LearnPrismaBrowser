# CLAUDE.md — LearnPrismaBrowser

Grounded Q&A knowledge base for **Palo Alto Prisma Access Secure Enterprise Browser**
("Prisma Browser"): ~20 Markdown docs / ~11 MB crawled from official documentation, built to be
queried by an LLM with citations.

## Resume protocol

1. **Read [PROJECT-STATUS.md](PROJECT-STATUS.md) first** — current state, Q&A already answered,
   open threads. Update it at the end of each working session.
2. Operating procedure for answering questions: [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md).
   Grounding rules: [LLM-PROMPT.md](LLM-PROMPT.md). Catalogue: [INDEX.md](INDEX.md).

## Corpus handling (hard rules)

- **Never bulk-read the corpus.** Index the folder once per session (RAG/ctx_index), route via
  INDEX.md, then Grep + Read only the exact sections needed. `strata-logging-service.md` is
  ~6 MB — sections only, never whole.
- **Answers must be grounded:** cite `file → section heading → *Source:` URL; quote exact values
  verbatim; label inference as inference; "not covered in the docs" is a valid answer — but open
  the specific page before concluding absence (summary snippets truncate).

## Git conventions

- This folder **is** the working clone of `https://github.com/nialljenIT365/LearnPrismaBrowser`
  (public). Commit and push directly from here.
- Author: `nialljenIT365 <nialljen@gmail.com>` (already set in local git config). **No AI
  co-author lines.**
- The owner also commits via the GitHub web UI — **always `git pull` before pushing.**
- Source PDFs (`*.pdf`) and build scripts other than `convert_pdfs_to_md.py` are deliberately
  **untracked** — don't commit them without being asked.

## Related locations

- `C:\Users\blink\OneDrive\Documents\PrismaBrowser` — original build folder, now **archive**;
  don't edit docs there.

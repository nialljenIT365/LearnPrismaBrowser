# Agent Onboarding — how to engage with this repo

How an AI agent (fresh, no prior context) should read and answer questions from this
Prisma Browser documentation corpus **accurately and traceably**. This is the *how to
operate*; the *what to obey* lives in [LLM-PROMPT.md](LLM-PROMPT.md).

> **TL;DR** — Point the agent at [INDEX.md](INDEX.md) and [LLM-PROMPT.md](LLM-PROMPT.md);
> give it a way to retrieve (index-and-search, **or** fetch-INDEX-then-the-named-file);
> have it read **only the exact sections it needs**; and require a **file → section → Source URL**
> citation for every claim — with *"not in the docs"* an allowed, expected answer.

---

## The corpus in one breath

~20 Markdown documents, ~11 MB total (one file, `strata-logging-service.md`, is ~6 MB on
its own). Far too large to hold all at once — so **don't**. Work like a research assistant
with a filing cabinet: catalogue it, look things up, pull the exact pages, cite chapter and
verse. [INDEX.md](INDEX.md) is the catalogue; web-extracted pages each carry a `*Source:` line
that is the authoritative URL for that page.

## Three layers

1. **Rulebook** — [LLM-PROMPT.md](LLM-PROMPT.md). Paste the block between its
   `=== BEGIN ===` / `=== END ===` markers into the agent's system prompt. Anti-hallucination
   rules, citation format, and the "say so when it isn't there" templates live there. Do not
   reinvent these.
2. **Maps** — [INDEX.md](INDEX.md) (which file holds what) and
   [prisma-browser-routing-model.md](prisma-browser-routing-model.md) (the architecture:
   Explicit Proxy on-ramp, Service Connection / ZTNA Connector off-ramps, Authentication
   Gateway, Direct Internet Access). Read these two **first** to orient. They are small.
3. **Operating procedure** — the rest of this file.

## Operating procedure

**1. Orient before answering.** Read [INDEX.md](INDEX.md) and the routing model. Don't read
anything large up front.

**2. Pick a reading strategy based on available tools:**

| You have… | Do this |
|---|---|
| A **search / index tool (RAG)** | Index the whole folder **once**, then query it per question (index → search → pull exact sections). |
| Only **web-fetch / browse** | Use the raw base URL below. Fetch **INDEX.md first**, let it route you to the right file(s), then fetch **only those**. Never pull the whole corpus; reuse fetched files across turns. |
| The **files already in context** | Just route via INDEX.md; open only the relevant section. |

**3. Per question: route → pull exact text → answer.** Use INDEX.md to choose the file, then
open **only the relevant section** (find the heading, read that slice) instead of the whole
document. Search/fetch previews get truncated — pull the exact passage when you need precise,
ordered steps.

**4. Mind the size trap.** `strata-logging-service.md` is ~6 MB — never fetch or read it whole.
Read only the needed section, or ask the user to narrow the question.

**5. Answer by the house rules** ([LLM-PROMPT.md](LLM-PROMPT.md)):
- Cite **file → section heading → the page's `*Source:` URL**.
- **Quote exact values verbatim** — role names, ports, menu paths, license SKUs, IP ranges.
- **Label inference** as inference, with the passages it rests on.
- If it isn't in the docs, **say so plainly**. A correct "not covered" beats a confident guess.

**6. Treat a shallow "not found" as a prompt to dig.** If summary snippets look thin, open the
specific page before concluding it's absent. (Example: the "does initial login go straight to
Entra ID?" answer isn't in the summaries — it's in the Azure AD IP-based-enforcement page, as
the conditional-access exclusion of the Prisma Browser app.)

## Repo raw base URL (for fetch/browse agents)

```
https://raw.githubusercontent.com/nialljenIT365/LearnPrismaBrowser/main
```

Resolve any relative filename `X.md` to `<base>/X.md` — e.g.
`https://raw.githubusercontent.com/nialljenIT365/LearnPrismaBrowser/main/INDEX.md`.

## Quick-start checklist

- [ ] Loaded the [LLM-PROMPT.md](LLM-PROMPT.md) grounding block into the system prompt.
- [ ] Read [INDEX.md](INDEX.md) + [prisma-browser-routing-model.md](prisma-browser-routing-model.md).
- [ ] Chose a retrieval strategy (RAG vs fetch-by-name).
- [ ] For each question: routed via INDEX → opened only the needed section → answered.
- [ ] Every factual claim carries a file + section + `*Source:` URL.
- [ ] Said "not in the docs" where true, instead of guessing.

# Project Status — session handoff

> **Last updated: 2026-07-02.** Read this together with [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md)
> to pick the project up where it was left off. Update this file at the end of each working session.

## What this project is

A grounded, citable Markdown knowledge base for **Palo Alto Prisma Access Secure Enterprise
Browser (Prisma Browser)** — catalogued in [INDEX.md](INDEX.md), queried under the rules in
[LLM-PROMPT.md](LLM-PROMPT.md), with agent instructions in [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md)
and a paste-ready browsing prompt in [WEB-AGENT-PROMPT.md](WEB-AGENT-PROMPT.md).

## Where things stand (2026-07-02)

- **Corpus: complete and verified.** ~20 docs / ~11 MB / ~935 pages; every extracted page carries a
  `*Source:` URL; INDEX.md is the catalogue. No open extraction work.
- **Agent enablement: shipped.** `LLM-PROMPT.md` (grounding rules, raw base URL baked in),
  `AGENT-ONBOARDING.md` (operating procedure), `WEB-AGENT-PROMPT.md` (copy-paste prompt),
  README section pointing at both. Commits `858690b`, `d153ed5`.
- **Local folder ↔ GitHub: in sync** as of this handoff (verified by full-content diff, CRLF-insensitive).
- **Findings notes:** [prisma-browser-first-login-conditional-access.md](prisma-browser-first-login-conditional-access.md)
  (owner-added) records the first-login / conditional-access "bootstrap exclusion" investigation with
  per-claim [OFFICIAL] vs [COMMUNITY/SUPPORT] source labels.

## Working conventions (read before changing anything)

- **Local source-of-truth folder:** `C:\Users\blink\OneDrive\Documents\PrismaBrowser` — it is **not**
  a git repo. To commit: clone `https://github.com/nialljenIT365/LearnPrismaBrowser` fresh to a temp
  dir, copy changed files in, commit as `nialljenIT365 <nialljen@gmail.com>` (**no AI co-author
  lines**), push, and copy any merge results back so local and remote stay identical.
- **The owner also commits via the GitHub web UI** — always clone/pull fresh immediately before
  pushing; never push from a stale clone.
- **Answering questions from the corpus:** follow [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) —
  orient via INDEX → retrieve (RAG index or fetch-by-name) → read **only** the needed sections →
  cite `file → section → *Source:` URL → say "not covered" when true, but **open the specific page
  before concluding absence** (summary snippets truncate; the first-login answer was found this way).
- **Never read `strata-logging-service.md` whole** (~6 MB) — sections only.

## Q&A already answered this session (don't re-derive; ask for the transcript topic if needed)

Service connection planning + full SCM config steps (incl. IKE/IPSec options, verify) · sub-tenant
licensing via Common Services allocation · Explicit Proxy vs Authentication Gateway · DIA
authentication (auth leg is separate; proxy is "SSO login pages only") · first-login-to-Entra
exclusion ("Prisma Browser can't be a required application"; exclude it from CA policy) · Entra app
registrations (CIE Enterprise App vs Client Credential Flow; OneDrive; Purview; CA cloud-app
reference) · Explicit Proxy overview + 5 connection methods · Forwarding Profiles (multiple PACs /
rules / GP attach) · PAC optional for PAB ("No PAC File" + Traffic Flow control) + EP-to-datacenter
via service connection · screen-capture protection (Screenshot control + Webpage Watermarking +
bypass) · PAB RBAC (six roles) + IAM assignment workflow + service accounts · service-connection
special use cases (SC-vs-ZTNA matrix + Advanced Deployments).

## Open threads (natural next steps)

1. **ZTNA Connector configuration steps** — repeatedly flagged as the better off-ramp for
   Azure-hosted apps; config walkthrough not yet done (in corpus: `prisma-access-scoped.md`).
2. **Panorama variants** — service-connection and EP procedures were summarized for SCM only;
   Panorama versions exist in the corpus if needed.
3. **Advanced deployments deep-dives** — Multi-Cloud Redundancy and Traffic Steering sections
   located but not yet summarized.
4. **Windows Account-Based SSO** — whether it needs its own Entra app registration is unverified.
5. **Known corpus gaps (flag, don't guess):** no Azure-portal-side steps (VPN Gateway / Local
   Network Gateway); no manual registration steps for the "Prisma Browser" conditional-access
   cloud app; no per-seat Prisma-Browser license quantity field documented in allocation.
6. **Possible repo additions:** map the six PAB roles → the SCM pages each can edit; OAuth 2.0
   token-request how-to for service accounts (pan.dev link is in `common-services.md`).

## Session log

- **2026-06-27** — corpus built (crawls + PDF conversions), INDEX/LLM-PROMPT deployed to GitHub,
  RAG bootstrap instructions fixed (base URL + INDEX-first fetch).
- **2026-07-02** — grounded Q&A session (topics above); added AGENT-ONBOARDING.md,
  WEB-AGENT-PROMPT.md, README pointers (`858690b`, `d153ed5`); this status file added.

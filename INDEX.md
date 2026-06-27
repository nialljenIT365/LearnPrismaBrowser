# Prisma Browser — Documentation Index

A consolidated, offline Markdown corpus for **Palo Alto Prisma Access Browser** —
covering the product itself plus every dependency needed to **license → activate →
onboard → deploy → configure**, including identity/Entra ID integration, the routing
model, and tenant/sub-tenant management.

**Corpus:** 20 Markdown documents · ~11 MB · ~935 captured doc pages · 6 source PDFs.
All web content carries per-page `*Source:` links back to `docs.paloaltonetworks.com`;
all files verified for clean headings, working in-page links, and no HTML leakage.

> **🤖 If you are an LLM or agent answering from this corpus — read this first.**
> Before answering any question, **load and follow [LLM-PROMPT.md](LLM-PROMPT.md)** — the
> grounded-QA system prompt. It requires you to: answer **only** from these files; cite
> **file → section → `*Source:` URL** for every claim; and reply *"not covered in the
> documentation"* rather than guess. If you can fetch URLs, retrieve it from
> `https://raw.githubusercontent.com/nialljenIT365/LearnPrismaBrowser/main/LLM-PROMPT.md`.
> Then use the tables below to route to the right file(s) for the question, and fetch
> only those.

> **Start here (humans):** [prisma-browser-routing-model.md](prisma-browser-routing-model.md) — the
> architecture map that ties the whole corpus to the "Route Private Applications Only"
> design (EP, Service Connection, ZTNA Connector, Authentication Gateway, Direct Internet Access).

---

## 1. Core Prisma Browser reference

| Document | Size / Pages | Contents |
|---|---|---|
| [prisma-access-browser-docs.md](prisma-access-browser-docs.md) | 858 KB · 133 pp | **The complete Prisma Access Browser doc set** (web-extracted): activation & onboarding, getting started + prerequisites, deployment (MDM/Intune/Jamf/Linux/Windows/macOS), administration (policy, data controls, dashboards), integrations, user guide. |
| [prisma-browser-routing-model.md](prisma-browser-routing-model.md) | 10 KB | **Synthesis map** of the routing architecture: each component (EP, Service Connection, ZTNA Connector, Authentication Gateway, DIA) → its authoritative source + which local files cover it + status. |

## 2. Converted product PDFs (born-digital → Markdown, no OCR)

| Document | Size | Contents |
|---|---|---|
| [sec-int-and-private-apps-pb-design.md](sec-int-and-private-apps-pb-design.md) | 64 KB | *Securing Internet & Private Apps with Prisma Browser* — **design** guide. |
| [sec-int-and-private-apps-pb-deployment.md](sec-int-and-private-apps-pb-deployment.md) | 60 KB | Same series — **deployment** guide. |
| [sec-int-and-private-apps-pb-prisma-access-design.md](sec-int-and-private-apps-pb-prisma-access-design.md) | 76 KB | **Prisma Access** edition — design (EP, service connections, ZTNA). |
| [sec-int-and-private-apps-pb-prisma-access-deployment.md](sec-int-and-private-apps-pb-prisma-access-deployment.md) | 77 KB | **Prisma Access** edition — deployment. |
| [secure-browser-for-dummies.md](secure-browser-for-dummies.md) | 11 KB | *The Secure Browser for the Modern Enterprise* — concepts/marketing primer. |
| [prisma-access-browser.md](prisma-access-browser.md) | 7 KB | 3-page cover/overview (content overlaps the web extraction above). |

## 3. Setup & lifecycle

| Document | Size / Pages | Contents |
|---|---|---|
| [prisma-browser-licensing-onboarding.md](prisma-browser-licensing-onboarding.md) | 741 KB · 113 pp | **Setup prerequisites** across 3 doc-sets: Prisma Access license & activation, Strata Cloud Manager onboarding/settings, Cloud Identity Engine licensing. The steps *before* browser onboarding. |
| [prisma-tenants-and-sub-tenants.md](prisma-tenants-and-sub-tenants.md) | 580 KB · 126 pp | **Tenant / multitenancy** for building a dedicated Prisma Browser sub-tenant: tenant concepts & device associations (Common Services), subscription & multitenant management (Strata Cloud Manager), multitenancy (Prisma Access). Opens with a 5-step sub-tenant roadmap. |

## 4. Identity / Entra ID integration

| Document | Size / Pages | Contents |
|---|---|---|
| [prisma-browser-entra-id-references.md](prisma-browser-entra-id-references.md) | 10 KB · 3 pp | Prisma Browser ↔ Entra ID: IP-Based Enforcement via Authentication Gateway, automatic web-app sign-in with Entra ID, macOS support; + index of 33 pages referencing Entra/Azure AD. |
| [strata-cloud-manager-entra-id-integration.md](strata-cloud-manager-entra-id-integration.md) | 52 KB · 1 pg | Cloud Identity Engine "Configure an Identity Provider" — *Configure Azure as an IdP* (Entra ID via SAML 2.0) alongside Okta/Ping/Google. |
| [scm-referenced-pages.md](scm-referenced-pages.md) | 6 KB · 2 pp | Two SCM pages the PB docs link to: Log Viewer, Monitor Data Centers — ZTNA Connectors. |
| [prisma-browser-first-login-conditional-access.md](prisma-browser-first-login-conditional-access.md) | findings note | **Findings note (mixed sources — [OFFICIAL] vs [COMMUNITY/SUPPORT]).** First login / "bootstrap exclusion" question: confirms **no** documented first-login CA carve-out; the only practical carve-out (exclude native Outlook/Teams from the CA policy) is **community/support, not official**. Each claim is source-labelled. |

## 5. Dependency reference library (full/scoped doc-set crawls)

| Document | Size / Pages | Contents |
|---|---|---|
| [cloud-identity.md](cloud-identity.md) | 894 KB · 82 pp | **Cloud Identity Engine** (full) — directories (Entra/Azure, Okta, on-prem), SAML/SCIM IdP setup, authentication profiles. |
| [common-services.md](common-services.md) | 594 KB · 113 pp | **Common Services** (full) — subscription/tenant management (licensing), Identity & Access (roles/permissions), device associations. |
| [strata-logging-service.md](strata-logging-service.md) | 6.1 MB · 219 pp | **Strata Logging Service** (full) — log storage, forwarding, administration (largest set). |
| [prisma-access-scoped.md](prisma-access-scoped.md) | 1.08 MB · 143 pp | **Prisma Access** (scoped) — the 5 routing-component sub-trees: explicit proxy, service connections, traffic-steering (DIA), mobile-user auth, ZTNA connector. |

## 6. Methodology & tooling

| Document | Size | Contents |
|---|---|---|
| [LLM-PROMPT.md](LLM-PROMPT.md) | 9 KB | **The grounded Q&A system prompt.** Paste the block between its BEGIN/END markers into your LLM to query this corpus with cited, hallucination-resistant answers (see [README.md](README.md) for setup). |
| [doc-site-to-markdown-playbook.md](doc-site-to-markdown-playbook.md) | 11 KB | **Generic, agent-ready** method for crawling a documentation site into accurate Markdown (TOC∪BFS discovery, extraction, hygiene, resumability, coverage audit). |
| [scanned-pdf-to-markdown-playbook.md](scanned-pdf-to-markdown-playbook.md) | 11 KB | Generic method for OCR-ing scanned/watermarked PDFs into Markdown. |
| [SUMMARY.md](SUMMARY.md) | 5 KB | Runbook/status for the Prisma Access Browser web extraction (how to re-run). |
| [convert_pdfs_to_md.py](convert_pdfs_to_md.py) | — | Reproducible PDF→Markdown converter (text-layer, no OCR) for the source PDFs in this folder. |

---

## Quick navigation by task

- **Understand the architecture** → [prisma-browser-routing-model.md](prisma-browser-routing-model.md)
- **License & activate** → [prisma-browser-licensing-onboarding.md](prisma-browser-licensing-onboarding.md)
- **Build a dedicated sub-tenant** → [prisma-tenants-and-sub-tenants.md](prisma-tenants-and-sub-tenants.md)
- **Set up identity / Entra ID SSO** → [strata-cloud-manager-entra-id-integration.md](strata-cloud-manager-entra-id-integration.md) + [cloud-identity.md](cloud-identity.md)
- **Onboard, deploy & configure the browser** → [prisma-access-browser-docs.md](prisma-access-browser-docs.md)
- **Connectivity (proxy / connector / private apps)** → [prisma-access-scoped.md](prisma-access-scoped.md)

> **Source PDFs** (originals, kept for reference): `*.pdf` in this folder — converted to the
> `sec-int-…` / `secure-browser-for-dummies` / `prisma-access-browser` Markdown files above.

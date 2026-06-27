# Prisma Access Browser — Routing Model ("Route Private Applications Only")

> A synthesized map of the Prisma Browser routing architecture and where each
> component is documented. Built from the local corpus in this folder + the live
> Palo Alto docs. Source of the architecture: the "Prisma Access Browser: Routing —
> Route Private Applications Only" design diagram.

## The model in one picture

The Prisma Browser ships an **internal PAC file** that splits a user's traffic three ways:

```
                                  ┌──────────────── PRISMA ACCESS ────────────────┐
                                  │   (On-Ramp)                      (Off-Ramp)    │
                                  │                  ┌─ Routing(iBGP) ─► Service ──┐│
 Prisma Browser ──(PAC: private)─┼─► Explicit Proxy ┤                  Connection ├┼─► Private Apps
        │                        │       (EP)       └─ DNS proxy ─────► ZTNA ──────┘│
        │                        │                                     Connector   │
        │                        │                                                 │
        ├──(PAC: auth/known-IP)──┼─► Authentication Gateway ───────────────────────┼─► Identity Providers
        │                        │   (forward proxy; known source IPs for          │   (Okta / Ping / Entra ID)
        │                        │    PB conditional-access policies)               │
        │                        └─────────────────────────────────────────────────┘
        │
        └──(PAC: internet/SaaS)──── Direct Internet Access ──────────────────────────► SaaS Apps
                                    (bypasses Prisma Access)                            (Zoom, Gmail, Dropbox, …)
```

**Only private-application traffic is routed into Prisma Access**; internet/SaaS
traffic egresses **directly** (Direct Internet Access). Authentication traffic is
steered to the Authentication Gateway so the IdP sees known, stable source IPs.

## Component map

| # | Component | Role | Primary documentation | In this folder |
|---|---|---|---|---|
| 1 | **Explicit Proxy (EP)** | On-ramp: private-app traffic enters Prisma Access here (selected by the PAC file) | [prisma-access › mobile-users-explicit-proxy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy) | **`prisma-access-scoped.md`** (68 pp), `sec-int-…-pb-prisma-access-deployment.md` (25) |
| 2 | **Service Connection** | Off-ramp #1: iBGP routing from Prisma Access to private apps | [prisma-access › prisma-access-service-connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-service-connections/plan-a-service-connection) | **`prisma-access-scoped.md`** (7 + 27 advanced pp), `sec-int-…-pb-prisma-access-deployment.md` (7) |
| 3 | **ZTNA Connector** | Off-ramp #2: DNS-proxy path from Prisma Access to private apps (a.k.a. *Prisma Browser Connector*) | [prisma-access-browser › onboard-the-prisma-browser-connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/onboard-the-prisma-browser-connector) | `prisma-access-browser-docs.md`, **`prisma-access-scoped.md`** (38 pp), `sec-int-…-pb-deployment.md` (17) |
| 4 | **Authentication Gateway** | Forward proxy that gives the IdP **known source IPs** for PB conditional-access; talks to Identity Providers | [prisma-access-browser › ip-based-enforcement-using-an-authentication-gateway](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway) | `prisma-access-browser-docs.md` (15), `prisma-browser-entra-id-references.md`, **`cloud-identity.md`** |
| 5 | **Direct Internet Access (DIA)** | Internet/SaaS traffic egresses **direct**, not via Prisma Access (the "private-apps-only" routing choice) | [prisma-access › default-routes-with-traffic-steering-direct-to-internet-example](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-advanced-deployments/service-connection-advanced-deployments/use-traffic-forwarding-rules-with-service-connections/default-routes-with-traffic-steering-direct-to-internet-example) | **`prisma-access-scoped.md`** (traffic-steering, 27 pp), `sec-int-…-pb-prisma-access-design.md` (9) |

## Component detail

### 1. Explicit Proxy (EP) — the on-ramp
The internal PAC file directs **private-application** traffic to the Prisma Access
Explicit Proxy. From the EP, Prisma Access reaches the private apps via one of the two
off-ramps below. Deployment/onboarding specifics for Prisma Browser are in
[Onboard the Prisma Browser](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding).
Deeper PA reference (auth methods for explicit proxy, internet-traffic restriction,
GlobalProtect interop) is now in **`prisma-access-scoped.md`** — the
`mobile-users-explicit-proxy` sub-tree (68 pages).

### 2. Service Connection — off-ramp via iBGP
Carries traffic from Prisma Access to the customer's private applications using iBGP
routing. Full planning/config reference is now in **`prisma-access-scoped.md`**:
`prisma-access-service-connections` (7 pages) + `service-connection-advanced-deployments`
incl. traffic-steering (27 pages).

### 3. ZTNA Connector — off-ramp via DNS proxy
The **Prisma Browser Connector** ("ZTNA Connector" in the diagram) provides secure
access to private apps via a DNS-proxy path. Covered locally in
`prisma-access-browser-docs.md` (*Prisma Browser Connector for Secure Access to
Private Apps*) and the deployment PDFs; monitored in SCM via
[monitor-data-centers-ztna-connectors](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/insights-scm/monitor-data-centers/monitor-data-centers-ztna-connectors)
(already pulled to `scm-referenced-pages.md`).

### 4. Authentication Gateway — known source IPs for conditional access
Per the docs, the Authentication Gateway **"serves as a forward proxy"** with a set of
**egress IP addresses**, so an IdP's conditional-access policy can trust traffic by
source IP (**IP-Based Enforcement**). Offered as a **Shared** Authentication Gateway
(legacy) or **Dedicated** Authentication Gateways. This is the bridge to the Identity
Providers (Okta / Ping / **Entra ID**). See the dedicated page above, plus the Entra
specifics already extracted to `prisma-browser-entra-id-references.md` and
`strata-cloud-manager-entra-id-integration.md` (Cloud Identity Engine → *Configure
Azure as an IdP*).

### 5. Direct Internet Access (DIA) — the bypass
DIA is the *routing decision* that internet/SaaS-bound traffic egresses directly from
the browser instead of being sent into Prisma Access. There is no page literally titled
"Direct Internet Access", but the **traffic-steering** mechanism that implements it is
now fully captured in **`prisma-access-scoped.md`** — the
`service-connection-advanced-deployments › use-traffic-forwarding-rules-with-service-connections`
sub-tree, including the dedicated page **"Default Routes with Traffic Steering Direct to
Internet Example"** plus *configure-traffic-steering*, *traffic-steering-requirements*,
and *default-routes*. The PB-side design rationale stays in
`sec-int-and-private-apps-pb-prisma-access-design.md` / `…-deployment.md`.

## Identity provider integration (the Auth Gateway → IdP edge)
- **Entra ID (Prisma Browser side):** `prisma-browser-entra-id-references.md` — IP-Based
  Enforcement via Authentication Gateway, Automatic Web App Sign-In with Entra ID, macOS support.
- **Entra ID (SCM / Cloud Identity Engine side):** `strata-cloud-manager-entra-id-integration.md`
  — *Configure Azure as an IdP in the Cloud Identity Engine* (SAML 2.0), alongside Okta/Ping/Google.

## Documentation status (library crawl complete — 2026-06-27)
| Component | Status | Where |
|---|---|---|
| Explicit Proxy | ✅ Full | `prisma-access-scoped.md` (mobile-users-explicit-proxy, 68 pp) + PB PDFs |
| Service Connection | ✅ Full | `prisma-access-scoped.md` (service-connections + advanced, 34 pp) + PB PDFs |
| ZTNA Connector | ✅ Full | PB docs + `prisma-access-scoped.md` (ztna-connector, 38 pp) |
| Authentication Gateway | ✅ Full | PB dedicated page + `cloud-identity.md` (IdP depth) + Entra files |
| Direct Internet Access | ✅ Resolved | `prisma-access-scoped.md` traffic-steering "direct-to-internet" pages |

## Library (full reference, crawled 2026-06-27)
| File | Pages | Notes |
|---|---|---|
| `cloud-identity.md` | 82 | Cloud Identity Engine — incl. Entra ID / Azure AD directory + IdP setup |
| `strata-logging-service.md` | 217 | Strata Logging Service — log storage/forwarding (largest set) |
| `common-services.md` | 110 | Tenant/subscription mgmt (licensing) + Identity & Access |
| `prisma-access-scoped.md` | 143 | The 5 routing-component sub-trees (EP, Service Connection, ZTNA, auth, traffic-steering/DIA) |

> All four were crawled via `crawl_docset.py` (TOC-json discovery ∪ BFS, on-disk cache,
> gentle rate-limiting). 557 pages total; 0 HTML leakage, 0 dead in-page links.

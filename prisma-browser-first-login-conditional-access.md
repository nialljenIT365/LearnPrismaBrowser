# Prisma Browser — First Login & Conditional-Access "Bootstrap" (Findings Note)

> ⚠️ **This is a FINDINGS / ANALYSIS note, not a verbatim documentation page.** It mixes
> sources, each labelled:
> - **[OFFICIAL]** — from `docs.paloaltonetworks.com` (authoritative).
> - **[COMMUNITY/SUPPORT]** — from Palo Alto **LIVEcommunity** threads and user-reported
>   support outcomes. **Not official documentation. Treat as unverified, version-specific,
>   and subject to change.** Do not present these as official Palo Alto guidance.
>
> Compiled 2026-06-27 to fill a gap the rest of this corpus does not cover.

## The question

If conditional access (CA) trusts **only** the Prisma Browser Authentication Gateway's
egress IPs (an Entra **Named Location**), how does a user's **first** sign-in /
enrollment succeed — before the browser is routing IdP traffic through the gateway?
Is there a documented **"bootstrap exclusion"** or **first-login CA carve-out**?

## Finding 1 — There is NO documented first-login bootstrap exclusion **[OFFICIAL]**

Verified directly against the live pages (2026-06-27): neither the IP-based-enforcement
page nor the sign-in-rules page mentions first login, initial sign-in, enrollment,
policy staging, or any CA exclusion. The IP-enforcement page stops at *"toggle
**Authentication Traffic Routing** on, then validate"* with no guidance for the initial
sign-in.

- *Source (official):* <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway>
- *Source (official):* <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-sign-in-rules>

## Finding 2 — Why no carve-out is documented: the architecture sidesteps it **[OFFICIAL]**

The onboarding flow implies the first sign-in already egresses from the gateway IP, so
no exclusion is needed:
- The Prisma Browser **installer is distributed via MDM** — obtaining/installing the
  browser does **not** require an Entra sign-in, so there is no pre-install auth that a
  CA policy could block.
- Once launched, the browser **routes IdP authentication traffic through the gateway**;
  the user simply enters work email → password → **Sign in**. So the *first* in-browser
  sign-in also comes from the gateway egress IP and satisfies the Named-Location CA rule.
- Prerequisite: the **Cloud Identity Engine** and an **authentication profile** must be
  configured before users can sign in.

- *Source (official):* <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding>
- *Source (official):* <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement>

> **Inference (not stated directly in the docs):** Because the installer comes via MDM and
> the browser routes IdP auth through the gateway from launch, Palo Alto's design appears
> to assume no first-login exclusion is required. The corpus contains no statement
> confirming or denying a true cold-start case (e.g. a user who must complete an Entra
> sign-in **outside** Prisma Browser before the gateway is in the path). If such a case
> exists in your environment, it is **undocumented** — validate with Palo Alto support.

## Finding 3 — Where the carve-out actually bites: native desktop apps **[COMMUNITY/SUPPORT]**

The real-world failure reported by users is **not** first login — it is **native
desktop apps (Outlook / Teams)** whose embedded authentication windows (Edge
**WebView2**, an embedded HTML page) do **not** open inside Prisma Browser, so they do
not egress from the gateway IP and therefore **fail** a CA policy that requires the
Prisma Browser Named Location.

Reported outcome (a user + Palo Alto support, **not** official docs):
- *"there [is] nothing we can do about this authentication window as it is an embedded
  html page."*
- Working resolution: **restrict the list of applications the CA policy applies to** —
  i.e. **exclude the problematic native apps** (Outlook/Teams desktop) from the
  Prisma-Browser-required CA policy. This is an **application-scoped carve-out**, not a
  first-login one.
- Palo Alto's framing: web app versions work with PB enforcement; native-app embedded
  auth is **"primarily a Microsoft issue,"** with **no official workaround**.

- *Source (community/support):* <https://live.paloaltonetworks.com/t5/prisma-access-discussions/prisma-browser-conditional-access-issue-with-outlook-app/td-p/1243310>

## Bottom line

| Question | Answer | Basis |
|---|---|---|
| Documented first-login bootstrap exclusion / CA carve-out? | **No** | [OFFICIAL] — verified absent |
| Does first in-browser login bypass the gateway to reach Entra directly? | **No** — it routes *through* the gateway from launch (so the Named-Location CA is satisfied) | [OFFICIAL] — inferred from onboarding flow |
| Any carve-out that exists in practice? | **App-scoped only** — exclude native Outlook/Teams (embedded-auth) apps from the CA policy | [COMMUNITY/SUPPORT] — unofficial |
| True cold-start (Entra auth required outside PB before gateway is in path)? | **Undocumented** — confirm with Palo Alto support | gap |

## Sources

**Official (docs.paloaltonetworks.com):**
- IP-Based Enforcement Using an Authentication Gateway — <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway>
- IP Based Enforcement (overview) — <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement>
- Manage Prisma Browser Sign-in Rules — <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-sign-in-rules>
- Onboard the Prisma Browser — <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding>
- Manage Prisma Browser Requests to Bypass Policy Rules — <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-requests>

**Community / support (NOT official):**
- LIVEcommunity — Prisma Browser conditional access issue with Outlook app — <https://live.paloaltonetworks.com/t5/prisma-access-discussions/prisma-browser-conditional-access-issue-with-outlook-app/td-p/1243310>

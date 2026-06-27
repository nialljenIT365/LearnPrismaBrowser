# Prisma Browser — Licensing & Onboarding (Setup Prerequisites)

> Compiled 2026-06-27. The upstream prerequisites that precede browser onboarding —
> **license → activate → register product → onboard** — pulled from three doc-sets so the
> Prisma Browser corpus is complete end-to-end (license → activate → onboard → deploy → configure).

**Contents**
1. **Prisma Access — License & Activation** (47 pages) — `prisma-access/activation-and-onboarding`
2. **Strata Cloud Manager — Onboarding, Settings & Product Activation** (53 pages) — `strata-cloud-manager/activation-and-onboarding` + `getting-started/settings`
3. **Cloud Identity Engine — Activation & Licensing** (13 pages) — `identity/activation-and-onboarding`

> Each part keeps its own Table of Contents and per-page `*Source:` links. Anchors are
> namespaced (`pa-`/`scm-`/`cie-`) so in-page links never collide across parts.

---

# Prisma Access - Activation and Onboarding

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access on 2026-06-27. 47 pages. Absolute URLs.

> Scoped to: /activation-and-onboarding

## Table of Contents

  - [Your Prisma Access License](#pa-your-prisma-access-license)
    - [Remote Networks—High Performance Site-Based Licensing](#pa-remote-networkshigh-performance-site-based-licensing)
    - [Validate Your License](#pa-validate-your-license)
    - [All Available Apps and Services](#pa-all-available-apps-and-services)
      - [Cheat Sheet: ADEM with Prisma Access](#pa-cheat-sheet-adem-with-prisma-access)
      - [Cheat Sheet: IoT Security with Prisma Access](#pa-cheat-sheet-iot-security-with-prisma-access)
      - [Cheat Sheet: Enterprise DLP with Prisma Access](#pa-cheat-sheet-enterprise-dlp-with-prisma-access)
      - [Cheat Sheet: SaaS Security with Prisma Access](#pa-cheat-sheet-saas-security-with-prisma-access)
      - [Cheat Sheet: URL Filtering with Prisma Access](#pa-cheat-sheet-url-filtering-with-prisma-access)
      - [Cheat Sheet: Remote Browser Isolation](#pa-cheat-sheet-remote-browser-isolation)
    - [Reset or Transfer Your Prisma Access (Managed by Panorama) License](#pa-reset-or-transfer-your-prisma-access-managed-by-panorama-license)
      - [Reset Your Prisma Access (Managed by Panorama) License](#pa-reset-your-prisma-access-managed-by-panorama-license)
      - [Transfer Or Update Your Prisma Access (Managed by Panorama) License](#pa-transfer-or-update-your-prisma-access-managed-by-panorama-license)
    - [Verify Your Prisma Access (Managed by Panorama) Account](#pa-verify-your-prisma-access-managed-by-panorama-account)
  - [Activate Your Prisma Access License](#pa-activate-your-prisma-access-license)
    - [Prisma Access (Managed by Strata Cloud Manager) and Add-Ons License Activation](#pa-prisma-access-managed-by-strata-cloud-manager-and-add-ons-license-activation)
      - [Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Services](#pa-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-services)
        - [Allocate Licenses for Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Services](#pa-allocate-licenses-for-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-services)
        - [Plan Service Connections for Prisma Access (Managed by Strata Cloud Manager) Through Common Services](#pa-plan-service-connections-for-prisma-access-managed-by-strata-cloud-manager-through-common-services)
        - [Add Additional Locations for Prisma Access (Managed by Strata Cloud Manager) Through Common Services](#pa-add-additional-locations-for-prisma-access-managed-by-strata-cloud-manager-through-common-services)
        - [Enable Available Add-Ons for Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Servicess](#pa-enable-available-add-ons-for-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-servicess)
      - [Search for Subscription Details Through Common Services](#pa-search-for-subscription-details-through-common-services)
      - [Share a License for Prisma Access (Managed by Strata Cloud Manager) Through Common Services](#pa-share-a-license-for-prisma-access-managed-by-strata-cloud-manager-through-common-services)
      - [Increase Subscription Allocation Quantity Through Common Services](#pa-increase-subscription-allocation-quantity-through-common-services)
    - [Prisma Access (Managed by Panorama) and Add-Ons License Activation](#pa-prisma-access-managed-by-panorama-and-add-ons-license-activation)
      - [Activate a License for Prisma Access (Managed by Panorama) and Add-Ons Through Common Services](#pa-activate-a-license-for-prisma-access-managed-by-panorama-and-add-ons-through-common-services)
      - [Activate a License for Prisma Access (Managed by Panorama) China Through Common Services](#pa-activate-a-license-for-prisma-access-managed-by-panorama-china-through-common-services)
    - [Activate a License for Prisma Access (Managed by Strata Cloud Manager) and Prisma SD-WAN Bundle Through Common Services](#pa-activate-a-license-for-prisma-access-managed-by-strata-cloud-manager-and-prisma-sd-wan-bundle-through-common-services)
  - [Prisma Access Onboarding Workflow](#pa-prisma-access-onboarding-workflow)
    - [Onboarding Workflow for Prisma Access GlobalProtect Deployments](#pa-onboarding-workflow-for-prisma-access-globalprotect-deployments)
    - [Onboarding Workflow for Prisma Access Explicit Proxy Deployments](#pa-onboarding-workflow-for-prisma-access-explicit-proxy-deployments)
    - [Onboarding Workflow for Remote Networks—High Performance With Site-Based Licensing](#pa-onboarding-workflow-for-remote-networkshigh-performance-with-site-based-licensing)
    - [Onboarding Workflow for Prisma Access Service Connections](#pa-onboarding-workflow-for-prisma-access-service-connections)
    - [Onboarding Workflow for Prisma Access ZTNA Connector](#pa-onboarding-workflow-for-prisma-access-ztna-connector)
- [Prisma Access Activation and Onboarding](#pa-prisma-access-activation-and-onboarding)
        - [First Time Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation](#pa-first-time-prisma-access-managed-by-strata-cloud-manager-and-add-ons-activation)
        - [Return Visit Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation](#pa-return-visit-prisma-access-managed-by-strata-cloud-manager-and-add-ons-activation)
      - [Strata Cloud Manager](#pa-strata-cloud-manager)
      - [Panorama](#pa-panorama)
        - [Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Strata Cloud Manager)](#pa-cheat-sheet-enterprise-dlp-with-prisma-access-managed-by-strata-cloud-manager)
        - [Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Panorama)](#pa-cheat-sheet-enterprise-dlp-with-prisma-access-managed-by-panorama)
        - [Cheat Sheet: Remote Browser Isolation (Strata Cloud Manager)](#pa-cheat-sheet-remote-browser-isolation-strata-cloud-manager)
        - [Cheat Sheet: Remote Browser Isolation (Panorama)](#pa-cheat-sheet-remote-browser-isolation-panorama)
        - [Cheat Sheet: SaaS Security with Prisma Access (Managed by Strata Cloud Manager)](#pa-cheat-sheet-saas-security-with-prisma-access-managed-by-strata-cloud-manager)
        - [Cheat Sheet: SaaS Security with Prisma Access (Managed by Panorama)](#pa-cheat-sheet-saas-security-with-prisma-access-managed-by-panorama)
      - [Validate Your License (Strata Cloud Manager)](#pa-validate-your-license-strata-cloud-manager)
      - [Validate Your License (Prisma Access (Managed by Panorama))](#pa-validate-your-license-prisma-access-managed-by-panorama)

---

<a id="pa-your-prisma-access-license"></a>

### Your Prisma Access License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license>*

Learn about Prisma Access licenses.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

Prisma Access offers a licensing model that enables you to implement and use the
capabilities of Prisma Access aligned to your business needs in a way that delivers
the fastest return on investment. Whether your applications are migrating to the cloud,
your users are working from anywhere, or if you're looking to gain operational
efficiencies, Prisma Access offers the relevant type of license for your deployment.

You can choose from the following license editions (more details are in the [Prisma Access Licensing Guide](https://www.paloaltonetworks.com/resources/datasheets/prisma-access-licensing-guide)):

- **Secure Web Gateway (Secure Internet)**
- **ZTNA (secure private apps)**
- **Enterprise (Secure all apps)**

Some Prisma Access SKUs are [End-Of-Sale (EoS)](https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-sale); if your deployment uses one
of these SKUs, Palo Alto Networks [migrates these SKUs](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/license-migration) to alternative SKUs.

Your Prisma Access license edition determines the security capabilities that are
available to you. If you use any capability in security rules or profiles that’s
unsupported based on your license type, Prisma Access removes those configurations
and those capabilities are not enforced in your Prisma Access tenants until you
update Prisma Access with a license edition that supports those capabilities. To
find the capabilities included with your license, refer to the [Prisma Access](https://www.paloaltonetworks.com/resources/datasheets/prisma-access-licensing-guide).

Prisma Access uses *units* in for Mobile User licenses.

- For mobile user deployments, a *unit* is defined as one mobile user. When
  you assign units in Prisma Access from your Mobile User license, each unit
  enables a mobile user to utilize Prisma Access—GlobalProtect, Prisma
  Access—Explicit Proxy, or both GlobalProtect and Explicit Proxy.

  Mobile users who access apps using [Clientless VPN](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/configure-clientless-vpn-prisma-access) are also counted as a
  unit for licensing purposes.
- For remote networks deployments, a *unit* is defined as 1 Mbps.

When a Prisma Access license expires, you can still use the service and collect
logs for 15 days after license expiration. You can’t make changes to the
configuration. Prisma Access shuts down its instances 15 days after license
expiration and completely deletes the instances and tenants 30 days after license
expiration.

#### License Enforcement for Prisma Access Mobile User Deployments

Learn how mobile user (GlobalProtect and Explicit Proxy) licenses are counted in
Prisma Access.

Prisma Access uses these enforcement policies for Mobile User licenses:

- Though there is no strict policing of the mobile user count, the service does
  track the number of unique users over the last 30 days to ensure that you
  have purchased the proper license tier for your user base, and stricter
  policing of the user count may be enforced if continued overages occur.
- A Prisma Access Mobile User license enables you to use both GlobalProtect
  and Explicit Proxy connect methods. With a single Mobile User license, the
  user can connect with GlobalProtect, Explicit Proxy, or both.
- If you use Prisma Access for users—GlobalProtect, the GlobalProtect app
  is required on each [supported](https://docs.paloaltonetworks.com/compatibility-matrix/globalprotect/where-can-i-install-the-globalprotect-app.html) endpoint. The
  GlobalProtect app isn’t required for Mobile Users—Explicit Proxy
  deployments.

#### Other Licenses to Use With Prisma Access (Managed by Strata Cloud Manager)

These licenses are required with Prisma Access (Managed by Strata Cloud Manager):

- **Strata Cloud Manager
  (Required)**—Strata Cloud Manager supports two licensing
  tiers—Essentials and Pro. Essentials is [available for free](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support) with a Prisma Access and Pro is available as an add-on. Both licenses
  unlock a range of network security features and management tools to optimize
  NGFW and Prisma Access operations.
- **Strata Logging Service (Required)**—Prisma Access logs are stored in Strata Logging Service, and so
  Prisma Access requires you to also have a Strata Logging Service license. It’s a good idea to activate Strata Logging Service before you begin activating Prisma Access.
  If you try to activate Prisma Access without first activating Strata Logging Service, Prisma Access will guide you to activate
  Strata Logging Service before allowing you to continue Prisma Access activation. Your Strata Logging Service instance
  and Prisma Access instance must be deployed in the same region.
- **Cloud Identity Engine (Directory Sync)**—Cloud Identity Engine gives Prisma Access
   [read-only access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access) to your Active
  Directory information, so that you can easily set up and manage security and
  decryption policies for users and groups. Cloud Identity Engine is free and
  does not require a license to get started.
- **SaaS Security API**—Integrate SaaS Security API with Prisma Access for
  Clientless VPN and authentication support.
- **Remote Browser Isolation (RBI)**—Integrate [RBI](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi.html) with Prisma Access to provide a browsing environment that
  isolates all malware, including zero-day attacks that result from browsing
  and web activity, away from your end users and your network.

#### Other Licenses to Use with Prisma Access (Managed by Panorama)

See the other licenses that are required for Prisma Access (Managed by Panorama).

In addition to the Prisma Access licenses, to run the service you must also have
the following licensed components:

- **Panorama**—You deploy and manage Prisma Access using the Cloud
  Services plugin for Panorama. To use this plugin, you must have Panorama
  with a valid support license. See the [Palo Alto Networks Compatibility
  Matrix](https://docs.paloaltonetworks.com/compatibility-matrix/panorama/plugins.html#id17C8A0Y0M9I) for the Panorama versions that are supported with the
  Cloud Services plugin. When you license the Prisma Access components,
  you must tie the auth code to a licensed Panorama serial number.
- **Strata Logging Service **(Required)****—The Prisma Access infrastructure forwards all logs to [Strata Logging Service](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started). You can
  view the Prisma Access logs, ACC, and reports directly from Panorama for
  an aggregated view into your remote network and mobile user traffic. To
  enable logging for Prisma Access, you must purchase a Strata Logging Service license.
- **Cloud Identity Engine (Directory Sync)**—Cloud Identity Engine gives Prisma Access
   [read-only access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access) to your Active
  Directory information, so that you can easily set up and manage security and
  decryption policies for users and groups. Cloud Identity Engine is free and
  does not require a license to get started.

#### Prisma Access Add-On Licenses

Learn about the add-on licenses that are provided by Prisma Access.

You can add the following capabilities to use with Prisma Access as an add-on
license:

- [App Acceleration](https://docs.paloaltonetworks.com/prisma-access/administration/app-acceleration-in-prisma-access)
- [Autonomous Digital Experience
  Management (ADEM)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-adem-with-prisma-access.html#idedd37c14-dd97-4301-a747-fed0cb047c19)
- [DLP with Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access.html#tabs-id2b618325-b9fc-42aa-860f-7b68a03704a7)
- [IoT Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-iot-with-prisma-access.html#id54c8e33d-93d2-4c6d-83d7-a6876f54dcd6)
- [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline.html)
- [ZTNA Connector](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access)

---

<a id="pa-remote-networkshigh-performance-site-based-licensing"></a>

#### Remote Networks—High Performance Site-Based Licensing

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/remote-networks-site-based-licensing>*

Learn how site-based licensing works starting with Prisma Access 6.0.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license  Minimum [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license) 6.0   version required. |

Prisma Access 6.0 introduces site-based licensing for Remote Networks, enhancing
flexibility and [simplifying deployment](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) for branch sites. This
licensing model lets you allocate your sites with predefined bandwidth capacities,
ranging from 25 Mbps to 2.5 Gbps. By moving away from aggregate bandwidth-based
licensing, you can more easily estimate and allocate resources for your remote
locations.

With site-based licensing, you no longer need to preallocate bandwidth to specific Prisma Access compute regions or configure redundancy manually. This approach
reduces complexity in network planning and provides a more straightforward way to manage
and scale your branch sites. Using this model, you can focus on the number and types of
sites needed rather than estimating total bandwidth consumption across your network.
Site-based licensing in Prisma Access aligns better with your organizational
structure and growth plans, providing a more intuitive and scalable approach to securing
and connecting your branch sites.

Some features and
configurations [are not supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) for site-based licensing.

Site-based licensing introduces several key enhancements to improve your organization's
Prisma Accesss experience:

- **Support for Large Branch Offices**—With Large (1 Gbps) and X-Large (2.5
  Gbps) site types, you can now effectively secure and connect large branch
  locations with high-bandwidth requirements.
- **Egress NAT Support**—All site licenses include egress NAT capabilities,
  allowing for more flexible network address translation configurations at your
  remote locations.
- **Regional Redundancy Support**—Your site license now [includes regional redundancy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) at no additional charge,
  eliminating the need for separate redundancy configuration and providing
  enhanced reliability for your branch connections.

Site-based licensing offers you the following site types:

- Very Small (up to 25 Mbps)
- Small (up to 50 Mbps)
- Medium (up to 250 Mbps)
- Large (up to 1 Gbps)
- X-Large (up to 2.5 Gbps)

When implementing site-based licensing, keep the following considerations in mind:

- **Bandwidth Aggregation**—Licensed site bandwidth represents the aggregation of
  both ingress and egress bandwidth at each location.
- **Bandwidth Enforcement**—Licensed site bandwidth is enforced according to the
  selected site type, with 10% oversubscription allowed. You can experience degraded
  performance if a site exceeds its licensed bandwidth limit.
- **License Combination Restrictions**—To achieve higher throughput exceeding
  2.5Gbps at a branch location, you can onboard a remote site as multiple individual
  2.5Gbps sites, enabling high-bandwidth and secure internet access. For instance, you
  can onboard a large campus as two separate 2.5Gbps sites through Prisma Access to
  facilitate 5Gbps internet connectivity. However, this deployment model does not
  support access to private applications.

---

<a id="pa-validate-your-license"></a>

#### Validate Your License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license>*

Learn how to validate your Prisma Access license type,
and the services and support it includes.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

Learn more about the apps and services that are natively built in or are integrated with
Prisma Access and how to validate your Prisma Access license. Some apps and services are
supported based on license type. The Prisma Access flexible licensing scheme enables you
to purchase just what you need to secure your remote networks and mobile users. You can
purchase Prisma Access licenses based on your organization's deployment method, the
edition needed, and location. You can check what’s supported with your license directly
in Prisma Access. You can also purchase optional add-ons. After you verify your license
details, you can start configuring Prisma Access.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management.html#id7c606868-9216-4e2f-bf20-00740d888cd4)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama.html#idd917c1b3-0181-4d19-978c-11ea4f25948e)

#### Validate Your License (Strata Cloud Manager)

Validate your license and what’s supported with it directly
in Prisma Access (Managed by Strata Cloud Manager).

Here’s how to validate your Prisma Access license type, and the services and support it
includes.

You can also double-check that your configuration is compliant with your license coverage; the
License Compliance widget shows you if there are any areas
where your license coverage isn’t aligned with your configuration, so that you can
identify where fixes need to be made. Validate your license and what’s supported with it
directly in Prisma Access (Managed by Strata Cloud Manager). Go to ConfigurationNGFW and Prisma AccessOverviewLicense.

|  |  |
| --- | --- |
|

**VALIDATE YOUR LICENSE** To validate your license information, go to ConfigurationNGFW and Prisma AccessConfiguration ScopePrisma AccessOverviewLicense. |  |

|

**CHECK LICENSE COMPLIANCE**: See if there are any conflicts between your configuration and your license support. For example, this might happen if you change your license type, and a configuration that was previously valid, is no longer supported with the new license type. If you see any issues here:  1. Select the failure to see what needs to be fixed. 2. Do a **License Check** to validate your fixes. |  |

#### Validate Your License (Prisma Access (Managed by Panorama))

Learn how to determine the Prisma Access license type
you have by checking the Panorama UI.

Some license requirements, such as the requirements you need to [enable tenants in a multitenant configuration](https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/multitenancy-configuration-overview),
are dependent on the type of Prisma Access license you have. To determine your
license type, select PanoramaLicenses and find the information in the Prisma Access area.

Licenses available after November 17, 2020 include the license Edition and
provide you with the type of Prisma Access Locations you
can deploy (either Local or Worldwide locations).

![]()

Licenses available before November 17, 2020, contain the words GlobalProtect
Cloud Service in the license areas and are divided by
remote networks, mobile users, or Clean Pipe.

![]()

---

<a id="pa-all-available-apps-and-services"></a>

#### All Available Apps and Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services>*

Many key Palo Alto Networks apps and services are natively
built-in or are integrated with Prisma Access (Managed by Strata Cloud Manager).
See what’s available to you.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

Many key Palo Alto Networks apps and services
are natively built-in or are integrated with Prisma Access (Managed by Strata Cloud Manager). Some apps and services are available for all Prisma
Access users; support for others might depend on your license type.

Here’s a list of all the apps and services that are available
with Prisma Access.

|

Apps and Services that Are Available with Prisma Access | | |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**Security Services** | **URL Filtering** | URL Filtering (URL Access Management) gives you a way to control not only web access, but how users interact with online content. PAN-DB—the URL Filtering cloud— classifies sites based on content, features, and safety, and you can enforce your security policy based on these URL categories. You can also prevent credential phishing theft by tightly controlling the types of sites to which users can enter their corporate credentials.   - [Cheat Sheet: URL Filtering](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-url-filtering-with-prisma-access.html) with Prisma Access |

|

| **DNS Security** | DNS Security is a continuously evolving threat prevention service designed to protect and defend your network from advanced threats using DNS. By leveraging advanced machine learning and predictive analytics, the service provides real-time DNS request analysis and rapidly produces and distributes DNS signatures that are specifically designed to defend against malware using DNS for C2 and data theft. Combined with an extensible cloud architecture, it provides access to a scalable threat intelligence system to keep your network protections up to date.   - [DNS for Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/dns-for-prisma-access) |

|

| **Threat Prevention** | Threat Prevention defends your network against both commodity threats—which are pervasive but not sophisticated—and targeted, advanced threats perpetuated by organized cyber adversaries. Threat Prevention includes comprehensive exploit, malware, and command-and-control protection, and Palo Alto Networks frequently publishes updates that equip Prisma Access with the very latest threat intelligence. The Palo Alto Networks Threat Vault is built directly in to Prisma Access cloud management so you can easily check threat coverage.   - [Set Up Antivirus, Anti-Spyware,   and Vulnerability Protection](https://docs.paloaltonetworks.com/content/techdocs/en_US/advanced-threat-prevention/administration/configure-threat-prevention/set-up-antivirus-anti-spyware-and-vulnerability-protection.html) |

|

| **Advanced WildFire** | WildFire and Antivirus protects against malware concealed in files, executables, and email links.  Prisma Access (Managed by Strata Cloud Manager) forwards files, executables, and email links to WildFire™ cloud service for analysis, and also performs inline ML analysis for certain files. Advanced WildFire analyzes files and email links to detect threats and create protections to block malware. When WildFire identifies a zero-day threat, it globally distributes protection for that threat in under five minutes.   - [Configure Advanced WildFire Analysis](https://docs.paloaltonetworks.com/advanced-wildfire/administration/configure-advanced-wildfire-analysis) |

|

**Add-On Licenses** | **SaaS Security Inline** | [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-for-prisma-access.html) is built-in to Prisma Access (Managed by Strata Cloud Manager) to give you a centralized view of network and CASB security. SaaS Security Inline offers SaaS visibility—[advanced analytics](http://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/view-data.html) and [reporting](http://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)—so that your organization has the insights to understand the data security risks of sanctioned and unsanctioned SaaS application usage on your network.   - [Cheat Sheet: SaaS Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access.html) with Prisma Access |

|

**Add-On Licenses** | **App Acceleration** | App Acceleration directly addresses the causes of poor app performance and acts in real-time to mitigate them. The add-on securely optimizes each individual user session to drive the highest possible throughput, dramatically improving the user experience for Prisma Access GlobalProtect and Remote Network users. Additionally, it enriches AI-Powered ADEM with RUM (Real User Metrics) so you can easily see the performance boost in Strata Cloud Manager.   - [App Acceleration in Prisma   Access](https://docs.paloaltonetworks.com/prisma-access/administration/app-acceleration-in-prisma-access) |

|

| **Remote Browser Isolation** | Remote Browser Isolation is a service that isolates and transfers browsing activity away from your users' devices and corporate networks to an outside entity such as Prisma Access, which secures and isolates potentially malicious code and content within their platform, and separates any threats from direct connections to end-user devices and networks.   - [Cheat Sheet: Remote Browser Isolation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi.html#tabs-cheat-sheet-rbi) |

|

| **Autonomous DEM** | Provides native, end-to-end visibility and insights for all user traffic in your Secure Access Service Edge (SASE) environment. Autonomous DEM functionality is natively integrated into the GlobalProtect app and Prisma Access and therefore does not require you to deploy any additional appliances or agents. You can quickly isolate the source of digital experience problems, and simplify remediation.   - [Cheat Sheet: ADEM](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-adem-with-prisma-access.html) with Prisma Access |

|

| **AI-Powered ADEM** | [AI-Powered ADEM](https://docs.paloaltonetworks.com/autonomous-dem/administration) is a Prisma Access add-on license that automates complex IT operations, to increase productivity and reduce time to resolution for issues. AI-Powered ADEM is supported in Cloud Management for all Prisma Access users, regardless of the interface you're using to manage Prisma Access (Prisma Access (Managed by Strata Cloud Manager) or Prisma Access (Managed by Panorama)). If you've enabled AI-Powered ADEM license, then the license is auto enabled for all the compute locations. |

|

| **CASB** | Cloud Access Security Broker (CASB) bundle includes SaaS Security Inline, Enterprise Data Loss Prevention (DLP) Inline, SaaS Security API, Data Loss Prevention (DLP) API, and SaaS Security Posture Management (SSPM). |

|

| **Next-Generation CASB-X** | The [Next-Generation Cloud Access Security Broker](https://docs.paloaltonetworks.com/next-gen-casb) (CASB-X) license contains all the CASB components such as SaaS Security Inline, SaaS Security API, SaaS Security Posture Management (SSPM), and Enterprise DLP. It can be applied on Prisma Access (Managed by Strata Cloud Manager), Prisma Access (Managed by Panorama), and Panorama-Managed Next Generation Firewall (NGFW) devices in a single tenant environment. |

|

| **Prisma SD-WAN** | Prisma SD-WAN is a cloud-delivered service that implements app-defined and autonomous SD-WAN to help you secure and connect your branch offices, data centers, and large campus sites without increasing cost and complexity.  Prisma SD-WAN leverages with a centralized controller-based model, enabling simple deployments at remote offices and data centers. You can view granular application-driven analytics, build a robust policy, and performance-based traffic management of the WAN.   - [Get Started with Prisma SD-WAN](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan/prisma-sd-wan-admin/get-started-with-prisma-sd-wan) |

|

| **Enterprise DLP** | Data loss prevention (DLP) protects sensitive information against unauthorized access, misuse, extraction, or sharing. DLP on Prisma Access enables you to enforce your organization’s data security standards and prevent the loss of sensitive data across mobile users and remote networks.   - [Cheat Sheet: Enterprise DLP](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access.html) with Prisma Access |

|

| **IoT Security** | IoT Security is an on-demand cloud subscription service designed to discover and protect the growing number of connected “things” on your network.   - [Cheat Sheet: IoT Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-iot-with-prisma-access.html) with Prisma Access |

|

| **Net Interconnect** | Net Interconnect for Remote Network-to-Remote Network and Mobile Users-to-Remote Network access (SD-WAN) |

|

| **Private App Access** | Additional Service Connections for Private App Access |

|

**Available for all License Types** | **Strata Logging Service** | All Prisma Access logs are stored in the Strata Logging Service, providing centralized analysis, reporting, andforensics across all users, applications, and locations. In Prisma Access Cloud Management, you can go to [Activity](https://docs.paloaltonetworks.com/prisma-access/administration/monitor/activity-dashboards-and-reports) to view and interact with your logs. You can also use the Strata Logging Service app on the Activation Console to view logs and to set up log forwarding.   - [Get Started with Strata Logging   Service](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake.html) |

|

| **Cloud Identity Engine** | Cloud Identity Engine gives Prisma Access read-only access to your Active Directory information, so that you can easily set up and manage security and decryption policies for users and groups. Cloud Identity Engine also enables certain [Activity](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/user-activity) data and reports.   - [Configure Mobile Users Using   the Cloud Identity Engine](https://docs.paloaltonetworks.com/prisma-access/integration/microsoft-integrations-with-prisma-access/azure-ad-saml-authentication-for-mobile-user-deployments/configure-mobile-users-using-cloud-identity-engine) |

|

| **View and Monitor Prisma Access** | Palo Alto Networks Strata Cloud Manager is an AI-powered Network Security platform. With Strata Cloud Manager, you can easily manage your Palo Alto Networks Network Security infrastructure from a single, streamlined user interface.  You can get comprehensive visibility across your network traffic and for the products and subscriptions you're managing using the [Monitor](https://docs.paloaltonetworks.com/cloud-management/administration/monitor) and [Workflows](https://docs.paloaltonetworks.com/cloud-management/administration/workflows) sections of Strata Cloud Manager and [Monitor Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/monitor/monitor-prisma-access-in-strata) in Strata Cloud Manager. |

|

| **Activity** | Activity gives you monitoring and visibility into your network traffic, and surfaces key findings that you can use to inform policy updates and close enterprise security and user productivity gaps. Activity features include:   - Log   Viewer - Interactive Dashboards - Offline reports for sharing  - [Prisma Access Activity   Dashboards and Reports](https://docs.paloaltonetworks.com/prisma-access/administration/monitor/activity-dashboards-and-reports) |

---

<a id="pa-cheat-sheet-adem-with-prisma-access"></a>

##### Cheat Sheet: ADEM with Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-adem-with-prisma-access>*

Use IoT Security with Prisma Access.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license - [Autonomous DEM](https://docs.paloaltonetworks.com/autonomous-dem.html) add-on   license |

[Autonomous Digital Experience
Management (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-in-prisma-access/autonomous-dem.html) provides native, end-to-end visibility
and performance metrics for real application traffic in your Secure
Access Service Edge (SASE) environment.

###### Get Started

Here’s how to get up and running with ADEM
on Prisma Access.

- Check that your license covers ADEM.

  - [Here’s how to check
    what’s available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license.html#tabs-id87b83135-128a-4f2c-b50b-6030899fb8e1)
- Enable ADEM for your Mobile Users—GlobalProtect and Remote
  Networks deployments.

  - [Enable ADEM in Prisma Access for
    a Mobile Users—GlobalProtect deployment](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-admin/get-started-with-adem/enable-adem-for-mobile-users)
  - [Enable ADEM in Prisma Access for
    a Remote Network deployment](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-admin/get-started-with-adem/enable-adem-for-remote-networks)
- [Manage ADEM mobile users and
  remote sites](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-in-prisma-access/manage-autonomous-dem-users.html).
- [Learn how to use Autonomous DEM
  in Prisma Access](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-in-prisma-access/first-look-at-autonomous-dem-in-prisma-access.html) to troubleshoot common help desk scenarios,
  such as complaints about application access, or end users reporting
  performance issues.

---

<a id="pa-cheat-sheet-iot-security-with-prisma-access"></a>

##### Cheat Sheet: IoT Security with Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-iot-with-prisma-access>*

Use IoT Security with Prisma Access (Managed by Panorama).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) | - Prisma Access license - [IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin) add-on   license |

IoT Security is
an on-demand cloud subscription service designed to discover and
protect the growing number of connected “things” on your network.
Unlike IT devices such as laptop computers that perform a wide variety
of tasks, IoT devices tend to be purpose-built with a narrowly defined
set of functions. As a result, IoT devices generate unique, identifiable
patterns of network behavior. Using machine learning and AI, IoT
Security recognizes these behaviors and identifies every device
on the network, creating a rich, context-aware inventory that’s
dynamically maintained and always up to date.

After it identifies a device and establishes a baseline of its
normal network activities, it continues monitoring its network activity
so it can detect any unusual behavior indicative of an attack or
breach. If it detects such behavior, IoT Security notifies administrators
through security alerts in the IoT Security portal and, depending
on each administrator’s notification settings, through email and
SMS notifications.

You get the same benefits from integrating IoT Security with
Prisma Access as you do from integrating it with next-generation
firewalls. IoT is available as an add-on; after you purchase the
add-on, you [activate your product](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/onboard-iot-security.html) during [Prisma Access installation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license.html#tabs-id52b93ec9-9f3c-4cd9-a064-d884f186e9e7).

###### Get Started

Here’s how to get up and running with IoT Security on Prisma Access.

- Check that your license covers IoT Security.

  [Here’s how to check what’s
  available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license.html#tabs-id87b83135-128a-4f2c-b50b-6030899fb8e1).
- Learn how [Prisma Access works with IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/iot-security-solution/iot-security-solution-structure.html#idddb0e05d-6b2d-4635-97e6-fd588c6f57f1_id9642dfed-4c35-4e98-9ea1-9002a58293c9)
  instead of next-generation firewalls.
- [Integrate IoT Security with Prisma
  Access](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/iot-security-integration-with-prisma-access.html).
- [Check the status of your IoT Security
  Integration with Prisma Access](https://docs.paloaltonetworks.com/iot/iot-security-admin/iot-security-overview/iot-security-integration-status-with-prisma-access.html).

---

<a id="pa-cheat-sheet-enterprise-dlp-with-prisma-access"></a>

##### Cheat Sheet: Enterprise DLP with Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access>*

Data loss prevention (DLP) is a set of tools and processes
that allow you to protect sensitive information against unauthorized
access, misuse, extraction, or sharing.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

Data loss prevention (DLP) protects sensitive information against unauthorized access,
misuse, extraction, or sharing. Enterprise DLP on Prisma Access enables you to enforce
your organization’s data security standards and prevent the loss of sensitive data
across mobile users and remote networks.

Prisma Access integrates its DLP capability to allow Prisma Access (Managed by Strata Cloud Manager) to use
the same DLP capabilities as those used in Panorama and on next-generation firewalls.
This integration provides you with an improved experience that allows you to use the
same DLP patterns, profiles, and rules as those used in next-generation firewalls.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access/cheat-sheet-enterprise-dlp-with-prisma-access-cloud-management.html#id05e49a6c-8ec0-4207-ae24-3fac80eee09b)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access/cheat-sheet-enterprise-dlp-with-prisma-access-panorama.html#idd0b0d205-9e62-45be-a91d-7824a7cb17fa)

##### Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Strata Cloud Manager)

Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data.

**Important:** If you’re already using Panorama to manage Enterprise DLP for next-gen
firewalls, your DLP configuration (data patterns and DLP profiles) in Prisma Access
Cloud Management is read-only; continue to manage DLP from Panorama.

- [Feature Highlights](#pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_g1l_cjs_zxb)
- [Get Started](#pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_tmf_djs_zxb)

<a id="pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_g1l_cjs_zxb"></a>

###### Feature Highlights

**The Data Loss Prevention Dashboard**

In Strata
Cloud Manager, go to ConfigurationData Loss Prevention to configure and manage Enterprise DLP.

Your Enterprise DLP
configuration is shared across the products where you’re using Enterprise DLP.
So, you might see settings here that were configured elsewhere, and some
settings you can configure here can also be leveraged in other
products.

**Predefined + Custom Enterprise DLP Settings**

Enterprise DLP
includes built-in settings that you can use to quickly start protecting your
most sensitive content:

- [Predefined data patterns](https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/data-patterns-and-data-filtering-profiles)
  specify common types of sensitive information (like credit cards and
  social security numbers) that you might want to scan for and protect
- [Predefined DLP Profiles](https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/data-patterns-and-data-filtering-profiles) group
  together data patterns that commonly require the same type of
  enforcement

You can also create custom data patterns and profiles directly in Prisma
Access Cloud Management.

**Investigation for DLP Incidents**

A DLP
incident is generated when traffic matches a DLP data profile on Prisma Access (Managed by Strata Cloud Manager). On the [DLP Incidents dashboard](https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/view-dlp-log-details), you can view
details for the traffic that triggered the incident, such as matched data
patterns, the source and destination of the traffic, the file and file type. Go
to ConfigurationData Loss PreventionDLP Incidents.

**Scanning for Images in Supported File
Formats**

Strengthen your security posture to further prevent accidental
data misuse, loss, or theft with [Optical Character Recognition (OCR)](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/enable-ocr).
OCR allows the DLP cloud service to scan supported file types with images
containing sensitive information that match your Enterprise DLP filtering
profiles.

**Exact Data Matching (EDM)**

[EDM](https://docs.paloaltonetworks.com/enterprise-dlp/enterprise-dlp-admin/configure-enterprise-dlp/configure-exact-data-matching.html) is an advanced detection tool to
monitor and protect sensitive data from exfiltration. Use EDM to detect
sensitive and personally identifiable information (PII) such as social security
numbers, Medical Record Numbers, bank account numbers, and credit card numbers,
in a structured data source such as databases, directory servers, or structured
data files (CSV and TSV), with high accuracy.

**Role-Based Access for
Enterprise DLP**

You can provide role-based access to Enterprise DLP
controls inside Prisma Access (Managed by Strata Cloud Manager):

- **Data Loss Prevention Admin**—Can access Enterprise DLP settings but
  can't push configuration changes to Prisma Access.
- **Data Security Admin**—Can access Enterprise DLP and SaaS Security
  controls, but can't push configuration changes to Prisma Access.

<a id="pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_tmf_djs_zxb"></a>

###### Get Started

Here’s how to get up and running with Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager).

1. Check that Your License Covers Enterprise DLP.

   - [Here’s how to
     check what’s available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management.html#id7c606868-9216-4e2f-bf20-00740d888cd4)
2. Enable Role-Based Access for Enterprise DLP.

   - [Here’s how to add a Data Loss
     Prevention Admin or a Data Security Admin](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/app-access-using-roles)
3. Set Up decryption for Enterprise DLP

   Enterprise DLP supports HTTP/1.1. Some applications, like SharePoint and
   OneDrive, support HTTP/2 for uploads by default. To make applications
   that use HTTP/2 compatible with Enterprise DLP, you’ll need to strip
   ALPN headers from uploaded files.

   In Strata Cloud Manager, go to ConfigurationNGFW and Prisma AccessSecurity ServicesDecryption. Select the Prisma Access
   configuration scope and:

   1. Create a decryption profile, and set it to Strip
      ALPN.

      (Find the Advanced Settings in the
      SSL Forward Proxy section).
   2. Add the decryption profile to an SSL Forward
      Proxy decryption rule.
4. Create a Data Pattern.

   Enterprise DLP data patterns specify what content is sensitive and needs
   to be protected—this is the content you’re filtering. You can create a
   [custom data pattern based on regular
   expressions](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-pattern) or a [data pattern based on file
   properties](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-pattern/create-a-file-property-data-pattern).
5. Create a Data Profile.

   Group data patterns that should be enforced the same way into a data
   profile. You can also use data profiles to specify additional match
   criteria and confidence levels for matching.

   Data profiles can contain regular expression data patterns, [Exact Data Matching (EDM)](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-profile) data
   patterns, or a combination of both.

   [Here’s how to create a data
   profile](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-profile)
6. Create a DLP rule.

   Specify the traffic and file types you want Enterprise DLP to protect.
   Set the action for Enterprise DLP to take when it detects a DLP
   incident.

   [Here’s how to create a DLP
   rule](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/modify-a-dlp-rule-on-prisma-access-cloud-managed)
7. Enable the DLP rule.

   In Prisma Access (Managed by Strata Cloud Manager), a DLP rule is a type of security
   profile. To enable a security profile to enforce traffic: Add it to a
   profile group, and add the profile group to a security rule.

   [Here’s how to enable a security
   profile (including a DLP rule)](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp)

##### Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Panorama)

Enterprise DLP on Prisma Access (Managed by Panorama) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data.

Use DLP with Prisma Access (Managed by Panorama) by [installing the Enterprise DLP plugin](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/install-the-enterprise-dlp-plugin-on-panorama) on the
same Panorama appliance that manages Prisma Access.

If you have migrated from an existing DLP on Prisma Access license to the DLP plugin, the
locations of data patterns and data filtering profiles move in Panorama after the
migration:

- Data
  patterns move from ObjectsCustom ObjectsData Patterns to ObjectsDLPDLP
  Data Patterns.
- Data filtering profiles move from ObjectsSecurity ProfilesData Filtering to ObjectsDLPDLP
  Data Filters.

---

<a id="pa-cheat-sheet-saas-security-with-prisma-access"></a>

##### Cheat Sheet: SaaS Security with Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access>*

Manage your organization’s shadow IT risks, secure SaaS
applications from cloud threats, and ensure compliance across all
SaaS applications.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license - [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security) add-on   license |

Identify cloud-based threats and risky user activity in sanctioned and unsanctioned
apps with SaaS Security Inline.

[SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-for-prisma-access.html) on Prisma Access—both
Panorama Managed and Cloud Managed—provides SaaS visibility so that you can identify
cloud-based threats and risky user activity on sanctioned and unsanctioned SaaS
apps. For Prisma Access (Managed by Strata Cloud Manager) users, SaaS Inline Security is built right in
to give you a centralized view of network and CASB security. It offers SaaS
visibility—which includes [advanced analytics](http://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/view-data.html) and [reporting](http://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)—so that your organization has
the insights to understand the data security risks of sanctioned and unsanctioned
SaaS application usage on your network.

Cloud Access Security Broker (CASB) bundle includes Saas Security Inline, Enterprise
Data Loss Prevention (DLP) Inline, SaaS Security API, Data Loss Prevention (DLP)
API, and SaaS Security Posture Management (SSPM).

Learn how to manage your organization’s shadow
IT risks, secure SaaS applications from cloud threats, and ensure
compliance across all SaaS applications.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access/cheat-sheet-saas-security-with-prisma-access-cloud-management.html#id0f9efe6b-1df5-49c4-bcf2-3961b9be3577)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access/cheat-sheet-saas-security-with-prisma-access-panorama.html#id89a63a43-8f66-48d0-892d-93220d3072bb)

##### Cheat Sheet: SaaS Security with Prisma Access (Managed by Strata Cloud Manager)

Integrate SaaS Security Inline with Prisma Access.

|  |
| --- |
|

**[Here’s everything you need to know](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline) to use SaaS Security with Prisma Access (Managed by Strata Cloud Manager).** |

- [Get Started](#pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id56a654cf-29af-43e4-a823-b0160b0bb289)
- [SaaS Policy Recommendations](#pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id874483ef-e1d9-49fc-b624-f68fc0d8b8c4)

<a id="pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id56a654cf-29af-43e4-a823-b0160b0bb289"></a>

###### Get Started

Here’s how to get up and running with SaaS
Security Inline on Prisma Access (Managed by Strata Cloud Manager):

- Confirm that the SaaS Security add-on
  license is included with your Prisma Access subscription.

  Go to ConfigurationNGFW and Prisma AccessOverview. Select the Prisma Access
  configuration scope.
- If you haven’t already, [activate the SaaS Security Inline
  app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/activate-saas-security-inline-on-prisma-access.html) on the Activation Console.

  After activation, SaaS Security Inline automatically discovers all SaaS
  applications and users and analyzes users’ SaaS activity and usage data
  from your Prisma Access logs that are stored in Strata Logging Service.
- Manage administrator roles and access.

  Go to the Activation Console to provide [roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles)-based access to SaaS
  Security [controls](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) in Prisma Access
  Cloud Management.

  To
  comprehensively manage SaaS Security, users must also be an administrator
  for the SaaS Security Inline app. Jump directly from the Prisma
  Access Cloud Management dashboard to the SaaS Security
  Console to [add](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) SaaS Security Inline
  administrators.
- Explore the SaaS Security dashboard
  in Prisma Access (Managed by Strata Cloud Manager).

  Go to ConfigurationSaaS Security.

  All dashboard views are supported
  directly in Prisma Access (Managed by Strata Cloud Manager). Examine these views
  to [identify risky SaaS applications
  and users](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/identify-risky-saas-apps.html) and [SaaS Security
  Posture Management](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm.html#ide2069884-8ab8-485b-9853-81dca764a5e1). SaaS Security Posture Management (SSPM)
  helps detect and remediate misconfigured settings in sanctioned
  SaaS applications through continuous monitoring.

  ![]()
- Review and share the SaaS Security report.

  SaaS Security Inline includes a SaaS Security report that
  provides a snapshot of application usage with advanced aggregated
  data and views. This report serves as a communication tool between
  your SaaS security team and executive management. You can share
  this on-demand PDF report with your SaaS security team for a periodic
  check-in, or email the report to your executives to highlight the
  SaaS applications in use in your organization and the security risks
  they pose.

  - [Here’s more on the SaaS Security
    report](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/saas-security-inline-report.html#id4f415957-b5c1-4e78-bbd8-7e440186f11c)
  - [Here’s how to generate the SaaS
    Security report in the SaaS Security Inline app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)
- See what else you can do with [SaaS Security and](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-cloud-managed) .

<a id="pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id874483ef-e1d9-49fc-b624-f68fc0d8b8c4"></a>

###### SaaS Policy Recommendations

To gain visibility into and control of SaaS
applications, SaaS Security admins create SaaS rule recommendations
with specific SaaS App-IDs provided by the App-ID Cloud Engine (ACE).

In
Prisma Access (Managed by Strata Cloud Manager), you can now review and choose to
accept the rules that SaaS Security admins recommend. SaaS rule
recommendations are added to your web access policy—you must have [Web Security](https://docs.paloaltonetworks.com/network-security/security-policy/administration/internet-access-rules) enabled to leverage
SaaS rule recommendations.

**Here’s how you can get started
— review the [workflow to review and accept
SaaS policy recommendations](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline) here:**

1. SaaS
   Security admins create SaaS rule recommendations in the SaaS Security
   Inline app or directly in Prisma Access (Managed by Strata Cloud Manager).

   ➡ In Prisma Access (Managed by Strata Cloud Manager), go to ConfigurationSaaS SecurityPolicy Recommendations.

   ![]()
2. You can review and import SaaS rule recommendations.

   Go to ConfigurationNGFW and Prisma AccessSecurity ServicesWeb SecurityWeb Access Policy. Select the Prisma Access
   configuration scope.

   ![]()
3. The SaaS rule recommendations you’ve imported are labeled
   so you can easily identify them.

   ![]()

##### Cheat Sheet: SaaS Security with Prisma Access (Managed by Panorama)

Get up and running with SaaS Security Inline on Prisma Access (Managed by
Panorama).

|  |
| --- |
|

**[Here’s everything you need to know](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-panorama-managed) to use SaaS Security with Prisma Access (Managed by Panorama).** |

###### Get Started

Here’s how to get up and running with SaaS
Security Inline on Prisma Access (Managed by Panorama):

- Confirm that the SaaS Security add-on
  license is included with your Prisma Access subscription.

  Go to PanoramaLicenses to [check what’s available
  with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama.html#idd917c1b3-0181-4d19-978c-11ea4f25948e).
- If you haven’t already, [activate the SaaS Security Inline
  app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/activate-saas-security-inline-on-prisma-access.html) on the Activation Console.

  After activation, SaaS Security Inline automatically discovers all SaaS
  applications and users and analyzes users’ SaaS activity and usage data
  from your Prisma Access logs that are stored in Strata Logging Service.
- Manage administrator roles and access.

  Go to the Activation Console to provide [roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles)-based access to SaaS
  Security [controls](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) in Prisma Access
  Cloud Management.

  To
  comprehensively manage SaaS Security, users must also be an administrator
  for the SaaS Security Inline app. Jump directly from the Prisma
  Access Cloud Management dashboard to the SaaS Security
  Console to [add](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) SaaS Security Inline
  administrators.
- Explore the SaaS Security dashboard
  in Prisma Access (Managed by Panorama).

  Go to Visibility.

  All [dashboard views](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-api/get-started-with-saas-security-api/navigate-to-saas-security-api-in-cloud-management-console) are supported
  directly in Prisma Access (Managed by Strata Cloud Manager). Examine these views
  to [identify risky SaaS applications
  and users](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/identify-risky-saas-apps.html) and [SaaS Security
  Posture Management](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm.html#ide2069884-8ab8-485b-9853-81dca764a5e1). SaaS Security Posture Management (SSPM)
  helps detect and remediate misconfigured settings in sanctioned
  SaaS applications through continuous monitoring.

  ![]()
- Review and share the SaaS Security report.

  SaaS Security Inline includes a SaaS Security report that
  provides a snapshot of application usage with advanced aggregated
  data and views. This report serves as a communication tool between
  your SaaS security team and executive management. You can share
  this on-demand PDF report with your SaaS security team for a periodic
  check-in, or email the report to your executives to highlight the
  SaaS applications in use in your organization and the security risks
  they pose.

  - [Here’s more on the SaaS
    Security report](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/saas-security-inline-report.html#id4f415957-b5c1-4e78-bbd8-7e440186f11c)
  - [Here’s how to generate the
    SaaS Security report in the SaaS Security Inline app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)
- See what else you can do with [SaaS Security and Panorama Managed
  Prisma Access](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-panorama-managed).

---

<a id="pa-cheat-sheet-url-filtering-with-prisma-access"></a>

##### Cheat Sheet: URL Filtering with Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-url-filtering-with-prisma-access>*

URL Filtering—also called *URL Access Management*—gives
you control not only over web access, but how users interact with
online content.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

URL Filtering—also called *URL Access Management*—gives
you a way to control not only web access, but how users interact
with online content.

PAN-DB, the URL Filtering cloud service,
classifies sites into URL categories based on content, features,
and safety, and Prisma Access can enforce your security policy and
decrypt traffic based on the latest site classifications.

- [Configure URL Filtering (URL
  Access Management)](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/configuring-url-filtering/configure-url-filtering)
- [Integrate with a Remote Browser
  Isolation (RBI) Provider](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-features/integrate-with-a-remote-browser-isolation-rbi-provider)

**MORE URL
FILTERING RESOURCES**

These resources give you an idea of the full feature set that URL Filtering offers, and how URL
Filtering features work. However, the topics linked to here describe how the
features are implemented on a next-generation firewall. While the workflows are
different on Prisma Access (Managed by Strata Cloud Manager) (and often, they’re simpler), the
concepts—”how it works”—remains the same.

- [Advanced URL Filtering Homepage](https://docs.paloaltonetworks.com/advanced-url-filtering/administration)
- [URL Filtering Features](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-basics/url-filtering-support)
- [Where and How to Use URL Categories](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-basics/url-filtering-use-cases)

---

<a id="pa-cheat-sheet-remote-browser-isolation"></a>

##### Cheat Sheet: Remote Browser Isolation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi>*

Use Remote Browser Isolation to isolate and transfer browsing activity away from your
end user's managed devices and corporate networks to Prisma Access, which secures and
isolates potentially malicious code and content within their platform.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access 5.0 Innovation - [Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license.html)   with the Mobile User or Remote Networks subscription - [Remote Browser   Isolation](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/activate-a-license-for-remote-browser-isolation) license |

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation) by Palo Alto Networks is a
service that isolates and transfers browsing activity away from your users' devices and
corporate networks to an outside entity such as Prisma Access, which secures and
isolates potentially malicious code and content within their platform, and separates any
threats from direct connections to end-user devices and networks.

Natively integrated with Prisma Access, RBI allows you to easily
apply isolation profiles to your existing security policies. Isolation profiles can
restrict browser controls such as copy and paste actions, keyboard inputs, and sharing
options like uploading, downloading, and printing files to keep sensitive data and
information secure. All traffic in isolation undergoes analysis and threat prevention
provided by Cloud-Delivered Security Services (CDSS) such as Advanced Threat Prevention,
Advanced WildFire, Advanced URL Filtering, DNS Security, and SaaS Security.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi/cheat-sheet-rbi-cloud-management.html#cheat-sheet-rbi-cloud-management)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi/cheat-sheet-rbi-panorama.html#cheat-sheet-remote-browser-isolation-panorama)

##### Cheat Sheet: Remote Browser Isolation (Strata Cloud Manager)

Set up Remote Browser Isolation (RBI) to isolate and transfer browsing activity away from
your users' devices and corporate networks to Prisma Access.

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation) creates a no-code
execution isolation environment for a user's local browser, so that no website code
and files are executed on their local browser.

###### Get Started

Here's how to get up and running with RBI.

1. Check that your license covers RBI.

   [Here's how to check
   what’s available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management.html#id7c606868-9216-4e2f-bf20-00740d888cd4)
2. Configure at least one connection method, otherwise you won't be able to
   enable RBI.

   - [Here's how to configure
     GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
   - [Here's how to configure Explicit
     Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy)
   - [Here's how to configure Prisma
     Access Remote Networks](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks)
   - [Here's how to configure a Remote
     Network—High Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance)
3. Enable decryption so that Prisma Access can decrypt and inspect traffic
   to determine what needs to be isolated according to the policies that you
   configured.

   [Here's how to enable
   decryption](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/security-services/decryption)
4. Configure RBI to set up a theme for the remote
   browsing session, define what browser actions are permitted, and defined
   which website categories that your users access in isolation.

   [Here's how you configure
   RBI](https://docs.paloaltonetworks.com/remote-browser-isolation/administration/configure-rbi)

##### Cheat Sheet: Remote Browser Isolation (Panorama)

Set up Remote Browser Isolation (RBI) to isolate and transfer browsing activity away from
your users' devices and corporate networks to Prisma Access.

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation) creates a no-code
execution isolation environment for a user's local browser, so that no website code
and files are executed on their local browser.

###### Get Started

Here's how to get up and running with RBI.

1. Check that your license covers RBI.

   [Here's how to check what’s
   available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama.html#idd917c1b3-0181-4d19-978c-11ea4f25948e)
2. Configure at least one connection method, otherwise you won't be able to
   enable RBI.

   - [Here's how to configure
     GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
   - [Here's how to configure Explicit
     Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy)
   - [Here's how to configure Prisma
     Access Remote Networks](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks)
   - [Here's how to configure a Remote
     Network—High Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance)
3. Enable decryption so that Prisma Access can decrypt and inspect traffic
   to determine what needs to be isolated according to the policies that you
   configured.

   [Here's how to enable
   decryption](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/security-services/decryption)
4. Configure RBI to set up a theme for the remote
   browsing session, define what browser actions are permitted, and defined
   which website categories that your users access in isolation.

   [Here's how you configure
   RBI](https://docs.paloaltonetworks.com/remote-browser-isolation/administration/configure-rbi#configure-rbi-panorama)

---

<a id="pa-reset-or-transfer-your-prisma-access-managed-by-panorama-license"></a>

#### Reset or Transfer Your Prisma Access (Managed by Panorama) License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama>*

Learn how to use make changes to your license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) | - Prisma Access license |

If you need to transfer your Panorama Managed
Prisma Access license from one Panorama appliance to another, or
if you have an evaluation Prisma Access license and you purchase
a production license, use one of the following supported upgrade
paths to transfer or upgrade your license.

The license update
procedure you use for Prisma Access (Managed by Panorama) depends on
the type of Prisma Access license you have. If you are upgrading
from an evaluation to a paid Prisma Access license, the update path
differs depending on the type of license your Panorama appliance
has.

- If you are transferring a production (paid) Prisma
  Access license from one Panorama appliance to another, use the workflow
  in [Transfer or Update](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/transfer-or-update-your-license-panorama.html#id707f346c-9230-4e39-9af0-d6a8201c791a) to transfer
  the Prisma Access license.
- If you are upgrading from an evaluation Prisma Access license
  to a production Prisma Access license, use one of the following
  workflows to transfer the license:

  - If your Panorama is a production appliance with active, paid licenses, [reset your Panorama
    Managed Prisma Access License](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/reset-your-license-panorama.html#id7b5ee561-21e3-45e0-bda5-d7a03af3f8cf) to update your licenses to
    the production service. We recommend using this update path because
    you do not have to migrate your existing configuration.
  - If your Panorama is an evaluation appliance, you need to [transfer your
    license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/transfer-or-update-your-license-panorama.html#id707f346c-9230-4e39-9af0-d6a8201c791a) to a production appliance.

  Before you upgrade
  from an evaluation to a paid (production) license, be aware of the
  following guidelines and requirements:

  - Do not proceed
    with the workflow until the order process is complete, the order
    has been fulfilled, and the support portal is showing the newly
    purchased cloud service licenses.
  - An evaluation license has the same capabilities as the Prisma
    Access Local Enterprise edition, including supporting a maximum
    of 5 locations and 2 service connections, and includes all the supported
    add-ons. After you purchase your Prisma Access production license,
    you must determine what is supported [with your Prisma
    Access production license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license.html) and deactivate the unsupported
    capabilities before you update your license from evaluation to production.
  - The number of locations and service connections for your
    production license depends on the license type; check your license
    details to see the maximum number of locations and service connections
    that are supported.

The following table
shows the supported license update methods based on the type of
Panorama appliance used with the evaluation.

![]()

---

<a id="pa-reset-your-prisma-access-managed-by-panorama-license"></a>

##### Reset Your Prisma Access (Managed by Panorama) License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/reset-your-license-panorama>*

Learn how to reset your license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) | - Prisma Access license |

Use this workflow if you need to modify one
or more of your licenses; for example, if you update your Prisma
Access license from an evaluation to a production version.

If
you are upgrading your Prisma Access license from evaluation to
production, make sure that your Panorama appliance has active, paid
licenses before starting this procedure. If your Panorama has an
evaluation license, you need to [transfer the Prisma
Access license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/transfer-or-update-your-license-panorama.html#id707f346c-9230-4e39-9af0-d6a8201c791a) to a Panorama with a production license.

1. In the Panorama appliance, select PanoramaLicenses.
2. Make a note or take a screenshot of the licenses you
   have, the quantity of licenses, and the expiration date of each
   license.
3. Remove the license that you need to modify.

   For example, if you are upgrading from an evaluation to
   a production license, remove the evaluation cloud service licenses
   you have installed.

   1. Open a SSH console session to the Panorama
      appliance.
   2. Enter the delete license key command,
      then press the Tab key to view all installed
      license keys.
   3. Delete all Prisma Access license keys, including the
      license keys for Strata Logging Service, Prisma Access for Users, Prisma
      Access for Networks, and Prisma Access for Clean Pipe, as applicable
      to your deployment.

      The following is an example of the process:

      ```
      admin-Panorama>
      								delete
      									license key [then click tab]
      								GlobalProtect_Cloud_Service_f_2017_11_07.key 2017/11/0712:32:51 0.3K
      								GlobalProtect_Cloud_Service_for_Mobile_Users_2017_11_07.key 2018/01/10 13:52:18 0.3K
      								GlobalProtect_Cloud_Service_for_Remote_Networks_2017_11_07.key 2018/01/10 13:52:18 0.3K
      								Logging_Service_2017_11_07.key 2018/01/10 13:52:18 0.3K

      								admin-Panorama>
      								delete license key Logging_Service_2017_11_07.key
      								successfully removed Logging_Service_2017_11_07.key

      								admin-Panorama>
      								delete license key GlobalProtect_Cloud_Service_f_2017_11_07.key
      								successfully removed GlobalProtect_Cloud_Service_f_2017_11_07.key

      								admin-Panorama>
      								delete license key GlobalProtect_Cloud_Service_for_Remote_Networks_2017_11_07.key
      								successfully removed GlobalProtect_Cloud_Service_for_Remote_Networks_2017_11_07.key

      								admin-Panorama>
      								delete license key GlobalProtect_Cloud_Service_for_Mobile_Users_2017_11_07.key
      								successfully removed GlobalProtect_Cloud_Service_for_Mobile_Users_2017_11_07.key
      							
      ```
4. From the Panorama administration console, select PanoramaLicenses and
   click Retrieve license keys from license server.

   This step should refresh the licenses you already have,
   and the new licenses should reflect the new quantity you purchased
   and the new expiration date.
5. Delete
   any existing certificates using CLI from Panorama by entering the
   following command:

   ```
   admin-Panorama>
   						request plugins cloud_services
   							panorama-certificate delete
   					
   ```
6. Enter the debug plugins cloud\_services reset-endpoint command
   to reset the Panorama appliance.
7. Create the new certificate with the new OTP by entering
   the following command, where value is the new
   OTP:

   ```
   admin-Panorama>
   						request plugins cloud_services
   							panorama-certificate fetch debug yes otp
   							value
   						
   					
   ```
8. Complete the [One Time Password (OTP)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons.html)
   procedure and verify the Panorama appliance.
9. In Panorama, verify that you can make configuration changes and can
   successfully push the configuration.

   If the licenses do not update correctly, or if you are not able to make
   configuration changes after the refresh, contact Palo Alto Networks support.

---

<a id="pa-transfer-or-update-your-prisma-access-managed-by-panorama-license"></a>

##### Transfer Or Update Your Prisma Access (Managed by Panorama) License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/make-changes-to-your-license-panorama/transfer-or-update-your-license-panorama>*

Learn how to transfer or update your Prisma Access license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) | - Prisma Access license |

Use the following workflow if you need to transfer
Prisma Access licenses from one Panorama appliance to another, for
example:

- If you need to transfer production (paid)
  licenses from one Panorama appliance to another.
- If you are running an evaluation license on an evaluation
  Panorama appliance. After you upgrade the Prisma Access license
  to a paid license, you cannot transfer this license to a Panorama
  that has an evaluation license; in this case, you must transfer
  the production Prisma Access license from an evaluation to a production
  Panorama appliance.

When you renew your license, you must also perform these steps to retrieve the
new license key. Panorama does not retrieve the licenses after a renewal.

Prisma Access automatically preserves all instances and public and loopback IP addresses
during the license transfer.

Make a note of the following guidelines before starting this procedure:

- Make sure that both Panorama appliances use the same Tenant or Tenant Service
  Group (TSG) ID.
- If you are performing multiple license transfers, do not perform the license
  transfer one after the other. Wait at least 15 minutes before starting another
  transfer after the first has completed.

1. ( Optional) [Export a snapshot of your Panorama
   configuration](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations) to a host external to Panorama or to a firewall.

   While Prisma Access saves all its infrastructure settings, including
   public and loopback IP addresses, you need to transfer any Panorama-specific
   configuration to the new Panorama appliance. You can export your
   configuration after the license transfer process is complete, but we
   recommend exporting it before you transfer the licenses as a best practice.
2. Log in to the Palo Alto Networks [Customer Support Portal](https://support.paloaltonetworks.com).
3. Select AssetsDevices.
4. Find the production Panorama appliance to which you will
   be transferring the production Prisma Access plugin and complete
   these steps:
   1. Verify that it has an active support license.
   2. Make a note of this serial number; you use it in a
      later step.
5. Search for the current Panorama appliance you are using
   to run Prisma Access by using the serial number.

   The model name should be in the format PAN-PRA-25-E xx.

   ![]()
6. Click the Actions icon for the
   current Panorama appliance.
7. Select Transfer Licenses and choose
   the Panorama appliance to which you will be migrating.

   ![]()
8. Review the EULA and click Agree,
   then click Submit.
9. Wait for a confirmation message in the Support Portal
   for a successful transfer.
10. After the successful transfer of licenses, login to the
    administration console of your production Panorama appliance.
11. Select PanoramaSupport and verify that the
    Panorama appliance has a valid support license.
12. Click Dashboard and verify that
    the Panorama appliance is running the minimum supported software
    version. See [Minimum Required Panorama Software
    Versions](https://docs.paloaltonetworks.com/compatibility-matrix/reference/prisma-access) for details.
13. Verify that the Panorama appliance is configured to use
    NTP by selecting PanoramaSetupServicesNTP and
    setting a value, such as pool.ntp.org, for the
    NTP Server.
14. Download and install the Cloud Services plugin.

    See the [Palo Alto Networks Compatibility
    Matrix](https://docs.paloaltonetworks.com/compatibility-matrix/panorama/plugins.html#id17C8A0Y0M9I) for the Panorama versions that are supported with the
    Cloud Services plugin.

    You can either download the plugin from the Customer Support Portal, or you
    can check for plugin updates directly from Panorama.

    - To download and install the Cloud Services plugin by downloading it
      from the Customer Support Portal, complete the following steps.

      1. Log in to the [Customer Support
         Portal](https://support.paloaltonetworks.com) and select Software UpdatesPanorama Integration Plug In.
      2. Find the Cloud Services plugin in the Panorama Integration
         Plug In section and download it.

         Do not rename the plugin file or you will not be able to
         install it on Panorama.
      3. Log in to the Panorama Web Interface of the Panorama you
         licensed for use with the Prisma Access, select PanoramaPluginsUpload and Browse for the
         plugin File that you downloaded from
         the CSP.
      4. Install the plugin.
    - To download and install the Cloud Services plugin directly from
      Panorama, complete the following steps:

      1. Select PanoramaPlugins and click Check Now to
         display the latest Cloud Services plugin updates.

         ![]()
      2. Download the plugin version you want
         to install.
      3. After downloading the plugin, Install
         it.

    Installing a newer version of the Cloud Services plugin overwrites the
    previously installed version. If you are installing the plugin for the first
    time, after you successfully install, Panorama refreshes and the Cloud
    Services menu displays on the Panorama tab.

    ![]()
15. Select PanoramaLicenses and click Retrieve
    license keys from license server.

    This should refresh the screen with recently transferred
    Prisma Access and Strata Logging Service licenses you purchased. If the
    cloud service licenses do not appear, contact Palo Alto Networks
    Support for assistance.
16. Complete the [one-time password (OTP)
    verification](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons.html) procedure and verify the Panorama appliance.
17. Migrate the configuration from the previous Panorama
    appliance to the current Panorama appliance.

    - If the production Panorama appliance is completely
      new, [export the configuration](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations) from
      the Panorama appliance you used during the evaluation (if you have
      not done so already) and [import it](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/revert-panorama-configuration-changes) to this Panorama
      appliance.
    - If this is the Panorama appliance that you have been using
      to manage your existing VMs and devices, [load a partial configuration](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/manage-firewalls/transition-a-firewall-to-panorama-management/load-a-partial-firewall-configuration-into-panorama) to
      this Panorama appliance.

    You can now use this Panorama
    appliance to configure and manage Prisma Access.

---

<a id="pa-verify-your-prisma-access-managed-by-panorama-account"></a>

#### Verify Your Prisma Access (Managed by Panorama) Account

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/verify-your-prisma-access-account>*

Verify your Prisma Access (Managed by Panorama) account using
the OTP.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) | - Prisma Access license |

To generate and retrieve the one-time password (OTP) for your Prisma Access (Managed by Panorama) deployment,
complete one of the following tasks:

1. Generate an OTP by going to the [CSP](https://support.paloaltonetworks.com/), selecting AssetsCloud Services, selecting Generate OTP, selecting the
   serial number of your Panorama appliance and Generate
   OTP.

   ![]()
2. Verify your account.

   When you try to use the Cloud Services plugin for the first
   time after installing it, you will be prompted to verify your account.
   This step ensures that the Panorama serial number is registered
   to use Prisma Access and enables a secure communication path between
   the Prisma Access components and Panorama.

   1. In Panorama, select PanoramaCloud ServicesConfiguration and
      click Verify.

      If Verify is disabled, check that
      you have configured a DNS server and NTP server on PanoramaSetupServices.
   2. Paste the One-time Password you
      copied and click OK.

      ![]()

      You
      have ten minutes to enter the OTP before it expires.

---

<a id="pa-activate-your-prisma-access-license"></a>

### Activate Your Prisma Access License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license>*

Learn how to activate your Prisma Access license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) - Prisma Access (Managed by Panorama) | - Prisma Access license |

Prisma Access provides a [flexible licensing scheme](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license.html) so that you can purchase just what
you need to secure your remote networks and mobile users.

Our licensing model allows you to consume the capabilities of Prisma Access aligned to
your business needs in the manner that delivers the fastest return on investment
(ROI).

Both Prisma Access (Managed by Strata Cloud Manager) and Prisma Access (Managed by Panorama) options for Prisma Access support this
licensing model. You can choose your Prisma Access edition based on your access needs
and security goals.

**Managing Prisma Access**

There are two ways you can manage Prisma Access:

- Prisma Access (Managed by Strata Cloud Manager)
- Prisma Access (Managed by Panorama)

You must decide how you want to manage Prisma Access before you follow the
activation guides.

Follow the instructions for activating and installing Prisma Access (Managed by Strata Cloud Manager) or
Prisma Access (Managed by Panorama).

- [Prisma Access (Managed by Strata
  Cloud Manager) License Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation.html)
- [Prisma Access (Managed by Panorama)
  License Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation.html)

---

<a id="pa-prisma-access-managed-by-strata-cloud-manager-and-add-ons-license-activation"></a>

#### Prisma Access (Managed by Strata Cloud Manager) and Add-Ons License Activation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation>*

Learn how to activate Prisma Access and add-on licenses in Common Services.

Welcome to Prisma Access (Managed by Strata Cloud Manager) and add-ons license activation.

- [Activate a License for Prisma Access
  (Managed by Strata Cloud Manager)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons.html) and Add-ons:
  - [Allocate licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html)
  - [Plan service
    connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html)
  - [Add additional
    locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html)
  - [Enable available add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html)
- [Share a License for Prisma Access
  (Managed by Strata Cloud Manager)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html) and Add-ons to share subscription
  quantity between multiple tenants.
- [Increase Subscription Allocation Quantity](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity.html) to increase the
  number of mobile users allocated, the amount of bandwidth allocated, or enable
  add-ons that you previously did not allocate.

---

<a id="pa-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-services"></a>

##### Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons>*

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through .

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or FedRAMP Moderate | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

After you receive an email from Palo Alto Networks identifying the license you're
activating, including all your add-ons and capacities, use the activation link to
begin the activation process. The service will help you with the process of claiming
your license, creating your tenant, and managing your users.

Select Activate Subscription in your email.

![]()

Use one of the following options:

- [First time license
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/activate-cloud-managed-prisma-access-and-add-ons-first-time-one-csp.html#one-csp)
- [Return visit license
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/activate-cloud-managed-prisma-access-and-add-ons-repeat-visits.html#return)

##### First Time Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through
Common Services for the first time if you have only one Customer Support Portal
account.

If you have only one Customer Support Portal account, follow these steps for
first-time Prisma Access (Managed by Strata Cloud Manager) and add-ons license activation.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the 
   Superuser role.
2. Choose Cloud management for your setup and management
   method.

   ![]()
3. Allocate the subscription to the recipients of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)

   1. If you need just one tenant, use or rename the tenant provided. The
      name provided matches your Customer Support Portal account for
      convenience.

      ![]()
   2. (Optional) This step applies if you are a managed security
      service provider (MSSP), a distributed enterprise customer, or need
      multiple tenants. After you create the first tenant, you can
      Allocate to subtenant and use or rename the
      tenant provided.

      ![]()

      A subscription gets allocated on a tenant or a sub-tenant. This step
      is for choosing a tenant where you want to allocate a license, not
      for building a complete tenant hierarchy. You can create only a
      tenant and subtenant here, and you can choose to allocate a license
      to that subtenant.

      After activation, you can build out your tenant hierarchy as needed
      through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants). You can
      create your tenant hierarchy to reflect your existing organizational
      structure. You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy
      limits](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants).

      After you create a tenant hierarchy, you can [share a
      license.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html)
   3. Select Done.

   After first time or return visit license activation, continue with the
   following steps:
   1. [Allocate
      licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html)
   2. [Plan service
      connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html)
   3. [Add additional
      locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html)
   4. [Enable available add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html)
   5. [Search for subscription
      details](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions)
   6. [Increase subscription
      quantity](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity.html)
   7. [First time setup](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/first-time-multitenant-setup) for Prisma Access multitenancy.

##### Return Visit Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through Common Services for repeat visits.

Follow these steps if you have already completed Prisma Access and add-ons
license activation, you have already created your tenant hierarchy through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants), and you are returning
to activate another license in your existing hierarchy.

1. Log in with your email address.
2. Choose Cloud management for your setup and management
   method.

   ![]()
3. Allocate the subscription to the recipient tenant of your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()

   After first time or return visit license activation, continue with the
   following steps:
   1. [Allocate
      licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html)
   2. [Plan service
      connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html)
   3. [Add additional
      locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html)
   4. [Enable available add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html)
   5. [Search for subscription
      details](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions)
   6. [Increase subscription
      quantity](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity.html)
   7. [First time setup](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/first-time-multitenant-setup) for Prisma Access multitenancy.

---

<a id="pa-allocate-licenses-for-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-services"></a>

###### Allocate Licenses for Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access>*

Learn how to allocate licenses for your Prisma Access (Managed by Strata Cloud Manager) tenants through
Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

After you activate a license, continue to allocate licenses. You can purchase Prisma Access with a
Combination SKU of Mobile User + Remote Network or as individual Remote Network
and Mobile User SKUs. During activation of a Combination SKU, you must allocate
to each tenant with equal quantities of Mobile User capacity and Remote
Network capacity.

Supported examples: If the license is a combination SKU
quantity of 1000, you can create two tenants with the following capacity:

- Tenant One — 500 Mobile Users and 500 Mbps Remote Network
- Tenant Two — 500 Mobile Users and 500 Mbps Remote Network

Unsupported examples: If the license is a combination
Mobile Users + Remote Networks SKU of 1000 units:

- Tenant One — 500 Mobile Users and 200 Mbps Remote Network
- Tenant Two — 200 Mobile Users and 500 Mbps Remote Network
- Tenant Three — 300 Mobile Users
- Tenant Four — 300 Remote Networks

If you need Mobile Users only, Remote Networks only, or
unequal quantities of Mobile Users and Remote Networks, you need to purchase
Mobile-Users-only and Remote-Networks-only SKUs separately.

1. Select the Region storage location for the data logs,
   known as Strata Logging Service. Further information about [supported regions](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations#id089612c2-6bca-417d-8e99-f2af7c5a44fc).

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
2. Assign Mobile User and Remote Network licenses to
   the recipient tenant.

   ![]()

   1. Allocate licenses per number of mobile users.

      - Each tenant can accept only one type of Prisma Access
        license, such as: Enterprise, Business Premium, or Business. One
        tenant can't contain a mix of different Prisma Access
        licenses.
      - The maximum number of users available for your first tenant
        is based on your Prisma Access license quantity.
      - The number of users available for other tenants is based on
        the remainder after allocation.
      - Based on your license, you need a minimum capacity to share
        with another tenant. For example, Prisma Access
        local edition requires a minimum of 200 licenses that need
        to be allocated whether it's a root tenant or a child
        tenant, but Prisma Access global or worldwide
        edition requires a minimum of 1,000 licenses that need to be
        allocated whether it's a root tenant or a child tenant.

        - If you have a license that is a combination of MU+RN
          together, you can’t split it into different tenants. For
          example, a 200 MU+RN local edition license still needs
          to be split as minimum 200 MU+RN in each tenant. You
          can’t have 200 MU in one tenant and 200 RN in another
          tenant.
      - [Secure mobile users
        with](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/secure-mobile-users-with-prisma-access.html)
        Prisma Access.
   2. Allocate licenses per bandwidth of remote networks.

      - Each tenant can accept only one type of Prisma Access
        license, such as: Enterprise, Business Premium, or Business. One
        tenant can't contain a mix of different Prisma Access
        licenses.
      - The maximum amount of bandwidth available for your first
        tenant is based on your Prisma Access license
        quantity.
      - The amount of bandwidth available for other tenants is based
        on the remainder after allocation.
      - Based on your license, you need a minimum capacity to share
        with another tenant. For example, a Prisma Access
        local edition requires 200 Mbps that need to be allocated
        whether it's a root tenant or a child tenant, but a Prisma Access global or worldwide requires min of 1,000
        Mbps that need to be allocated whether it's a root tenant or
        a child tenant.

        - If you have a license that is a combination of MU+RN
          together, you can’t split it into different tenants. For
          example, a 200 MU+RN local edition license still needs
          to be split as minimum 200 MU+RN in each tenant. You
          can’t have 200 MU in one tenant and 200 RN in another
          tenant.
      - [Secure remote networks
        with](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/secure-remote-networks-with-prisma-access.html)
        Prisma Access.

      Continue to [plan service
      connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html).

---

<a id="pa-plan-service-connections-for-prisma-access-managed-by-strata-cloud-manager-through-common-services"></a>

###### Plan Service Connections for Prisma Access (Managed by Strata Cloud Manager) Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access>*

Learn how to plan service connections for your Prisma Access (Managed by Strata Cloud Manager) license
through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

After you activate a license and [allocate a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html), continue to plan service
connections.

1. Choose how many service connections to allocate to your tenant.

   ![]()

   - If you have a local edition license, the default number of service
     connections is 2. If you have a global enterprise or worldwide
     license, the number of locations is 5. For additional service
     connections, the number available for allocating to your tenants is
     based on the Service Connection add-on.
   - When [license sharing](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html),
     the number available for other tenants is based on the remainder
     after allocation.
   - Consider a scenario where you purchase 3000 enterprise edition
     licenses and share with three tenants. The example tenant license
     allocations are Tenant A = 1000, Tenant B = 1000, and Tenant C =
     1000. Each tenant has five service connections by default. If you
     purchase 10 additional service connections, you can allocate them
     per tenant so that Tenant A can have six additional service
     connections, Tenant B can have the remaining 3, and Tenant C can
     have the one remaining. This is in addition to the default.

   Continue to [add additional locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html).

---

<a id="pa-add-additional-locations-for-prisma-access-managed-by-strata-cloud-manager-through-common-services"></a>

###### Add Additional Locations for Prisma Access (Managed by Strata Cloud Manager) Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access>*

Learn how to add additional locations for your Prisma Access (Managed by Strata Cloud Manager) license
through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

After you activate a license and [allocate a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html), continue to add
additional locations.

1. Choose how many locations to allocate to your tenant.

   ![]()

   - If you have a local edition license, the default number of locations
     is 5, and the number available for allocating to your tenants is
     based on the Additional Locations add-on. If you have a global or
     worldwide license, the number of locations is unlimited, so you do
     not have the option to add the quantity.
   - The select or deselect check box is available for toggle if you have
     chosen to allocate part of the license to this tenant for Prisma Access
     [license
     sharing](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html).
   - The number available for other tenants is based on the remainder
     after allocation.

   Continue to [enable available
   add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html).

---

<a id="pa-enable-available-add-ons-for-prisma-access-managed-by-strata-cloud-manager-and-add-ons-through-common-servicess"></a>

###### Enable Available Add-Ons for Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Through Common Servicess

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access>*

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through
Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

After you activate a license, [allocate a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html), and [plan service connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html), continue to enable
the available add-ons.

1. Products or Add-ons are enabled
   by default based on your contract. Disable (deselect) add-ons you don’t want
   to activate now, such as Autonomous DEM and Service Connection.

   ![]()

   1. Select a New or existing
      instance.
   2. For the CASB Bundle, SaaS Security Inline URL
      Subnet is the URL to launch the corresponding service
      web interface.
   3. For IoT Security, enter a unique App Subdomain
      to complete the <subdomain>.iot.paloaltonetworks.com URL for your IoT
      Security application. This is the URL where you log in to the IoT
      Security portal.
2. Add your Strata Logging Service for storing tenant data such as
   configuration, telemetry logs, system logs, and stats.

   ![]()

   - Allocate part of the available storage to this tenant if you want to
     conserve part of the storage for another tenant.
   - Allocate the entire available storage to this tenant if you don't
     have other tenants or if you will purchase additional capacity to
     allocate to your other tenants.
   - Based on your license, you need a minimum capacity to share with
     another tenant. For example, a Prisma Access local and
     business licenses require 1 TB.
   - See [Strata Logging
     Service Administration Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html).
3. Agree to the Terms and Conditions.
4. Activate Now. The products and
   add-ons that you're activating (such as Prisma Access or Strata Logging Service) are now provisioned. As the subscriptions are
   activating, the progress status will display. When the process is complete, the
   tenant status displays as Up. You now have a tenant
   provisioned with instances of the products that you purchased. The tenant has
   one user — the account that you used when you began this process.
5. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - [Open APIs](https://pan.dev/sase/docs/)
   - [Strata Logging Service](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
   - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access)
   - [Prisma Access](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-insights/insights)
   - [Next-Generation CASB](https://docs.paloaltonetworks.com/next-gen-casb)
   - [Enterprise DLP](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp)
   - [Autonomous DEM in](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-in-prisma-access)
   - [Onboard IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/onboard-iot-security)
6. (Optional) In a multitenant hierarchy, monitor your tenants with the
   [Prisma Access](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-pa-summary-dashboard).
7. (Optional) [add user access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-users) and [assign roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles).

---

<a id="pa-search-for-subscription-details-through-common-services"></a>

##### Search for Subscription Details Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions>*

Learn how to search for subscriptions and add-on license details through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Strata Multitenant Cloud Manager - Activation Console - Commercial or   FedRAMP Moderate | - Any [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) supported app - A [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) depending   on your needs |

You can search the subscriptions table with your contract number or Tenant Service
Group ID (tsg\_id). The Subscription page contains information
about all the licenses that you have access to based on your support account.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started)
   Subscription.
2. Type your contract number, tsg\_id, or product name in the search bar.

   ![]()

   You'll see the following:

   - Name of the licensed product.
   - Status of the license, such as partially assigned or all assigned.
   - The assigned quantity of the license compared to the total quantity
     available.
   - The number of tenants associated with the license.
   - The contract number associated with the license.
   - The expiration date of the license.
   - The actions available for the license.

---

<a id="pa-share-a-license-for-prisma-access-managed-by-strata-cloud-manager-through-common-services"></a>

##### Share a License for Prisma Access (Managed by Strata Cloud Manager) Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access>*

Learn how to share your Prisma Access (Managed by Strata Cloud Manager) license through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Existing tenant with partially allocated Prisma Access   license quantity - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

During your Prisma Access
[and add-ons license activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons.html),
you can choose to allocate the whole license to your tenant or allocate part of the
license. If you do not allocate the entire quantity to one tenant at that time, then
you can share a license between multiple tenants. This assumes that you have already
[added tenants](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants) to create your tenant
hierarchy.

All tenants created using a shared license need to be deployed with the 10.1.3 or
later dataplane version and Prisma Access 3.2 Innovation or later version. Open a
[support case](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/related-documentation/open-support-case) to request the migration of
your tenant from the default 10.0.8 dataplane to the 10.1.3 or later dataplane
version.

Consider an example where you start with a contract for 10,000 Mobile Users and
Remote Networks. During your initial activation, you allocate a quantity of 2,000.
From Tenant Management, you see the currently allocated
quantity in the License column.

![]()

You can share the allocation quantity by completing the following steps.

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click :Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   If you are
   modifying the allocation for the default tenant, ensure that you reduce the
   assigned license quantity. The reduced quantity becomes available for
   reallocation to other tenants in the hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat step 3 to allocate licenses to additional tenant.
9. Validate the license allocation by switching to the corresponding tenant in the
   tenant browser and reviewing the allocation details.

   ![]()

---

<a id="pa-increase-subscription-allocation-quantity-through-common-services"></a>

##### Increase Subscription Allocation Quantity Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity>*

Learn how to increase the quantity of subscriptions and add-ons through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Strata Multitenant Cloud Manager - Activation Console - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

During your Prisma Access
[and add-ons license activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons.html),
you can choose to allocate the whole license to your tenant or allocate part of the
license. If you do not allocate the entire quantity to one tenant at that time, or
you do not allocate your add-ons, then you can increase the quantity or allocate the
add-ons later.

Consider an example where you start by [sharing your subscription](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html) between two
tenants, but you still have additional quantity remaining in your subscription. You
have two options for increasing the number of mobile users allocated to a tenant,
increasing the amount of bandwidth allocated to a tenant, increasing the Cortex Data
Lake (Strata Logging Service) quantity, or enabling add-ons that were previously not allocated to a
tenant:

- [Increase Quantity from the Tenant Table](#pa-increase-subscriptions_tenant-table)
- [Increase Quantity from the Subscription Table](#pa-increase-subscriptions_subscription-table)

<a id="pa-increase-subscriptions_tenant-table"></a>

###### Increase Quantity from the Tenant Table

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started)
   Tenants.
2. Search or scroll to find the tenant where you want to increase the
   quantity.
3. From Actions, select Edit
   License.

   ![]()
4. You are directed to the Activate Subscription page
   where the Customer Support Account is already filled in, and the cloud
   management method is already enabled. Select
   Done.

   ![]()
5. The Recipient and the Region
   are already filled in. Increase the number of mobile users allocated, the
   bandwidth allocated, or enable add-ons that were previously not allocated.
   Select Done.

   ![]()
6. In this example, Strata Logging Service and Cloud Identity Engine are unchanged.
   Agree to the Terms and Conditions and
   Activate.

   ![]()
7. From both Subscription and Tenant
   Management, you can see that the allocated quantity has
   increased. The following example shows Tenant
   Management.

   ![]()

<a id="pa-increase-subscriptions_subscription-table"></a>

<a id="pa-subscription-table_step-recipient"></a>

###### Increase Quantity from the Subscription Table

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started)
   Subscription.
2. [Search the subscriptions](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions) table
   with your contract number or Tenant Service Group ID (tsg\_id).
3. You see the status of partially assigned and the assigned quantity compared
   to the total quantity. You also see the associated tenants where the
   subscription is currently allocated.

   ![]()
4. From Actions, select Activate Cloud
   Tenant.
5. Select the Associated Tenant number to verify which
   tenants are associated with this subscription.

   Take note of these tenant names. To increase the
   quantity, you need to select one of these tenants as the [recipient](#pa-subscription-table_step-recipient) in a later step.
6. You are directed to the Activate Subscription page
   where the Customer Support Account is already filled in, and the cloud
   management method is already enabled. Select
   Done.

   ![]()
7. Select one of the tenants where the subscription is already associated as
   the Recipient.

   If you do not select one of the tenants where
   the subscription is already associated, then you are not increasing the
   quantity. By selecting a completely different tenant, you are sharing
   instead.
8. The Region is already filled in based on the region
   of the associated tenant.
9. Increase the number of mobile users allocated, the bandwidth allocated, or
   enable add-ons that you previously did not allocate. Select
   Done.

   ![]()
10. You can change the Strata Logging Service quantity here, but in this example,
    Strata Logging Service and Cloud Identity Engine are unchanged. Agree
    to the Terms and Conditions and
    Activate.

    ![]()
11. From both Subscription and Tenant
    Management, you can see that the allocated quantity has
    increased. The following example shows Tenant
    Management.

    ![]()

---

<a id="pa-prisma-access-managed-by-panorama-and-add-ons-license-activation"></a>

#### Prisma Access (Managed by Panorama) and Add-Ons License Activation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation>*

Learn how to activate Prisma Access (Managed by Panorama) and add-on licenses in Common Services.

Welcome to Prisma Access (Managed by Panorama) and add-ons license activation.

- [Activate a License for](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons.html)
  Prisma Access (Managed by Panorama) and Add-ons for Commercial and FedRAMP Moderate
  deployments
- [Activate a License for](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-single-tenant-panorama-managed-prisma-access-china.html)
  Prisma Access (Managed by Panorama) China for Commercial deployments

---

<a id="pa-activate-a-license-for-prisma-access-managed-by-panorama-and-add-ons-through-common-services"></a>

##### Activate a License for Prisma Access (Managed by Panorama) and Add-Ons Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons>*

Learn how to activate your Prisma Access (Managed by Panorama) tenants through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Panorama - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser - FedRAMP Moderate: [Panorama-managed](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/panorama-managed-prisma-access-fedramp-plugin-and-dataplane-requirements)   Prisma Access FedRAMP Plugin and Dataplane   Requirements |

###### Register Panorama with Customer Support Portal

1. Log in to the [Customer Support Portal](https://support.paloaltonetworks.com/Support/Index).
2. Select ProductDevices.
3. Click **Register New Device** and follow the on-screen prompts to
   register Panorama.

###### Activate Premium Support License

1. Log in to the [Customer Support Portal](https://support.paloaltonetworks.com/Support/Index).
2. Select ProductDevices.
3. Search for the newly registered device.
4. Click ActionActivate Auth-Code for the specific product.
5. Specify the auth code you received as part of the purchase order.
6. Agree and Submit.

###### Activate Subscription

After you receive an email from Palo Alto Networks identifying the license you
are activating, including all your add-ons and capacities, use the activation
link to begin the activation process. The service will help you with the process
of claiming your license, creating your tenant, and managing your users.

Select **Activate Subscription** in your email.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, enter the
     email address you used when you registered for that account, and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account,
     then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to
   the tenant that you use for this license. This tenant, and any
   others created by this email address, will have the
   Multitenant Superuser role.
2. Choose the Customer Support Account number that you
   want to use to claim the license.

   ![]()
3. Choose Panorama management for your setup and
   management method.

   ![]()
4. Allocate the subscription to the recipients of your choice. You can select
   an existing tenant or create a new tenant. The following example shows
   creating a new tenant.

   For Managed Security Service Providers (MSSPs) and distributed
   enterprises, you can allocate the subscription directly on any tenant in
   the hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)

   1. Create a new tenant from All Tenants +.

      ![]()
   2. Name the tenant and select Done.

      ![]()
   3. (Optional) For Managed Security Service Providers (MSSPs)
      and distributed enterprises, create a new child tenant by selecting
      + from the parent tenant that you
      previously created.

      ![]()
   4. (Optional) Name the child tenant and select
      Done.

      ![]()
5. Select the Region where you want to deploy your
   product.

   There is no cross-region aggregation. Make sure
   that all your tenants are in the same region for monitoring
   purposes.
6. Select Create New from the Panorama drop-down and
   make a note of the Panorama Serial Number.

   You use this serial number during product setup.

   ![]()
7. Add-ons are enabled by default based on your
   contract. Disable (deselect) any add-ons you
   don’t want to activate now.

   ![]()
8. Select Cloud Identity Engine if you might use it in
   the future.
9. Agree to the Terms and Conditions.
10. Activate Now. The products and
    add-ons that you are activating (such as Prisma Access or Strata Logging Service) are now provisioned. As the subscriptions are
    activating, the progress status will display. You now have a tenant
    provisioned with instances of the products that you purchased. The tenant
    has one user — the Customer Support account that you used when you began
    this process.
11. Generate your One Time Password (OTP) from Common ServicesTenant ManagementTenant nameGenerate OTP for setting up Panorama.

    ![]()
12. Complete the product setup:

    - Prisma Access (Managed by Panorama)
      [Administrators Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin)
    - Strata Logging Service
      [Getting Started Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
    - Prisma Access
      [Insights Administrators Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-insights/insights)
    - [Autonomous DEM in](https://docs.paloaltonetworks.com/autonomous-dem/autonomous-dem-in-prisma-access)
      Prisma Access
    - [Enterprise DLP](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp)
    - [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline)

---

<a id="pa-activate-a-license-for-prisma-access-managed-by-panorama-china-through-common-services"></a>

##### Activate a License for Prisma Access (Managed by Panorama) China Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-single-tenant-panorama-managed-prisma-access-china>*

Learn how to activate your single tenant Prisma Access (Managed by Panorama) China
license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Panorama located in mainland China - Commercial deployments | - Prisma Access license with optional add-ons - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser |

This process applies to only single tenant Prisma Access (Managed by Panorama) China license activation. The
Panorama you use to manage Prisma Access China must be installed and
located in mainland China. If it is a [hardware](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prepare-the-prisma-access-infrastructure/get-started-with-prisma-access-overview) appliance, it
must be based in mainland China; if it is a [VM-series](https://docs.paloaltonetworks.com/vm-series) Panorama, the processing location must be in
mainland China. These license activation instructions assume that you already have
[deployed](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/guides/panorama-on-aws-deployment-guide) your VM-Series or hardware
Panorama with the China-specific Panorama image.

Make sure that you have reviewed the requirements and prerequisites for [configuring a](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-china/prisma-access-in-china/configure-a-prisma-access-china-deployment)
Prisma Access China deployment. Be aware that the CLI commands must be
completed prior to generating your one-time password (OTP).

1. After you receive an email from Palo Alto Networks identifying the license you
   are activating, including all your add-ons and capacities, select Get
   Started with Prisma Access in your email to begin the
   activation process.
2. Choose the Customer Support Account number that you want
   to use to claim the license.

   ![]()
3. Choose Panorama management for your setup and management
   method.

   ![]()
4. Select the activation flow for Panorama Managed / Single Tenant
   Cloud Management.

   ![]()
5. You are automatically directed to Common ServicesSubscriptions & Add-ons, where you manage your license.
6. Select your products to highlight them for activation, then
   Activate.

   ![]()
7. Select Create New Tenant from the tenant drop-down to
   create the tenant that you want to use for this license.
8. Choose the Customer Support Portal account number that
   you want to use to claim the license. This is limited to CSPs that are
   associated with Prisma Access China.
9. Select Create New Instance to create the Cortex Data
   Lake that you want to use for this license.
10. China is selected by default to create the SASE Region
    for the logs.

    ![]()
11. Toggle off Cloud-Managed to select Panorama and follow
    the web interface instructions.
12. Select Create New from the Panorama drop-down and copy
    the Panorama serial number for use in [step 16](#pa-activate-a-license-for-prisma-access-managed-by-panorama-china-through-common-services).

    ![]()
13. Add-ons are enabled by default
    based on your contract.

    - Level 1 support includes the following add-ons:

      - Additional SC for Private App Access
      - Site-to-Site and User-to-Site Access
    - Level 2 support includes the following add-ons:

      - Additional
        SC for Private App Access
      - Site-to-Site and User-to-Site Access
      - CASB Bundle for PA China
      - DLP (individual)
      - Internet of Things (IoT) security for PA China
      - SaaS Inline (individual)
14. Select Cloud Identity Engine regardless
    if you intend to use it now or if you might use it in the future.
15. Agree to the Terms and Conditions.
16. Activate Now. The
    products and add-ons that you are activating (such as Prisma Access
    China or Strata Logging Service) are now provisioned. As the subscriptions
    are activating, the progress status will display. You now have a
    tenant provisioned with instances of the products that you purchased.
    The tenant has one user — the Customer Support account that you
    used when you began this process.
17. After the provisioning is complete, you receive an email
    confirmation.
18. In the Serial Number field of the Panorama web interface, enter the serial
    number that you copied from the license activation page, and then select
    OK.

    Panorama will become unresponsive after you select
    OK. If it does not return after a few minutes, refresh your browser.
19. Change the Panorama update server location to the update
    server in China.
    1. In Panorama,
       go to PanoramaSetupServices and click the gear
       to edit the Settings.
    2. Change the update server to
       updates.paloaltonetworks.cn.
    3. Update the DNS servers and NTP servers to the servers of your choice.

       ![]()
20. Perform a local commit to Panorama from CommitCommit to Panorama.

    ![]()
21. Upgrade the Cloud Services plugin to the minimum required version.
    1. From the Panorama that manages Prisma Access, select PanoramaPlugins and click Check Now to display the
       latest Cloud Services plugin updates.
    2. Download the plugin version you want to
       install.
    3. After downloading the plugin, Install it.
22. Open a CLI session with the Panorama appliance and enter the following commands
    to make sure that the Panorama appliance points to the Customer Support Portal
    that contains Prisma Access China and Panorama Assets to retrieve its one-time
    password (OTP):

    debug plugins cloud\_services set-csp-endpoint
    api.sb.prismaaccess.com

    debug plugins cloud\_services set-csp-trusted-endpoint
    api-trusted.sb.prismaaccess.com

    request certificate secure-bridge enable

    If you do not enter these commands, the Panorama appliance will not be able
    to retrieve the OTP or certificate.
23. Generate
    your one-time password (OTP) from Common
    ServicesTenant ManagementTenant
    nameGenerate OTP for setting
    up Panorama.

    ![]()
24. After you validate your OTP, the Cloud Services page will become available.
    However, it might take up to 2 hours for the China region of Strata Logging Service to show up
    under Settings; until it does, you can't save your configuration.
25. Complete the product setup:

    - Prisma Access (Managed by Panorama)
      [Administrators
      Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prepare-the-prisma-access-infrastructure/get-started-with-prisma-access-overview)
    - Strata Logging Service
      [Getting Started
      Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
    - Prisma Access
      [Insights
      Administrators Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-insights/insights)
    - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
    - [Enterprise DLP](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp)
    - [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline)

---

<a id="pa-activate-a-license-for-prisma-access-managed-by-strata-cloud-manager-and-prisma-sd-wan-bundle-through-common-services"></a>

#### Activate a License for Prisma Access (Managed by Strata Cloud Manager) and Prisma SD-WAN Bundle Through Common Services

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/activate-a-license-for-cloud-managed-prisma-access-and-prisma-sd-wan>*

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) and Prisma SD-WAN tenants
through Common Services

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma Access and Prisma SD-WAN bundle license - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser |

After you receive an email from Palo Alto Networks identifying the license you are
activating, including all your add-ons and capacities, use the activation link to
begin the activation process. The service will help you with the process of claiming
your license, creating your tenant, and managing your users.

Select Activate Subscription in your email.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the Multitenant
   Superuser role.
2. Allocate the subscription to the recipients of your choice.

   For Managed Security Service Providers (MSSPs) and distributed enterprises,
   you can allocate the subscription directly on any tenant in the hierarchy.
   [What is a tenant?](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) For a Prisma SD-WAN tenant, allocating the license at the
   child-level automatically provisions it at the top-most, root-level, parent
   Prisma SD-WAN tenant as well. This enables the
   parent tenant to do ION device management for the child tenants.

   After activation, you can build out your tenant hierarchy as needed. You can
   create your tenant hierarchy to reflect your existing organizational
   structure. You can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access)
   when creating the hierarchy, in addition to [tenant hierarchy limits](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants).

   However, any tenants that you create between the child tenant and the
   top-most, root-level, parent tenant do not get automatically provisioned
   with the license. That is a one-time process that happens only at
   activation.

   1. Create a new tenant from All Tenants +.

      ![]()
   2. Name the tenant and select Done.

      ![]()
   3. (Optional) For Managed Security Service Providers (MSSPs) and
      distributed enterprises, create a new child tenant by selecting Edit+ from the parent tenant that you previously created.

      ![]()
   4. (Optional) Name the child tenant and select
      Done.

      ![]()
3. Select the Region where you want to deploy your product.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
4. Create New
   Strata Logging Service for storing logs, amount of data log storage,
   and Strata Logging Service Region is populated based on your earlier
   region selection.
5. (Optional) Select a Cloud Identity Engine for
   this tenant.
6. Agree to the Terms and Conditions.
7. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or Strata Logging Service) are
   now provisioned. As the subscriptions are activating, the progress status will
   display. When the process is complete, the tenant status displays as
   Up. You now have a tenant provisioned with
   instances of the products that you purchased. The tenant has one user — the
   account that you used when you began this process.
8. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - Prisma Access
     [Prisma Access
     Administrator's Guide](https://docs.paloaltonetworks.com/prisma-access)
   - Prisma SD-WAN
     [Administration Guide](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan)
   - [Open APIs](https://pan.dev/sase/docs/)
   - Strata Logging Service
     [Getting Started
     Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
9. (Optional) In a multitenant hierarchy, monitor your tenants with the
   [SASE Summary Dashboard](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-summary).
10. (Optional) [add user access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-users) and [assign roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles).

---

<a id="pa-prisma-access-onboarding-workflow"></a>

### Prisma Access Onboarding Workflow

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access>*

Learn how to onboard Prisma Access after activating your license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) (*new   deployments only*) | - Prisma Access license - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license) 6.0   or later |

The Prisma Access onboarding
workflow uses a simplified initial setup process for new Prisma Access deployments.
This workflow rapidly deploys and configures various Prisma Access components,
including mobile users and private applications. This guided workflow can significantly
reduce deployment time.

The Prisma Access onboarding
workflow provides best practice defaults and automates many backend tasks, simplifying
the configuration process. You benefit from the integration of the [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/learn-about-the-cloud-identity-engine) and [Strata Cloud Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/workflows-prisma-access-setup) with Prisma Access
components in a single, cohesive interface. The setup is context-driven and based on
your activated licenses, ensuring that you only configure what's necessary for your
deployment.

Included with the Prisma Access onboarding workflow are automated Day 0 Security
policy creation and simplified configuration for services such as [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-basics/url-filtering-overview) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security/administration/about-dns-security). By using this
onboarding workflow, you can accelerate your time-to-value, reduce complexity in the
setup process, and ensure your Prisma Access deployment adheres to recommended best
practices. This process is particularly useful if you're new to Prisma Access or
want to quickly set up a new deployment with minimal manual configuration.

You can only use these onboarding
workflows when setting up Prisma Access for the first time. After you save your
changes and complete the setup, modify your Prisma Access deployment using the Prisma Access web interface.

- [GlobalProtect Onboarding Workflow](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-globalprotect-deployments.html)
- [Explicit Proxy Onboarding Workflow](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-explicit-proxy-deployments.html)
- [Site-Based Remote Network Onboarding
  Workflow](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html#tabs-use-branch-sites-to-set-up-high-bw-rns)

  If you have an existing Remote
  Network deployment; use the onboarding workflow for [Remote Networks—High Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance).
- [Service Connection Onboarding Workflow](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-service-connections.html)
- [ZTNA Connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-ztna-connector.html)

If you have not
upgraded to Prisma Access 6.0, use these instructions to set up Prisma Access:

- Secure access [for your mobile users](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users) by implementing:
  - [Agent-based tunnels using
    GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
  - [Explicit Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
  - A hybrid deployment with GlobalProtect and Explicit Proxy using [tunnel and proxy mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-tunnel-and-proxy-mode)
- Secure access to your branch sites using [Remote Networks](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks) or a [Remote Network—High
  Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance)
- Secure access to private apps by implementing:
  - [Service Connections](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-service-connections)
  - [ZTNA Connector](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access)
  - [Colo-Connect](https://docs.paloaltonetworks.com/prisma-access/administration/colo-connect-in-prisma-access)

---

<a id="pa-onboarding-workflow-for-prisma-access-globalprotect-deployments"></a>

#### Onboarding Workflow for Prisma Access GlobalProtect Deployments

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-globalprotect-deployments>*

Learn how to set up Prisma Access agent-based access deployments for the first
time.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager)   (*new deployments only*) | - Prisma Access license - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   6.0 or later |

To secure mobile users with [GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect) or a hybrid deployment using
GlobalProtect and Explicit Proxy in [Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-proxy-mode) or [Tunnel and Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-tunnel-and-proxy-mode), complete this task.

1. Go to ConfigurationOnboardingOnboard Users.
2. In the Onboard Users area,
   Configure GlobalProtect agent-based access.

   You might not see the same choices in your Prisma Access deployment; the choices you see in the UI depend on the
   licenses you have. For example, if you don't have a [site-based remote network license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/remote-networks-site-based-licensing.html),
   you don't see a choice to onboard branch sites.

   ![]()
3. In the Agent-Based Access area,
   Enable GlobalProtect Mobile users.

   ![]()
4. Specify authentication for your mobile users.

   You can use either the Cloud Identity Engine or Prisma Access Authentication.
   Cloud Identity Engine authentication is recommended since Prisma Access
   Authentication only authenticates the current tenant.

   - To use the Cloud Identity Engine for authentication, select
     Cloud Identity Engine and, if you have
     already created an authentication profile, enter it. 

     ![]()

     If you have not created a profile, follow the steps below to
     create a new profile.
     1. Add New.

        To use the Cloud Identity Engine with an identity
        provider (IdP) vendor, [configure a
        cloud-based directory](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory) in the Cloud Identity
        Engine before starting this procedure.

        ![]()
     2. Configure IdP for SAML authentication by selecting an
        Identity Provider Vendor for SAML
        2.0.

        ![]()
     3. Download the Metadata file.
     4. Set up an IdP profile.

        You can either upload a metadata
        file you downloaded (Upload
        Metadata) or a URL (Enter
        URL).

        The Identity
        Provider ID, Identity
        Provider Certificate,
        Identity Provider SSO URL,
        and HTTP Binding for SSO Request to Identity
        Provider fields populate using the
        metadata file or URL you provided. If you see any issues
        with the information in these fields, correct it on the
        IdP vendor site and upload the metadata again.

        Test SAML
        setup to verify the SAML IdP
        configuration with Prisma Access.

        ![]()
     5. Select the Username Attribute for the
        Cloud Identity Engine to use for authentication and
        Confirm your changes.

        Select
        the username attribute that uses the Name
        (/identity/claims/name)
        format. If you don’t select the correct username
        attribute, user authentication for projects isn’t
        successful. For more information, refer to the [Microsoft
        documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/the-role-of-claims).

        ![]()
     6. Enter a CIE Authentication Profile
        Name for the profile you created and
        Finish the setup.

        ![]()
   - To use local authentication, select Prisma Access
     Authentication.

     ![]()

     Prisma Access creates a local profile for you and you can
     [add local users and groups](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access/identity-services/local-users-and-groups)
     to the profile. Confirm your changes when
     complete.
5. Go to the Next setup screen.
6. Set up portal information, access mode, and the infrastructure subnet to
   use.

   For local access mode, you can specify to use agent-based mobile user access
   only (Tunnel Mode), or using agent-based access with
   Explicit Proxy in either [Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-proxy-mode) or [Tunnel and Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-tunnel-and-proxy-mode).

   1. Select a Portal Name Type.

      - Default Domain—Your portal hostname uses
        the default domain name:
        <portal-hostname>.gpcloudservice.com.
        Enter a **Portal Hostname** to append to the default domain
        name. Prisma Access for Users will automatically create the
        necessary certificates and publish the hostname to public DNS
        servers.
      - Custom Domain—[Customize the portal
        address](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/set-up-globalprotect-mobile-users?otp=id741805cc-60d7-4074-978a-9acf7689ae19) if you want to change the domain in the
        portal hostname (for example,
        mycompanyportal.mycompanydomain.com).
   2. Enter the Portal Hostname.

      ![]()
   3. Select the Agent Mode for Prisma Access.

      - Tunnel Mode—Secure traffic with a tunnel
        from the users' endpoint devices to Prisma Access. This mode
        does not require setting up Explicit Proxy.

        The following
        modes require that you set up Explicit Proxy as well as an
        agent:
      - **[Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-proxy-mode)**—Use
        this mode if you want to use tunnel mode as a proxy service.
        This mode is useful if you have an existing (legacy) proxy
        architecture or have a requirement to maintain your proxy
        architecture for regulatory or compliance reasons. To use this
        mode, you also set up Explicit Proxy.
      - **[Tunnel and Proxy
        Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-tunnel-and-proxy-mode)**—Use this mode to send internet-bound
        traffic to the internet-based rules defined in a PAC file. The
        remaining traffic uses split tunneling rules and logic defined
        in the PAC file to determine which traffic to send through the
        tunnel and which traffic can bypass the tunnel. To use this
        mode, you also set up an Explicit Proxy.

        If you select
        Proxy Mode or Tunnel
        and Proxy Mode, configure these additional
        options:

        ![]()

        - Select the locations to use with Explicit Proxy
          (Prisma Access Locations for
          Proxy), as well as the locations to use
          with agent-based access (Prisma Access
          Locations for Tunnel).

          Explicit Proxy
          locations [are a subset](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations?otp=idaaf4f030-a095-40ea-b70a-3a3cdc3e2932)
          of agent-based access locations.
        - If authentication traffic is used in Explicit Proxy,
          specify the Authentication
          Domains that are used in the
          authentication traffic flow. Explicit Proxy requires
          decryption to authenticate users. 

          ![]()
        - Enter the [PAC file](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/pac-file-guidelines) to
          use with Explicit Proxy.

          Prisma Access provides
          you with a default PAC file. Edit the existing PAC
          file or create a new PAC file to use with Explicit
          Proxy.

          You can also use [Forwarding
          Profiles](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/explicit-proxy-forwarding-profiles) with Explicit Proxy.

          ![]()
   4. If your license includes remote networks or service connections,
      Show Advanced Options and enter an
      Infrastructure Subnet and BGP
      AS.

      Prisma Access uses the infrastructure subnet to create the
      network backbone for communication between your branch sites, mobile
      users and the Prisma Access security infrastructure, as well as
      with the HQ and data center networks you plan to connect to Prisma Access over service connections.

      Prisma Access provides you with a default
      Infrastructure Subnet of
      192.168.255.0/24. If you want to create a custom infrastructure
      subnet:

      Note: In addition to this Infrastructure Subnet, Prisma Access
      provides you a default [Client IP Pool](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/ip-address-pools-for-a-globalprotect-mobile-users-deployment) of
      100.127.0.0/16. Prisma Access assigns an IP address from this
      pool to each GlobalProtect-connected device. We recommend that
      the number of IP addresses in this pool is 2 times the number of
      mobile user devices that will connect to Prisma Access. If you
      want to modify this subnet, [you can do so](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/set-up-globalprotect-mobile-users#idc777c6e5-19b4-4f05-bf7d-2c50d6017266) after
      you complete the onboarding workflow.

      - Use an RFC 1918-compliant subnet. While the use of non-RFC
        1918-compliant (public) IP addresses is supported, we don't
        recommend it because of possible conflicts with the internet
        public IP address space.
      - Don’t specify any subnets that overlap with the
        169.254.0.0/16 and 100.64.0.0/10 subnet range because Prisma Access reserves those IP addresses and subnets
        for its internal use.
      - This subnetwork is an extension to your existing network and
        therefore, can’t overlap with any IP subnets that you use
        within your corporate network or with the IP address pools
        that you assign for Prisma Access for users or Prisma Access for networks.
      - Because the service infrastructure requires a large number of
        IP addresses, you must designate a /24 subnetwork (for
        example, 172.16.55.0/24).

      For the BGP AS, enter an RFC 6996-compliant
      BGP AS number. This number identifies the routes through which BGP
      can send traffic. If you don’t supply an AS number, Prisma Access uses the default AS number (65534).

      The BGP Private AS number is the autonomous system (AS)

      ![]()
7. Go to the Next setup screen.
8. (Optional) Set the Prisma Access locations and number of mobile users
   per location. This enables the system to allocate the ingress and egress IP
   addresses that you can use for whitelisting.

   1. Expand the IP Capacity Planning section and either upload a CSV file
      with the city and user information or click
      Add.

      If you uploaded a CSV, the city,
      users, and IP address information is populated.

      If you are
      adding this information manually, click
      Add.
   2. Enter the city name and approximate number of users click
      Add.

      The Prisma Access location
      corresponding to each city is displayed. If required, you can change
      the Prisma Access Location by clicking in the cell.
   3. Click Next and then click **Confirm**.

      ![]()

      A table with the IP addresses corresponding to each Prisma
      Access location is displayed.
9. Expand the Prisma Access Locations for Tunnel
   section.

   Prisma Access provides multiple locations within each region to ensure
   that your users connect to a location that provides a user experience
   tailored to the users’ locale. By limiting your deployment to a single
   region, you have more granular control over your deployed regions and
   exclude regions required by your policy or industry regulations.

   If you configured IP capacity, the Prisma Access Locations for
   Tunnel section automatically displays the Prisma Acces
   locations you specified You can select a different location as
   appropriate.

   ![]()
10. Go to the Next setup screen.
11. Configure Security Policy rules for your agent-based
    access Prisma Access deployment.

    To simplify the onboarding process, Prisma Access provides you with
    best practise snippet and folder associations. Click **Associate** next
    to the snippet you want to associate. You can examine the policy rules for
    the sniippet by navigating to ConfigurationNGFW and Prisma AccesConfiguration ScopeSnippetsSecurity Services.

    ![]()

     There are also predefined, best practice settings for decryption bypass,
    Advanced Threat Protection, and Vulnerability Protection. You can modify these
    settings as required. 

    ![]()
12. Finalize your configuration.
    1. Push Config to push your configuration changes
       to Prisma Access.

       ![]()
    2. Select the GlobalProtect version to use.

       Use the recommended version displayed in the web interface, or select
       the GlobalProtect version to use based on your company's policy. 

       ![]()
    3. [Deploy the GlobalProtect app to end
       users](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-apps/deploy-the-globalprotect-app-software).

       You can use a [mobile device management (MDM)](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/mobile-endpoint-management)
       system, or have your users download and install the agent.

---

<a id="pa-onboarding-workflow-for-prisma-access-explicit-proxy-deployments"></a>

#### Onboarding Workflow for Prisma Access Explicit Proxy Deployments

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-explicit-proxy-deployments>*

Learn how to set up Prisma Access Explicit Proxy deployments for the first time.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager)   (*new deployments only*) | - Prisma Access license - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   6.0 or later |

To secure mobile users with [Explicit Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy), complete this task.

1. Go to ConfigurationOnboardingOnboard Users.
2. Configure Explicit Proxy.

   You might not see the same choices in your Prisma Access deployment; the choices you see in the UI depend on the
   licenses you have. For example, if you don't have a [site-based remote network license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/remote-networks-site-based-licensing.html),
   you don't see a choice to onboard branch sites.

   ![]()
3. In the Explicit Proxy area,
   Enable Explicit Proxy.

   ![]()
4. Configure the Explicit Proxy infrastructure and locations.
   1. Enter an FQDN for Explicit Proxy.

      The name for the proxy is
      proxyname.proxy.prismaaccess.com, where
      proxyname is the subdomain you specify.
   2. (Optional) Show Advanced Options and
      enter an Infrastructure Subnet and BGP
      AS.

      An infrastructure subnet is only required if you have the following
      deployments:

      - Explicit Proxy in [Proxy Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-proxy-mode)
      - Explicit Proxy in [Tunnel and Proxy
        Mode](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/agent-based-proxy-globalprotect-tunnel-and-proxy-mode)
      - Explicit Proxy with a [Service
        Connection](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-service-connections/configure-a-service-connection)

      Prisma Access uses the infrastructure subnet to create the
      network backbone for communication between your mobile users and the
      Prisma Access security infrastructure, as well as with the
      HQ and data center networks you plan to connect to Prisma Access
      over service connections. The BGP Private AS number is the
      autonomous system (AS) number that identifies the routes through
      which BGP can send traffic. If you don’t supply an AS number, Prisma Access uses the default AS number (65534).

      Prisma Access provides you with a default
      Infrastructure Subnet of 192.168.255.0/24.
      If you want to create a custom infrastructure subnet:

      - Use an RFC 1918-compliant subnet. While the use of non-RFC
        1918-compliant (public) IP addresses is supported, we don't
        recommend it because of possible conflicts with the internet
        public IP address space.
      - Don’t specify any subnets that overlap with the
        169.254.0.0/16 and 100.64.0.0/10 subnet range because Prisma Access reserves those IP addresses and subnets
        for its internal use.
      - This subnetwork is an extension to your existing network and
        therefore, can’t overlap with any IP subnets that you use
        within your corporate network or with the IP address pools
        that you assign for Prisma Access for users or Prisma Access for networks.
      - Because the service infrastructure requires a large number of
        IP addresses, you must designate a /24 subnetwork (for
        example, 172.16.55.0/24).

      For the BGP AS, enter an RFC 6996-compliant
      BGP AS number. This number identifies the routes through which BGP
      can send traffic. If you don’t supply an AS number, Prisma Access uses the default AS number (65534).

      The BGP Private AS number is the autonomous system (AS)

      ![]()
   3. Enter the Locations for your Explicit Proxy
      mobile users.

      We recommend deploying Explicit Proxy in at least two different [compute locations](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations?otp=idf6de761e-2601-46d8-a61a-aaeb5e030069) for
      redundancy.

      If you're limiting the number of locations, choose locations that are
      closest to your users or in the same country as your users for the
      best user experience. If a location isn’t available in the country
      where your mobile users reside, choose a location that’s closest to
      your users for the best performance.

      ![]()
   4. (Optional) Add domains that you use for authentication to the
      Domains Used in Authentication Flow.

      Explicit Proxy uses decryption on these domains to authenticate users.
   5. (Optional) Edit the [PAC file](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/pac-file-guidelines) in the
      Forwarding Profiles area.

      Either Edit PAC File to edit the existing PAC
      file or Upload New PAC file.

      Prisma Access
      provides you with a default PAC file. Edit the existing PAC file or
      create a new PAC file and upload it to use with Explicit Proxy.

      If you need to set up multiple PAC files,
      you can do that by [creating a forwarding
      profile](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/explicit-proxy-forwarding-profiles) after you complete onboarding.

      ![]()
   6. Go to the Next step.
5. Specify authentication for your mobile users.

   You can use either the Cloud Identity Engine or local authentication.

   - To use the Cloud Identity Engine for authentication:
     1. Select Cloud Identity Engine and, if you
        have already created an authentication profile, enter it. 

        ![]()
     2. If you have not created a profile:

        1. Add New.

           To use the Cloud Identity Engine with an identity
           provider (IdP) vendor, [configure a
           cloud-based directory](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory) in the Cloud Identity
           Engine before starting this procedure.

           ![]()
        2. Configure IdP for SAML authentication by selecting an
           Identity Provider Vendor for SAML
           2.0.

           ![]()
     3. Download the Metadata file.
     4. Set up an IdP profile.

        You can either upload a metadata file
        you downloaded (Upload Metadata) or a
        URL (Enter URL).

        The
        Identity Provider ID,
        Identity Provider Certificate,
        Identity Provider SSO URL, and
        HTTP Binding for SSO Request to Identity
        Provider fields populate using the metadata
        file or URL you provided. If you see any issues with the
        information in these fields, correct it on the IdP vendor
        site and upload the metadata again.

        Test SAML
        setup to verify the SAML IdP configuration
        with Prisma Access.

        ![]()
     5. Select the Username Attribute for the
        Cloud Identity Engine to use for authentication and
        Confirm your changes.

        Select the
        username attribute that uses the Name
        (/identity/claims/name)
        format. If you don’t select the correct username attribute,
        user authentication for projects isn’t successful. For more
        information, refer to the [Microsoft
        documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/the-role-of-claims).

        ![]()
     6. Enter a CIE Authentication Profile Name
        for the profile you created and Finish
        the setup.

        ![]()
   - To use local authentication, select Prisma Access
     Authentication.

     ![]()

     Prisma Access creates a local profile for you and you can
     [add local users and groups](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access/identity-services/local-users-and-groups)
     to the profile. Confirm your changes when
     complete.
6. Configure Security policy rules for your Explicit Proxy Prisma Access
   deployment.

   To simplify the onboarding process, Prisma Access provides you with
   predefined internet access and decryption policy rules based on best
   practices. You can quickly set up IPSec tunnels using defaults suitable for
   the most common IPSec-capable devices and enable SSL decryption for
   recommended URL categories.

   ![]()

    There are also predefined, best practice settings for decryption bypass,
   Advanced Threat Protection, and Vulnerability Protection. You can modify these
   settings as required. 

   ![]()
7. Go to the Next screen and complete your
   configuration.
   1. Push Config to push your configuration
      changes.
   2. Deploy your Explicit Proxy configuration to your mobile uses.

      - Deploy the PAC file using mobile device management (MDM) or
        another method.
      - [Retrieve the IP
        addresses](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/retrieve-ip-addresses-for-prisma-access) used by Explicit Proxy and add them to your
        network's allow lists.
      - Review the [Explicit Proxy best
        practices](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/explicit-proxy-best-practices).
      - If you encounter any issues, use the [Explicit Proxy
        troubleshooting steps](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/monitor-and-troubleshoot-explicit-proxy).

---

<a id="pa-onboarding-workflow-for-remote-networkshigh-performance-with-site-based-licensing"></a>

#### Onboarding Workflow for Remote Networks—High Performance With Site-Based Licensing

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network>*

Deploy your Prisma Access branch sites using using remote networks—high
performance with site-based bandwidth allocation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) (*new deployments   only*) If you have an existing Remote Network   deployment that uses aggregate bandwidth and doesn't use   site-based licensing; use the onboarding workflow for   [Remote Networks—High   Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance). | - Prisma Access license - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   6.0 or later |

As your business scales and your office locations become geographically distributed,
Prisma Access remote networks enable you to quickly onboard your branch
sites and deliver best-in-class security for your users and devices.

Starting with Prisma Access 6.0, you onboard a site by specifying the location
and the site type. The site type enables you to allocate your sites with predefined
bandwidth capacities, ranging from 25 Mbps to 2.5 Gbps. By moving away from
aggregate bandwidth-based licensing, you can more easily estimate and allocate
resources for your remote locations.

To onboard a remote network, you specify the branch site's location, and Prisma Access recommends the location that’s closest to the site. Prisma Access also recommends a secondary location in a separate [compute location](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations?otp=idf6de761e-2601-46d8-a61a-aaeb5e030069) that you can optionally
set up for redundancy and resiliency.

You then select the site type based on its bandwidth (from 25 Mbps up to 2.5 Gbps).

You can begin the configuration process, which includes onboarding the
site-based remote network to Prisma Access and enabling QoS and routing at a
per-site level.

A site-based remote network provides you with up to 2.5 Gbps bandwidth per remote
network tunnel from a remote site.

When configuring a site-based remote network for a branch site, be aware of the
following guidelines and differences between sites and remote networks:

- **Branch Site Planning and Enforcement**—Before you secure your branch site
  with Prisma Access, determine the bandwidth that's required for your site
  and specify one of the site types:
  - Very Small (up to 25 Mbps)
  - Small (up to 50 Mbps)
  - Medium (up to 250 Mbps)
  - Large (up to 1 Gbps)
  - X-Large (up to 2.5 Gbps)

  Prisma Access allows 10% oversubscription and enforces the bandwidth
  based on the site type. For example, if you choose a Very Small site type,
  Prisma Access caps the throughput at 25 Mbps with 10%
  oversubscription.
- **Prisma Access Locations**—Remote Networks—High Performance support
  [a subset](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations?otp=remote-networks-high-performance-locations#remote-networks-high-performance-locations) of Prisma Access
  locations.
- **Quality of Service (QoS)**—For branch sites, Prisma Access supports QoS
  at a per-site level, and the QoS Profile you select applies to the entire site.
- **IPSec Termination Nodes No Longer Needed**—Unlike traditional remote
  networks, you don't need to select an [IPSec termination node](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/planning-checklist-for-remote-networks) during
  onboarding for Prisma Access (Managed by Strata Cloud Manager) deployments. Prisma Access automatically
  load-balances the remote network connections to maximize the bandwidth
  allocation to the sites.
- **Service Endpoint Address Allocation Based on Deployment Type**—The number
  of Service Endpoint addresses that you receive depends on
  if you have set up your site-based remote networks in a single location or if
  you have set them up using two different locations in a primary and secondary
  deployment.

  You use the Service Endpoint address as
  the peer IP or FQDN address on your CPE to terminate the IPSec tunnel.

  As a best practice, specify the
  FQDN instead of the IP address.

  - If you have set up your site-based remote network in a single location
    with no secondary location, Prisma Access provides you with a single
    Service Endpoint address.
  - If you set up compute location redundancy in a primary and secondary
    configuration, Prisma Access provides you with two
    Service Endpoint addresses (one each for the
    primary and secondary location).

  If you set up IPSec tunnels in an Active/Passive configuration, Prisma Access provides you with a single Service
  Endpoint address for both tunnels (the same as a standard
  Prisma Access remote network configuration).

  Remote networks
  use one Service Endpoint address for every 3 Gbps of
  bandwidth, removing the complexity in configuring and managing multiple
  IPSec devices at every remote location.
- **User-ID Redistribution and SSL Decryption**—If you configure an SSL
  decryption profile on your tenant, User-ID redistribution from the Remote
  Networks—High Performance node to service connections is not supported.
- **Unsupported Configurations**— The following features and configurations are
  not supported:
  - [IPv6](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/ipv6-support-for-private-app-access)
  - Prisma Access does not honor the Multi-Exit Discriminator (MED)
    attributes advertised by the CPE. This caveat applies if you use
    multiple BGP peers on either remote network connections or service
    connections and whether or not you select a secondary (backup)
    connection.
  - [Traffic Replication](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/mobile-user-globalprotect-advanced-deployments/traffic-mirroring)
  - [IPSec Serviceability](https://docs.paloaltonetworks.com/prisma-access/release-notes/5-1/prisma-access-about/new-features?otp=concept-nx5_dp3_1bc#concept-nx5_dp3_1bc)
- **Tunnel Modes and Circuit Settings**—A site-based remote network lets you
  configure both location and IPSec redundancy.
  - Location redundancy (specifying a Primary
    location in one [compute location](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations?otp=idf6de761e-2601-46d8-a61a-aaeb5e030069) and
    specifying a Secondary location in a separate
    compute location).

    Configuring a secondary location is optional.
  - IPSec tunnel redundancy (specifying tunnels as
    Active/Active or
    Active/Passive).

  Before you begin setup, it's important to understand how you specify
  circuits and tunnels. Set up circuits and tunnels in the following
  configurations:

  - Active/Passive—Set up either one circuit (the
    default) or two circuits.

    If you specify one circuit (ISP in the
    diagram), configure two tunnels (one for the primary remote network
    location and one for the secondary remote network location). Prisma Access uses this circuit for the tunnels for both the
    primary and secondary locations. If the primary location is
    unreachable (for example, if the tunnels experienced an ISP failure
    or CPE failure, or if the tunnels couldn't be established for any
    other reason), Prisma Access fails over from Tunnel 1 to Tunnel
    2 and switches from the primary to the secondary remote network
    location.

    ![]()

    If you specify two circuits, configure four tunnels (two for
    the primary remote network location and two for the secondary remote
    network location).

    If the primary location is unreachable by
    Tunnel 1, then Tunnel 2 becomes active. If both Tunnel 1 and Tunnel
    2 primary tunnels go down, Prisma Access switches from the
    primary to the secondary location and Tunnel 3 becomes active. If
    Tunnel 3 to the secondary location goes down, then Tunnel 4 becomes
    active.

    ![]()
  - Active/Active—Set up either two circuits (the
    default), three circuits or four circuits.

    If you specify two
    circuits, configure four tunnels. If Tunnel 1 and Tunnel 2 to the
    primary remote network location go down, Tunnels 3 and 4 to the
    secondary remote network location become active. All active tunnels
    to the primary location must go down before Prisma Access fails
    over to the secondary location.

    ![]()

    If you specify three circuits, configure six tunnels. Each ISP
    has one active tunnel to the primary location and one passive tunnel
    to the secondary location. If all active tunnels to the primary
    location go down, the standby tunnels to the secondary location
    become active.

    ![]()

    If you specify four circuits, configure eight tunnels. Each ISP
    has one active tunnel to the primary location and one passive tunnel
    to the secondary location. If all active tunnels to the primary
    location go down, the standby tunnels to the secondary location
    become active.

    ![]()

To configure site-based remote networks, complete one of the following tasks.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network/onboard-a-site-based-remote-network-cloud-management.html#site-based-rns-cloud-management)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network/onboard-a-site-based-remote-network-panorama.html#site-based-rns-panorama)

#### Strata Cloud Manager

Here’s how to add a site-based remote network using Strata Cloud Manager.

1. From Strata Cloud Manager, go to ConfigurationOnboardingOnboard Branch Sites.

   ![]()
2. In Branch Site Management, Add a third-party branch
   site.

   If you are licensed for Prisma SD-WAN
   and want to configure that type of branch site, use [the procedure to configure Prisma
   SD-WAN](https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-native-integrations/onboard-branch-sites-to-prisma-access).
3. Add Site and give the remote network a descriptive
   Site name.
4. Select the City and Country of
   the site.

   For more precise searches, add an
   address.

   ![]()
5. Click Next.
6. Select a location and a site type.
   1. Select a Site Type.

      The types are [based on bandwidth](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html).

      Some locations don't support X-Large sites; in this case, that
      choice is grayed out.
   2. Select a Primary Prisma Access Location.

      If multiple locations are Recommended in the
      list; select the location that works best for your deployment.

      ![]()
7. (Optional) To create a secondary (backup) site, select
   Allow connection to a secondary Prisma Access Location as backup
   when necessary and then select a Secondary Prisma
   Access Location.

   If you select this choice, Prisma Access prepopulates the best secondary
   location or locations that are in a different compute location than the primary
   location. If multiple locations are Recommended; select
   the location that works best for your deployment.

   You can toggle between
   Map View and List View to
   see the best location for your site.

   ![]()
8. Select a QoS Profile to use for this site, or
   Add a new one.

   Prisma Access uses a single QoS Profile per site.

   ![]()

   If you have not yet created a QoS Profile, Add a QoS
   Profile, specifying the following values:

   - Enter a unique QoS Profile Name.
   - Select a Class Bandwidth Type of
     Percentage. Prisma Access does not
     support bandwidth types of Mbps in site-based QoS
     profiles.
   - (Optional) Enter an Egress Guaranteed
     (Mbps) value that represents the guaranteed bandwidth
     for this profile in Mbps.
   - Enter a Class Bandwidth Type of either
     Percentage or Mbps.

     ![]()
   - In the Classes section, Add Class and specify how
     to mark up to eight individual QoS classes.
     - Enter a Class Name.
     - Select the Priority for the class
       (either real-time,
       high,
       medium, or
       low).
     - (Optional) Enter an Egress Max
       that represents the maximum throughput (in Mbps) for traffic
       leaving the service connection or remote network connection.
     - (Optional) Enter an Egress
       Guaranteed value that represents the guaranteed
       bandwidth for this profile (in Mbps).
   - Save your changes, Save
     your QoS profile, and go to the Next step.

   ![]()
9. Define Tunnel & Circuit Settings.
   1. Select a Tunnel Mode: either
      Active/Active or
      Active/Passive.

      The [tunnel mode](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) specifies how many of
      your ISP circuits you want to utilize for the remote network. Specify a
      minimum of one circuit and a maximum of four circuits.
      - If you select Active/Passive (the default
        setting), Prisma Access utilizes either one or two ISP
        circuits to create two active tunnels. If the active tunnel goes
        down, the passive tunnel becomes active.
      - If you select Active/Active, Prisma Access Prisma Access utilizes either two or four ISP
        circuits to create either two or four active tunnels,
        respectively.
   2. Select the Number of circuits to use.

      Prisma Access assigns tunnels [based on the number of
      circuits](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) you specify here, and whether your deployment is
      Active/Active or Active/Passive, as shown in the following table.
   3. (Optional) Configure your IPSec tunnel
      settings.

      Prisma Access provides you with default IPSec tunnel settings.
      These settings determine the IPSec and IKE crypto settings for the
      remote network tunnel. If you want to change them, select the
      Primary Tunnel and
      Edit your settings.

      If you specify a secondary location, Prisma Access autopopulates
      the values from the primary tunnel to the secondary tunnel; to edit
      the secondary tunnel, select that tunnel and
      Edit the settings.

      Make a note of these settings; you must match the settings on the
      customer premises equipment (CPE) that terminates the IPSec tunnel
      at your site.

      - Give the Active tunnel a unique Tunnel
        Name.
      - Specify IPSec Settings.
        - Specify an Authentication type
          (either Pre-Shared Key or
          Certificate).

          If you
          specify Pre-Shared Key, enter
          and confirm the Pre-Shared
          Key.

          If you specify a
          Certificate, enter the
          Local Certificate to use.
          This certificate must already exist in Strata Cloud Manager.
        - (Required for Dynamic Branch IP Addresses Only)
          Specify the IKE Local
          Identification (either IP
          Address, Distinguished Name
          (Subject), User FQDN (email
          address), or FQDN (hostname)
          .
        - (Required for Dynamic Branch IP Addresses Only)
          Specify the IKE Peer
          Identification (either IP
          Address, Distinguished Name
          (Subject), User FQDN (email
          address), or FQDN (hostname).

          If you specify a
          Dynamic branch IP address,
          specify either the IKE Local
          Identification, IKE Peer
          Identification, or both; at least one
          of those IPSec settings are required.

          ![]()
      - Specify the type of Peer ID Check:
        - Exact—Ensures that the local
          setting and peer IKE ID payload match exactly.
        - Wildcard—Allows the peer
          identification to match as long as every character
          before the wildcard (\*) matches. The characters after
          the wildcard don't need to match.
      - (Optional) Permit peer identification and
        certificate payload identification mismatch to
        allow a successful IKE security association (SA) even when the
        peer identification does not match the peer identification in
        the certificate.
      - Choose a Certificate Profile. A
        certificate profile contains information about how to
        authenticate the peer gateway.
      - (Optional) Enable strict validation of
        peer’s extended key use to control strictly how
        the key can be used.
      - Choose the Branch Device IP Address
        (Static or
        Dynamic).
        - If you select Static, enter the
          Static IP Address to use for
          the IPSec tunnel.
        - If you specify Dynamic, which
          obtains the IP address automatically, specify either the
          IKE Local Identification,
          IKE Peer Identification, or
          both; at least one of those IPSec settings are required.
      - (Optional, Recommended) Enable IKE Passive
        Mode to have Prisma Access respond to IKE
        connections but not initiate them.

        While not required,
        IKE Passive Mode is the
        recommended setting.
      - (Optional) Turn on Tunnel
        Monitoring.

        Enter a Tunnel Monitoring
        Destination IP  address on the
        remote network for Prisma Access to determine whether
        the tunnel is up and, if your branch IPSec device uses a
        policy-based VPN, enter the associated Proxy
        ID as the Monitored Proxy
        ID.
      - ![]()
      - (Optional) If you need a proxy ID:
        - Add Proxy ID and enter the
          Proxy ID.
        - Optionally, enter the Local Proxy
          ID and Remote Proxy
          ID.
        - Enter the Protocol to use for the
          proxy ID. Enter a Number,
          TCP, or
          UDP.
        - Specify a Local Port and
          Remote Port for TCP or
          UDP.
        - Save your changes.

        ![]()
      - (Optional) Specify IKE Advanced
        Options.
        - Select an IKE Protocol
          Version.
        - Select an IKEv1 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
        - Select an IKEv2 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
      - (Optional) Specify IPSec Advanced
        Options.
        - Select an IPSec Crypto
          Profile.

          To add a crypto profile,
          Add IPSec. To manage an
          existing IPSec profile, Manage
          IPSec and select the profile to edit.

          ![]()
      - Choose your routing settings.
        - Select the Routing Type (either
          Static or
          Dynamic).

          If you select
          Static,
          Add the IP subnets or IP
          addresses that you want to secure at the
          site.

          If you select
          Dynamic:

          - Enter the Peer As (the
            autonomous system (AS) for your network).

            Use
            an RFC 6996-compliant BGP Private AS
            number.
          - Enter the Peer IP Address
            assigned as the Router ID of the eBGP router on
            the HQ or data center network.
          - (Optional) Enter a Shared
            Secret password to authenticate BGP
            peer communications.
          - Enter the Local IP
            Address that Prisma Access uses as
            its Local IP address for BGP.
          - (Optional) Summarize Mobile
            User Routes before advertising to
            reduce the number of mobile user IP subnet
            advertisements over BGP to your CPE by having Prisma Access summarize the subnets before it
            advertises them.
          - (Optional) Advertise Default
            Route to have Prisma Access
            originate a default route advertisement for the
            remote network using eBGP. Be sure that your
            network does not have another default route
            advertised by BGP, or you could introduce routing
            issues in your network.
          - (Optional) Don't Export
            Routes to prevent Prisma Access
            from forwarding routes into the HQ or data
            center.
   4. Save your IPSec tunnel changes.

      ![]()
10. Save & Exit.
11. Push Configuration to save your configuration changes,
    making sure to select Remote Networks in the
    Push Scope.

    ![]()
12. Find the Service Endpoint address (the IP or FQDN
    address you use on your CPE to terminate the IPSec tunnel).

    As a best practice, specify the FQDN instead of the IP address.

    1. Go to ConfigurationPrisma Access SetupBranch SitesPrisma Access.
    2. Find the Service Endpoint address.

       ![]()

#### Panorama

Configure a Prisma Access remote network deployment that allocates bandwidth by
compute location.

Here’s how to add a site-based remote network in Prisma Access (Managed by Panorama).

Before you start, you can check that your license includes site-based licensing by
going to PanoramaLicenses and view your Sites Capacity and check how
many sites you have remaining per site type. You can onboard any site types that
are remaining in your license.

![]()

. To check:

1. Define tunnel settings and, optionally, QoS settings for your remote
   network.

   During setup, you select an IPSec tunnel and a QoS profile, so you need to
   define those settings before you begin.

   1. Define IPSec tunnel settings for your remote networks by [creating a new IPSec Tunnel](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/set-up-ipsec/set-up-an-ipsec-tunnel)
      and configuring the [IKE Gateway](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/set-up-an-ike-gateway), [IPSec Crypto Profile](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/define-cryptographic-profiles), and
      [Tunnel Monitoring](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-tunnel-monitoring) settings.

      Make a note of these settings; you must match the settings on the
      customer premises equipment (CPE) that terminates the IPSec tunnel
      at your site.

      Be sure that you create the tunnel settings in the
      Remote\_Network\_Template.

      You can also use one of the [predefined IPSec templates](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/predefined-templates-onboard-a-service-connection-or-remote-network)
      in the Remote\_Network\_Template; in this case, you don’t need to
      create a new tunnel.
   2. (Optional) Decide whether you want to add QoS settings to your
      remote network deployment; if you do; [create a QoS Profile](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/qos-for-remote-networks#id09789755-b749-4e05-91a4-e689865695f3) for your
      site-based remote network.

      Be sure that you create the profile in the
      Remote\_Network\_Template.
2. From the Panorama that manages Prisma Access, go to Cloud ServicesConfigurationRemote Networks and Add a site.

   ![]()
3. Give the remote network a descriptive Site Name.
4. Enter the site's City and
   Country.

   For more precise searches, add an address. 

   ![]()
5. Go to the Next screen.
6. Select a site type, a primary location, and, optionally, a secondary
   location.
   1. Select a site type (License Type).

      The types are [based on bandwidth](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html).

      Some locations don't support X-Large sites; in this case, that
      choice isn’t selectable.
   2. Select a Primary Prisma Access Location.

      If multiple locations are Recommended in the
      list; select the location that works best for your deployment.
   3. (Optional) To create a secondary (backup) site, select
      Allow connection to a secondary Prisma Access Location as
      backup when necessary and then select a
      Secondary Prisma Access Location.

      If you select this choice, Prisma Access prepopulates the best
      secondary location or locations that are in a different compute location
      than the primary location. If multiple locations are
      Recommended; select the location that works
      best for your deployment.
   4. (Optional) If you want to enable QoS for your site, select the
      QoS Profile you created at the start of this
      procedure and go to the Next step.

      ![]()
7. Define Tunnel & Circuit Settings.
   1. Select a Tunnel Mode: either
      Active/Active or
      Active/Passive.

      The tunnel mode specifies how many of your ISP circuits you want to
      utilize for the remote network. Specify a minimum of one circuit and a
      maximum of four circuits.
      - If you select Active/Passive (the default
        setting), Prisma Access utilizes either one or two ISP
        circuits to create two active tunnels. If the active tunnel goes
        down, the passive tunnel becomes active.
      - If you select Active/Active, Prisma Access Prisma Access utilizes either two or four ISP
        circuits to create either two or four active tunnels,
        respectively.
   2. Select the Number of circuits to use.

      Prisma Access assigns tunnels [based on the number of
      circuits](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) you specify here, and whether your deployment is
      Active/Active or Active/Passive, as shown in the following table.
   3. Select the IPSec tunnels to use for your primary and secondary sites by
      selecting either:

      - One of the [predefined IPSec
        templates](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/predefined-templates-onboard-a-service-connection-or-remote-network) in the Remote\_Network\_Template
      - An IPSec tunnel you created at the start of this procedure.

      ![]()
   4. Go to the Next step.
8. Choose your Routing Settings.

   - Choose your Routing Settings.
     - Select the Routing Type (either
       Static or
       Dynamic).

       If you select
       Static routing,
       Add the IP subnets or IP
       addresses that you want to secure at the site.

       ![]()

       If you select Dynamic
       routing:

       - Enter the Peer As (the autonomous
         system (AS) for your network).

         Use an RFC
         6996-compliant BGP Private AS number.
       - Enter the Peer IP Address
         assigned as the Router ID of the eBGP router on the HQ
         or data center network.
       - (Optional) Enter a Shared
         Secret password to authenticate BGP peer
         communications.
       - Enter the Local IP Address that
         Prisma Access uses as its Local IP address for
         BGP.
       - (Optional) Select Summarize Mobile
         User Routes before advertising to reduce
         the number of mobile user IP subnet advertisements over
         BGP to your CPE by having Prisma Access summarize
         the subnets before it advertises them.
       - (Optional) Select Advertise Default
         Route to have Prisma Access
         originate a default route advertisement for the remote
         network using eBGP. Be sure that your network does not
         have another default route advertised by BGP, or you
         could introduce routing issues in your network.
       - (Optional) Select Don't Export
         Routes to prevent Prisma Access from
         forwarding routes into the HQ or data center.

     If you have a secondary tunnel, the BGP settings copy over; you
     can use the copied-over settings for the secondary tunnel or modify
     those settings.

     ![]()
9. Click OK to save your changes.
10. Go to CommitCommit and Push and Commit and Push your changes.

    ![]()
11. Find the Service Endpoint address (the IP or FQDN
    address you use on your CPE to terminate the IPSec tunnel).

    As a best practice, specify the FQDN instead of the IP address.

    1. Go to Cloud ServicesConfigurationRemote NetworksPrisma Access.
    2. Find the Service Endpoint address.

       ![]()

---

<a id="pa-onboarding-workflow-for-prisma-access-service-connections"></a>

#### Onboarding Workflow for Prisma Access Service Connections

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-service-connections>*

Learn how to set up Prisma Access service connections for the first time.

[Service connections](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-service-connections) provide access to your
internal resources (for example, resources at a data center or HQ). If your license
includes it, service connections also act as an interconnect between the internal
resources in your network, agent-based mobile users, and users at branch
sites.

To secure private apps using service connections, complete the following task.

1. Go to ConfigurationOnboarding.
2. Configure connectivity to private apps.

   ![]()
3. Create a service connection.

   ![]()
4. Enter infrastructure and DNS settings.

   If your license includes it, Prisma Access uses the infrastructure subnet
   to create the network backbone for communication between your branch sites,
   mobile users and the Prisma Access security infrastructure, as well as
   with the HQ and data center networks you plan to connect to Prisma Access over service connections.

   If you have already added an infrastructure subnet
   or DNS information as part of another Prisma Access onboarding, skip
   this step and go to the Next screen.

   - Enter an Infrastructure Subnet.

     Prisma Access provides you with a default
     Infrastructure Subnet of 192.168.255.0/24.
     If you want to create a custom infrastructure subnet:

     - Use an RFC 1918-compliant subnet. While the use of non-RFC
       1918-compliant (public) IP addresses is supported, we don't
       recommend it because of possible conflicts with the internet
       public IP address space.
     - Don’t specify any subnets that overlap with the
       169.254.0.0/16 and 100.64.0.0/10 subnet range because Prisma Access reserves those IP addresses and subnets
       for its internal use.
     - This subnetwork is an extension to your existing network and
       therefore, can’t overlap with any IP subnets that you use
       within your corporate network or with the IP address pools
       that you assign for Prisma Access for users or Prisma Access for networks.
     - Because the service infrastructure requires a large number of
       IP addresses, you must designate a /24 subnetwork (for
       example, 172.16.55.0/24).
   - Enter an RFC 6996-compliant Infrastructure BGP
     AS.

     The BGP Private AS number is the autonomous system (AS) number that
     identifies the routes through which BGP can send traffic. If you
     don’t supply an AS number, Prisma Access uses the default AS
     number (65534).

     ![]()
   - (Optional) If you have a DNS server that can access your
     internal domains, enter Internal DNS Server
     information to have your internal resources use an alternative DNS
     server.
     - Specify the **Primary DNS** and, optionally, **Secondary
       DNS** server IP addresses.
     - If you want your internal DNS server to only resolve the domains
       you specify, enter the domains to resolve in the **Domain
       Name**. You can specify an asterisk in front of the
       domain; for example, \*.acme.local or \*.acme.com. Prisma Access uses the DNS servers you have specified to resolve the
       domains you add here. 

       ![]()
   - Go to the Next step when complete.
5. Create service connections.

   - Enter a unique Name for the service connection.
   - Enter a Prisma Access Location for the service
     connection.

     Select a location closest to where the internal resources
     are located.
   - (Optional) Enable source NAT for [agent-based access IP address
     pools](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/ip-address-pools-for-a-globalprotect-mobile-users-deployment), IP addresses in the [infrastructure subnet](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/configure-the-prisma-access-service-infrastructure), or
     both.
     - **Enable Data Traffic source NAT**—Performs NAT on Mobile
       User IP address pool addresses so that they are not advertised
       to the data center, and only the subnets you specify at the
       service connections are advertised and routed in the data
       center.
     - **Enable Infrastructure Traffic source NAT**—Performs NAT on
       addresses from the Infrastructure subnet so that they are not
       advertised to the data center, and only those subnets you
       specify at the service connections are advertised and routed in
       the data center.
   - Confirm your changes when done.

     ![]()
6. In the IPSec Tunnel area, Set Up Primary
   Tunnel for the service connection

   ![]()

   1. Select an existing tunnel or Create New.

      ![]()
   2. Enter IPSec tunnel settings for the site.

      Make a note of these settings; you specify the same settings in the
      CPE (such as a next-generation firewall or router) at your data
      center or HQ.

      - Enter a unique Tunnel Name.
      - Enter a Branch Device Type.

        Prisma Access includes predefined IPSec templates for
        common third-party IPSec and SD-WAN devices. These profiles
        expedite and simplify the onboarding of service connections
        and remote network connections that use one of these devices
        to terminate the connection.
      - Specify the Authentication Type.
        - If you specify Pre-Shared Key,
          enter and confirm the Pre-Shared
          Key.
        - If you specify a Certificate,
          enter the Local Certificate to
          use. This certificate must already exist in Strata Cloud
          Manager.
      - Specify the IKE Local Identification
        (either IP Address, KEYID
        (binary format ID string in hex),
        User FQDN (email address), or
        FQDN (hostname).
      - Specify the IKE Peer Identification
        (either IP Address, KEYID
        (binary format ID string in hex),
        User FQDN (email address), or
        FQDN (hostname).
      - Specify the type of Branch Device IP
        Address (either Static IP
        or Dynamic).
        - If you set the Branch Device IP
          Address to
          Static, enter the address
          of the CPE at the branch or HQ location (the peer
          device IP address).
        - If you set the Branch Device IP
          Address to
          Dynamic, you must also add
          the IKE ID for the HQ or data center (IKE
          Local Identification) or for Prisma Access (IKE Peer
          Identification) to enable the IPSec
          peers to authenticate.

          Because you don't have the values to use for the Prisma Access IKE ID (IKE Peer
          Identification) until the service
          connection is fully deployed, you would typically
          want to set the IKE ID for the HQ or data center
          (IKE Local Identification)
          rather than the Prisma Access IKE ID.
      - (Optional) Enable IKE Passive
        Mode so that Prisma Access only response to
        IKE connections and does not initiate them.
      - (Optional) Turn on Tunnel
        Monitoring.

        Enter a tunnel monitoring
        Destination IP address on the HQ
        or data center network for Prisma Access to determine
        whether the tunnel is up. If your branch IPSec device uses
        policy-based VPN, enter one or more associated
        Monitored Proxy IDs. The IP
        address you enter is automatically added to the list of
        branch subnetworks.
      - (Optional) If you need a proxy ID:
        - Add Proxy ID and enter the
          Proxy ID.
        - (Optional) Enter the Local Proxy
          ID and Remote Proxy
          ID.
        - Enter the Protocol to use for the
          proxy ID.
      - (Optional) Specify IKE Advanced
        Options.
        - Select an IKE Protocol
          Version.
        - Select an IKEv1 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
        - Select an IKEv2 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
      - (Optional) Specify IPSec Advanced
        Options.
        - Select an IPSec Crypto
          Profile.

          To add a crypto profile,
          Add IPSec. To manage an
          existing IPSec profile, Manage
          IPSec and select the profile to edit.

          ![]()
   3. Optionally, Set Up Secondary Tunnel to create a
      backup tunnel for the service connection.

      If you specify a secondary location, Prisma Access autopopulates
      the values from the primary tunnel to the secondary tunnel; to edit
      the secondary tunnel, select that tunnel and
      Edit the settings.
   4. Save your changes when done.

      ![]()

      ![]()
7. Set Up routing to enable communication to your internal
   resources.

   ![]()

   - If you're using static routing to route traffic to and from your
     internal resources, add IP Subnets for Static
     Routing.

     ![]()
   - If you're using dynamic (BGP) routing to advertise subnets to your
     private resources, Enable BGP for Dynamic Routing
     and select BGP options.

     Prisma Access
     does not honor the Multi-Exit Discriminator (MED) attributes
     advertised by the CPE. This caveat applies if you use multiple BGP
     peers on either remote network connections or service connections
     and whether or not you select a secondary (backup)
     connection.

     1. (Optional) Select an MRAI Timer
        value.

        BGP routing offers a timer you can use to tailor BGP
        routing convergence in your network called the *Minimum
        Route Advertisement Interval (MRAI)*. MRAI acts to
        rate-limit updates on a per-destination basis, and the BGP
        routers wait for at least the configured MRAI time before
        sending an advertisement for the same prefix. A smaller
        number gives you faster convergence time but creates more
        advertisements in your network. A larger number decreases
        the number of advertisements that can be sent, but can also
        make routing convergence slower. You decide the number to
        put in your network for the best balance between faster
        routing convergence and fewer
        advertisements.

        Configure an MRAI range of between 1
        and 600 seconds, with a default value of 30
        seconds.
     2. To reduce the number of mobile user IP subnet advertisements
        over BGP to your customer premises equipment (CPE), specify Prisma Access to summarize the subnets before it advertises
        them by selecting Summarize Mobile User Routes before
        advertising.

        By default, Prisma Access
        advertises the mobile users IP address pools in [blocks of /24
        subnets](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/how-bgp-advertises-mobile-user-ip-address-pools); if you summarize them, Prisma Access
        advertises the pool based on the subnet you specified. For
        example, Prisma Access advertises a public user mobile IP
        pool of 10.8.0.0/20 using the /20 subnet, rather than
        dividing the pool into subnets of 10.8.1.0/24, 10.8.2.0/24,
        10.8.3.0/24, and so on, before advertising them. Summarizing
        these advertisements can reduce the number of routes stored
        in CPE routing tables. For example, use IP pool
        summarization with cloud VPN gateways (Virtual Private
        Gateways (VGWs) or Transit Gateways (TGWs)) that can accept
        a limited number of routes.
     3. (Optional) If you configured a secondary WAN and you
        need to change the peer address for the secondary (backup) BGP
        peer, select Use different BGP Peer for Secondary
        Tunnel and enter a unique Peer and, optionally,
        Local IP address for the secondary WAN.
     4. Enter the Peer IP Address assigned as the
        Router ID of the eBGP router on the HQ or data center
        network.
     5. To add a community from service connections to the outbound
        prefixes from the eBGP peers at the customer premises equipment
        (CPE), set Add no-export community to
        Enabled Out. This capability is
        disabled by default.

        Don’t select Enabled
        In or Enabled Both as
        these choices are not supported.
     6. (Optional) Select Don’t Export
        Routes to prevent Prisma Access from
        forwarding routes into the HQ or data center.

        By default,
        Prisma Access advertises all BGP routing information,
        including local routes and all prefixes it receives from
        other service connections, remote networks, and mobile user
        subnets. Select this check box to prevent Prisma Access from
        sending any BGP advertisements, but still use the BGP
        information it receives to learn routes from other BGP
        neighbors.

        Because Prisma
        Access does not send BGP advertisements, if you select this
        option you must configure static routes on your on-premises
        equipment to establish routes back to Prisma
        Access.
     7. Enter the Peer IP Address assigned as the
        Router ID of the eBGP router on the HQ or data center
        network.
     8. Enter the Peer AS, the autonomous system
        (AS) for your network.

        Use and RFC 6996-compliant BGP Private
        AS number.
     9. Enter the Local IP Address that Prisma Access uses as its Local IP address for BGP.

        A
        local address is only required if your HQ or data center
        device requires it for BGP peering to be successful. Make
        sure the address you specify does not conflict or overlap
        with IP addresses in the infrastructure subnet or subnets in
        the remote network.
     10. Enter a Secret password and
         Confirm Secret to authenticate BGP
         peer communications.
   - Save your changes when done.

     ![]()
8. Push your configuration changes and set up routing in the data center.
   1. To retrieve the Service IP address (either an IP
      address or FQDN), Retrieve Service IP
      Address.

      Use this address as the peer IP address for your CPE when you set up
      the IPSec tunnel for the remote network connection.

      ![]()
   2. Push Config to save your configuration changes.

      ![]()
9. Set up your data center or HQ to complete the service connection.
   1. Copy the Service IP Address and configure the
      tunnel or tunnels from your CPE on your corporate network back to Prisma Access.
   2. Commit the changes on your CPE.
10. Verify your connection by going to ConfigurationPrisma Access SetupService Connections.

    ![]()

---

<a id="pa-onboarding-workflow-for-prisma-access-ztna-connector"></a>

#### Onboarding Workflow for Prisma Access ZTNA Connector

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-ztna-connector>*

Learn how to set up a Prisma Access ZTNA Connector for the first time.

Zero Trust Network Access (ZTNA) Connector helps connect Prisma
Access to your organization's private apps quickly and securely. It gives
mobile users and branch users access to private apps using an automated secure
tunnel, so you don't have to manually configure IPSec tunnels or routing to your
data center, public cloud environments, or partner networks.

When you deploy ZTNA Connector VMs, they automatically connect to the nearest Prisma Access location to ensure optimal latency. Each
Connector supports up to 2 Gbps of bandwidth per Connector.

Prisma Access blocks all traffic by default. As an
administrator, you must create policy rules that explicitly allow access to private
apps using User-ID, App-ID, and Device-ID. This approach reduces your attack surface
and improves security.

After you allow a connection, Prisma Access:

- Continuously verifies the trust of the connection
- Inspects traffic for threats
- Scans for data leakage

ZTNA Connector also hides the private IP addresses of your apps, adding another layer
of protection.

To secure private apps using ZTNA Connector, complete the following task.

Before you begin, configure the [Application block and Connector](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/enable-ztna-connector) IP
address block and Push Config to save the
configuration.

1. Go to ConfigurationOnboarding.
2. Configure connectivity to private apps.

   ![]()
3. Create a ZTNA Connector.

   ![]()
4. Create a Connector Group.
   1. Add Connector Group, give the Connector Group a
      unique Name, and select the Group
      Type as ZTNA Connector.
   2. (Optional) Add a Description and enable
      Preserve User ID, if required.
   3. Create to add the Connector Group, and then
      select Next.

      ![]()
5. Create a Connector.
   1. Give the Connector a unique Name.
   2. Select the Connector Group and optionally add a
      Description for the Connector, and then
      select Next.

      ![]()
6. Configure Application Targets.
   1. Select the add icon to add a FQDN Target or a
      Wildcard Target.

      ![]()
   2. Configure an FQDN Target:

      1. Add a unique Name for the target and
         assign a Connector Group to associate
         with the target. The Group must be a type of
         FQDN/Wildcard.
      2. Add the FQDN to use with the target.
      3. Enable Microsoft AD Firewall Ports, if
         you want to enable all TCP and UDP ports required for Microsoft
         Active Directory Domain Services.
      4. Select the Protocol
         (tcp, udp or
         both).
      5. (Optional) To enable ICMP protocol from a GlobalProtect user to a ZTNA
         Connector data center Allow ICMP
         Protocol.
      6. Select the **Port** to use for the app.

         Enter ports in one
         or more of these formats:
         - A single port
         - Multiple ports using commas between the ports
         - A range of ports using dashes
         - A range of ports using commas and dashes

         If you have selected **both** under
         **Protocol**, add ports to **TCP Port** and **UDP
         Port**.

         When you enter a range in the **TCP
         Port** field, under **Advanced Settings**, **icmp
         ping** and **Probing Type** of **none** are
         activated.
      7. Enter a Probing Type of tcp
         ping, icmp ping, or
         none, depending on the protocol you
         select.

         If you select tcp ping,
         select a Probing Port, and enter a
         single port. The port does not have to be in the range of
         ports you entered in the **Port** and
         Protocol area. ZTNA Connector
         determines the reachability of the app by performing a TCP
         ping from the probing port to the FQDN's resolved IP
         address. If the ping is successful, the app is considered
         **Up**.

         You can also edit the probing port,
         which you have added during application onboarding. When the
         probe port is updated, ZTNA Connector starts a TCP probing
         application on the updated port and the application status
         is updated accordingly.

         If you select icmp
         ping, ZTNA Connector performs an ICMP ping
         to the FQDN's resolved IP address. When a response is
         received to the ICMP ping, the app is considered **Up**.
         If you select none, no probing is
         performed and the application is always marked as
         **Up**.
      8. Select Enabled to create the target.
      9. (Optional) Enable Keep Data Center IP
         Address.

         Normally, FQDN targets are allocated
         an IP address from the ZTNA Connector IP Blocks and DNS
         Proxies. However, Microsoft Active Directory DS applications
         won't function properly with DNS Proxy NAT. FQDN targets
         with Keep Data Center IP Address keep
         the data center IP address resolved at the ZTNA Connector
         DNS Server. DNS Resolution must be consistent with no
         overlapping IP addresses.
      10. Create to add the required FQDN
          target.

      ![]()
   3. Configure a Wildcard Target:

      1. Add a unique Name for the target and
         assign a Connector Group to associate
         with the target. The Group must be a type of
         FQDN/Wildcard.
      2. Add the Wildcard to use with the
         target.

         Enter it in the format of .example.com or
         .my.example.com (the UI implicitly adds the asterisk to the
         front of the wildcard). Don't allow all sites by specifying
         a wildcard of \*.\*, example.\*.com, or \*.com.
      3. Enable Microsoft AD Firewall Ports, if
         you want to enable all TCP and UDP ports required for Microsoft
         Active Directory Domain Services.
      4. Select the Protocol
         (tcp, udp or
         both).
      5. (Optional) To enable ICMP protocol from a GlobalProtect user to a ZTNA
         Connector data center Allow ICMP
         Protocol.
      6. Select the **Port** to use for the app.

         Enter ports in one
         or more of these formats:
         - A single port
         - Multiple ports using commas between the ports
         - A range of ports using dashes
         - A range of ports using commas and dashes

         If you have selected **both** under
         **Protocol**, you have to add ports to **TCP
         Port** and **UDP Port**.

         When you enter a
         range in the **TCP Port** field, under **Advanced
         Settings**, **icmp ping** and **Probing Type**
         of **none** are activated.
      7. Enter a Probing Type of tcp
         ping, icmp ping, or
         none, depending on the protocol you
         select.

         If you select tcp ping,
         select a Probing Port, and enter a
         single port. The port does not have to be in the range of
         ports you entered in the **Port** and
         Protocol area. ZTNA Connector
         determines the reachability of the app by performing a TCP
         ping from the probing port to the FQDN's resolved IP
         address. If the ping is successful, the app is considered
         **Up**.

         You can also edit the probing port,
         which you have added during application onboarding. When the
         probe port is updated, ZTNA Connector starts a TCP probing
         application on the updated port and the application status
         is updated accordingly.

         If you select icmp
         ping, ZTNA Connector performs an ICMP ping
         to the FQDN's resolved IP address. When a response is
         received to the ICMP ping, the app is considered **Up**.
         If you select none, no probing is
         performed and the application is always marked as
         **Up**.
      8. Select Activated to create the
         target.
      9. (Optional) Enable Keep Data Center IP
         Address.

         Normally, FQDN targets are allocated
         an IP address from the ZTNA Connector IP Blocks and DNS
         Proxies. However, Microsoft Active Directory DS applications
         won't function properly with DNS Proxy NAT. FQDN targets
         with Keep Data Center IP Address keep
         the data center IP address resolved at the ZTNA Connector
         DNS Server. DNS Resolution must be consistent with no
         overlapping IP addresses.
      10. Create to add the required Wildcard
          target and select Next.

      ![]()
7. Retrieve the key and token to set up and activate and authenticate the
   connectors. For advanced monitoring and troubleshooting, navigate to ConfigurationZTNA ConnectorConnectors.

   ![]()
8. Complete the setup by [deploying your ZTNA Connector VMs in your
   data center](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/ztna-connector-in-prisma-access/onboard-a-cloud-instance-or-vm-for-the-ztna-connector.html).
9. Navigate to ConfigurationNGFW and Prisma Access to create a Security policy under the Prisma
   Access configuration scope to control user access to the applications
   that ZTNA Connector discovers.
10. [Create security policy rules to allow users
    access to the apps in the connectors](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/ztna-connector-in-prisma-access/ztna-connector-policy-and-access.html).
11. Finish to complete the onboarding process.
12. Push Config to push your configuration changes.
13. (Optional) View [Monitor: Data Centers ZTNA Connectors](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-data-centers#um-monitor-data-centers-ztna-connectors)
    to see how your ZTNA connectors and connector groups are performing.
14. (Optional) If you encounter issues with accessing private apps using
    ZTNA Connector, use the [ping, traceroute, and nslookup](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/ztna-connector-in-prisma-access/configure-a-ztna-connector/ztna-connector-diagnostic-tools.html)
    diagnostic tools to check app reachability.

---

<a id="pa-prisma-access-activation-and-onboarding"></a>

## Prisma Access Activation and Onboarding

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding>*

---

<a id="pa-first-time-prisma-access-managed-by-strata-cloud-manager-and-add-ons-activation"></a>

###### First Time Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/activate-cloud-managed-prisma-access-and-add-ons-first-time-one-csp>*

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through
Common Services for the first time if you have only one Customer Support Portal
account.

If you have only one Customer Support Portal account, follow these steps for
first-time Prisma Access (Managed by Strata Cloud Manager) and add-ons license activation.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the 
   Superuser role.
2. Choose Cloud management for your setup and management
   method.

   ![]()
3. Allocate the subscription to the recipients of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)

   1. If you need just one tenant, use or rename the tenant provided. The
      name provided matches your Customer Support Portal account for
      convenience.

      ![]()
   2. (Optional) This step applies if you are a managed security
      service provider (MSSP), a distributed enterprise customer, or need
      multiple tenants. After you create the first tenant, you can
      Allocate to subtenant and use or rename the
      tenant provided.

      ![]()

      A subscription gets allocated on a tenant or a sub-tenant. This step
      is for choosing a tenant where you want to allocate a license, not
      for building a complete tenant hierarchy. You can create only a
      tenant and subtenant here, and you can choose to allocate a license
      to that subtenant.

      After activation, you can build out your tenant hierarchy as needed
      through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants). You can
      create your tenant hierarchy to reflect your existing organizational
      structure. You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy
      limits](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants).

      After you create a tenant hierarchy, you can [share a
      license.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access.html)
   3. Select Done.

   After first time or return visit license activation, continue with the
   following steps:
   1. [Allocate
      licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html)
   2. [Plan service
      connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html)
   3. [Add additional
      locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html)
   4. [Enable available add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html)
   5. [Search for subscription
      details](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions)
   6. [Increase subscription
      quantity](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity.html)
   7. [First time setup](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/first-time-multitenant-setup) for Prisma Access multitenancy.

---

<a id="pa-return-visit-prisma-access-managed-by-strata-cloud-manager-and-add-ons-activation"></a>

###### Return Visit Prisma Access (Managed by Strata Cloud Manager) and Add-Ons Activation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/activate-cloud-managed-prisma-access-and-add-ons-repeat-visits>*

Learn how to activate your Prisma Access (Managed by Strata Cloud Manager) tenants through Common Services for repeat visits.

Follow these steps if you have already completed Prisma Access and add-ons
license activation, you have already created your tenant hierarchy through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants), and you are returning
to activate another license in your existing hierarchy.

1. Log in with your email address.
2. Choose Cloud management for your setup and management
   method.

   ![]()
3. Allocate the subscription to the recipient tenant of your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()

   After first time or return visit license activation, continue with the
   following steps:
   1. [Allocate
      licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access.html)
   2. [Plan service
      connections](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access.html)
   3. [Add additional
      locations](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/add-additional-locations-cloud-managed-prisma-access.html)
   4. [Enable available add-ons](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access.html)
   5. [Search for subscription
      details](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions)
   6. [Increase subscription
      quantity](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/increase-subscription-quantity.html)
   7. [First time setup](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/first-time-multitenant-setup) for Prisma Access multitenancy.

---

<a id="pa-strata-cloud-manager"></a>

##### Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network/onboard-a-site-based-remote-network-cloud-management>*

Here’s how to add a site-based remote network using Strata Cloud Manager.

1. From Strata Cloud Manager, go to ConfigurationOnboardingOnboard Branch Sites.

   ![]()
2. In Branch Site Management, Add a third-party branch
   site.

   If you are licensed for Prisma SD-WAN
   and want to configure that type of branch site, use [the procedure to configure Prisma
   SD-WAN](https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-native-integrations/onboard-branch-sites-to-prisma-access).
3. Add Site and give the remote network a descriptive
   Site name.
4. Select the City and Country of
   the site.

   For more precise searches, add an
   address.

   ![]()
5. Click Next.
6. Select a location and a site type.
   1. Select a Site Type.

      The types are [based on bandwidth](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html).

      Some locations don't support X-Large sites; in this case, that
      choice is grayed out.
   2. Select a Primary Prisma Access Location.

      If multiple locations are Recommended in the
      list; select the location that works best for your deployment.

      ![]()
7. (Optional) To create a secondary (backup) site, select
   Allow connection to a secondary Prisma Access Location as backup
   when necessary and then select a Secondary Prisma
   Access Location.

   If you select this choice, Prisma Access prepopulates the best secondary
   location or locations that are in a different compute location than the primary
   location. If multiple locations are Recommended; select
   the location that works best for your deployment.

   You can toggle between
   Map View and List View to
   see the best location for your site.

   ![]()
8. Select a QoS Profile to use for this site, or
   Add a new one.

   Prisma Access uses a single QoS Profile per site.

   ![]()

   If you have not yet created a QoS Profile, Add a QoS
   Profile, specifying the following values:

   - Enter a unique QoS Profile Name.
   - Select a Class Bandwidth Type of
     Percentage. Prisma Access does not
     support bandwidth types of Mbps in site-based QoS
     profiles.
   - (Optional) Enter an Egress Guaranteed
     (Mbps) value that represents the guaranteed bandwidth
     for this profile in Mbps.
   - Enter a Class Bandwidth Type of either
     Percentage or Mbps.

     ![]()
   - In the Classes section, Add Class and specify how
     to mark up to eight individual QoS classes.
     - Enter a Class Name.
     - Select the Priority for the class
       (either real-time,
       high,
       medium, or
       low).
     - (Optional) Enter an Egress Max
       that represents the maximum throughput (in Mbps) for traffic
       leaving the service connection or remote network connection.
     - (Optional) Enter an Egress
       Guaranteed value that represents the guaranteed
       bandwidth for this profile (in Mbps).
   - Save your changes, Save
     your QoS profile, and go to the Next step.

   ![]()
9. Define Tunnel & Circuit Settings.
   1. Select a Tunnel Mode: either
      Active/Active or
      Active/Passive.

      The [tunnel mode](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) specifies how many of
      your ISP circuits you want to utilize for the remote network. Specify a
      minimum of one circuit and a maximum of four circuits.
      - If you select Active/Passive (the default
        setting), Prisma Access utilizes either one or two ISP
        circuits to create two active tunnels. If the active tunnel goes
        down, the passive tunnel becomes active.
      - If you select Active/Active, Prisma Access Prisma Access utilizes either two or four ISP
        circuits to create either two or four active tunnels,
        respectively.
   2. Select the Number of circuits to use.

      Prisma Access assigns tunnels [based on the number of
      circuits](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) you specify here, and whether your deployment is
      Active/Active or Active/Passive, as shown in the following table.
   3. (Optional) Configure your IPSec tunnel
      settings.

      Prisma Access provides you with default IPSec tunnel settings.
      These settings determine the IPSec and IKE crypto settings for the
      remote network tunnel. If you want to change them, select the
      Primary Tunnel and
      Edit your settings.

      If you specify a secondary location, Prisma Access autopopulates
      the values from the primary tunnel to the secondary tunnel; to edit
      the secondary tunnel, select that tunnel and
      Edit the settings.

      Make a note of these settings; you must match the settings on the
      customer premises equipment (CPE) that terminates the IPSec tunnel
      at your site.

      - Give the Active tunnel a unique Tunnel
        Name.
      - Specify IPSec Settings.
        - Specify an Authentication type
          (either Pre-Shared Key or
          Certificate).

          If you
          specify Pre-Shared Key, enter
          and confirm the Pre-Shared
          Key.

          If you specify a
          Certificate, enter the
          Local Certificate to use.
          This certificate must already exist in Strata Cloud Manager.
        - (Required for Dynamic Branch IP Addresses Only)
          Specify the IKE Local
          Identification (either IP
          Address, Distinguished Name
          (Subject), User FQDN (email
          address), or FQDN (hostname)
          .
        - (Required for Dynamic Branch IP Addresses Only)
          Specify the IKE Peer
          Identification (either IP
          Address, Distinguished Name
          (Subject), User FQDN (email
          address), or FQDN (hostname).

          If you specify a
          Dynamic branch IP address,
          specify either the IKE Local
          Identification, IKE Peer
          Identification, or both; at least one
          of those IPSec settings are required.

          ![]()
      - Specify the type of Peer ID Check:
        - Exact—Ensures that the local
          setting and peer IKE ID payload match exactly.
        - Wildcard—Allows the peer
          identification to match as long as every character
          before the wildcard (\*) matches. The characters after
          the wildcard don't need to match.
      - (Optional) Permit peer identification and
        certificate payload identification mismatch to
        allow a successful IKE security association (SA) even when the
        peer identification does not match the peer identification in
        the certificate.
      - Choose a Certificate Profile. A
        certificate profile contains information about how to
        authenticate the peer gateway.
      - (Optional) Enable strict validation of
        peer’s extended key use to control strictly how
        the key can be used.
      - Choose the Branch Device IP Address
        (Static or
        Dynamic).
        - If you select Static, enter the
          Static IP Address to use for
          the IPSec tunnel.
        - If you specify Dynamic, which
          obtains the IP address automatically, specify either the
          IKE Local Identification,
          IKE Peer Identification, or
          both; at least one of those IPSec settings are required.
      - (Optional, Recommended) Enable IKE Passive
        Mode to have Prisma Access respond to IKE
        connections but not initiate them.

        While not required,
        IKE Passive Mode is the
        recommended setting.
      - (Optional) Turn on Tunnel
        Monitoring.

        Enter a Tunnel Monitoring
        Destination IP  address on the
        remote network for Prisma Access to determine whether
        the tunnel is up and, if your branch IPSec device uses a
        policy-based VPN, enter the associated Proxy
        ID as the Monitored Proxy
        ID.
      - ![]()
      - (Optional) If you need a proxy ID:
        - Add Proxy ID and enter the
          Proxy ID.
        - Optionally, enter the Local Proxy
          ID and Remote Proxy
          ID.
        - Enter the Protocol to use for the
          proxy ID. Enter a Number,
          TCP, or
          UDP.
        - Specify a Local Port and
          Remote Port for TCP or
          UDP.
        - Save your changes.

        ![]()
      - (Optional) Specify IKE Advanced
        Options.
        - Select an IKE Protocol
          Version.
        - Select an IKEv1 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
        - Select an IKEv2 Crypto
          Profile.

          To add a crypto profile,
          Add IKE. To manage an
          existing IKE profile, Manage
          IKE and select the profile to edit.
      - (Optional) Specify IPSec Advanced
        Options.
        - Select an IPSec Crypto
          Profile.

          To add a crypto profile,
          Add IPSec. To manage an
          existing IPSec profile, Manage
          IPSec and select the profile to edit.

          ![]()
      - Choose your routing settings.
        - Select the Routing Type (either
          Static or
          Dynamic).

          If you select
          Static,
          Add the IP subnets or IP
          addresses that you want to secure at the
          site.

          If you select
          Dynamic:

          - Enter the Peer As (the
            autonomous system (AS) for your network).

            Use
            an RFC 6996-compliant BGP Private AS
            number.
          - Enter the Peer IP Address
            assigned as the Router ID of the eBGP router on
            the HQ or data center network.
          - (Optional) Enter a Shared
            Secret password to authenticate BGP
            peer communications.
          - Enter the Local IP
            Address that Prisma Access uses as
            its Local IP address for BGP.
          - (Optional) Summarize Mobile
            User Routes before advertising to
            reduce the number of mobile user IP subnet
            advertisements over BGP to your CPE by having Prisma Access summarize the subnets before it
            advertises them.
          - (Optional) Advertise Default
            Route to have Prisma Access
            originate a default route advertisement for the
            remote network using eBGP. Be sure that your
            network does not have another default route
            advertised by BGP, or you could introduce routing
            issues in your network.
          - (Optional) Don't Export
            Routes to prevent Prisma Access
            from forwarding routes into the HQ or data
            center.
   4. Save your IPSec tunnel changes.

      ![]()
10. Save & Exit.
11. Push Configuration to save your configuration changes,
    making sure to select Remote Networks in the
    Push Scope.

    ![]()
12. Find the Service Endpoint address (the IP or FQDN
    address you use on your CPE to terminate the IPSec tunnel).

    As a best practice, specify the FQDN instead of the IP address.

    1. Go to ConfigurationPrisma Access SetupBranch SitesPrisma Access.
    2. Find the Service Endpoint address.

       ![]()

---

<a id="pa-panorama"></a>

##### Panorama

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network/onboard-a-site-based-remote-network-panorama>*

Configure a Prisma Access remote network deployment that allocates bandwidth by
compute location.

Here’s how to add a site-based remote network in Prisma Access (Managed by Panorama).

Before you start, you can check that your license includes site-based licensing by
going to PanoramaLicenses and view your Sites Capacity and check how
many sites you have remaining per site type. You can onboard any site types that
are remaining in your license.

![]()

. To check:

1. Define tunnel settings and, optionally, QoS settings for your remote
   network.

   During setup, you select an IPSec tunnel and a QoS profile, so you need to
   define those settings before you begin.

   1. Define IPSec tunnel settings for your remote networks by [creating a new IPSec Tunnel](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/set-up-ipsec/set-up-an-ipsec-tunnel)
      and configuring the [IKE Gateway](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/set-up-an-ike-gateway), [IPSec Crypto Profile](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-site-to-site-vpn/define-cryptographic-profiles), and
      [Tunnel Monitoring](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/set-up-tunnel-monitoring) settings.

      Make a note of these settings; you must match the settings on the
      customer premises equipment (CPE) that terminates the IPSec tunnel
      at your site.

      Be sure that you create the tunnel settings in the
      Remote\_Network\_Template.

      You can also use one of the [predefined IPSec templates](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/predefined-templates-onboard-a-service-connection-or-remote-network)
      in the Remote\_Network\_Template; in this case, you don’t need to
      create a new tunnel.
   2. (Optional) Decide whether you want to add QoS settings to your
      remote network deployment; if you do; [create a QoS Profile](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/qos-for-remote-networks#id09789755-b749-4e05-91a4-e689865695f3) for your
      site-based remote network.

      Be sure that you create the profile in the
      Remote\_Network\_Template.
2. From the Panorama that manages Prisma Access, go to Cloud ServicesConfigurationRemote Networks and Add a site.

   ![]()
3. Give the remote network a descriptive Site Name.
4. Enter the site's City and
   Country.

   For more precise searches, add an address. 

   ![]()
5. Go to the Next screen.
6. Select a site type, a primary location, and, optionally, a secondary
   location.
   1. Select a site type (License Type).

      The types are [based on bandwidth](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html).

      Some locations don't support X-Large sites; in this case, that
      choice isn’t selectable.
   2. Select a Primary Prisma Access Location.

      If multiple locations are Recommended in the
      list; select the location that works best for your deployment.
   3. (Optional) To create a secondary (backup) site, select
      Allow connection to a secondary Prisma Access Location as
      backup when necessary and then select a
      Secondary Prisma Access Location.

      If you select this choice, Prisma Access prepopulates the best
      secondary location or locations that are in a different compute location
      than the primary location. If multiple locations are
      Recommended; select the location that works
      best for your deployment.
   4. (Optional) If you want to enable QoS for your site, select the
      QoS Profile you created at the start of this
      procedure and go to the Next step.

      ![]()
7. Define Tunnel & Circuit Settings.
   1. Select a Tunnel Mode: either
      Active/Active or
      Active/Passive.

      The tunnel mode specifies how many of your ISP circuits you want to
      utilize for the remote network. Specify a minimum of one circuit and a
      maximum of four circuits.
      - If you select Active/Passive (the default
        setting), Prisma Access utilizes either one or two ISP
        circuits to create two active tunnels. If the active tunnel goes
        down, the passive tunnel becomes active.
      - If you select Active/Active, Prisma Access Prisma Access utilizes either two or four ISP
        circuits to create either two or four active tunnels,
        respectively.
   2. Select the Number of circuits to use.

      Prisma Access assigns tunnels [based on the number of
      circuits](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network.html) you specify here, and whether your deployment is
      Active/Active or Active/Passive, as shown in the following table.
   3. Select the IPSec tunnels to use for your primary and secondary sites by
      selecting either:

      - One of the [predefined IPSec
        templates](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/predefined-templates-onboard-a-service-connection-or-remote-network) in the Remote\_Network\_Template
      - An IPSec tunnel you created at the start of this procedure.

      ![]()
   4. Go to the Next step.
8. Choose your Routing Settings.

   - Choose your Routing Settings.
     - Select the Routing Type (either
       Static or
       Dynamic).

       If you select
       Static routing,
       Add the IP subnets or IP
       addresses that you want to secure at the site.

       ![]()

       If you select Dynamic
       routing:

       - Enter the Peer As (the autonomous
         system (AS) for your network).

         Use an RFC
         6996-compliant BGP Private AS number.
       - Enter the Peer IP Address
         assigned as the Router ID of the eBGP router on the HQ
         or data center network.
       - (Optional) Enter a Shared
         Secret password to authenticate BGP peer
         communications.
       - Enter the Local IP Address that
         Prisma Access uses as its Local IP address for
         BGP.
       - (Optional) Select Summarize Mobile
         User Routes before advertising to reduce
         the number of mobile user IP subnet advertisements over
         BGP to your CPE by having Prisma Access summarize
         the subnets before it advertises them.
       - (Optional) Select Advertise Default
         Route to have Prisma Access
         originate a default route advertisement for the remote
         network using eBGP. Be sure that your network does not
         have another default route advertised by BGP, or you
         could introduce routing issues in your network.
       - (Optional) Select Don't Export
         Routes to prevent Prisma Access from
         forwarding routes into the HQ or data center.

     If you have a secondary tunnel, the BGP settings copy over; you
     can use the copied-over settings for the secondary tunnel or modify
     those settings.

     ![]()
9. Click OK to save your changes.
10. Go to CommitCommit and Push and Commit and Push your changes.

    ![]()
11. Find the Service Endpoint address (the IP or FQDN
    address you use on your CPE to terminate the IPSec tunnel).

    As a best practice, specify the FQDN instead of the IP address.

    1. Go to Cloud ServicesConfigurationRemote NetworksPrisma Access.
    2. Find the Service Endpoint address.

       ![]()

---

<a id="pa-cheat-sheet-enterprise-dlp-with-prisma-access-managed-by-strata-cloud-manager"></a>

###### Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Strata Cloud Manager)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access/cheat-sheet-enterprise-dlp-with-prisma-access-cloud-management>*

Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data.

**Important:** If you’re already using Panorama to manage Enterprise DLP for next-gen
firewalls, your DLP configuration (data patterns and DLP profiles) in Prisma Access
Cloud Management is read-only; continue to manage DLP from Panorama.

- [Feature Highlights](#pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_g1l_cjs_zxb)
- [Get Started](#pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_tmf_djs_zxb)

<a id="pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_g1l_cjs_zxb"></a>

###### Feature Highlights

**The Data Loss Prevention Dashboard**

In Strata
Cloud Manager, go to ConfigurationData Loss Prevention to configure and manage Enterprise DLP.

Your Enterprise DLP
configuration is shared across the products where you’re using Enterprise DLP.
So, you might see settings here that were configured elsewhere, and some
settings you can configure here can also be leveraged in other
products.

**Predefined + Custom Enterprise DLP Settings**

Enterprise DLP
includes built-in settings that you can use to quickly start protecting your
most sensitive content:

- [Predefined data patterns](https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/data-patterns-and-data-filtering-profiles)
  specify common types of sensitive information (like credit cards and
  social security numbers) that you might want to scan for and protect
- [Predefined DLP Profiles](https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/data-patterns-and-data-filtering-profiles) group
  together data patterns that commonly require the same type of
  enforcement

You can also create custom data patterns and profiles directly in Prisma
Access Cloud Management.

**Investigation for DLP Incidents**

A DLP
incident is generated when traffic matches a DLP data profile on Prisma Access (Managed by Strata Cloud Manager). On the [DLP Incidents dashboard](https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/view-dlp-log-details), you can view
details for the traffic that triggered the incident, such as matched data
patterns, the source and destination of the traffic, the file and file type. Go
to ConfigurationData Loss PreventionDLP Incidents.

**Scanning for Images in Supported File
Formats**

Strengthen your security posture to further prevent accidental
data misuse, loss, or theft with [Optical Character Recognition (OCR)](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/enable-ocr).
OCR allows the DLP cloud service to scan supported file types with images
containing sensitive information that match your Enterprise DLP filtering
profiles.

**Exact Data Matching (EDM)**

[EDM](https://docs.paloaltonetworks.com/enterprise-dlp/enterprise-dlp-admin/configure-enterprise-dlp/configure-exact-data-matching.html) is an advanced detection tool to
monitor and protect sensitive data from exfiltration. Use EDM to detect
sensitive and personally identifiable information (PII) such as social security
numbers, Medical Record Numbers, bank account numbers, and credit card numbers,
in a structured data source such as databases, directory servers, or structured
data files (CSV and TSV), with high accuracy.

**Role-Based Access for
Enterprise DLP**

You can provide role-based access to Enterprise DLP
controls inside Prisma Access (Managed by Strata Cloud Manager):

- **Data Loss Prevention Admin**—Can access Enterprise DLP settings but
  can't push configuration changes to Prisma Access.
- **Data Security Admin**—Can access Enterprise DLP and SaaS Security
  controls, but can't push configuration changes to Prisma Access.

<a id="pa-id05e49a6c-8ec0-4207-ae24-3fac80eee09b_task_tmf_djs_zxb"></a>

###### Get Started

Here’s how to get up and running with Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager).

1. Check that Your License Covers Enterprise DLP.

   - [Here’s how to
     check what’s available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management.html#id7c606868-9216-4e2f-bf20-00740d888cd4)
2. Enable Role-Based Access for Enterprise DLP.

   - [Here’s how to add a Data Loss
     Prevention Admin or a Data Security Admin](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/app-access-using-roles)
3. Set Up decryption for Enterprise DLP

   Enterprise DLP supports HTTP/1.1. Some applications, like SharePoint and
   OneDrive, support HTTP/2 for uploads by default. To make applications
   that use HTTP/2 compatible with Enterprise DLP, you’ll need to strip
   ALPN headers from uploaded files.

   In Strata Cloud Manager, go to ConfigurationNGFW and Prisma AccessSecurity ServicesDecryption. Select the Prisma Access
   configuration scope and:

   1. Create a decryption profile, and set it to Strip
      ALPN.

      (Find the Advanced Settings in the
      SSL Forward Proxy section).
   2. Add the decryption profile to an SSL Forward
      Proxy decryption rule.
4. Create a Data Pattern.

   Enterprise DLP data patterns specify what content is sensitive and needs
   to be protected—this is the content you’re filtering. You can create a
   [custom data pattern based on regular
   expressions](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-pattern) or a [data pattern based on file
   properties](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-pattern/create-a-file-property-data-pattern).
5. Create a Data Profile.

   Group data patterns that should be enforced the same way into a data
   profile. You can also use data profiles to specify additional match
   criteria and confidence levels for matching.

   Data profiles can contain regular expression data patterns, [Exact Data Matching (EDM)](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-profile) data
   patterns, or a combination of both.

   [Here’s how to create a data
   profile](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-profile)
6. Create a DLP rule.

   Specify the traffic and file types you want Enterprise DLP to protect.
   Set the action for Enterprise DLP to take when it detects a DLP
   incident.

   [Here’s how to create a DLP
   rule](https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/modify-a-dlp-rule-on-prisma-access-cloud-managed)
7. Enable the DLP rule.

   In Prisma Access (Managed by Strata Cloud Manager), a DLP rule is a type of security
   profile. To enable a security profile to enforce traffic: Add it to a
   profile group, and add the profile group to a security rule.

   [Here’s how to enable a security
   profile (including a DLP rule)](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp)

---

<a id="pa-cheat-sheet-enterprise-dlp-with-prisma-access-managed-by-panorama"></a>

###### Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Panorama)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access/cheat-sheet-enterprise-dlp-with-prisma-access-panorama>*

Enterprise DLP on Prisma Access (Managed by Panorama) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data.

Use DLP with Prisma Access (Managed by Panorama) by [installing the Enterprise DLP plugin](https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/install-the-enterprise-dlp-plugin-on-panorama) on the
same Panorama appliance that manages Prisma Access.

If you have migrated from an existing DLP on Prisma Access license to the DLP plugin, the
locations of data patterns and data filtering profiles move in Panorama after the
migration:

- Data
  patterns move from ObjectsCustom ObjectsData Patterns to ObjectsDLPDLP
  Data Patterns.
- Data filtering profiles move from ObjectsSecurity ProfilesData Filtering to ObjectsDLPDLP
  Data Filters.

---

<a id="pa-cheat-sheet-remote-browser-isolation-strata-cloud-manager"></a>

###### Cheat Sheet: Remote Browser Isolation (Strata Cloud Manager)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi/cheat-sheet-rbi-cloud-management>*

Set up Remote Browser Isolation (RBI) to isolate and transfer browsing activity away from
your users' devices and corporate networks to Prisma Access.

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation) creates a no-code
execution isolation environment for a user's local browser, so that no website code
and files are executed on their local browser.

###### Get Started

Here's how to get up and running with RBI.

1. Check that your license covers RBI.

   [Here's how to check
   what’s available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management.html#id7c606868-9216-4e2f-bf20-00740d888cd4)
2. Configure at least one connection method, otherwise you won't be able to
   enable RBI.

   - [Here's how to configure
     GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
   - [Here's how to configure Explicit
     Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy)
   - [Here's how to configure Prisma
     Access Remote Networks](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks)
   - [Here's how to configure a Remote
     Network—High Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance)
3. Enable decryption so that Prisma Access can decrypt and inspect traffic
   to determine what needs to be isolated according to the policies that you
   configured.

   [Here's how to enable
   decryption](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/security-services/decryption)
4. Configure RBI to set up a theme for the remote
   browsing session, define what browser actions are permitted, and defined
   which website categories that your users access in isolation.

   [Here's how you configure
   RBI](https://docs.paloaltonetworks.com/remote-browser-isolation/administration/configure-rbi)

---

<a id="pa-cheat-sheet-remote-browser-isolation-panorama"></a>

###### Cheat Sheet: Remote Browser Isolation (Panorama)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-rbi/cheat-sheet-rbi-panorama>*

Set up Remote Browser Isolation (RBI) to isolate and transfer browsing activity away from
your users' devices and corporate networks to Prisma Access.

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation) creates a no-code
execution isolation environment for a user's local browser, so that no website code
and files are executed on their local browser.

###### Get Started

Here's how to get up and running with RBI.

1. Check that your license covers RBI.

   [Here's how to check what’s
   available with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama.html#idd917c1b3-0181-4d19-978c-11ea4f25948e)
2. Configure at least one connection method, otherwise you won't be able to
   enable RBI.

   - [Here's how to configure
     GlobalProtect](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect)
   - [Here's how to configure Explicit
     Proxy](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy)
   - [Here's how to configure Prisma
     Access Remote Networks](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks)
   - [Here's how to configure a Remote
     Network—High Performance](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/remote-networks-high-performance)
3. Enable decryption so that Prisma Access can decrypt and inspect traffic
   to determine what needs to be isolated according to the policies that you
   configured.

   [Here's how to enable
   decryption](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/security-services/decryption)
4. Configure RBI to set up a theme for the remote
   browsing session, define what browser actions are permitted, and defined
   which website categories that your users access in isolation.

   [Here's how you configure
   RBI](https://docs.paloaltonetworks.com/remote-browser-isolation/administration/configure-rbi#configure-rbi-panorama)

---

<a id="pa-cheat-sheet-saas-security-with-prisma-access-managed-by-strata-cloud-manager"></a>

###### Cheat Sheet: SaaS Security with Prisma Access (Managed by Strata Cloud Manager)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access/cheat-sheet-saas-security-with-prisma-access-cloud-management>*

Integrate SaaS Security Inline with Prisma Access.

|  |
| --- |
|

**[Here’s everything you need to know](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline) to use SaaS Security with Prisma Access (Managed by Strata Cloud Manager).** |

- [Get Started](#pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id56a654cf-29af-43e4-a823-b0160b0bb289)
- [SaaS Policy Recommendations](#pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id874483ef-e1d9-49fc-b624-f68fc0d8b8c4)

<a id="pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id56a654cf-29af-43e4-a823-b0160b0bb289"></a>

###### Get Started

Here’s how to get up and running with SaaS
Security Inline on Prisma Access (Managed by Strata Cloud Manager):

- Confirm that the SaaS Security add-on
  license is included with your Prisma Access subscription.

  Go to ConfigurationNGFW and Prisma AccessOverview. Select the Prisma Access
  configuration scope.
- If you haven’t already, [activate the SaaS Security Inline
  app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/activate-saas-security-inline-on-prisma-access.html) on the Activation Console.

  After activation, SaaS Security Inline automatically discovers all SaaS
  applications and users and analyzes users’ SaaS activity and usage data
  from your Prisma Access logs that are stored in Strata Logging Service.
- Manage administrator roles and access.

  Go to the Activation Console to provide [roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles)-based access to SaaS
  Security [controls](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) in Prisma Access
  Cloud Management.

  To
  comprehensively manage SaaS Security, users must also be an administrator
  for the SaaS Security Inline app. Jump directly from the Prisma
  Access Cloud Management dashboard to the SaaS Security
  Console to [add](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) SaaS Security Inline
  administrators.
- Explore the SaaS Security dashboard
  in Prisma Access (Managed by Strata Cloud Manager).

  Go to ConfigurationSaaS Security.

  All dashboard views are supported
  directly in Prisma Access (Managed by Strata Cloud Manager). Examine these views
  to [identify risky SaaS applications
  and users](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/identify-risky-saas-apps.html) and [SaaS Security
  Posture Management](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm.html#ide2069884-8ab8-485b-9853-81dca764a5e1). SaaS Security Posture Management (SSPM)
  helps detect and remediate misconfigured settings in sanctioned
  SaaS applications through continuous monitoring.

  ![]()
- Review and share the SaaS Security report.

  SaaS Security Inline includes a SaaS Security report that
  provides a snapshot of application usage with advanced aggregated
  data and views. This report serves as a communication tool between
  your SaaS security team and executive management. You can share
  this on-demand PDF report with your SaaS security team for a periodic
  check-in, or email the report to your executives to highlight the
  SaaS applications in use in your organization and the security risks
  they pose.

  - [Here’s more on the SaaS Security
    report](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/saas-security-inline-report.html#id4f415957-b5c1-4e78-bbd8-7e440186f11c)
  - [Here’s how to generate the SaaS
    Security report in the SaaS Security Inline app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)
- See what else you can do with [SaaS Security and](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-cloud-managed) .

<a id="pa-id0f9efe6b-1df5-49c4-bcf2-3961b9be3577_id874483ef-e1d9-49fc-b624-f68fc0d8b8c4"></a>

###### SaaS Policy Recommendations

To gain visibility into and control of SaaS
applications, SaaS Security admins create SaaS rule recommendations
with specific SaaS App-IDs provided by the App-ID Cloud Engine (ACE).

In
Prisma Access (Managed by Strata Cloud Manager), you can now review and choose to
accept the rules that SaaS Security admins recommend. SaaS rule
recommendations are added to your web access policy—you must have [Web Security](https://docs.paloaltonetworks.com/network-security/security-policy/administration/internet-access-rules) enabled to leverage
SaaS rule recommendations.

**Here’s how you can get started
— review the [workflow to review and accept
SaaS policy recommendations](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline) here:**

1. SaaS
   Security admins create SaaS rule recommendations in the SaaS Security
   Inline app or directly in Prisma Access (Managed by Strata Cloud Manager).

   ➡ In Prisma Access (Managed by Strata Cloud Manager), go to ConfigurationSaaS SecurityPolicy Recommendations.

   ![]()
2. You can review and import SaaS rule recommendations.

   Go to ConfigurationNGFW and Prisma AccessSecurity ServicesWeb SecurityWeb Access Policy. Select the Prisma Access
   configuration scope.

   ![]()
3. The SaaS rule recommendations you’ve imported are labeled
   so you can easily identify them.

   ![]()

---

<a id="pa-cheat-sheet-saas-security-with-prisma-access-managed-by-panorama"></a>

###### Cheat Sheet: SaaS Security with Prisma Access (Managed by Panorama)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-saas-security-with-prisma-access/cheat-sheet-saas-security-with-prisma-access-panorama>*

Get up and running with SaaS Security Inline on Prisma Access (Managed by
Panorama).

|  |
| --- |
|

**[Here’s everything you need to know](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-panorama-managed) to use SaaS Security with Prisma Access (Managed by Panorama).** |

###### Get Started

Here’s how to get up and running with SaaS
Security Inline on Prisma Access (Managed by Panorama):

- Confirm that the SaaS Security add-on
  license is included with your Prisma Access subscription.

  Go to PanoramaLicenses to [check what’s available
  with your license](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama.html#idd917c1b3-0181-4d19-978c-11ea4f25948e).
- If you haven’t already, [activate the SaaS Security Inline
  app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/activate-saas-security-inline-on-prisma-access.html) on the Activation Console.

  After activation, SaaS Security Inline automatically discovers all SaaS
  applications and users and analyzes users’ SaaS activity and usage data
  from your Prisma Access logs that are stored in Strata Logging Service.
- Manage administrator roles and access.

  Go to the Activation Console to provide [roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles)-based access to SaaS
  Security [controls](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) in Prisma Access
  Cloud Management.

  To
  comprehensively manage SaaS Security, users must also be an administrator
  for the SaaS Security Inline app. Jump directly from the Prisma
  Access Cloud Management dashboard to the SaaS Security
  Console to [add](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/add-sspm-administrators) SaaS Security Inline
  administrators.
- Explore the SaaS Security dashboard
  in Prisma Access (Managed by Panorama).

  Go to Visibility.

  All [dashboard views](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-api/get-started-with-saas-security-api/navigate-to-saas-security-api-in-cloud-management-console) are supported
  directly in Prisma Access (Managed by Strata Cloud Manager). Examine these views
  to [identify risky SaaS applications
  and users](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/identify-risky-saas-apps.html) and [SaaS Security
  Posture Management](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm.html#ide2069884-8ab8-485b-9853-81dca764a5e1). SaaS Security Posture Management (SSPM)
  helps detect and remediate misconfigured settings in sanctioned
  SaaS applications through continuous monitoring.

  ![]()
- Review and share the SaaS Security report.

  SaaS Security Inline includes a SaaS Security report that
  provides a snapshot of application usage with advanced aggregated
  data and views. This report serves as a communication tool between
  your SaaS security team and executive management. You can share
  this on-demand PDF report with your SaaS security team for a periodic
  check-in, or email the report to your executives to highlight the
  SaaS applications in use in your organization and the security risks
  they pose.

  - [Here’s more on the SaaS
    Security report](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/saas-security-inline-report.html#id4f415957-b5c1-4e78-bbd8-7e440186f11c)
  - [Here’s how to generate the
    SaaS Security report in the SaaS Security Inline app](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/generate-the-saas-security-inline-report.html)
- See what else you can do with [SaaS Security and Panorama Managed
  Prisma Access](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/saas-visibility-and-controls-for-prisma-access-panorama-managed).

---

<a id="pa-validate-your-license-strata-cloud-manager"></a>

##### Validate Your License (Strata Cloud Manager)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-cloud-management>*

Validate your license and what’s supported with it directly
in Prisma Access (Managed by Strata Cloud Manager).

Here’s how to validate your Prisma Access license type, and the services and support it
includes.

You can also double-check that your configuration is compliant with your license coverage; the
License Compliance widget shows you if there are any areas
where your license coverage isn’t aligned with your configuration, so that you can
identify where fixes need to be made. Validate your license and what’s supported with it
directly in Prisma Access (Managed by Strata Cloud Manager). Go to ConfigurationNGFW and Prisma AccessOverviewLicense.

|  |  |
| --- | --- |
|

**VALIDATE YOUR LICENSE** To validate your license information, go to ConfigurationNGFW and Prisma AccessConfiguration ScopePrisma AccessOverviewLicense. |  |

|

**CHECK LICENSE COMPLIANCE**: See if there are any conflicts between your configuration and your license support. For example, this might happen if you change your license type, and a configuration that was previously valid, is no longer supported with the new license type. If you see any issues here:  1. Select the failure to see what needs to be fixed. 2. Do a **License Check** to validate your fixes. |  |

---

<a id="pa-validate-your-license-prisma-access-managed-by-panorama"></a>

##### Validate Your License (Prisma Access (Managed by Panorama))

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/your-prisma-access-license/validate-your-license/validate-your-prisma-access-license-panorama>*

Learn how to determine the Prisma Access license type
you have by checking the Panorama UI.

Some license requirements, such as the requirements you need to [enable tenants in a multitenant configuration](https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/multitenancy-configuration-overview),
are dependent on the type of Prisma Access license you have. To determine your
license type, select PanoramaLicenses and find the information in the Prisma Access area.

Licenses available after November 17, 2020 include the license Edition and
provide you with the type of Prisma Access Locations you
can deploy (either Local or Worldwide locations).

![]()

Licenses available before November 17, 2020, contain the words GlobalProtect
Cloud Service in the license areas and are divided by
remote networks, mobile users, or Clean Pipe.

![]()

---

---

# Strata Cloud Manager - Activation, Onboarding and Settings

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager on 2026-06-27. 53 pages. Absolute URLs.

> Scoped to: /activation-and-onboarding, /getting-started/settings

## Table of Contents

  - [Strata Cloud Manager Licenses](#scm-strata-cloud-manager-licenses)
  - [Activate Your Strata Cloud Manager Licenses](#scm-activate-your-strata-cloud-manager-licenses)
    - [Activate Strata Cloud Manager Essentials](#scm-activate-strata-cloud-manager-essentials)
    - [Activate Strata Cloud Manager Pro](#scm-activate-strata-cloud-manager-pro)
  - [Upgrade to Strata Cloud Manager Pro, from Strata Cloud Manager Essentials](#scm-upgrade-to-strata-cloud-manager-pro-from-strata-cloud-manager-essentials)
  - [Strata Cloud Manager Prerequisites](#scm-strata-cloud-manager-prerequisites)
  - [Migrate from Panorama to Strata Cloud Manager](#scm-migrate-from-panorama-to-strata-cloud-manager)
  - [Migrate from Zscaler to Strata Cloud Manager](#scm-migrate-from-zscaler-to-strata-cloud-manager)
    - [Prepare Your Zscaler Data for Migration](#scm-prepare-your-zscaler-data-for-migration)
    - [Migrate Zscaler Configurations to Strata Cloud Manager](#scm-migrate-zscaler-configurations-to-strata-cloud-manager)
  - [Onboard to Strata Cloud Manager](#scm-onboard-to-strata-cloud-manager)
    - [Onboard NGFWs with Site Management](#scm-onboard-ngfws-with-site-management)
    - [Onboard NGFWs using Zero Touch Provisioning (ZTP)](#scm-onboard-ngfws-using-zero-touch-provisioning-ztp)
      - [Onboard a ZTP NGFW Using the ZTP Web App](#scm-onboard-a-ztp-ngfw-using-the-ztp-web-app)
  - [Validate Strata Cloud Manager Onboarding](#scm-validate-strata-cloud-manager-onboarding)
  - [Operationalize Strata Cloud Manager](#scm-operationalize-strata-cloud-manager)
    - [Example: Manage and Secure Network Security with Strata Cloud Manager](#scm-example-manage-and-secure-network-security-with-strata-cloud-manager)
  - [Device Associations in Strata Cloud Manager](#scm-device-associations-in-strata-cloud-manager)
    - [Device Model Compatibility](#scm-device-model-compatibility)
    - [Firewall and License Type Compatibility](#scm-firewall-and-license-type-compatibility)
- [Strata Cloud Manager Activation & Onboarding](#scm-strata-cloud-manager-activation-onboarding)
      - [Activate Strata Cloud Manager Pro with the Enterprise License Agreement](#scm-activate-strata-cloud-manager-pro-with-the-enterprise-license-agreement)
      - [Activate Strata Cloud Manager Pro with the Enterprise Support Agreement](#scm-activate-strata-cloud-manager-pro-with-the-enterprise-support-agreement)
      - [Activate Strata Cloud Manager Pro for NGFW](#scm-activate-strata-cloud-manager-pro-for-ngfw)
      - [Activate Strata Cloud Manager Pro for Prisma Access](#scm-activate-strata-cloud-manager-pro-for-prisma-access)
      - [Activate Strata Cloud Manager Pro for VM-Series with Software NGFW Credits](#scm-activate-strata-cloud-manager-pro-for-vm-series-with-software-ngfw-credits)
    - [Device Associations (Associate Devices with a Tenant)](#scm-device-associations-associate-devices-with-a-tenant)
    - [Device Associations (Associate Devices with a Product)](#scm-device-associations-associate-devices-with-a-product)
    - [Device Associations (Remove Device Associations)](#scm-device-associations-remove-device-associations)
      - [AIOps for NGFW](#scm-aiops-for-ngfw)
      - [Device Security](#scm-device-security)
      - [SaaS Security Inline](#scm-saas-security-inline)
      - [Strata Cloud Manager](#scm-strata-cloud-manager)
      - [AIOps for NGFW or Strata Cloud Manager](#scm-aiops-for-ngfw-or-strata-cloud-manager)
      - [CASB-X](#scm-casb-x)
      - [Device Security](#scm-device-security-1)
      - [SaaS Security](#scm-saas-security)
    - [Migrate Configurations From Panorama to Strata Cloud Manager (NGFW)](#scm-migrate-configurations-from-panorama-to-strata-cloud-manager-ngfw)
    - [Migrate from Panorama to Strata Cloud Manager (Prisma Access)](#scm-migrate-from-panorama-to-strata-cloud-manager-prisma-access)
    - [Onboard NGFWs, ZTP NGFWs, and VM-Series to Strata Cloud Manager](#scm-onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager)
      - [Onboard NGFWs](#scm-onboard-ngfws)
      - [Onboard VM-Series](#scm-onboard-vm-series)
    - [Onboard Prisma Access to Strata Cloud Manager](#scm-onboard-prisma-access-to-strata-cloud-manager)
    - [Visibility](#scm-visibility)
    - [Configuration Management](#scm-configuration-management)
    - [Strata Cloud Manager Essentials](#scm-strata-cloud-manager-essentials)
    - [Essentials and Pro Feature Support](#scm-essentials-and-pro-feature-support)
    - [Strata Cloud Manager Pro](#scm-strata-cloud-manager-pro)
    - [Strata Cloud Manager Prerequisites for NGFW and VM-Series Funded by Software NGFW Credits](#scm-strata-cloud-manager-prerequisites-for-ngfw-and-vm-series-funded-by-software-ngfw-credits)
    - [Strata Cloud Manager Prerequisites for Prisma Access](#scm-strata-cloud-manager-prerequisites-for-prisma-access)
    - [NGFW](#scm-ngfw)
    - [Prisma Access](#scm-prisma-access)
- [System Settings: Strata Cloud Manager](#scm-system-settings-strata-cloud-manager)

---

<a id="scm-strata-cloud-manager-licenses"></a>

### Strata Cloud Manager Licenses

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support>*

Strata Cloud Manager supports two licensing tiers: Essentials and Pro. Learn about
what's supported for each and how to get started.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | One of these:  - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before these licensing tiers were introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

Strata Cloud Manager provides AI-powered, [unified management and operations](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/whats-supported) for
your NGFWs and Prisma Access. The features and capabilities available to you in Strata
Cloud Manager depend on your licenses.

Strata Cloud Manager supports two licensing tiers—**Strata Cloud Manager Essentials**,
which is free with the purchase of NGFW and Prisma Access, and **Strata Cloud Manager
Pro**, which is available as an upgrade.

Both licenses unlock a range of network security features and management tools
to optimize NGFW and Prisma Access operations. Here is a brief comparison of features
available with Strata Cloud Manager Essentials and Strata Cloud Manager Pro.

![]()

**Important:**

Before we introduced Strata Cloud Manager Essentials and Pro, the AIOps for NGFW and
Prisma Access licenses enabled access to Strata Cloud Manager. If you have AIOps for
NGFW Premium or activated Prisma Access before the two new licensing tiers were
introduced, there is no impact, and you can continue to amend, extend, or renew your
licenses:

- If you're already using Strata Cloud Manager and have **AIOps for NGFW
  Free**, **AIOps for NGFW Premium**, **Prisma Access with Autonomous
  DEM**, or **Strata Logging Service with sized storage**, your existing
  licenses remain unaffected. You can continue to amend, extend, renew, or
  activate these products without any changes.
- Strata Cloud Manager Essentials and Strata Cloud Manager Pro are not
  yet available to activate in customer support portal (CSP) accounts that already
  have: Strata Logging Service with sized storage, AIOps for NGFW Free or Premium,
  or Prisma Access.

#### License Migration for AIOps for NGFW Premium, AI-Powered ADEM, and Strata Logging Service

Palo Alto Networks has announced May 8, 2025, as the [end-of-sale date](https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-sale) for the AIOps for NGFW
Premium, AI-Powered Autonomous Digital Experience Management (ADEM), and Strata
Logging Service with sized storage licenses.

Starting in March 2025, existing customers with these licenses will be
automatically migrated in phases to alternative licenses at no additional cost. The
updated licenses will retain the same expiration dates and terms as the original
licenses.

**Migration Impact**

- The license migration does not disrupt operations.
- Your updated licenses will automatically be reflected in your
  license subscriptions, requiring no action from you.
- You can view product and license changes in the
  Activation Console portal under
  Common Services > Tenant
  Management.
- After the migration, you retain access to all previous product
  capabilities and gain additional features enabled by the updated
  licenses.

Here’s the post migration view of AIOps for NGFW Premium license to Strata Cloud
Manager Pro on the
Activation Console portal. The AIOps for NGFW product
will change to Strata Cloud Manager, and includes Strata Logging Service.

![]()

The following table shows the current products and their migration path:

|  |  |
| --- | --- |
|

**Current Product** | **Migrated to** |

|

AIOps for NGFW Free | Strata Cloud Manager Essentials |

|

Strata Logging Service with sized storage | Strata Logging Service with one year retention |

|

AIOps for NGFW Free + Strata Logging Service with sized storage | Strata Cloud Manager Essentials + Strata Logging Service with one year retention |

|

Prisma® Access + Strata Logging Service with sized storage | Strata Cloud Manager Essentials for Prisma Access + Strata Logging Service with one year retention |

|

Prisma Access + ADEM + Strata Logging Service with sized storage | Strata Cloud Manager Pro for Prisma Access (includes Strata Logging Service with one year retention) |

|

AIOps for NGFW Premium + Strata Logging Service with sized storage | Strata Cloud Manager Pro for NGFW (includes Strata Logging Service with one year retention) |

|

VM-Series funded by Software NGFW Credits + Strata Logging Service with sized storage | VM-Series funded by Software NGFW Credits + Strata Logging Service with one year retention |

|

VM-Series funded by Software NGFW Credits + Strata Cloud Manager with AIOps for NGFW Premium | VM-Series funded by Software NGFW Credits + Strata Cloud Manager Pro |

|

Cloud NGFW + Strata Logging Service with sized storage | Cloud NGFW + Strata Logging Service with one year retention |

- [Feature
  Support](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-feature-support.html#strata-cloud-manager-feature-support)
- [Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-essentials.html#strata-cloud-manager-essentials)
- [Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-pro.html#strata-cloud-manager-pro)

### Essentials and Pro Feature Support

Learn about the features supported for Strata Cloud Manager Essentials and Pro
licensing tiers.

|

Feature Set | Strata Cloud Manager Essentials | Strata Cloud Manager Essentials + Strata Logging Service | Strata Cloud Manager Pro |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

**Operational Health** | | | |

|

Hardware Health incidents | Yes | Yes | Yes |

|

Software and licensing incidents | Yes | Yes | Yes |

|

Deployment specific incidents | No | No | Yes |

|

Forecasting and Anomaly detection in incidents | No | No | Yes |

|

Root Cause Analysis in incidents | No | No | Yes |

|

In-product support ticket creation | Yes | Yes | Yes |

|

Deployment wide status and metric trends | Yes | Yes | Yes |

|

Capacity Analyzer | No | No | Yes |

|

Upgrade Recommendations | No | No | Yes |

|

ServiceNow Integration | Yes | Yes | Yes |

|

API access | Yes | Yes | Yes |

|

**Security Posture** | | | |

|

Custom Configuration Settings | No | No | Yes |

|

Compliance | No | No | Yes |

|

Policy Analyzer (ML) | No | No | Yes |

|

Policy Optimizer (ML) | No | No | Yes |

|

Config Cleanup | No | No | Yes |

|

**Configuration Management** | | | |

|

Cloud Management for NGFW | Yes | Yes | Yes |

|

Cloud Management for Prisma Access | Yes | Yes | Yes |

|

Cloud Management for standalone SD-WAN | Yes | Yes | Yes |

|

Cloud Management for other licensed CDSS subscriptions | Yes | Yes | Yes |

|

Rule Hit Count within the Cloud Manager configuration | No | Yes | Yes |

|

Configuration exceptions from logs | No | Yes | Yes |

|

**Strata Logging Service** | | | |

|

Retention (1 year default) | No | Yes | Yes |

|

Log Forwarding | No | Yes | Yes |

|

**Autonomous Digital Experience Management (ADEM)** | | | |

|

AI-Powered ADEM | No | No | Yes |

|

**Visualization and Reporting Dashboards** | | | |

|

Command Center | No | Yes | Yes |

|

Activity Insights | No | Yes | Yes |

|

Executive Summary | No | Yes | Yes |

|

WildFire dashboard | Yes | Yes | Yes |

|

DNS security dashboard | Yes | Yes | Yes |

|

DLP Incidents dashboard | No | Yes | Yes |

|

SaaS Security dashboard | No | Yes | Yes |

|

Log Viewer | No | Yes | Yes |

|

IOC Search | No | Yes | Yes |

|

SASE Health | No | Yes | Yes |

|

Prisma Access Usage | No | Yes | Yes |

|

Reports | No | Yes | Yes |

|

SD-WAN Dashboard | No | Yes | Yes |

|

IoT Dashboard | Yes | Yes | Yes |

|

CASB-X Dashboard | Yes | Yes | Yes |

|

Branch Sites | No | Yes | Yes |

|

Data Centers | No | Yes | Yes |

|

Network Services | No | Yes | Yes |

|

Prisma Access Locations | No | Yes | Yes |

|

Strata Copilot | Yes | Yes | Yes |

|

AI Canvas | No | No | Yes |

In-App support case creation capability is only available to Strata Cloud Manager Pro
and devices' with platinum support.

### Strata Cloud Manager Essentials

Learn about Strata Cloud Manager Essentials that provides management and security
features, and the features that are available to you for free.

Strata Cloud Manager Essentials is the free tier that offers configuration
management, network security lifecycle management, and can also provide visibility if
the you have Strata Logging Service. It is supported for the below products:

- [Next-Generation Firewalls (NGFW)](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments)
- [VM-Series funded by Software NGFW
  Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license)

[**Strata Logging Service**](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) is available as
an optional add-on for Strata Cloud Manager Essentials. Strata Logging Service provides
centralized log storage and retrieval across your deployment, but you must purchase it
separately from Strata Cloud Manager Essentials.

Here are the features Strata Cloud Manager Essentials gives you:

- [**Command Center and Activity
  Insights**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) provide interactive dashboards that help you
  to know how Palo Alto Networks security services are protecting your network.
  You can interact with data on the applications, threats, users, and security
  subscriptions at work in your network.
- [**Configuration and Policy Management for
  NGFW and SASE**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access) provides centralized configuration
  management across all your firewalls and SASE environments. This ensures
  consistent security policy enforcement and simplifies administrative tasks.
- [**Best Practices Reporting**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
  helps you adopt NGFW and SASE services quickly by providing tools and
  recommendations to align configurations with industry best practices, improving
  the overall security posture.
- [**Health Insights**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards) **and**[**Alerts**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts) provide
  fundamental insights into the operational health of Prisma Access and NGFWs.
  These insights include deployment-wide status updates, key metrics such as
  traffic volumes, and proactive identification of potential hardware or software
  issues.

See [Activate Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html).

### Strata Cloud Manager Pro

Learn about Strata Cloud Manager Pro.

Strata Cloud Manager Pro provides advanced features on top of the Essentials
license. Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview), unlike the
Essentials version, and one year of log retention. You can purchase Strata Cloud Manager
Pro for the following products:

- [Next-Generation Firewalls (NGFW)](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments)
- [VM Series funded by Software NGFW
  Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license)
- Cloud NGFW for [Azure](https://docs.paloaltonetworks.com/cloud-ngfw-azure/getting-started/introducing-cloud-ngfw-for-azure) and [AWS](https://docs.paloaltonetworks.com/cloud-ngfw-aws/release-notes/whats-new-cloud-ngfw-for-aws)

Here are the features Strata Cloud Manager Pro gives you:

- All the features available in Strata Cloud Manager Essentials.
- [**Strata Logging Service**](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)
  with one year of log retention and unlimited storage, enabling centralized
  logging and seamless data retrieval across your deployment.
- [**AI-Powered Observability with
  ADEM**](https://docs.paloaltonetworks.com/autonomous-dem): Strata Cloud Manager Pro integrates Autonomous
  Digital Experience Management (ADEM) for holistic observability across your
  network. ADEM helps to automate complex IT operations, reduce ticket volume, and
  shorten the mean time to resolution (MTTR).
- [**Real-time inline best
  practices**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices) provide proactive, context-aware recommendations
  directly within the web interface as you configure and manage security policies.
  This feature ensures that your configurations align with industry standards and
  Palo Alto Networks' security best practices, reducing misconfigurations and
  enhancing your overall security posture.
- [**AI-Powered Policy
  Analysis**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-analyzer) leverages advanced artificial intelligence and
  machine learning to analyze your security policies in real time, providing
  actionable insights to optimize, streamline, and strengthen your security
  posture. This feature automates the evaluation of complex policy sets, helping
  administrators make informed decisions to improve network security and
  performance.
- [**AI-Powered Operational
  Health**](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about) includes enhanced operational health capabilities
  designed to anticipate and prevent issues before they impact your network. For
  example, forecasting and anomaly detection in alerts, Root Cause Analysis in
  alerts, and Capacity Analyzer.
- [**Software Upgrade Planner**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/software-upgrades#software-upgrades-ngfw)
  analyzes the features enabled on firewalls and provides a customized
  recommendation. You can create upgrade recommendations to identify the best
  software version for upgrading your devices.

See [Activate Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html).

---

<a id="scm-activate-your-strata-cloud-manager-licenses"></a>

### Activate Your Strata Cloud Manager Licenses

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager>*

Learn how to activate Strata Cloud Manager to manage your security infrastructure
from a unified platform.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | One of these:  - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before these licensing tiers were introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

To begin using Strata Cloud Manager, you need to activate the appropriate licensing
tier—Essentials or Pro.

- [Activate Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html): The free tier that offers configuration
  management, network security lifecycle management, and can also provide
  visibility if you have a paid license of [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/license-overview).
- [Activate Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html): This tier provides advanced features plus all the Strata Cloud
  Manager Essentials features. When you activate Strata Cloud Manager Pro, it also
  includes access to the Strata Logging Service, which comes with one year of log
  retention and unlimited storage.

If you were using Strata Cloud Manager before the introduction of these new
licensing tiers, your existing licenses for Prisma Access and AIOps for NGFW Premium
remain supported. You can continue to amend, extend, or renew these licenses.
Additionally, if you're using AIOps for NGFW Free, you have the option to upgrade to
AIOps for NGFW Premium.

- [Activating AIOps for NGFW Premium](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-for-ngfw/activate-aiops-for-ngfw)
- [Activate ELA for AIOps for NGFW
  Premium](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/enterprise-license-agreement/activate-an-enterprise-license-agreement.html#idb22044ba-c033-439c-9a80-e58818b072d9)
- [Activate a Software NGFW Credits License
  Agreement](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/vm-flex-license-activation/activate-vm-flex-license#task-vm-flex-aiops.html)
- [Activate Your Prisma Access
  License](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license)
- [ADEM Licensing](https://docs.paloaltonetworks.com/autonomous-dem/administration/autonomous-dem/adem-licensing)

---

<a id="scm-activate-strata-cloud-manager-essentials"></a>

#### Activate Strata Cloud Manager Essentials

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials>*

Learn about how to activate Strata Cloud Manager Essentials that offers configuration
and network security lifecycle management features.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before these licensing tiers were introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

Strata Cloud Manager Essentials is the free tier that offers configuration
and network security lifecycle management features to streamline operations and
provide essential security. For details about device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

You can [activate VM-Series funded by software NGFW
credits](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-vm-flex-aiops) using the Strata Cloud Manager Essentials license tier. If you
don’t select a [cloud subscription in the deployment
profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series), Strata Cloud Manager Essentials activates automatically.

1. Log in to
   [Activation Console](https://apps.paloaltonetworks.com/hub).
2. Go to the Strata Cloud Manager Essentials activation URL: [scm-essentials.](https://apps.paloaltonetworks.com/activation/scm-essentials)
3. Create New
   [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where you will activate Strata
   Cloud Manager.
4. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   Region support varies based on whether you want to manage NGFWs, Prisma
   Access, or both simultaneously. To manage both, you must select a region
   that supports both NGFWs and Prisma Access.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure. You
   can also skip it by selecting None.
6. Agree to the Terms and Conditions, and
   Activate.
7. Wait for Strata Cloud Manager to initialize and for Status to show Complete.

   If you have created a new Cloud Identity Engine instance, wait for it's
   Status to show Complete.

   ![]()
8. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.

      ![]()
   3. Select one or more firewalls or Panorama appliances and
      Save.
9. If you have [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview), you can [associate it with devices](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices). Otherwise,
   you can skip it.

   After activating Strata Cloud Manager Essentials, you can specify the
   firewalls or Panorama appliances that you want to use with Strata Logging
   Service.

   1. Select Common Services > Device
      Associations.
   2. **Associate Products**.

      ![]()
   3. In the Products selection column, select Strata
      Logging Service.

      ![]()
   4. Select devices and **Save**.
10. [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
    Cloud Manager assesses the health of the devices in your deployment by analyzing
    telemetry data that your PAN-OS devices send to Strata Logging Service. To send
    this data, you must have enabled device telemetry on your devices.

    Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
    10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
    configures telemetry to be enabled by default on your devices. Upon
    onboarding a new device (Panorama or firewall), telemetry is automatically
    enabled with settings centrally controlled through Strata Cloud Manager or
    Activation Console.
11. Log in to Strata Cloud Manager by clicking on its icon in the
    Activation Console.

---

<a id="scm-activate-strata-cloud-manager-pro"></a>

#### Activate Strata Cloud Manager Pro

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro>*

Learn about how to activate Strata Cloud Manager Pro which provides advanced features
beyond the Essentials license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before this licensing tiers was introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

Strata Cloud Manager Pro provides advanced features beyond the Essentials
license. Unlike the Essentials version, it includes the Strata Logging Service and
provides one year of log retention. For details about device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

When your Strata Cloud Manager Pro license expires, the Strata Cloud Manager instance
will revert to Strata Cloud Manager Essentials licensing tier. Upon license expiration
for other subscriptions, some continue to function in a limited capacity, and others
stop operating completely. See [what happens when each subscription
expires](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/subscriptions/what-happens-when-licenses-expire).

- [NGFW](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ngfw.html#activate-strata-cloud-manager-pro-for-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-prisma-access.html#activate-strata-cloud-manager-pro-prisma-access)
- [VM-Series with Software NGFW
  Credits](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-vm-series-with-software-ngfw-credits.html#activate-vm-series-with-software-ngfw-credits)
- [ELA](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ela.html#ela)
- [ESA Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-esa.html#esa)

#### Activate Strata Cloud Manager Pro for NGFW

Learn about how to activate Strata Cloud Manager Pro for NGFW.

This task shows how to activate Strata Cloud Manager Pro for NGFW. For details about
device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

Here are the prerequisites for NGFW:

- **[Cloud Management Onboarding
  Prerequisites](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/prerequisites-for-cloud-management-onboarding)** - Before onboarding your NGFW to Strata Cloud
  Manager, verify that all conditions for device readiness are fulfilled. This
  includes network configuration, software compatibility, and licensing
  requirements. Completing these steps ensures that your firewall can be
  successfully managed using Strata Cloud Manager.
- **[TCP Ports and FQDNs for Cloud
  Management](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/tcp-ports-and-fqdns-required-for-cloud-management)** - To enable seamless communication between the
  NGFW and Strata Cloud Manager, configure specific TCP ports and Fully Qualified
  Domain Names (FQDNs).

1. After you receive an email from Palo Alto Networks identifying the Strata Cloud
   Manager Pro license you're activating, click the email link to begin the
   activation process.
2. Select Tenant where you will activate Strata Cloud
   Manager Pro. If you don't have an existing [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), **Create New**.
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with
   one year of log retention.
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager, Cloud Identity Engine, and Strata Logging
   Service to initialize, and for Status to show Complete.

   ![]()
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Navigate to Common Services > Device
      Associations.
   2. **Associate Products**.

      ![]()
   3. In the Products selection column, select Strata
      Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
   Cloud Manager assesses the health of the devices in your deployment by analyzing
   telemetry data that your PAN-OS devices send to Strata Logging Service. To send
   this data, you must have enabled device telemetry on your devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    Activation Console.

#### Activate Strata Cloud Manager Pro for Prisma Access

Learn about how to activate Strata Cloud Manager Pro for Prisma Access.

All [Prisma Access license types](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license) include access
to Strata Cloud Manager, and all Prisma Access deployments can leverage Strata Cloud
Manager for visibility features – like Command Center and Activity Insights – and
 [Autonomous DEM](https://docs.paloaltonetworks.com/autonomous-dem) monitoring.

Additionally, can optionally choose to use Strata Cloud Manager for your [Prisma Access configuration management](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/how-to-manage-prisma-access);
your other option is to use Panorama for configuration management. In both cases,
you'll be guided to activate Strata Cloud Manager Pro during your Prisma Access
license activation:

- [Activate Prisma Access, with Strata Cloud
  Manager configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation)
- [Activate Prisma Access, with Panorama
  configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation)

#### Activate Strata Cloud Manager Pro for VM-Series with Software NGFW Credits

Learn about how to activate Strata Cloud Manager Pro for VM-Series with Software NGFW
Credits.

You can manage VM-Series firewalls funded by Software NGFW Credits using Strata Cloud
Manager, enabling seamless access to advanced management and monitoring features
through Strata Cloud Manager Pro activation.

Strata Cloud Manager supports management of both standalone VM-Series firewalls and
Panorama-managed VM-Series deployments, offering a comprehensive solution for
overseeing multiple environments:

- [Activate Strata Cloud Manager Pro for
  VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-vm-flex-aiops)
- [Activate Strata Cloud Manager Pro for
  Panorama Managed VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-aiops-panorama-credits)

#### Activate Strata Cloud Manager Pro with the Enterprise License Agreement

Learn about how to activate Strata Cloud Manager Pro for Enterprise License Agreement
users.

This task shows how to activate Enterprise License Agreement (ELA) for Strata Cloud
Manager. The add-on for ELA is a consumption model for large enterprises to assign
subscriptions in bulk to assets purchased from Palo Alto Networks.

Here are the prerequisites for NGFW:

- **[Cloud Management Onboarding
  Prerequisites](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/prerequisites-for-cloud-management-onboarding)** - Before onboarding your NGFW to Strata Cloud
  Manager, verify that all conditions for device readiness are fulfilled. This
  includes network configuration, software compatibility, and licensing
  requirements. Completing these steps ensures that your firewall can be
  successfully managed using Strata Cloud Manager.
- **[TCP Ports and FQDNs for Cloud
  Management](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/tcp-ports-and-fqdns-required-for-cloud-management)** - To enable seamless communication between the
  NGFW and Strata Cloud Manager, configure specific TCP ports and Fully Qualified
  Domain Names (FQDNs).

You can activate multiple Strata Cloud Manager Pro tenants using the same license
for devices belonging to the same support accounts. To do this, navigate to the
Tenant Management to [create new tenants](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants). Then, go to the
Subscriptions & Add-ons, search for your
subscription, click Activate Cloud Tenant that will
redirect you to the activation page. Choose the same TSG on the activation page
that you used initially.

1. Use one of the following activation methods.

   - Log in to
     [Activation Console](https://apps.paloaltonetworks.com/hub) and select ELA Activation Strata Cloud Manager.

     ![]()
   - Log into the Customer Support Portal and activate from License ManagementLicenses, and then click ELA-Ngfw
     Activation.
2. Select Tenant where you will activate Strata Cloud
   Manager Pro. If you don't have an existing [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), **Create New**.
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with
   one year of log retention.

   ![]()
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
   Activation Status for both to show Complete.
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) and select Common Services > Device
      Associations.
   2. **Associate Products**.
   3. In the Licensed Products selection column, select
      Strata Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
   Cloud Manager assesses the health of the devices in your deployment by analyzing
   telemetry data that your PAN-OS devices send to Strata Logging Service. To send
   this data, you must have enabled device telemetry on your devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    Activation Console.

#### Activate Strata Cloud Manager Pro with the Enterprise Support Agreement

Learn about how to activate Strata Cloud Manager Pro for NGFW with the Enterprise
Support Agreement.

The Palo Alto Networks Enterprise Support Agreement (ESA) Pro includes
Strata Cloud Manager Pro for NGFW. ESA Pro provides a streamlined solution for a
consistent support experience across your existing assets and anticipated purchases.
This enterprise program enables organizations to maximize savings and benefits as
they scale up, making it an ideal choice for customers with large, expanding
firewall deployments.

This task shows how to activate ESA Pro for Strata Cloud Manager. You can
start the ESA Pro activation process from the
Activation Console or Customer Support Portal as
described below.

1. Use one of the following activation methods:

   - Log in to
     [Activation Console](https://apps.paloaltonetworks.com/hub) and select ESA Activation Strata Cloud Manager.

     ![]()
   - Log in to the Customer Support Portal. In the left side-panel, go to
     License Management, and then, under
     Licenses, select Activate
     Enterprise Agreement.

     ![]()
2. Create a New tenant where you will activate the Strata
   Cloud Manager instance.

   ![]()
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   A Strata Cloud Manager Pro license includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with one
   year of log retention.

   ![]()
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
   Activation Status for both to show Complete.
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Log in to the
      Activation Console and select
      Common Services > Device
      Associations.
   2. **Associate Products**.
   3. In the Licensed Products selection column, select
      Strata Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on the devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics).
   Strata Cloud Manager assesses the health of the devices in your deployment by
   analyzing telemetry data that your PAN-OS devices send to Strata Logging
   Service. To send this data, you must have enabled device telemetry on your
   devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    [Activation Console](https://apps.paloaltonetworks.com/hub).

---

<a id="scm-upgrade-to-strata-cloud-manager-pro-from-strata-cloud-manager-essentials"></a>

### Upgrade to Strata Cloud Manager Pro, from Strata Cloud Manager Essentials

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/upgrade-to-strata-cloud-manager-pro>*

Learn how to upgrade to Strata Cloud Manager Pro from Strata Cloud Manager
Essentials.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before this licensing tiers was introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

You can upgrade to Strata Cloud Manager Pro only from Strata Cloud Manager
Essentials. You can activate Strata Cloud Manager Pro only in a Customer Support
Portal (CSP) account that does not have the following product licenses:

- [Strata Logging Service with sized
  storage](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)
- [AIOps for NGFW (Free or Premium)](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about)
- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access)

1. After you receive an email from Palo Alto Networks identifying the Strata Cloud
   Manager Pro license you're activating, click the email link to begin the
   activation process.
2. To upgrade from Strata Cloud Manager Essentials to Strata Cloud Manager Pro,
   select the tenant where Strata Cloud Manager Essentials is currently
   active.
3. Strata Cloud Manager Pro will use the same region selected for Strata Cloud
   Manager Essentials.

   Continue with the remaining steps for [Strata Cloud Manager Pro activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html).

---

<a id="scm-strata-cloud-manager-prerequisites"></a>

### Strata Cloud Manager Prerequisites

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites>*

Learn about the prerequisites for Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | One of these:  - [AIOps for NGFW Free](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

Strata Cloud Manager offers detailed visibility and insights into your
Next-Generation Firewalls (NGFW) and Prisma Access deployments, regardless of whether
they are managed through Strata Cloud Manager or Panorama. To fully leverage Strata
Cloud Manager, it's essential to meet the necessary prerequisites before you [onboard](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html) your NGFW devices or Prisma Access for configuration
management or connect your Panorama instance to Strata Cloud Manager for visibility
features.

The prerequisites include ensuring connectivity between your devices and Strata
Cloud Manager, verifying software compatibility to enable full feature access,
validating licenses to activate critical functionalities, and selecting the appropriate
region to optimize performance and compliance. These requirements are essential for
successfully integrating your security devices into the platform.

- [NGFW](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-ngfw.html#strata-cloud-manager-prerequisites-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-prisma-access.html#strata-cloud-manager-prerequisites-prisma-access)

### Strata Cloud Manager Prerequisites for NGFW and VM-Series Funded by Software NGFW Credits

Learn about Strata Cloud Manager prerequisites for NGFWs.

Strata Cloud Manager provides comprehensive visibility and insights for your Palo Alto
Networks Next-Generation Firewalls (NGFW) deployments, whether managed by Strata Cloud
Manager or Panorama. You can onboard your NGFW to Strata Cloud Manager to manage and
gain insights. If you already have NGFWs managed by Panorama, you can connect Strata
Cloud Manager to your Panorama using the [Panorama CloudConnector Plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama).

When preparing to onboard and manage your NGFW and VM-Series funded by software
NGFW credits through Strata Cloud Manager, ensure that the necessary prerequisites are
met. This section covers the essential areas for successful onboarding, including
connectivity requirements and supported regions.

- **[Cloud Management for NGFWs Onboarding Prerequisites](#scm-strata-cloud-manager-prerequisites-ngfw_concept-crd_mf1_ggc)** - Before onboarding your NGFW to Strata Cloud Manager, verify that all
  conditions for device readiness are fulfilled. This includes network configuration,
  software compatibility, and licensing requirements. Completing these steps ensures
  that your firewall can be successfully managed using Strata Cloud Manager.

  To onboard VM-series funded by software NGFW credits, see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).
- **[Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility)** -
  Device models that you can associate with Strata Cloud Manager.
- **[TCP Ports and FQDNs Required for Cloud Management of NGFWs](#scm-strata-cloud-manager-prerequisites-ngfw_concept-i2t_1lr_lgc)** - To enable seamless communication between the NGFW and Strata Cloud
  Manager, configure specific TCP ports and Fully Qualified Domain Names (FQDNs).
- **[Enable Telemetry on Devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics)** -
  Enable telemetry on your NGFW to allow Strata Cloud Manager to collect necessary
  data for insights and recommendations. Strata Cloud Manager assesses the health of
  the devices in your deployment by analyzing telemetry data that your PAN-OS devices
  send to Strata Logging Service.
- **[Create Device Labels](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use Device Labels in Strata
  Cloud Manager to automate and streamline NGFW onboarding and management
  processes.
- **[Create a Device Onboarding Rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use device
  onboarding rules to automate parts of the NGFW onboarding process for Strata Cloud
  Manager.

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept-crd_mf1_ggc"></a>

#### Cloud Management for NGFWs Onboarding Prerequisites

Review the requirements to onboard a Strata Cloud Manager tenant and
firewalls to Strata Cloud Manager.

Note that some requirements, such as PAN-OS Version, Firewall Model,
Ports, and Services, apply to the firewall. While others, such as the Logging and
Authentication service requirements, apply to your Customer Support Portal (CSP)
account.

|

Prerequisite | Supported | Required? |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

PAN-OS Version | (minimum)PAN-OS 10.2.3 | Yes |

|

Firewall Model  Single vsys firewalls only  Multi-vsys firewalls are not supported  PA-410 not supported if Enterprise DLP license is active | PA-220 and PA-220R  PA-400 Series  PA-450R, PA-455R, and PA-455R-5G  PA-500 Series  PA-800 Series  PA-1400 Series  PA-3200 Series  PA-3400 Series  PA-5200 Series  PA-5400 Series  PA-5500 Series  PA-7000 Series  PA-7500  VM-Series | N/A |

|

Device Certificates | The device certificate must be installed on NGFWs before onboarding to Strata Cloud Manager.  Some NGFW models automatically install the device certificate when you first register the device on the support portal. For others, you need to [manually install device certificates](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate) before onboarding.  For any NGFW models with expired certificates, you must manually renew the certificates before onboarding. | Yes  Whether you need to manually install the device certificate before onboarding depends on your [NGFW model](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate), or the status of your device certificates. |

|

Ports  Ports are used for outbound communication from the firewall to Strata Cloud Manager and SLS | 443  444  3978 | Yes |

|

Services  Services are used for resolution of the Strata Cloud Manager tenant, as well as software and content updates | DNS  NTP | Yes |

|

Firewall Onboarding | AIOps for NGFW (Premium)  (Optional) Zero Touch Provisioning (ZTP) | Yes  ZTP onboarding is optional |

|

Firewall Management | Strata Cloud Manager | Yes Account Administrator or App Administrator [hub roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles) |

|

Logging | Strata Logging Service | Yes |

|

Data Filtering | Enterprise data loss prevention (DLP) | No |

|

Routing | Advanced Routing Engine  Enabled by default during onboarding | Yes |

|

SaaS Application Management | Next-Generation CASB | No |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept-i2t_1lr_lgc"></a>

#### TCP Ports and FQDNs Required for Cloud Management of NGFWs

Review the TCP ports and Fully Qualified Domain Names (FQDN) that you must enable on
your network communication and between the Palo Alto Networks Next-Gen Firewall
(NGFW) and Strata Cloud Manager. Communication on these TCP ports and FQDNs must
allowed on your network to successfully manage your firewalls from Strata Cloud Manager.

- [Connections to Strata Cloud Manager](#scm-strata-cloud-manager-prerequisites-ngfw_concept_hzr_py2_lvb)
- [Connections to Strata Logging Service](#scm-strata-cloud-manager-prerequisites-ngfw_concept_y5r_h2f_lvb)
- [Connections for Firewall Certificates](#scm-strata-cloud-manager-prerequisites-ngfw_concept_ocq_pkf_lvb)

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_hzr_py2_lvb"></a>

##### Connections to Strata Cloud Manager

You must allow the following app, FQDNs, and TCP ports on your network to enable
connectivity between the firewall and Strata Cloud Manager.

The Virtus service is a device connectivity service that facilitates the
connection between the firewall and Strata Cloud Manager. The FQDN and/or IP
address for the region where your Strata Cloud Manager tenant is deployed must
be allowed on your network for the firewall to successfully connect to Strata Cloud Manager. The firewall cannot connect to Strata Cloud Manager if
the FQDN or IP address is blocked.

Required App-ID and Port for Strata Cloud Manager

|

App-ID | TCP Port |

| --- | --- |

|  |  |
| --- | --- |
|

panorama | 3978 |

Required FQDNs, IP Addresses, and Ports for Strata Cloud Manager

|

Service | FQDN | IP Address | TCP Ports |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

OCSP | - [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/) - [ocsp.godaddy.com](http://ocsp.godaddy.com) | N/A | 80 |

|

Virtus | **Australia**—\*.aus.ngfw.cloudmgmt.paloaltonetworks.com | 34.151.118.202 | 3978  443 |

|

**Canada**—\*.ca.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.139.11 |

|

**E.U**—\*.eu.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.199.57 |

|

**France**—\*.fr.ngfw.cloudmgmt.paloaltonetworks.com | 34.155.195.45 |

|

**India**—\*.in.ngfw.cloudmgmt.paloaltonetworks.com | 35.200.223.12 |

|

**Israel** —\*.il.ngfw.cloudmgmt.paloaltonetworks.com | 34.165.153.154 |

|

**Italy**—\*.it.ngfw.cloudmgmt.paloaltonetworks.com | 34.154.245.218 |

|

**Indonesia**—\*.id.ngfw.cloudmgmt.paloaltonetworks.com | 34.101.126.22 |

|

**Japan**—\*.jp.ngfw.cloudmgmt.paloaltonetworks.com | 34.146.27.93 |

|

**Poland**—\*.pl.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.28.91 |

|

**Qatar**—\*.qa.ngfw.cloudmgmt.paloaltonetworks.com | 34.18.53.154 |

|

**Saudi Arabia**— \*.sa.ngfw.cloudmgmt.paloaltonetworks.com | 34.166.126.37 |

|

**Singapore**—\*.sg.ngfw.cloudmgmt.paloaltonetworks.com | 35.198.210.240 |

|

**South Africa**—\*.za.ngfw.cloudmgmt.paloaltonetworks.com | 34.35.27.12 |

|

**Spain**—\*.es.ngfw.cloudmgmt.paloaltonetworks.com | 34.175.25.27 |

|

**Switzerland**—\*.ch.ngfw.cloudmgmt.paloaltonetworks.com | 34.65.231.25 |

|

**U.K**—\*.uk.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.86.14 |

|

**U.S.A**—\*.us.ngfw.cloudmgmt.paloaltonetworks.com | 34.31.195.141 |

|

Discovery Service | ds-cloudmgmt.paloaltonetworks.com | N/A | 443 |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_y5r_h2f_lvb"></a>

##### Connections to Strata Logging Service

You must allow the following apps, FQDNs, and TCP ports on your network to
forward logs from the managed firewall to Strata Logging Service (SLS). For more
details, see the [TCP Ports and FQDNs Required for](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns)  (SLS).

Required App-ID and Ports for SLS

|

App-ID | TCP Port |

| --- | --- |

|  |  |
| --- | --- |
|

- paloalto-shared-services - panorama | 444  3978 |

|

Required if you’re sending [device telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry/device-telemetry-overview) data to SLS.   - paloalto-device-telemetry - google-base | 443  5222-5224  5228  5229 |

Required FQDNs and Ports for SLS

|

Service | FQDN | TCP Ports |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

OCSP | - [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/) - [crl.paloaltonetworks.com/](http://crl.paloaltonetworks.com/) - [ocsp.godaddy.com](http://ocsp.godaddy.com) | 80 |

|

SLS Certificates | - [api.paloaltonetworks.com](https://api.paloaltonetworks.com) - [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com) - [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) - [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) | 3978 |

|

Prisma Access | \*.gpcloudservice.com | 443 |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_ocq_pkf_lvb"></a>

##### Connections for Firewall Certificates

You must allow the following FQDNs, and TCP ports on your network to enable your
managed firewalls to install the device certificates for Strata Cloud Manager.

|

Service | FQDN | TCP Ports |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

API | - [api.paloaltonetworks.com](https://api.paloaltonetworks.com) - [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com) | 443 |

|

Device Certificates | - [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) - [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) | 443 |

### Strata Cloud Manager Prerequisites for Prisma Access

Here's what you need to know to plan your Prisma Access deployment

Strata Cloud Manager provides comprehensive visibility and insights into all Prisma
Access deployments, whether managed by Strata Cloud Manager or Panorama. Additionally,
you have the option to use Strata Cloud Manager as the management interface for Prisma
Access if needed.

During Prisma Access activation, you can choose either Strata Cloud Manager or Panorama
as the management interface. If Panorama currently manages your Prisma Access
deployment, you can migrate the configuration to Strata Cloud Manager for management.
However, after migrating, you cannot switch back to Panorama.

Before onboarding Prisma Access to Strata Cloud Manager, carefully review the following
prerequisites to ensure your existing Prisma Access deployment satisfies all necessary
conditions for a smooth and seamless onboarding.

- **Panorama Version** - Ensure you are using Panorama version 10.0 or higher.
- **Administrative Privileges** - You need an account with superuser privileges to
  log into Strata Cloud Manager.
- **License Requirements** - Ensure you have a valid [Prisma Access license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license).
- **Cloud Identity Engine** - Ensure that you have [integrated the Directory Sync component](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access/integrate-cloud-identity-engine-with-prisma-access-panorama#integrate-cloud-identity-engine-with-prisma-access-panorama) of
  the Cloud Identity Engine with the current Prisma Access (Managed by Panorama)
  tenant

Additionally, if you are migrating from Panorama to Strata Cloud Manager, review the
[migration prerequisites](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-bcj_p2w_zbc#task-bcj_p2w_zbc) to confirm whether
your deployment is eligible for configuration migration.

---

<a id="scm-migrate-from-panorama-to-strata-cloud-manager"></a>

### Migrate from Panorama to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager>*

Learn about migrating your Prisma Access or NGFW deployments from Panorama to Strata
Cloud Manager using the automated migration workflow.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW (Managed by Panorama) - Prisma Access (Managed by Panorama) | Migrating NGFWs:  - [Strata   Cloud Manager Essentials or Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) license - [Ensure   that your NGFWs meet the prerequisites for cloud   management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)  Migrating Prisma Access:  - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license - To begin the migration from Prisma Access (Managed by   Panorama) to Prisma Access (Managed by Strata Cloud   Manager), reach out to your Palo Alto Networks account   team |

Migration from Panorama to Strata Cloud Manager is now available for both Prisma
Access and NGFW Panorama configurations, allowing you the benefits of cloud
management and shared configuration management in the cloud environment. The
migration process addresses considerations such as configuration preservation and
policy continuity.

For NGFW deployments, you can follow this workflow to review configuration
compatibility, even if you're not yet ready to migrate. You can decide to trim or
accept any features that aren't supported or are partially supported for Strata
Cloud Manager configuration management. During migration, Strata Cloud Manger
converts Panorama device group hierarchies into corresponding Strata Cloud Manager
folder structures, and converts Panorama templates and template stacks into reusable
snippets.

For Prisma Access deployments, migrations focus on preserving your remote access
infrastructure, mobile user configurations, and site-to-site connectivity while
transitioning management oversight to Strata Cloud Manager.

- [Panorama Configuration
  Migration](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-ngfw.html#migrate-from-panorama-to-strata-cloud-manager-ngfw)
- [Prisma Access Migration](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-prisma-access.html#migrate-from-panorama-to-strata-cloud-manager-prisma-access)

### Migrate Configurations From Panorama to Strata Cloud Manager (NGFW)

Learn about the migration process for migrating your NGFW deployments from Panorama to
Strata Cloud Manager.

This feature is available on request. Contact your account team to enable the
feature.

You can migrate your existing NGFW configurations from Panorama to Strata Cloud
Manager for cloud-based configuration management.

During the migration, Strata Cloud Manager:

- Copies and translates supported security policies, network configurations, and
  objects.
- Maintains existing network topology and NGFW deployments.
- Highlights areas that are partially supported or unsupported.

Managing your NGFWs using [Strata Cloud Manager instead of Panorama can offer you benefits such
as](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview) unified management for Prisma Access and NGFWs, cloud-native scalability of your
network, and enhanced visibility.

Strata Cloud Manager guides you through migrating your configurations with these
key steps:

- Upload existing configurations — Import your current Panorama
  configurations.
- Run compatibility assessment — Identify unsupported features or
  configurations that need attention.
- Perform validation and prepare for deployment — Complete final checks before
  migration.
- Migration control — Devices and device groups can be migrated in phases,
  allowing you to migrate non-critical devices or go site-by-site.

Review results at each step, make necessary adjustments, and verify that your
configurations are fully compatible with Strata Cloud Manager before completing the
migration.

#### How Configuration Management Changes When You Move from Panorama to Strata Cloud Manager

Panorama configuration management is based on:

- Device Groups — Organize firewalls into hierarchical groups for security policy
  management (security rules, NAT policies, application filters).
- Templates and Template Stacks — Define network and device settings (interfaces,
  zones, routing, system settings).
- Inheritance — Device Groups inherit policies from parent groups; Template Stacks
  layer multiple templates with override capabilities.

Strata Cloud Manager configuration management is based on:

- Folders — Hierarchical containers that hold both security policies AND network
  configurations.
- Snippets — Reusable configuration blocks that can be attached to folders at any
  level.
- Containers — Device-specific configuration holders for unique firewall requirements
  .

During migration, Strata Cloud Manager converts your Panorama-based
configuration and builds it into folders and snippets:

|

**Panorama** | **Strata Cloud Manager** |

| --- | --- |

|  |  |
| --- | --- |
|

Device Groups | Folders |

|

Templates & Template Stacks | Snippets |

|

Policies and Profiles | Snippets |

|

Shared Objects | Global folder as an attached Snippet |

|

Policies in Device Groups | Policies under mapped Folder(s) |

|

Objects (addresses, EDLs, etc.) | Objects under mapped Folder(s) |

Key difference between Panorama and Strata Cloud Manager to keep in mind:

- Strata Cloud Manager Folders contain both network and security
  configurations, while Panorama separates these between Templates and Device Groups
- Strata Cloud Manager Folders provide more flexible inheritance with
  Snippet-based overrides versus the lower-level group overrides seen in Panorama
- Strata Cloud Manager Snippets provide a more plug-and-play approach to configurations
  compared to Panorama's Templates and Template stacks that are inherited down the
  stack.

After migration, you manage configurations through the folder and snippet
model. Snippet attachment order determines configuration precedence, providing granular
control over how multiple configuration sources combine. You can also create
device-specific containers for NGFWs requiring unique configurations outside the folder
inheritance model.

**Additional Resources**

Learn more about [Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups) and [Templates](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks).

Learn more about [Snippets](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets) and [Folders](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management)

#### Prepare to Migrate Your Panorama NGFW Configurations to Strata Cloud Manager

Before beginning the migration, ensure you have the following items ready:

- Minimum Software Requirements: PAN-OS 10.2.3 or later
- [Export Panorama Configuration File](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations): Export the
  complete running configuration from your source Panorama instance in XML format
- [Panorama Master Key](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-the-master-key-from-panorama): Obtain the master key used for
  encryption in your Panorama configuration (if not using the default key)
- [Strata Cloud Manager Tenant](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager): Verify that your Strata
  Cloud Manager tenant is deployed, properly licensed, and operational
- [NGFW Configuration](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/troubleshooting/troubleshoot-panorama-system-issues/generate-diagnostic-files-for-panorama): Collect the last-pushed
  configuration files (Technical Support Files) from NGFWs you plan to validate
  post-migration
- [Network Topology](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management): Review your current device group
  hierarchies, template relationships, and NGFW assignments
- [Configuration Backup](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups): Create complete backups of your
  current Panorama and NGFW configurations as a safety measure
- [Administrative Access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Ensure you have access to the
  Superuser role in both Panorama and Strata Cloud Manager.
- Migration Planning: Identify which device groups, templates, and NGFWs you
  want to migrate in your initial phase
- [Compatibility Matrix](https://docs.paloaltonetworks.com/compatibility-matrix): Understand which features may not be
  supported in Strata Cloud Manager and plan for any necessary configuration
  adjustments
- Unsupported Functionalities: Migration of configurations to Strata Cloud Manager is
  not supported if the **intrazone-default** and **interzone-default** policies
  have been overwritten at the Device Group level. If these default security rules are
  overwritten, the migration tool cannot process the Panorama configuration. You must
  remove these overwritten policies from Panorama, commit your changes, and re-export
  the running-config.xml before attempting the migration.

#### Migrate Your Panorama NGFW Configurations to Strata Cloud Manager

Migrate your NGFW configurations from Panorama to Strata Cloud Manager:

1. Prepare your Panorama for the migration.
   1. Log in to the Panorama that manages your NGFWs with an administrative account
      that is assigned the [Superuser](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-cli-quick-start/get-started-with-the-cli/give-administrators-access-to-the-cli/administrative-privileges) role.
   2. **(Optional)** If you have configured a custom Master Key for
      Panorama, make a note of it.

      If your deployment uses the default Master Key, this step isn't
      required.
   3. Ensure that your current Panorama configuration is up to date and that you have
      committed and pushed all your current changes to Panorama by going to CommitCommit & Push and Preview Changes.
   4. **(Optional)** Check the diffs between the running configuration and
      the candidate configuration and determine whether you want to push those changes. To
      commit and push the changes, Edit Selections and select the
      NGFWs you want to push in the Push Scope.
   5. **(Optional)**
      Commit and Push your changes.
   6. Go to PanoramaSetupOperations and Export the named Panorama configuration
      snapshot.

      The .xml file is required to upload to Strata Cloud Manager during the migration
      process. Don't upload a techsupport file or any other file except an .xml
      configuration file.
   7. Select the running-config.xml configuration file and click
      OK.
2. Log in to Strata Cloud Manager as an administrator with a Superuser role and go to ConfigurationOnboarding.

   ![]()

   The migration program detects that you have a Panorama managed
   deployment.

   1. Confirm the tenant is correct.
   2. (Optional) [Create a Named Snapshot](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot?otp=task-uzv_3lr_vcc#task-uzv_3lr_vcc) of your running
      configuration in the event that a rollback is necessary.

   Migration should not be attempted during an Strata Cloud Manager upgrade
   window. Check your upgrade schedule to see if you have an upcoming upgrade.
3. Read the migration Overview.

   ![]()

   1. Review the management building blocks of Strata Cloud Manager:
      Folders and Snippets.
   2. Click Next: Upload Panorama Configuration.
4. Upload the Panorama configuration.

   ![]()

   ![]()

   1. Select the Panorama configuration *.xml* file you downloaded in an earlier
      step by dragging and dropping it from your file explorer or selecting
      Choose File.
   2. **(Optional)** Input your Master Key or, if
      you did not create a custom master key, use the Default
      one.

      ![]()
   3. Click Next: Review Migration Compatibility.

   If the migration tool produces any errors that cannot
   resolve automatically, you may have a configuration that is unsupported. Click
   Cancel Migration, remove these overwritten policies from your
   Panorama configuration, re-export the configuration file, and restart the migration
   process.
5. Review the configuration compatibility.

   ![]()

   1. **(Optional)**
      Export Compatibility Summary and review your organization’s
      configuration compatibility before continuing and allowing Strata Cloud Manager to
      trim any unsupported or partially supported configurations.

      The trimming of unsupported and partially supported features avoids migrating
      features that cannot be deployed safely or securely in Strata Cloud Manager.

      This process will only impact the staged configuration for Strata Cloud Manager.
      The configurations in Panorama will remain unaffected.

      For each flagged area, you should plan to rebuild, replace, or defer those
      configurations.

      ![]()
   2. Review the Unsupported Features that will be trimmed from
      your configuration during the migration.

      These features will be trimmed from your configurations and will not be staged in
      Strata Cloud Manager during the configuration migration process.
   3. Review the Partially Supported Features and determine a
      resolution path.

      Identify what exactly is going to be missing from the configuration.

      You can accept the partially supported features and build a remediation plan
      post-migration or return to your Panorama configuration and clean these areas up
      before starting the migration process again.
   4. Acknowledge the unsupported and partially supported
      features.
   5. Click Next: Select Device Groups to Migrate.

   For those just looking to compare supported
   configurations, or if it is decided than more planning is needed, you can end the
   migration process here.
6. Select the Devices or Device Groups you
   would like to migrate.

   If you are migrating NGFWs from Panorama for the first
   time, it is recommended to only migrate non-critical devices or device groups first to
   test how your configurations will be migrated to Strata Cloud Manager.

   ![]()

   During the migration:

   - Objects are imported to a Snippet and attached to the Global
     folder.
   - Policies are imported under the Folder(s) migrated by the workflow.
   - Shared Device Groups are automatically mapped to the All Firewalls
     Folder.

   After selecting the devices, click Next: Map Templates to
   Folders.
7. Map Templates to your newly configured
   Folders.

   ![]()

   You can choose between two template mapping
   options:

   - Auto Template Mapping: Automatically associate template
     and template stack configurations with folders after migration to snippets. This
     feature eliminates the need for manual configuration mapping and reduces the
     iterative process that you typically face during the migration workflow.

     Strata Cloud Manager processes the entire Panorama configuration, even
     when you only select a subset of device groups for migration. This comprehensive
     analysis prevents issues in subsequent device group migrations; however, it may
     extend the processing time for the initial migration.
   - Manual Template Mapping: Manually associate template and
     template stack configurations with folders after migration to snippets.

   - During migration, Device Groups are transformed into folders, while templates
     and template stacks are converted into configuration snippets.
   - If two or more Device Groups reuse the same template, elevate it to a higher
     folder. If only one site requires it, keep it at the site level.

   Here is the procedure to manually associate templates:

   1. Select a Device Group to reveal the
      Templates/Template Stacks used by that device group.

      ![]()
   2. Edit the mapping to assign each
      Template/Template Stack to a
      Folder.
   3. Elevate templates referenced in multiple places to higher folders.

      For example, if you have global template settings, mapping them to the All
      Firewalls folder establishes those settings as the source of truth for all NGFWs.
   4. After assigning more than one Snippet to a Folder, adjust the order.
   5. Move Up or Move Down to finalize
      the order.
   6. Update the order.
   7. Save the new order.

      Before moving on to the next step, ensure the following:
      - No unassigned templates or template stacks remain.
      - Any templates referenced by multiple device groups have been elevated to the
        proper folders.
8. Click Next: Prepare Migration.

   The migration process begins.

   Wait for all steps to be completed.

   If there are any issues with the migration, return to the previous steps to
   evaluate and make changes. If issues continue to persist, please contact Palo Alto
   Networks Support.
9. Prepare to migrate.
   1. Load Configuration to Strata Cloud Manager to prepare to
      migrate.

      1. The migration worfklow:
         - Translates Devices and Device Groups and Templates and Template Stacks to
           Folders and Snippets using the mappings and snippets order defined by
           you.
         - Creates a Strata Cloud Manager snapshot to enable rollback of staged
           changes.
         - Checks for conflicts in existing Strata Cloud Manager configurations (name
           collisions, missing references, 31-character limits, RBAC scope).
         - Builds the staged configuration that will be in Strata Cloud Manager
           post-load.
   2. Load Results and review what objects, policies, or
      snippets were created, updated, or skipped.
   3. Review the Validation Results for any errors, warning, and
      informational messages post migration.
   4. Click Next: Review Config Diffs.

      This commits the newly generated configuration to Strata Cloud Manager.
10. Review the configuration diffs.

    When reviewing your configuration diffs, you may notice
    that secret keys or passwords appear as **Modified**. This is expected behavior.
    Because Strata Cloud Manager uses a different Master Key than your Panorama instance,
    the encrypted string representing the key changes during the translation process. The
    underlying plaintext key remains exactly the same, and no action is required.

    1. In the left folder tree, expand to the Folder and select an NGFW serial number to
       be validated
    2. Browse File and choose the TSF for the selected serial
       number.

       Uploading the TSF for the chosen NGFW will allow you to properly validating all
       the supported, partially supported, and unsupported configurations.

       The configuration diff viewer provides a structured interface to
       inspect complex configuration changes by organizing modifications, additions, and
       deletions into categorized views. The diff viewer helps you identify created,
       modified, or deleted configuration elements. Because the migration process might
       trim certain configurations, you can use the search functionality to locate
       specific configuration elements by name, object type, or difference category. This
       streamlines the review process for migrations with extensive configuration
       differences.

       Strata Cloud Manager
       categorizes configuration diffs into three groups:

       - Modified/Missing—Represents changes to
         existing objects during the migration process. This includes items with
         changed values or missing object references.
       - Unsupported—Represents items that cannot be
         migrated due to feature parity gaps between Panorama® and Strata Cloud
         Manager, detected using predefined parity checks. This category also includes
         features that have alternate implementation in Strata Cloud Manager.
       - Informational—Represents changes where object
         functionality remains the same but names or references have been automatically
         updated to comply with Strata Cloud Manager naming conventions (for example,
         profile names).

       The diff viewer includes the following components and capabilities to
       help you analyze these configuration changes:

       - **Grid grouping and full-screen mode**—Diff entries are grouped
         by object type in the grid, allowing you to expand and collapse sections for
         an organized review. To facilitate the inspection of complex changes, you can
         activate a full-screen mode using the maximize button.
       - **Informational category tags**—When you select the
         Informational category, descriptive tags display
         counts for each subcategory: Default Additions, Reference Updated, Removed
         Unused, and Renamed. You can hover over each tag for a tooltip description and
         use the grid filter to narrow results to a specific subcategory.
       - **Tabbed views**—A tabbed interface allows you to switch between
         a **Diff** view, which shows the before-and-after configuration state, and
         an **Object Names** view, which lists every individual object affected by
         that change pattern.
       - **Detailed columns**—Each diff entry displays an **Action**
         column indicating whether the change is an addition, deletion, or
         modification. A **Sub-Category** column appears for Informational diffs and
         is hidden by default for other categories. Additionally, a **Description**
         column is available for the Unsupported category to explain why a
         configuration element cannot be migrated.

       Because of naming conventions in Strata Cloud Manager, some long names will be
       compressed when needed.

       ![]()
    3. Review the configuration diff panes.

       1. Green Panes: Created or added. They are present in Strata Cloud
          Manager, but not on the original device.
       2. Red Panes: Deleted or trimmed. May not be supported in Strata Cloud
          Manager, but are on the device.

       The diff view may be extensive, limited to one NGFW at a time, and
       calculated from the last pushed XML from the TSF.
    4. Verify the diffs for representative devices from each pattern or site type.
    5. (Optional)
       Export the diff results.
    6. (Optional)Regenerate Diffs if any corrections
       have been made.
    7. Click Next: Confirm and Finish.
11. Confirm and finish your migration of configurations to Strata
    Cloud Manager.

    The migration tool does not onboard your NGFWs! You must still onboard your NGFWs
    to Strata Cloud Manager.

    Now that your Panorama configurations are Strata Cloud Manager, ready for device
    onboarding and pushes performed from SCM.

    With the configuration migration complete, review the available [documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) for onboarding and managing NGFWs in Strata Cloud Manager.

    1. Ensure the results from Steps 8 and 9 are accepted.
    2. Confirm the migration.

       This officially marks the migration as complete.
    3. (Optional) To revert the configuration to its pre-migration state at any
       point, select Revert. This initiates a rollback workflow,
       restoring Strata Cloud Manager to a Snapshot taken before the migration was
       loaded.
    4. (Optional) To cancel the migration at any point, select
       Cancel Migration. This aborts the migration process and
       cleans up any temporary changes.

#### Post-Migration

After confirming the configuration migration in the tool, the configuration is staged in
Strata Cloud Manager but has not yet been pushed to your NGFWs. The NGFWs are still
managed by Panorama, now you must onboard them to Strata Cloud Manager to proceed with
cloud management.

To complete the transition to Strata Cloud Manager, you must perform pre-onboarding
checks, [onboard your NGFWs to Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html), and execute a [configuration push](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config).

##### Onboard NGFWs to Strata Cloud Manager

You must onboard your NGFWS to Strata Cloud Manager to transfer management authority
from Panorama to the cloud. You can migrate devices in phases (for example, by device
group or site). For detailed steps on associating devices and configuring connectivity,
see [Onboard to Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html).

**General Onboarding Guidelines**

- **Associate Devices:** Ensure all firewalls are associated with your Strata Cloud
  Manager tenant.
- **Move to Cloud Management:** Use the Strata Cloud Manager onboarding workflow to
  move the device to **Cloud Management**.
- **Verify Placement:** Confirm that the device shows a **Connected** status in
  Strata Cloud Manager and appears under the correct intended Folder.

##### First Push and Validation

Once devices are onboarded and connected, you must [push the staged configuration](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config) from Strata Cloud
Manager to enforce policies.

Once you have pushed the staged configuration, validate:

- Commit success.
- Session health and traffic flow.
- Interface, virtual router, and HA status.
- Log forwarding to Strata Logging Service.

Once you have validated your push, take screenshots of the connected state and
successful push for your validation report.

##### Rollback Readiness

If critical issues arise during the pre-onboarding or onboarding phases, you can revert
Strata Cloud Manager to its state prior to the migration.

Use [Configuration: Config Version Snapshots](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot) to load
the **pre-migration-snapshot** created by the tool. This reverts the staged Strata
Cloud Manager configuration but does not push changes to devices.

### Migrate from Panorama to Strata Cloud Manager (Prisma Access)

Learn about the migration process for migrating your Prisma Access deployments from
Panorama to Strata Cloud Manager.

If you have an existing Prisma Access Deployment for which the configuration is
managed by Panorama and want to migrate to Strata Cloud Manager for configuration
management, Palo Alto Networks offers an in-product workflow that lets you migrate
your existing Prisma Access configuration to Strata Cloud Manager.

To enable migration workflow, you must contact your Palo
Alto Networks account team.

Managing your Prisma Access configuration using Strata Cloud Manager instead of
Panorama can offer you benefits such as:

- Continuous [best practice assessments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
- Secure default configurations
- Machine Learning (ML)-based configuration optimization
- Streamlined web security workflows
- An interactive visual summary ([Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center)) that helps you to
  assess the health, security, and efficiency of the network
- Intuitive [workflows](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows) for complex tasks
- Simple and secure [management APIs](https://pan.dev/access/api/prisma-access-config/)
- Cloud-native architecture provides scalability, resilience, and global
  reach
- No hardware to manage or software to maintain

#### Migrate to Prisma Access (Managed by Strata Cloud Manager)

To migrate Prisma Access (Managed by Panorama) to Strata Cloud Manager, see [**Migrate Prisma Access from Panorama to
Strata Cloud Manager**](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager)

---

<a id="scm-migrate-from-zscaler-to-strata-cloud-manager"></a>

### Migrate from Zscaler to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager>*

Accelerate Zscaler to Prisma SASE migration with Strata Cloud Manager, automating
ZIA and ZPA configuration transition with actionable insights.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) | Permissions and Credentials:   - Superuser or Network Administrator role - Zscaler API Credentials (Cloud URL, Username, Password, API   Key for ZIA; Cloud URL, Client ID, Client Secret, Customer   ID for ZPA) or Zscaler JSON configuration files bundled in   .zip format   Licenses:   - Prisma Access license - Enterprise Data Loss Prevention license - ZTNA Connector license - Privileged Remote Access (PRA) license - Remote Browser Isolation (RBI) license   Additional Requirements:   - Strata Cloud Manager 2026.R2 release or later - Application IP Blocks configured in Prisma Access   Infrastructure Settings - Network connectivity to Zscaler Cloud API on port 443 - Zscaler SCIM or SCIM groups configured for Cloud Identity   Engine |

The Zscaler to Prisma® SASE migration engine automates the transition of Zscaler
Internet Access (ZIA) and Zscaler Private Access (ZPA) configurations to Prisma
Access security policies. This tool reduces manual effort and potential errors by
automating the assessment, translation, and optimization of Zscaler configurations
into Prisma Access-compatible formats.

To begin the migration process, you upload your Zscaler configuration either
programmatically via Zscaler Cloud APIs or through a JSON file. The migration engine
parses, analyzes, and converts the configuration into a Prisma Access-compatible
format. The engine applies optimization logic to clean up duplicate and redundant
data, thereby reducing the total policy footprint. You can review and refine the
translated configuration before importing it into Prisma Access.

For general security policies and objects, the tool generates a Strata Cloud Manager
snippet — a reusable set of configuration that can be applied to a Strata Cloud
Manager folder. Snippets make it easy to deploy standard settings consistently
across your network. ZTNA, Privileged Remote Access (PRA), and Remote Browser
Isolation (RBI) configurations are applied immediately after the migration is
completed without an explicit commit. It is strongly recommended that you test the
migration on a pre-production tenant before migrating production workflows.

Migration is only supported for commercial tenants.

The following Zscaler Private Access (ZPA) policies and objects are not currently
supported for migration. These unsupported elements are excluded from the
translation process and added to your migration report:

- CLIENTLESS\_SESSION\_PROTECTION\_POLICY (Browser Protection Policy)
- CLIENT\_FORWARDING\_POLICY (BYPASS\_POLICY)
- Servers
- Server Groups
- Service Edge Connections
- Service Edge Connection Groups
- Isolation Profiles

Note the following caveats:

- ZTNA objects can have a maximum of 4 connector groups per FQDN or wildcard
  targets.
- Only one Connector Group per Compute Region is supported.

The migration is a 2-step process and the steps must be completed in order.

1. [Prepare Your Zscaler Data for Migration](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/prepare-your-zscaler-data-for-migration.html)
2. [Migrate Zscaler Configurations to Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/migrate-zscaler-configurations-to-strata-cloud-manager.html)

---

<a id="scm-prepare-your-zscaler-data-for-migration"></a>

#### Prepare Your Zscaler Data for Migration

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/prepare-your-zscaler-data-for-migration>*

You can upload Zscaler data to the migration engine either via API calls or by uploading
a configuration file.

##### Retrieve API Parameters for a Zscaler Internet Access Account or Private Access Account

To import your data via API, you need to retrieve a set of parameters. The
credentials are deleted from the system immediately after the data is imported. For
information on how to retrieve these parameters, see [How to Generate and Setup the API
Parameters](https://github.com/PaloAltoNetworks/zscaler-api-connector/blob/main/Generate-And-Setup-API-Parameter-Instructions.md).

##### Prepare Configuration Data Using a Script

You can run the fetch\_zscaler\_zia\_zpa\_config.py Python script to
export configuration data such as firewall rules, network objects, URL categories,
and policies from Zscaler ZIA and ZPA. The data is stored locally in the same
directory as the script. You can then upload this data to the migration engine.

You can access the fetch\_zscaler\_zia\_zpa\_config.py script at
[Palo Alto Networks GitHub](https://github.com/PaloAltoNetworks/zscaler-api-connector/blob/main/fetch_zscaler_zia_zpa_config.py). For
instructions on running the script, see the [Fetch Zscaler Config Guide](https://github.com/PaloAltoNetworks/zscaler-api-connector/blob/main/Fetch-Zscaler-Config-Guide.md).

---

<a id="scm-migrate-zscaler-configurations-to-strata-cloud-manager"></a>

#### Migrate Zscaler Configurations to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/migrate-zscaler-configurations-to-strata-cloud-manager>*

Migrate your ZIA and ZPA configurations to Prisma Access using the Strata Cloud
Manager migration wizard.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) | Permissions and Credentials:   - Superuser or Network Administrator role - Zscaler API Credentials (Cloud URL, Username, Password, API   Key for ZIA; Cloud URL, Client ID, Client Secret, Customer   ID for ZPA) or Zscaler JSON configuration files bundled in   .zip format   Licenses:   - Prisma Access license - Enterprise Data Loss Prevention license - ZTNA Connector license - Privileged Remote Access (PRA) license - Remote Browser Isolation (RBI) license   Additional Requirements:   - Strata Cloud Manager 2026.R2 release or later - Application IP Blocks configured in Prisma Access   Infrastructure Settings - Network connectivity to Zscaler Cloud API on port 443 - Zscaler SCIM or SCIM groups configured for Cloud Identity   Engine |

1. Log in to Strata Cloud Manager.
2. Select ConfigurationOnboarding.
3. In the Migration Catalog, locate
   Zscaler and then Start
   Migration.
4. On the Import Configuration screen, select how to import
   your Zscaler data to the migration engine.

   ![]()

   **API Method**

   Select Use API to import your configuration
   programmatically by connecting to the Zscaler API. For information on how to
   retrieve the required parameters, see [Prepare Your Zscaler Data for Migration](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/prepare-your-zscaler-data-for-migration.html).

   1. Both ZIA and ZPA are selected by default. To import only one of the
      configurations, clear the appropriate option.
   2. For ZIA, enter your Cloud URL,
      Username, Password,
      and API Key.
   3. For ZPA, enter your Cloud URL, Client
      ID, Client Secret, and
      Customer ID.
   4. Authorize Palo Alto Networks to use the Zscaler API credentials and then
      Fetch Configuration.

   **Configuration File Method**

   Select Upload configuration from files to manually
   upload your Zscaler configuration. For information on creating the ZIP file,
   see [Prepare Your Zscaler Data for Migration](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-zscaler-to-strata-cloud-manager/prepare-your-zscaler-data-for-migration.html).

   1. Browse or drag and drop the prepared ZIP file containing your Zscaler
      configuration. The ZIP file must contain separate directories for
      zia and/or zpa with JSON
      files.

   The system validates your inputs and begins the upload process, generating a
   unique migration\_id for your task.

   You can click the Hide Steps (

   ![]()

   ) icon in the left navigation bar to expand the main
   configuration area.
5. Click Next: Analyze and Convert.

   During the analyze step, the tool parses, analyzes, and converts your Zscaler
   configuration to a Prisma Access-compatible format.

   ![]()

   - Section 1 identifies the policy types (for example, Firewall, URL
     Filtering, CASB, ZPA policies) and configuration objects. Click
     Proceed after you review this section.
   - Section 2 verifies the licenses available and displays configurations
     corresponding to these licenses. By default, all policies and
     configurations for the detected licenses are selected for migration. You
     can skip a policy migration by clearing the relevant checkbox.

     If any
     licenses are missing, you have two options:

     - **Re-run Job**: Enable the required licenses (ZTNA Connector,
       PRA, RBI) and re-initiate the analysis.
     - **Proceed without Missing/Deselected Licenses**: Proceed with
       the migration, but the configurations dependent on missing
       licenses will be skipped.

     Click Proceed after you review this
     section.
   - Section 3 is the Translation and Optimize section, which displays a
     summary of the conversion. Zscaler configurations do not contain
     profiles, so the migration engine maps policy types to rule sections
     and objects to Strata Cloud Manager profiles. The numbers in
     parentheses show the total number of rules or objects being
     migrated.

     This section also provides statistics on how many original Zscaler
     rules and objects were optimized (for example, merged or
     deduplicated) to a more concise set of Strata Cloud Manager policy
     rules and objects by applying Palo Alto Networks best practices in
     your environment.

     The following Zscaler rules are split into two rules:

     - Rules that include address groups with combinations of full
       FQDNs and wildcard FQDNs.
     - Rules where protocols are mapped to AppIDs and URL
       categories.

     The first rule uses the address group or AppIDs to define trusted or
     restricted destinations at the network level and the second rule
     maps specific protocols to AppIDs for application-level visibility
     and URL categories for content-based filtering. After the split, the
     primary rule handles identity and destination, while the secondary
     rule provides granular content control via URL categorization.

     ![]()
6. Click Next: Review Converted Migration.

   The Review Converted Configuration screen displays the
   translated policies and objects. Each tab displays the number of objects
   that were translated. The tabs are determined by the licenses and features
   selected for migration. Example tabs include:

   - Security Policy: Displays Zscaler rules
     translated into Strata Cloud Manager security policies.
   - Authentication Policy: Shows migrated
     authentication rules.
   - Decryption Policy: Displays translated decryption
     policies and profiles.
   - Configuration Objects: Lists all migrated
     configuration objects and applications.
   - Profile: Shows migrated Profile Groups, Security
     Profiles, and Decryption Profiles.

   Within each tab, the migration status for each rule is displayed:

   - Full Migration indicates that the rule is ready
     for import.
   - Partial Migration indicates that the rule
     requires manual review due to missing information.
   - Skip Migration refers to invalid, duplicate, or
     conflicting rules that will not be migrated.

   You can perform the following actions to review the data:

   - To filter a column, click the icon next to the column name and select
     the criteria.
   - To view the details for a row, click the icon in the
     Actions column.
   - To view the mapping tab for the selected objects in the rule, click the
     icon in the Actions column.

   ![]()

   Zscaler items not converted to an SCM configuration are displayed in the
   Missed Mapping Objects tab. To manually map these objects, click
   Map Manually to SCM in the Action column. Select
   the SCM object this should be converted to and click Apply to
   all.
7. Click Next: Generate Strata Cloud Manager Config.
8. Review the reports.

   This report provides detailed statistics on rule and object optimization,
   including original counts, merged counts, conflict counts, and optimization
   percentages. Click View Details to view policy
   details.

   ![]()
9. Enter a descriptive Snippet Name (for example,
   zscaler-migration-prod).

   This name identifies the configuration snippet in Strata Cloud Manager. If
   you do not specify a name, the system creates a local snippet in the format
   zscaler-{migration\_id}.
10. Select Import to SCM.

    The system validates the imported configuration and saves it as a snippet.
    These snippets can be applied directly to your Prisma Access policy in
    Strata Cloud Manager at any point in your deployment process — whether
    before or after you complete infrastructure setup such as onboarding users
    and private apps. This flexibility ensures you have full control to deploy
    your optimized security whenever it best fits your migration plan.

    ![]()
11. On the Generate Strata Cloud Manager Config screen,
    monitor the progress and review any errors displayed under Show the
    detail.

    This provides logs of any issues during object or policy creation, including
    API error codes, allowing you to identify and address unmigrated elements in
    your environment. The import status is displayed after the processing is
    completed.
12. Click Next: Finish and Infrastructure Setup.

    This page displays the import status for the snippet and potential next
    steps:

    - Edit the migration snippet.
    - Assign the generated snippet to an NGFW or Prisma Access folder.
    - Push the config.
13. (Optional) Click Download Report to save a
    comprehensive Migration Report (PDF summary) or a Detailed Report (JSON format)
    for audit, compliance, and future reference.

    These reports detail what was migrated, optimized, or skipped.
14. Do one of the following.
    - Click Rollback Migration to revert the changes
      made during the migration. Click Confirm Rollback to
      complete the process.
    - Click Close to exit the migration
      wizard.

---

<a id="scm-onboard-to-strata-cloud-manager"></a>

### Onboard to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager>*

Learn about onboarding Prisma Access and Palo Alto Networks NGFWs to Strata Cloud
Manager.

Onboarding is the process of integrating your existing NGFWs and Prisma Access into
Strata Cloud Manager for management, visibility, or both. You can manage NGFWs directly
through Strata Cloud Manager along with Prisma Access deployments, or connect your
Panorama instance to Strata Cloud Manager to gain visibility.

After you've activated [Strata Cloud Manager Essentials or
Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) and met the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html), here's how to start
onboarding your NGFWs and Prisma Access to Strata Cloud Manager.

- [NGFWs, ZTP NGFWs, & VM-Series
  NGFWs](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager.html#tabs-onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager)
- [Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-prisma-access-to-strata-cloud-manager.html#tabs-onboard-prisma-access-to-strata-cloud-manager)

### Onboard NGFWs, ZTP NGFWs, and VM-Series to Strata Cloud Manager

Procedures for onboarding NGFWs to Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) | One of these:  - [AIOps for NGFW Free](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

You can onboard your NGFW to Strata Cloud Manager to manage and gain
insights. If you already have NGFWs managed by Panorama, you can connect Strata
Cloud Manager to your Panorama using the [Panorama CloudConnector Plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) for
visibility and monitoring.

To get started managing your NGFWs with Strata Cloud Manager, follow the initial
onboarding steps below:

1. [Deploy your NGFWs and complete the
   initial setup.](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/getting-started)

   Start by integrating the firewall into your network, segmenting your
   network into zones, setting up a basic security policy, assessing
   network traffic, and reviewing the best practices.
2. [Review the prerequisites for onboarding
   your NGFWs to Strata Cloud Manager.](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)

   The prerequisites include minimum PAN-OS versions supported, supported
   NGFW models, ports, licenses, and other hard-stop requirements for using
   your NGFWs with Strata Cloud Manager.
3. [Activate your Strata Cloud Manager
   license and start associating devices to your tenant.](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager)

   If you are simply utilizing Strata Cloud Manager for the advanced
   monitoring and visibility features that will benefit your PAN-OS or
   Panorama managed firewalls, you can stop here.
4. Onboard your NGFWs to Strata Cloud Manager.
5. [Configure general settings to get
   your NGFWs up and running.](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/configure-the-firewall-general-settings.html)

   After you successfully onboard your NGFWs to Strata Cloud Manager, you have the option to configure and specify the
   general firewall management settings. The general settings include the
   following: domain name, login banner, certificates, time zones, locales,
   coordinates, and tunnel acceleration.
6. [Configure the NGFW session
   settings.](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/configure-the-firewall-session-settings.html)

   Define the general and VPN session settings, and as well the session
   timeout settings, for your firewall.
7. [Learn about how local NGFW
   configuration management works in](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/local-configuration-management.html)

   The local configuration management feature eliminates the need for
   context switching from central management to individual firewalls for
   managing local configurations.

   After you complete these steps, you can start  [managing your NGFWs with Strata
   Cloud Manager.](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access)

To onboard NGFWs using Zero Touch Provisioning (ZTP), click
[here](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws.html).

- [Onboard NGFWs](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-ngfws.html#onboard-ngfws)
- [Onboard VM-Series NGFWs](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-vm-series.html#onboard-vm-series)

### Onboard NGFWs

Workflow for onboarding NGFWs to Strata Cloud Manager.

Learn about device labels, onboarding rules, and onboarding NGFWs to Strata Cloud
Manager.

#### Create a Device Label or Device Label Group

Device labels in Strata Cloud Manager provide a powerful and flexible
way to automate and streamline NGFW onboarding and management processes. You can
use labels to group devices based on common characteristics, enabling more
efficient configuration and software update management. This feature
enhances:

- **Zero Touch Provisioning**
  **(ZTP)** - by allowing you to assign labels during bootstrap,
  facilitating automated provisioning and near-zero touch onboarding of
  devices.
- **Standard Device Onboarding** - by enabling you to create
  label-based onboarding rules, ensuring the correct configuration is
  applied to the right NGFWs.
- **Software Updates** - by simplifying the process of
  managing multiple devices across distributed environments and being able
  to group NGFWs by software version.

By implementing device labels, you can reduce manual coordination,
minimize human errors, and accelerate remote site onboarding. To start managing
your devices using Device Labels, go to ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
Firewall or Firewall Folder, Device OnboardingDevice Labels.

##### Create a Device Label

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice Labels.
3. Add Label.
   1. Enter a descriptive Name.
   2. Select a Label Group.
   3. Save the Label.

##### Create a Device Label Group

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice LabelsManage Label Group.
3. Add Label Group.
   1. Enter a descriptive Name.
   2. Enable exposure to any combination of
      the following: ZTP, Device
      Onboarding, NGFW Software
      updates.
   3. Save the Label Group.

#### Create a Device Onboarding Rule

Use a device onboarding rule to automate parts of the Palo Alto Networks Next
Generation Firewall (NGFW) onboarding to Strata Cloud Manager whether you're
manually onboarding Palo Alto Networks NGFW or onboarding using Zero Touch
Provisioning (ZTP). This allows you to associate the firewall with a folder and
push a configuration when the firewall first connects to Strata Cloud Manager.
Device onboarding rules are designed to simplify and greatly reduce the time
spent onboarding new Palo Alto Networks NGFW at scale and ensure the correct
configuration is applied to newly onboarded Palo Alto Networks NGFW. You can
create multiple device onboarding rules to define different match criteria that
apply to different Palo Alto Networks NGFW.

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

The Match Criteria, Action,
VPN Onboarding, and User Context
Onboarding configurations are optional and can be configured as
needed. If no Match Criteria is specified then the device
onboarding rule applies to Any Palo Alto Networks NGFW
model and serial number. The Palo Alto Networks NGFW must match all
Match Criteria defined in the rule for Strata Cloud Manager to take the configured Action or
push the VPN Onboarding and User Context
Onboarding configurations.

For example, you don't configure the Match Criteria and
configure only the Target Folder in the rule
Action. Additionally, you don't configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager applies the
rule to all Palo Alto Networks NGFW onboarded to Strata Cloud Manager and only
adds them to the Target Folder. Another example is that
you specify Palo Alto Networks NGFW models and serial numbers in the
Match Criteria but you don't configure the rule
Action at all. Additionally, you configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager pushes the
VPN Onboarding and User Context
Onboarding configurations to only the Palo Alto Networks NGFW
models and serial numbers that match the Match
Criteria.

1. [Log in to](https://stratacloudmanager.paloaltonetworks.com/)
   Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
   Firewall or Firewall Folder, Device Onboarding.
3. Add Rule.
4. Configure the General device onboarding rule
   settings.
   1. The device onboarding rule is Enabled by
      default. Toggle the Enable setting to disable
      the onboarding rule after you Save.
   2. Enter a descriptive Name for the onboarding
      rule.
   3. (Optional) Enter a Description for
      the onboarding rule.
5. Define the onboarding rule Match Criteria.

   The match criteria define to which Palo Alto Networks NGFW the device
   onboarding rule applies.

   1. Specify which Palo Alto Networks NGFW
      Models.

      - Any—Applies to all Palo Alto
        Networks NGFW onboarded to Strata Cloud Manager.
      - Match—Inclusive condition that
        applies to the Palo Alto Networks NGFW models added to
        the match list. You can select one or multiple different
        Palo Alto Networks NGFW models.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies only to those
        Palo Alto Networks NGFW.
      - Exclude (Negate)—Exclusive
        condition that applies to all Palo Alto Networks NGFW
        models not added to the exclude match list.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies to all Palo
        Alto Networks NGFW models except for those added to the
        exclude list.
   2. Specify the Device S/N.

      This compliments the Models match criteria
      by allowing you to identify specific serial numbers of Palo Alto
      Networks NGFW Models that the onboarding
      rule applies to.

      - Any—Applies to all Palo Alto
        Networks NGFW serial numbers.
      - Match—Enter a regular expression
        (regex) to identify Palo Alto Networks NGFW serial
        numbers.
   3. Specify Labels applied to Palo Alto Networks
      NGFW during onboarding that the onboarding rule applies to.

      You can use And,
      Or, and Not
      operators to write a logical expression of labels to match. You
      can use parentheses (()) to group sets of
      labels and logical operators when writing your regular
      expression.

   ![]()
6. Define the onboarding rule Action.
   1. Select the Target Folder the firewall is
      added to if it matches the device onboarding rule.

      If no Target Folder is specified, then the
      firewall is added to the default All
      Firewalls folder.

      (VM-Series, funded with Software NGFW Credits) You can configure
      the dgname field in the
      init.cfg.txt bootstrap
      parameters to add the VM-Series firewall to a
      target folder. In this case, Strata Cloud Manager
      prioritizes adding the VM-Series firewall to
      the target folder configured in the
      init.cfg.txt file over the
      one configured in the device onboarding rule.
   2. For Snippet Association, apply [snippet](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/configuration-scope/snippets) configuration to
      the onboarded firewall after it successfully connects to Strata Cloud Manager.

      Snippets are a tool used to standardize a common base
      configuration for a set of firewalls or deployments. This allows
      you to quickly onboard a new firewall with a known good
      configuration and reduces the time required to onboard a new
      firewall.

      ![]()
   3. Enable VPN Onboarding if you have configured
      [Auto VPN](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html) for secure
      hub-and-spoke connectivity between Strata Cloud Manager and your
      managed firewalls.

      If enabled, select the VPN Cluster to add
      the firewall to. This determines the gateway devices and
      automatically creates secure connections between the configured
      gateway and the newly onboarded firewall.

      Click Configure to [configure the Palo Alto
      Networks NGFW as a hub or branch firewall.](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html)

      ![]()
   4. Enable User Context Onboarding to configure
      the user and tag mappings required for [User Context for Cloud Identity
      Engine (CIE)](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context).

      User Context provides simplified granular control over the data
      that is shared across your security devices. It provides your
      administrators the flexibility to specify the data types each
      device sends and receives.

      If enabled, you must configure the Segments to
      Contribute Data To to customize the segment
      mappings the firewall sends to CIE and the Segments
      to Receive Data From to customize how CIE
      provides segment mappings to the firewall.

      ![]()
7. Save.
8. In Device Onboarding, review your newly configured
   onboarding rule and verify it's Enabled.

   Device onboarding rules are processed in a top-down priority. Strata Cloud Manager evaluates each onboarding rule Match
   Criteria starting with the rule highest in the rule
   hierarchy until the Palo Alto Networks NGFW meets all Match
   Criteria. Strata Cloud Manager then takes the
   Action specified in the matching rule. In the
   event two rules in the device onboarding rule hierarchy apply to the
   same firewall, Strata Cloud Manager takes the
   Action configured in the device onboarding
   rule higher up in the rule hierarchy.
9. Onboard your Palo Alto Networks NGFW manually or using ZTP.

#### Onboard a NGFW to Strata Cloud Manager

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

After you activate Strata Cloud Manager, you can begin to onboard Palo Alto
Networks firewalls to it. Onboarding to Strata Cloud Manager is supported for
firewalls running PAN-OS 10.2.3 and later releases.

Strata Cloud Manager is available, featuring [two licensing tiers: Strata Cloud Manager
Essentials and Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support). This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service.

If you were using Strata Cloud Manager before the introduction of these new
licensing tiers, your existing license for AIOps for NGFW Premium remains
supported. You can continue to amend, extend, renew, or activate without any
changes.

There are four components involved in firewall onboarding:

- The [tenant](#) — Created when you activate a product license on
  your Customer Support Portal (CSP) account. You add firewalls to your
  tenant to associate them with Strata Cloud Manager.
- The firewall — The Palo Alto Networks firewall that you intend to use
  with Strata Cloud Manager.

  You can only onboard a firewall not already associated with Strata Logging Service. If a firewall is already associated
  with Strata Logging Service, it’s ineligible for Strata Cloud Manager and isn't displayed.
- AIOps for NGFW Premium, Strata Cloud Manager Essentials, or Strata Cloud Manager Pro— One of the licenses required for cloud
  management of firewalls.
- Strata Cloud Manager — The app you will be associating with the firewall
  to manage its configuration from the cloud.

1. Review the [prerequisites to onboard your
   NGFW to](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)Strata Cloud Manager.
2. [Activate](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/activate-cortex-data-lake-toc/activate-cortex-data-lake-easy) the Strata Logging Service license.

   Skip this step if you already activated the Prisma Access (Managed by Strata Cloud Manager) license
   on the same tenant you are activating AIOps for NGFW Premium
   license.
3. Activate Strata Cloud Manager.

   - [Activate Strata Cloud Manager
     Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html): The free tier that offers configuration
     management, network security lifecycle management, and can also
     provide visibility if you have a paid license of [Strata Logging
     Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/license-overview).
   - [Activate Strata Cloud Manager
     Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html): This tier provides advanced features plus all the
     Strata Cloud Manager Essentials features. When you activate Strata
     Cloud Manager Pro, it also includes access to the Strata Logging
     Service, which comes with one year of log retention and unlimited
     storage.

   If you were using Strata Cloud Manager before the introduction of these
   new licensing tiers, your existing AIOps for NGFW Premium license
   remains supported. You need to [activate Strata Cloud Manager](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-premium-activation)
   using the AIOps for NGFW Premium license.

   Skip this step if you already activated Strata Cloud Manager.
4. (Optional) [Activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine
   license.

   Activate Cloud Identity Engine (CIE) if you plan to use user-based
   authentication policy rules. CIE activation is not required for initial
   onboarding and can be activated at a later time as needed.
5. Register the firewall with the Palo Alto Networks Customer Support Portal
   (CSP) and activate licenses.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and find the Serial
      # under the General Information widget in the
      Dashboard.
   2. [Register the firewall](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/getting-started/register-the-firewall).
   3. [Activate the Support
      license](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/subscriptions/activate-subscription-licenses) on the firewall.
6. [Install the device certificate](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/certificate-management/obtain-certificates/device-certificate) on
   the firewall.

   This is required to successfully authenticate the firewall with the Palo
   Alto Networks CSP and use Strata Cloud Manager.
7. Configure the firewall Panorama Settings required to connect to Strata Cloud Manager.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface).
   2. Configure the firewall DNS and NTP servers.

      This is required to successfully connect the firewall to Strata Cloud Manager and install software and content
      updates.

      1. Select DeviceSetupServices and edit the Services.
      2. Select Servers and configure the
         Primary DNS Server and
         Secondary DNS Server.
      3. Select NTP and configure the
         Primary and Secondary NTP Server
         Address.
      4. Click OK.
   3. Configure the Panorama Settings.

      1. Select DeviceSetupManagement and edit the Panorama Settings.
      2. Select Managed By Cloud
         Service.
      3. (NGFW (Managed by Strata Cloud Manager) Running PAN-OS 11.2
         and later) Select the
         Port used for connectivity
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **Default**—The [default TCP port
           3978](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama). This port is dedicated for
           communication between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **443**—TCP port 443 is the standard port
           used for HTTP traffic encrypted with SSL. Using
           port 443 for NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager communication greatly simplifies
           network configuration management for both
           administrators and end users.

           Additionally, using port 443 reduces your
           network attack surface by reducing the number of
           open ports on your network.
      4. (Optional for (NGFW (Managed by Strata Cloud Manager)
         Running PAN-OS 11.2 and later) Check
         Enable Compress Config to
         compress the size of the configuration file exchanged
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager, and vice versa, to increase file
         transfer times.

         Enabling this setting does not cause load or delay in
         firewall processing or increase commit operation
         times.
      5. Click OK.

      ![]()
   4. Commit.
8. (Optional) Create a Device Onboarding Rule to associate the
   firewall with a folder and push a configuration when the firewall first
   connects to Strata Cloud Manager.
9. [Associate a firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) with your
   Palo Alto Networks Customer Support Portal (CSP) account.
   1. Log in to Strata Cloud Manager.
   2. In the bottom-left corner of the window, select the icon for your
      tenant and select System SettingsDevice Associations.

      ![]()
   3. Add Devices.
   4. Select one or more firewalls you want to onboard with your CSP
      account.

      You can use the firewall serial number you gathered in the
      previous step to search for a specific firewall.
   5. Save.
10. (Optional) If you are activating AIOps for NGFW Premium license or
    Strata Cloud Manager Pro, you need to [associate the firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with Strata Cloud Manager.
    1. In Device Associations, select the firewall you added and
       Associate Products.
    2. For the Licensed Products, select Strata Cloud
       Manager or AIOps for
       NGFW.
    3. From the Select Firewall Model, License Type, and
       Term drop-down, select the firewall and support
       license to apply to the firewall.

       The model for the firewall license must match the firewall model
       you are onboarding to Strata Cloud Manager.
    4. Apply Licenses.

       ![]()
    5. In the Device Associations page, verify the Associated Products for
       the onboarded firewall display AIOps for
       NGFW and Strata Logging Service.
11. Add the available device to Strata Cloud Manager.
    1. Select System SettingsDevice ManagementAvailable Devices.
    2. In the Available Devices select the
       firewall you just added.
    3. Move to Cloud Management.

       You are prompted to confirm the number of selected firewalls.
       Click Move to Cloud Management to
       continue.

       ![]()
    4. (Optional) Apply Labels to the
       onboarded firewall.

       You can select an existing label or create a new label by typing
       the label you want to create.

       Click Move to Cloud to continue adding the
       firewall to Strata Cloud Manager.

       ![]()
    5. Confirm that the selected firewall is now listed in the list of
       Cloud Managed Devices and that the
       Onboarding Status shows
       Success.
12. Verify that the firewall successfully onboarded to Strata Cloud Manager.

    Two configuration pushes occur by default to the firewall after
    successful onboarding to Strata Cloud Manager. The first push from
    Strata Cloud Manager automatically enables the Advanced Routing
    Engine and restarts the firewall. The second pushes the
    configuration from Strata Cloud Manager to the firewall.

    If the Advanced Routing Engine is not automatically enabled as part
    of the onboarding process to Strata Cloud Manager, you need to
    manually [enable Advanced Routing](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/networking/advanced-routing/enable-advanced-routing.html) on
    the firewall.

    1. Select System SettingsDevice ManagementCloud Managed Devices.

       You should see the serial number for the firewall that you just
       added, but you won’t see any additional device information for
       it yet.
    2. [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli)
       and verify the firewall successfully connected to Strata Cloud Manager.

       After you connect the firewall to Strata Cloud Manager, it’s
       automatically converted to logical router mode, restarted, and
       Strata Cloud Manager pushes the default configuration to
       the firewall.

       For this to work, make sure:

       - You’ve installed the device certificate on the
         firewall.
       - The firewall meets the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html) for Strata Cloud Manager.
       - You’ve resolved variables. If variables aren’t
         resolved, Strata Cloud Manager will fail to push
         the default configuration to the firewall.

       ```
       admin> show cloud-management-status
       ```

       ![]()

       Verify the firewall successfully connected to a Strata Cloud Manager
       Endpoint and that the
       Connected status displays
       Yes.

       Once the firewall is Connected, the
       firewall automatically converts to logical router mode and
       restarts, and Strata Cloud Manager pushes the default
       configuration to the firewall.
    3. Return to [Strata Cloud Manager](https://sase.paloaltonetworks.com/) and
       select System SettingsDevice ManagementCloud Managed Devices and verify that the details for the firewall appear,
       such as serial number, model, type, and IP address.

       By default, newly onboarded firewalls are added to the
       All Firewalls folder.
13. Create and associate your firewall with a [folder](https://docs.paloaltonetworks.com/cloud-management/administration/workflows/workflows-ngfw-setup/folder-management).

    Folders are used to logically group your firewalls for simplified
    configuration management. Skip this step if you created a device
    onboarding rule to automatically move the firewall to a target folder.

    (HA only) Both firewalls must be in the same folder to
    configure HA. If you need to configure your firewalls in a [high availability](https://docs.paloaltonetworks.com/ngfw/administration/high-availability) (HA)
    configuration, be sure to plan your folder structure accordingly and
    move both firewalls to the same folder before you configure HA.

    Additionally, firewalls in an HA configuration can't be moved to a
    new folder. To move them, you must first break the HA configuration,
    move both firewalls to the new folder, and then reconfigure HA.

    1. Select System SettingsFolder Management and Add Folder to create a new
       folder.
    2. Locate the newly added firewall that is associated with the
       All Firewalls by default.
    3. In the Action column, Move the firewall to
       the folder you created.
14. (Optional) Modify the displayed firewall name.

    By default, firewalls onboarded to Strata Cloud Manager display the
    firewall serial number as the displayed firewall name throughout Strata Cloud Manager. Rename the displayed firewall from the serial
    number to a more user-friendly name to make it easier to identify.

    1. Select System SettingsFolder Management and locate the firewall you onboarded.
    2. In the Actions column, expand the Actions menu and
       Edit.
    3. Enter a new Display Name for the
       firewall.
    4. Save.
15. Review the predefined interface and logical router configurations.

    The predefined interfaces and logical router configuration are required
    to successfully push configuration changes to managed firewalls after
    they’re successfully added to Strata Cloud Manager.

    - **$eth-internet (eth1/3)**—Ethernet interface for outbound
      internet connections. Associated with the default logical router
      configuration.
    - **$eth-local (eth1/4)**—Ethernet interface for local network
      connections. Associated with the default router
      configuration.

    The predefined interface and logical router configuration are associated
    with the default All Firewalls folder and
    are inherited by all other folders you create. You might reassign the
    $eth-internet and
    $eth-local interfaces for a newly
    created folder or for the individual firewall as needed.

    1. Select ConfigurationDevice SettingsInterfacesEthernet and verify that
       $eth-internet and
       $eth-local are displayed.

       To reassign the interface, click the interface name to select
       a new Default Interface Assignment
       and Save.

       ![]()
    2. Select ConfigurationDevice SettingsRoutingRouters and verify the default
       logical router is displayed.

       ![]()
16. Push Config to push your configuration
    changes.
17. Select ConfigurationPush Status and to verify that your configuration push was successful.
18. Finally, check the [Strata Cloud Manager Command
    Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) and confirm that your firewall appears in the
    Summary view.

#### Offboard NGFWs or VM-Series

To remove a physical or VM-Series NGFW that is managed by Strata Cloud
Manager:

1. Log in to Strata Cloud Manager.
2. Navigate to **System Settings** > **Device Management** >
   **Available Devices**.
3. Select the option **Back to Available Devices** to move the firewall
   out of Strata Cloud Manager.

You can [remove device associations](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager#device-associations-remove-associations) if, for
example, you are retiring or returning a firewall or Panorama appliance, or if
you want to associate it with another [tenant service group (TSG)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant).

### Onboard VM-Series

Information for onboarding VM-Series NGFWs to Strata Cloud Manager.

To onboard VM-series funded by software NGFW credits, see
[Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

### Onboard Prisma Access to Strata Cloud Manager

Learn about how to onboard Prisma Access to Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access | One of these:  - [Prisma Access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

Strata Cloud Manager provides comprehensive visibility and insights into all Prisma
Access deployments, whether managed by Strata Cloud Manager or Panorama. Additionally,
you have the option to use Strata Cloud Manager as the management interface for Prisma
Access if needed.

During Prisma Access activation, you can choose either Strata Cloud Manager or Panorama
as the management interface. If Panorama currently manages your Prisma Access
deployment, you can migrate the configuration to Strata Cloud Manager for management.
However, after migrating, you cannot switch back to Panorama.

#### Onboard Prisma Access for Visibility

Before you begin, confirm that your Prisma Access deployment meets the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-prisma-access.html) for visibility and monitoring
in Strata Cloud Manager.

To use Strata Cloud Manager for visibility and monitoring, you just need to log into
Strata Cloud manager and choose the appropriate Prisma Access tenant. Once you
select the correct tenant, you can see Prisma Access data in Command Center,
Dashboards and Activity Insights.

1. **Access Strata Cloud Manager** - You can access Strata Cloud Manager from
   the
   [Activation Console](https://apps.paloaltonetworks.com/hub), or
   you can access it directly at [stratacloudmanager.paloaltonetworks.com](http://stratacloudmanager.paloaltonetworks.com).
2. **Verify or switch tenant** - Go to the bottom of the navigation menu and
   check your tenant details. If the tenant name is incorrect, use the search
   option to find and switch to the correct tenant.

#### Onboard Prisma Access for Configuration Management

- **New Prisma Access Deployment**  - If you have chosen Strata Cloud
  Manager as the management interface during Prisma Access activation, you
  need to begin by [configuring your Prisma Access
  features](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access) in Strata Cloud Manager after activation.
- **Migration from Panorama** - If your Prisma Access deployment is managed
  by Panorama, you can migrate the configuration from Panorama to Strata Clod
  Manager. Once you migrate to Strata Cloud Manager, you cannot switch back to
  Panorama.

  Before you migrate Prisma Access to Strata Cloud Manager,
  review the [prerequisites](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-bcj_p2w_zbc#task-bcj_p2w_zbc) to confirm that
  your existing deployment meets all necessary requirements.

  Palo
  Alto Networks offers an **in-product workflow** to [migrate](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-j3r_p2w_zbc#task-j3r_p2w_zbc) your existing Prisma
  Access Deployment managed by Panorama to Strata Cloud Manager.

---

<a id="scm-onboard-ngfws-with-site-management"></a>

#### Onboard NGFWs with Site Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-with-site-management>*

Automate NGFW configuration variable resolution during onboarding using Site
Management in Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW | Contact your account representative if you are interested in enabling this feature.  One of these licenses:   - Strata Cloud Manager Essentials - Strata Cloud Manager Pro   Roles needed:   - Network Administrator - Superuser - Business Admin |

Site Management in Strata Cloud Manager streamlines Next-Generation Firewall (NGFW)
deployment by automating configuration variable resolution. This feature introduces a
"Site" as a core entity for NGFW deployment, abstracting device complexity in your
environment. You define reusable properties and rules to generate specific variable
values for individual devices, eliminating manual operations and standardizing your
provisioning process.

Site Management improves NGFW deployments by ensuring consistency and reducing errors,
especially at scale. Previously, configuring settings like IP addresses or hostnames
manually for each device often caused inconsistencies and increased administrative
effort. Site Management automates these calculations and standardizes value generation
across NGFWs, reducing configuration drift and enhancing scalability for large
deployments.

Site Management operates by centralizing your configurations. You define
Properties — customer-defined metadata consisting of user-specified keys and values
that describe each site's unique characteristics (such as location, region, or site
ID) — and assign specific property values to individual Sites. These site-specific
values are then used by Onboarding Rules, which contain Variable Resolution Rules.
The Site Manager component dynamically calculates complex configuration details,
such as derived IP addresses or hostnames, by substituting variables with site
property values.

The workflow begins when you define Properties, Site Properties Groups, Sites, and
Onboarding Rules within Strata Cloud Manager. An installer then selects a target
site while installing the NGFWs. Strata Cloud Manager resolves the configuration in
accordance with the variable resolution rules defined by the admin. This process
includes Onboarding Properties as customizable metadata and Variable Resolution Rules
that support string substitution and bit operations for precise IPv4 address
generation. A Claim process then ties a physical or virtual NGFW to a
pre-configured Site, triggering automated variable resolution and provisioning
through Strata Cloud Manager.

- This feature is only available during the onboarding of NGFWs.
- This feature exclusively supports IPv4 for all IP address fields,
  variables, and resolution rules; IPv6 is not supported.
- A site is restricted to being claimed by one single device.

1. Define Site Properties.
   1. [Log in to](https://stratacloudmanager.paloaltonetworks.com/)
      Strata Cloud Manager.
   2. Navigate to ConfigurationNGFW and Prisma Access, set the Configuration Scope to
      All Firewalls, and continue to SetupDevice OnboardingSite ManagementSite Properties.
   3. Add Property.

      Properties are defined at the tenant level.
   4. Enter a unique Name for the property, for
      example, region\_id or
      location.
   5. Select the Type for the property and configure
      the type-specific constraints.

      - String—Enter a Maximum
        Length, for example,
        1024.
      - Integer—Enter a
        Minimum and
        Maximum value, for example,
        0 to 7.
   6. Save.
2. Create Site Property Groups.

   Site Groups are a collection of Sites with similar properties.

   1. Navigate to ConfigurationNGFW and Prisma Access, set the Configuration Scope to
      All Firewalls, and continue to SetupDevice OnboardingSite ManagementSite Property Groups.
   2. Add Site Properties Group.
   3. Enter a Name for the site group, for example,
      Branch Deployments.
   4. Define and associate the properties that belong to this group.
   5. Save.
3. Create Sites.
   1. Navigate to ConfigurationNGFW and Prisma Access, set the Configuration Scope to
      All Firewalls, and continue to SetupDevice OnboardingSite ManagementSites.
   2. Add Site.
   3. Select the Site Group this site belongs to, for
      example, Branch Deployments.
   4. Enter a unique Name for the site, for example,
      sc-store-1.
   5. (Optional) Enter the physical Address
      for the site.
   6. Provide Property Values for each property
      defined in the selected Site Group, for example,
      region\_id: 7.
   7. (Optional) To add multiple sites at once, select the
      Site Properties Group created in Step 2 and
      choose to either manually add sites in a grid or Import
      CSV.
   8. Save.
4. Configure Site-Based Onboarding Rules.
   1. Navigate to ConfigurationNGFW and Prisma Access, set the Configuration Scope to
      All Firewalls, and continue to SetupDevice OnboardingOnboarding Rules.
   2. Add Rule and configure the general
      settings.

      - Enter a descriptive Name for the rule
        and optionally a Description.
      - Ensure the Enabled toggle is
        active.
      - Select Site-Based as the
        Onboarding Type.
   3. Configure the Match Criteria.

      - Select the Site Properties Group from
        Step 2 that this rule will apply to, for example,
        Branch Deployments.
      - (Optional) Specify
        Models.
   4. Configure the Actions.

      - Select Target Folder.
      - Select any Snippet Association.
      - Select the Target OS Version for the
        device.
      - (Optional) Enable VPN
        Onboarding.
      - (Optional) Enable Custom
        Interface.

        Custom Interface
        is disabled by default. When enabled, it disables the
        automatic application of the ZTP Default Snippet
        post-bootstrap, allowing administrator-defined interface and
        routing configurations to take effect. Use this option only
        when the management interface or non-standard ports are
        required for post-onboarding connectivity. Ensure all
        necessary interface and routing configurations are defined
        before enabling this option to prevent connectivity
        interruptions.
      - (Optional) Enable User Context
        Onboarding.
   5. Enable Variable Resolution and configure
      variables.

      Only variables defined at the folder selected in
      Target Folder or defined in an associated
      snippet will be available for resolution.

      For each variable you want to override:

      1. Select the variable Name, for example,
         mgmt\_ip.
      2. Choose the appropriate Resolution Rule
         Type:

         - Replacement—Enter an
           Expression using site
           properties, for example,
           10.1.${region\_id}.2.
         - Bitwise Expression—Define the
           bitwise resolution to dynamically generate an IP
           address for each site. This option provides the
           flexibility to dynamically configure every bit of the
           IP address and use properties to resolve the IP
           address for every site.
   6. Save.
5. Preview Site Resolution.

   To prevent potential runtime errors from inconsistent variable resolution, you
   can preview how variables will resolve for your sites before
   deployment.

   1. Navigate to ConfigurationNGFW and Prisma Access, set the Configuration Scope to
      All Firewalls, and continue to SetupDevice OnboardingSite ManagementSites.
   2. Preview Resolution.
   3. (Optional) Select the Model
      Family.
   4. Review the Resolved Onboarding Rule and
      Resolved Variables for each site.
6. Claim a Site during device onboarding.
   1. Initiate the NGFW device onboarding process using [Zero Touch Provisioning (ZTP)](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws.html) or [manual onboarding](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-ngfws.html).
   2. On the ZTP activation page or Strata Cloud Manager onboarding page,
      enter the device's Serial Number and
      Claim Key.
   3. Select a pre-defined Onboarding (Site) from the
      available list.

      A site can only be claimed by one device
      at a time.

      If you are using the [ZTP mobile web
      app](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws/onboard-ztp-ngfw-with-web-app.html), location detection automatically populates sites
      within a 2 km radius of your current position. You can tap
      Tap to change location to update your
      location or toggle Show All Sites to browse
      the complete list of available sites.
   4. Submit.
7. Verify Onboarding Status and Resolved Variables.
   1. Navigate to SettingsDevice Management.
   2. Locate the newly onboarded device.
   3. Review the Onboarding Status.
   4. Select the device and navigate to its specific Configuration
      Scope.
   5. Manage Variables.
   6. Review the Resolved Variables.

---

<a id="scm-onboard-ngfws-using-zero-touch-provisioning-ztp"></a>

#### Onboard NGFWs using Zero Touch Provisioning (ZTP)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws>*

Use this workflow for onboarding NGFWs to Strata Cloud Manager using Zero Touch
Provisioning (ZTP).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW | One of these:  - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

Learn about onboarding NGFWs using Zero Touch Provisioning (ZTP).

##### Onboard a ZTP NGFW

ZTP is designed to simplify and automate the onboarding of new
firewalls to Strata Cloud Manager. ZTP streamlines the initial firewall
deployment process by allowing network administrators to ship managed firewalls
directly to their branches and automatically add the firewall to their tenant
after the ZTP firewall successfully connects to the Palo Alto Networks ZTP
service. This allows businesses to save on time and resources when deploying new
firewalls at branch locations by removing the need for IT administrators to
manually provision the new managed firewall. After successful onboarding, Strata Cloud Manager provides the means to configure and manage your
firewalls.

The ZTP cloud service supports a direct
internet connection via Ethernet or cellular interfaces (exclusively for 5G
hardware) to successfully onboard a firewall to Strata Cloud Manager. It
supports Generation 5 firewalls with standalone cellular connections or a
combination of Ethernet and cellular interfaces. This allows automated
provisioning for remote sites relying on mobile data.

If only cellular 1/1 is connected, it is automatically
configured as the management interface. If both cellular 1/1 or Ethernet 1/1 are
connected, Ethernet 1/1 serves as the primary management interface. If the
Ethernet link goes down, the firewall fails over to cellular 1/1 for management
access.

The ZTP cloud service does not support an explicit web proxy. It cannot onboard a
ZTP firewall to Strata Cloud Manager if an explicit web proxy is configured as
a gateway to the internet for your firewalls and Strata Cloud Manager.

Review and subscribe to [ZTP Service Status](https://status.paloaltonetworks.com/) events to be notified about
scheduled maintenance windows, outages, and workarounds.

Before you begin setting up ZTP on Strata Cloud Manager, review the
[Firewall Hardware Quick Start and Reference Guides](https://docs.paloaltonetworks.com/hardware.html)
to understand how to correctly install your firewall to successfully leverage
ZTP.

###### ZTP Configuration Elements

The following elements work together to allow you to quickly onboard newly
deployed ZTP firewalls by automatically adding them to Strata Cloud Manager
using the ZTP service.

- **Customer Support Portal (CSP) Account**—The ZTP
  service uses the Palo Alto Networks [Customer Support Portal](https://support.paloaltonetworks.com/) to register the
  firewall with your account and identify the tenants that you can
  associate with your ZTP firewall.
- **Tenant**—The Strata Cloud Manager
  [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) the ZTP
  firewall will be associated with. This is a logical container for
  your apps and devices.
- **Business Administrator or Superuser Role**—The [enterprise roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)
  that can onboard a ZTP firewall. These roles are [assigned through Common
  Services](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles#id9a032461-859e-4598-8645-3c28030bad75).
- **Claim Key**—Eight-digit numeric key physically
  attached to the ZTP firewall used to register the ZTP firewall with
  the CSP.
- **Serial Number**—A 10-32 character alphanumeric
  identifier attached to the ZTP firewall. You can find this on a
  sticker on the back of the firewall.
- **Activation URL**—URL used to onboard your ZTP firewall
  to cloud management [ZTP activation URL](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation).

  For the 5G hardware models, you can scan the unique QR code on
  the device label to instantly retrieve the activation link,
  Serial Number, and Claim Key.

1. Business Administrator or higher role activates a ZTP firewall by
   visiting the ZTP activation [URL](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation) and the firewall
   serial number and claim key. If you have more than one tenant or CSP
   account, you can select which one you want to associate with the
   firewall.
2. The ZTP firewall registers with the CSP and with the Strata Cloud Manager tenant specified during activation.
3. A ZTP firewall successfully registered with the ZTP service
   automatically appears in Strata Cloud Manager (**Settings > Firewall
   Setup > Device Management**).
4. When the firewall connects to the internet, the ZTP firewall requests
   a device certificate from the CSP in order to connect to the ZTP
   service.
5. The ZTP service pushes the Strata Cloud Manager FQDN and the ZTP
   configuration to the firewall.
6. The ZTP firewall connects to Strata Cloud Manager.

###### Onboard a ZTP NGFW to Strata Cloud Manager

With a Business Administrator or greater [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions), access [ZTP device activation](https://cloud.apps.paloaltonetworks.com/ztpdeviceactivation) to initiate
ZTP. To initiate ZTP, you must enter the firewall serial number and claim
key provided by Palo Alto Networks and then activate the ZTP process. The
[ZTP Activation Page](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation) registers your
firewall to the Customer Support Portal (CSP) and associates the firewall to
the selected tenant.

Before you initiate ZTP, you must ensure that you have deployed a
Dynamic Host Configuration Protocol (DHCP) server on the network. You must
have a DHCP server configured to successfully onboard a firewall to Strata Cloud Manager. The firewall is unable to connect to the Palo Alto
Networks ZTP service to facilitate onboarding without a DHCP server.

You can't migrate a firewall added to Strata Cloud Manager using
ZTP from one tenant to another.

While adding a firewall to Strata Cloud Manager using ZTP, don't
perform any commits on the ZTP firewall before you verify that the firewall
appears in Strata Cloud Manager according to the steps below. Performing a
local commit on the ZTP firewall disables ZTP functionality and results in
the failure to successfully add the firewall to Strata Cloud Manager.

All the PA-Series NGFW models are supported for ZTP.

- PA-400 Series
- PA-400R Series
- PA-1400 Series
- PA-3400 Series
- PA-5400 Series
- PA-5450 and PA-7500 Series
- PA-500 and PA-5500 Series

1. Activate the licenses required for Strata Cloud Manager (Strata Cloud Manager Essentials or Strata Cloud Manager Pro).
2. (Optional) Create a device onboarding rule to associate the
   firewall with a folder and push a configuration when the firewall first
   connects to Strata Cloud Manager.
3. Onboard the firewall to Strata Cloud Manager.
   1. With the [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of Business
      Administrator or higher, access [ZTP device
      activation](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation).
   2. Select the tenant (if you have more than one in your CSP
      account).
   3. Enter the Serial Number of the ZTP firewall.
   4. Enter the Claim Key for the ZTP firewall.
   5. (Optional) Select any labels if defined by the admin
      for grouping.

      For the 5G hardware
      models, you can scan the unique QR code on the device label
      to instantly retrieve the activation link, Serial Number,
      and Claim Key.
   6. ActivateZTP.
4. Connect the network interface on the ZTP firewall and power on.

   Ensure that you have correctly cabled the firewall before powering it
   on. ZTP connection is a one-time event, and if it fails, you will
   need to take corrective action.

   - **Ethernet ZTP:** Connect the Ethernet cable
     to **Ethernet1/1**.
   - (5G hardware only) **Cellular
     ZTP:** Ensure a valid **SIM card with an active
     data plan** is installed.
   - (5G hardware only) **Hybrid (Ethernet
     and Cellular):** Connect the Ethernet cable to
     **Ethernet1/1** and ensure the **SIM card** is
     installed

   SCM automatically pushes the correct ZTP snippet based on the
   available interfaces reported by the firewall.
5. Power On the firewall.

   The device will power up, initialize its interface (Ethernet or
   Cellular), and automatically connect to the Palo Alto Networks ZTP
   service.
6. Monitor the Bootstrap Status.

   1. In Strata Cloud Manager, select System SettingsDevice ManagementCloud Managed Devices.

      You can
      also monitor the activation status from the ZTP
      Activation Page.
   2. Locate your device. The Bootstrap Status displays the progress
      of the automated onboarding steps. Wait for the status to change
      to Done.
7. Verify the firewall successfully onboarded to Strata Cloud Manager.
   1. Log in to Strata Cloud Manager.
   2. Select System SettingsDevice Management and verify the ZTP firewall appears.
8. [Move the firewall to a folder](https://docs.paloaltonetworks.com/oneapp/administration/workflows/workflows-ngfw-setup/folder-management)
   of your choice.

   Folders are used to logically group your firewalls for simplified
   configuration management. Skip this step if you created a device
   onboarding rule to automatically move the firewall to a target
   folder.

   (HA only) Both firewalls must be in the same folder to
   configure HA. If you need to configure your firewalls in a [high availability](https://docs.paloaltonetworks.com/ngfw/administration/high-availability) (HA)
   configuration, be sure to plan your folder structure accordingly
   and move both firewalls to the same folder before you configure
   HA.

   Additionally, firewalls in an HA configuration cannot be moved to
   a new folder. To move them, you must first break the HA
   configuration, move both firewalls to the new folder, and then
   reconfigure HA.

   1. Select System SettingsDevice Management and expand the All
      Firewalls folder.
   2. Expand the Actions menu and Move.
   3. Select the folder Destination and
      Move.
9. Push Config to push your configuration
   changes.
10. Finally, check the [Strata Cloud Manager Command
    Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) and confirm that your firewall appears in the
    Summary view.

---

<a id="scm-onboard-a-ztp-ngfw-using-the-ztp-web-app"></a>

##### Onboard a ZTP NGFW Using the ZTP Web App

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws/onboard-ztp-ngfw-with-web-app>*

Activate NGFWs at branch locations from a mobile device using the Zero Touch
Provisioning (ZTP) NGFW Activation web app.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW | One of these:   - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   And all of these:   - Business Administrator or Superuser role in Strata Cloud Manager - iOS or Android smartphone with a camera and internet   connectivity - A Customer Support Portal (CSP) account - DHCP server deployed on the branch network |

The ZTP NGFW Activation web app extends the existing Zero Touch Provisioning (ZTP)
portal to mobile devices, enabling field installers to activate NGFWs at branch
locations without a laptop or detailed knowledge of the customer's network
configuration. The web app is browser-based and works on both iOS and Android
devices, so no separate native app installation is required.

The ZTP web app introduces two features that further simplify field deployments:
location detection automatically identifies nearby sites pending deployment so you
can select a site without manual lookup, and port detection uses your device's camera
to verify physical cable connections before activation begins, preventing
misconfiguration errors.

You can reach the ZTP Activation Page in two ways: by scanning the QR code on Gen
5 or newer NGFW hardware, or by navigating directly to the page URL. The QR code
opens the page automatically and pre-populates the Serial Number and Claim Key
fields, so no manual entry is needed. After activation, the NGFW bootstrap process
begins automatically and takes approximately 25 minutes, or up to 35 minutes if a
software upgrade is required. You can monitor bootstrap progress and review the last
seven days of activation history directly from the web app.

The ZTP web app only supports onboarding
to Strata Cloud Manager at this time. For more information about the ZTP onboarding
process for Panorama, see [Set Up Zero Touch Provisioning](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/set-up-zero-touch-provisioning).

###### Activate a ZTP NGFW

Sign in, enter device details, select your deployment site or label, and activate
a ZTP NGFW from your mobile device using the ZTP NGFW Activation web app.

The activation workflow guides you through signing in, entering device details,
associating the NGFW with a deployment site or label, and submitting the
activation. Depending on your setup, you can select a site, a label (if your
administrator has enabled labels), or both. To reach the ZTP Activation Page,
you can either navigate directly to [ztpdeviceactivation or scan the QR code on the back of the
NGFW. On Gen 5 or newer hardware, the QR code opens the page automatically and
pre-populates the Serial Number and Claim Key fields — on all other hardware,
you enter those details manually.](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation)

Port detection checks whether a
cable is connected to the eth1/1 port. It supports select branch and remote
office PA-Series form factors. Only the connected state of the port is detected
— data flow through the port is not verified.

1. Navigate to the [ZTP NGFW Activation](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation) page.
   - (Gen 5 or newer hardware) Open the Camera app on your smartphone
     and scan the QR code on the back of the NGFW. The QR code opens the ZTP
     Activation Page directly and automatically populates the Serial Number
     and Claim Key fields.

     ![]()
   - On your mobile device, navigate directly to [stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation](https://stratacloudmanager.paloaltonetworks.com/ztpdeviceactivation).
2. Sign in to your CSP account.

   ![]()
3. Confirm the device details on the ZTP Activation Page.

   ![]()

   If you scanned the QR code, the Serial Number and
   Claim Key fields are already populated. If
   you are entering details manually, complete all of the following:

   1. Select the Tenant where the ZTP NGFW is
      activated.
   2. Select the CSP Account where the ZTP NGFW
      is activated.
   3. (Manual entry only) Enter the 10–32 character Serial
      Number found on the back of the device.
   4. (Manual entry only) Enter the 8-digit Claim
      Key found on the back of the device.
4. Select a Deployment Site
5. Select your site from the Select Site list and tap
   OK.

   ![]()

   The web app uses your device's location to display sites pending
   deployment within a 2 km radius. If your site is not shown:

   - Tap Tap to change location to manually
     update your location and refresh the filtered list.
   - Toggle Show All Sites to browse the complete
     list of sites pending deployment.
6. Verify Port Connections
7. Tap Verify and confirm eth1/1 connection?.

   Before capturing, ensure the following conditions are met for accurate
   detection:

   - **Clear cable area** — The area around the eth1/1 port must be
     relatively clear. A disorganized bundle of cables overlapping the
     front of the firewall can obstruct the model's view and cause
     incorrect results.
   - **Front-facing angle** — Hold your phone at a front-facing angle
     to the firewall. Looking directly down on top of the chassis
     (bird's-eye view) obscures the port openings and is not
     supported.
   - **Adequate lighting** — The firewall should be illuminated by
     standard office lighting or your phone's flash. Extreme shadows or
     direct glare may reduce detection accuracy.
   - **Horizontal placement only** — The firewall must be placed
     horizontally on a flat surface. Vertical orientations are not
     supported in this release.
8. (Optional) View the reference image in the app to understand the
   required cable configuration for your firewall model.
9. Align the firewall front panel within the overlay guide box on your screen,
   hold your phone steady, and tap the camera button to capture the
   image.

   ![]()

   Ensure the entire firewall fits within the guide box. If you are working
   with a stack of firewalls, focus on the specific firewall you are
   onboarding.

   The web app analyzes the image and reports one of the following
   results:

   - **Eth 1/1 Active** — A cable is detected in the eth1/1 port.
     A checkmark on the activation form confirms the connection. Proceed
     with activation.
   - **Eth 1/1 Not Connected** — No cable is detected in the eth1/1
     port. Check the cabling and retake the image before
     proceeding.
10. Click Activate Device.

    ![]()

    Strata Cloud Manager registers the firewall and the NGFW bootstrap
    process starts. Bootstrap takes approximately 25 minutes, or up to 35
    minutes if a software upgrade is required. You can monitor progress on
    the ZTP Activation Page.

    ![]()
11. (Optional) Select Activate Another
    Device.
12. (Optional) Select Check Activation
    Details to monitor bootstrap progress.
13. Click Done when activation is complete.

###### Monitor Bootstrap Status Using the ZTP Web App

Track the real-time status of the NGFW bootstrap process from your mobile device
after initiating ZTP activation.

After you activate a ZTP NGFW, the firewall begins an automated bootstrap
sequence that downloads licenses, content updates, and software upgrades, then
applies the initial configuration pushed by Strata Cloud Manager. Bootstrap
takes approximately 25 minutes, or up to 35 minutes if a software upgrade is
required.

The ZTP Activation Page shows real-time bootstrap progress through the following
sequential stages:

- **Firewall Licensing** — The firewall downloads and installs its
  assigned license.
- **Content Updates** — App-ID and threat content packages are
  downloaded.
- **WildFire Updates** — WildFire signatures are downloaded.
- **Antivirus Updates** — Antivirus signatures are downloaded.
- **Software Upgrade** — PAN-OS software is upgraded to the target
  version.
- **Default Config Push** — Strata Cloud Manager pushes the initial
  configuration to the firewall.

If an error occurs during bootstrap, the ZTP Activation Page displays a message
with an error code. Contact your network administrator if you see a technical
error during bootstrap. Non-critical failures in antivirus or WildFire updates
display a warning but do not stop the bootstrap process.

1. From the ZTP Activation Page, select Check Activation
   Details.

   ![]()
2. Review the bootstrap status stages and wait for the status to change to
   Done.

   ![]()

   Each stage displays a progress indicator. If a stage shows an error,
   note the error code and contact your administrator. Your administrator
   can monitor the same bootstrap status and any warnings from
   System SettingsDevice ManagementCloud Managed Devices in Strata Cloud Manager.

###### View Activation History Using the ZTP Web App

Monitor recently activated NGFWs and track deployment progress directly from a
mobile device using the ZTP Web App activation history.

The ZTP web app lets you view activation history for devices processed within the
last seven days directly from your mobile device. You can filter results by CSP
account and TSG, search for a specific device by serial number, and tap any
device in the list to view its full activation details.

1. From the ZTP NGFW Activation landing page, select Check
   Activation History.
2. Select your CSP account and TSG
   ID and click Search.
3. (Optional) Enter a serial number to filter the results to a
   specific device.
4. Tap a serial number in the list to view detailed activation status for that
   NGFW.

---

<a id="scm-validate-strata-cloud-manager-onboarding"></a>

### Validate Strata Cloud Manager Onboarding

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding>*

Learn how to validate if you have successfully onboarded to Strata Cloud
Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | One of these:  - [Prisma Access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

This section provides information to help you verify the successful onboarding of NGFW
and Prisma Access deployments. It outlines the necessary details to ensure your devices
are properly integrated and functioning as expected after onboarding.

- [NGFW](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-ngfw-onboarding.html#topic-5ef0de0f-aadf-4b0c-9bad-0a13963bdcca)
- [Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-prisma-access-onboarding.html#validate-prisma-access-onboarding)

### NGFW

#### NGFW for Visibility

After installing the [Panorama CloudConnector plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) and
enabling [Device Telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry), you need to wait for 24
hours to see data in the Strata Cloud Manager Dashboards and Activity Insights.

#### NGFW for Configuration Management

After moving your firewalls to Strata Cloud Manager, validate the onboarding of the
devices by verifying the following:

- **Verify the state of configuration pushes**

  After successful onboarding to
  Strata Cloud Manager, two configuration pushes occur by default to the
  firewall. Select ConfigurationOPERATIONS Push Status to verify that your configuration push was successful.

  1. The first push from Strata Cloud Manager automatically enables the
     Advanced Routing Engine and restarts the firewall.
  2. The second pushes the configuration from Strata Cloud Manager to the
     firewall.
- **Verify the device details in the Cloud Managed Devices**

  Select System SettingsDevice ManagementCloud Managed Devices and check for the serial number for the firewall that you
  just added. By default, newly onboarded firewalls are added to the **All
  Firewalls** folder.
- **Validate firewall connection**

  [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and
  verify that the firewall is successfully connected to Strata Cloud
  Manager.
- Verify that your firewall appears in the **Summary View** of Strata Cloud
  Manager [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center).

### Prisma Access

Validate your successful onboarding by launching Strata Cloud Manager and checking for
data in the [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-overview) and [Dashboards](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/prisma-access-usage).

If you are using Strata Cloud Manager for visibility or have migrated the management
interface from Panorama to Strata Cloud Manager, you will immediately see data in Strata
Cloud Manager. However, if you installed Prisma Access with Strata Cloud Manager as the
management interface and are in the process of configuring its features, you must
complete the full setup to start viewing data.

---

<a id="scm-operationalize-strata-cloud-manager"></a>

### Operationalize Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager>*

Learn how to start using Strata Cloud Manager after onboarding.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access | One of these:  - [Prisma Access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

This section outlines how to operationalize Strata Cloud Manager by detailing the key
configurations and management settings it offers. If you are using Strata Cloud Manager
solely for visibility, you can evaluate the data directly on the respective pages.
However, if you are using Strata Cloud Manager as the management interface, you need to
complete a few configurations to unlock enhanced management experiences and
capabilities.

**Key Configurations in Strata Cloud Manager**

The following are key features and configurations offered by Strata Cloud Manager for
unified management of products in your environment. You can configure these settings
regardless of whether you use SCM for management or visibility.

- [**Configuration Scope**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access/configuration-scope)

  Allows you to
  define the scope of the specific strata cloud manager configuration, whether the
  configuration must apply to a particular device,a folder, or a deployment. There
  are predefined folders which you can refine according to your requirement for
  easy of use. You can also configure snippets to group the
  configuration.
- [**Scope Management**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/access-control/scope-management)

  Update or
  restrict access based on the configuration scope.
- [**Configure reports**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/reports)

  Schedule
  reports to receive dashboard and insights data at regular intervals.
- [**Add favorites**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/favorites)

  Save items of
  interest as favorites and quickly access them from anywhere in Strata Cloud
  Manager.
- [**Access Analyzer for Prisma
  Access**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-access-analyzer)

  Create and run access queries to monitor and analyze access
  and connectivity issues in your SASE environment.

- [Visibility](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager/opeartionalize-visibility.html#topic-f037b1ae-eb02-4e4f-898c-53afb145ebd8)
- [Configuration Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager/operationalize-config-mgmt.html#topic-17f356e7-8911-454e-9b36-c6b2f2f57478)

### Visibility

Learn how to access the Strata Cloud Manager's visibility features after
onboarding.

Here’s a list of pages you can check out to make the most of Strata Cloud Manager’s
visibility features such as, [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards?otp=task_yvz_cqt_fyb#task_yvz_cqt_fyb) and [Activity Insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights) based on your use case and
product.

Some pages listed in the table will contain data only if Strata Logging Service is
configured.

|

Products | Visibility Features | Navigation |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**NGFW** | [Device Health](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/device-health) | Insights OPERATIONALNetsec Health |

|

[Security Posture of NGFW devices](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/security-posture-insights) | InsightsPOSTURESecurity Posture Insights |

|

[Health and Status of ZTNA Connectors](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-data-centers) | ConfigurationZTNA Connector |

|

[Color-coded representation of the devices in your deployment](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/ngfw-devices) | Insights OPERATIONALNetsec Health |

|

[Inventory of devices on your network](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-assets) | InsightsSecurityDevice Security |

|

**Prisma Access** | [Health of all your Prisma Access locations](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-prisma-access-locations) | InsightsPrisma SASEPrisma Access Locations |

|

[Health and performance of your Prisma Access environment](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/prisma-access-usage) | InsightsPrisma SASEPrisma Access Usage |

|

[Health and Conectivity of Remote Networks](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-branch-sites) | InsightsPrisma SASEBranch Sites |

|

[Health and Status of Service Connections](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-data-centers) | InsightsPrisma SASEData CentersService Connections |

|

[Application Experience](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/application-experience) | InsightsApplication Experience |

|

**Common for NGFW and Prisma Access** | [Comprehensive Visibility into your Deployments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center#strata-command-center-threats) | Command center |

|

[Incidents](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts/incidents-and-alerts-prisma-access) | IncidentsNGFW / Prisma Access |

|

[DNS Security data across your NGFW and Prisma Access Deployments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/dns-security) | InsightsActivity InsightsDomains |

|

[Security Posture or Best Practice Adoption](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/best-practices) | InsightsPOSTUREBest Practices |

|

[Threats in your network](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-threats) | InsightsActivity InsightsThreats |

|

[User Activity](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-users-scm) | InsightsActivity InsightsUsers |

|

[URL and Domain Activity](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-urls) | InsightsActivity InsightsDomains |

|

[Rules Inventory](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-rules) | InsightsActivity InsightsRules |

|

[Traffic by Region](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-regions) | InsightsActivity InsightsRegions |

|

[Search any Security Artifact](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/search) | InsightsThreat Search |

<a id="scm-topic-17f356e7-8911-454e-9b36-c6b2f2f57478_ul-msy_jmk_d2c"></a>

### Configuration Management

Learn how to use Strata Cloud Manager's to manage the products in your
environment.

This section highlights the unique Strata Cloud Manager management features compared to
Panorama and outlines the actions you can take after setting up your product for new
deployments.

- **Migrated from Panorama**

  After migrating your configuration from Panorama
  to Strata Cloud Manager, here are some distinctive features you can
  configure and automated tasks you can perform to optimize and secure your
  deployment.

  - [**Feature Parity**](https://docs.paloaltonetworks.com/compatibility-matrix/reference/feature-parity)

    In
    addition to the configuration that is covered in the Strata Cloud
    Manager for Visibility section, there are additional custom
    configuration which are included when you are using Strata Cloud
    Manager for configuration Management.
  - **Exclusive Configuration Management Features**

    In addition to the
    configuration that is covered in the Strata Cloud Manager for
    Visibility section, there are additional custom configuration which
    are included when you are using Strata Cloud Manager for
    configuration Management.

    - [**Custom
      Dashboards**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/custom-dashboard)- Create custom dashboards to get
      visibility into areas of your interest in your network.
    - **[Policy
      Analyzer](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-analyzer)**- Analyze and provide suggestions for
      possible consolidation or removal of specific rules, and also
      checks for anomalies in your rulebase.
    - **[Custom Best Practice
      Check](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/security-posture-settings?otp=task_orq_xlr_jxb#task_orq_xlr_jxb)**-Create custom best practice
      checks.
    - [**User Coaching Notification
      Template**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access/global-settings/user-coaching-notification-template)- Configure the notification
      displayed to your users in the [Access Experience User
      Interface](https://docs.paloaltonetworks.com/autonomous-dem/self-serve-application-experience-troubleshooting/application-experience-user-interface) (UI) when they generate an Enterprise Data
      Loss Prevention (E-DLP) [incident](https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/view-dlp-log-details).
  - **Immediate Actions**
    - [**Optimize rule**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-optimizer)-
      Check the optimized rule suggestions for overly permissive rules
      to close the security gaps.
    - [**Cleanup unused
      configuration and rules**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/config-cleanup)-Remove unused
      configuration and policy rules to ease the administration.
- **New Deployment**

  After setting up Prisma Access or NGFW, you can
  configure the following features exclusive to Strata Cloud Manager:
  - [**Global
    Configurations**](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager.html#tabs-operationalize-strata-cloud-manager_ul-ngl_ybk_d2c)
  - [**Exclusive Configuration
    Management Features**](#scm-topic-17f356e7-8911-454e-9b36-c6b2f2f57478_ul-msy_jmk_d2c)

After completing the initial configuration you can evaluate the data in dashboards and
[Activity insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights%20Activity%20insights%20-) to refine the security
policies and act on any immediate threats.

---

<a id="scm-example-manage-and-secure-network-security-with-strata-cloud-manager"></a>

#### Example: Manage and Secure Network Security with Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager/operationalize-network-security>*

Learn how to operationalize network security with Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) | One of these:  - [AIOps for NGFW Free](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

This example demonstrates how to manage and secure a large financial institution's global
network infrastructure using Strata Cloud Manager.

##### Day 0: Resolve Critical Health Alerts

To address critical health alerts, navigate to [Incidents > NGFW](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts/incidents-and-alerts-ngfw)
in Strata Cloud Manager and filter by the **Health** category. Address the
following alerts:

- **Adverse Encrypted Traffic Resource Usage**

  Indicates low resources for encrypted traffic.

  **Action:** Analyze traffic patterns and reallocate resources to support
  encrypted traffic.
- **Approaching Max Configuration Limits**

  Firewall objects (rules, groups, and security profiles) are nearing device
  limits.

  **Action:** Review and optimize configurations to stay within limits.
- **Increased Traffic Latency - Packet Buffer**

  Packet Buffer resources are running low.

  **Action:** Analyze network traffic and adjust resource allocation to
  ensure sufficient buffer capacity.
- **Tunnel Down**

  Site-to-Site VPN Tunnels are down.

  **Action:** Investigate the VPN configuration and connectivity issues, and
  restore the affected tunnels.
- **NAT Allocation Failure**

  A NAT rule cannot allocate sufficient resources for translation.

  **Action:** Review and adjust NAT rules to ensure adequate resource
  allocation.

##### Day 1: Improve Security Posture and Device Health

- **Best Practices Compliance**

  Navigate to the [Best Practices dashboard](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/best-practices) to
  evaluate security feature configurations against Palo Alto Networks' best
  practices.

  **Action:** Filter by device group and assess specific
  policy rules for compliance. Adjust configurations as needed.
- **Device Posture Insights**

  Use the Security Posture Insights dashboard to review device health,
  including operational status and software versions.

  **Action:** Plan upgrades for outdated software versions using **Insights
  > NGFW > Upgrade Recommendations**.
- **Threat Detection and Response**

  Ensure threat intelligence feeds are updated regularly to detect threats
  effectively.

  **Action:**
  [Set up alert notifications for
  critical alerts](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts/incident-and-alert-settings) so that you can respond to them
  immediately. Furthermore, [integrate AIOps](https://docs.paloaltonetworks.com/ngfw/incidents-and-alerts/alerts/create-a-notification-rule/integrate-with-servicenow) with your
  incident response platform to automate the response process.

##### Day 2: Address Remaining Health Alerts

Resolve vulnerabilities flagged in health alerts, such as:

- **Stale Threat Content**

  Threat intelligence feeds are outdated.

  **Action:** Update feeds by verifying connectivity with the threat
  intelligence servers and scheduling regular updates.
- **Expired Certificates**

  SSL/TLS certificates used for secure communication have expired.

  **Action:** Renew certificates through the issuing Certificate Authority
  (CA) and configure them on relevant devices.
- **Expired Licenses**

  Licenses for Palo Alto Networks products have expired.

  **Action:** Renew licenses through your Palo Alto Networks sales
  representative or customer portal.
- **HA Issues**

  High Availability (HA) between firewalls is not functioning correctly.

  **Action:** Verify HA configurations, including links, statuses, and
  synchronization, and resolve any issues per documentation.

##### Day 3: Review Critical Security Alerts and Assess CVEs

**Review Critical Security Alerts**

Let’s consider some examples to review security alerts.

- **Anti-Spyware Profile Not Strict**

  This alert indicates that one of your Anti-spyware profiles isn't strict,
  which could potentially allow spyware activity on the network. After
  receiving this alert, your security team reviews the alert details. They
  find that the alert is related to the security posture of their platform and
  falls under the category of Malware Defenses. The alert suggests that to
  prevent spyware activity on the network, they should clone the predefined
  strict Anti-Spyware profile and retain the default “reset-both” Action for
  critical, high, and medium severity levels.

  **Action:** Clone and configure a strict profile to block spyware
  effectively.
- **Application Not Set in Rule**

  This alert indicates that an application isn't set in a rule, which could
  potentially allow unauthorized traffic through the firewall. However, upon
  reviewing the alert, the security team realizes that this is due to a new
  application that they are currently testing. They have intentionally not set
  the application in a rule yet because they are still in the process of
  evaluating the application's security.

  **Action:** Temporarily suppress the alert if the application is under
  evaluation. Revisit and configure the rule after completing testing.

**Assess CVE Health**

Navigate to [PAN-OS CVEs](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/pan-os-cve) to see
the security advisories impacting your firewall. This information helps you decide
whether to upgrade a firewall based on the vulnerability and its impact on the
NGFW’s Health and Security.

For example, select a PAN-OS Known Vulnerability
(CVE-2021-44228) incident to see the security advisory on this CVE
impacting your firewall, and then navigate to Vulnerabilities Affecting
this Device Based on Enabled Features to view the affected features
for a vulnerability in the Feature Affected column. If a CVE
is not associated with a feature, then the value under Feature
Affected is empty.

You also select Vulnerabilities in this PAN-OS
version. This helps you decide whether to upgrade a firewall based
on the vulnerability and its impact beyond your enabled features. This type of CVE
affects the firewall with the specified model or version.

After understanding the vulnerabilities for impacted devices, you can plan
your patching using the Software Upgrade Recommendations
feature. View the Impacted Devices and
select firewalls that you want to upgrade to fix the vulnerabilities, and
Generate Upgrade Recommendations. You are redirected to
Software Upgrade Recommendations to view the generated
report.

You can also navigate to [Insights > NGFW > Upgrades
Recommendations](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/software-upgrades) and Generate a New Upgrade
Recommendation. Use this recommendation to upgrade all your NGFWs to
the recommended PAN-OS version.

##### Day 4: Analyze Activity Insights and Address Security Policy Gaps

- **Review Activity Insights:** Navigate to the [Activity
  Insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights) dashboard in your Strata Cloud Manager. You
  can view a holistic picture of all threats detected and blocked in your
  network across various security subscriptions. As an example, you notice an
  alert about "Anti-Spyware Profile Not Strict". After reviewing the alert
  details, you clone the predefined strict Anti-Spyware profile and adjust the
  settings as suggested.
- **Addressing Security Gaps:** While reviewing the
  Activity Insights dashboard, identify the
  security policy rules that enforced the blocked and allowed threats. You
  notice that some rules are allowing threats. To address this, you review
  these rules and make necessary modifications to ensure they block such
  threats in the future.
- **Suppression**: In another instance, you notice an alert about
  "Application Not Set In Rule". However, upon reviewing the alert, you
  realize that this is due to a new application that you are currently
  testing. You have intentionally not set the application in a rule yet
  because you are still in the process of evaluating the application's
  security. In this case, you decide to suppress the alert temporarily until
  you have complete your testing and evaluation of the new application.
- **Assessing Most Impacted Applications and Users:** The
  Activity Insights dashboard also provides
  information about the applications and users most impacted by the threats.
  You review this information to identify any patterns or trends that might
  indicate a larger security issue. If necessary, you take action to address
  these issues, such as updating security policies or providing additional
  training to users.

##### **Ongoing Risk Management**

- Regularly review the [Activity
  Insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights) dashboard to monitor threats and refine
  operational workflows.
- Check the [Best Practices](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/best-practices)
  dashboard periodically, as recommendations evolve with product improvements and
  industry trends.

By following this workflow, you can streamline ongoing risk management and maintain a
secure and efficient network infrastructure.

---

<a id="scm-device-associations-in-strata-cloud-manager"></a>

### Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager>*

Learn about Device Associations and how to get started organizing devices and
associating them with licenses and tenants in Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFWs, including those funded by Software NGFW Credits | One of these:  - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)   If you began using Strata Cloud Manager before these licensing tiers were introduced, [your licenses remain supported](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html). |

Part of Strata Cloud Manager and Common Services, Device Associations provides a centralized management view of all devices in your
deployment. It enables you to organize devices into [tenant service group (TSGs)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) (logical
containers for organizing devices) and makes it easy to associate supported products
with your devices.

You can use Device Associations with the following products:

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/strata-cloud-manager)
- [AIOps for NGFW](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about)
- [Device Security](https://docs.paloaltonetworks.com/iot)
  (Enterprise License Agreement)
- [Next-Generation
  CASB for Prisma Access and NGFW (CASB-X)](https://docs.paloaltonetworks.com/next-gen-casb)
- [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security)
- [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)

![]()

1. In Device Associations
   **(SettingsDevice Associations)**, you can view a list of all of the [tenant service groups (TSGs)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)
   associated with your customer support account.
2. Select a TSG to view any firewalls or Panorama appliances associated
   with it. If you don't see any, you can Add Devices from
   your customer support account.
3. Add Device whenever you need to associate new devices with
   your TSG.
4. After you've added a firewall or Panorama appliance, you can
   Associate Products to begin using the device with
   products that you have activated. The app must be compatible with the hardware
   model of your device, otherwise the device will not appear during app
   association.

- [Associate Devices](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-associate-devices.html#device-associations-associate-devices)
- [Associate Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-associate-product.html#device-associations-associate-product)
- [Remove Associations](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-remove-associations.html#device-associations-remove-associations)

### Device Associations (Associate Devices with a Tenant)

Learn about associating your devices with a tenant.

Before you can begin using a firewall or Panorama
appliance with licensed products that you have activated, you must first associate it
with the [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) in which you have activated a [compatible
product](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html).

1. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
2. Add the firewall or Panorama appliance to your tenant.
   1. Select Add Device.

      Your Customer Support Account is automatically
      selected based on the activated products in the tenant you are in. If
      you have not activated any [products that
      support](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html)
      Device Associations, Add Device will be greyed
      out.
   2. Select one or more firewalls or Panorama appliances.

      You can use a serial number to search for a specific device.
   3. Save.
3. Continue to associate products with devices.

### Device Associations (Associate Devices with a Product)

Learn about associating your devices with a product.

After activating the license for a [supported product](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html), you
use Device Associations to
specify the firewalls or Panorama appliances that you want to use with the
product.

1. Activate your product license.

   How you do this depends on the license you are activating. Please see the
   specific product documentation for more details. You can also see the license
   compatibility with Strata Cloud Manager here.
2. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
3. Associate products with firewalls or Panorama appliances.

   ![]()

   1. Select Associate Products.
   2. In the Products selection column, select the product you want to
      associate.
   3. If applicable, select the type of license.

      Some products have licenses for specific validity terms and device
      models. Only the devices [compatible with the license type](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility.html)
      you selected will appear for association.
   4. Select
      devices.
   5. Save or Apply Licenses.
4. Verify that the association was successful.

   If the association failed, copy the error ID and follow [the steps to open a support case](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/related-documentation/open-support-case). When
   opening the support case, be sure to include the error ID, device serial number,
   TSG ID, and the name of the product that failed association.
5. Return to the documentation for the product you are associating for further
   onboarding steps.

### Device Associations (Remove Device Associations)

Remove Device Associations if you are retiring or returning a device, or associating
it with another tenant.

You may want to remove device associations if, for
example, you are retiring or returning a firewall or Panorama appliance, or if you want
to associate it with another [tenant service group (TSG)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant).

If you are
trying to [convert a trial license to production](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/about-subscription-management/convert-trial-license-to-production),
convert the license instead of disassociating.

1. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
2. Remove product associations.

   If you want to remove a firewall or Panorama appliance from your TSG, you must
   first remove any associated products.

   1. Select the firewalls or Panorama appliances whose products you want to
      disassociate.
   2. Select Remove AssociationsRemove product association.
   3. Select the products you want to remove and Remove
      Associations.
3. Remove a tenant association.

   You can remove tenant associations only from devices
   that have no app associations. If the device is associated with an app,
   remove the app association before proceeding.

   1. Select the firewalls or Panorama appliances that you want to remove
      from your tenant.
   2. Select Remove AssociationsRemove tenant association.
   3. Confirm that you want to proceed and
      Remove.
4. If you are removing a firewall or Panorama appliance to add it to a new TSG,
   [associate it
   with the new TSG](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html).

---

<a id="scm-device-model-compatibility"></a>

#### Device Model Compatibility

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility>*

Check here for the device models that your applications support.

These are the device models that you can associate with different applications.

- [AIOps for NGFW or Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/aiops-for-ngfw-hardware-model-compatibility.html#concept_gqx_52q_hwb)
- [CASB-X](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/casb-x-hardware-model-compatibility.html#id1d78102d-b0fc-46c7-929f-9dbccbb7be02)
- [Device Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-iot.html#concept_k3s_npj_wwb)
- [SaaS Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-saas.html#concept_f3r_1jm_p1c)

#### AIOps for NGFW or Strata Cloud Manager

These are the device models compatible with AIOps for NGFW or Strata Cloud Manager.

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

Panorama Virtual Appliances | - PRA-25 - PRA-100 - PRA-1000 |

|

VM-Series | - VM-200 - VM-300 - VM-500 - VM-600 - VM-700 |

|

200 | - 220 |

|

400 | - 410 - 410R - 440 - 445 - 450 - 450R - 460 |

|

800 | - 820 - 850 |

|

3000 | - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5410 - 5420 - 5430 - 5445 - 5450 |

|

7000 | - 7050 - 7080 |

|

5500 | - 5540 - 5550 - 5560 - 5580 - 5570 |

#### CASB-X

These are the device models compatible with AIOps for NGFW.

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

200 | - 220 |

|

400 | - 400 - 410 - 415 - 440 - 445 - 450 - 450R - 460 |

|

800 | - 820 - 850 |

|

1000 | - 1410 - 1420 |

|

3000 | - 3200 - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5400 - 5420 - 5430 - 5440 - 5445 - 5450 |

|

7000 | - 7050 - 7080 |

#### Device Security

These are the device models compatible with Device Security.

This table contains only the device models that you can associate with Device Security
in Device Associations. The table does not contain information about the Device Security
 [features available with different device model and
PAN-OS version combinations](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/firewall-and-pan-os-support-of-iot-security).

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

VM-Series | - VM-100 - VM-300 - VM-500 - VM-700 |

|

200 | - 200 - 220 - 220R |

|

400 | - 410 - 410R - 440 - 450 - 450R - 460 |

|

500 | - 500 |

|

800 | - 820 - 850 |

|

3000 | - 3020 - 3050 - 3060 - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

7000 | - 7050 - 7080 |

#### SaaS Security

These are the device models compatible with SaaS Security.

This table contains only the device models that you can associate with SaaS Security in Device Associations. The table does not contain information
about the SaaS Security
 [features available with different device model and
PAN-OS version combinations](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/firewall-and-pan-os-support-of-iot-security).

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

200 | - 220 - 220R |

|

400 | - 410 - 410R - 440 - 440R - 450 - 450R - 460 - 460R |

|

800 | - 820 - 850 |

|

3000 | - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5410 - 5420 - 5430 - 5450 |

|

7000 | - 7050 - 7080 |

---

<a id="scm-firewall-and-license-type-compatibility"></a>

#### Firewall and License Type Compatibility

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility>*

Check which firewall and license type combinations your application
supports.

Certain product subscriptions have different license types, which makes them compatible
with only specific types of firewalls and appliances. When you [associate products with devices](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) and select
your product license, only devices that correspond to the license type will appear.
However, some license types, such as eval, trial, and Enterprise License Agreement (ELA)
are compatible with any firewall model.

A firewall type is defined by the firewall SKU. To see the SKU for a firewall, log in to
your Customer Support Portal account and select AssetsDevices and check the entry for the serial number of your firewall in the Model
Name column. This is the SKU, which indicates the firewall type as follows:

- A prod SKU ends with the firewall model name; for example, PAN-PA-410
- An eval SKU ends with -E60, which stands for *Eval + 60 days*; for example,
  PAN-PA-410-E60
- A lab SKU ends with -LAB; for example, PAN-PA-410-LAB

See below for the firewall and license type combinations that your application
supports.

- [Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/strata-cloud-manager-firewall-and-license-type-compatibility.html#strata-cloud-manager-firewall-and-license-type-compatibility)
- [AIOps for NGFW](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/aiops-for-ngfw-firewall-and-license-type-compatibility.html#aiops-for-ngfw-firewall-and-license-type-compatibility)
- [Device Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/firewall-and-license-type-compatibility-iot.html#firewall-and-license-type-compatibility-iot)
- [SaaS Security Inline](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/firewall-and-license-type-compatibility-saas.html#firewall-and-license-type-compatibility-saas)

#### Strata Cloud Manager

These are the firewall and license type combinations that Strata Cloud Manager
supports.

|

Strata Cloud Manager Pro License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**EVAL** | **Yes** | **Yes** | **Yes** | **Yes** |

|

**PROD** | **Yes** | **Yes** | **Yes** | **Yes** |

#### AIOps for NGFW

These are the firewall and license type combinations that AIOps for NGFW
supports.

|

AIOps for NGFW License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

#### Device Security

These are the firewall and license type combinations that Device Security
supports.

|

Device Security License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

#### SaaS Security Inline

These are the firewall and license type combinations that SaaS Security Inline
supports.

|

SaaS Security Inline License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

---

<a id="scm-strata-cloud-manager-activation-onboarding"></a>

## Strata Cloud Manager Activation & Onboarding

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding>*

---

<a id="scm-activate-strata-cloud-manager-pro-with-the-enterprise-license-agreement"></a>

##### Activate Strata Cloud Manager Pro with the Enterprise License Agreement

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ela>*

Learn about how to activate Strata Cloud Manager Pro for Enterprise License Agreement
users.

This task shows how to activate Enterprise License Agreement (ELA) for Strata Cloud
Manager. The add-on for ELA is a consumption model for large enterprises to assign
subscriptions in bulk to assets purchased from Palo Alto Networks.

Here are the prerequisites for NGFW:

- **[Cloud Management Onboarding
  Prerequisites](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/prerequisites-for-cloud-management-onboarding)** - Before onboarding your NGFW to Strata Cloud
  Manager, verify that all conditions for device readiness are fulfilled. This
  includes network configuration, software compatibility, and licensing
  requirements. Completing these steps ensures that your firewall can be
  successfully managed using Strata Cloud Manager.
- **[TCP Ports and FQDNs for Cloud
  Management](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/tcp-ports-and-fqdns-required-for-cloud-management)** - To enable seamless communication between the
  NGFW and Strata Cloud Manager, configure specific TCP ports and Fully Qualified
  Domain Names (FQDNs).

You can activate multiple Strata Cloud Manager Pro tenants using the same license
for devices belonging to the same support accounts. To do this, navigate to the
Tenant Management to [create new tenants](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants). Then, go to the
Subscriptions & Add-ons, search for your
subscription, click Activate Cloud Tenant that will
redirect you to the activation page. Choose the same TSG on the activation page
that you used initially.

1. Use one of the following activation methods.

   - Log in to
     [Activation Console](https://apps.paloaltonetworks.com/hub) and select ELA Activation Strata Cloud Manager.

     ![]()
   - Log into the Customer Support Portal and activate from License ManagementLicenses, and then click ELA-Ngfw
     Activation.
2. Select Tenant where you will activate Strata Cloud
   Manager Pro. If you don't have an existing [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), **Create New**.
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with
   one year of log retention.

   ![]()
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
   Activation Status for both to show Complete.
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) and select Common Services > Device
      Associations.
   2. **Associate Products**.
   3. In the Licensed Products selection column, select
      Strata Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
   Cloud Manager assesses the health of the devices in your deployment by analyzing
   telemetry data that your PAN-OS devices send to Strata Logging Service. To send
   this data, you must have enabled device telemetry on your devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    Activation Console.

---

<a id="scm-activate-strata-cloud-manager-pro-with-the-enterprise-support-agreement"></a>

##### Activate Strata Cloud Manager Pro with the Enterprise Support Agreement

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-esa>*

Learn about how to activate Strata Cloud Manager Pro for NGFW with the Enterprise
Support Agreement.

The Palo Alto Networks Enterprise Support Agreement (ESA) Pro includes
Strata Cloud Manager Pro for NGFW. ESA Pro provides a streamlined solution for a
consistent support experience across your existing assets and anticipated purchases.
This enterprise program enables organizations to maximize savings and benefits as
they scale up, making it an ideal choice for customers with large, expanding
firewall deployments.

This task shows how to activate ESA Pro for Strata Cloud Manager. You can
start the ESA Pro activation process from the
Activation Console or Customer Support Portal as
described below.

1. Use one of the following activation methods:

   - Log in to
     [Activation Console](https://apps.paloaltonetworks.com/hub) and select ESA Activation Strata Cloud Manager.

     ![]()
   - Log in to the Customer Support Portal. In the left side-panel, go to
     License Management, and then, under
     Licenses, select Activate
     Enterprise Agreement.

     ![]()
2. Create a New tenant where you will activate the Strata
   Cloud Manager instance.

   ![]()
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   A Strata Cloud Manager Pro license includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with one
   year of log retention.

   ![]()
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
   Activation Status for both to show Complete.
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Log in to the
      Activation Console and select
      Common Services > Device
      Associations.
   2. **Associate Products**.
   3. In the Licensed Products selection column, select
      Strata Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on the devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics).
   Strata Cloud Manager assesses the health of the devices in your deployment by
   analyzing telemetry data that your PAN-OS devices send to Strata Logging
   Service. To send this data, you must have enabled device telemetry on your
   devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    [Activation Console](https://apps.paloaltonetworks.com/hub).

---

<a id="scm-activate-strata-cloud-manager-pro-for-ngfw"></a>

##### Activate Strata Cloud Manager Pro for NGFW

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ngfw>*

Learn about how to activate Strata Cloud Manager Pro for NGFW.

This task shows how to activate Strata Cloud Manager Pro for NGFW. For details about
device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

Here are the prerequisites for NGFW:

- **[Cloud Management Onboarding
  Prerequisites](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/prerequisites-for-cloud-management-onboarding)** - Before onboarding your NGFW to Strata Cloud
  Manager, verify that all conditions for device readiness are fulfilled. This
  includes network configuration, software compatibility, and licensing
  requirements. Completing these steps ensures that your firewall can be
  successfully managed using Strata Cloud Manager.
- **[TCP Ports and FQDNs for Cloud
  Management](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/tcp-ports-and-fqdns-required-for-cloud-management)** - To enable seamless communication between the
  NGFW and Strata Cloud Manager, configure specific TCP ports and Fully Qualified
  Domain Names (FQDNs).

1. After you receive an email from Palo Alto Networks identifying the Strata Cloud
   Manager Pro license you're activating, click the email link to begin the
   activation process.
2. Select Tenant where you will activate Strata Cloud
   Manager Pro. If you don't have an existing [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), **Create New**.
3. Select a Region where you want to deploy Strata Cloud
   Manager. See the [supported regions for Strata Cloud
   Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).

   Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with
   one year of log retention.
4. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
5. Agree to the Terms and Conditions, and
   Activate.
6. Wait for Strata Cloud Manager, Cloud Identity Engine, and Strata Logging
   Service to initialize, and for Status to show Complete.

   ![]()
7. [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
   a tenant containing your Strata Cloud Manager.

   Make sure to individually associate all the
   firewalls managed by Panorama to the tenant.

   1. Navigate to Common Services > Device
      Associations.
   2. Add Devices.
   3. Select one or more firewalls or Panorama appliances and
      Save.
8. [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
   activating Strata Cloud Manager Pro, you need to specify the firewalls or
   Panorama appliances that you want to use with it.

   1. Navigate to Common Services > Device
      Associations.
   2. **Associate Products**.

      ![]()
   3. In the Products selection column, select Strata
      Cloud Manager.
   4. Select devices and **Save**.
9. [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
   Cloud Manager assesses the health of the devices in your deployment by analyzing
   telemetry data that your PAN-OS devices send to Strata Logging Service. To send
   this data, you must have enabled device telemetry on your devices.

   Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
   10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
   configures telemetry to be enabled by default on your devices. Upon
   onboarding a new device (Panorama or firewall), telemetry is automatically
   enabled with settings centrally controlled through Strata Cloud Manager or
   Activation Console.
10. Log in to Strata Cloud Manager by clicking on its icon in the
    Activation Console.

---

<a id="scm-activate-strata-cloud-manager-pro-for-prisma-access"></a>

##### Activate Strata Cloud Manager Pro for Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-prisma-access>*

Learn about how to activate Strata Cloud Manager Pro for Prisma Access.

All [Prisma Access license types](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license) include access
to Strata Cloud Manager, and all Prisma Access deployments can leverage Strata Cloud
Manager for visibility features – like Command Center and Activity Insights – and
 [Autonomous DEM](https://docs.paloaltonetworks.com/autonomous-dem) monitoring.

Additionally, can optionally choose to use Strata Cloud Manager for your [Prisma Access configuration management](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/how-to-manage-prisma-access);
your other option is to use Panorama for configuration management. In both cases,
you'll be guided to activate Strata Cloud Manager Pro during your Prisma Access
license activation:

- [Activate Prisma Access, with Strata Cloud
  Manager configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation)
- [Activate Prisma Access, with Panorama
  configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation)

---

<a id="scm-activate-strata-cloud-manager-pro-for-vm-series-with-software-ngfw-credits"></a>

##### Activate Strata Cloud Manager Pro for VM-Series with Software NGFW Credits

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-vm-series-with-software-ngfw-credits>*

Learn about how to activate Strata Cloud Manager Pro for VM-Series with Software NGFW
Credits.

You can manage VM-Series firewalls funded by Software NGFW Credits using Strata Cloud
Manager, enabling seamless access to advanced management and monitoring features
through Strata Cloud Manager Pro activation.

Strata Cloud Manager supports management of both standalone VM-Series firewalls and
Panorama-managed VM-Series deployments, offering a comprehensive solution for
overseeing multiple environments:

- [Activate Strata Cloud Manager Pro for
  VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-vm-flex-aiops)
- [Activate Strata Cloud Manager Pro for
  Panorama Managed VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-aiops-panorama-credits)

---

<a id="scm-device-associations-associate-devices-with-a-tenant"></a>

#### Device Associations (Associate Devices with a Tenant)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-associate-devices>*

Learn about associating your devices with a tenant.

Before you can begin using a firewall or Panorama
appliance with licensed products that you have activated, you must first associate it
with the [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) in which you have activated a [compatible
product](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html).

1. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
2. Add the firewall or Panorama appliance to your tenant.
   1. Select Add Device.

      Your Customer Support Account is automatically
      selected based on the activated products in the tenant you are in. If
      you have not activated any [products that
      support](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html)
      Device Associations, Add Device will be greyed
      out.
   2. Select one or more firewalls or Panorama appliances.

      You can use a serial number to search for a specific device.
   3. Save.
3. Continue to associate products with devices.

---

<a id="scm-device-associations-associate-devices-with-a-product"></a>

#### Device Associations (Associate Devices with a Product)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-associate-product>*

Learn about associating your devices with a product.

After activating the license for a [supported product](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html), you
use Device Associations to
specify the firewalls or Panorama appliances that you want to use with the
product.

1. Activate your product license.

   How you do this depends on the license you are activating. Please see the
   specific product documentation for more details. You can also see the license
   compatibility with Strata Cloud Manager here.
2. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
3. Associate products with firewalls or Panorama appliances.

   ![]()

   1. Select Associate Products.
   2. In the Products selection column, select the product you want to
      associate.
   3. If applicable, select the type of license.

      Some products have licenses for specific validity terms and device
      models. Only the devices [compatible with the license type](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility.html)
      you selected will appear for association.
   4. Select
      devices.
   5. Save or Apply Licenses.
4. Verify that the association was successful.

   If the association failed, copy the error ID and follow [the steps to open a support case](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/related-documentation/open-support-case). When
   opening the support case, be sure to include the error ID, device serial number,
   TSG ID, and the name of the product that failed association.
5. Return to the documentation for the product you are associating for further
   onboarding steps.

---

<a id="scm-device-associations-remove-device-associations"></a>

#### Device Associations (Remove Device Associations)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-remove-associations>*

Remove Device Associations if you are retiring or returning a device, or associating
it with another tenant.

You may want to remove device associations if, for
example, you are retiring or returning a firewall or Panorama appliance, or if you want
to associate it with another [tenant service group (TSG)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant).

If you are
trying to [convert a trial license to production](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/about-subscription-management/convert-trial-license-to-production),
convert the license instead of disassociating.

1. Navigate to Device Associations using the
   Activation Console or Strata Cloud Manager.
   1. (Optional) Log in to the
      [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.

      ![]()
   2. (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
2. Remove product associations.

   If you want to remove a firewall or Panorama appliance from your TSG, you must
   first remove any associated products.

   1. Select the firewalls or Panorama appliances whose products you want to
      disassociate.
   2. Select Remove AssociationsRemove product association.
   3. Select the products you want to remove and Remove
      Associations.
3. Remove a tenant association.

   You can remove tenant associations only from devices
   that have no app associations. If the device is associated with an app,
   remove the app association before proceeding.

   1. Select the firewalls or Panorama appliances that you want to remove
      from your tenant.
   2. Select Remove AssociationsRemove tenant association.
   3. Confirm that you want to proceed and
      Remove.
4. If you are removing a firewall or Panorama appliance to add it to a new TSG,
   [associate it
   with the new TSG](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html).

---

<a id="scm-aiops-for-ngfw"></a>

##### AIOps for NGFW

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/aiops-for-ngfw-firewall-and-license-type-compatibility>*

These are the firewall and license type combinations that AIOps for NGFW
supports.

|

AIOps for NGFW License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

---

<a id="scm-device-security"></a>

##### Device Security

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/firewall-and-license-type-compatibility-iot>*

These are the firewall and license type combinations that Device Security
supports.

|

Device Security License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

---

<a id="scm-saas-security-inline"></a>

##### SaaS Security Inline

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/firewall-and-license-type-compatibility-saas>*

These are the firewall and license type combinations that SaaS Security Inline
supports.

|

SaaS Security Inline License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**TRIAL** | No | **Yes** | **Yes** | **Yes** |

|

**EVAL** | No | **Yes** | **Yes** | **Yes** |

|

**NFR** | **Yes** | No | No | No |

|

**LAB** | No | **Yes** | No | No |

|

**PROD** | No | No | **Yes** | No |

---

<a id="scm-strata-cloud-manager"></a>

##### Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility/strata-cloud-manager-firewall-and-license-type-compatibility>*

These are the firewall and license type combinations that Strata Cloud Manager
supports.

|

Strata Cloud Manager Pro License Types | Firewall Types | | | |

| --- | --- | --- | --- | --- |
|

**NFR** | **LAB** | **PROD** | **EVAL** |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

**EVAL** | **Yes** | **Yes** | **Yes** | **Yes** |

|

**PROD** | **Yes** | **Yes** | **Yes** | **Yes** |

---

<a id="scm-aiops-for-ngfw-or-strata-cloud-manager"></a>

##### AIOps for NGFW or Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/aiops-for-ngfw-hardware-model-compatibility>*

These are the device models compatible with AIOps for NGFW or Strata Cloud Manager.

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

Panorama Virtual Appliances | - PRA-25 - PRA-100 - PRA-1000 |

|

VM-Series | - VM-200 - VM-300 - VM-500 - VM-600 - VM-700 |

|

200 | - 220 |

|

400 | - 410 - 410R - 440 - 445 - 450 - 450R - 460 |

|

800 | - 820 - 850 |

|

3000 | - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5410 - 5420 - 5430 - 5445 - 5450 |

|

7000 | - 7050 - 7080 |

|

5500 | - 5540 - 5550 - 5560 - 5580 - 5570 |

---

<a id="scm-casb-x"></a>

##### CASB-X

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/casb-x-hardware-model-compatibility>*

These are the device models compatible with AIOps for NGFW.

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

200 | - 220 |

|

400 | - 400 - 410 - 415 - 440 - 445 - 450 - 450R - 460 |

|

800 | - 820 - 850 |

|

1000 | - 1410 - 1420 |

|

3000 | - 3200 - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5400 - 5420 - 5430 - 5440 - 5445 - 5450 |

|

7000 | - 7050 - 7080 |

---

<a id="scm-device-security-1"></a>

##### Device Security

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-iot>*

These are the device models compatible with Device Security.

This table contains only the device models that you can associate with Device Security
in Device Associations. The table does not contain information about the Device Security
 [features available with different device model and
PAN-OS version combinations](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/firewall-and-pan-os-support-of-iot-security).

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

VM-Series | - VM-100 - VM-300 - VM-500 - VM-700 |

|

200 | - 200 - 220 - 220R |

|

400 | - 410 - 410R - 440 - 450 - 450R - 460 |

|

500 | - 500 |

|

800 | - 820 - 850 |

|

3000 | - 3020 - 3050 - 3060 - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

7000 | - 7050 - 7080 |

---

<a id="scm-saas-security"></a>

##### SaaS Security

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-saas>*

These are the device models compatible with SaaS Security.

This table contains only the device models that you can associate with SaaS Security in Device Associations. The table does not contain information
about the SaaS Security
 [features available with different device model and
PAN-OS version combinations](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/firewall-and-pan-os-support-of-iot-security).

|

Series | Models |

| --- | --- |

|  |  |
| --- | --- |
|

200 | - 220 - 220R |

|

400 | - 410 - 410R - 440 - 440R - 450 - 450R - 460 - 460R |

|

800 | - 820 - 850 |

|

3000 | - 3220 - 3250 - 3260 - 3410 - 3420 - 3430 - 3440 |

|

5000 | - 5220 - 5250 - 5260 - 5280 - 5410 - 5420 - 5430 - 5450 |

|

7000 | - 7050 - 7080 |

---

<a id="scm-migrate-configurations-from-panorama-to-strata-cloud-manager-ngfw"></a>

#### Migrate Configurations From Panorama to Strata Cloud Manager (NGFW)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-ngfw>*

Learn about the migration process for migrating your NGFW deployments from Panorama to
Strata Cloud Manager.

This feature is available on request. Contact your account team to enable the
feature.

You can migrate your existing NGFW configurations from Panorama to Strata Cloud
Manager for cloud-based configuration management.

During the migration, Strata Cloud Manager:

- Copies and translates supported security policies, network configurations, and
  objects.
- Maintains existing network topology and NGFW deployments.
- Highlights areas that are partially supported or unsupported.

Managing your NGFWs using [Strata Cloud Manager instead of Panorama can offer you benefits such
as](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview) unified management for Prisma Access and NGFWs, cloud-native scalability of your
network, and enhanced visibility.

Strata Cloud Manager guides you through migrating your configurations with these
key steps:

- Upload existing configurations — Import your current Panorama
  configurations.
- Run compatibility assessment — Identify unsupported features or
  configurations that need attention.
- Perform validation and prepare for deployment — Complete final checks before
  migration.
- Migration control — Devices and device groups can be migrated in phases,
  allowing you to migrate non-critical devices or go site-by-site.

Review results at each step, make necessary adjustments, and verify that your
configurations are fully compatible with Strata Cloud Manager before completing the
migration.

##### How Configuration Management Changes When You Move from Panorama to Strata Cloud Manager

Panorama configuration management is based on:

- Device Groups — Organize firewalls into hierarchical groups for security policy
  management (security rules, NAT policies, application filters).
- Templates and Template Stacks — Define network and device settings (interfaces,
  zones, routing, system settings).
- Inheritance — Device Groups inherit policies from parent groups; Template Stacks
  layer multiple templates with override capabilities.

Strata Cloud Manager configuration management is based on:

- Folders — Hierarchical containers that hold both security policies AND network
  configurations.
- Snippets — Reusable configuration blocks that can be attached to folders at any
  level.
- Containers — Device-specific configuration holders for unique firewall requirements
  .

During migration, Strata Cloud Manager converts your Panorama-based
configuration and builds it into folders and snippets:

|

**Panorama** | **Strata Cloud Manager** |

| --- | --- |

|  |  |
| --- | --- |
|

Device Groups | Folders |

|

Templates & Template Stacks | Snippets |

|

Policies and Profiles | Snippets |

|

Shared Objects | Global folder as an attached Snippet |

|

Policies in Device Groups | Policies under mapped Folder(s) |

|

Objects (addresses, EDLs, etc.) | Objects under mapped Folder(s) |

Key difference between Panorama and Strata Cloud Manager to keep in mind:

- Strata Cloud Manager Folders contain both network and security
  configurations, while Panorama separates these between Templates and Device Groups
- Strata Cloud Manager Folders provide more flexible inheritance with
  Snippet-based overrides versus the lower-level group overrides seen in Panorama
- Strata Cloud Manager Snippets provide a more plug-and-play approach to configurations
  compared to Panorama's Templates and Template stacks that are inherited down the
  stack.

After migration, you manage configurations through the folder and snippet
model. Snippet attachment order determines configuration precedence, providing granular
control over how multiple configuration sources combine. You can also create
device-specific containers for NGFWs requiring unique configurations outside the folder
inheritance model.

**Additional Resources**

Learn more about [Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups) and [Templates](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks).

Learn more about [Snippets](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets) and [Folders](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management)

##### Prepare to Migrate Your Panorama NGFW Configurations to Strata Cloud Manager

Before beginning the migration, ensure you have the following items ready:

- Minimum Software Requirements: PAN-OS 10.2.3 or later
- [Export Panorama Configuration File](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations): Export the
  complete running configuration from your source Panorama instance in XML format
- [Panorama Master Key](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-the-master-key-from-panorama): Obtain the master key used for
  encryption in your Panorama configuration (if not using the default key)
- [Strata Cloud Manager Tenant](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager): Verify that your Strata
  Cloud Manager tenant is deployed, properly licensed, and operational
- [NGFW Configuration](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/troubleshooting/troubleshoot-panorama-system-issues/generate-diagnostic-files-for-panorama): Collect the last-pushed
  configuration files (Technical Support Files) from NGFWs you plan to validate
  post-migration
- [Network Topology](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management): Review your current device group
  hierarchies, template relationships, and NGFW assignments
- [Configuration Backup](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups): Create complete backups of your
  current Panorama and NGFW configurations as a safety measure
- [Administrative Access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Ensure you have access to the
  Superuser role in both Panorama and Strata Cloud Manager.
- Migration Planning: Identify which device groups, templates, and NGFWs you
  want to migrate in your initial phase
- [Compatibility Matrix](https://docs.paloaltonetworks.com/compatibility-matrix): Understand which features may not be
  supported in Strata Cloud Manager and plan for any necessary configuration
  adjustments
- Unsupported Functionalities: Migration of configurations to Strata Cloud Manager is
  not supported if the **intrazone-default** and **interzone-default** policies
  have been overwritten at the Device Group level. If these default security rules are
  overwritten, the migration tool cannot process the Panorama configuration. You must
  remove these overwritten policies from Panorama, commit your changes, and re-export
  the running-config.xml before attempting the migration.

##### Migrate Your Panorama NGFW Configurations to Strata Cloud Manager

Migrate your NGFW configurations from Panorama to Strata Cloud Manager:

1. Prepare your Panorama for the migration.
   1. Log in to the Panorama that manages your NGFWs with an administrative account
      that is assigned the [Superuser](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-cli-quick-start/get-started-with-the-cli/give-administrators-access-to-the-cli/administrative-privileges) role.
   2. **(Optional)** If you have configured a custom Master Key for
      Panorama, make a note of it.

      If your deployment uses the default Master Key, this step isn't
      required.
   3. Ensure that your current Panorama configuration is up to date and that you have
      committed and pushed all your current changes to Panorama by going to CommitCommit & Push and Preview Changes.
   4. **(Optional)** Check the diffs between the running configuration and
      the candidate configuration and determine whether you want to push those changes. To
      commit and push the changes, Edit Selections and select the
      NGFWs you want to push in the Push Scope.
   5. **(Optional)**
      Commit and Push your changes.
   6. Go to PanoramaSetupOperations and Export the named Panorama configuration
      snapshot.

      The .xml file is required to upload to Strata Cloud Manager during the migration
      process. Don't upload a techsupport file or any other file except an .xml
      configuration file.
   7. Select the running-config.xml configuration file and click
      OK.
2. Log in to Strata Cloud Manager as an administrator with a Superuser role and go to ConfigurationOnboarding.

   ![]()

   The migration program detects that you have a Panorama managed
   deployment.

   1. Confirm the tenant is correct.
   2. (Optional) [Create a Named Snapshot](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot?otp=task-uzv_3lr_vcc#task-uzv_3lr_vcc) of your running
      configuration in the event that a rollback is necessary.

   Migration should not be attempted during an Strata Cloud Manager upgrade
   window. Check your upgrade schedule to see if you have an upcoming upgrade.
3. Read the migration Overview.

   ![]()

   1. Review the management building blocks of Strata Cloud Manager:
      Folders and Snippets.
   2. Click Next: Upload Panorama Configuration.
4. Upload the Panorama configuration.

   ![]()

   ![]()

   1. Select the Panorama configuration *.xml* file you downloaded in an earlier
      step by dragging and dropping it from your file explorer or selecting
      Choose File.
   2. **(Optional)** Input your Master Key or, if
      you did not create a custom master key, use the Default
      one.

      ![]()
   3. Click Next: Review Migration Compatibility.

   If the migration tool produces any errors that cannot
   resolve automatically, you may have a configuration that is unsupported. Click
   Cancel Migration, remove these overwritten policies from your
   Panorama configuration, re-export the configuration file, and restart the migration
   process.
5. Review the configuration compatibility.

   ![]()

   1. **(Optional)**
      Export Compatibility Summary and review your organization’s
      configuration compatibility before continuing and allowing Strata Cloud Manager to
      trim any unsupported or partially supported configurations.

      The trimming of unsupported and partially supported features avoids migrating
      features that cannot be deployed safely or securely in Strata Cloud Manager.

      This process will only impact the staged configuration for Strata Cloud Manager.
      The configurations in Panorama will remain unaffected.

      For each flagged area, you should plan to rebuild, replace, or defer those
      configurations.

      ![]()
   2. Review the Unsupported Features that will be trimmed from
      your configuration during the migration.

      These features will be trimmed from your configurations and will not be staged in
      Strata Cloud Manager during the configuration migration process.
   3. Review the Partially Supported Features and determine a
      resolution path.

      Identify what exactly is going to be missing from the configuration.

      You can accept the partially supported features and build a remediation plan
      post-migration or return to your Panorama configuration and clean these areas up
      before starting the migration process again.
   4. Acknowledge the unsupported and partially supported
      features.
   5. Click Next: Select Device Groups to Migrate.

   For those just looking to compare supported
   configurations, or if it is decided than more planning is needed, you can end the
   migration process here.
6. Select the Devices or Device Groups you
   would like to migrate.

   If you are migrating NGFWs from Panorama for the first
   time, it is recommended to only migrate non-critical devices or device groups first to
   test how your configurations will be migrated to Strata Cloud Manager.

   ![]()

   During the migration:

   - Objects are imported to a Snippet and attached to the Global
     folder.
   - Policies are imported under the Folder(s) migrated by the workflow.
   - Shared Device Groups are automatically mapped to the All Firewalls
     Folder.

   After selecting the devices, click Next: Map Templates to
   Folders.
7. Map Templates to your newly configured
   Folders.

   ![]()

   You can choose between two template mapping
   options:

   - Auto Template Mapping: Automatically associate template
     and template stack configurations with folders after migration to snippets. This
     feature eliminates the need for manual configuration mapping and reduces the
     iterative process that you typically face during the migration workflow.

     Strata Cloud Manager processes the entire Panorama configuration, even
     when you only select a subset of device groups for migration. This comprehensive
     analysis prevents issues in subsequent device group migrations; however, it may
     extend the processing time for the initial migration.
   - Manual Template Mapping: Manually associate template and
     template stack configurations with folders after migration to snippets.

   - During migration, Device Groups are transformed into folders, while templates
     and template stacks are converted into configuration snippets.
   - If two or more Device Groups reuse the same template, elevate it to a higher
     folder. If only one site requires it, keep it at the site level.

   Here is the procedure to manually associate templates:

   1. Select a Device Group to reveal the
      Templates/Template Stacks used by that device group.

      ![]()
   2. Edit the mapping to assign each
      Template/Template Stack to a
      Folder.
   3. Elevate templates referenced in multiple places to higher folders.

      For example, if you have global template settings, mapping them to the All
      Firewalls folder establishes those settings as the source of truth for all NGFWs.
   4. After assigning more than one Snippet to a Folder, adjust the order.
   5. Move Up or Move Down to finalize
      the order.
   6. Update the order.
   7. Save the new order.

      Before moving on to the next step, ensure the following:
      - No unassigned templates or template stacks remain.
      - Any templates referenced by multiple device groups have been elevated to the
        proper folders.
8. Click Next: Prepare Migration.

   The migration process begins.

   Wait for all steps to be completed.

   If there are any issues with the migration, return to the previous steps to
   evaluate and make changes. If issues continue to persist, please contact Palo Alto
   Networks Support.
9. Prepare to migrate.
   1. Load Configuration to Strata Cloud Manager to prepare to
      migrate.

      1. The migration worfklow:
         - Translates Devices and Device Groups and Templates and Template Stacks to
           Folders and Snippets using the mappings and snippets order defined by
           you.
         - Creates a Strata Cloud Manager snapshot to enable rollback of staged
           changes.
         - Checks for conflicts in existing Strata Cloud Manager configurations (name
           collisions, missing references, 31-character limits, RBAC scope).
         - Builds the staged configuration that will be in Strata Cloud Manager
           post-load.
   2. Load Results and review what objects, policies, or
      snippets were created, updated, or skipped.
   3. Review the Validation Results for any errors, warning, and
      informational messages post migration.
   4. Click Next: Review Config Diffs.

      This commits the newly generated configuration to Strata Cloud Manager.
10. Review the configuration diffs.

    When reviewing your configuration diffs, you may notice
    that secret keys or passwords appear as **Modified**. This is expected behavior.
    Because Strata Cloud Manager uses a different Master Key than your Panorama instance,
    the encrypted string representing the key changes during the translation process. The
    underlying plaintext key remains exactly the same, and no action is required.

    1. In the left folder tree, expand to the Folder and select an NGFW serial number to
       be validated
    2. Browse File and choose the TSF for the selected serial
       number.

       Uploading the TSF for the chosen NGFW will allow you to properly validating all
       the supported, partially supported, and unsupported configurations.

       The configuration diff viewer provides a structured interface to
       inspect complex configuration changes by organizing modifications, additions, and
       deletions into categorized views. The diff viewer helps you identify created,
       modified, or deleted configuration elements. Because the migration process might
       trim certain configurations, you can use the search functionality to locate
       specific configuration elements by name, object type, or difference category. This
       streamlines the review process for migrations with extensive configuration
       differences.

       Strata Cloud Manager
       categorizes configuration diffs into three groups:

       - Modified/Missing—Represents changes to
         existing objects during the migration process. This includes items with
         changed values or missing object references.
       - Unsupported—Represents items that cannot be
         migrated due to feature parity gaps between Panorama® and Strata Cloud
         Manager, detected using predefined parity checks. This category also includes
         features that have alternate implementation in Strata Cloud Manager.
       - Informational—Represents changes where object
         functionality remains the same but names or references have been automatically
         updated to comply with Strata Cloud Manager naming conventions (for example,
         profile names).

       The diff viewer includes the following components and capabilities to
       help you analyze these configuration changes:

       - **Grid grouping and full-screen mode**—Diff entries are grouped
         by object type in the grid, allowing you to expand and collapse sections for
         an organized review. To facilitate the inspection of complex changes, you can
         activate a full-screen mode using the maximize button.
       - **Informational category tags**—When you select the
         Informational category, descriptive tags display
         counts for each subcategory: Default Additions, Reference Updated, Removed
         Unused, and Renamed. You can hover over each tag for a tooltip description and
         use the grid filter to narrow results to a specific subcategory.
       - **Tabbed views**—A tabbed interface allows you to switch between
         a **Diff** view, which shows the before-and-after configuration state, and
         an **Object Names** view, which lists every individual object affected by
         that change pattern.
       - **Detailed columns**—Each diff entry displays an **Action**
         column indicating whether the change is an addition, deletion, or
         modification. A **Sub-Category** column appears for Informational diffs and
         is hidden by default for other categories. Additionally, a **Description**
         column is available for the Unsupported category to explain why a
         configuration element cannot be migrated.

       Because of naming conventions in Strata Cloud Manager, some long names will be
       compressed when needed.

       ![]()
    3. Review the configuration diff panes.

       1. Green Panes: Created or added. They are present in Strata Cloud
          Manager, but not on the original device.
       2. Red Panes: Deleted or trimmed. May not be supported in Strata Cloud
          Manager, but are on the device.

       The diff view may be extensive, limited to one NGFW at a time, and
       calculated from the last pushed XML from the TSF.
    4. Verify the diffs for representative devices from each pattern or site type.
    5. (Optional)
       Export the diff results.
    6. (Optional)Regenerate Diffs if any corrections
       have been made.
    7. Click Next: Confirm and Finish.
11. Confirm and finish your migration of configurations to Strata
    Cloud Manager.

    The migration tool does not onboard your NGFWs! You must still onboard your NGFWs
    to Strata Cloud Manager.

    Now that your Panorama configurations are Strata Cloud Manager, ready for device
    onboarding and pushes performed from SCM.

    With the configuration migration complete, review the available [documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) for onboarding and managing NGFWs in Strata Cloud Manager.

    1. Ensure the results from Steps 8 and 9 are accepted.
    2. Confirm the migration.

       This officially marks the migration as complete.
    3. (Optional) To revert the configuration to its pre-migration state at any
       point, select Revert. This initiates a rollback workflow,
       restoring Strata Cloud Manager to a Snapshot taken before the migration was
       loaded.
    4. (Optional) To cancel the migration at any point, select
       Cancel Migration. This aborts the migration process and
       cleans up any temporary changes.

##### Post-Migration

After confirming the configuration migration in the tool, the configuration is staged in
Strata Cloud Manager but has not yet been pushed to your NGFWs. The NGFWs are still
managed by Panorama, now you must onboard them to Strata Cloud Manager to proceed with
cloud management.

To complete the transition to Strata Cloud Manager, you must perform pre-onboarding
checks, [onboard your NGFWs to Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html), and execute a [configuration push](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config).

###### Onboard NGFWs to Strata Cloud Manager

You must onboard your NGFWS to Strata Cloud Manager to transfer management authority
from Panorama to the cloud. You can migrate devices in phases (for example, by device
group or site). For detailed steps on associating devices and configuring connectivity,
see [Onboard to Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html).

**General Onboarding Guidelines**

- **Associate Devices:** Ensure all firewalls are associated with your Strata Cloud
  Manager tenant.
- **Move to Cloud Management:** Use the Strata Cloud Manager onboarding workflow to
  move the device to **Cloud Management**.
- **Verify Placement:** Confirm that the device shows a **Connected** status in
  Strata Cloud Manager and appears under the correct intended Folder.

###### First Push and Validation

Once devices are onboarded and connected, you must [push the staged configuration](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config) from Strata Cloud
Manager to enforce policies.

Once you have pushed the staged configuration, validate:

- Commit success.
- Session health and traffic flow.
- Interface, virtual router, and HA status.
- Log forwarding to Strata Logging Service.

Once you have validated your push, take screenshots of the connected state and
successful push for your validation report.

###### Rollback Readiness

If critical issues arise during the pre-onboarding or onboarding phases, you can revert
Strata Cloud Manager to its state prior to the migration.

Use [Configuration: Config Version Snapshots](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot) to load
the **pre-migration-snapshot** created by the tool. This reverts the staged Strata
Cloud Manager configuration but does not push changes to devices.

---

<a id="scm-migrate-from-panorama-to-strata-cloud-manager-prisma-access"></a>

#### Migrate from Panorama to Strata Cloud Manager (Prisma Access)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-prisma-access>*

Learn about the migration process for migrating your Prisma Access deployments from
Panorama to Strata Cloud Manager.

If you have an existing Prisma Access Deployment for which the configuration is
managed by Panorama and want to migrate to Strata Cloud Manager for configuration
management, Palo Alto Networks offers an in-product workflow that lets you migrate
your existing Prisma Access configuration to Strata Cloud Manager.

To enable migration workflow, you must contact your Palo
Alto Networks account team.

Managing your Prisma Access configuration using Strata Cloud Manager instead of
Panorama can offer you benefits such as:

- Continuous [best practice assessments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
- Secure default configurations
- Machine Learning (ML)-based configuration optimization
- Streamlined web security workflows
- An interactive visual summary ([Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center)) that helps you to
  assess the health, security, and efficiency of the network
- Intuitive [workflows](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows) for complex tasks
- Simple and secure [management APIs](https://pan.dev/access/api/prisma-access-config/)
- Cloud-native architecture provides scalability, resilience, and global
  reach
- No hardware to manage or software to maintain

##### Migrate to Prisma Access (Managed by Strata Cloud Manager)

To migrate Prisma Access (Managed by Panorama) to Strata Cloud Manager, see [**Migrate Prisma Access from Panorama to
Strata Cloud Manager**](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager)

---

<a id="scm-onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager"></a>

#### Onboard NGFWs, ZTP NGFWs, and VM-Series to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager>*

Procedures for onboarding NGFWs to Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) | One of these:  - [AIOps for NGFW Free](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) - [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) or [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

You can onboard your NGFW to Strata Cloud Manager to manage and gain
insights. If you already have NGFWs managed by Panorama, you can connect Strata
Cloud Manager to your Panorama using the [Panorama CloudConnector Plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) for
visibility and monitoring.

To get started managing your NGFWs with Strata Cloud Manager, follow the initial
onboarding steps below:

1. [Deploy your NGFWs and complete the
   initial setup.](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/getting-started)

   Start by integrating the firewall into your network, segmenting your
   network into zones, setting up a basic security policy, assessing
   network traffic, and reviewing the best practices.
2. [Review the prerequisites for onboarding
   your NGFWs to Strata Cloud Manager.](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)

   The prerequisites include minimum PAN-OS versions supported, supported
   NGFW models, ports, licenses, and other hard-stop requirements for using
   your NGFWs with Strata Cloud Manager.
3. [Activate your Strata Cloud Manager
   license and start associating devices to your tenant.](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager)

   If you are simply utilizing Strata Cloud Manager for the advanced
   monitoring and visibility features that will benefit your PAN-OS or
   Panorama managed firewalls, you can stop here.
4. Onboard your NGFWs to Strata Cloud Manager.
5. [Configure general settings to get
   your NGFWs up and running.](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/configure-the-firewall-general-settings.html)

   After you successfully onboard your NGFWs to Strata Cloud Manager, you have the option to configure and specify the
   general firewall management settings. The general settings include the
   following: domain name, login banner, certificates, time zones, locales,
   coordinates, and tunnel acceleration.
6. [Configure the NGFW session
   settings.](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/configure-the-firewall-session-settings.html)

   Define the general and VPN session settings, and as well the session
   timeout settings, for your firewall.
7. [Learn about how local NGFW
   configuration management works in](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/administration/onboard-devices-and-deployments/local-configuration-management.html)

   The local configuration management feature eliminates the need for
   context switching from central management to individual firewalls for
   managing local configurations.

   After you complete these steps, you can start  [managing your NGFWs with Strata
   Cloud Manager.](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access)

To onboard NGFWs using Zero Touch Provisioning (ZTP), click
[here](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws.html).

- [Onboard NGFWs](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-ngfws.html#onboard-ngfws)
- [Onboard VM-Series NGFWs](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-vm-series.html#onboard-vm-series)

#### Onboard NGFWs

Workflow for onboarding NGFWs to Strata Cloud Manager.

Learn about device labels, onboarding rules, and onboarding NGFWs to Strata Cloud
Manager.

##### Create a Device Label or Device Label Group

Device labels in Strata Cloud Manager provide a powerful and flexible
way to automate and streamline NGFW onboarding and management processes. You can
use labels to group devices based on common characteristics, enabling more
efficient configuration and software update management. This feature
enhances:

- **Zero Touch Provisioning**
  **(ZTP)** - by allowing you to assign labels during bootstrap,
  facilitating automated provisioning and near-zero touch onboarding of
  devices.
- **Standard Device Onboarding** - by enabling you to create
  label-based onboarding rules, ensuring the correct configuration is
  applied to the right NGFWs.
- **Software Updates** - by simplifying the process of
  managing multiple devices across distributed environments and being able
  to group NGFWs by software version.

By implementing device labels, you can reduce manual coordination,
minimize human errors, and accelerate remote site onboarding. To start managing
your devices using Device Labels, go to ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
Firewall or Firewall Folder, Device OnboardingDevice Labels.

###### Create a Device Label

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice Labels.
3. Add Label.
   1. Enter a descriptive Name.
   2. Select a Label Group.
   3. Save the Label.

###### Create a Device Label Group

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice LabelsManage Label Group.
3. Add Label Group.
   1. Enter a descriptive Name.
   2. Enable exposure to any combination of
      the following: ZTP, Device
      Onboarding, NGFW Software
      updates.
   3. Save the Label Group.

##### Create a Device Onboarding Rule

Use a device onboarding rule to automate parts of the Palo Alto Networks Next
Generation Firewall (NGFW) onboarding to Strata Cloud Manager whether you're
manually onboarding Palo Alto Networks NGFW or onboarding using Zero Touch
Provisioning (ZTP). This allows you to associate the firewall with a folder and
push a configuration when the firewall first connects to Strata Cloud Manager.
Device onboarding rules are designed to simplify and greatly reduce the time
spent onboarding new Palo Alto Networks NGFW at scale and ensure the correct
configuration is applied to newly onboarded Palo Alto Networks NGFW. You can
create multiple device onboarding rules to define different match criteria that
apply to different Palo Alto Networks NGFW.

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

The Match Criteria, Action,
VPN Onboarding, and User Context
Onboarding configurations are optional and can be configured as
needed. If no Match Criteria is specified then the device
onboarding rule applies to Any Palo Alto Networks NGFW
model and serial number. The Palo Alto Networks NGFW must match all
Match Criteria defined in the rule for Strata Cloud Manager to take the configured Action or
push the VPN Onboarding and User Context
Onboarding configurations.

For example, you don't configure the Match Criteria and
configure only the Target Folder in the rule
Action. Additionally, you don't configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager applies the
rule to all Palo Alto Networks NGFW onboarded to Strata Cloud Manager and only
adds them to the Target Folder. Another example is that
you specify Palo Alto Networks NGFW models and serial numbers in the
Match Criteria but you don't configure the rule
Action at all. Additionally, you configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager pushes the
VPN Onboarding and User Context
Onboarding configurations to only the Palo Alto Networks NGFW
models and serial numbers that match the Match
Criteria.

1. [Log in to](https://stratacloudmanager.paloaltonetworks.com/)
   Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
   Firewall or Firewall Folder, Device Onboarding.
3. Add Rule.
4. Configure the General device onboarding rule
   settings.
   1. The device onboarding rule is Enabled by
      default. Toggle the Enable setting to disable
      the onboarding rule after you Save.
   2. Enter a descriptive Name for the onboarding
      rule.
   3. (Optional) Enter a Description for
      the onboarding rule.
5. Define the onboarding rule Match Criteria.

   The match criteria define to which Palo Alto Networks NGFW the device
   onboarding rule applies.

   1. Specify which Palo Alto Networks NGFW
      Models.

      - Any—Applies to all Palo Alto
        Networks NGFW onboarded to Strata Cloud Manager.
      - Match—Inclusive condition that
        applies to the Palo Alto Networks NGFW models added to
        the match list. You can select one or multiple different
        Palo Alto Networks NGFW models.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies only to those
        Palo Alto Networks NGFW.
      - Exclude (Negate)—Exclusive
        condition that applies to all Palo Alto Networks NGFW
        models not added to the exclude match list.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies to all Palo
        Alto Networks NGFW models except for those added to the
        exclude list.
   2. Specify the Device S/N.

      This compliments the Models match criteria
      by allowing you to identify specific serial numbers of Palo Alto
      Networks NGFW Models that the onboarding
      rule applies to.

      - Any—Applies to all Palo Alto
        Networks NGFW serial numbers.
      - Match—Enter a regular expression
        (regex) to identify Palo Alto Networks NGFW serial
        numbers.
   3. Specify Labels applied to Palo Alto Networks
      NGFW during onboarding that the onboarding rule applies to.

      You can use And,
      Or, and Not
      operators to write a logical expression of labels to match. You
      can use parentheses (()) to group sets of
      labels and logical operators when writing your regular
      expression.

   ![]()
6. Define the onboarding rule Action.
   1. Select the Target Folder the firewall is
      added to if it matches the device onboarding rule.

      If no Target Folder is specified, then the
      firewall is added to the default All
      Firewalls folder.

      (VM-Series, funded with Software NGFW Credits) You can configure
      the dgname field in the
      init.cfg.txt bootstrap
      parameters to add the VM-Series firewall to a
      target folder. In this case, Strata Cloud Manager
      prioritizes adding the VM-Series firewall to
      the target folder configured in the
      init.cfg.txt file over the
      one configured in the device onboarding rule.
   2. For Snippet Association, apply [snippet](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/configuration-scope/snippets) configuration to
      the onboarded firewall after it successfully connects to Strata Cloud Manager.

      Snippets are a tool used to standardize a common base
      configuration for a set of firewalls or deployments. This allows
      you to quickly onboard a new firewall with a known good
      configuration and reduces the time required to onboard a new
      firewall.

      ![]()
   3. Enable VPN Onboarding if you have configured
      [Auto VPN](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html) for secure
      hub-and-spoke connectivity between Strata Cloud Manager and your
      managed firewalls.

      If enabled, select the VPN Cluster to add
      the firewall to. This determines the gateway devices and
      automatically creates secure connections between the configured
      gateway and the newly onboarded firewall.

      Click Configure to [configure the Palo Alto
      Networks NGFW as a hub or branch firewall.](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html)

      ![]()
   4. Enable User Context Onboarding to configure
      the user and tag mappings required for [User Context for Cloud Identity
      Engine (CIE)](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context).

      User Context provides simplified granular control over the data
      that is shared across your security devices. It provides your
      administrators the flexibility to specify the data types each
      device sends and receives.

      If enabled, you must configure the Segments to
      Contribute Data To to customize the segment
      mappings the firewall sends to CIE and the Segments
      to Receive Data From to customize how CIE
      provides segment mappings to the firewall.

      ![]()
7. Save.
8. In Device Onboarding, review your newly configured
   onboarding rule and verify it's Enabled.

   Device onboarding rules are processed in a top-down priority. Strata Cloud Manager evaluates each onboarding rule Match
   Criteria starting with the rule highest in the rule
   hierarchy until the Palo Alto Networks NGFW meets all Match
   Criteria. Strata Cloud Manager then takes the
   Action specified in the matching rule. In the
   event two rules in the device onboarding rule hierarchy apply to the
   same firewall, Strata Cloud Manager takes the
   Action configured in the device onboarding
   rule higher up in the rule hierarchy.
9. Onboard your Palo Alto Networks NGFW manually or using ZTP.

##### Onboard a NGFW to Strata Cloud Manager

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

After you activate Strata Cloud Manager, you can begin to onboard Palo Alto
Networks firewalls to it. Onboarding to Strata Cloud Manager is supported for
firewalls running PAN-OS 10.2.3 and later releases.

Strata Cloud Manager is available, featuring [two licensing tiers: Strata Cloud Manager
Essentials and Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support). This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service.

If you were using Strata Cloud Manager before the introduction of these new
licensing tiers, your existing license for AIOps for NGFW Premium remains
supported. You can continue to amend, extend, renew, or activate without any
changes.

There are four components involved in firewall onboarding:

- The [tenant](#) — Created when you activate a product license on
  your Customer Support Portal (CSP) account. You add firewalls to your
  tenant to associate them with Strata Cloud Manager.
- The firewall — The Palo Alto Networks firewall that you intend to use
  with Strata Cloud Manager.

  You can only onboard a firewall not already associated with Strata Logging Service. If a firewall is already associated
  with Strata Logging Service, it’s ineligible for Strata Cloud Manager and isn't displayed.
- AIOps for NGFW Premium, Strata Cloud Manager Essentials, or Strata Cloud Manager Pro— One of the licenses required for cloud
  management of firewalls.
- Strata Cloud Manager — The app you will be associating with the firewall
  to manage its configuration from the cloud.

1. Review the [prerequisites to onboard your
   NGFW to](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)Strata Cloud Manager.
2. [Activate](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/activate-cortex-data-lake-toc/activate-cortex-data-lake-easy) the Strata Logging Service license.

   Skip this step if you already activated the Prisma Access (Managed by Strata Cloud Manager) license
   on the same tenant you are activating AIOps for NGFW Premium
   license.
3. Activate Strata Cloud Manager.

   - [Activate Strata Cloud Manager
     Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html): The free tier that offers configuration
     management, network security lifecycle management, and can also
     provide visibility if you have a paid license of [Strata Logging
     Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/license-overview).
   - [Activate Strata Cloud Manager
     Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html): This tier provides advanced features plus all the
     Strata Cloud Manager Essentials features. When you activate Strata
     Cloud Manager Pro, it also includes access to the Strata Logging
     Service, which comes with one year of log retention and unlimited
     storage.

   If you were using Strata Cloud Manager before the introduction of these
   new licensing tiers, your existing AIOps for NGFW Premium license
   remains supported. You need to [activate Strata Cloud Manager](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-premium-activation)
   using the AIOps for NGFW Premium license.

   Skip this step if you already activated Strata Cloud Manager.
4. (Optional) [Activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine
   license.

   Activate Cloud Identity Engine (CIE) if you plan to use user-based
   authentication policy rules. CIE activation is not required for initial
   onboarding and can be activated at a later time as needed.
5. Register the firewall with the Palo Alto Networks Customer Support Portal
   (CSP) and activate licenses.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and find the Serial
      # under the General Information widget in the
      Dashboard.
   2. [Register the firewall](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/getting-started/register-the-firewall).
   3. [Activate the Support
      license](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/subscriptions/activate-subscription-licenses) on the firewall.
6. [Install the device certificate](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/certificate-management/obtain-certificates/device-certificate) on
   the firewall.

   This is required to successfully authenticate the firewall with the Palo
   Alto Networks CSP and use Strata Cloud Manager.
7. Configure the firewall Panorama Settings required to connect to Strata Cloud Manager.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface).
   2. Configure the firewall DNS and NTP servers.

      This is required to successfully connect the firewall to Strata Cloud Manager and install software and content
      updates.

      1. Select DeviceSetupServices and edit the Services.
      2. Select Servers and configure the
         Primary DNS Server and
         Secondary DNS Server.
      3. Select NTP and configure the
         Primary and Secondary NTP Server
         Address.
      4. Click OK.
   3. Configure the Panorama Settings.

      1. Select DeviceSetupManagement and edit the Panorama Settings.
      2. Select Managed By Cloud
         Service.
      3. (NGFW (Managed by Strata Cloud Manager) Running PAN-OS 11.2
         and later) Select the
         Port used for connectivity
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **Default**—The [default TCP port
           3978](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama). This port is dedicated for
           communication between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **443**—TCP port 443 is the standard port
           used for HTTP traffic encrypted with SSL. Using
           port 443 for NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager communication greatly simplifies
           network configuration management for both
           administrators and end users.

           Additionally, using port 443 reduces your
           network attack surface by reducing the number of
           open ports on your network.
      4. (Optional for (NGFW (Managed by Strata Cloud Manager)
         Running PAN-OS 11.2 and later) Check
         Enable Compress Config to
         compress the size of the configuration file exchanged
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager, and vice versa, to increase file
         transfer times.

         Enabling this setting does not cause load or delay in
         firewall processing or increase commit operation
         times.
      5. Click OK.

      ![]()
   4. Commit.
8. (Optional) Create a Device Onboarding Rule to associate the
   firewall with a folder and push a configuration when the firewall first
   connects to Strata Cloud Manager.
9. [Associate a firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) with your
   Palo Alto Networks Customer Support Portal (CSP) account.
   1. Log in to Strata Cloud Manager.
   2. In the bottom-left corner of the window, select the icon for your
      tenant and select System SettingsDevice Associations.

      ![]()
   3. Add Devices.
   4. Select one or more firewalls you want to onboard with your CSP
      account.

      You can use the firewall serial number you gathered in the
      previous step to search for a specific firewall.
   5. Save.
10. (Optional) If you are activating AIOps for NGFW Premium license or
    Strata Cloud Manager Pro, you need to [associate the firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with Strata Cloud Manager.
    1. In Device Associations, select the firewall you added and
       Associate Products.
    2. For the Licensed Products, select Strata Cloud
       Manager or AIOps for
       NGFW.
    3. From the Select Firewall Model, License Type, and
       Term drop-down, select the firewall and support
       license to apply to the firewall.

       The model for the firewall license must match the firewall model
       you are onboarding to Strata Cloud Manager.
    4. Apply Licenses.

       ![]()
    5. In the Device Associations page, verify the Associated Products for
       the onboarded firewall display AIOps for
       NGFW and Strata Logging Service.
11. Add the available device to Strata Cloud Manager.
    1. Select System SettingsDevice ManagementAvailable Devices.
    2. In the Available Devices select the
       firewall you just added.
    3. Move to Cloud Management.

       You are prompted to confirm the number of selected firewalls.
       Click Move to Cloud Management to
       continue.

       ![]()
    4. (Optional) Apply Labels to the
       onboarded firewall.

       You can select an existing label or create a new label by typing
       the label you want to create.

       Click Move to Cloud to continue adding the
       firewall to Strata Cloud Manager.

       ![]()
    5. Confirm that the selected firewall is now listed in the list of
       Cloud Managed Devices and that the
       Onboarding Status shows
       Success.
12. Verify that the firewall successfully onboarded to Strata Cloud Manager.

    Two configuration pushes occur by default to the firewall after
    successful onboarding to Strata Cloud Manager. The first push from
    Strata Cloud Manager automatically enables the Advanced Routing
    Engine and restarts the firewall. The second pushes the
    configuration from Strata Cloud Manager to the firewall.

    If the Advanced Routing Engine is not automatically enabled as part
    of the onboarding process to Strata Cloud Manager, you need to
    manually [enable Advanced Routing](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/networking/advanced-routing/enable-advanced-routing.html) on
    the firewall.

    1. Select System SettingsDevice ManagementCloud Managed Devices.

       You should see the serial number for the firewall that you just
       added, but you won’t see any additional device information for
       it yet.
    2. [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli)
       and verify the firewall successfully connected to Strata Cloud Manager.

       After you connect the firewall to Strata Cloud Manager, it’s
       automatically converted to logical router mode, restarted, and
       Strata Cloud Manager pushes the default configuration to
       the firewall.

       For this to work, make sure:

       - You’ve installed the device certificate on the
         firewall.
       - The firewall meets the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html) for Strata Cloud Manager.
       - You’ve resolved variables. If variables aren’t
         resolved, Strata Cloud Manager will fail to push
         the default configuration to the firewall.

       ```
       admin> show cloud-management-status
       ```

       ![]()

       Verify the firewall successfully connected to a Strata Cloud Manager
       Endpoint and that the
       Connected status displays
       Yes.

       Once the firewall is Connected, the
       firewall automatically converts to logical router mode and
       restarts, and Strata Cloud Manager pushes the default
       configuration to the firewall.
    3. Return to [Strata Cloud Manager](https://sase.paloaltonetworks.com/) and
       select System SettingsDevice ManagementCloud Managed Devices and verify that the details for the firewall appear,
       such as serial number, model, type, and IP address.

       By default, newly onboarded firewalls are added to the
       All Firewalls folder.
13. Create and associate your firewall with a [folder](https://docs.paloaltonetworks.com/cloud-management/administration/workflows/workflows-ngfw-setup/folder-management).

    Folders are used to logically group your firewalls for simplified
    configuration management. Skip this step if you created a device
    onboarding rule to automatically move the firewall to a target folder.

    (HA only) Both firewalls must be in the same folder to
    configure HA. If you need to configure your firewalls in a [high availability](https://docs.paloaltonetworks.com/ngfw/administration/high-availability) (HA)
    configuration, be sure to plan your folder structure accordingly and
    move both firewalls to the same folder before you configure HA.

    Additionally, firewalls in an HA configuration can't be moved to a
    new folder. To move them, you must first break the HA configuration,
    move both firewalls to the new folder, and then reconfigure HA.

    1. Select System SettingsFolder Management and Add Folder to create a new
       folder.
    2. Locate the newly added firewall that is associated with the
       All Firewalls by default.
    3. In the Action column, Move the firewall to
       the folder you created.
14. (Optional) Modify the displayed firewall name.

    By default, firewalls onboarded to Strata Cloud Manager display the
    firewall serial number as the displayed firewall name throughout Strata Cloud Manager. Rename the displayed firewall from the serial
    number to a more user-friendly name to make it easier to identify.

    1. Select System SettingsFolder Management and locate the firewall you onboarded.
    2. In the Actions column, expand the Actions menu and
       Edit.
    3. Enter a new Display Name for the
       firewall.
    4. Save.
15. Review the predefined interface and logical router configurations.

    The predefined interfaces and logical router configuration are required
    to successfully push configuration changes to managed firewalls after
    they’re successfully added to Strata Cloud Manager.

    - **$eth-internet (eth1/3)**—Ethernet interface for outbound
      internet connections. Associated with the default logical router
      configuration.
    - **$eth-local (eth1/4)**—Ethernet interface for local network
      connections. Associated with the default router
      configuration.

    The predefined interface and logical router configuration are associated
    with the default All Firewalls folder and
    are inherited by all other folders you create. You might reassign the
    $eth-internet and
    $eth-local interfaces for a newly
    created folder or for the individual firewall as needed.

    1. Select ConfigurationDevice SettingsInterfacesEthernet and verify that
       $eth-internet and
       $eth-local are displayed.

       To reassign the interface, click the interface name to select
       a new Default Interface Assignment
       and Save.

       ![]()
    2. Select ConfigurationDevice SettingsRoutingRouters and verify the default
       logical router is displayed.

       ![]()
16. Push Config to push your configuration
    changes.
17. Select ConfigurationPush Status and to verify that your configuration push was successful.
18. Finally, check the [Strata Cloud Manager Command
    Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) and confirm that your firewall appears in the
    Summary view.

##### Offboard NGFWs or VM-Series

To remove a physical or VM-Series NGFW that is managed by Strata Cloud
Manager:

1. Log in to Strata Cloud Manager.
2. Navigate to **System Settings** > **Device Management** >
   **Available Devices**.
3. Select the option **Back to Available Devices** to move the firewall
   out of Strata Cloud Manager.

You can [remove device associations](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager#device-associations-remove-associations) if, for
example, you are retiring or returning a firewall or Panorama appliance, or if
you want to associate it with another [tenant service group (TSG)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant).

#### Onboard VM-Series

Information for onboarding VM-Series NGFWs to Strata Cloud Manager.

To onboard VM-series funded by software NGFW credits, see
[Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

---

<a id="scm-onboard-ngfws"></a>

##### Onboard NGFWs

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-ngfws>*

Workflow for onboarding NGFWs to Strata Cloud Manager.

Learn about device labels, onboarding rules, and onboarding NGFWs to Strata Cloud
Manager.

###### Create a Device Label or Device Label Group

Device labels in Strata Cloud Manager provide a powerful and flexible
way to automate and streamline NGFW onboarding and management processes. You can
use labels to group devices based on common characteristics, enabling more
efficient configuration and software update management. This feature
enhances:

- **Zero Touch Provisioning**
  **(ZTP)** - by allowing you to assign labels during bootstrap,
  facilitating automated provisioning and near-zero touch onboarding of
  devices.
- **Standard Device Onboarding** - by enabling you to create
  label-based onboarding rules, ensuring the correct configuration is
  applied to the right NGFWs.
- **Software Updates** - by simplifying the process of
  managing multiple devices across distributed environments and being able
  to group NGFWs by software version.

By implementing device labels, you can reduce manual coordination,
minimize human errors, and accelerate remote site onboarding. To start managing
your devices using Device Labels, go to ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
Firewall or Firewall Folder, Device OnboardingDevice Labels.

###### Create a Device Label

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice Labels.
3. Add Label.
   1. Enter a descriptive Name.
   2. Select a Label Group.
   3. Save the Label.

###### Create a Device Label Group

1. Log in to Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to
   the Firewall or Firewall Folder, Device OnboardingDevice LabelsManage Label Group.
3. Add Label Group.
   1. Enter a descriptive Name.
   2. Enable exposure to any combination of
      the following: ZTP, Device
      Onboarding, NGFW Software
      updates.
   3. Save the Label Group.

###### Create a Device Onboarding Rule

Use a device onboarding rule to automate parts of the Palo Alto Networks Next
Generation Firewall (NGFW) onboarding to Strata Cloud Manager whether you're
manually onboarding Palo Alto Networks NGFW or onboarding using Zero Touch
Provisioning (ZTP). This allows you to associate the firewall with a folder and
push a configuration when the firewall first connects to Strata Cloud Manager.
Device onboarding rules are designed to simplify and greatly reduce the time
spent onboarding new Palo Alto Networks NGFW at scale and ensure the correct
configuration is applied to newly onboarded Palo Alto Networks NGFW. You can
create multiple device onboarding rules to define different match criteria that
apply to different Palo Alto Networks NGFW.

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

The Match Criteria, Action,
VPN Onboarding, and User Context
Onboarding configurations are optional and can be configured as
needed. If no Match Criteria is specified then the device
onboarding rule applies to Any Palo Alto Networks NGFW
model and serial number. The Palo Alto Networks NGFW must match all
Match Criteria defined in the rule for Strata Cloud Manager to take the configured Action or
push the VPN Onboarding and User Context
Onboarding configurations.

For example, you don't configure the Match Criteria and
configure only the Target Folder in the rule
Action. Additionally, you don't configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager applies the
rule to all Palo Alto Networks NGFW onboarded to Strata Cloud Manager and only
adds them to the Target Folder. Another example is that
you specify Palo Alto Networks NGFW models and serial numbers in the
Match Criteria but you don't configure the rule
Action at all. Additionally, you configure
VPN Onboarding and User Context
Onboarding. In this example Strata Cloud Manager pushes the
VPN Onboarding and User Context
Onboarding configurations to only the Palo Alto Networks NGFW
models and serial numbers that match the Match
Criteria.

1. [Log in to](https://stratacloudmanager.paloaltonetworks.com/)
   Strata Cloud Manager.
2. Select ConfigurationNGFW and Prisma AccessSetup, set the Configuration Scope to the
   Firewall or Firewall Folder, Device Onboarding.
3. Add Rule.
4. Configure the General device onboarding rule
   settings.
   1. The device onboarding rule is Enabled by
      default. Toggle the Enable setting to disable
      the onboarding rule after you Save.
   2. Enter a descriptive Name for the onboarding
      rule.
   3. (Optional) Enter a Description for
      the onboarding rule.
5. Define the onboarding rule Match Criteria.

   The match criteria define to which Palo Alto Networks NGFW the device
   onboarding rule applies.

   1. Specify which Palo Alto Networks NGFW
      Models.

      - Any—Applies to all Palo Alto
        Networks NGFW onboarded to Strata Cloud Manager.
      - Match—Inclusive condition that
        applies to the Palo Alto Networks NGFW models added to
        the match list. You can select one or multiple different
        Palo Alto Networks NGFW models.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies only to those
        Palo Alto Networks NGFW.
      - Exclude (Negate)—Exclusive
        condition that applies to all Palo Alto Networks NGFW
        models not added to the exclude match list.

        For example, if you add PA-1410
        and PA-3260, then the onboarding
        rule Action applies to all Palo
        Alto Networks NGFW models except for those added to the
        exclude list.
   2. Specify the Device S/N.

      This compliments the Models match criteria
      by allowing you to identify specific serial numbers of Palo Alto
      Networks NGFW Models that the onboarding
      rule applies to.

      - Any—Applies to all Palo Alto
        Networks NGFW serial numbers.
      - Match—Enter a regular expression
        (regex) to identify Palo Alto Networks NGFW serial
        numbers.
   3. Specify Labels applied to Palo Alto Networks
      NGFW during onboarding that the onboarding rule applies to.

      You can use And,
      Or, and Not
      operators to write a logical expression of labels to match. You
      can use parentheses (()) to group sets of
      labels and logical operators when writing your regular
      expression.

   ![]()
6. Define the onboarding rule Action.
   1. Select the Target Folder the firewall is
      added to if it matches the device onboarding rule.

      If no Target Folder is specified, then the
      firewall is added to the default All
      Firewalls folder.

      (VM-Series, funded with Software NGFW Credits) You can configure
      the dgname field in the
      init.cfg.txt bootstrap
      parameters to add the VM-Series firewall to a
      target folder. In this case, Strata Cloud Manager
      prioritizes adding the VM-Series firewall to
      the target folder configured in the
      init.cfg.txt file over the
      one configured in the device onboarding rule.
   2. For Snippet Association, apply [snippet](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/configuration-scope/snippets) configuration to
      the onboarded firewall after it successfully connects to Strata Cloud Manager.

      Snippets are a tool used to standardize a common base
      configuration for a set of firewalls or deployments. This allows
      you to quickly onboard a new firewall with a known good
      configuration and reduces the time required to onboard a new
      firewall.

      ![]()
   3. Enable VPN Onboarding if you have configured
      [Auto VPN](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html) for secure
      hub-and-spoke connectivity between Strata Cloud Manager and your
      managed firewalls.

      If enabled, select the VPN Cluster to add
      the firewall to. This determines the gateway devices and
      automatically creates secure connections between the configured
      gateway and the newly onboarded firewall.

      Click Configure to [configure the Palo Alto
      Networks NGFW as a hub or branch firewall.](http://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn.html)

      ![]()
   4. Enable User Context Onboarding to configure
      the user and tag mappings required for [User Context for Cloud Identity
      Engine (CIE)](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context).

      User Context provides simplified granular control over the data
      that is shared across your security devices. It provides your
      administrators the flexibility to specify the data types each
      device sends and receives.

      If enabled, you must configure the Segments to
      Contribute Data To to customize the segment
      mappings the firewall sends to CIE and the Segments
      to Receive Data From to customize how CIE
      provides segment mappings to the firewall.

      ![]()
7. Save.
8. In Device Onboarding, review your newly configured
   onboarding rule and verify it's Enabled.

   Device onboarding rules are processed in a top-down priority. Strata Cloud Manager evaluates each onboarding rule Match
   Criteria starting with the rule highest in the rule
   hierarchy until the Palo Alto Networks NGFW meets all Match
   Criteria. Strata Cloud Manager then takes the
   Action specified in the matching rule. In the
   event two rules in the device onboarding rule hierarchy apply to the
   same firewall, Strata Cloud Manager takes the
   Action configured in the device onboarding
   rule higher up in the rule hierarchy.
9. Onboard your Palo Alto Networks NGFW manually or using ZTP.

###### Onboard a NGFW to Strata Cloud Manager

To onboard VM-series funded by software NGFW credits,
see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

After you activate Strata Cloud Manager, you can begin to onboard Palo Alto
Networks firewalls to it. Onboarding to Strata Cloud Manager is supported for
firewalls running PAN-OS 10.2.3 and later releases.

Strata Cloud Manager is available, featuring [two licensing tiers: Strata Cloud Manager
Essentials and Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support). This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service.

If you were using Strata Cloud Manager before the introduction of these new
licensing tiers, your existing license for AIOps for NGFW Premium remains
supported. You can continue to amend, extend, renew, or activate without any
changes.

There are four components involved in firewall onboarding:

- The [tenant](#) — Created when you activate a product license on
  your Customer Support Portal (CSP) account. You add firewalls to your
  tenant to associate them with Strata Cloud Manager.
- The firewall — The Palo Alto Networks firewall that you intend to use
  with Strata Cloud Manager.

  You can only onboard a firewall not already associated with Strata Logging Service. If a firewall is already associated
  with Strata Logging Service, it’s ineligible for Strata Cloud Manager and isn't displayed.
- AIOps for NGFW Premium, Strata Cloud Manager Essentials, or Strata Cloud Manager Pro— One of the licenses required for cloud
  management of firewalls.
- Strata Cloud Manager — The app you will be associating with the firewall
  to manage its configuration from the cloud.

1. Review the [prerequisites to onboard your
   NGFW to](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)Strata Cloud Manager.
2. [Activate](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/activate-cortex-data-lake-toc/activate-cortex-data-lake-easy) the Strata Logging Service license.

   Skip this step if you already activated the Prisma Access (Managed by Strata Cloud Manager) license
   on the same tenant you are activating AIOps for NGFW Premium
   license.
3. Activate Strata Cloud Manager.

   - [Activate Strata Cloud Manager
     Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html): The free tier that offers configuration
     management, network security lifecycle management, and can also
     provide visibility if you have a paid license of [Strata Logging
     Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/license-overview).
   - [Activate Strata Cloud Manager
     Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html): This tier provides advanced features plus all the
     Strata Cloud Manager Essentials features. When you activate Strata
     Cloud Manager Pro, it also includes access to the Strata Logging
     Service, which comes with one year of log retention and unlimited
     storage.

   If you were using Strata Cloud Manager before the introduction of these
   new licensing tiers, your existing AIOps for NGFW Premium license
   remains supported. You need to [activate Strata Cloud Manager](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-premium-activation)
   using the AIOps for NGFW Premium license.

   Skip this step if you already activated Strata Cloud Manager.
4. (Optional) [Activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine
   license.

   Activate Cloud Identity Engine (CIE) if you plan to use user-based
   authentication policy rules. CIE activation is not required for initial
   onboarding and can be activated at a later time as needed.
5. Register the firewall with the Palo Alto Networks Customer Support Portal
   (CSP) and activate licenses.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and find the Serial
      # under the General Information widget in the
      Dashboard.
   2. [Register the firewall](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/getting-started/register-the-firewall).
   3. [Activate the Support
      license](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/subscriptions/activate-subscription-licenses) on the firewall.
6. [Install the device certificate](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/certificate-management/obtain-certificates/device-certificate) on
   the firewall.

   This is required to successfully authenticate the firewall with the Palo
   Alto Networks CSP and use Strata Cloud Manager.
7. Configure the firewall Panorama Settings required to connect to Strata Cloud Manager.
   1. [Log in to the firewall web
      interface](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface).
   2. Configure the firewall DNS and NTP servers.

      This is required to successfully connect the firewall to Strata Cloud Manager and install software and content
      updates.

      1. Select DeviceSetupServices and edit the Services.
      2. Select Servers and configure the
         Primary DNS Server and
         Secondary DNS Server.
      3. Select NTP and configure the
         Primary and Secondary NTP Server
         Address.
      4. Click OK.
   3. Configure the Panorama Settings.

      1. Select DeviceSetupManagement and edit the Panorama Settings.
      2. Select Managed By Cloud
         Service.
      3. (NGFW (Managed by Strata Cloud Manager) Running PAN-OS 11.2
         and later) Select the
         Port used for connectivity
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **Default**—The [default TCP port
           3978](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama). This port is dedicated for
           communication between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager.
         - **443**—TCP port 443 is the standard port
           used for HTTP traffic encrypted with SSL. Using
           port 443 for NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager communication greatly simplifies
           network configuration management for both
           administrators and end users.

           Additionally, using port 443 reduces your
           network attack surface by reducing the number of
           open ports on your network.
      4. (Optional for (NGFW (Managed by Strata Cloud Manager)
         Running PAN-OS 11.2 and later) Check
         Enable Compress Config to
         compress the size of the configuration file exchanged
         between the NGFW (Managed by Strata Cloud Manager) and Strata Cloud Manager, and vice versa, to increase file
         transfer times.

         Enabling this setting does not cause load or delay in
         firewall processing or increase commit operation
         times.
      5. Click OK.

      ![]()
   4. Commit.
8. (Optional) Create a Device Onboarding Rule to associate the
   firewall with a folder and push a configuration when the firewall first
   connects to Strata Cloud Manager.
9. [Associate a firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) with your
   Palo Alto Networks Customer Support Portal (CSP) account.
   1. Log in to Strata Cloud Manager.
   2. In the bottom-left corner of the window, select the icon for your
      tenant and select System SettingsDevice Associations.

      ![]()
   3. Add Devices.
   4. Select one or more firewalls you want to onboard with your CSP
      account.

      You can use the firewall serial number you gathered in the
      previous step to search for a specific firewall.
   5. Save.
10. (Optional) If you are activating AIOps for NGFW Premium license or
    Strata Cloud Manager Pro, you need to [associate the firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with Strata Cloud Manager.
    1. In Device Associations, select the firewall you added and
       Associate Products.
    2. For the Licensed Products, select Strata Cloud
       Manager or AIOps for
       NGFW.
    3. From the Select Firewall Model, License Type, and
       Term drop-down, select the firewall and support
       license to apply to the firewall.

       The model for the firewall license must match the firewall model
       you are onboarding to Strata Cloud Manager.
    4. Apply Licenses.

       ![]()
    5. In the Device Associations page, verify the Associated Products for
       the onboarded firewall display AIOps for
       NGFW and Strata Logging Service.
11. Add the available device to Strata Cloud Manager.
    1. Select System SettingsDevice ManagementAvailable Devices.
    2. In the Available Devices select the
       firewall you just added.
    3. Move to Cloud Management.

       You are prompted to confirm the number of selected firewalls.
       Click Move to Cloud Management to
       continue.

       ![]()
    4. (Optional) Apply Labels to the
       onboarded firewall.

       You can select an existing label or create a new label by typing
       the label you want to create.

       Click Move to Cloud to continue adding the
       firewall to Strata Cloud Manager.

       ![]()
    5. Confirm that the selected firewall is now listed in the list of
       Cloud Managed Devices and that the
       Onboarding Status shows
       Success.
12. Verify that the firewall successfully onboarded to Strata Cloud Manager.

    Two configuration pushes occur by default to the firewall after
    successful onboarding to Strata Cloud Manager. The first push from
    Strata Cloud Manager automatically enables the Advanced Routing
    Engine and restarts the firewall. The second pushes the
    configuration from Strata Cloud Manager to the firewall.

    If the Advanced Routing Engine is not automatically enabled as part
    of the onboarding process to Strata Cloud Manager, you need to
    manually [enable Advanced Routing](https://docs.paloaltonetworks.com/content/techdocs/en_US/ngfw/networking/advanced-routing/enable-advanced-routing.html) on
    the firewall.

    1. Select System SettingsDevice ManagementCloud Managed Devices.

       You should see the serial number for the firewall that you just
       added, but you won’t see any additional device information for
       it yet.
    2. [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli)
       and verify the firewall successfully connected to Strata Cloud Manager.

       After you connect the firewall to Strata Cloud Manager, it’s
       automatically converted to logical router mode, restarted, and
       Strata Cloud Manager pushes the default configuration to
       the firewall.

       For this to work, make sure:

       - You’ve installed the device certificate on the
         firewall.
       - The firewall meets the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html) for Strata Cloud Manager.
       - You’ve resolved variables. If variables aren’t
         resolved, Strata Cloud Manager will fail to push
         the default configuration to the firewall.

       ```
       admin> show cloud-management-status
       ```

       ![]()

       Verify the firewall successfully connected to a Strata Cloud Manager
       Endpoint and that the
       Connected status displays
       Yes.

       Once the firewall is Connected, the
       firewall automatically converts to logical router mode and
       restarts, and Strata Cloud Manager pushes the default
       configuration to the firewall.
    3. Return to [Strata Cloud Manager](https://sase.paloaltonetworks.com/) and
       select System SettingsDevice ManagementCloud Managed Devices and verify that the details for the firewall appear,
       such as serial number, model, type, and IP address.

       By default, newly onboarded firewalls are added to the
       All Firewalls folder.
13. Create and associate your firewall with a [folder](https://docs.paloaltonetworks.com/cloud-management/administration/workflows/workflows-ngfw-setup/folder-management).

    Folders are used to logically group your firewalls for simplified
    configuration management. Skip this step if you created a device
    onboarding rule to automatically move the firewall to a target folder.

    (HA only) Both firewalls must be in the same folder to
    configure HA. If you need to configure your firewalls in a [high availability](https://docs.paloaltonetworks.com/ngfw/administration/high-availability) (HA)
    configuration, be sure to plan your folder structure accordingly and
    move both firewalls to the same folder before you configure HA.

    Additionally, firewalls in an HA configuration can't be moved to a
    new folder. To move them, you must first break the HA configuration,
    move both firewalls to the new folder, and then reconfigure HA.

    1. Select System SettingsFolder Management and Add Folder to create a new
       folder.
    2. Locate the newly added firewall that is associated with the
       All Firewalls by default.
    3. In the Action column, Move the firewall to
       the folder you created.
14. (Optional) Modify the displayed firewall name.

    By default, firewalls onboarded to Strata Cloud Manager display the
    firewall serial number as the displayed firewall name throughout Strata Cloud Manager. Rename the displayed firewall from the serial
    number to a more user-friendly name to make it easier to identify.

    1. Select System SettingsFolder Management and locate the firewall you onboarded.
    2. In the Actions column, expand the Actions menu and
       Edit.
    3. Enter a new Display Name for the
       firewall.
    4. Save.
15. Review the predefined interface and logical router configurations.

    The predefined interfaces and logical router configuration are required
    to successfully push configuration changes to managed firewalls after
    they’re successfully added to Strata Cloud Manager.

    - **$eth-internet (eth1/3)**—Ethernet interface for outbound
      internet connections. Associated with the default logical router
      configuration.
    - **$eth-local (eth1/4)**—Ethernet interface for local network
      connections. Associated with the default router
      configuration.

    The predefined interface and logical router configuration are associated
    with the default All Firewalls folder and
    are inherited by all other folders you create. You might reassign the
    $eth-internet and
    $eth-local interfaces for a newly
    created folder or for the individual firewall as needed.

    1. Select ConfigurationDevice SettingsInterfacesEthernet and verify that
       $eth-internet and
       $eth-local are displayed.

       To reassign the interface, click the interface name to select
       a new Default Interface Assignment
       and Save.

       ![]()
    2. Select ConfigurationDevice SettingsRoutingRouters and verify the default
       logical router is displayed.

       ![]()
16. Push Config to push your configuration
    changes.
17. Select ConfigurationPush Status and to verify that your configuration push was successful.
18. Finally, check the [Strata Cloud Manager Command
    Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) and confirm that your firewall appears in the
    Summary view.

###### Offboard NGFWs or VM-Series

To remove a physical or VM-Series NGFW that is managed by Strata Cloud
Manager:

1. Log in to Strata Cloud Manager.
2. Navigate to **System Settings** > **Device Management** >
   **Available Devices**.
3. Select the option **Back to Available Devices** to move the firewall
   out of Strata Cloud Manager.

You can [remove device associations](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager#device-associations-remove-associations) if, for
example, you are retiring or returning a firewall or Panorama appliance, or if
you want to associate it with another [tenant service group (TSG)](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant).

---

<a id="scm-onboard-vm-series"></a>

##### Onboard VM-Series

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-ztp-ngfws-and-vm-series-to-strata-cloud-manager/onboard-vm-series>*

Information for onboarding VM-Series NGFWs to Strata Cloud Manager.

To onboard VM-series funded by software NGFW credits, see
[Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

---

<a id="scm-onboard-prisma-access-to-strata-cloud-manager"></a>

#### Onboard Prisma Access to Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-prisma-access-to-strata-cloud-manager>*

Learn about how to onboard Prisma Access to Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access | One of these:  - [Prisma Access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation) - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html) |

Strata Cloud Manager provides comprehensive visibility and insights into all Prisma
Access deployments, whether managed by Strata Cloud Manager or Panorama. Additionally,
you have the option to use Strata Cloud Manager as the management interface for Prisma
Access if needed.

During Prisma Access activation, you can choose either Strata Cloud Manager or Panorama
as the management interface. If Panorama currently manages your Prisma Access
deployment, you can migrate the configuration to Strata Cloud Manager for management.
However, after migrating, you cannot switch back to Panorama.

##### Onboard Prisma Access for Visibility

Before you begin, confirm that your Prisma Access deployment meets the [prerequisites](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-prisma-access.html) for visibility and monitoring
in Strata Cloud Manager.

To use Strata Cloud Manager for visibility and monitoring, you just need to log into
Strata Cloud manager and choose the appropriate Prisma Access tenant. Once you
select the correct tenant, you can see Prisma Access data in Command Center,
Dashboards and Activity Insights.

1. **Access Strata Cloud Manager** - You can access Strata Cloud Manager from
   the
   [Activation Console](https://apps.paloaltonetworks.com/hub), or
   you can access it directly at [stratacloudmanager.paloaltonetworks.com](http://stratacloudmanager.paloaltonetworks.com).
2. **Verify or switch tenant** - Go to the bottom of the navigation menu and
   check your tenant details. If the tenant name is incorrect, use the search
   option to find and switch to the correct tenant.

##### Onboard Prisma Access for Configuration Management

- **New Prisma Access Deployment**  - If you have chosen Strata Cloud
  Manager as the management interface during Prisma Access activation, you
  need to begin by [configuring your Prisma Access
  features](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access) in Strata Cloud Manager after activation.
- **Migration from Panorama** - If your Prisma Access deployment is managed
  by Panorama, you can migrate the configuration from Panorama to Strata Clod
  Manager. Once you migrate to Strata Cloud Manager, you cannot switch back to
  Panorama.

  Before you migrate Prisma Access to Strata Cloud Manager,
  review the [prerequisites](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-bcj_p2w_zbc#task-bcj_p2w_zbc) to confirm that
  your existing deployment meets all necessary requirements.

  Palo
  Alto Networks offers an **in-product workflow** to [migrate](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-j3r_p2w_zbc#task-j3r_p2w_zbc) your existing Prisma
  Access Deployment managed by Panorama to Strata Cloud Manager.

---

<a id="scm-visibility"></a>

#### Visibility

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager/opeartionalize-visibility>*

Learn how to access the Strata Cloud Manager's visibility features after
onboarding.

Here’s a list of pages you can check out to make the most of Strata Cloud Manager’s
visibility features such as, [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards?otp=task_yvz_cqt_fyb#task_yvz_cqt_fyb) and [Activity Insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights) based on your use case and
product.

Some pages listed in the table will contain data only if Strata Logging Service is
configured.

|

Products | Visibility Features | Navigation |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**NGFW** | [Device Health](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/device-health) | Insights OPERATIONALNetsec Health |

|

[Security Posture of NGFW devices](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/security-posture-insights) | InsightsPOSTURESecurity Posture Insights |

|

[Health and Status of ZTNA Connectors](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-data-centers) | ConfigurationZTNA Connector |

|

[Color-coded representation of the devices in your deployment](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/ngfw-devices) | Insights OPERATIONALNetsec Health |

|

[Inventory of devices on your network](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-assets) | InsightsSecurityDevice Security |

|

**Prisma Access** | [Health of all your Prisma Access locations](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-prisma-access-locations) | InsightsPrisma SASEPrisma Access Locations |

|

[Health and performance of your Prisma Access environment](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/prisma-access-usage) | InsightsPrisma SASEPrisma Access Usage |

|

[Health and Conectivity of Remote Networks](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-branch-sites) | InsightsPrisma SASEBranch Sites |

|

[Health and Status of Service Connections](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/monitor-data-centers) | InsightsPrisma SASEData CentersService Connections |

|

[Application Experience](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/application-experience) | InsightsApplication Experience |

|

**Common for NGFW and Prisma Access** | [Comprehensive Visibility into your Deployments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center#strata-command-center-threats) | Command center |

|

[Incidents](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts/incidents-and-alerts-prisma-access) | IncidentsNGFW / Prisma Access |

|

[DNS Security data across your NGFW and Prisma Access Deployments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/dns-security) | InsightsActivity InsightsDomains |

|

[Security Posture or Best Practice Adoption](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/best-practices) | InsightsPOSTUREBest Practices |

|

[Threats in your network](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-threats) | InsightsActivity InsightsThreats |

|

[User Activity](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-users-scm) | InsightsActivity InsightsUsers |

|

[URL and Domain Activity](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-urls) | InsightsActivity InsightsDomains |

|

[Rules Inventory](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-rules) | InsightsActivity InsightsRules |

|

[Traffic by Region](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-regions) | InsightsActivity InsightsRegions |

|

[Search any Security Artifact](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/monitor/search) | InsightsThreat Search |

---

<a id="scm-configuration-management"></a>

#### Configuration Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager/operationalize-config-mgmt>*

Learn how to use Strata Cloud Manager's to manage the products in your
environment.

This section highlights the unique Strata Cloud Manager management features compared to
Panorama and outlines the actions you can take after setting up your product for new
deployments.

- **Migrated from Panorama**

  After migrating your configuration from Panorama
  to Strata Cloud Manager, here are some distinctive features you can
  configure and automated tasks you can perform to optimize and secure your
  deployment.

  - [**Feature Parity**](https://docs.paloaltonetworks.com/compatibility-matrix/reference/feature-parity)

    In
    addition to the configuration that is covered in the Strata Cloud
    Manager for Visibility section, there are additional custom
    configuration which are included when you are using Strata Cloud
    Manager for configuration Management.
  - **Exclusive Configuration Management Features**

    In addition to the
    configuration that is covered in the Strata Cloud Manager for
    Visibility section, there are additional custom configuration which
    are included when you are using Strata Cloud Manager for
    configuration Management.

    - [**Custom
      Dashboards**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/custom-dashboard)- Create custom dashboards to get
      visibility into areas of your interest in your network.
    - **[Policy
      Analyzer](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-analyzer)**- Analyze and provide suggestions for
      possible consolidation or removal of specific rules, and also
      checks for anomalies in your rulebase.
    - **[Custom Best Practice
      Check](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/security-posture-settings?otp=task_orq_xlr_jxb#task_orq_xlr_jxb)**-Create custom best practice
      checks.
    - [**User Coaching Notification
      Template**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access/global-settings/user-coaching-notification-template)- Configure the notification
      displayed to your users in the [Access Experience User
      Interface](https://docs.paloaltonetworks.com/autonomous-dem/self-serve-application-experience-troubleshooting/application-experience-user-interface) (UI) when they generate an Enterprise Data
      Loss Prevention (E-DLP) [incident](https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/view-dlp-log-details).
  - **Immediate Actions**
    - [**Optimize rule**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-optimizer)-
      Check the optimized rule suggestions for overly permissive rules
      to close the security gaps.
    - [**Cleanup unused
      configuration and rules**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/config-cleanup)-Remove unused
      configuration and policy rules to ease the administration.
- **New Deployment**

  After setting up Prisma Access or NGFW, you can
  configure the following features exclusive to Strata Cloud Manager:
  - [**Global
    Configurations**](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager.html#tabs-operationalize-strata-cloud-manager_ul-ngl_ybk_d2c)
  - [**Exclusive Configuration
    Management Features**](#scm-topic-17f356e7-8911-454e-9b36-c6b2f2f57478_ul-msy_jmk_d2c)

After completing the initial configuration you can evaluate the data in dashboards and
[Activity insights](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights%20Activity%20insights%20-) to refine the security
policies and act on any immediate threats.

---

<a id="scm-strata-cloud-manager-essentials"></a>

#### Strata Cloud Manager Essentials

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-essentials>*

Learn about Strata Cloud Manager Essentials that provides management and security
features, and the features that are available to you for free.

Strata Cloud Manager Essentials is the free tier that offers configuration
management, network security lifecycle management, and can also provide visibility if
the you have Strata Logging Service. It is supported for the below products:

- [Next-Generation Firewalls (NGFW)](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments)
- [VM-Series funded by Software NGFW
  Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license)

[**Strata Logging Service**](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) is available as
an optional add-on for Strata Cloud Manager Essentials. Strata Logging Service provides
centralized log storage and retrieval across your deployment, but you must purchase it
separately from Strata Cloud Manager Essentials.

Here are the features Strata Cloud Manager Essentials gives you:

- [**Command Center and Activity
  Insights**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center) provide interactive dashboards that help you
  to know how Palo Alto Networks security services are protecting your network.
  You can interact with data on the applications, threats, users, and security
  subscriptions at work in your network.
- [**Configuration and Policy Management for
  NGFW and SASE**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access) provides centralized configuration
  management across all your firewalls and SASE environments. This ensures
  consistent security policy enforcement and simplifies administrative tasks.
- [**Best Practices Reporting**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
  helps you adopt NGFW and SASE services quickly by providing tools and
  recommendations to align configurations with industry best practices, improving
  the overall security posture.
- [**Health Insights**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards) **and**[**Alerts**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts) provide
  fundamental insights into the operational health of Prisma Access and NGFWs.
  These insights include deployment-wide status updates, key metrics such as
  traffic volumes, and proactive identification of potential hardware or software
  issues.

See [Activate Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html).

---

<a id="scm-essentials-and-pro-feature-support"></a>

#### Essentials and Pro Feature Support

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-feature-support>*

Learn about the features supported for Strata Cloud Manager Essentials and Pro
licensing tiers.

|

Feature Set | Strata Cloud Manager Essentials | Strata Cloud Manager Essentials + Strata Logging Service | Strata Cloud Manager Pro |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

**Operational Health** | | | |

|

Hardware Health incidents | Yes | Yes | Yes |

|

Software and licensing incidents | Yes | Yes | Yes |

|

Deployment specific incidents | No | No | Yes |

|

Forecasting and Anomaly detection in incidents | No | No | Yes |

|

Root Cause Analysis in incidents | No | No | Yes |

|

In-product support ticket creation | Yes | Yes | Yes |

|

Deployment wide status and metric trends | Yes | Yes | Yes |

|

Capacity Analyzer | No | No | Yes |

|

Upgrade Recommendations | No | No | Yes |

|

ServiceNow Integration | Yes | Yes | Yes |

|

API access | Yes | Yes | Yes |

|

**Security Posture** | | | |

|

Custom Configuration Settings | No | No | Yes |

|

Compliance | No | No | Yes |

|

Policy Analyzer (ML) | No | No | Yes |

|

Policy Optimizer (ML) | No | No | Yes |

|

Config Cleanup | No | No | Yes |

|

**Configuration Management** | | | |

|

Cloud Management for NGFW | Yes | Yes | Yes |

|

Cloud Management for Prisma Access | Yes | Yes | Yes |

|

Cloud Management for standalone SD-WAN | Yes | Yes | Yes |

|

Cloud Management for other licensed CDSS subscriptions | Yes | Yes | Yes |

|

Rule Hit Count within the Cloud Manager configuration | No | Yes | Yes |

|

Configuration exceptions from logs | No | Yes | Yes |

|

**Strata Logging Service** | | | |

|

Retention (1 year default) | No | Yes | Yes |

|

Log Forwarding | No | Yes | Yes |

|

**Autonomous Digital Experience Management (ADEM)** | | | |

|

AI-Powered ADEM | No | No | Yes |

|

**Visualization and Reporting Dashboards** | | | |

|

Command Center | No | Yes | Yes |

|

Activity Insights | No | Yes | Yes |

|

Executive Summary | No | Yes | Yes |

|

WildFire dashboard | Yes | Yes | Yes |

|

DNS security dashboard | Yes | Yes | Yes |

|

DLP Incidents dashboard | No | Yes | Yes |

|

SaaS Security dashboard | No | Yes | Yes |

|

Log Viewer | No | Yes | Yes |

|

IOC Search | No | Yes | Yes |

|

SASE Health | No | Yes | Yes |

|

Prisma Access Usage | No | Yes | Yes |

|

Reports | No | Yes | Yes |

|

SD-WAN Dashboard | No | Yes | Yes |

|

IoT Dashboard | Yes | Yes | Yes |

|

CASB-X Dashboard | Yes | Yes | Yes |

|

Branch Sites | No | Yes | Yes |

|

Data Centers | No | Yes | Yes |

|

Network Services | No | Yes | Yes |

|

Prisma Access Locations | No | Yes | Yes |

|

Strata Copilot | Yes | Yes | Yes |

|

AI Canvas | No | No | Yes |

In-App support case creation capability is only available to Strata Cloud Manager Pro
and devices' with platinum support.

---

<a id="scm-strata-cloud-manager-pro"></a>

#### Strata Cloud Manager Pro

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/strata-cloud-manager-pro>*

Learn about Strata Cloud Manager Pro.

Strata Cloud Manager Pro provides advanced features on top of the Essentials
license. Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview), unlike the
Essentials version, and one year of log retention. You can purchase Strata Cloud Manager
Pro for the following products:

- [Next-Generation Firewalls (NGFW)](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments)
- [VM Series funded by Software NGFW
  Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license)
- Cloud NGFW for [Azure](https://docs.paloaltonetworks.com/cloud-ngfw-azure/getting-started/introducing-cloud-ngfw-for-azure) and [AWS](https://docs.paloaltonetworks.com/cloud-ngfw-aws/release-notes/whats-new-cloud-ngfw-for-aws)

Here are the features Strata Cloud Manager Pro gives you:

- All the features available in Strata Cloud Manager Essentials.
- [**Strata Logging Service**](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)
  with one year of log retention and unlimited storage, enabling centralized
  logging and seamless data retrieval across your deployment.
- [**AI-Powered Observability with
  ADEM**](https://docs.paloaltonetworks.com/autonomous-dem): Strata Cloud Manager Pro integrates Autonomous
  Digital Experience Management (ADEM) for holistic observability across your
  network. ADEM helps to automate complex IT operations, reduce ticket volume, and
  shorten the mean time to resolution (MTTR).
- [**Real-time inline best
  practices**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices) provide proactive, context-aware recommendations
  directly within the web interface as you configure and manage security policies.
  This feature ensures that your configurations align with industry standards and
  Palo Alto Networks' security best practices, reducing misconfigurations and
  enhancing your overall security posture.
- [**AI-Powered Policy
  Analysis**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-analyzer) leverages advanced artificial intelligence and
  machine learning to analyze your security policies in real time, providing
  actionable insights to optimize, streamline, and strengthen your security
  posture. This feature automates the evaluation of complex policy sets, helping
  administrators make informed decisions to improve network security and
  performance.
- [**AI-Powered Operational
  Health**](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about) includes enhanced operational health capabilities
  designed to anticipate and prevent issues before they impact your network. For
  example, forecasting and anomaly detection in alerts, Root Cause Analysis in
  alerts, and Capacity Analyzer.
- [**Software Upgrade Planner**](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/software-upgrades#software-upgrades-ngfw)
  analyzes the features enabled on firewalls and provides a customized
  recommendation. You can create upgrade recommendations to identify the best
  software version for upgrading your devices.

See [Activate Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html).

---

<a id="scm-strata-cloud-manager-prerequisites-for-ngfw-and-vm-series-funded-by-software-ngfw-credits"></a>

#### Strata Cloud Manager Prerequisites for NGFW and VM-Series Funded by Software NGFW Credits

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-ngfw>*

Learn about Strata Cloud Manager prerequisites for NGFWs.

Strata Cloud Manager provides comprehensive visibility and insights for your Palo Alto
Networks Next-Generation Firewalls (NGFW) deployments, whether managed by Strata Cloud
Manager or Panorama. You can onboard your NGFW to Strata Cloud Manager to manage and
gain insights. If you already have NGFWs managed by Panorama, you can connect Strata
Cloud Manager to your Panorama using the [Panorama CloudConnector Plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama).

When preparing to onboard and manage your NGFW and VM-Series funded by software
NGFW credits through Strata Cloud Manager, ensure that the necessary prerequisites are
met. This section covers the essential areas for successful onboarding, including
connectivity requirements and supported regions.

- **[Cloud Management for NGFWs Onboarding Prerequisites](#scm-strata-cloud-manager-prerequisites-ngfw_concept-crd_mf1_ggc)** - Before onboarding your NGFW to Strata Cloud Manager, verify that all
  conditions for device readiness are fulfilled. This includes network configuration,
  software compatibility, and licensing requirements. Completing these steps ensures
  that your firewall can be successfully managed using Strata Cloud Manager.

  To onboard VM-series funded by software NGFW credits, see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).
- **[Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility)** -
  Device models that you can associate with Strata Cloud Manager.
- **[TCP Ports and FQDNs Required for Cloud Management of NGFWs](#scm-strata-cloud-manager-prerequisites-ngfw_concept-i2t_1lr_lgc)** - To enable seamless communication between the NGFW and Strata Cloud
  Manager, configure specific TCP ports and Fully Qualified Domain Names (FQDNs).
- **[Enable Telemetry on Devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics)** -
  Enable telemetry on your NGFW to allow Strata Cloud Manager to collect necessary
  data for insights and recommendations. Strata Cloud Manager assesses the health of
  the devices in your deployment by analyzing telemetry data that your PAN-OS devices
  send to Strata Logging Service.
- **[Create Device Labels](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use Device Labels in Strata
  Cloud Manager to automate and streamline NGFW onboarding and management
  processes.
- **[Create a Device Onboarding Rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use device
  onboarding rules to automate parts of the NGFW onboarding process for Strata Cloud
  Manager.

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept-crd_mf1_ggc"></a>

##### Cloud Management for NGFWs Onboarding Prerequisites

Review the requirements to onboard a Strata Cloud Manager tenant and
firewalls to Strata Cloud Manager.

Note that some requirements, such as PAN-OS Version, Firewall Model,
Ports, and Services, apply to the firewall. While others, such as the Logging and
Authentication service requirements, apply to your Customer Support Portal (CSP)
account.

|

Prerequisite | Supported | Required? |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

PAN-OS Version | (minimum)PAN-OS 10.2.3 | Yes |

|

Firewall Model  Single vsys firewalls only  Multi-vsys firewalls are not supported  PA-410 not supported if Enterprise DLP license is active | PA-220 and PA-220R  PA-400 Series  PA-450R, PA-455R, and PA-455R-5G  PA-500 Series  PA-800 Series  PA-1400 Series  PA-3200 Series  PA-3400 Series  PA-5200 Series  PA-5400 Series  PA-5500 Series  PA-7000 Series  PA-7500  VM-Series | N/A |

|

Device Certificates | The device certificate must be installed on NGFWs before onboarding to Strata Cloud Manager.  Some NGFW models automatically install the device certificate when you first register the device on the support portal. For others, you need to [manually install device certificates](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate) before onboarding.  For any NGFW models with expired certificates, you must manually renew the certificates before onboarding. | Yes  Whether you need to manually install the device certificate before onboarding depends on your [NGFW model](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate), or the status of your device certificates. |

|

Ports  Ports are used for outbound communication from the firewall to Strata Cloud Manager and SLS | 443  444  3978 | Yes |

|

Services  Services are used for resolution of the Strata Cloud Manager tenant, as well as software and content updates | DNS  NTP | Yes |

|

Firewall Onboarding | AIOps for NGFW (Premium)  (Optional) Zero Touch Provisioning (ZTP) | Yes  ZTP onboarding is optional |

|

Firewall Management | Strata Cloud Manager | Yes Account Administrator or App Administrator [hub roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles) |

|

Logging | Strata Logging Service | Yes |

|

Data Filtering | Enterprise data loss prevention (DLP) | No |

|

Routing | Advanced Routing Engine  Enabled by default during onboarding | Yes |

|

SaaS Application Management | Next-Generation CASB | No |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept-i2t_1lr_lgc"></a>

##### TCP Ports and FQDNs Required for Cloud Management of NGFWs

Review the TCP ports and Fully Qualified Domain Names (FQDN) that you must enable on
your network communication and between the Palo Alto Networks Next-Gen Firewall
(NGFW) and Strata Cloud Manager. Communication on these TCP ports and FQDNs must
allowed on your network to successfully manage your firewalls from Strata Cloud Manager.

- [Connections to Strata Cloud Manager](#scm-strata-cloud-manager-prerequisites-ngfw_concept_hzr_py2_lvb)
- [Connections to Strata Logging Service](#scm-strata-cloud-manager-prerequisites-ngfw_concept_y5r_h2f_lvb)
- [Connections for Firewall Certificates](#scm-strata-cloud-manager-prerequisites-ngfw_concept_ocq_pkf_lvb)

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_hzr_py2_lvb"></a>

###### Connections to Strata Cloud Manager

You must allow the following app, FQDNs, and TCP ports on your network to enable
connectivity between the firewall and Strata Cloud Manager.

The Virtus service is a device connectivity service that facilitates the
connection between the firewall and Strata Cloud Manager. The FQDN and/or IP
address for the region where your Strata Cloud Manager tenant is deployed must
be allowed on your network for the firewall to successfully connect to Strata Cloud Manager. The firewall cannot connect to Strata Cloud Manager if
the FQDN or IP address is blocked.

Required App-ID and Port for Strata Cloud Manager

|

App-ID | TCP Port |

| --- | --- |

|  |  |
| --- | --- |
|

panorama | 3978 |

Required FQDNs, IP Addresses, and Ports for Strata Cloud Manager

|

Service | FQDN | IP Address | TCP Ports |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

OCSP | - [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/) - [ocsp.godaddy.com](http://ocsp.godaddy.com) | N/A | 80 |

|

Virtus | **Australia**—\*.aus.ngfw.cloudmgmt.paloaltonetworks.com | 34.151.118.202 | 3978  443 |

|

**Canada**—\*.ca.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.139.11 |

|

**E.U**—\*.eu.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.199.57 |

|

**France**—\*.fr.ngfw.cloudmgmt.paloaltonetworks.com | 34.155.195.45 |

|

**India**—\*.in.ngfw.cloudmgmt.paloaltonetworks.com | 35.200.223.12 |

|

**Israel** —\*.il.ngfw.cloudmgmt.paloaltonetworks.com | 34.165.153.154 |

|

**Italy**—\*.it.ngfw.cloudmgmt.paloaltonetworks.com | 34.154.245.218 |

|

**Indonesia**—\*.id.ngfw.cloudmgmt.paloaltonetworks.com | 34.101.126.22 |

|

**Japan**—\*.jp.ngfw.cloudmgmt.paloaltonetworks.com | 34.146.27.93 |

|

**Poland**—\*.pl.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.28.91 |

|

**Qatar**—\*.qa.ngfw.cloudmgmt.paloaltonetworks.com | 34.18.53.154 |

|

**Saudi Arabia**— \*.sa.ngfw.cloudmgmt.paloaltonetworks.com | 34.166.126.37 |

|

**Singapore**—\*.sg.ngfw.cloudmgmt.paloaltonetworks.com | 35.198.210.240 |

|

**South Africa**—\*.za.ngfw.cloudmgmt.paloaltonetworks.com | 34.35.27.12 |

|

**Spain**—\*.es.ngfw.cloudmgmt.paloaltonetworks.com | 34.175.25.27 |

|

**Switzerland**—\*.ch.ngfw.cloudmgmt.paloaltonetworks.com | 34.65.231.25 |

|

**U.K**—\*.uk.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.86.14 |

|

**U.S.A**—\*.us.ngfw.cloudmgmt.paloaltonetworks.com | 34.31.195.141 |

|

Discovery Service | ds-cloudmgmt.paloaltonetworks.com | N/A | 443 |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_y5r_h2f_lvb"></a>

###### Connections to Strata Logging Service

You must allow the following apps, FQDNs, and TCP ports on your network to
forward logs from the managed firewall to Strata Logging Service (SLS). For more
details, see the [TCP Ports and FQDNs Required for](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns)  (SLS).

Required App-ID and Ports for SLS

|

App-ID | TCP Port |

| --- | --- |

|  |  |
| --- | --- |
|

- paloalto-shared-services - panorama | 444  3978 |

|

Required if you’re sending [device telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry/device-telemetry-overview) data to SLS.   - paloalto-device-telemetry - google-base | 443  5222-5224  5228  5229 |

Required FQDNs and Ports for SLS

|

Service | FQDN | TCP Ports |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

OCSP | - [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/) - [crl.paloaltonetworks.com/](http://crl.paloaltonetworks.com/) - [ocsp.godaddy.com](http://ocsp.godaddy.com) | 80 |

|

SLS Certificates | - [api.paloaltonetworks.com](https://api.paloaltonetworks.com) - [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com) - [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) - [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) | 3978 |

|

Prisma Access | \*.gpcloudservice.com | 443 |

<a id="scm-strata-cloud-manager-prerequisites-ngfw_concept_ocq_pkf_lvb"></a>

###### Connections for Firewall Certificates

You must allow the following FQDNs, and TCP ports on your network to enable your
managed firewalls to install the device certificates for Strata Cloud Manager.

|

Service | FQDN | TCP Ports |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

API | - [api.paloaltonetworks.com](https://api.paloaltonetworks.com) - [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com) | 443 |

|

Device Certificates | - [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) - [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com) | 443 |

---

<a id="scm-strata-cloud-manager-prerequisites-for-prisma-access"></a>

#### Strata Cloud Manager Prerequisites for Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-prisma-access>*

Here's what you need to know to plan your Prisma Access deployment

Strata Cloud Manager provides comprehensive visibility and insights into all Prisma
Access deployments, whether managed by Strata Cloud Manager or Panorama. Additionally,
you have the option to use Strata Cloud Manager as the management interface for Prisma
Access if needed.

During Prisma Access activation, you can choose either Strata Cloud Manager or Panorama
as the management interface. If Panorama currently manages your Prisma Access
deployment, you can migrate the configuration to Strata Cloud Manager for management.
However, after migrating, you cannot switch back to Panorama.

Before onboarding Prisma Access to Strata Cloud Manager, carefully review the following
prerequisites to ensure your existing Prisma Access deployment satisfies all necessary
conditions for a smooth and seamless onboarding.

- **Panorama Version** - Ensure you are using Panorama version 10.0 or higher.
- **Administrative Privileges** - You need an account with superuser privileges to
  log into Strata Cloud Manager.
- **License Requirements** - Ensure you have a valid [Prisma Access license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license).
- **Cloud Identity Engine** - Ensure that you have [integrated the Directory Sync component](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access/integrate-cloud-identity-engine-with-prisma-access-panorama#integrate-cloud-identity-engine-with-prisma-access-panorama) of
  the Cloud Identity Engine with the current Prisma Access (Managed by Panorama)
  tenant

Additionally, if you are migrating from Panorama to Strata Cloud Manager, review the
[migration prerequisites](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-bcj_p2w_zbc#task-bcj_p2w_zbc) to confirm whether
your deployment is eligible for configuration migration.

---

<a id="scm-ngfw"></a>

#### NGFW

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-ngfw-onboarding>*

##### NGFW for Visibility

After installing the [Panorama CloudConnector plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) and
enabling [Device Telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry), you need to wait for 24
hours to see data in the Strata Cloud Manager Dashboards and Activity Insights.

##### NGFW for Configuration Management

After moving your firewalls to Strata Cloud Manager, validate the onboarding of the
devices by verifying the following:

- **Verify the state of configuration pushes**

  After successful onboarding to
  Strata Cloud Manager, two configuration pushes occur by default to the
  firewall. Select ConfigurationOPERATIONS Push Status to verify that your configuration push was successful.

  1. The first push from Strata Cloud Manager automatically enables the
     Advanced Routing Engine and restarts the firewall.
  2. The second pushes the configuration from Strata Cloud Manager to the
     firewall.
- **Verify the device details in the Cloud Managed Devices**

  Select System SettingsDevice ManagementCloud Managed Devices and check for the serial number for the firewall that you
  just added. By default, newly onboarded firewalls are added to the **All
  Firewalls** folder.
- **Validate firewall connection**

  [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and
  verify that the firewall is successfully connected to Strata Cloud
  Manager.
- Verify that your firewall appears in the **Summary View** of Strata Cloud
  Manager [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center).

---

<a id="scm-prisma-access"></a>

#### Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-prisma-access-onboarding>*

Validate your successful onboarding by launching Strata Cloud Manager and checking for
data in the [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-overview) and [Dashboards](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/prisma-access-usage).

If you are using Strata Cloud Manager for visibility or have migrated the management
interface from Panorama to Strata Cloud Manager, you will immediately see data in Strata
Cloud Manager. However, if you installed Prisma Access with Strata Cloud Manager as the
management interface and are in the process of configuring its features, you must
complete the full setup to start viewing data.

---

<a id="scm-system-settings-strata-cloud-manager"></a>

## System Settings: Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/settings>*

Manage all global processes for Strata Cloud Manager.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Strata Cloud Manager) | - Any [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) supported app - A [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) depending   on your needs - Strata Logging Service to manage logs |

From System Settings, you can manage the processes that pertain to
all services offered in Strata Cloud Manager. These processes include:

### Identity & Access

Control authentication and authorization of user roles and permissions for all
applications and API-based access. Through Identity & Access, you can manage:

- User access
- Service accounts
- Roles
- Third-party identity provider integration

[Get started with Identity &
Access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/get-started/supertask).

### Products

If you have a single tenant environment, view, launch, and manage your products:

- Get product information
- Rename instance
- Manage sharing
- Add a tenant

Get started with [Product Management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-products).

### Tenants

If you're a managed security service provider (MSSP) or distributed enterprise, you
can create and manage your hierarchy of business organizations and units,
represented by tenants. From Tenants, you can:

- Add a tenant
- Edit a tenant
- Manage tenant licenses
- Delete a tenant
- Transition from a single tenant to a multitenant deployment

[Get started with Tenant Management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants).

### Audit Logs

View records of all actions initiated by users of Strata Cloud Manager

[View Audit Logs](https://docs.paloaltonetworks.com/cloud-management/administration/settings/audit-logs.html).

### Device Associations

Most often used in device and app onboarding, Device Associations enables you
to:

- Associate new devices with a tenant
- Associate apps with your devices
- Manage device and app associations

[Get started with Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).

### Trusted IPs

Use Trusted IP Lists to restrict access to your applications by specifying IP
addresses that are allowed on a per tenant basis.

[Configure a
Trusted IP List](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/trusted-ip-list.html).

### Device Management

Review all your NGFW device and choose a device to move to cloud management. NGFW
device that is managed by Strata Cloud Manager is called a *Cloud Managed
Device*

[System Settings: Device Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-device-management.html).

### Folder & Snippet Management

Create and manage folders, which are a logical group of firewalls and deployments,
for simplified configuration management. View and
manage all snippets in your configuration, and browse the Snippet Library to
opt in to predefined snippets.

[System Settings: Folder & Snippet Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management.html).

### Scope Management

Configure scope management to enforce custom role-based access control. This allows
you to specify which Strata Cloud Manager administrators can access and modify
specific folders, firewalls, Prisma Access deployments, and snippet
configurations.

[System Settings: Scope Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-scope-management.html).

### Access Experience Management

Allows you to manage your Autonomous DEM users and remote sites.

[System Settings: Access Experience Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-access-experience-management.html).

### Subscriptions List

View the approved subscriptions for your product.

[Manage Subscriptions](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/about-subscription-management).

### vION Subscription Management

Generate authorization tokens for virtual ION devices. This provides a set of
controls to prevent unauthorized addition of virtual devices to an environment.

[Manage vION Subscriptions](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan/deployment-and-integrations/prisma-sd-wan-virtual-ion-on-gcp-deployment/plan-a-prisma-sd-wan-gcp-virtual-deployment/virtual-ion-licensing-and-token-management).

---

---

# Cloud Identity Engine - Activation and Licensing

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/identity on 2026-06-27. 13 pages. Absolute URLs.

> Scoped to: /activation-and-onboarding

## Table of Contents

  - [Get Started with Cloud Identity Engine](#cie-get-started-with-cloud-identity-engine)
    - [Cloud Identity Engine Licensing](#cie-cloud-identity-engine-licensing)
    - [Plan Your Cloud Identity Engine Deployment](#cie-plan-your-cloud-identity-engine-deployment)
      - [Configure Your Network to Allow Cloud Identity Agent Traffic](#cie-configure-your-network-to-allow-cloud-identity-agent-traffic)
      - [Configure Domains for the Cloud Identity Engine](#cie-configure-domains-for-the-cloud-identity-engine)
    - [Activate the Cloud Identity Engine](#cie-activate-the-cloud-identity-engine)
      - [First time Cloud Identity Engine Activation - One Customer Support Portal Account](#cie-first-time-cloud-identity-engine-activation-one-customer-support-portal-account)
      - [First time Cloud Identity Engine Activation - Multiple Customer Support Portal Account](#cie-first-time-cloud-identity-engine-activation-multiple-customer-support-portal-account)
      - [Return Visit Cloud Identity Engine Activation](#cie-return-visit-cloud-identity-engine-activation)
      - [Share Cloud Identity Engine](#cie-share-cloud-identity-engine)
    - [Manage Cloud Identity Engine App Roles](#cie-manage-cloud-identity-engine-app-roles)
    - [Configure the Cloud Identity Engine Visibility Scope](#cie-configure-the-cloud-identity-engine-visibility-scope)
- [Get Started with Cloud Identity Engine](#cie-get-started-with-cloud-identity-engine-1)

---

<a id="cie-get-started-with-cloud-identity-engine"></a>

### Get Started with Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine>*

How to get started with the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Welcome to the Cloud Identity Engine! The Cloud Identity Engine provides a centralized,
cloud-native source of truth for user identity and authentication, enabling your
organization to move toward a Zero Trust security posture. By aggregating and
normalizing identity data from on-premises, cloud-based, and hybrid infrastructures, the
service allows you to enforce consistent security policies based on users and groups
rather than IP addresses,. This ensures that security decisions remain accurate and
effective across data centers, campuses, public clouds, and remote user
environments.

Deployment begins with planning your architecture, specifically selecting the appropriate
region to ensure compliance with data residency regulations and defining the visibility
scope to control firewall access to your tenants. Next, you activate the service within
the Palo Alto Networks Hub to provision your tenant and prepare for synchronization. You
then set up your identity sources by installing the Cloud Identity Agent for on-premises
directories or establishing secure API connections for cloud-based providers like
Microsoft Entra ID and Okta. Finally, you associate the Cloud Identity Engine with your
Palo Alto Networks applications, such as Prisma Access or Next-Generation Firewalls, to
enable them to consume identity data for policy enforcement.

---

<a id="cie-cloud-identity-engine-licensing"></a>

#### Cloud Identity Engine Licensing

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing>*

Learn about Cloud Identity Engine licensing.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | See requirements below. |

The Cloud Identity Engine is designed as a core infrastructure component to facilitate
Zero Trust and is generally available at no additional cost to Palo Alto Networks
customers. It does not require a standalone subscription license or an authorization
code for activation.

##### Core Service Availability

The full feature set of the Cloud Identity Engine—including Directory Sync and the
Cloud Authentication Service—is included as a free core feature for the following
platforms:

- **Next-Generation Firewalls (Hardware and Virtual):** Available for PA-Series
  and VM-Series firewalls running **PAN-OS 10.1** and later.
- **Panorama:** Available for management platforms running **PAN-OS 10.1**
  and later.
- **Prisma Access:** Available for Strata Cloud Manager managed or Panorama
  managed Prisma Access running any software version with the Panorama
  plugin.
- **Strata Cloud Manager:** The service is integrated into Strata Cloud
  Manager, with availability depending on the licenses held (e.g., Prisma
  Access, AIOps for NGFW Premium, or Strata Cloud Manager Essentials/Pro).

##### Required Roles

To activate, configure, and manage the Cloud Identity Engine within the Palo Alto
Networks Hub (Common Services), you [must assign specific app roles to your administrators](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/manage-cloud-identity-engine-app-roles.html).
These roles determine the level of access users have to tenant management, directory
data, and secrets configuration.

##### Feature Specific Licensing

While the Cloud Identity Engine service itself is free, specific advanced features or
integrations may require licenses on the associated enforcement points:

- **Third-Party Device-ID:** To utilize APIs for managing IP address-to-device
  mappings or to configure Third-Party Device-ID in Prisma Access, a **Device
  Security** license is required in addition to a **Prisma Access**
  license.
- **Dynamic Privilege Access (DPA):** This feature, which allows for
  project-based resource isolation, requires a **Prisma Access** license and
  must be activated by your account representative.
- **Data Security & DLP:** Features involving Enterprise DLP or
  Next-Generation CASB integrations require their respective licenses (e.g.,
  Enterprise DLP, CASB-X) to be active on the associated tenant.

##### Activation

You can activate the Cloud Identity Engine directly through the Palo Alto Networks
Hub without an authorization code. During the onboarding process, you may be asked
to claim licenses for other products (like Prisma Access), but the Cloud Identity
Engine itself does not require a specific claim code.

To start planning your Cloud Identity Engine deployment, click here.

---

<a id="cie-plan-your-cloud-identity-engine-deployment"></a>

#### Plan Your Cloud Identity Engine Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment>*

Learn about pre-deployment planning for the Cloud Identity
Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Successful implementation of the Cloud Identity Engine begins with evaluating your
infrastructure to ensure it meets the necessary connectivity and architectural
requirements. Before activating tenants or installing agents, you must [configure your network](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-your-network-to-allow-cloud-identity-engine-traffic.html#id0947ba4b-3d5a-49f3-8698-feee03469d3b) to allow
specific traffic between your directory sources, the Cloud Identity Agent, and the cloud
service. This includes allowing traffic to region-specific hostnames and ensuring that
required ports—such as port 80 for certificate verification and port 443 for secure TLS
communication—are open.

You must also prepare your [directory domains](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-multiple-domains-for-the-cloud-identity-engine.html#id18A1GG0M0WB) for integration.
For on-premises Active Directory, this involves provisioning a service account with
permissions to execute LDAP queries against all target domains and planning agent
placement to ensure redundancy if a domain controller becomes unavailable.

Strategic planning also requires defining the scope of your deployment. You must select a
Region that aligns with your data residency requirements and other Palo Alto Networks
applications, such as Prisma Access, to minimize latency and ensure compliance.

---

<a id="cie-configure-your-network-to-allow-cloud-identity-agent-traffic"></a>

##### Configure Your Network to Allow Cloud Identity Agent Traffic

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-your-network-to-allow-cloud-identity-engine-traffic>*

Learn how to configure your network to allow traffic for the agent, your directory, and
the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Depending on your network configuration and Cloud Identity Engine deployment type, allow the
traffic for the agent (if you have an on-premises directory), your directory, and
the Cloud Identity Engine.

- Based on your region, allow traffic to the hostname for the region. To
  determine what region-based traffic to allow, refer to the table in [Configure the Cloud Identity agent](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent).
- Use the ssl App-ID in your Security policy (following
  our recommended [Decryption Best Practices](https://docs.paloaltonetworks.com/best-practices/10-2/decryption-best-practices/decryption-best-practices) guidelines)
  to allow traffic to the Cloud Identity Engine.
- If you have deployed a Palo Alto Networks firewall
  between the agent and the Cloud Identity Engine:

  The Cloud Identity agent version 1.7.0 and previous
  versions require direct reachability to the regional agent configuration
  endpoint and don't support proxy servers between the agent and the endpoint.
  If your network configuration uses a proxy server, you must [update the Cloud Identity agent](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/update-the-cloud-identity-agent) to
  version 1.7.1 or later.

  - Use the paloalto-cloud-identity App-ID
    to allow traffic from the Cloud Identity agent to the Cloud Identity
    Engine. This App-ID requires the ssl and web-browsing application
    signatures.
  - Allow Cloud Identity agent traffic from the specified ports to the following URLs.
    - http://crl.godaddy.com on port 80.
    - http://ocsp.godaddy.com on port 80.
    - https://certs.godaddy.com on port
      443.
  - If you’re using Secure Socket Layer (SSL) decryption on the firewall, [exclude](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/decryption/decryption-exclusions/exclude-a-server-from-decryption) the traffic between
    the agent and the Cloud Identity Engine from SSL decryption to allow the
    mutual authentication between the agent and the service.
- If you have deployed a Palo Alto Networks firewall between the
  agent and the Active Directory:

  Depending on which protocol you select when you [configure the Cloud Identity agent](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent),
  use one of the following App-IDs to allow traffic from the Cloud Identity agent
  to your domain controllers.
  - If the agent uses the LDAP protocol, use the ldap
    App-ID.
  - If the agent uses the LDAPS or LDAP with STARTTLS protocol, use the
    ssl App-ID.
- If you're using a non-Palo Alto Networks firewall:

  - Allow LDAP or LDAPS traffic to the LDAP or LDAPS port from the Cloud
    Identity agent to your Active Directory or Domain Controller.
  - Allow HTTPS traffic from the Cloud Identity agent on port 443 to your
    Cloud Identity Engine destination URL. You need to allow traffic only
    for the region that you specify for your tenant and you need to allow
    traffic for multiple regions only if you have tenants in multiple
    regions. For the region-specific agent configurations, refer to [Configure the Cloud Identity
    agent](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent).
  - Allow traffic from the Cloud Identity agent from the specified ports to
    the following URLs.
    - http://crl.godaddy.com on port 80.
    - http://ocsp.godaddy.com on port 80.
    - https://certs.godaddy.com on port
      443.

---

<a id="cie-configure-domains-for-the-cloud-identity-engine"></a>

##### Configure Domains for the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-multiple-domains-for-the-cloud-identity-engine>*

Learn about best practices for configuring domains for
the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

###### On-Premises Active Directory Domains

A
single Cloud Identity agent can communicate with multiple domains.
The service account you use to query the Active Directory must have
permission to query all domains you configure on the agent. We recommend
configuring multiple domain controllers for each domain so that
if a domain controller is unavailable, the agent can try the next
available domain controller.

To ensure agent redundancy for
a domain, configure multiple agents for that domain. The server
hosting the agent should be physically located near the domain controllers
from which the agent will collect attributes. If the domain controllers
are in different locations, we recommend that you configure multiple agents
and install each agent on a host server that is physically located
near the domain controllers from which the agent will collect attributes.

To
obtain cross-domain memberships for groups with members from other domains
in the forest, configure those domains on the Cloud Identity agent(s).
In this scenario, you must configure the agent to connect to the
domain controllers using the LDAP or LDAPS port (by default, 389
and 636 respectively).

When you configure the Active Directory
in the Cloud Identity agent, do not configure the agent to use the
Global Catalog port (3268 for LDAP or 3269 for LDAPS).

###### Azure Active Directory Domains

Ensure that your Azure Active Directory (Azure AD) does not contain any circular references,
where a group is a direct or indirect member of itself (for example, Group 2 is a
member of Group 1 and Group 1 is a member of Group 2). If your Azure AD contains circular references, the
Cloud Identity Engine cannot accurately populate the membership of the groups and
you must change the membership of the groups to remove the circular references.
After removing the circular references, [sync](https://docs.paloaltonetworks.com/identity/cloud-identity-engine//cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances.html) the attributes to verify that the
Cloud Identity Engine can successfully collect the attributes.

To successfully sync the attributes from
Azure AD, the Cloud Identity Engine automatically removes circular
references. If you do not make any changes, the Cloud Identity Engine
is still operational and other applications, such as Prisma Access,
can successfully retrieve data from the Cloud Identity Engine, but
the membership of the circular groups may not be correctly computed
in Cloud Identity Engine. Therefore, we strongly recommend that
you manually remove any circular references from the Azure AD to
ensure the Cloud Identity Engine operates as expected.

---

<a id="cie-activate-the-cloud-identity-engine"></a>

#### Activate the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine>*

Activate the Cloud Identity Engine in the hub to create your first tenant.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

Activating the Cloud Identity Engine is the foundational step in establishing
a centralized, cloud-native source of truth for user identities across your security
infrastructure. This process is performed within the Palo Alto Networks Hub and
initializes the tenant that will aggregate and normalize user, group, and device
data from your disparate directory sources. Unlike traditional hardware deployments,
activation focuses on provisioning the cloud service, enabling you to prepare your
environment for identity synchronization without the need for immediate physical
appliance installation.

The activation workflow is designed to accommodate
various organizational structures, ranging from **Single Customer Support Portal
(CSP) Accounts** to complex environments managing **Multiple CSP Accounts**
or child tenants. While the service is often included as a free integration
requiring no standalone authorization code, the activation process allows you to
claim licenses and link the engine to your existing support accounts. Once
activation is complete, the system automatically creates your primary tenant,
allowing you to immediately begin associating firewalls and configuring your
on-premises or cloud-based directories.

To activate the Cloud Identity Engine, refer to the documentation
for the type of account you have and how you want to configure the Cloud Identity
Engine:

---

<a id="cie-first-time-cloud-identity-engine-activation-one-customer-support-portal-account"></a>

##### First time Cloud Identity Engine Activation - One Customer Support Portal Account

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine/activate-cie-first-time-one-csp>*

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have only one Customer Support Portal account.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

If you have only one Customer Support Portal account, follow these steps for first
time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select
   Activate.
2. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
3. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
4. Select a Region where you want to deploy your product.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.

   ![]()
6. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
7. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
8. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cie-first-time-cloud-identity-engine-activation-multiple-customer-support-portal-account"></a>

##### First time Cloud Identity Engine Activation - Multiple Customer Support Portal Account

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine/activate-cie-first-time-multiple-csp>*

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have multiple Customer Support Portal accounts.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

If you have multiple Customer Support Portal accounts, follow these steps for first
time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select Activate.
2. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
3. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. What is a tenant?

   1. If you need just one tenant, use or rename the tenant provided. The
      name provided matches your Customer Support Portal account for
      convenience.

      ![]()
   2. (Optional) This step applies if you are a managed security
      service provider (MSSP), a distributed enterprise customer, or need
      multiple tenants. After you create the first tenant, you can
      Allocate to subtenant and use or rename the
      tenant provided.

      ![]()

      A subscription gets allocated on a tenant or a sub-tenant. This step
      is for choosing a tenant where you want to allocate a license, not
      for building a complete tenant hierarchy. You can create only a
      tenant and subtenant here, and you can choose to allocate a license
      to that subtenant.

      After activation, you can build out your tenant hierarchy as needed
      through tenant management. You can create your tenant hierarchy to
      reflect your existing organizational structure. You can also
      consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      tenant hierarchy.

      After you create a tenant hierarchy, you can [share a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine/share-cie-subscriptions.html).
   3. Select Done.
4. Select a Region where you want to deploy your product.
5. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
7. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
8. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cie-return-visit-cloud-identity-engine-activation"></a>

##### Return Visit Cloud Identity Engine Activation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine/activate-cie-repeat-visits>*

Learn how to activate your Cloud Identity Engine for repeat visits.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or tenant management, and you are returning to activate
another product in your existing hierarchy.

1. From the Activation Console, select Activate.
2. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
3. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
4. Select a Region where you want to deploy your product.
5. **Agree to the terms and conditions**, and **Activate**.
6. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
7. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
8. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cie-share-cloud-identity-engine"></a>

##### Share Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine/share-cie-subscriptions>*

Learn how to share Cloud Identity Engine (CIE) on tenants through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

After you activate Cloud Identity Engine on a tenant and add child tenants, you can
share (CIE) with the child tenants in your hierarchy.

Regardless if you activate a new CIE instance on an existing tenant with existing
Prisma Access or you activate a new CIE instance on a new tenant, you
can share CIE under the following circumstances:

- Share CIE from a parent tenant during a new Prisma Access
  activation

  ![]()
- Share CIE from a parent tenant during the Prisma Access edit
  operation
- Share CIE to a child tenant that is not already running CIE
- Share CIE to a child tenant that is in the same region as the parent

If you don't have access to a parent tenant, the sharing option is not displayed. The
parent can control which child can have access to see CIE sharing through Identity
& Access Management [Roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions).

1. Use one of the various ways to access Tenant
   Management.
2. Search or scroll to find the parent tenant where CIE is activated, and select
   **Actions > Manage Sharing**.

   ![]()
3. Select which tenants to share CIE:

   ![]()

   - All — share CIE with all the child tenants.
   - Share — individually select the check box for
     each child tenant to share CIE.
4. Save.

---

<a id="cie-manage-cloud-identity-engine-app-roles"></a>

#### Manage Cloud Identity Engine App Roles

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/manage-cloud-identity-engine-app-roles>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console | - Customer Support Portal account |

App roles determine the privileges that users have and how they can use the Cloud Identity Engine
app. For more information on roles, refer to the [Common Services](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) documentation. To configure a
role:

1. Select Common ServicesIdentity & Access.
2. Select the tenant containing the user whose role you want to assign.
3. Select a user and click Assign Roles or if the user already has a role,
   click Add Another.
4. Select Cloud Identity Engine from the list of All Apps &
   Services.
5. Based on the user’s access needs, select the appropriate Role for the
   user from the following table:

|

Role | Description |

| --- | --- |

|  |  |
| --- | --- |
|

Deployment Administrator | This role provides access to deployment functionality and view-only access to other functions. This role allows users to view directory summary data but they can't view or query detailed directory data. |

|

Multitenant Superuser | This role provides full viewing and editing privileges for all functions for all tenants in a multitenant hierarchy. Assign this role only to users or service accounts who need unrestricted access to the Cloud Identity Engine. |

|

Superuser | This role provides full viewing and editing privileges for all available functions system-wide. It includes all privileges for all other roles. Assign this role only to users or service accounts who need unrestricted privileges. |

|

Vault View Only Administrator | This role provides read-only access to Cloud Identity Engine vault functionality. It allows administrators to view vault configurations, secrets metadata, and policies without modification capabilities. |

|

Vault Administrator | This role provides full read and write access to Cloud Identity Engine vault functionality. It enables administrators to manage vault configurations, secrets, policies, and access controls. |

|

View Only Administrator | This role allows users to view all available data for the tenant in the Cloud Identity Engine, including detailed directory data. |

If a user has multiple roles in the hub, the user is granted the
same privileges for the role that allows all granted privileges for all of the user's
roles.

For example, if a user has the View Only Administrator role and the Deployment
Administrator role for the Cloud Identity Engine, the Deployment Administrator role
grants management privileges without the ability to view or query detailed data,
while the View Only Administrator role grants privileges to view all Cloud Identity
Engine data, including detailed data. To allow the privileges granted by both of
these roles, a user who has both of these roles is granted the same privileges as a
user with the Superuser role, which allows full viewing and editing privileges.

---

<a id="cie-configure-the-cloud-identity-engine-visibility-scope"></a>

#### Configure the Cloud Identity Engine Visibility Scope

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/configure-the-cloud-identity-engine-visibility-scope>*

Learn about the Visibility Scope for the Cloud Identity Engine and how to configure
it.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

An individual firewall that you associate with the Cloud Identity Engine can belong
to a Customer Support Portal ([CSP](https://docs.paloaltonetworks.com/vm-series/9-1/vm-series-deployment/license-the-vm-series-firewall/create-a-support-account)) account as well as a Tenant Service
Group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants)). There is a one-to-many relationship
between CSP accounts and TSGs. This means that a single CSP account can have many
associated TSGs.

When you use the Cloud Identity Engine's Directory Sync or Cloud Authentication
Service, your firewall can view and connect to all tenants associated with your CSP
account. To isolate firewalls and ensure a particular firewall is only associated
with and can only view specific tenants, you can configure the Visibility Scope.

When you configure the Visibility Scope, you can configure each tenant for CSP
visibility or TSG visibility. When you configure a tenant for CSP visibility, that
tenant is visible and available to firewalls that are a member of any TSG within
that CSP account. If you configure a tenant for TSG visibility, the tenant is only
visible and available to firewalls associated with that TSG.

![]()

In the diagram above, there are two firewalls (Firewall\_1 and Firewall\_2), each with
a different configuration. Visibility and availability depends on the Visibility
Scope for the tenant. In this example, there are two TSGs (TSG\_1 and TSG\_2) within a
single CSP account (CSP\_1). Each tenant has its own Cloud Identity Engine instance.
Both firewalls are associated with CSP\_1.

One of the firewalls is associated with TSG\_1 and the other firewall is associated
with TSG\_2. In this example, the Cloud Identity Engine instance for TSG\_1 uses the
CSP Visibility Scope and the instance for TSG\_2 uses the TSG Visibility Scope. As a
result, on Firewall\_1, only the instance for TSG\_1 is visible. This is because
Firewall\_1 is associated with TSG\_1 and TSG\_2's Visibility Scope is configured so
that only firewalls associated with TSG\_2 can view and select Firewall\_2.

Firewall\_2 has visibility for both the Cloud Identity Engine instance for TSG\_1 and
the instance for TSG\_2. This is because although Firewall\_2 is associated with
TSG\_2, TSG\_1's Visibility Scope is configured for CSP visibility, so any firewall
associated with the CSP account can view and select Firewall\_1.

1. If you have not already done so, associate your tenant with a device.
2. Log in to the Cloud Identity Engine and select
   Settings.

   ![]()
3. Select the scope type you want to use for the Cloud Identity Engine.

   - TSG— The Cloud Identity Engine tenant is only
     visible and available to firewalls associated with the current tenant.

     Due to recent security enhancements,
     for a Panorama that manages Prisma Access in the same TSG as the
     Cloud Identity Engine (particularly if the visibility scope is TSG),
     you must associate your applications so that Panorama can access
     data from the Cloud Identity Engine.
   - CSP—The tenant is visible and available to
     firewalls that are a member of any tenant within the current CSP
     account.

   If you use Panorama to manage Prisma Access in the
   same tenant service group (TSG) as the Cloud Identity Engine, associate
   Panorama with the Cloud Identity Engine to ensure that Panorama and Prisma
   Access can access the Cloud Identity Engine (for more information, refer to
   User Context, step 1). This a requirement if you select
   TSG as the Scope Type.

   ![]()
4. Save your changes.

   ![]()

---

<a id="cie-get-started-with-cloud-identity-engine-1"></a>

## Get Started with Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/activation-and-onboarding>*

How to get started with the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Welcome to the Cloud Identity Engine! The Cloud Identity Engine provides a centralized,
cloud-native source of truth for user identity and authentication, enabling your
organization to move toward a Zero Trust security posture. By aggregating and
normalizing identity data from on-premises, cloud-based, and hybrid infrastructures, the
service allows you to enforce consistent security policies based on users and groups
rather than IP addresses,. This ensures that security decisions remain accurate and
effective across data centers, campuses, public clouds, and remote user
environments.

Deployment begins with planning your architecture, specifically selecting the appropriate
region to ensure compliance with data residency regulations and defining the visibility
scope to control firewall access to your tenants. Next, you activate the service within
the Palo Alto Networks Hub to provision your tenant and prepare for synchronization. You
then set up your identity sources by installing the Cloud Identity Agent for on-premises
directories or establishing secure API connections for cloud-based providers like
Microsoft Entra ID and Okta. Finally, you associate the Cloud Identity Engine with your
Palo Alto Networks applications, such as Prisma Access or Next-Generation Firewalls, to
enable them to consume identity data for policy enforcement.

---

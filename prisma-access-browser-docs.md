# Prisma Access Browser — Documentation

> Extracted from https://docs.paloaltonetworks.com/prisma-access-browser and all child pages on 2026-06-27.  
> 133 pages. Images/links use absolute URLs on docs.paloaltonetworks.com.

## Table of Contents

- [Activate New Prisma Browser with Prisma Access Enterprise Bundle License](#activate-new-prisma-browser-with-prisma-access-enterprise-bundle-license)
  - [Activate New Prisma Browser with Prisma Access Enterprise Bundle License](#activate-new-prisma-browser-with-prisma-access-enterprise-bundle-license-1)
    - [Cloud Managed Prisma Browser Bundle License](#cloud-managed-prisma-browser-bundle-license)
    - [Panorama Managed Prisma Browser Bundle License](#panorama-managed-prisma-browser-bundle-license)
  - [Activate Standalone Prisma Browser License](#activate-standalone-prisma-browser-license)
  - [Prisma Browser Connector for Secure Access to Private Apps](#prisma-browser-connector-for-secure-access-to-private-apps)
  - [Onboard the Prisma Browser](#onboard-the-prisma-browser)
  - [Assign Prisma Browser Roles](#assign-prisma-browser-roles)
- [Prisma Browser Administration](#prisma-browser-administration)
  - [Use the Prisma Browser Dashboards](#use-the-prisma-browser-dashboards)
  - [Digest Prisma Browser Home Screen Highlights](#digest-prisma-browser-home-screen-highlights)
  - [Device Health](#device-health)
  - [Analyse Account Usage](#analyse-account-usage)
  - [Roaming Profiles: Ensuring a Consistent Browser Experience](#roaming-profiles-ensuring-a-consistent-browser-experience)
  - [Explore Prisma Browser Events](#explore-prisma-browser-events)
    - [Prisma Browser Investigations](#prisma-browser-investigations)
  - [Account Protection for the Prisma Browser](#account-protection-for-the-prisma-browser)
  - [Manage Prisma Browser Users](#manage-prisma-browser-users)
  - [Manage Configuration Versions (Draft Mode)](#manage-configuration-versions-draft-mode)
  - [Manage Prisma Browser Devices](#manage-prisma-browser-devices)
    - [Manage Prisma Browser Device Groups](#manage-prisma-browser-device-groups)
    - [Configure Prisma Browser Device Posture Attributes](#configure-prisma-browser-device-posture-attributes)
    - [Live Session Streaming](#live-session-streaming)
    - [Configure Prisma Browser Extension Posture Attributes](#configure-prisma-browser-extension-posture-attributes)
    - [Configure Prisma Browser Mobile Device Posture Attributes](#configure-prisma-browser-mobile-device-posture-attributes)
  - [Manage Prisma Browser Applications](#manage-prisma-browser-applications)
    - [Configure Native RDP/SSH](#configure-native-rdpssh)
  - [Manage Prisma Browser Extensions](#manage-prisma-browser-extensions)
  - [Manage Prisma Browser Policy Rules](#manage-prisma-browser-policy-rules)
    - [Manage Prisma Browser Access and Data Control Rules](#manage-prisma-browser-access-and-data-control-rules)
      - [Login Controls](#login-controls)
        - [Login Forms](#login-forms)
        - [Passkey Login](#passkey-login)
    - [Manage Prisma Browser Security Rules](#manage-prisma-browser-security-rules)
    - [Manage Prisma Browser Customization Rules](#manage-prisma-browser-customization-rules)
  - [Manage Prisma Browser Policy Profiles](#manage-prisma-browser-policy-profiles)
    - [Configure Prisma Browser Data Controls](#configure-prisma-browser-data-controls)
      - [Configure Data Leak Prevention](#configure-data-leak-prevention)
      - [Configure Malware Protection](#configure-malware-protection)
      - [Live Page Scanning](#live-page-scanning)
      - [Webpage Element Removal](#webpage-element-removal)
    - [Configure Prisma Browser Browser Security Controls](#configure-prisma-browser-browser-security-controls)
      - [Configure Browser Session](#configure-browser-session)
      - [Configure Browser Hardening](#configure-browser-hardening)
      - [Configure Saved Data](#configure-saved-data)
      - [Configure Network Protection](#configure-network-protection)
      - [Configure Extensions](#configure-extensions)
      - [Configure Internet Explorer Compatibility Mode](#configure-internet-explorer-compatibility-mode)
      - [Configure Printers](#configure-printers)
      - [Configure Privacy](#configure-privacy)
      - [Configure Protected Browsing](#configure-protected-browsing)
    - [Configure Prisma Browser Browser Customization Controls](#configure-prisma-browser-browser-customization-controls)
      - [Configure Branding](#configure-branding)
      - [Configure Autonomous Digital Experience Management (ADEM)](#configure-autonomous-digital-experience-management-adem)
      - [Configure Customization](#configure-customization)
      - [Configure Routing](#configure-routing)
      - [Configure New Tab and Home Page](#configure-new-tab-and-home-page)
      - [Configure Upgrade Management](#configure-upgrade-management)
    - [New Tab Page](#new-tab-page)
  - [Manage Prisma Browser Sign-in Rules](#manage-prisma-browser-sign-in-rules)
  - [Manage Prisma Browser Requests to Bypass Policy Rules](#manage-prisma-browser-requests-to-bypass-policy-rules)
  - [Manage Rollback Control for the Prisma Browser](#manage-rollback-control-for-the-prisma-browser)
  - [Prisma Browser Remote Connections](#prisma-browser-remote-connections)
  - [Prisma Browser Self-Protection for Windows](#prisma-browser-self-protection-for-windows)
  - [Prisma Browser Guest Mode](#prisma-browser-guest-mode)
  - [The Prisma Browser Enterprise Password Manager](#the-prisma-browser-enterprise-password-manager)
  - [Location-based Policy](#location-based-policy)
  - [The Prisma Browser Extension](#the-prisma-browser-extension)
    - [Prisma Browser Extension History Collection](#prisma-browser-extension-history-collection)
    - [Prisma Browser Extension - Best Practices](#prisma-browser-extension-best-practices)
    - [Prisma Browser Extension Bulk Extension ID Import](#prisma-browser-extension-bulk-extension-id-import)
  - [File Types per Category](#file-types-per-category)
- [Deploy the Prisma Browser via MDM](#deploy-the-prisma-browser-via-mdm)
  - [Deploy the Prisma Browser via MDM](#deploy-the-prisma-browser-via-mdm-1)
    - [Deploy Prisma Browser Using Jamf](#deploy-prisma-browser-using-jamf)
    - [Deploy Prisma Browser Using Intune](#deploy-prisma-browser-using-intune)
    - [Deploy Prisma Browser Using Workspace ONE](#deploy-prisma-browser-using-workspace-one)
    - [Deploy using IGEL](#deploy-using-igel)
    - [Deploy using Linux](#deploy-using-linux)
  - [Installers and Updates](#installers-and-updates)
    - [Windows Deployment](#windows-deployment)
    - [macOS Deployment](#macos-deployment)
    - [IGEL Deployment](#igel-deployment)
    - [Linux Deployment](#linux-deployment)
  - [Prisma Browser for Mobile](#prisma-browser-for-mobile)
    - [Prisma Browser for Mobile Setup Using Intune](#prisma-browser-for-mobile-setup-using-intune)
  - [Deploy the Prisma Browser Extension](#deploy-the-prisma-browser-extension)
    - [Prisma Access Browser Extension Auto Login](#prisma-access-browser-extension-auto-login)
    - [Removing the Prisma Browser Extension](#removing-the-prisma-browser-extension)
  - [Prisma Browser End-of-Life Policy](#prisma-browser-end-of-life-policy)
  - [Prisma Browser Localization Guide](#prisma-browser-localization-guide)
  - [Prisma Browser Guide to Performance and Security Exclusions](#prisma-browser-guide-to-performance-and-security-exclusions)
  - [Privacy Datasheet](#privacy-datasheet)
  - [Troubleshoot the Prisma Browser](#troubleshoot-the-prisma-browser)
    - [Overview: What is the Prisma Browser?](#overview-what-is-the-prisma-browser)
    - [Prisma Browser Prerequisites](#prisma-browser-prerequisites)
      - [UK Region](#uk-region)
      - [AU Region](#au-region)
      - [CA Region](#ca-region)
      - [Domains to Allow-CH](#domains-to-allow-ch)
      - [EU Region](#eu-region)
      - [FedRAMP Moderate](#fedramp-moderate)
      - [IN Region](#in-region)
      - [ID Region](#id-region)
      - [JP Region](#jp-region)
      - [SGP Region](#sgp-region)
      - [US Region](#us-region)
    - [Roaming Profiles: Ensuring a Consistent Browser Experience](#roaming-profiles-ensuring-a-consistent-browser-experience-1)
    - [Certificate-Based Enforcement](#certificate-based-enforcement)
    - [Cloud Storage Integrations](#cloud-storage-integrations)
      - [Cloud Provider - Google Drive](#cloud-provider-google-drive)
      - [Cloud Provider - Microsoft OneDrive](#cloud-provider-microsoft-onedrive)
    - [First-Party Integrations](#first-party-integrations)
      - [Enterprise Data Loss Prevention](#enterprise-data-loss-prevention)
      - [File Handling and Analysis in Advanced WildFire](#file-handling-and-analysis-in-advanced-wildfire)
      - [IP-Based Enforcement Using an Authentication Gateway](#ip-based-enforcement-using-an-authentication-gateway)
    - [How Is Synched Data Stored?](#how-is-synched-data-stored)
    - [Integrate Prisma Browser and Okta with the Device Posture Provider](#integrate-prisma-browser-and-okta-with-the-device-posture-provider)
    - [IP Based Enforcement](#ip-based-enforcement)
    - [Third-Party Integrations](#third-party-integrations)
      - [Enforce Prisma Access Browser Mobile Access on Managed Devices Using MDM App Configuration](#enforce-prisma-access-browser-mobile-access-on-managed-devices-using-mdm-app-configuration)
      - [Integrate Prisma Browser with CrowdStrike Falcon Intelligence](#integrate-prisma-browser-with-crowdstrike-falcon-intelligence)
      - [Integrate Prisma Browser with Google Workspace](#integrate-prisma-browser-with-google-workspace)
      - [Integrate Prisma Browser with Microsoft 365](#integrate-prisma-browser-with-microsoft-365)
      - [Integrate Prisma Browser with Microsoft Information Protection](#integrate-prisma-browser-with-microsoft-information-protection)
      - [Integrate Prisma Browser with OPSWAT MetaDefender](#integrate-prisma-browser-with-opswat-metadefender)
      - [Integrate Prisma Browser with Votiro](#integrate-prisma-browser-with-votiro)
      - [Windows Account Based SSO Authentication](#windows-account-based-sso-authentication)
    - [Captive Portal Experience](#captive-portal-experience)
    - [Set Up and Use the Prisma Browser](#set-up-and-use-the-prisma-browser)
    - [Use the Prisma Browser Control Pane](#use-the-prisma-browser-control-pane)
    - [Prisma Browser User Guide Overview](#prisma-browser-user-guide-overview)

---

# Prisma Access Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser>*

---

<a id="activate-new-prisma-browser-with-prisma-access-enterprise-bundle-license"></a>

## Activate New Prisma Browser with Prisma Access Enterprise Bundle License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding>*

Learn how to activate your Cloud Managed or Panorama Managed Prisma Access Secure Enterprise Browser
(Prisma Browser) with Prisma Access bundle license through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Panorama | - Activation link for your product - Strata Logging Service (SLS) is needed for   activation - Cloud Identity Engine (CIE) is included and spun up   during activation - Customer Support Portal account |

See the [prerequisites](https://docs.paloaltonetworks.com/prisma-access-browser/getting-started/prisma-access-browser-prerequisites.html) before you begin this
task.

- [Cloud](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-cloud-managed-prisma-access-browser-bundle-license.html#cloud-managed-pab)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-panorama-managed-prisma-access-browser-bundle-license.html#panorama-managed-pab)

## Cloud Managed Prisma Browser Bundle License

Learn how to activate your Cloud Managed Prisma Access Secure Enterprise Browser (Prisma Browser)
tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons),
   [allocating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access),
   and [planning service connections](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access).
3. Continue to Assign the Prisma Access Secure Enterprise Browser Licenses and Add-ons.
   Products or Add-ons are
   enabled by default based on your contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.

   This is similar to [allocating PA Mobile User
   licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access). You will be able to partially allocate and activate
   Prisma Browser licenses across multiple Prisma Access tenants. For
   example:

   - You can purchase 5,000 units of Prisma Browser
     Enterprise Mobile Users.
   - You can allocate:

     - 1,000 to a PoC tenant (this is the minimum quantity
       required)
     - 3,000 to a production tenant
     - Leave 1,000 units unactivated for later use
5. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
6. (Optional) Assign roles so your admins can manage the Prisma Browser.

## Panorama Managed Prisma Browser Bundle License

Learn how to activate your Panorama Managed Prisma Access Secure Enterprise Browser (Prisma Browser) tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

Not available for Panorama multitenancy.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access (managed by
   Panorama) license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons).
3. Continue to enable the available add-ons. Products or
   Add-ons are enabled by default based on your
   contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.
5. In Panorama, go to the Panorama tabCloud Services PluginPrisma Browser tab.

   This launches a new tab with a pared-down version of Strata Cloud Manager
   that has just the Prisma Browser specific views.
6. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
7. (Optional) Assign roles so your admins can manage the Prisma Browser.

---

<a id="activate-new-prisma-browser-with-prisma-access-enterprise-bundle-license-1"></a>

### Activate New Prisma Browser with Prisma Access Enterprise Bundle License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license>*

Learn how to activate your Cloud Managed or Panorama Managed Prisma Access Secure Enterprise Browser
(Prisma Browser) with Prisma Access bundle license through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Panorama | - Activation link for your product - Strata Logging Service (SLS) is needed for   activation - Cloud Identity Engine (CIE) is included and spun up   during activation - Customer Support Portal account |

See the [prerequisites](https://docs.paloaltonetworks.com/prisma-access-browser/getting-started/prisma-access-browser-prerequisites.html) before you begin this
task.

- [Cloud](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-cloud-managed-prisma-access-browser-bundle-license.html#cloud-managed-pab)
- [Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-panorama-managed-prisma-access-browser-bundle-license.html#panorama-managed-pab)

### Cloud Managed Prisma Browser Bundle License

Learn how to activate your Cloud Managed Prisma Access Secure Enterprise Browser (Prisma Browser)
tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons),
   [allocating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access),
   and [planning service connections](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access).
3. Continue to Assign the Prisma Access Secure Enterprise Browser Licenses and Add-ons.
   Products or Add-ons are
   enabled by default based on your contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.

   This is similar to [allocating PA Mobile User
   licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access). You will be able to partially allocate and activate
   Prisma Browser licenses across multiple Prisma Access tenants. For
   example:

   - You can purchase 5,000 units of Prisma Browser
     Enterprise Mobile Users.
   - You can allocate:

     - 1,000 to a PoC tenant (this is the minimum quantity
       required)
     - 3,000 to a production tenant
     - Leave 1,000 units unactivated for later use
5. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
6. (Optional) Assign roles so your admins can manage the Prisma Browser.

### Panorama Managed Prisma Browser Bundle License

Learn how to activate your Panorama Managed Prisma Access Secure Enterprise Browser (Prisma Browser) tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

Not available for Panorama multitenancy.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access (managed by
   Panorama) license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons).
3. Continue to enable the available add-ons. Products or
   Add-ons are enabled by default based on your
   contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.
5. In Panorama, go to the Panorama tabCloud Services PluginPrisma Browser tab.

   This launches a new tab with a pared-down version of Strata Cloud Manager
   that has just the Prisma Browser specific views.
6. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
7. (Optional) Assign roles so your admins can manage the Prisma Browser.

---

<a id="cloud-managed-prisma-browser-bundle-license"></a>

#### Cloud Managed Prisma Browser Bundle License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-cloud-managed-prisma-access-browser-bundle-license>*

Learn how to activate your Cloud Managed Prisma Access Secure Enterprise Browser (Prisma Browser)
tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons),
   [allocating a Prisma Access license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access),
   and [planning service connections](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/plan-service-connections-cloud-managed-prisma-access).
3. Continue to Assign the Prisma Access Secure Enterprise Browser Licenses and Add-ons.
   Products or Add-ons are
   enabled by default based on your contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.

   This is similar to [allocating PA Mobile User
   licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access). You will be able to partially allocate and activate
   Prisma Browser licenses across multiple Prisma Access tenants. For
   example:

   - You can purchase 5,000 units of Prisma Browser
     Enterprise Mobile Users.
   - You can allocate:

     - 1,000 to a PoC tenant (this is the minimum quantity
       required)
     - 3,000 to a production tenant
     - Leave 1,000 units unactivated for later use
5. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
6. (Optional) Assign roles so your admins can manage the Prisma Browser.

---

<a id="panorama-managed-prisma-browser-bundle-license"></a>

#### Panorama Managed Prisma Browser Bundle License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-new-prisma-access-browser-with-prisma-access-enterprise-bundle-license/activate-panorama-managed-prisma-access-browser-bundle-license>*

Learn how to activate your Panorama Managed Prisma Access Secure Enterprise Browser (Prisma Browser) tenants through Common Services.

After you receive an email from Palo Alto Networks identifying the license you're
activating, use the activation link to begin the activation process.

Not available for Panorama multitenancy.

1. Select Activate Subscription in your email.

   ![]()
2. Follow the instructions for [activating a Prisma Access (managed by
   Panorama) license](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-panorama-managed-prisma-access-and-add-ons).
3. Continue to enable the available add-ons. Products or
   Add-ons are enabled by default based on your
   contract.
4. Select the Secure Enterprise Browser with Prisma Access
   Enterprise.
5. In Panorama, go to the Panorama tabCloud Services PluginPrisma Browser tab.

   This launches a new tab with a pared-down version of Strata Cloud Manager
   that has just the Prisma Browser specific views.
6. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
7. (Optional) Assign roles so your admins can manage the Prisma Browser.

---

<a id="activate-standalone-prisma-browser-license"></a>

### Activate Standalone Prisma Browser License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/activate-standalone-prisma-access-browser-license>*

Learn how to activate your Cloud Managed standalone Prisma Access Secure Enterprise Browser (Prisma Browser) with Prisma Access bundle license through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager | - Activation link for your product - Cloud Identity Engine (CIE) is included and   spun up during activation - Customer Support Portal account |

See the [prerequisites](https://docs.paloaltonetworks.com/prisma-access-browser/getting-started/prisma-access-browser-prerequisites.html) before you begin this
task.

After you receive a notification from Palo Alto Networks identifying the license
you're activating, use the activation link to begin the activation process.

![]()

1. Log in to the **Activate Subscription** window.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the 
   Superuser role.
2. Allocate the product to the Recipient of your
   choice.

   The name provided matches your Customer Support Portal account for
   convenience. You can use the name provided or change it.
3. Choose the data ingestion Region where you want to
   deploy your product.
4. Assign the Prisma Access Secure Enterprise Browser Licenses and Add-ons
   1. Select Prisma Access Secure Enterprise Browser.
   2. This is similar to [allocating PA Mobile User
      licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/allocate-licenses-cloud-managed-prisma-access). You will be able to partially allocate and activate
      Prisma Browser licenses across multiple Prisma Access tenants.
      For example:

      - You can purchase 1,000 units of Standalone Prisma Browser
      - You can allocate:

        - 200 to a PoC tenant (this is the minimum
          quantity required)
        - 600 to a production tenant
        - Leave 200 units unactivated for later
          use
5. Add [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)
   (formerly known as Cortex Data Lake) for storing tenant data such as
   configuration, telemetry logs, system logs, and stats. You can select an
   existing instance or create a new instance.
6. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.
7. Agree to the terms and conditions, and
   Activate.

   ![]()
8. Go to the Prisma Browser
   [Admin Guide](https://docs.paloaltonetworks.com/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards) to manage your Prisma Browser.
9. (Optional) Assign [roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) so your admins can manage the
   Prisma Browser.

---

<a id="prisma-browser-connector-for-secure-access-to-private-apps"></a>

### Prisma Browser Connector for Secure Access to Private Apps

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/onboard-the-prisma-browser-connector>*

Secure private applications on remote, unmanaged devices with Prisma Browser
Connector, by allowing Prisma Browser to seamlessly connect to Data Centers using
ZTNA-Connectors.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Browser Standalone | - Prisma Browser Standalone license - Prisma Browser Connector dd-on license - Prisma Browser Connector - Network Administrator or Superuser role. |

Prisma® Browser Connector integrates Prisma Browser with ZTNA Connector to
provide secure access to private applications. This feature simplifies private
application access for remote unmanaged devices with new or existing Prisma Browser Standalone deployments or existing Next Generation Firewall
(NGFW) customers by eliminating the need for a full Prisma Access deployment. It
offers a streamlined, secure channel for private application traffic, focusing on
ease of use and integration within your network. 

![]()

The Prisma Browser Connector leverages the Prisma Browser as a client-side
endpoint and a ZTNA Connector virtual machine (VM) in your private network.

#### Connection Protocols

The Prisma Browser Connector supports the following connection protocols:

- MASQUE
- HTTP 2
- HTTP 1.1

The Prisma Browser Connector establishes a secure and efficient connection
using the MASQUE (QUIC) Protocol. If the QUIC protocol is unavailable or blocked
in transit, then it falls back to HTTP2 automatically.

The process involves:

- **Automated Connection and Orchestration**: The Prisma Browser
  Connector and MASQUE Proxy work with Orchestration for ZTNA-C (Zero
  Trust Network Access Connector) to manage the connection.
- **Closest Region Selection**: The Prisma Browser Connector
  automatically selects the cloud region closest to where the
  ZTNA-Connector is deployed.
- **Connection Establishment**: The Prisma Browser establishes the
  connection, creating Automated Tunnels across the Internet to the
  selected worldwide data center location.

The Prisma Browser Connector supports secure access to both web-based
(HTTP/HTTPS) and non-web-based private applications (SSH/RDP). It is also able
to scale automatically to meet traffic needs.

The Prisma Browser Connector supports up to 10 ZTNA Connectors per deployment.
This allows you to manage the scope and resource allocation. For more
information, refer to [ZTNA Connection Requirements and
Guidelines](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/ztna-connector-requirements-and-guidelines). 

![]()

#### Deploy the Prisma Browser Connector for Private Application Access

This section provides the step-by-step instructions for configuring the Prisma
Browser Connector within the Strata Cloud Manager. This section describes:

- **Step 1:** User Onboarding
- **Step 2:** Private Application Setup
- **Step 3:** Enforce SSO Applications
- **Step 4:** Download and Distribute
- **Step 5:** Browser Policy

#### Step 1: User Onboarding

Onboard users and configure [Cloud Identity Engine (CIE)
integration](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance). This establishes the necessary user
authentication framework, allowing authorized users to access private
applications via the Prisma Browser.

If you have already completed user onboarding as part of
the regular Prisma Browser Standalone onboarding process, you can skip this
step.

1. Click the **Users** tab.
2. Select an [authentication profile](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile) from
   the **Cloud Identity Engine (CIE)**.
3. Specify the relevant **user groups** that will be granted access.

![]()

#### Step 2: Private Application Setup

Download and deploy the [ZTNA Connector](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/insights-scm/monitor-data-centers/monitor-data-centers-ztna-connectors). This initiates
the deployment and configuration process for the ZTNA Connector, which serves as
the secure gateway for private application access.

1. Click the **Private Applications** tab.

   ![]()
2. Click **Deploy**
   **ZTNA Connectors.** This section defines the infrastructure and specific
   private applications that the ZTNA Connector manages. In the dropdown
   section, click “Follow the setup instructions in the **ZTNA Connection
   Configuration."** Go to [Configure ZTNA Connector](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/configure-a-ztna-connector)
   for more information. 

   ![]()

   When you configure Target Apps in the ZTNA
   Connector, you must add them to the Prisma Browser Application page as
   well. Apps added on IP Subnets are not currently supported on Prisma
   Browser.
3. Open the Prisma Browser Applications page (ConfigurationPrisma BrowserApplications and select the **Private Applications** tab. This allows
   you to define **application targets** using FQDNs, and wildcards. These
   targets specify the internal private applications (web or non-web) the ZTNA
   Connector will make accessible to Prisma Browser users.

   Applications added to the ZTNA Connector must also
   be added to the Prisma Browser in the Applications page.

   Public apps configured as Private apps are not
   supported.

   1. Click **Add private app**, and enter the required information.
      For more information, refer to [Add a Private
      Application](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-applications?otp=task-iq1_skt_fcc#task-iq1_skt_fcc). 

      ![]()
   2. Select the Non-web Apps tab and click Add non-web App if you need to
      add apps that are SSH- or RDP-based. This extends secure access
      capabilities beyond web-based applications to include other crucial
      enterprise services.

      ![]()

The remaining steps are configured in a manner similarly to thoes in the Prisma
Browser Onboarding. Refer to the following steps:

- [Enforce SSO
  applications](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding?otp=task-brr_td4_gcc#task-brr_td4_gcc)
- [Download and distribute](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding?otp=task-ebf_d24_gcc#task-ebf_d24_gcc)
- [Browser policy](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding?otp=task-hnh_bf4_gcc#task-hnh_bf4_gcc)

#### Validate Private Application Access with Prisma Browser

Once the Strata Cloud Manager is properly configured, your end-users can validate
private application access using the Prisma Browser.

#### Step 1: Log into the Prisma Browser

1. Open the Prisma Browser application.
2. Complete the SSO login process, which typically redirects through your
   configured CIE.§§§§§§§

#### Step 2: Access a Configured Private Web App

Access a configured private web application. This step verifies that web-based
private applications are correctly routed and accessible through the Prisma
Browser Connector infrastructure.

1. Navigate to the URL of a private web application (for example, WC app1
   van2 auto.com) within the **Prisma Browser**.
2. Confirm successful access and functionality of the application.

#### Step 3: Access a Configured Private Non-Web App

Access a configured private non-web application (for example, SSH) using remote
connections. This validates secure access to non-web services, demonstrating the
full capability of the Prisma Browser Connector for diverse application
types.

1. In the **Prisma Browser**, go to **Non-web connections**..
2. Select and connect to a configured private non-web application, such as
   an **SSH** server.
3. Provide any necessary credentials (for example, a **private key**)
   and confirm a successful connection.

#### Step 4: Check the Troubleshooting Page

Review the Prisma Browser troubleshooting page for proxy status and routing
details. This diagnostic step allows you to confirm that traffic is being
correctly proxied through the Prisma Browser Connector infrastructure and to
identify any potential routing issues.

1. In the **Prisma Browser** address bar, type prisma://troubleshoot and
   press **Enter**..
2. Review the **Prisma integration** page to verify the **proxy**
   status, type (for example, MASQUE), and confirm that traffic is routing
   over the **MASQUE** infrastructure for private applications. 

   ![]()

   ![]()

#### Known Limitations

The following are the known limitations of the Prisma Browser Connector:

1. Apps added via IP Subnets are currently not supported. They can only be
   defined using FQDNs and wildcards.
2. Public apps configured as Private apps are not supported.
3. Once a group, connector, or application is created, the IP blockers
   cannot be changed.
4. The system supports a limit of up to 10 ZTNA Connectors per tenant.
5. If the MASQUE (QUIC) is not available or blocked, the system defaults to
   HTTP2.
6. The system only supports RDP and SSH protocols for non-web apps.
7. Application targets must be defined using FQDNs or wildcards.
8. Some menus that are unavailable in **Prisma Browser** (but are
   available in **Prisma Access**) may still appear in the interface;
   however, these menus are not functional and should not be used.

---

<a id="onboard-the-prisma-browser"></a>

### Onboard the Prisma Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding>*

Learn how to onboard Prisma Access Secure Enterprise Browser (Prisma Browser) on the Strata Cloud Manager and integrate with Prisma Access.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager | - Prisma Access with Prisma Browser bundle   license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

See the [prerequisites](https://docs.paloaltonetworks.com/prisma-access-browser/getting-started/prisma-access-browser-prerequisites.html) before you begin this
task.

#### Onboard the Prisma Browser

Welcome to the Prisma Browser

Use the onboarding step-by-step wizard to configure the essential components of
Prisma Browser. The wizard guides you through each stage of the setup,
ensuring that both the admin and end users have a complete and functional basic
configuration.

The steps that you see in your tenant depends on your Prisma Browser license; not all the onboarding steps are available for all licenses.

Onboarding users depends on the browser license.

- If you have a **standalone licence**, then onboardiing includes 4
  steps:
  - Users
  - Enforce SSO applications
  - Download and Distribute
  - Browser PolicyIn all other cases, the steps will include Prisma Access
  Integration and Routing.

From the Strata Cloud Manager, select Configuration Onboarding.Configuration Onboarding

In the **Onboarding Users** section, select Prisma Browser and click
**view**

If you have a standalone license, Step 1 will open. Otherwise, the **Onboarding
with Strata Cloud Manager** page will open.

On the **Onboarding with Strata Cloud Manager** page, under **Onboard Users**,
locate Prisma Browser, and click **View**.

![]()

##### Step 1 - Users

The first part is to determine who can log into your browser, and how.

**Prerequisites**

Before completing this step, configure your Cloud Identity Engine (CIE). You
can either:

- Create a local CIE directory and manually onboard a few initial end
  users, or
- Connect your cloud or on-premises identity provider (IdP) to onboard
  users at scale.

Also, you need to configure an authentication profile to enable user access.

You can configure only one authentication
profile . If you use multiple identity providers (IdP), add them all to
the same profile. To do this, select **Authentication Mode:
Multiple** when setting up the authentication profile.

Define the user authentication method and onboard User groups.

1. From the drop-down, select the Authentication profile for the
   systems you plan to deploy. The choices are Prisma
   Browser and Prisma Browser Extension.
2. Choose one or more directories from the drop-down list/ For each
   selected directory, select the User groups that
   will be able to access the Prisma Browser.
3. The default primary Identification attribute is ***mail***
   (email addresses). If you're using UPN (User Principal Name) as your
   primary identifier, make sure that you set it to UPN. For more
   information, refer to [Manage Users](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-users).
4. Next: Prisma Access Integration.

   ![]()

##### Step 2 - Prisma Access Integration

1. Enable external connectivity to Prisma Access.
   1. Review the [**Explicit Proxy Review
      Guidelines**](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/explicit-proxy-guidelines#idcc79d0d3-f7f8-4895-acfa-5a0242b5f39e).
   2. Go to the [**Set Up Explicit Proxy
      page**](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy/set-up-explicit-proxy).
   3. Select the tab for the **Strata Cloud Manager**.
   4. Complete steps **1**- **3**.
   5. Enable the Prisma Browser.
   6. Push configuration to deploy login.
   7. Done
2. Enable the Prisma Browser in the Prisma Access Security
   policy.
   1. Click Explicit Proxy settings.
   2. Add a rule that allows web traffic in your Security policy.
   3. Push configuration to accept the rule.
   4. Done.
3. Create a service connection.
   1. Click Service connection.
   2. This takes you to the **Add Service Connection** page.
   3. Done.
   4. Next: Routing.

      ![]()

##### Step 3 - Routing

The Routing control enables you to manage the way that the Prisma Browser
handles network traffic. This feature sets up the default configuration for
Prisma Browser. If you need to adjust the granularity of the control
for a specific rule, refer to Browser Customization Controls for [traffic flows](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization.html?otp=task-qmp_thr_hcc#task-qmp_thr_hcc) .

1. Choose one of the following Traffic Control options:

   If all browser traffic is configured to be
   routed through Prisma Access, this configuration is
   ignored.

   - Only route private application traffic through Prisma
     Access.
   - Route all traffic through Prisma Access.
   - Don’t route traffic through Prisma Access.

     Mobile Devices:
     To ensure an optimal experience with Network Detection and
     Prisma Access, either route only Private App traffic, or
     exclude the Mobile device group from routing.

   The Traffic Control option appears only
   if the Prisma Access Licensing exists.
2. (Optional) Ensure that the Prisma Browser traffic flows in
   an optimal manner when the browser detects it's running within the
   internal network. This identification is based on establishing a
   connection with a host that is only available inside the internal
   network.
   - Enter the FQDN to resolve.
   - Enter the expected IP address.
3. Choose whether or not to identify the internal network by detecting if
   the GlobalProtect or the Prisma Access Agent is running on the
   device.
4. Choose whether or not to enable Agent Detection on your network.

   Agent Detection will detect that the device is
   on the internal network even if GlobalProtect or Prisma Access is
   not connected, as long as at least one of these applications is
   running.

   - **Toggle on** - Enable Agent Detection.
   - **Toggle off** - Disable Agent Detection.
   - Next: Enforce SSO applications

     ![]()

##### Step 4 - Enforce SSO Applications

It's important that the only way your users can authenticate on SSO-enabled
applications is by using the Prisma Browser. This will ensure that
external actors will have no access to your enterprise applications. Prisma
Browser offers you three ways to enforce your selected SSO option.

- Conditional access using your authentication proxy.
- Conditional access using device posture IdP (Okta).
- Conditional access using certificates (Google workspace).

Prisma Browser supports the following IdPs:

- Okta
- Microsoft Azure Active Directory
- PingID
- OneLogin
- VMware workspace ONE Access

1. When you configure your local settings, be sure to take note of the
   egress IP addresses.
2. Next: Download and distribute.

   ![]()

##### Step 5 - Download and Distribute

You can download the Prisma Browser
installation files to test on your own device before sending it out to your
users. Once you're satisfied with your tests, you can download the relevant
installer to be distributed by your mobile device management (MDM) application.

You can download the Prisma Browser installation files to
test on your own device before sending it out to your users. Once you're
satisfied with your tests, you can download the relevant installer to be
distributed by your mobile device management (MDM) application.

You can also send your users the download link so that they can
download the Prisma Access Browser on their own. This is a single link for
macOS, Windows and Linux users only.

1. Select from the available options:
   - Desktop:
     - macOS
     - Windows
     - Linux
       - Fedora
       - Ubuntu
   - Mobile:
     - iOS
     - Android

   You can also send your users the download link so that they can
   download the Prisma Browser on their own. This is a single link
   for macOS, Windows, and Linux users only.

   If you send your users the download link,
   remind them that they can only log in with the email that is
   configured in the IdP service.
2. Prisma Browser for IGEL is deployed via the
   [IGEL App Portal](https://app.igel.com/) only.
3. Next: Browser Policy

   ![]()

##### Step 6 - Browser Policy

You can now begin to explore and configure the Prisma Browser Policy Engine to create a safe and secure user environment.

1. Select Browser Policy.
2. This directs you to ConfigurationPrisma BrowserPolicyRules.
3. Manage Prisma Browser
   [Policy Rules](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html).

   ![]()

#### New Onboard Users

The Onboarding workflow is a configurable series of windows displayed
when a new end user starts using the browser.

Based on the IT needs and requirements, you can select up to eight
individual pages that allow the end users to customize the browser with their
pictures and bookmarks, and to find out some basic information about the browser
– a sort of “Quick-Start” guide.

The Onboarding Wizard customization control configures the onboarding
workflow. You can select which windows will be displayed in your network.

You configure this in ManageConfigurationPrisma Access BrowserPolicyProfiles when you create or edit a Browser
Customization profile and choose Onboarding
Wizard. For configuration details, see the Browser Customization
Controls for the [Onboarding Wizard](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization.html?otp=task-ccn_fgr_hcc#task-ccn_fgr_hcc).

You configure this in ConfigurationPrisma BrowserPolicyProfiles when you create or edit a Browser
Customization profile and choose Onboarding
Wizard. For configuration details, see the Browser Customization
Controls for the [Onboarding Wizard](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization.html?otp=task-ccn_fgr_hcc#task-ccn_fgr_hcc).

#### Onboard Local Users

You can create a special **CIE directory** in the Cloud Identity Engine. This
feature enables you to create a system where the time from adding users to their
ability to log in to the browser with a password is a few minutes.

The CIE directory only supports a single *Auth
Profile* . This means that if you use a CIE directory, you can’t also
use your regular IdP at the same time. Innovation

This feature is mainly used when
starting a POC to avoid waiting for your IT department to integrate your
IdP.

---

<a id="assign-prisma-browser-roles"></a>

### Assign Prisma Browser Roles

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles>*

Learn which RBAC roles and privileges are available for (Prisma Browser)
administrators.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager | - Prisma Access with Prisma Browser bundle license or Prisma Browser standalone license - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Multitenant   Superuser or Superuser with access to the [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

You can create and manage role-based access control for different types of administrators
of the Prisma Browser. This allows the main administrator in a large organization to
appoint additional administrators with relevant permissions for their specific roles,
including visibility and access.

After activating your Prisma Access Browser license, you can manage admin user access and
assign one of the following roles that are specific to Prisma Browser.

|

Enterprise Roles | Permissions |

| --- | --- |

|  |  |
| --- | --- |
|

Prisma Browser Access & Data Administrator | Read-write access:  - setting and managing access and data policies - defining custom and private applications - handling end user requests related to policies  Read-only permission to inventory aspects:  - users - devices - extensions - applications - any visibility aspects within the Prisma Browser management   section:   - dashboards   - end-user events |

|

Prisma Browser Customization Administrator | Read-write access to set and manage browser customization policies. Read-only permission to inventory aspects:   - users - devices - extensions - applications - any visibility aspects within the Prisma Browser management   section:   - dashboards   - end-user events |

|

Prisma Browser Permission Request Administrator | Read write access to handle end user requests related to policies. Read-only permissions to visibility aspects within the Prisma Browser management section"  - dashboards - end-user events |

|

Prisma Browser Security Administrator | Read-write access to set and manage browser security policies. Read-only permission to inventory aspects:   - users - devices - extensions - applications - any visibility aspects within the Prisma Browser management   section:   - dashboards   - end-user events |

|

Prisma Browser Security & Device Posture Administrator | Read-write access to  - set and manage browser security policies - manage device posture groups - set sign-in rules   Read-only permission to inventory aspects:   - users - devices - extensions - applications - any visibility aspects within the Prisma Browser management   section:   - dashboards   - end-user events |

|

Prisma Browser View Only Analytics | Read-only permission to inventory aspects:   - users - devices - extensions - applications - any visibility aspects within the Prisma Browser management   section:   - dashboards   - end-user events |

---

<a id="prisma-browser-administration"></a>

## Prisma Browser Administration

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration>*

---

<a id="use-the-prisma-browser-dashboards"></a>

### Use the Prisma Browser Dashboards

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/use-the-prisma-access-browser-dashboards>*

Learn how to use the Prisma Browser dashboards to monitor browser users and
devices.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser dashboards deliver real-time, relevant data, and metrics for
various use cases, catering to the specific needs and interests of diverse user
groups. Use the dashboards to derive meaningful insights from the analysis of user
behavior and browsing data. There are a variety of dashboards for specific use cases
you might want to monitor, such as user behavior, data leak prevention, web
security, and policy. Each dashboard contains a collection of widgets and some of
the widgets appear in multiple dashboards.

To access the Prisma Browserdashboards:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser.

   By default, the Overview dashboard displays on the
   Home screen.

   You can also access the dashboards from DashboardsPrisma Browser. If the Prisma Browser
   dashboard is not showing, click More Dashboards and
   select it for display.

   ![]()
2. To add additional Prisma Browser dashboards to the display, click the
   + icon and select a dashboard to open in a new tab
   (up to a total of 12 tabs).

   In addition to the [Overview dashboard](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/monitor-prisma-access-browser-statistics.html) that
   displays by default, the following dashboards are available:
   - [Web security](#use-the-prisma-access-browser-dashboards_task-eng_hnj_hcc)
   - [Data leakage prevention](#use-the-prisma-access-browser-dashboards_task-gh2_2pj_hcc)
   - [Assets](#use-the-prisma-access-browser-dashboards_task-yf1_tsk_hcc)
   - [Policy](#use-the-prisma-access-browser-dashboards_task-n4v_l5k_hcc)
   - [User behavior](#use-the-prisma-access-browser-dashboards_task-xyn_xvk_hcc)

   You can open a total of 12 dashboard tabs, including opening multiple
   instances of the same dashboard.

   ![]()
3. Use the following dashboard features to perform deep dives and analyze
   information, data patterns, and user behavior.

   - **Filter by users or user groups**—Sometimes, you may want to examine
     data for specific entities, such as Users or
     User groups to see how they compare to the
     overall user data shown in the widget. This can help identify if a
     specific group is skewing the displayed data.
   - **Filter by time**—Select a different Time
     frame, ranging from the last 24 hours up to the last 30
     days. This allows you to investigate the behavior over time so that you
     can see trends in activity, fine-tune existing rules, and create new
     rules based on the information gleaned from the investigations. The
     default time frame for all dashboards except Web Security is 7 days; the
     default for the Web Security dashboard is 30 days.
   - **Look at raw data**—Many of the widgets provide links to the raw
     data for better data analysis and additional filtering options. Clicking
     the link takes you to the corresponding page in Strata Cloud Manager.

     ![]()

   Open multiple instances of the same
   dashboard and filter by a different set of users or time frames. You can tab
   between the dashboards to compare and analyze the different
   groupings.
4. (Optional) Adjust the widget layouts.

   The dashboard widgets have a flexible layout, allowing you to adjust the
   widget layout and order as needed. This is useful when the information you want
   to see isn't next to each other in the default tab layout. For example, if you
   want to examine the Top 10 most visited apps and websites and compare it to the
   Top 5 SaaS applications by user data volume. To move a widget:

   1. Hover over the title bar on the widget you want to move until the drag
      tool appears.
   2. Drag the widget to its desired location.

<a id="use-the-prisma-access-browser-dashboards_task-eng_hnj_hcc"></a>

#### Web Security Dashboard

The Prisma Browser Web Security dashboard displays the occurrence of issues
that are based on user access to web applications and websites and the related
information to help you asses and troubleshoot the issues. This dashboard
contains the following widgets:

- Top 10 most visited apps and websites
- Top 10 most visited web classifications, by events
- Allowed and Blocked access activities —Correlation
- Top 10 most active apps and websites (data focus)
- Top 5 SaaS applications by data volume
- Blocked access activities (Average and Median per user)

![]()

This dashboard shows a filtered view of events based on time, users, and user
groups. You can click directly from the dashboard to the corresponding Event log
entry. For example, if you click into the Top 5 SaaS applications by user data
volume widget, you can see a filtered view of the Events page as follows.

![]()

You can continue to drill-down from the Events page. For example, click on one of
the apps or websites listed in the widget to go to the Applications directory.
For example, if you click on Google Drive, you will see the following view:

![]()

<a id="use-the-prisma-access-browser-dashboards_task-gh2_2pj_hcc"></a>

#### Data Leakage Prevention Dashboard

This dashboard highlights events—primarily upload, download, cut, and copy
events—that could potentially lead to a data leakage. This dashboard contains
the following widgets:

- Data leakage prevention overview
- Top 10 most active apps and websites (data focus)
- Top 5 SaaS applications by user data volume
- File type distribution and data volume—File download by events
- File type distribution and data volume—File upload by events

![]()

<a id="use-the-prisma-access-browser-dashboards_task-yf1_tsk_hcc"></a>

#### Assets Dashboard

The Assets dashboard provides details about the [devices](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html) and their [security posture](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html), [device groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#manage-prisma-access-browser-devices_task-hns_lt1_gcc), and device usage in your
enterprise browser environment. This dashboard contains the following
widgets:

- OS platform distribution by devices
- OS platform and violations correlation, by events
- Extensions installation method, by extensions
- Device type distribution, by devices
- Screen lock status breakdown, by devices
- Disk encryption status breakdown, by devices
- Firewall status breakdown, by devices
- EPP status breakdown by devices
- Top 10 device group distribution, by devices

![]()

<a id="use-the-prisma-access-browser-dashboards_task-n4v_l5k_hcc"></a>

#### Policy Dashboard

The Policy dashboard displays information about the different [policies](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html) and rules governing your Prisma Browser deployment. This dashboard contains the Top 5 most active
user defined rules widget, which lists the most active rules and details the
diffrence bettween active events and monitoring events.

![]()

<a id="use-the-prisma-access-browser-dashboards_task-xyn_xvk_hcc"></a>

#### User Behavior Dashboard

The User Behavior dashboard allows you to track and analyze the behavior or your
users. This dashboard contains the following widgets:

- Top 5 most active users
- Top 5 most active users (data focus)
- Top 5 users by data volume
- Allowed and blocked activities volumes (data focus)—Relative analysis

![]()

---

<a id="digest-prisma-browser-home-screen-highlights"></a>

### Digest Prisma Browser Home Screen Highlights

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/monitor-prisma-access-browser-statistics>*

Use the Prisma Browser Overview dashboard to deep dive into statistics about your
enterprise browser users and associated events.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser Overview dashboard serves as the landing page for the Prisma Browser administration. This dashboard gives you insights into the Prisma Browser users and devices, as well as events. From here, you can deep
dive into the data to investigate incidents and identify trends.

![]()

#### Monitor Users

The Users section displays a breakdown of active and inactive users.

- **Active users**—Users who have used the Prisma Browser during the
  selected Time frame. The displayed trend compares the
  number of Active users in the current Time frame with
  the number of Active users in the previous Time
  frame. As a result of this, the trend can fluctuate daily. An
  upwards trend is displayed in green, while a downward trend is displayed in
  red. 

  ![]()
- **Inactive users**—Users who have not used the Prisma Browser during
  the selected Time frame.

Expand the widget to show the Users directory page so that you can search for
specific users. From there, you can see which groups each user belongs to, which
devices belong to each user, and what policy rules associated with the user.

#### Monitor Devices

The Devices section displays the number of devices within your organization that
are using the Prisma Browser. You can see the breakdown of usage by
OS  or by Version. The
Version view indicates the devices with the latest
browser version, a maintained browser version, a browser version approaching
End-of-Life, and a browser version that has reached its end of life.

![]()

Click into the display to see a more detailed version of the information, along
with the ability to adjust the Time frame, and the
browser type (Desktop browser, Mobile browser). This provides a better view of
the trends. In addition, you can get a better image of when each browser version
expired. Upwards trends show in green, while a downward trend shows in red.
Click the icon to open the Devices directory so that you can search for specific
devices. You can drill down to see which device groups include the user.

![]()

#### Monitor Blocked Events

The Blocked events section displays a line chart showing the trend in blocked
events over all the users connected to the Prisma Browser. These events
include incidents and other policy-generated events within the specified
Time frame. Hover over the chart to see the number of
blocked events per day (or per hour in the case of 24-hour time frames). The
longer the time frame, the higher the granularity of the chart.

The displayed trend compares the number of blocked devices detected during the
current time frame with the number of blocked events detected during the
previous time frame. As a result, the trend can fluctuate. Upward trends show in
red and downward trends show in green.

Click the icon to open the Investigate Prisma Browser Events page, which
shows blocked and blocked encrypted events. You can use this to search for
specific blocked events. Use the Events log to filter and sort for different
parameters.

![]()

#### Monitor Events

The main section of the Overview dashboard displays
the Total Events from all Prisma Browser users. There are
four categories of events:

- **Access events**—Access events display the information regarding the
  applications/URLs that Prisma Browser users are using most.
- **Data events**—Data events display the information regarding the
  operations that Prisma Browser perform most on data, such as copy,
  paste, download, or print.
- **Posture events**—Represent non-compliant sign-in issues.
- **Incidents**—Represent malicious events. Click on an event to open the
  event log so you can see the type of event and the associated user.

You can deep-dive into the data for each type of event.

- Deep Dive into Access Events
  1. Select the Access category from the
     Total Events part of the screen.

     ![]()
  2. Click into one of the applications or URLs

     From here, you can see which users are having the most
     interactions with the selected application. 

     ![]()
  3. To see application events for a specific user in the Events log,
     click on the user name.

     To help you investigate access activities for the selected user,
     this view automatically filters on:
     - Time frame
     - Type, which includes the following additional filters:
       - Website access
       - Login attempts
       - Login failed
       - User
       - User
       - Application

     ![]()
- Deep dive into data events.
  1. Select the Data category from the
     Total Events part of the screen.

     ![]()
  2. Click into one of the data events.

     From here, you can see which users are using the selected data
     operation most frequently. 

     ![]()
  3. To see data events for a specific user in the Events log, click on
     the user name.

     ![]()
- Deep dive into posture events.
  1. Select the Posture category from the
     Total Events part of the screen and then
     click into one of the posture events.

     From here, you can see details about non-compliant sign-in events
     that Prisma Browser blocked based on the device group settings.

     ![]()
  2. To drill into specific posture events, select an OS platform and
     then select a particular user.

  To help you investigate posture events for the selected user, this view
  automatically filters on:
  - Time frame
  - Type: Non-compliant sign-in
  - User
  - OS platform

  ![]()

---

<a id="device-health"></a>

### Device Health

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/device-health>*

Device Health displays the issues with the device and its dependencies.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The **Device Health view** provides you with immediate visibility into the operational
state of individual devices across the organization. This centralized interface
consolidates critical diagnostics and posture data, enabling faster investigation and
resolution of device-related issues. By streamlining access to key metrics and device
status, the view helps reduce downtime and improve overall system reliability and
understanding.

#### Access the Device Health View

To view the health status of a specific device, follow these steps:

1. Open the Devices screen. 

   ![]()
2. **Search** for the specific device you want to inspect. You can use the
   filters to help in the search. For more information, see [Manage Prisma Access Browser Devices](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html).
3. Click the **Device record** to open the **Device Drawer view**. 

   ![]()
4. In the top-right corner of the drawer, click the three-dot menu (**⋮**),
   then select **Device health**. 

   ![]()
5. The **Device Health view** will open, displaying detailed information
   about the selected device. 

   ![]()

#### Dashboard Sections

#### Device Details

This section displays basic identification information for the device.

The Device Health dashboard contains the following information in the Device Details
section.

- **Device details** - Displays the basic identification information for
  the device.
  - **Hostname** - The name of the device.
  - **User** - The name of the user registered on the device.
  - **Status** - the current status of the device (offline, online).
- **Metadata** - Displays the different identifying information for the
  device.
- **Posture details** - This section provides insights into the device’s
  security posture and configuration. Some entries include an **(ℹ)** icon,
  indicating that additional information is available when you hover or
  click.
- **Diagnostics** - Displays the current status of all monitored services.
  This section helps identify operational issues quickly.

The following products do not
support the Device Health dashboard:

- Prisma Browser for Mobile
- Prisma Browser Extension (PABX)

You need to consider these limitations when planning
diagnostics.

#### Refresh the Display

Use the **Refresh** button located in the top-right corner of the screen to reload
the most recently received telemetry data. This feature is especially useful when
new metrics are available and you want to ensure the display reflects the latest
information.

![]()

The **Refresh** button does not request live data from
the device or endpoint. Instead, it reloads data that the device already sent based
on its preconfigured reporting cycle. If the device has not sent new data, the
information on the screen will stay the same.

---

<a id="analyse-account-usage"></a>

### Analyse Account Usage

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/analyse-account-usage>*

This is the information regarding Account Usage.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama or Strata Cloud Manager) | - Security Administrator, Superuser, or Readonly roles within the   platform's Identity Management System. - Permission for viewing Analytics → Account Usage page, accessing   drilldown details, applying filters and sorting options. |

The Account Usage screen (account inventory) provides you with a centralized,
data-driven view of user identities and access patterns across the organization. It
aggregates successful login attempt events from Prisma Browser and Prisma Browser
Extension to offer a comprehensive understanding of user access in your environment.

Account Usage is a proactive tool for identifying and addressing key security
vulnerabilities, such as:

- Shadow IT
- Non-SSO usage
- Shared accounts
- High-risk login behaviors

**Data Anonymization:** Usernames are anonymized based on the
Activity Logging section in the Tracking. A username becomes visible only after it
appears in a non-anonymized form in a system event. Anonymization can be controlled in
the **Tracking** section of each rule.

**Data Retention:** Account identifiers and basic metadata
are retained indefinitely. Event-based data, such as login activity and risk scores,
adhere to your organization's standard event retention policy. Associated activity and
risk data will no longer appear in the inventory once underlying events are
cleared.

#### Login Methods

The Account Inventory system recognizes the following login methods:

- **Form:** Login using a standard username/password login form.
- **Passkeys:** Login using the WeAuthN protocol (passkey).
- **SSO:** Login using a SAML-based Identity Provider.
- **Social:** Login using supported social login provide:
  - Google
  - Microsoft
  - Facebook
  - Apple
  - Github
  - LinkedIn
  - x (Twitter)
- OIDC SSO: Login using an OIDC-based identity provider.
  - In many cases social logins that are not in the supported list above
    will be categorized under this login method.
  - Many websites that seem to provide form-based login actually use
    OIDC SSO behind the scenes (e.g. government, healthcare and other
    similar websites).

##### Manage and Analyse User Accounts

From the Strata Cloud Manager, ConfigurationAnalyticsAccount Usage to open the Accounts Usage page. 

![]()

##### Spotlights

Spotlights allow you to quickly identify commpn security concerns. The following
Spotlights are available for Account Usage:

- **Non-SSO Accounts:** Accounts not protected by your primary Identity
  Providers.
- **Unknown App Accounts:** Accounts found on domains not currently in
  your application catalog.
- **Risky-App Accounts**: Accounts that use applications that are
  considered risky.
- **Risky Accounts**: Accounts that are considered risky based on
  established criteria.
- **Shared Accounts:** Identities used by more than one person.
- **GenAI Accounts:** Accounts on applications that use generative AI.

  ![]()

##### Filter and Sort Account Data

**Main table columns:** 

- **Account Username / Account Application:**  These are presented in a
  single cell. The Account Username is the username or unique identifier
  of the user. The account Application is the catalog or custom
  application, including GenAI tags and Application Risk indicators. Hover
  over the field to see all the information.

  ![]()
- **Account URL:** The URL of the page on which the login occurred.
- **Identity Provider:**  The type and URL of the identity provider
  used to login to the account (for SSO, OIDC SSO and Social login
  methods).
- **User:**  The PB users that logged into this account (Note:
  Currently limited to 100 users for a shared account, open the drawer to
  see the rest of the users).
- **Device:**  The devices on which this account was accessed.
- **Login Activity:**  Total successful logins in the selected
  timeframe, with a trend arrow compared to the previous period of the
  same length as the one selected in the Time filter.
- **Login Methods:**  The method used (Form, SSO, OIDC SSO, Social,
  Passkey).
- **Identity provider:**  The IdP's type and URL. Hover to see the
  provider URL.
  - **Risk:** The dynamically calculated severity of the risk
    posed by the account (No risk, Low, Medium, or High).
- **Latest Login:**  The time of the last successful login.

**Filter Account Data**

- **Time:** Filter by time frame. Select one of the options:
  - Last 24 hours
  - 2 days
  - 7 days [default]
  - 14 days
  - 30 days
- **Account Username:** Filter by the username used to login to the
  account.
  - **Unknown username** - Is the username of the account
    unknown?
  - **Anonymized username** - Is the username of the account
    anonymized?
- **Account Application:** Filter by the catalog/custom application
  used to login to the account.
- **Account URL:** Filter by the URL used to login to the account.
- **Identity provider:** Filter by identity provider type (e.g. Okta,
  Entra, Google, Facebook).
- **Identity provider URL:** Filter by the specific Identity Provider
  URL.
- **User:** Filter by PB user that logged into the account.
- **Device:** Filter by the device that logged into the account.
- **Login method:** The login methods used to login to the account.
- **Application risk:** Is the application identified as risky in the
  catalog?
- **Is GenAI app:** Is the application identified as a GenAI
  application?
- **Shared account:** Is this a shared account used by multiple users?
- **Account risk:** Filter by the risk level of the account.
- **Trusted IdP:** Filter accounts on trusted identity providers,
  defined as:
  - An account within the trusted identity provider (e.g. The [username@acme.com](mailto:username@acme.com) entra ID
    account).
  - An account that uses the trusted identity provider to login
    (e.g. The Sales Force account [username@acme.com](mailto:username@acme.com) that uses
    entra for login).
  - You can modify the list of trusted identity providers within the
    filter. 

    ![]()

###### Investigate Individual Account Details

Select any account in the main table. A drawer will open on the right side
containing granular information.

![]()

The information in the drawer includes the fill account metadata, including:

- Full ID
- Provider/tenant details
- Detailed Risk information
- Detailed Login activity
- Full list of users and devices that accessed the account

###### Risk Remediation - What Should I Do?

The risks displayed in the drawer display not only the risk type, but also
suggest the proper resolution. 

![]()

The following risks are calculated for each account:

- **Analyze associated users and devices:** Review the
  list of users and the specific devices (Prisma Browser Desktop vs.
  Prisma Browser Extension) they use.
- **Review login activity and attempts:** Examine
  detailed widgets showing successful versus failed or blocked
  attempts.

---

<a id="roaming-profiles-ensuring-a-consistent-browser-experience"></a>

### Roaming Profiles: Ensuring a Consistent Browser Experience

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/roaming-profiles-setup>*

Set up roaming profiles

Roaming profiles are a fundamental Windows feature that delivers a consistent
and personalized computing environment, allowing a user's browser data to follow them
across various domain-joined computers. This mechanism is network-centric, providing
data persistence without needing cloud synchronization or active internet access, which
is especially beneficial in high-security or air-gapped corporate and educational
settings.Profile Components

A roaming profile synchronizes essential user-specific browser data, ensuring
continuity regardless of the physical machine used:

- **Bookmarks and Favorites:** Web links and folder structures are
  preserved.
- **Browser Settings:** Custom configurations, including the default
  homepage, display options, and security settings, remain consistent.
- **Saved Passwords:** Encrypted login credentials are securely
  synchronized for easy access.
- **Extensions:** Installed browser add-ons are maintained to ensure
  customized functionality.
- **History:** Core browsing history is typically included, though
  caching may be managed separately for optimal performance.

#### The Local Network Synchronization Mechanism

The process by which a roaming profile enables user mobility relies on
local network server interaction:

1. **Login:** Upon signing into any Windows domain machine, the
   system identifies the user's roaming profile path on the central network
   server.
2. **Download:** The complete copy of the user's profile data is
   transferred from the server to the local computer's hard drive.
3. **Usage:** The user works with and modifies this local copy of
   the data.
4. **Logoff:** When the session ends, the operating system copies
   all changes (e.g., new bookmarks, setting modifications) back to the central
   network server, ensuring the profile is up-to-date for the next login.

#### Prisma Browser Implementation

**Enable Roaming Profiles:**

Set the following registry key on each machine:

|

Registry Path | Registry Value | Value |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Software\Policies\Palo Alto Networks\PrismaAccessBrowser | RoamingProfileSupportEnabled | 1 (DWORD) |

The [Profile Sync](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-customization?otp=task-kkc_tfr_hcc#task-kkc_tfr_hcc) control only governs
cloud synchronization and has no impact on this policy.

**Change roaming profile Location** (Optional)

Each user’s roaming profile is kept in a file named profile.pb. By default,
this file is located in %APPDATA%\Palo Alto
Networks\PrismaAccessBrowser\User Data\Default\profile.pb, under the
Windows Roaming Profile directory.

To configure a different location for profile.pb, set the
RoamingProfileLocation registry key. You can use any of the [supported path variables](https://www.chromium.org/administrators/policy-list-3/user-data-directory-variables).

If setting the RoamingProfileLocation policy, do not set
either the UserDataDir or the DiskCacheDir policy to the same directory. Doing so
may cause the local profiles to interfere with roaming profiles and voids the
benefits of the feature.

You can point RoamingProfileLocation directly to a network
share (e.g., \\Server\Profiles\${user\_name}). In this case, Prisma
Browser reads/writes profile.pb directly to the network. **Windows
Roaming User Profiles is not required**.

To customize the location, set:

|

Registry Path | Registry Value |  |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Software\Policies\Palo Alto Networks\PrismaAccessBrowser | RoamingProfileLocation | {roaming\_app\_data}\PrismaBrowser |

If you disable the RoamingProfileSupportEnabled policy or don't configure it, this
value stored in this policy isn't used.

##### Example Setup

![]()

What Syncs

|

Syncs | Does Not Sync |

| --- | --- |

|  |  |
| --- | --- |
|

Bookmarks | Cookies |

|

Saved Passwords | Active Sessions |

|

Autofill Data | Cached Files |

|

Browser Settings | Downloads |

|

Extensions | Temporary Data |

|

Browseing History |  |

Important Limitations

|

Limitation | Details |

| --- | --- |

|  |  |
| --- | --- |
|

**No simultaneous sessions** | Users cannot run Prisma Browser on two machines at the same time. The profile file is locked during use. |

|

**Mutually exclusive with cloud sync** | Roaming Profiles and Browser Cloud Sync cannot be used together. You need to choose one. |

|

**Single profile recommended** | Multiple browser profiles may not map correctly across the machines. |

|

**Large profiles slow login** | Thousands of bookmarks / extensions increase Windows login time |

Your users cannot run Prisma Browser on two machines at
the same time. The profile is locked during use.

---

<a id="explore-prisma-browser-events"></a>

### Explore Prisma Browser Events

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/investigate-prisma-access-browser-events>*

Use the Prisma Browser Events log to monitor activity within your Enterprise
Browser deployment.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Tenant Visibility for SaaS Apps - any role with access to   the Events page. |

The Prisma Browser Events screen is the key visibility tool for investigating
every activity within your Enterprise Browser deployment. Use this screen to assess
the state of your current deployment and ensure that your policy is working as
expected. From here, you can fine-tune the rules that define what actions you allow
your users to perform within the applications you allow. For example, suppose you
have set rules to block file downloads, but have enabled users to bypass this rule
and proceed anyway. From the Events screen, you can see every bypass event and
determine whether you need to refine the rule.

You can also view the browser events and audit logs from Strata Cloud Manager
[Log Viewer](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/incidents-and-alerts/log-viewer). These
logs in [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service) can be
forwarded to Amazon Security Lake, AWS S3, and Snowflake.

To review Prisma Browser events:

1. From Strata Cloud Manager, select ConfigurationPrisma BrowserAnalyticsEvents.

   You can see the total number of events displayed at the top of the page. By
   default, the Events screen displays the 50 most recent events. Click
   Load 50 More to move to the next page of
   events.

   ![]()
2. Investigate events using search and filters.

   An important part of your role with the Prisma Browser is analyzing
   events, and looking for patterns and anomalies in user behavior. Whenever
   you notice unexpected or unusual activity, you need to see if you need to
   tune the rules to meet the needs and requirements of the end users. The Prisma Browser allows you to search and filter the events to discover
   and analyze user behavior patterns. At the top of the screen, you can search
   for specific events using specific data to help find a particular event. You
   can also narrow the list of events by filtering on any of the following
   Events screen columns:

   - **Time**—Select a predefined time period for which to display events,
     or create a Custom time period.
   - **Category**—Narrow down the type of events displayed by selecting
     one or more categories. Available event categories include:
     - Access—Events involving access to websites and apps.
     - DLP—Events involving file upload, file download, and clipboard
       controls (copy/paste)
     - Extensions—Events involving installation, removal, enabling, and
       disabling extensions.
     - PIN Code—Events involving access to apps and features that
       require a PIN code or authorization.
     - Malware—Incidents involving attempted access to malicious
       websites.
     - Tampering—Incidents involving unauthorized file tampering.
     - Tenant—Instances associated with Multi-Tenant applications.
   - **Type**—The type of action that triggered the event log. The event
     types vary by category.
   - **URL**—The URL associated with the event.
   - **App/Extension**—The application or extension associated with the
     event.
   - **Action**—The action that is associated with the event.
   - **User**—The user associated with the event.
   - **MITRE**—The MITRE ATT&CK technique related to the event.
   - **Policy rule**—The policy rule that generated the event.
   - **Recording**—Indicates if a recording is available.

   You can also add additional filters to narrow down the events to display:

   - **Event recordings**—Show only events that have screen recordings.
   - **Web classifications**—Filter by types of web applications
     controlled by the policy rule that triggered the event.
   - **Device**—Filter events based on the device where the event
     originated.
   - **Browser brand**—Filter the events by the browser brand.
   - **Browser version**—Filter the events based on the version of the
     browser where the event originated.
   - **Browser type**—Filter the events based on the browser where the
     event originated.
   - **Device groups**—Filter the events by the device group.
   - **OS platform**—Filter the event based on the operating system on the
     device where the event originated.
   - **User group**—Filter the events based on the user group to which the
     users belong.
   - **MITRE**—Filter the events based on the MITRE ATT&CK Mitigation
     resource.
   - **Compliance**—Compliance Filter the events based on compliance
     issues (for example HIPAA, SOC 2, PCI DSS).
   - **Mode**—The behavior of the policy rule as applied to end
     users.
   - **Is incident**—Filter whether or not the event is an incident.
3. Click into an event to view details about the event.

   ![]()

   There are additional sources of information that you can investigate here.
   - **Device Posture** - The device security posture and the metadata
     information collected t the time of this event. 

     ![]()
   - The following Posture details are available:
     - Endpoint protection
     - Active firewall
     - Disk encryption
     - Screen lock
     - Password policy
     - System integrity
     - Remote desktop connection
   - **Raw Data** - The raw data associated with this event. 

     ![]()
4. Export events for offline investigation.
   1. Click the Export icon.
   2. In the Export window, select one of the following options:

      - **Export all available events**—Export all the events in the
        database (up to a maximum of the 10,000 most recent
        events).
      - **Export filtered or searched events**—Export events based on
        the current filters.

#### Tenant Visibility for SaaS Apps

The **Prisma Browser** enhances visibility into SaaS usage by detecting
and reporting the logged-in tenant when a user signs in to supported
applications. This feature helps administrators identify which tenants employees
are accessing, enabling better control over **unsanctioned or unapproved
tenants**.

By capturing tenant-level details, administrators gain actionable insights to
strengthen governance and reduce the risk of shadow IT.

**Supported Applications and Collected Data**

Prisma Browser and Prisma Browser Extension currently support tenant
visibility for the following SaaS applications:

- **Google Workspace** - Tenant domain
- **Microsoft Office 365** - Tenant domain
- **Slack** - Tenant domain, workspace name, workspace id, channel
  id
- **Amazon Web Services** - Region, account id

**Event Data Access**

The system records tenant detection data and makes it available in two locations:

- Collected tenant data appears in the **Event drawer** in the
  browser.
- If **SIEM integration** is enabled, the collected data is forwarded
  to the customer's SIEM for centralized monitoring.

#### Detection Behavior

Prisma Browser uses **application-specific detection strategies**. These
strategies may rely on:

- URLs
- Cookies
- Local storage
- Network events

Because SaaS providers frequently update their applications, detection accuracy
may vary if the provider changes how information is shared with the browser.

#### Key Points

- **Login dependency**: A tenant is detected only when the user
  **actively signs in** to the application.

  - Example: Applications such as Google Gemini or
    google.com may not trigger detection since
    they do not always require a login.
- **Event variations**: Some behaviors can cause tenant detection to
  fail:

  - **Forced reauthentication**: If a user opens their laptop and
    Outlook redirects immediately to a sign-in page, Prisma Browser logs a *website access* event without
    tenant details.
  - **Fast redirection**: In certain Outlook versions, when a file
    download triggers a new tab and immediate redirect, the process
    may bypass tenant detection.

If a user is redirected to sign in immediately after
opening an app like Outlook, the system logs a "website access" event but does
not capture tenant information. This is due to the user needing to
reauthenticate before a new session can be established.

#### Real-Time Analysis for Malicious Sites

This task describes the Real time analysis engine.

The Prisma Browser has a Web Scan engine that scans URLs in
real-time. The results of the scan are used to determine whether the URL is
malicious or not. The browser uses the Phobos Real-Time Analysis or the Palo
Alto Networks database (PAN-DB).

The particular tool that
catches the malicious URL is displayed in the Event log and in the drawer. You
can filter the log for the selected analysis tool.

![]()

![]()

#### Screenshots

This task describes how to use event screenshots.

You can configure the Prisma Browser to take screenshots of the
activities that were preselected. This allows you to see the direct actions that
your users perform in the browser, increasing the effectiveness of your
monitoring and management capabilities.

The screenshots are based solely
on the information that you configure to provide more enhanced visibility and
monitoring. The information belongs to you. Neither Palo Alto Networks not its
employees have access to the recordings.

Screenshots are only captured within the browser box. The screenshot does NOT
include:

- tabs
- content from tabs not currently in focus
- areas outside the tab
- the omnibox

##### Enable Screenshots

1. Create or edit an Access & Data Control rule.
2. At the Log Level step, select **Enhanced**.
3. Click **Screenshots**.

###### Viewing Screenshots

1. The screenshots are available in the Event Drawer. Locate the event
   that contains the recording, open the Drawer, and click the
   Screenshot icon.

   ![]()
2. The screenshot will display in a separate window.

   ![]()

   For each configured action, the Prisma Browser will take
   another screenshot. This provides additional images of the
   user's experience, so you can see exactly what actions a user
   performed. For example, if you set rules against copyinig
   information from ChatGPT, there will be a screenshot when you
   open the page, and another when you copy information.

###### Current Screenshot Retention Policy

This task describes the retention policy for
the screen recordings.

Palo Alto Networks retains the screenshots for an
indefinite length of time in our own dedicated storage. This means that
you can review the user's actions long after the actual event took
place. With this retention policy, you can also use the information to
examine a user's behavior over a long period.

---

<a id="prisma-browser-investigations"></a>

#### Prisma Browser Investigations

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/investigate-prisma-access-browser-events/prisma-access-browser-forensics>*

This is the description of the forensic investigations.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser Investigation feature is an advanced forensic tool
designed to monitor, audit, and secure enterprise environments. This powerful solution
enables incident response teams to extract and analyze browser-related data,
facilitating security incident investigations, compliance enforcement, and unauthorized
activity detection.

By providing comprehensive forensic capabilities, the tool enables security
teams to reconstruct a clear narrative of events leading up to a security incident or
potential threat.

##### **Key Capabilities**

The Prisma Browser Investigation feature offers deep visibility into
user activity by capturing event data and relevant evidence. Its intuitive interface
enables rapid identification of anomalies and security threats.

##### **Features**

- **Time-based Sequential View:** Displays browser events
  chronologically per user and per device.
- **Interactive Event Mapping:** Enables navigation via mouse or
  keyboard.
- **Visual Evidence Integration:** Incorporates screenshots and
  event recordings for enhanced analysis.
- **Comprehensive Session Metrics & Event Histogram:**
  Includes policy rule enforcement indicators for precise monitoring.
- **One-Click Investigation Initiation:** Enables analysis of
  suspicious events.
- **Seamless Activity Chain Visualization:** Provides a structured
  view of user activities over time.

By employing Prisma Browser's Investigation feature, enterprises can
strengthen security measures, mitigate insider threats, and maintain full visibility
over browser-based activities. This tool is essential for security auditing,
incident response, and compliance verification.

##### Investigative Tools

The **Investigation feature** enables incident response teams to examine
potentially dangerous events occurring during a user's browsing session. For
example, if a policy rule blocks file uploads to Gmail and a user attempts an
upload, the **Event Log** records the activity, enabling further
investigation.

Incident response teams can:

- Inspect the event details
- Identify behavior patterns leading to the suspicious activity
- Analyze activities **30 minutes before and after** the event

The **Investigation window** displays the following key information:

The Investigation window provides a structured view of crucial forensic
data:

1. **Session Details:** Captures session details, including
   applications used and activity types.
2. **Filter Data:** Refine searches based on event type,
   application, action, and incident classification.
3. **Histogram:** A visual representation of events per minute. The
   display shows a Red bar if there is at least one blocked event during that
   time frame. If it displays a Blue bar, there are no blocked events.

   The default view focuses on a 10-minute block (five minutes before and after
   the event), adjustable within a 1-hour window.
4. **Activities Chain Map:** Displays a sequence of user activities
   surrounding the event, including relevant applications and timestamps.
5. **Evidence Drawer:** Stores visual records such as screenshots or
   event recordings.
6. **Event Drawer:** Consists of metadata, including raw event data
   for third-party analysis.

![]()

##### Navigating the Investigation Data

There are different ways that your Incident Response team can navigate through the
Investigation information to be able to properly examine the information and search
for appropriate information. The PPrisma Browser Investigation feature has many
different ways for you to navigate the data.

- Using a mouse - The mouse allows you to click between the different elements
  on the screen. Additionally, you can use the scroll button on the mouse to
  control the zoom in / zoom out for the Activity Chain Map, making it easier
  to concentrate on a particular area.
- Using a keyboard - It is easier to navigate the Activity Chain Events using
  the arrow keys on the keyboard. The arrow keys allow you to scroll through
  the different events within the time frame.
- Using a traackpad - This allows you to zoom in / zoom out, making it easier
  to concentrate on particular views.

##### Conducting an Investigation

The Prisma Browser Investigation feature enables incident response
teams to investigate suspicious user activities, such as Security policy violations
or attempts to access restricted content.

To begin an investigation:

1. **Select an Anchor Event:** Identify the suspicious or malicious
   event for further analysis.
2. **Initiate the Investigation:** Click the “**Investigate” icon** located
   in the **Event Drawer** or next to individual events in the log.

   ![]()

   ![]()

   When you click the icon, you are directed to the Investigation page.

   Your incident response team can also initiate an investigation
   directly through the **Investigation** link. Using this method to open an
   investigation requires the investigators to use the search filters to locate
   the incidents that they need to investigate.
3. **Analyze Metadata:** Review the forensic details,
   including:

   - Event timestamp and a one-hour investigation window.
   - Filter options for refining searches.
4. Click **Session details** to obtain the basic metadata for the
   user/device that you want to investigate. The Session details includes:

   - Time frame
   - Number of events
   - User name
   - Device hostname
   - Device type
   - Geolocation
   - Apps in the session
   - Events in the session

   ![]()
5. The **Histogram** visually represents event occurrences within
   the 1-hour time frame. The default focus area is 10 minutes, centered on the
   event. The incident response team can adjust this focus as needed when they
   are performing their investigation and analysis.

   If even a single event is blocked, then the display will show a red
   bar. Otherwise, the histogram will display a blue bar. The bars are
   connected to the Activities Chain Map display. The histogram reflects the
   system response - when an event is blocked, the histogram will be red. If
   there is no block, then the histogram is blue. By using this feature, you
   can see the frequency of blocked versus allowed responses.

   ![]()
6. The main part of the Forensic analysis is the **Activities Chain Map**. This
   feature displays activities that took place at any given moment during the
   investigation time. It displays two information sections:
   - The application/URL where the activity took place.
   - The events that took place at the time. 

     ![]()

     Blocked events are
     clearly marked with **red bars** on the left side, enabling quick
     identification of policy violations (e.g., **blocked file upload
     attempts to Gmail**). You can scroll through the events by either
     clicking on them using a mouse, or by using the arrow keys on the
     keyboard.

     If multiple events occur at *exactly* the
     same second, the event will be marked ***Multiple Events***,
     and a **badge** will display the count. To analyse the events,
     hover on the badge to see all the simultaneous events. If the events
     are exactly the same, the Activities Chain will display the badge
     with the event type named instead. 

     ![]()

     The events must occur at the exact same time
     to be considered as multiple events.

     Every event
     will have its own Event Drawer information, and if it is available,
     its own Evidence.
7. The **Event Drawer** displays all the relevant metadata for the event. This
   allows you to examine all the "back office" information that can assist you in
   investigating a suspicious event. In addition to all the meta data, the drawer
   contains the raw event data that you can copy and send to a third-party tool for
   analysis. The drawer allows you to examine the data carefully while looking for
   malicious or suspicious occurrences. 

   ![]()

   ![]()

The **Evidence Drawer** provides access to event recording and screen captures of
suspicious events. With this tool, you can visualize exactly what the user did to
trigger the suspicious event. This helps you increase the effectiveness of your
forensic investigations. Event recording start a few seconds before the incident,
and end a few seconds after the incident is complete.

The Evidence drawer has several special controls that helps your incident response
team analyse the different suspicious events.

1. **Collapse / Expand the Evidence Drawer:** This button toggles the
   drawer. If there is evidence associated with the event, there will be a blue
   button on this control.
2. **Previous / Next Evidence:** This control permits moving between events
   that have evidence associated with them. Instead of having to manually move
   through the different events in the Activity Chain Map, this control only
   moves between events that have evidence.
3. **Expand Evidence:**  Expand the size of the screenshot or event
   recording.
4. **Full Screen:**  Expand the evidence to full screen mode so that you can
   see things much closer. 

   ![]()

---

<a id="account-protection-for-the-prisma-browser"></a>

### Account Protection for the Prisma Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/account-protection-for-the-prisma-access-browser>*

This article describes how to perform the Account Protection deployment.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Many applications can’t integrate with a company’s Single Sign-On (SSO)
solution via an Identity Provider (IdP), such as Okta or Azure Active Directory
(AAD), despite handling sensitive data or enabling critical operations that impact
the organization. Examples of such applications include:

- **Virtual Data Rooms (VDRs):** Platforms for collaborating on contracts
  and documents between financial institutions.
- **Company Social Media Accounts:** Company social network accounts
  managed by marketing teams.
- **Third-Party or Partner-Managed Applications:** Services like secure
  file shares operated by external partners or vendors.

Organizations encounter significant challenges in achieving visibility and securing
these unmanaged services, leading to vulnerabilities caused by:

- **Lack of Security Oversight:** Applications not managed through an IdP
  often lack IT governance, creating uncertainties for security teams.
- **Weak Access Controls:** These services typically don’t support SSO
  integration or centralized authorization systems. Credential sharing is
  common, and multi-factor authentication (MFA) is frequently absent.
- **Limited Security Measures:** Without auditing and enforcement
  capabilities, these systems lack transparency and control over user access.
- **Inadequate Data Protection:** Security teams are unable to enforce
  stringent identity and data protection policies.

In many cases, users independently create, manage, and modify credentials
for such applications, or rely on third-party IT teams to handle security —
introducing significant risks.

**Account Protection** provides a solution by enabling security teams to regain
control over unmanaged, third-party, and non-SSO-enabled services. It achieves this
by ensuring all access occurs through a Privileged Access Broker (PAB), delivering:

- **Gain full visibility** into user actions within these systems.
- **Record sessions and events** for compliance and audit.
- **Apply advanced data loss prevention (DLP) controls** to protect
  sensitive data.
- **Implement modern step-up MFA** for applications that don’t support SSO.

By deploying **Account Protection**, organizations eliminate security gaps,
enhance oversight, and protect critical assets across all applications — whether
managed within the company’s SSO framework or not.

#### How Does It Work>

How does account protection work 

![]()

**Account
Protection** introduces an additional security layer for unmanaged
services by enhancing password management through the **Protected Access
Broker**. The process is as follows:

1. **Password creation / reset via Protected Access Broker:**
   - Users must create or reset their passwords exclusively through
     the Protected Access Broker.
   - Without resetting the password via PAB, users can’t log in to
     the application through the enterprise browser.
2. **Secure password generation:** 
   - Prisma Browser employs a proprietary algorithm to generate a
     secure password by combining:
     - **User-Selected Password:** A password chosen by the
       user, which is never stored in PAB.
     - **Secret Token:** A unique, system-generated token
       created by Prisma Browser, which is not disclosed to
       the user.
3. **Password Swapping:**
   - PAB replaces the user-selected password with the combined secure
     password.
   - The combined password is then set as the new application
     password during the password reset process.

**Key Benefits** 

- Users retain knowledge only of their selected password, while the **Prisma Browser** securely stores and appends the secret token
  during authentication.
- On subsequent logins, Prisma Browser appends its secure token to the
  user password, ensuring authentication success.
- **Access Restriction:** Logins from non-enterprise browsers are
  blocked because the secure token is absent, ensuring that access is
  limited to the enterprise browser environment.§

**Administrative Control**

You can enforce Prisma Browser policy rules, including visibility and security measures, for unmanaged,
third-party, and non-SSO-enabled services.

1. **Supported Login Methods:** Only password-based
   authentication methods are supported.
2. **Password Reset Requirement:** The application must support
   resetting user passwords before login (e.g., via a "Forgot Password"
   feature).
3. **Shared Account Handling:** For shared accounts, the same secure
   token is applied for all users. This configuration must be explicitly
   selected when enabling Account Protection for such applications.

This process ensures stronger security for unmanaged services while
maintaining usability and control.

##### Configure the Account Protection

Account Protection uses an Access & Data Control rule for configuration.
You can set up Account Protection in the **Login Controls** step.

To configure Account Protection:

1. **Create an Access & Data Control rule**. For more information,
   refer to [Manage Prisma Access Browser Access
   & Data Control Rules](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules?otp=task-pqd_js3_hcc#task-pqd_js3_hcc).
2. **Configure the Login Controls**.

   - Navigate to the **Login Control** step and do the following:
     1. **Click "Login Form"** to define login behavior.

        ![]()
     2. Select the desired **Login Control behavior** from
        the available options.
     3. Enable Account Protection:
        1. Click **Account Protection** to enforce
           access restrictions and secure application
           passwords.
        2. Check **Activate Account Protection** to
           enable the feature. 

           ![]()
        3. If shared accounts need to be supported, check
           **Enable Account Protection for shared
           accounts** to allow Prisma Browser to use
           the same secret token for all users of the
           application.

           ![]().
3. **Finalize configuration:** 

   - Once configured, users will only be able to access the protected
     application via the **Prisma Browser**.
   - Users will need to reset their password for the application,
     which will then be secured by Account Protection. 

     ![]()

     ![]()
   - For shared accounts, the same secret token will be applied to
     all users, enabling account sharing securely.

#### End-User Experience

1. **First-Time Login:**

   - When Account Protection is enabled, users attempting to log in to a
     protected application for the first time will receive a prompt to
     reset their password or create an account.
   - The account will automatically be added to Account Protection upon
     password reset or account creation.
2. **Access Restriction Before Password Reset:**

   - Users can’t log in to the application until they reset their
     password via Prisma Browser.
3. **Visual Indications:**

   - A dedicated browser **omnibox indicator** will show that Account
     Protection is active.
   - For some applications, additional indicators will appear during
     login attempts, offering guidance if login fails or when using a
     protected account.

   By configuring Account Protection, administrators ensure enhanced
   security for unmanaged services, allowing only secure access through the
   Prisma Access Browser.

---

<a id="manage-prisma-browser-users"></a>

### Manage Prisma Browser Users

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-users>*

Review the list of Prisma Browser users and user groups.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The User page can be used for several different needs.

1. **Review User Groups** - Review the User Groups that are enabled to
   access your Prisma® Access Browser tenant.
2. **Manage User Groups** - Manage the User Groups that are enabled to log
   in. In addition to the User configuration step in the [Onboarding step](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding?otp=task-z3p_t3n_gcc#task-z3p_t3n_gcc), you can add or
   remove user groups from the User Groups page.
3. **Review Users** - Review the status of your users - who is active, when
   they logged in, who has never logged in, and so on.

From the **Users page**, you perform the following actions:

- **Review User Groups**: Examine all user groups and identify those that
  have access to your tenant.
- **Modify User Groups**: Add or remove user groups, even after completing
  initial user configurations during onboarding.
- **View Individual Users**: Access individual user profiles, checking their
  **status** and tracking **key details**. These details
  include:

  - **Active or inactive status**

    The
    status categories are as follows:
    - **Active** - A regular user.
    - **Inactive** - A user who is no longer using the Prisma Browser (They gave been removed or
      blocked).
    - **Invited** - A user who has access to the Prisma Browser, but has not as yet started using
      it.
  - **Last login time**
  - **Login history** (including users who have never logged in)
  - **Connected devices**
  - **Group membership**

This page consolidates all essential user and group data in one location, which
streamlines your administrative tasks.

The page is tabbed so that you can choose which view you want to see:
Users or User Groups. The
User Groups tab allows you to create and examine groups
of users. This becomes important when defining rules and policies.

#### User Group Sync

1. If you did not configure which User Groups can
   access the Prisma Browser tenant compete the onboarding wizard,
   configure the authentication profile, and select the directories and User
   Groups that can access your tenant.
2. Prisma Browser manages user access to your tenant by syncing only the
   selected user groups from selected directories. When a directory is first
   configured, Prisma Browser initiates a full synchronization, importing
   the permitted user groups. This initial sync can take a few minutes,
   depending on the number of users in the directory, and a banner is displayed
   on the top of the screen until the sync completes. After the initial sync,
   Prisma Browser checks for changes and modifications every few
   minutes, adding or removing users as needed.

#### Manage Synced Users Groups

1. From Strata Cloud Manager, select ConfigurationPrisma BrowserDirectoryUsers. Select the User Groups tab.
2. Click **User Groups Sync**.
3. The following options are displayed in the window:

   - Click **Add directory**. This will add a new row. Use the
     drop-down list to select a new directory. **User name**—The
     user's name. You can then select the user groups from the CIE, and
     the primary identification (Mail/UPN) for this directory.
   - Use the drop-down to change the directory without selecting a new
     directory, then change the user groups as needed.
   - Click the trash bin icon to remove the entire row. The empty row
     will remain in the display.

     If there are
     no directories available, the **Add directory** button is
     disabled.
   - Changing the primary identifier between UPN/Mail will trigger a full
     synchronization between Prisma Browser and Cloud Identity Engine,
     which can take several minutes. During this time, logged-in users
     will not be affected.

     ![]()

#### Handling Duplicate Users

Prisma Browser supports environments that use multiple (IdPs). When the same
user appears in more than one IdP—or when the same email address appears
multiple times within a single IdP—Prisma Browser intelligently merges the
related records into a single, unified user profile.

Prisma Browser uses the user's primary identifier (email or UPN) for matching
and normalizes all identifiers to lowercase to ensure consistency.

Prisma Browser handles the following scenarios:

- **Adding a New User**:

  When synchronization introduces a user that matches an existing Prisma Browser profile, the browser merges the accounts and retains
  all existing data, including bookmarks, browsing history, and saved
  passwords. This ensures users experience no disruption.
- **User Group Handling**:

  Prisma Browser merges group memberships additively. A user becomes a
  member of all groups associated with their identities across all
  directories.
- **Attribute Conflict Resolution**:

  If user attributes (such as first or last name) differ across
  directories, Prisma Browser displays and makes them searchable in
  the UI.
- **User Removal**:

  When you remove a directory or user group, Prisma Browser evaluates
  the user's presence in remaining directories:

  - If the user exists in another directory, Prisma Browser
    retains the profile and updates access accordingly.
  - If the user appears only in the removed directory, Prisma Browser de-provisions the profile and marks it as
    **removed**. You can reactivate the profile automatically
    if the user reappears in a future sync.

#### Enhanced User Deduplication: Seamless User Management Across Directories

Prisma Browser now offers enhanced deduplication capabilities to prevent
duplicate user profiles across directories. This ensures smooth synchronization,
consistent user experiences, and uninterrupted access to bookmarks, passwords,
and other user data.

Previously, Prisma Browser could encounter duplicate users from one or multiple
identity providers (IdPs), which sometimes blocked syncs or disrupted
proofs-of-concept (POCs). Issues included:

- Local user creation followed by IDP sync.
- Multipler IdPs containing the same user email / UPN.
- `Case-sensitive email entries creating inconsistent profiles.

**Key Enhancements**

Prisma Browser now intelligently merges duplicate user profiles across
directories into a single, unified profile making use of primary identifiers
(email/UPN, normalized to lowercase).

**How it Works:**

1. **New User Merges**
   - When a new user sync triggers a merge, existing profile data
     (bookmarks, history, passwords) is fully preserved.
   - Users experience uninterrupted access to their data.
2. **Additive Group Merging** 
   - Group memberships from merged directories are combined additively.
   - Users retain access to all relevant groups across directories.
3. **Attribute Visibility**
   - Differing user attributes (such as first name, last name) remain
     searchable and visible within the interface.
4. **User Removal**
   - Users removed from specific directories or groups retain their
     profiles.
   - Users removed from ALL directories are de-provisioned, but can be
     reactivated if synced back in later.

**Benefits**

- Eliminates duplicate profiles and conflicts across IDPs.
- Maintains a seamless, uninterrupted user experience.
- Ensures consistency in bookmarks, passwords, and group memberships

#### Review the User Group Data

View the details about each user group, including:

1. **Name** - The user group name.
2. **Source**—The Directory name of this User Group.
3. **Rules**—The number of rules applied to the group.
4. **Created at**—The group creation date. Hover over the field to see
   the full timestamp.
5. **Last updated**—The time elapsed since the last group update. Hover
   over the field to see the full timestamp.

Investigate groups using search and filters:

1. Search by ID or Name.
2. Filter the users based on Source, Created at, or Last Updated.

View details about a specific user group.

1. Click on a specific group on the list to see details about the group.
2. Review the group-specific details, including:
   - **Policy Rules**—Lists the policy rules that control the Prisma Browser's group's. Click on a policy type to view the
     rules governing the group's browser experience in that category.
   - **Users**—Lists the members of the group. Click on a specific
     member to view details about the user.

Export user details for offline investigation.

1. Click the Export icon.
2. In the Export window, select one of the following options:
   - Export all - Export the data group.
   - Export filtered data - Export User Group details based on the
     current filters.

![]()

#### Add Local User Groups

The Prisma Browser
**Local User Group** function enables you to create groups that do not exist
in your Identity Provider (IdP) or groups that span existing directory
boundaries. You primarily use these for specific policy requirements. For
instance, when you roll out a new policy for a subset of users, you create a
dedicated local user group and add the specific users. Conversely, to exclude
certain users from a rule, you create a user group and manage its membership
directly from the UI or API[API](https://pan.dev/access/api/browser-mgmt/get-seb-api-v-1-user-groups/).

1. Click **Add Local Group**.
2. In the ***Add local group*** window, enter the following
   information:
   1. Enter a **name** for the local group.
   2. Click the **Add users** drop down and select all users who need
      to become members of this group.
   3. Click **Create Group**.

#### Manage User Groups

The Prisma Browser user group function allows you
to create groups for different users. For example, you can set up a group for IT
administrators, managed users, unmanaged users, or users with printing
permissions.

1. From Strata Cloud Manager, select ConfigurationPrisma BrowserDirectoryUsers and select the User Groups tab.

   You can see the total number of user groups displayed at the top of the
   page.

   ![]()
2. Review the user group data.

   View details about each user group, including:
   - **Name**—The user group name.
   - **Source**—The source directory of the user - the name of the
     directory.
   - **Rules**—The number of rules applied to the group.
   - **Created at**—The group creation date. Hover over the field to
     see the full timestamp.
   - **Last updated**—The time elapsed since the last group update.
     Hover over the field to see the full timestamp.
3. Investigate groups using search and filters.

   - Search by id or name.
   - Filter the users based on Source,
     Created at, or Last
     updated.
4. View details about a specific user group.
   1. Click on a specific group on the list to see details about the
      group.
   2. Review the group-specific details, including:

      - **Policy Rules**—Lists the [policy
        rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html) that control the group's use of the Prisma Browser. Click on a policy type to view the rules
        governing the group's browser experience in that
        category.
      - **Users**—Lists the members of the group. Click on a
        specific member to view details about the user.

      ![]()
5. Export user details for offline investigation.
   1. Click the Export icon.
   2. In the Export window, select one of the following options:

      - **Export all**—Export all group data.
      - **Export filtered data**—Export user group details based
        on the current filters.

---

<a id="manage-configuration-versions-draft-mode"></a>

### Manage Configuration Versions (Draft Mode)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-configuration-versions-draft-mode>*

Discussion of the draft mode.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-browser-roles.html) |

Draft Mode fundamentally changes how you manage and deploy your Prisma Browser configuration, instituting a robust, staged workflow that minimizes
risk and enhances control. Instead of the traditional method where every alteration
immediately affects the live system—the active configuration—we now safely capture and
store all modifications within a temporary, isolated draft environment.

This Draft Configuration serves as a staging area and provides a crucial buffer
between development and deployment. In this environment, you gain the necessary time and
tools to thoroughly review every detail of your proposed changes, iteratively modify
settings, and execute comprehensive validation tests. This critical staging process
ensures you optimize the configuration and verify it is error-free before you commit it
to the live environment.

Once satisfied with the drafted changes, you can initiate the publishing
process. This action is the gateway to production; it takes the validated draft and
promotes it to become the new active configuration, and the system immediately enforces
this new configuration across your production environment. A key feature of this system
is that it automatically creates a numbered configuration version upon every successful
publish. This systematic versioning establishes a complete, chronological audit trail of
changes. By maintaining a full history of configuration versions, Prisma Browser
offers unprecedented transparency and traceability, which allows administrators to
understand exactly what changed, when it changed, and who made the change. This version
history is indispensable for troubleshooting, compliance auditing, and, most
importantly, it allows you to quickly and reliably revert to a prior, stable
configuration should any unforeseen issues arise with the latest deployment.

#### Supported Entities

The Draft mode applies to the following entity types:

- **Policy Rules:** Sign-in rules, Access and Data Control rules, Browser
  Security Rules, Browser Customization Rules.
- **Applications:** Custom and Private Applications
- **Application Groups:** Groups of Applications
- **Device Groups:** Device Posture Groups

Entities not mentioned above (for example, System
Settings) continue to apply changes immediately. When you make a change outside
the draft workflow, an alert notifies you that your changes take place
immediately.

#### How Draft Mode Works?

Draft mode in the system utilizes a carefully managed, three-step lifecycle designed
to allow you to safely introduce changes without immediately impacting the live
production environment. This process ensures thorough review, collaboration, and
version control before any modification becomes active.

1. **Make the changes (Draft Configuration):**

   This is the initial phase where all modifications are prepared.
   When an administrator initiates a change—whether creating a new policy,
   editing an existing setting, or deleting an outdated entity—that action is
   immediately recorded and saved to the **draft configuration**.
   - **Isolation and Safety:** The fundamental principle of this step
     is isolation. All pending modifications reside exclusively within
     the draft configuration. This means the **active configuration**,
     which is currently controlling the live system or services, remains
     completely untouched and stable. Live operations continue to
     function based on the last published configuration.
   - **Iterative Work:** You can make any number of changes, save your
     work, log out, and return later. The draft persists until it is
     explicitly published or discarded. This allows for complex,
     multi-day, or multi-administrator projects to be managed
     effectively.
   - **Supported Entities:** The draft configuration accommodates
     changes to all supported entities within the platform, ensuring a
     comprehensive approach to configuration management.
2. **Review Changes (Audit and Verification):**

   Before any draft
   changes can be made permanent, a thorough review process is necessary to
   ensure accuracy, compliance, and prevent errors.
   - **Visibility:**
     Prisma Browser provides a comprehensive interface for reviewing
     all pending modifications. This step is critical for quality control
     and team collaboration.
   - **Detailed Audit:** Administrators can view the exact differences
     between the draft and the active configuration. The review tool
     clearly highlights:
     - **Creations:** New entities that have been added to the
       configuration.
     - **Updates:** Existing entities that have been modified,
       with a side-by-side comparison of the old and new values.
     - **Deletions:** Entities that have been marked for
       removal.
   - **Accountability:** A key feature of this step is the ability to
     track **who** made **what** change. The review log provides an
     audit trail, showing the identity of the administrator responsible
     for each modification, which is essential for troubleshooting and
     security compliance.
3. **Publish (Activate):**

   The final step formalizes the draft changes and
   makes them operational in the live environment.
   - **Commitment:** When the review process is complete, and all
     pending changes are verified and approved, the administrator
     executes the **Publish** action.
   - **Activation:** This action applies all pending changes from the
     Draft Configuration to the active configuration, making them
     immediately effective for the system.
   - **Version Control:** The publishing process is intrinsically
     linked to the platform's version control system. Prisma Browser
     automatically:
     - **Creates a New Configuration Version:** A permanent,
       immutable record (a snapshot) of the newly activated
       configuration is saved, complete with a version identifier
       and a timestamp. This allows for historical tracking and
       rollback capabilities if needed.
     - **Resets the Draft:** Once the draft has been
       successfully published and a new version created, the
       temporary draft configuration is automatically cleared and
       reset. It is synchronized to be an exact match of the newly
       published active configuration, ready for the next cycle of
       changes.You can also **discard** all pending changes at any time to reset
   the draft back to the current active configuration.

#### View Draft and Published Configurations

Pages that support Draft Mode (e.g., Policy Rules, Applications, or Device
Groups) allow you to switch between viewing the draft and published
configurations.

Near the page title, you will find the following controls for managing
configurations:

- **Published:** Shows the currently enforced, active configuration. This
  view is read-only.
- **Draft:** Displays the current working configuration where you make and
  view all pending changes.
- **Pending changes indicator:** Indicates the number of uncommitted
  changes in the draft. If there are none, it shows **No pending changes**.
- **Version number** Displays the version number and publication date of
  the current active configuration.

To modify, add, or remove entities,
switch from the published configuration view to the draft view. Changes cannot
be made while viewing the published configuration.

#### Review Pending Changes

Before you publish, review all pending changes to verify your configuration
updates.

1. From the draft view of any configuration page, click the **pending
   changes** indicator.
2. The **Review Changes** panel displays a list of all pending changes
   across all supported entity types. For each change, the following information is
   displayed:
   - **Entity type:** The type of entity (rule, section,
     application, device group).
   - **Name:** The name of the entity.
   - **Operation:** Whether the entity was Created, Updated, or
     Deleted.
   - **Updated by:** The administrator who made the change.
   - **Updated at:** The date and time of the change. Hover over
     the field to see the full timestamp.
3. Use the filters to narrow the list by entity type, operation, or
   search by name. Before committing and publishing your configuration updates, it
   is essential to meticulously review all pending changes to ensure accuracy,
   compliance, and the intended outcome. This process allows you to catch potential
   errors or unintended consequences before they affect the live system.

Here is a comprehensive guide to reviewing your configuration changes:

1. **Accessing the Pending Changes Review:**
   - While in the draft view of any configuration page within the
     management interface, locate and click the **pending changes**
     indicator. This indicator is typically prominently displayed and shows
     the count of modifications that have been made since the last published
     version.
2. **Understanding the Review Changes Panel:**
   - Clicking the indicator opens the **Review Changes** panel,
     which provides a detailed, centralized list of all modifications that
     are currently pending across *all* supported entity types within
     the configuration draft.
   - For every entry in this list, the panel displays crucial
     metadata, enabling a thorough review:
     - **Entity type:** Identifies the specific category of the
       configuration object that was altered. Examples include, but are
       not limited to, rule, section, application, device group,
       network interface, or security profile. This helps in
       immediately understanding the scope of the change.
     - **Name:** The specific, identifiable name of the entity that
       was affected. This could be the name of a security rule, a
       network zone, a user group, or a specific application
       definition.
     - **Operation:** Clearly states the action that was performed
       on the entity. The three primary operations are:
       - **Created:** A new entity was added to the
         configuration.
       - **Updated:** An existing entity's parameters or
         properties were modified.
       - **Deleted:** An existing entity was removed from the
         configuration.
     - **Updated by:** Indicates the administrator or system process
       that executed the change. This is vital for accountability and
       tracing the source of an update.
     - **Updated at:** Records the exact date and time when the
       change was finalized in the draft. To view the full, precise
       timestamp, simply hover your cursor over this field.
3. **Refining and Filtering the Change List:**
   - For configurations with a large volume of pending changes, the
     Review Changes panel includes robust filtering and search capabilities
     to help administrators focus on specific modifications:
     - **Filter by Entity Type:** Use the filter menu to narrow the
       displayed list to only show changes related to a specific entity
       category (e.g., only show changes to "rules").
     - **Filter by Operation:** Limit the view to only show entities
       that were Created, Updated, or Deleted.
     - **Search by Name:** Utilize the search bar to find changes
       affecting a specific entity name or part of a name. This is
       particularly useful when reviewing changes to a known, named
       object.

By utilizing these steps, administrators can ensure that the configuration
being published is exactly as intended, minimizing the risk of deployment errors and
maintaining the integrity of the system.

#### Publish Draft Changes

When your changes are reviewed and ready, publish the draft to make it the
active configuration.

1. Click the **pending changes** indicator to open the **Review
   Changes** panel.
2. Review the list of pending changes.
3. Click **Publish**.
4. (Optional) Add a description for this version. The description helps
   you identify this version in the version history.
5. Confirm the publish operation.

To activate your changes, you need to publish the draft after reviewing and
confirming it:

1. **Open the** **Review Changes** panel by clicking the **pending
   changes** indicator.
2. Examine the list of pending changes.
3. Click **Publish**.
4. Optionally, add a description to help identify this configuration version in
   the version history.
5. Confirm the publish action.

Once published, this becomes the active configuration.

**After Publishing:**

- A new configuration version is created with an auto-incrementing
  version number (e.g., Version 45 → Version 46).
- All pending changes become the active configuration and are enforced
  immediately.
- The draft resets to match the newly published active configuration.
- The previous active version is archived and available in the version
  history.

Publishing commits all pending changes as a
single, atomic operation. You cannot publish a subset of changes.

##### Discard Draft Changes (Reset the Draft)

If you want to discard all pending changes and start over from the current active
configuration, you can reset the draft.

1. Click the **Pending Changes** indicator to open the **Review Changes**panel.
2. Click **Discard all**.
3. Confirm the Discard operation.

   This action cannot be undone. All uncommitted draft
   changes are permanently lost. The active configuration is not
   affected.

##### View Configuration Version History

Every time you publish a configuration, Prisma Browser
automatically creates a new, numbered version. You can review this version
history to track past configurations and identify the changes introduced in each
one.

To view the configuration version:

1. Navigate to the Configuration Versions page.
2. The Version List displays all published versions, in ascending order.
   Each entry contains the following details.
   - **Version number:** A sequential, auto-incrementing
     identifier.
   - **Status:** Indicates if the version is the Active (current)
     configuration or Archived (historical).
   - **Published at:** The date and time the publication occurred.
   - **Published by:** The administrator who published the
     Configuration.
   - **Description:** The optional summary added during the
     publishing process.
   - **Changes summary:** A count of the entities Created,
     Updated, and Deleted in that specific version.
3. Click any version in the list to see a detailed breakdown of the
   changes.

#### Best Practices

- **Review before publishing:** Always review the pending changes list before
  publishing to verify that all changes are intentional and complete.
- **Use version descriptions:** Add meaningful descriptions when publishing to
  make it easier to identify versions in the history.
- **Coordinate with your team:** When multiple administrators work in the same
  draft, communicate to avoid publishing another administrator's incomplete work.
  Publishing commits all pending changes from all administrators.
- **Check for unsupported entities:** If you see an immediate change alert, the
  entity you modified is not part of the draft workflow, and the change is already
  live.

---

<a id="manage-prisma-browser-devices"></a>

### Manage Prisma Browser Devices

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices>*

Learn how to monitor devices running Prisma Browser, and create device
groups.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The device directory provides a roster of your Prisma Browser devices and device
groups.

The page is tabbed so that you can choose which view you want to see:
Devices or Device Groups. The
Device Groups tab allows you to create and examine groups
of devices. This becomes important when defining rules and policies.

#### Manage Devices

1. From Strata Cloud Manager, select ConfigurationPrisma BrowserDirectoryDevices.

   You can see the total number of Prisma Browser devices displayed at
   the top of the page. By default, the Devices screen displays the first
   50 devices based on your sort order. Click Load 50
   More to move to the next page of devices.
2. Review the device data.

   The Device Directory allows you to see the details of each device, and
   includes the following information:
   - **Name**—The device's host name.
   - **User**—The Prisma Browser user's browser login name. Click
     the name to see user details, such as the devices and device groups
     associated with the user.
   - **IP address**—The device's external IP address.
   - **Device groups**—The number of device groups to which the device
     belongs.
   - **Browser version**—The browser version that's running on the
     device.
   - **Device type**—The type of device. The options are:
     - Desktop
     - Laptop
     - VM
     - Mobile
     - Unknown
   - **OS platform**—The operating system installed on the device
     (Windows, macOS, iOS, Android, Linux, Unknown).
   - **OS version**—The version of OS running on the device.
   - **Last seen**—The time the device last recorded an event to Prisma Browser. Hover over the field to see the full
     timestamp.

   ![]()
3. Investigate devices using search and filters.

   - Search by device name or user name.
   - Filter the devices based on Device Groups,
     OS platform, EPP
     status, Last seen date,
     Screen lock status, Disk
     encryption status, and Firewall
     status.
4. View details about a specific device.
   1. Click on a specific device on the list to see the device
      details.
   2. Review the device-specific details, including:

      - **User**—The device user's name.
      - **Device type**—The device type (desktop, laptop, VM,
        mobile, or unknown).
      - **OS platform**—The operating system installed on the
        device (Windows, macOS, iOS, Android, Linux, or
        Unknown).
      - **OS version**—The OS version installed on the
        device.
      - **Browser brand**—The name of the selected browser.
      - **Browser version**—The browser version running on the
        device.
      - **First Seen**—The elapsed time since the device first
        connected to the network. Hover over the field to see the
        full timestamp.
      - **Last Seen**—The time the device last recorded an event
        to Prisma Browser. Hover over the field to see the full
        timestamp.
      - **Model**—The device model.
      - **Device management**—The device management system that's
        managing the device.
      - **Serial number**—The device serial number.
      - **IP address**—The device's external IP address.
      - **User-Agent**—The request string that identifies the
        browser, device, and OS to network peers.
      - **MAC addresses**—The MAC addresses of the network cards
        installed on the device.
      - **Posture**—The status of the different posture
        requirements. Specific postures have a link to the details,
        and others have some additional information.
      - **Extensions**—The Extensions (if any) installed with the
        browser.
      - **Device Groups**—A list of the device groups to which
        the device belongs. Each group displays the relevant posture
        information, and a link to the device group.
      - **User Groups**—A list of the user groups to which the
        device user belongs.
5. Export device details for offline investigation.
   1. Click the Export icon.
   2. In the Export window, select one of the following options:

      - **Export all**—Export all device data.
      - **Export filtered data**—Export device details based on
        the current filters.

#### Manage Device Groups

The Prisma Browser has a device group function that allows you to create
different groups for different devices. Groups are dynamic. For example, you can
set up groups for specific managed devices, different subsidiary devices, or
contractors. As an administrator, you can exercise a considerable amount of
flexibility in configuring the device groups you need within your organization.
For example, groups meet changing business, operational, and organizational
circumstances. You can use device groups either with sign-in rules to set the
security bar for accessing Prisma Browser, or with posture-focused scoping
for policy rules. For managing mobile device groups, see Create, Edit, and
Delete Prisma Browser for Mobile Device Groups.

1. From Strata Cloud Manager, select ConfigurationPrisma BrowserDirectoryDevices and then select the Device Groups
   tab.

   ![]()

   You can see the total number of Prisma Browser device groups
   displayed at the top of the page. By default, the Device Groups screen
   displays the first 50 device groups based on your sort order. Click
   Load 50 More to move to the next page of
   devices.
2. Review the device group data.

   The Device Group Directory allows you to see the details of each device
   group, and includes the following information:
   - **Name**—The device group name.
   - **Type**—Prisma Browser, Mobile, Prisma Browser
     Extension, or Chromebook.
   - **Attributes**—Matching criteria for identifying which devices
     belong to the device group.
   - **Created at**—The device group creation date. Hover over the
     field to see the full timestamp.
   - **Updated at**—The device group last update date. Hover over the
     field to see the full timestamp.
3. Add a device group.
   1. From the Device groups tab, click
      Add device group.
   2. Name the device group.
   3. Select whether you want to create a device group for
      Prisma Browser endpoints or
      for Mobile devices.
   4. Select and configure the attributes that devices must match in
      order to be part of the device group.

      Attributes match against device criteria, such as whether the
      device has disk encryption enabled, active endpoint protection, or
      complex password policy requirements. Enforcing device group
      membership based on attributes provides a granular way for you to
      ensure that the devices Prisma Browser allows have good security
      posture. There are different attributes depending on whether you are
      creating a device group for [Windows and macOS
      devices](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html) or for mobile devices.
   5. Click Create.

   To edit or delete a device group, hover over the
   device group name in the director and click the pencil icon (to edit) or
   the trash icon (to delete).
4. Investigate devices using search and filters.

   - Search by name or id.
   - Filter the device groups based on Type,
     Attributes, Created
     at, and Updated at.
5. Export device details for offline investigation.
   1. Click the Export icon.
   2. In the Export window, select one of the following options:

      - **Export all**—Export all device group data.
      - **Export filtered data**—Export device group details
        based on the current filters.

---

<a id="manage-prisma-browser-device-groups"></a>

#### Manage Prisma Browser Device Groups

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/manage-prisma-access-browser-device-groups>*

Manage the Device groups in the Prisma Access Browser

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or Prisma Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser has a Device Group function, where you can create
different groups for different devices. Groups are dynamic; you can set up groups
for specific managed devices, specific posture attributes, specific user groups and
so on. You can perform the following

*Changes to device groups are saved to a draft
configuration and do not take effect until you publish the draft. For more
information, see Manage Configuration Versions (Draft Mode).*

Below the tab, you can perform the following tasks:

- **Search** the groups via the Device Group **name**.
- **Filter** the Device Groups based on the **Type** (Prisma Browser, Prisma Browser for Mobile, Prisma Browser Extension,
  Chromebook), the **Attributes** assigned to the device group**, Created
  at** date, or **Updated at** date.

The list of Device Groups allows you to see the group types, including the
following information:

- **Name** - The Device Group name.
- **Platform** - Prisma Browser, Prisma Browser for Mobile,
  Prisma Browser Extension, Chromebook
- **Attributes** - The specific criteria utilized to identify
  which devices belong to the Device Group.
- **Created at** - The date when the Device Group was created.
  Hover over the field to see the full timestamp.
- **Updated at** - The date when the Device Group was last
  updated. Hover over the field to see the full timestamp.

![]()

##### Export Device Groups

You can export a list of the device groups. The export file is saved in .csv
format.

1. Click the Export icon

   ![]()
2. In the **Export** window, select one of the following options:
   1. **Export all** - Export all of the device
      groups.
   2. **Export filtered data** - Export the data that
      is visible in the filtered list.
3. The data will be exported to a .csv file.

##### Create Device Groups

As an administrator, you can exercise a considerable amount of
flexibility in configuring the Device Groups needed in the organization. For
example, groups meet changing business, operational, and organizational
circumstances.

Device Groups can be used either with sign-in rules to set the security
bar for accessing the Browser, or with posture-focused scoping for policy
rules.

You can create new Device Groups as needed.

**To create a new Device Group:**

1. On the **Devices** screen, select the **Devices Group**
   tab.
2. Click **Add device group**.

   ![]()
3. In the Add device group window, do the following:
   - Enter a descriptive **Group name**.
   - Select the platform. In the case, click **Desktop browser**.

     The method is the same for the
     Prisma Browser for Mobile and the Prisma Browser
     Extension.

     ![]()
4. Select the **Device group attributes** that you want to use in the group.

   You can choose either positive or negative attributes. For more
   information, refer to [Device Posture
   Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html).

   - You can require the device group to include specific OS versions
     only. For example, your device group will only include devices
     running Windows 10 Pro, build 19045.
   - You can require the device group to include specific OS versions
     only. For example, your device group will ***Not*** include
     devices running Windows 10 Pro, build 19045. All other browser
     versions will be accepted.
5. Click **Create**. 

   ![]()

Mobile Device group attributes:

![]()

Extension Device group attributes: 

![]()

##### Rule Logic - AND vs. OR

When configuring sign-in rules with **Device Groups**, it’s important to
understand how criteria logic works. This section explains how to achieve
**AND** or **OR** behavior depending on how you group your
criteria.

**Default Behavior: AND Logic within a Single Device Group**

If you define multiple criteria **within the same Device Group**, the system
evaluates them using the **AND** operator. This means **all conditions must
be true** for the Device Group to apply.

**Example:**

- You create a Device Group with the following two criteria:

  - Operating System is **not** macOS
  - Device is **not** running Avira
- You apply this Device Group to a sign-in rule set to **Block**.

**Result:**

If a user attempts to sign in from a macOS device **without** Avira
installed:

- The OS **does not match** the "not macOS" condition (because it
  *is* macOS).
- The Device **does match** the "not Avira" condition.
- Since the Device Group uses **AND** logic, the rule does **not**
  match both conditions, so **sign-in is allowed**.

**How to Use OR Logic: Create Separate Device Groups**

To evaluate criteria using the **OR** operator, you need to create **two or
more separate Device Groups**, each with its own condition. Then, add all
of those Device Groups to the same sign-in rule.

**To create OR logic:**

1. Create one Device Group with the condition:

   - OS is **not** macOS
2. Create a second Device Group with the condition:

   - Device is **not** running Avira
3. In your sign-in rule (set to **Block**), select **both** Device
   Groups under the **Device Groups** option.

**Result:**

If a user signs in from a macOS device **without** Avira:

- The device does **not match** the first Device Group ("not
  macOS").
- But it **does match** the second Device Group ("not Avira").
- Since the rule uses **OR** logic across the two Device Groups,
  matching **either** group triggers the rule.
- Therefore, **sign-in is blocked** as expected.

---

<a id="configure-prisma-browser-device-posture-attributes"></a>

#### Configure Prisma Browser Device Posture Attributes

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes>*

Define the device posture attributes that determine device group
membership.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

In Prisma Browser, you can add attributes as match criteria when you [add or edit a device group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc).
Because Prisma Browser policy rules are enforced at the device group level, the
attributes provide granular security that ensures the devices that Prisma Browser allows to access your apps are adequately maintained and adhere with your
security standards before they are allowed access to your network resources. For
example, before allowing access to your most sensitive apps, you might want to
ensure that the devices accessing the apps have encryption enabled on their hard
drives. In this case, you would create a device group with an attribute that only
allows devices that have encryption enabled. The following sections detail the
attributes you can use to determine device group membership for Windows, macOS, and
Linux devices. Please use the relevant filter (Windows/macOS/Linux/IGEL) to filter
relevant and supported device group attributes per OS ”

With this feature, you can also select negative attributes. This means that you can
create a device group that does not include devices made by Dell.

To learn about the attributes for controlling device group membership for mobile
devices, see [Configure Prisma Browser Mobile Device Posture Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-mobile-device-posture-attributes.html).

![]()

##### Negative Postures

In some cases, you may want to **exclude** certain device attributes rather
than require them. This is called creating a **negative posture**.

For example, you might normally create a rule that **requires** devices to run
a specific operating system. However, if a new rule requires that devices
**must not** use that operating system, you can use a negative posture
instead.

This feature allows you to define rules that **explicitly exclude** certain
attributes—such as a particular operating system—from being allowed.

##### OS Versions

Creating a device group that uses the device's operating system as a posture is a
good way to make sure that users have specific versions of the OS. If you add an
OS version attribute as match criteria for a device group, Prisma Browser
checks the device OS version matches the attribute you defined before allowing
membership in the device group.

Define the list of acceptable operating system versions for the Prisma Browser posture mechanism to check as follows.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), add the OS version attribute.
2. Select the Windows, macOS, or Linux versions, editions, and build numbers
   to allow into the device group and then click
   Save.

   Windows build numbers should include the
   revision number as well. This helps ensure that the most up-to-date
   security patches and features are installed.

   ![]()
3. Click **Save**.

   **What does the Prisma Browser check?**

   *Windows devices*

   - Run the command WIINVER to open the About
     Windows information.

     ![]()
   - The command WMIC OS GET VERSION will also display the
     information, however if the version on the device was upgraded (for
     example, Windows 10 to Windows 11), the result may not be correct.
     In this case, use the WINVER command.

   *macOS devices*

   - In the System Settings, search or select "macOS."
   - Click **About**.

     ![]()

   *Ubuntu devices*

   - Via GUI settings - Go to *Show*
   - *Applications->Settings->System->About*

     ![]()

   Via command line - using following command - *cat
   /etc/os-release*

   ![]()

   *Fedora devices*

   - Via GUI settings - Go to *Show
     Applications->Settings->System->About*

     ![]()
   - Bia command line - use the following command. *cat
     /etc/os-release*

##### Serial Number

Creating a device group that uses device serial numbers as match criteria is a
good way to ensure that only specific devices have access to the Prisma Browser. Before you can add a serial number attribute to a device
group, you must create a .txt or .csv file containing the list of serial
numbers. The file you create can't exceed 600 KB.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), add the serial number attribute.
2. Drag and drop or browse for the file containing the list of serial numbers.
   The file must be in CSV or TXT format. The serial numbers must be separated
   by commas or semicolons, or in a file with one serial number per line.

   ![]()
3. If necessary, remove any serial numbers that you do not want to include in
   the group.
4. Click Set.

   **What does the Prisma Browser check?**

   While the serial number often appears on a sticker or label on the
   device, these numbers aren't always accurate. Use the following methods
   to get the correct serial number.

   *Windows devices*

   - Open a Command Prompt and enter the command wmic bios get
     serialnumber

     ![]()

   *macOS devices*

   1. In the System Settings, search or select "macOS."
   2. Click **About**.

      ![]()

##### Issuer Certificate

To ensure that only devices that use a client certificate signed by your
organization for authentication, create a client certificate attribute as match
criteria for your device groups so that you can distinguish between managed and
unmanaged devices. To use a client certificate attribute, you must upload the
intermediate certificate or intermediate or root certificate to create the
attribute. When determining if a client certificate matches the issuer
certificate in the attribute, Prisma Browser matches against the
authorityKeyIdentifier. If you need to trust
multiple CAs, you can upload multiple certificates.

Device groups can match against multiple certificates. To add a new Issuer (root
or intermediate) certificate:

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), add the client certificate attribute.
2. Drag and drop one or more certificate .PEM files to the Issuer certificates
   dialog.

   ![]()
3. Click Set.

   You need to upload **issuer certificates**
   that issued the **client certificates** located on the
   devices.

   **Client Certificate Requirements:**

   - Stored in the **Current User → Personal** stopr. [Windows
     only].
   - Valid Client Certificate with a private key attached.

   **Issuer Certificate Requirements**

   - Contains either the intermediate or both the intermediate and root
     chains that signed the client certificate.
   - It must not be the actual client certificate and should not contain
     a private key.

   - If you need to trust multiple CAs, then you can upload multiple
     certificates.
   - Prisma Browser matches the certificates'
     **authorityKeyIdentifier** when matching an issuer
     certificate to a client certificate

   **What does the Prisma Browser check?**

   *Windows devices*

   1. To manually verify a device meets the criteria, open the current
      user store, and select **Start > Manage user certificates**.
   2. Navigate to **Personal → Certificates** and validate:
      - Yjhe client certificate exists here.
      - The certificate contains a private key.
      - The issuer matches the issuer f the certificate.
      - You can compare the thumbprint of the certificates. 

        ![]()

   The authority key identifier matches the issuer certificate
   identifier.

   *macOS devices*

   1. From the Launcher, search for Keychain Access.
   2. Click **Certificates** and search for the required certificate.

      ![]()
   3. Validate that the company client certificate exists.
   4. Validate that the authority key identifier matched the issuer
      certificate identifier.

   ![]()

##### Disk Encryption

**Disk encryption** is a data security feature that converts data on a storage
device (like a hard drive or solid-state drive) into an unreadable format. This
process, known as **cryptography**, uses an algorithm to scramble the data
and an encryption key to lock and unlock it. Without the correct key, the
encrypted data appears as gibberish, making it incomprehensible and unusable to
unauthorized individuals.

**Key benefits:**

- **Data Confidentiality:** The primary benefit of disk encryption is
  protecting sensitive information, such as **Personally Identifiable
  Information (PII)** and financial records. If a device is lost or
  stolen, the data on the drive remains secure and unreadable to anyone
  without the key.
- **Regulatory Compliance:** Many industries and government regulations,
  such as **HIPAA** or **GDPR**, require strict data protection
  measures. Disk encryption is a fundamental tool for meeting these
  compliance standards and avoiding legal penalties.
- **Breach Prevention:** By encrypting data at rest, you significantly
  reduce the risk and impact of a data breach. Even if an attacker
  bypasses other security layers, the stolen data will be useless without
  the encryption key.
- **Security for Portable Devices:** Devices like laptops and external
  hard drives are highly susceptible to loss or theft. Disk encryption
  provides a crucial layer of security, ensuring that the data on these
  devices is protected wherever they are.

  If you previously used File System Encryption,
  you will be migrated to this feature as follows:
  - If **File System Encryption** was *Enabled*, then the
    **Disk Encryption** will be set to **Any Vendor**. You
    can then change it as needed.
  - If **File System Encryption** was *Disabled*, then the
    **Disk Encryption** will not be set, and you will need to
    configure it as needed.

  A device will be matched if at least one of the disks is
  encrypted.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the you can enable Disk Encryption.
2. Click the Disk Encryption check box, choose whether you need a positive
   (IS) or negative (IS NOT) and click **Select Vendors**.
3. Select the appropriate vendors you require for devices accessing your
   network.

   - Select **Any vendor** to include all vendors to include in the
     device group.
   - Filter by **Common vendors** to select from the most common
     vendors.
   - Filter by Selected only to create your own custom group of
     vendors.

   ![]()
4. Click Set.

##### Screen Lock

Active screen lock mechanisms limit device access to authorized users only,
preventing malevolent players from gaining access to confidential information on
the device in the event that the user steps away from the device. When you
enable the Active screen lock attribute in a device
group, Prisma Browser verifies that the device is enabled with an automatic
screen lock, password, PIN, biometric, or similar lock feature before allowing
access to the group. To pass this check, a device must meet the following
requirements:

*Windows device*

There are two locations where you can set the options for an active screen lock:

1. **Screen saver settings** - this setting can be left as *None*.
2. **Windows Power Settings**
   1. Open the **Screen Saver** settings (either option can be
      selected.

      ![]()
   2. Select On resume, display logon screen.
   3. Select a time in the **Wait** ***n*** **minutes**.
      This will be the time that the device will wait before
      activating the screen lock.
   4. Click **Apply**.

   ![]()

   The Active Screen Lock is now activated.
3. **Sign-in Options**
   - In the **Accounts > Sign-in** options, scroll to Additional
     settings.
   - In the field *If you've been away, when should Windows require
     you to sign in again?*, select one of the options.

     ![]()

     Selecting **Never** does
     not activate the screen lock.

     The Active Screen
     Lock is now activated.

     In Windows 10 devices, this
     option is found under Require sign-in.

     ![]()

*macOS devices*

The active screen lock for macOS devices is based on code that the Prisma Browser developers contributed to the Chromium project.

1. From the Apple menu select **System Preferences > Security &
   Privacy**.
2. If the lock icon on the lower left is locked, click it and enter the
   password.
3. In the **General** tab, in the Lock Screen section, select **Require
   password after screen saver begins or display is turned off**, and
   make sure there is a time value set. 

   ![]()

##### Endpoint Protection

Devices secured with active endpoint protection have antivirus, anti-malware,
firewall protection, and intrusion detection and prevention features, which work
in concert to identify and block malicious activity. If you enable the endpoint
protection attribute within the device group, Prisma Browser checks for
active endpoint protection before allowing the device into the device group. A
device must meet the following requirements to pass this check:

When configuring attributes to check for endpoint protection, you can select
specific endpoint protection vendors to check for on the device as follows:

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the endpoint protection attribute.
2. Select the endpoint protection vendors you require devices accessing your
   network to use. You can select **Any vendor** to include any endpoint
   protection vendor,

   ![]()
3. (Optional) Enable Verify definitions are up to date
   (supported vendors only) to add an additional check to
   ensure that the endpoint protection software on the device is
   up-to-date.
4. Click Set.

   **What does the Prisma Browser check?**

   *Windows devices*

   Prisma Browser checks the Endpoint Protection in the
   Windows Security Center. The posture check is made by checking that the
   Virus & threat protection is turned on.

   The **Security at a glance** page displays the Endpoint protection
   status of the device.

   ![]()

   Clicking on one of the icons above will display more detailed information
   regarding the installed EPP.

   ![]()

   *macOS devices*

   For macOS devices, Prisma Browser looks at the **Extensions** in
   the **System Preferences**.

   ![]()

##### Device Type

Use the device type attribute to ensure that the device group only contains
specific types of devices—such as laptops or desktops—as follows:

- **Windows devices**—Prisma Browser checks to see if the device is a
  laptop or desktop based on whether or not it has a battery.

  ![]()
- **macOS devices**—Prisma Browser checks the hardware device machine
  type.
- **VM Detection**—Prisma Browser looks at the way the particular
  operating system views the CPU. The result is based on the CPU internal
  datasets.
- **Unknown**—This is an atypical result. It is only applicable if the
  posture mechanism cannot determine the hardware properties.

If Prisma Browser can not determine the device type it identifies it as
unknown.

You can select the device type to include in your group by selecting the
appropriate type. 

![]()

##### CrowdStrike ZTA Scores

CrowdStrike Zero Trust Assessment (ZTA) delivers real-time security posture
assessments across all endpoints regardless of location, network, or user.
CrowdStrike ZTA enables enforcement of dynamic conditional access based on
device health and compliance checks that mitigate the risk to users and the
organization. Prisma Browser can use the ZTA assessment score as access
criteria.

To use the ZTA score as part of the device posture assessment for determining
access to Prisma Browser you must:

1. Enable the ZTA score calculation for all devices (Host setup and managementZero trust assessmenthosts).
2. Find your CrowdStrike Customer ID.

   You can find this inside your CrowdStrike user profile. Click on the
   account email to view this information. 

   ![]()
3. Open a support ticket with CrowdStrike to enable the ZTA feature
   flag.

   This allows Prisma Browser to access the CrowdStrike Agent ID. To open
   the support ticket, you will need the customer ID you just obtained.
4. Integrate the ZTA score with Prisma Browser.

   After CrowdStrike enables the ZTA feature flag, you can integrate with  as follows:

   1. When you [add or edit a device
      group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), select CrowdStrike ZTA
      Score.
   2. Select the type of score you want to use:

      - Basic—Use the overall score that
        CrowdStrike assigns to the device, based on a range of
        Low (at least 65),
        Medium (at least 70),
        Strict (at least 80), or
        Very Strict (at least 95).
      - Advanced—Fine-tune the configuration
        to select either a specific Overall security
        score, or a Score
        breakdown, based on the OS and sensor
        values. Use the sliders to select the required score.

      ![]()
5. Enter the CrowdStrike customer identification number
   associated with the CrowdStrike agent.

   Add additional CrowdStrike IDs as needed to connect
   to all agents.

   ![]()
6. Click Set.

##### OS Password Protection

Use the OS password protection attribute to restrict device group membership to
devices that are password protected. You can also specify that the device must
have additional password policy enforced, such as password complexity, maximum
age, or maximum length. To determine this, Prisma Browser looks for the
following settings on the device:

- **Windows devices**—Prisma Browser checks the following Password
  Policy settings in the local Security Settings (Security SettingsAccount PolicyPassword Policy): Maximum password age,
  Minimum password length, and Password
  must meet complexity requirements.

  ![]()
- **macOS devices**—Prisma Browser checks the local password
  requirements in the management configuration profile (ManagementConfiguration profilesAddmacOSPassword): Allow simple value,
  Require alphanumeric value, Minimum
  length, Munimum number of complex
  characters, Expiration age, or
  History restriction. 

  ![]()

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the OS password policy attribute.
2. Select the endpoint protection vendors you require devices accessing your
   network to use.

   ![]()
3. Select the password policy settings that must be enforced on devices for
   inclusion in the device group.
4. Click Save.

##### Device Manufacturer

Use the device manufacturer attribute to restrict device group membership to
Windows or macOS devices from selected manufacturers.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the device manufacturer attribute.
2. Select the device manufacturers you want to support in the device
   group.

   ![]()
3. Click Save.

##### System Integrity

Use the system integrity attribute to ensure that the device group only allows
devices that have advanced system integrity protection enabled. Prisma Browser determines if a device qualifies as follows:

- **Windows devices**—Prisma Browser checks to ensure that driver test
  signing is off and no kernel debugger is present. Additionally, on UEFI
  computers, it verifies that secure boot is enabled.
- **macOS devices**—Prisma Browser checks to ensure that System
  Integrity Protection (SIP) and Gatekeeper are enabled.

##### Normal OS Boot Mode

Enable this attribute to create a device group that requires the devices to run
in full boot mode. This excludes devices that are running in safe mode, recovery
mode, or devices running in a pre-installation environment.

##### Privileged Process

This attribute allows you to create device groups where the Prisma Browser
runs without any elevated or root permissions.

##### Device Management

This attribute allows you to create device groups that use approved device
management systems. The Prisma Browser supports the following systems:

- Microsoft Intune
- Azure AD
- Active Directory (Windows only)
- Jamf (macOS only)

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the device management attribute.
2. Select the device management systems you want to allow in the device
   group.

   ![]()
3. Click Set.

##### **Registry Keys (Windows only)**

The Registry Key attribute allows you to create policy and posture rules based on
the existence of a particular custom attribute that is placed in the Registry
Keys. Using this feature, you can use more than one key as part of the device
group; Prisma Browser will make sure that the devices will have all of the
keys that were selected.

1. Select *is / is not* to determine if the requirement is a positive
   attribute (the key exists in the device) or a negative (the key does not
   exist in the device).
2. Click **Configure**.

   ![]()
3. Enter the full path of the key that forms the group. For example -
   HKEY\_CURRENT\_USER\Control Panel\Desktop.
4. Enter the Value name (optional) and a Value type (optional). 

   ![]()
5. Click **Set**.

##### Processes

The Processes attribute allows you to create device posture rules based
on whether or not specific processes are running. This feature allows you to
create Device Posture Attribute rules for computers running both Windows and
macOS systems. This means that you can create one attribute for both.

When this attribute is selected, the Prisma Browser will make sure
that the specified process is running (or not running) as you require.

1. Select **Processes**.
2. Select *is / is not* to determine if the requirement is a positive
   attribute (the process is running in the device) or a negative (the process
   is not running in the device).

   ![]()
3. Click **Configure**.
4. In the **Processes** window, do the following for each process that you
   need to add:
   1. Click **Add Process**.
   2. Select the operating system related to the process. You can select
      Windows or macOS.
   3. Enter the Process name on the process path.
   4. Optionally enter the **Team ID** (macOS) or the **Certificate
      Thumbprint** (Windows):
      - For machines running **macOS**:
        1. Open the Terminal.
        2. Enter the code codesign -dv
           followed by the full file path.
           - For example codesign -dv
             '/Applications/Prisma Access
             Browser.app/Contents/MacOS/Prisma Access
             Browser' will provide te Team ID for the
             Prisma Browser.
      - For machines running **Windows**:
        1. Locate the Process.
        2. Right-click on the process and select Properties.
           1. On the Digital Signature tab, select the
              required certificate and click Details.
           2. The Digital Signature Details window is
              displayed. Click View Certificate.
           3. On the Details tab, save the Thumbprint.
   5. Click **Set**.

      ![]()

**Locating Processes on macOS machines**

Open the Activity Monitor, locate the process, double click, and copy the
executable path,

Or use the process name from the Activity Monitor. 

![]()

![]()

**Locating Processes on Windows machines**

Process must have a .exe extension.

Open the Task Manager, right click on one of the columns, and copy the
information from the Process Name column.

![]()

![]()

![]()

##### Files

The Files attribute allows you to create device posture rules based on
whether or not specific files located on the machine. This feature allows you to
create Device Posture Attribute rules for computers running both WIndows and
macOS systems. This means that you can create one attribute for both.

When this attribute is selected, the Prisma Browser will make sure
that the specified files are located on the machine.

1. Select **Files**.
2. Select *is / is not* to determine if the requirement is a positive
   attribute (the file is located on the device) or a negative (the file is not
   located on the device).

   ![]()
3. Click **Configure**.
4. In the **Files**  window, do the following for each file:
   1. Click **Add File**.
   2. Select the operating system related to the process. You can select
      Windows or macOS.
   3. Enter the File Path.
   4. Optionally enter the **Team ID** (macOS) or the **Certificate
      Thumbprint** (Windows):
      - For machines running **macOS**:
        1. Verify that a process is running on the device
           and is signed by the specified Apple Team ID.
        2. Enter the code codesign -dv
           followed by the full file path.
           - For example codesign -dv
             '/Applications/Prisma Access
             Browser.app/Contents/MacOS/Prisma Access
             Browser' will provide te Team ID for the
             Prisma Browser.

           ```
           codesign -dv '/Applications/Prisma Access Browser.app/Contents/MacOS/Prisma Access Browser'
           ```

           ![]()
      - For machines running **Windows**:
        1. Locate the Process.
        2. Right-click on the process and select Properties.
           1. On the Digital Signature tab, select the
              required certificate and click Details.
           2. The Digital Signature Details window is
              displayed. Click View Certificate.
           3. On the Details tab, save the Thumbprint.
   5. Click **Set**.

   ![]()

##### Browser Version

In some cases, administrators may not have full control over browser deployment
through MDM services and must rely on users to manage their own browser updates.
Additionally, browser end-of-life status can sometimes be overlooked or
forgotten. As a result, outdated browser versions may continue to run, exposing
systems to vulnerabilities and other risks.

To address this, Prisma Browser now lets you create device groups based on
whether a browser has reached its end of life.

Browser Version support is available on Windows and macOS platforms.

![]()

##### OS Location Services

The Prisma Browser uses two methods to detect a user's location:

- OS Location Service (requires specific permissions)
- GeoIP

The Location Service uses system-level APIs to obtain precise,
real-time geographic coordinates, provided the necessary permissions are
granted. This method is preferred for its high level of accuracy and
consistency. Prisma Browser can now enforce the use of the operating
system’s native Location Services to ensure more reliable and precise location
data.

In contrast, GeoIP-based location determination relies on IP address
mapping, which is inherently less accurate. GeoIP results can be affected by
various external factors, leading to potential inaccuracies.

OS Location Services support is available on Windows and macOS platforms. 

![]()

###### Locating the OS Location Service Configuration

**macOS**

Open **System Settings → Privacy and Security → allow applications to access
your location**.

**Windows**

Open **Settings → Privacy and Security → App permissions → Location → Let
apps access your location**.

##### Firewalls

This feature gives you greater security and compliance control over device
access. Now, you can configure granular access policies using a new
**"Firewall"** device group attribute.

This new attribute allows you to permit any firewall vendor or select specific,
approved vendors from an expanded, categorized list. The system also gives you a
more comprehensive view of all detected firewall products and their status.

Older browser versions will continue to detect only
native firewalls until you install a new version.

---

<a id="live-session-streaming"></a>

#### Live Session Streaming

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/co-browsing>*

Describes how Live session Streaming works

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

Live session Streaming enables admins to connect to endpoint users to share a web session
in real time. This functionality is commonly employed in customer support, collaborative
workflows, and training scenarios. Additionally, Live session Streaming is critical for
overseeing sensitive configuration processes frequently performed by external
contractors, as these processes can impact secure systems. It creates a continuous
record of your users' activities, and provides you with a better view of the user
experience.

Existing solutions often depend on third-party applications, introduce latency, or
compromise security, and require elevated permission. By embedding Live session
Streaming capabilities directly into enterprise browsers, organizations can enhance
control, ensure compliance, and deliver a clean user experience. Live session Streaming
establishes secure, low-latency peer-to-peer connections, making it an optimal framework
for enterprise-grade implementations.

The Prisma Browser

##### Why Use Live Session Streaming?

There are many uses for Live session Streaming, all of which are designed to make
your management easier.

There are cases when you need to make sure that contractors, using unmanaged devices,
and having temporary access to sensitive data or critical systems, are following
security protocols. You need real-time monitoring to keep track of these users, and
they might not want to install intrusive third-party tools on their machines.

There are also situations where you need live troubleshooting to assist your users
with issues that they are having. Live session Streaming allows you to join the user
and see exactly what the issues are on their machines. Without this feature, you
need a variety of third-party tools that need to be installed on your machine as
well as on your user's, and configured properly. With Live session Streaming, all
the tools that you need are in the Prisma Browser.

##### Using Live Session Streaming

Live session Streaming can be accessed from two places in the Prisma Browser
Management Console.

- From the **Users Directory**.
  1. Search for the user who needs Live session Streaming. You can search by
     email.
  2. Click on the user to open the User drawer.

     The information in the
     drawer lists the available devices. Devices that are online will
     have a Request Live Stream icon. Click the icon to request live
     streaming. 

     ![]()
  3. Click the icon to send a request to the user, asking for permission to
     live stream.
- From the **Devices Directory**.
  1. Search for the device by the Device name or User,
  2. Hover on the online device to display the Request Live session icon.

     ![]()

     ***OR***

     Click on the device to open the Device
     drawer. The icon will be displayed.

     ![]()

###### Making a Live Session Streaming Request

The Live Stream session is limited to 30 minutes.

1. Once you click the icon, the Live Stream window will display. Click
   **Request** to begin.

   ![]()
2. When you make the request, the user will receive a button next to the
   address bar. They can accept the request and select what information that
   they want to share in the session:
   - **Tab** - Restrict the session to the information displayed in a
     single tab.
   - **Window** - Restrict the session to the information displayed in
     a window (which may contain multiple tabs).
   - b**Screen** - The Live session Stream will show all the
     information on the monitor.

   A Live Stream session is limited to 30
   minutes. It can be terminated by either you or the user.
3. When you're finished with the session, click **Terminate**.

   ![]()

   Click Terminate to confirm that you want to end the session.

   ![]()
4. When the session is over, you can download a recording of the session. 

   ![]()

   The session file is saved in \*.webm
   format. You can view this file in the Prisma® Access
   Browser.

Relevant information regarding the Live session
Recordings are saved to the Audit Log.

---

<a id="configure-prisma-browser-extension-posture-attributes"></a>

#### Configure Prisma Browser Extension Posture Attributes

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-extension-device-posture-attributes>*

Define the device posture attributes that determine which Devices can join the
device group.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

In Prisma Browser Extension, you can add attributes as match criteria when you
[add or edit a device group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc).
Because Prisma Browser policy rules are enforced at the device group level, the
attributes provide granular security that ensures the devices that Prisma Browser Extension allows to access your apps are adequately maintained and adhere with
your security standards before they are allowed access to your network resources.
For example, before allowing access to your most sensitive apps, you might want to
ensure that the devices using the Prisma Browser Extension accessing your apps
are using only the Opera browser. In this case, you would create a device group with
an attribute that only allows devices using the extension that are only using the
Opera browser. The following sections detail the attributes you can use to determine
device group membership for devices using the Prisma Browser Extension.

To learn about attributes for managing device group membership on Windows and macOS
devices, see [Configure Prisma Browser Device Posture Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html)

##### Negative Postures

In some cases, you may want to **exclude** certain device attributes rather
than require them. This is called creating a **negative posture**.

For example, you might normally create a rule that **requires** devices to run
a specific operating system. However, if a new rule requires that devices
**must not** use that operating system, you can use a negative posture
instead.

This feature allows you to define rules that **explicitly exclude** certain
attributes—such as a particular operating system—from being allowed.

##### Windows and macOS OS Versions

Creating a device group that uses the device's operating system as a posture is a
good way to make sure that users have specific versions of the OS. If you add an
OS version attribute as match criteria for a device group, Prisma Browser
checks the device OS version matches the attribute you defined before allowing
membership in the device group.

Define the list of acceptable operating system versions for the Prisma Browser posture mechanism to check as follows.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), add the OS version attribute.
2. Select the Windows or macOS versions, editions, and build numbers to allow
   into the device group.

   Selecting **All...versions**will use all historical versions of the operating systems, including
   those that re deprecated it yes.

   ![]()

   Selecting **All...versions**will use all historical versions of the operating systems, including
   those that re deprecated it yes.
3. Click **Save**.

##### Browser Brands

Enable the Browser Brands attribute to ensure that the
device group only contains specific types of browsers—such as Chrome, Edge, or
Brave. This can be especially useful when you need to create specialized rules
for different browsers.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the Browser Brands
   attribute.
2. Select the browser brands you want to support in the device group.

   ![]()
3. If you need to restrict the browsers to specific versions, click the pencil
   icon, and in the Specific brand version, enter the Minimum version of the
   browser that is acceptable.

   ![]()
4. Click Set.

---

<a id="configure-prisma-browser-mobile-device-posture-attributes"></a>

#### Configure Prisma Browser Mobile Device Posture Attributes

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-mobile-device-posture-attributes>*

Define the device posture attributes that determine which mobile devices can join the
device group.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

In Prisma Browser, you can add attributes as match criteria when you [add or edit a device group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc).
Because Prisma Browser policy rules are enforced at the device group level, the
attributes provide granular security that ensures the devices that Prisma Browser allows to access your apps are adequately maintained and adhere with your
security standards before they are allowed access to your network resources. For
example, before allowing access to your most sensitive apps, you might want to
ensure that the mobile devices accessing your apps are not rooted or jailbroken. In
this case, you would create a device group with an attribute that only allows mobile
devices that are not rooted or jailbroken. The following sections detail the
attributes you can use to determine device group membership for mobile devices. To
learn about attributes for managing device group membership on Windows and macOS
devices, see [Configure Prisma Browser Device Posture Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html)

![]()

##### Negative Postures

In some cases, you may want to **exclude** certain device attributes rather
than require them. This is called creating a **negative posture**.

For example, you might normally create a rule that **requires** devices to run
a specific operating system. However, if a new rule requires that devices
**must not** use that operating system, you can use a negative posture
instead.

This feature allows you to define rules that **explicitly exclude** certain
attributes—such as a particular operating system—from being allowed.

##### Root/Jailbreak Status

Enable this attribute to create a device group that only allows mobile devices
that have not been rooted or jailbroken.

##### Active Screen Lock

Active screen lock mechanisms limit device access to authorized users only,
preventing malevolent players from gaining access to confidential information on
a mobile device. When you enable the Active screen lock
attribute in a device group, Prisma Browser verifies that the device is
enabled with an automatic screen lock, password, PIN, biometric, or similar lock
feature before allowing access to the group.

##### iOS and Android OS Versions

Creating a device group that uses the device's operating system as a posture is a
good way to make sure that users have specific versions of the OS. If you add an
OS version attribute as match criteria for a device group, Prisma Browser
checks the device OS version matches the attribute you defined before allowing
membership in the device group.

Define the list of acceptable operating system versions for the Prisma Browser posture mechanism to check as follows.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), add the OS versions
   attribute.
2. Select the iOS or Android versions, minimal minor versions, and minimal
   security patch level to allow into the device group.
3. Click Save.

   ![]()

##### Device Type

Enable the Device type attribute to ensure that the device
group only contains specific types of devices—such as smartphones or tablets.
This can be especially useful when you need to create specialized rules for the
different devices.

![]()

##### Device Manufacturer

Enable the Device manufacturer attribute to restrict
device group membership to Android devices from selected manufacturers. This
attribute is supported for Android devices only; it does not support iOS
devices.

1. When you [add or edit a device
   group](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#task-hns_lt1_gcc_substeps-lrz_dz4_gcc), enable the Device manufacturer
   attribute.
2. Select the Android device manufacturers you want to support in the device
   group.

   ![]()
3. Click Set.

---

<a id="manage-prisma-browser-applications"></a>

### Manage Prisma Browser Applications

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-applications>*

Learn how to view and manage applications and application groups for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser comes equipped with a predefined list of Verified
applications. The Verified applications list references the Palo Alto Networks
App-ID™ catalog of applications, and is regularly synced with the cloud database.
The full application list is located in the Applipedia (<https://applipedia.paloaltonetworks.com/>), and more applications are
added to the Prisma Browser every day.

Additionally, you can create your custom applications if it is not included in the
cloud database.

*Changes to applications and
application groups are saved to a draft configuration and do not take effect
until you publish the draft. For more information, see Manage Configuration
Versions (Draft Mode).*

While the Prisma Browser uses the same application list generated
by the App-ID classification system as other Palo Alto Networks products, the
verified applications list might use a different naming schema compared to other
platforms. As a result, the application list found in the Prisma Browser
might differ in its naming conventions.

Applications have dynamic lifecycles. New applications
consistently join our catalog, while we remove others as they reach end-of-life,
face acquisition, or cease to exist. If a policy rule references an application we
deprecate, the UI immediately generates an alert, notifying you of the
change.

The application screens serve several purposes:

- They generate statistics, allowing you to understand how workflows
  operate in the company.
- You can incorporate the applications into Rules, allowing you to
  create workflows using only predefined applications and services.
- Use of the Applications Directory provides information that can be
  sent to the Dashboards.

The application list displays the details of each application, and includes
the following information:

- Name - The application name.
- Source – The source of the application; either from the
  catalog or customized.
- Category - The optionally configured category for the
  application. If the application isn't categorized, it will be listed as
  Uncategorized.
- Risk -The site reputation: Ok, Moderate, or Danger. Hover
  over the value to see the Risk Score.
- Rules - The number of policy rules where the application is
  included. This also includes rules that include “any” application.
- Updated - The date when the application information was last
  updated. Hover over the field to see the full timestamp.

![]()

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Search for specific applications.
3. Filter the applications based on specific options:

   - - Application Source - Filter by the
       application source - either Catalog - from the App-ID
       catalog, or Custom - a private application stored at the
       data center.
     - Category - The optionally configured
       category that can be selected for each application.
     - Risk - The reputation of the application -
       OK, Medium, or Danger.
     - Application groups - The groups that you can
       use to help manage the groups.
     - Is GenAI - Applications from the
       catalog that contain AI functionality.
     - Last updated – The date and time the application was
       last updated.
4. Select an application to open the application drawer. The drawer contains some
   additional information regarding the application.

   - Time Frame - Allows viewing of the graphs for
     specific periods. This allows you to see how the selected
     application is used over time. Select from the following time
     frames:

     - Last 24 hours
     - Last 3 days
     - Last 7 days
     - Last 14 days
     - Last 30 days

     Graphs - display specific information that can
     be useful for examining application usage. Click on See more for
     additional information. The following information is displayed in
     the graphs:

     - Total active users
     - Total access events
     - Total data events
     - Total volume sizeMetadata - view different metadata information that is
     associated with the applications.

#### Add a Custom Application

You have a considerable amount of flexibility when it comes to creating new
application entries on the Applications Directory. Whenever you need an
application that isn't one of the verified applications included with the Prisma Browser, you can create a new, custom application.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. On the Application screen, click Add custom app.
3. On the Add custom application window, enter the following
   information:

   1. Name - The name of the application. You can
      enter any name, and are not restricted to any application
      name.
   2. URLs - The URLs for the application. For more
      information on using the URL builder, click here. After you
      enter the URL, Add.
   3. Categories - You select entire classifications
      (categories) to add to the rule. The classification is divided
      into two categories - Malicious (for example, Phishing sites,
      Ransomware, Grayware) and Benign (for example, News and Media,
      Dating, Shopping).

   For more information, refer to [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-basics/url-categories).
4. Add.
5. The application will be added to the list of applications.

   **URL Limits**

   There are two types
   of URL Limits that apply to Custom Applications:
   1. Tenant-level URL limit:
      - A maximum number of URLs are allowed per tenant.
      - This represents the sum of all URLs across all
        custom applications.
   2. Custom application URL limit
      - A maximum number of URLs are allowed per custom
        application. The limit is 100 URLs per custom
        application.
      - Once the limit is exceeded, the application blocks
        additional URLs, and displays an error message.
      - There is a limit of 15,000 custom URLs permitted
        across all applications.

#### Edit a Custom Application

After you add a custom application, you can edit
it.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Click the pencil icon on the right side.
3. Make the required changes.
4. Save changes.

#### Delete a Custom Application

If you no longer need a custom application, you can
delete it.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Locate the custom application that you no longer need and hover on the
   entry.
3. Select the trash bin icon on the right side.
4. Delete at the prompt to confirm.

   If the custom application is linked to an
   existing rule, you need to disconnect it from the rule before deleting
   it.

#### Add a Private Application

Private applications are applications that your enterprise manages internally.
The application remains in your data center, and is only accessible by internal
users who have the appropriate permissions.

The Prisma Browser handles these applications separately from custom
applications. Private applications require that you configure the FQDN and
additional IP addresses that are required for using the application.

You can configure access to a wider set of private apps
by using wildcards.

Wildcards are supported **only** at the beginning of
subdomains.

For example: \*.[example.com](http://example.com/) or \*.[shop.example.com](http://shop.example.com/)

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. On the Application screen, click Private
   Applications and then Add private
   app.
3. On the Add private application window, enter the following
   information:

   1. Name - The name of the
      application. You can enter any name, and are not restricted to
      any application name.
   2. Application URL - The URLs for
      the application.
   3. **FQDN or IP Address** for the application.

      1. Once the URL and its associated FQDN is
         entered, click **Add**.
   4. **Categories** - If needed, you can manually assign a category
      for this application from a predefined list.
4. ClickAdd.
5. The application will be added to the list of applications.

   ![]()

#### Edit a Private Application

After you create private applications, you can modify
them by adding or removing URLs or FQDN, or changing the category.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Locate the application that you need to edit and hover on the entry.
3. Select the pencil icon on the right side.
4. Make the required changes.
5. Save.

#### Delete a Private Application

If you no longer need a custom application, you can
delete it.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Locate the custom application that you no longer need and hover on the
   entry.
3. Select the trash bin icon on the right side.
4. Delete at the prompt to confirm.

   If the private application is linked to an
   existing rule, you need to disconnect it from the rule before deleting
   it.

#### Add Remote Connections

Remote connections are non-web apps that are based on the Native RDP/SSH
protocols. For more information, refer to [Configure Native RDP/SSH](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-applications/configuring-native-rdp-ssh).

#### Add an Application Group

After you create your applications, you can now create
Application Groups and assign policies to these groups. Any changes to the content
of an Application Group will automatically update the list of apps in the assigned
policy. Application Groups can contain a mix of any app type (from catalog, custom,
and private).

You can use application groups for scenarios such as:

- Manage Policy at Scale: You can organize
  your apps into different groups and set basic rules for each group. This
  way, you can add or remove apps from the groups without needing to
  change the rules themselves.
- Management Tool: When you are managing hundreds of
  applications, you can use groups to better organize and contextualize
  applications. For example, you can create groups for internal QA/Staging
  vs. Production environments, internal productivity apps, or apps
  containing PII or sensitive information, even if you do not want to
  assign a rule to them.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications, select the Application Group
   tab.
2. Select + Add application group.
3. On the Add application group window, enter a Name for the group, an
   optional Description for the group.
4. Select the down arrow and select the applications to add to the group. You
   can filter the applications by the application Catalog, Private
   applications, or Custom applications. Additionally, you can search for
   specific apps.
5. After you have chosen the applications to add to your group,
   Save, and the group will be added to the
   list.

   ![]()

#### Edit an Application Group

After you create the Application Groups, you can
modify them by adding or removing applications.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Locate the application group that you need to edit and hover on the
   entry.
3. Select the pencil icon on the right side.
4. Make the required changes.
5. Save.

#### Delete an Application Group

If you no longer need an application group, you can
delete it.

If the Application Group is linked to an
existing Rule, you need to disconnect the group from the rule before deleting
it.

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryApplications.
2. Locate the application group that you no longer need and hover on the
   entry.
3. Select the trash bin icon on the right side.
4. Delete at the prompt to confirm.

---

<a id="configure-native-rdpssh"></a>

#### Configure Native RDP/SSH

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-applications/configuring-native-rdp-ssh>*

Guide to configure RDP/SSH

Native RDP/SSH is a feature in Prisma Browser that allows you to access
RDP (Remote Desktop Protocol) and SSH (Secure Shell) applications **without the
need for additional licenses.**

RDP connections can route through an RDS Gateway instead of requiring direct
connections.

**Key Changes Upon Activation:**

- Native RDP takes precedence over PRA (Prisma Access Remote Access)
  and Remote Connections will no longer work via Prisma Browser on the
  tenant.
- A new option, **Remote Connection,** appears under the
  **Applications Tab**.

  ![]()
- When specifying an Access and Data Control rule, options related to Remote
  Connections can be found under Access and Data Control Rule → Applications →
  Remote Connections.

  ![]()

##### Configure the Native RDP/SSH

**A. Applications Tab (Remote Connections)**

In the Applications directory, do the following:

1. Click the **Remote Connections** tab and click **Add Remote
   Connection**.
2. In the **Add remote connection** window, enter the
   information as needed.
3. Be sure to configure the **Remote Connection** using an
   **FQDN** (Fully Qualified Domain Name), an **IP address**, or
   a **PC Name** (the server where the application resides).
4. The configuration supports **non-standard ports**.

   1. The standard RDP port is 3389
   2. The standard SSH port is 22
5. Select the Classification for the connection. The options are:
   - **Sanctioned:** A Remote Connection that is permitted.
   - **Tolerated:** A Remote Connection that is allowed, but is not
     sanctioned by the organization.
   - **Unsanctioned:** The connection is not authorized by the
     organization at all.
   - **Unclassified:**  The connection has not yet been
     classified.
6. In the **Additional settings** section, select the following:
   - **Tags**, if needed
   - **Routing:** Select whether or not to route the Remote Connection
     through Prisma Access.
   - **RDS Gateway:** When this field is populated, the FQDN/IP/PC
     Name address field above no longer requires FQDN or IP address
     validation. Users can enter a PC name instead.

![]()

**B. Access and Data Control Rule**

- The rule creation flow remains the same as for any other
  application.
- Within the **Remote Connection Application** settings,
  - First, check to enable the Remote connections setting for your
    rule. This allows users to view and establish remote connections
    from the Prisma Browser.

    When this option is enabled, users
    can access remote connection capabilities in the browser.
    You can control which remote connections are available to
    users by configuring one or both of the following options:
    - **Administrator-Defined Remote
      Connections**

      Allow usders to access remote
      connections that were created and managed by an
      administrator.

      **You can select one of the
      following options:** 
      - **Any defined connection** — Users can
        access any remote connection defined by the
        administrator.
      - **Specific connections** — Users can access
        only the remote connections selected in the
        rule.

      Use this option when administrators
      need to control which RDP, SSH, or other supported
      remote connection targets are available to
      users.
    - **Any Remote Connection Using Manual
      Connect**

    Allow users to manually create remote
    connections from the Prisma Browser**.**

    When this
    option is enabled, users can add their own remote
    connections from the Remote connections settings panel in
    the browser by selecting “**+ New
    connection**.”

    Use this option when users need the
    flexibility to connect to remote resources that were not
    preconfigured by an administrator.

For tenants with Prisma Access entitlement, all traffic
associated with user-created applications established through the manual
connections option is routed through Prisma Access by default.

##### Enable Native RDP/SSH

RDP does not support Session Recording

To enable and fully utilize the Native RDP/SSH feature, follow these steps:

1. Configure a Remote Connection under the Applications directory.
2. Create an Access and Data Control Policy allow access to the newly
   configured Remote Connection.
3. Create a Security Policy under Explicit Proxy (EP).
   - This step is necessary to allow access to RDP/SSH applications that
     may reside within your data center.
     1. Navigate to **Configuration** > **NGFW and Prisma
        Access**.
     2. Change the Configuration Scope to **Prisma Access** or
        **Explicit Proxy**.
     3. Create a Security Rule in Explicit Proxy with the following
        parameters:
        - **Source:** Trust
        - **Destination:** Any or Specific Location
        - **Applications:**
          ms-RDP and
          SSH
        - **Action:** Allow

        You may need to duplicate
        these policies on other intermediaries, such as the
        Next-generation Firewall (NGFW), that are in the path to
        your private applications.

        Once a port is selected, it cannot
        be changed in any way. You need to define a new
        application with the desired port.

###### Migration from Remote Connections

Native Clients and Remote Connections/PRA **cannot co-exist** in Prisma
Browser. Remote Connections/PRA must be disabled first for Native RDP/SSH to
work.

If Remote Connections/PRA is currently not
enabled on your tenant, you must request that this feature be added by
contacting your customer-success manager.

1. **Take Note of All Configurations:** Before
   disabling, record all existing Remote Connection configurations
   as you will need to manually reconfigure the applications and
   update the policies later.

   - *Self-Correction: You will need this
     information to re-configure the apps as Remote
     Connection Apps.*
2. **Disable Remote Connections:**

   - Navigate to **Administration** > **Remote
     Connection**.
   - Disable the toggle switch.

1. **Configure Remote Connection Apps:** Once disabled,
   **Remote Connections** will be renamed to **Remote
   Connection Apps** in the administration screens. You can
   now configure the applications and policies for the new
   feature.
2. **Follow the Enablement Steps:** Proceed with the
   steps outlined in **Enable Native RDP/SSH**.

###### User Experience

Users access the Remote Connections feature through the Prisma
Browser client interface.

1. Click on the **Prisma Browser Profile Icon**.
2. Click on **Remote Connections**

   ![]()

   This will open a list of the available remote connections.
3. Select the remote connection that you need, and click
   **Connect**.
4. In the window, enter your username and password.
5. Select the check boxes you need. Select *Use these credentials for
   gateway* to apply the entered credentials to both the remote
   connection authentication and the gateway authentication..
6. Click **Connect now**.

This will open a new tab for Remote Connections where the user can
view:

- All RDP/SSH applications allowed per the policy created by
  the administrator.
- An option to add **"New Connections,"**
  *if* the **Manual Connect** option is enabled for their
  profile/scope.

**Connection Management:**

- Connections **defined by the user** can be **Edited**
  or **Deleted** from the list.
- Connections **defined by the administrator**
  **cannot** be edited by the user.

Only 1 additional connection can be defined with the
same IP/FQDN. This means that a maximum of 2 IP/FQDNs can share the same
connection.

---

<a id="manage-prisma-browser-extensions"></a>

### Manage Prisma Browser Extensions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-extensions>*

Learn how to view and manage extensions for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser maintains an Extension directory that includes extensions
installed by end-users on the browser. This information allows you to maintain
proper corporate policy management, manage visibility and risk analysis.

The Extension list displays details of each Extension, and includes the following
information:

- **Name** - The Extension name.
- **Users** - The number of users who have installed the extension
  on their devices.

  If there are more users than devices, it indicates that some
  devices are being used by multiple users..
- **Devices** - The number of devices where the extension is
  installed. If there are more users than devices, it indicates that some
  users have access to multiple devices.
- **Risk score**- Risk for an extension is determined by a
  combination of the risk impact and the risk likelihood considering its
  permissions, credibility of the reviews, and the reputation of the extension
  publisher. The higher the risk score, the greater the chance that the
  extension is malicious.

  In Prisma Browser, the malicious extension is blocked, and will be
  completely removed from the user's device. For Prisma Browser Extension,
  the malicious extension is disabled.

  You can hover over the Extension's Risk score to see the actual score `(pit
  of 5). The scores and the risk level are as follows:

  - **Low** - Score between 1-2
  - **Medium** - Score of 3
  - **High** - Score between 4-5
- **Extension ID** - The identification number of the extension. The ID
  links to the source of the extension.

![]()

1. From Strata Cloud Manager, ConfigurationPrisma Browser
   DirectoryExtensions.
2. Search for specific applications by name or Extension
   ID.
3. **Filter** the applications based on specific options:

   - **Source** - Filter the list by the original source of
     the extension.
   - **Status** - Filter the extensions based on whether or
     not the extension is in use or not.
4. Select an extension to open the extension drawer. The drawer contains some
   additional information regarding the extensions.

   - **Installation source** - Displays the source of the
     installation. There can be more than one source for the
     extension.
   - **Extension ID** - The identification number of the
     extension. The ID links to the source of the extension.
   - **Risk score**- The Risk Score is determined based on
     the extension's permissions, source code analysis, credibility of
     reviews, and the publisher's reputation. The score falls into the
     following ranges:

     - **Low** - Score between 0-2
     - **Medium** - Score of 3
     - **High** - Score between 4-5
   - **Risk likelihood** - This value determines the
     likelihood of an extension becoming malicious. The score falls into
     the following ranges:

     - **Low** - Score between 0-2
     - **Medium** - Score of 3
     - **High** - Score between 4-5
   - **Risk impact** - This value measures the impact of the extra
     permissions an extension can access. A high risk impact means that the
     extension has access not more sensitive permissions.
   - **Manifest** - The version of the Manifest platform that is
     used.
   - **Global stats**- Displays the basic global statistics
     from ChromeStats data. The information includes:

     - **Download count** - The number of times that
       the extension was downloaded.
     - **Rating** - The global rating for the
       extension.
     - **Last version update** - The last time that the
       publisher issued an update and version number.
   - **Overall permissions** - Displays the permissions that
     are granted to the extension. Click on the permission to see a
     description.
   - **Web access permissions** - Displays the list of
     websites with which the extension has permission to interact. If the
     extension has access to all websites, the result will be **All
     URLs**.If the extension does not have any website access
     permissions, then the section will *not* appear.
   - **Installations** - The number of devices where the extension is
     installed. The figure can be displayed by extension version or by
     source (if more than one source is applied to the extension.
   - **Recent Activities** - Displays the recent activity for the
     extension.

   ![]()

---

<a id="manage-prisma-browser-policy-rules"></a>

### Manage Prisma Browser Policy Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules>*

Learn how to manage policy rules for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

To see the rules from Strata Cloud Manager, select ConfigurationPrisma Browser
PolicyRules.

*All changes to policy rules are saved to a draft
configuration and do not take effect until you publish the draft. For more
information, see Manage Configuration Versions (Draft Mode).*

You can use rules to specify the users, user groups, and device groups that
will be impacted by the various policies you create. These rules govern access to
web applications, security policies, and customization options. By utilizing rules
you can precisely control user access to organizational tools and components.

Each Rule is composed of different parameters and controls so that you can
create finely tuned Rules for each use case. Each Rule type has its specific
contents and requirements.

You have three available Rule types in the Prisma Browser. The
components are displayed on each tab's Policy Rules page.

For each Rule type, the Rules are evaluated according to their priority.
The first Rule that matches all the requirements creates the trigger that will be
enforced. When this happens, the browser stops looking for Rules.

**Example with Access & Data Control rules:**

**Rule 1**: Scope - Mike (a member of the General Contractors Users
group)

Web application - linkedin.com

Access to the named web application *Allowed*Data controls - File
Download - *Blocked*

**Rule 2**: Scope -Gowri (a member of the General Contractors Users
group)

Web application - linkedin.com

Access to the named web application - *Allowed*Data controls - File
Upload - *Allowed* When contains - *email address.*

**Rule 3**: Scope - Summer Interns Users Group

Web application - linkedin.com

Access to the named web application -Blocked

**Rule 4**: Scope - General Contractors Users Group

Web application - linkedin.com

Access to the named web application - *Allowed*Data controls - File
Upload- *Blocked*

Mike will be allowed to access linkedin.com, however, he’ll be blocked when
he tries to download a file since his action matches Rule 1.

When he tries to upload a file, the Policy Engine will see that Rule 1 does
not apply. It then will move on to check the next Rule. Rule 2 does not apply due to
the Data controls. Rule 3 does not apply to Mike, as he is outside the Rule's scope.
Rule 4 will block Mike from uploading on linkedin.com.

As long as there is no matching rule, the Policy Engine will keep checking.
When it reaches the end of the list, the action will proceed according to the
default rule, as there is no other rule to apply.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|

**Rule** | **Scope** | **Access to linkedin.com** | **Download** | **Upload** | **When contains** |

|

1 | Mike | Allowed | Blocked |  |  |

|

2 | Gowri | Allowed |  | Allowed | email address |

|

3 | Summer Interns | Blocked | - - - - - - | - - - - - - |  |

|

4 | General Contractors | Allowed |  | Blocked |  |

Mike wants to download a file from linkedin.com.

- Rule 1 applies, and the download is Blocked. Policy Engine stops
  looking for rule matches.

Mike wants to upload a file to linkedin.com.

- Rule 1 does not apply (The rule is for downloads). Policy Engine
  continues.
- Rule 2 does not apply (Mike is out of scope). Policy Engine
  continues.
- Rule 3 applies, and the upload is Blocked. Policy Engine stops
  looking for rule matches.

Gowri wants to upload a file to linkedin.com.

- Rule 1 does not apply (Gowri is out of scope). Policy Engine
  continues.
- Rule 2 applies - but only if the upload includes an email address;
  if not, Policy Engine continues.
- Rule 3 does not apply (Gowri isn't a Summer Intern). Policy Engine
  continues.
- Rule 4 applies, and the upload is Blocked.

#### Control the Rules List

Three control icons on the right side of each rule
appear only when hovering over an existing rule. From Strata Cloud Manager, select
ConfigurationPrisma Browser
PolicyRules and hover over an existing rule.

![]()

1. **Edit** - Opens the rule for editing.
2. **Display** Presents the items from the Rule Menu. This menu
   provides the following options:

   - **Set to Monitoring** (Access & Data Control
     Rules only) - Allows admins to toggle the rule mode if needed.
     Monitoring allows admins to see the effects of the rule before
     it is actually enabled.
   - **Set to disabled / enabled** - Toggles the rule on
     or off.
   - **Clone** - Creates a copy of the rule.
3. **Delete** - Delete the rule.

#### Perform Bulk Actions & Move Rules

Administrators can perform bulk actions on multiple rules simultaneously to
streamline rule management in the Prisma Browser. By selecting one or more
rules, you can apply a single action to all selected entries. The available bulk
actions include:

- Set to Active
- Set to Monitoring
- Set to Disabled
- Delete selected rules

These actions help simplify large-scale policy updates and reduce the time
required to manage complex rule sets.

**Move Rules**

This feature allows you to quickly place rules at the top, or bottom, or specify
an exact position for the rules. This is much more efficient than dragging and
dropping rules, especially when dealing with large data sets.

**Performing Bulk Actions on Rules**

Follow these steps to apply bulk actions to multiple rules:

1. Navigate to the Rules Page.
2. Select the Rules Use the checkboxes next to each rule to select the
   rules you want to modify. You can select as many rules as needed. Once
   you select the first rule, the Bulk Actions menu will appear.
3. Choose an Action Select one of the following actions:
   - Active – Enables all selected rules.
   - Monitoring – Enables Monitoring for selected rules.
   - Disabled – Disables all selected rules
   - Move – Moves the selected rules.

   The following options are available for moving the rules:
   - Move to top – Move the selected rules to the top of the
     list.
   - Move to position – Move the selected rules to the current
     position on the list.
   - Move to bottom – Move the selected rules to the bottom of
     the list.

![]()

Choose an Action Select one of the following actions: Set to Set to . Set to
Monitoring Mode – Moves selected rules to monitoring-only status. Delete
Selected Rules – Permanently removes all selected rules. Confirm the Action (if
prompted) For actions like deletion, a confirmation dialog may appear. Review
the changes and confirm to proceed.

#### Organize Rules into Sections

Rule Sections allow you to enhance the organization and management of your
security policies in Prisma Browser. With this new feature, you can now
group your rules into collapsible sections, improving navigation and making it
easier to manage your policy rules. This allows you streamline your workflow and
make it mucch easier to find your rules.

For example, if you have several policy rules that are designed for contractors,
you can place them in the same section. When you need to change something in one
of the rules, instead of looking down the long list, all you need to do is look
for the contractor's group,

**Adding a new section:**

You can create as many sections as needed. The sections are created in the Policy
Rules page.

1. Open the Policy Rules page.
2. Select the controls group where the section is to be placed. You can choose
   from one of the following:

   - Access & Data Control
   - Browser Security
   - Browser Customization.
3. Place the cursor at the point where you want to place the Section. A
   section tool will be shown on the screen.

   1. Click the **+** to open the Policy Rules menu. 

      ![]()
   2. Click **Create new section.**
   3. Enter a name for the section.
   4. Select either **Create new rule**, or **Drag and drop existing
      rule**. 

      ![]()

   If you select **Create New Rule**, the appropriate Rule Policy type
   opens. You can then create the rule that is customized for the section.

   If you select **Drag and drop existing rule**, handles will appear
   that you can use to grab the rule and then drag and drop the rule.
4. Click **Save Changes**.

#### Manage Rule Sections

You can manage the Rule Sections very easily.

1. To manage the sections, click the rule menu. 

   ![]()
2. In the section menu, manage the section using the following controls:
   - **Create rule at top of section** - Opens the appropriate
     Policy Rule tab.
   - **Rename section** - Enables you to change the name of the
     section.
   - **Ungroup section** - Removes all the rules from the group,
     and deletes the section. The rules will be avaialble to be added
     to new sections or left alone as an unsectioned rule.
   - **Delete section** - Deletes the section and all the rules in
     the section.

     If you
     delete a section, you will delete all the rules that are
     included. The action cannot be reversed.

#### Manage Rule Priority

By default, every time you create a new rule, it is given the highest priority.
This means that it becomes the first rule to be evaluated until a new rule is
created; it will move down the list, and the newer rule moves into first place.

There are situations where you may want to make a rule with a lower priority. You
can do this as follows:

1. Select Policy > Rules from the menu. 

   ![]()
2. Scroll down the list of policy rules. There will be an indicator
   wherever you can set a lower priority for the new rule. 

   ![]()
3. Click on the +, and you will be able to create a new rule that will be
   located at the selected place in the list. In the example provided
   above, the new rule will be 5 on the list, and all the rules below that
   location will be moved down 1 place.

When adding a rule in a filtered table view:

- The rule is placed *after* the previous location based on absolute
  priority.
  - Example: If the filtered list shows rules at priorities 10, 20,
    and 30, adding a rule between 20 and 30 sets it at priority
    21.

This means that you can only add a rule *after* a rule that appears
in the filtered list.

If you do not select a different priority for the rule, it will
automatically default to have the highest priority. You will be reminded of this
when you create a new rule without selecting a different priority. 

![]()

#### Edit Rules

On occasion, rules need to be edited based on changing circumstances and
conditions. You can edit all rule types in the Prisma Browser.

1. On the Policy Rules page, filter the list to display the rules of a
   particular type, and if needed, continue the filtering to make it easier to
   find the rule that needs to be edited.
2. Click the pencil icon (edit).
3. Edit the rule based on the new requirements.

#### Delete Rules

There are rare occasions when a rule needs to be deleted. It could be
that the rule is no longer required, or that a new rule covers the same
requirements, or that the underlying scope is not longer applicable.

**NOTE:** When a rule is deleted, it is no longer available, and any
conditions that the rule established will no longer exist.

1. On the Policy Rules page, filter the list to display the rules of a
   particular type, and if needed, continue the filtering to make it easier to
   find the rule that needs to be deleted.
2. Open the Rule Menu and select Delete.
3. Delete at the prompt.

   The rule will be removed from the list.

#### Types of Rules

- [Data Access and Control
  Rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html)
- [Security Rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-security-rules.html)
- [Browser Customization
  Rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-customization-rules.html)
- [Sign-In Rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-sign-in-rules.html)

---

<a id="manage-prisma-browser-access-and-data-control-rules"></a>

#### Manage Prisma Browser Access and Data Control Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules>*

Learn how to manage access and Data Control rules for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Access & Data Control rules are designed to create the environment to keep the
data safe per application, website classification, or URL. You can create rules that
help make enforcement effective.

##### View the Rules

To view the rules:

The last
rule on the list is the **Access & Data - baseline**, also known as the
Default rule.

The Default rule is the policy rule that is used when no other
policy rule is applicable. Since this rule must be available for any given
user or device, only certain controls can be edited.

1. From Strata Cloud Manager, select .ConfigurationPrisma Browser
   PolicyRules
2. Select the Access & Data Control tab.

   ![]()

   The Access & Data Control displays the following
   information for each Rule:

   The information displays changes based on the
   policy rule type selected.

   - **Priority** - Access & Data Control rules are
     enforced based on the Zero Trust Access scope, the applications
     in the rule, and the enabled controls. The result of this is to
     enforce least-privileged access (the most restrictive context)
     for users and the applications that they are accessing.

     Rules are inspected from top to bottom based on the
     priority. But all rules are inspected which can result in
     multiple rules being matched to a user's session.

     The resulting access policy that is applied is a merge of all
     controls that are applicable to the user's context. If there is
     a conflict between the controls, the control in a higher
     priority rule supersedes a control in a lower priority rule.

     1. Select the cog icon to the left of
        Change priorities to modify which of the following fields
        you want to display.
     2. Select Change priorities to reorder
        the rules in the list. The rules are processed in order, and
        once a rule is matched, the processing stops.
   - **Mode** - The behavior of the Rule applied on the
     end users. The options are:

     - **Active** - The Rule will be applied and
       enforced on all end users.
     - **Monitoring** - The Rule will only create
       logging events without affecting the end users.
     - **Disabled** - The Rule won't be applied on
       end users.
   - **Name** - The name of the Rule.
   - **Scope** - A combination of the Users, User Groups,
     Device Groups, Networks, and Locations that will be included in
     the rule.

     If a rule references deleted users or
     user groups, an icon will be displayed in the header and the
     Scope field, suggesting that the user/user group be removed.

     ![]()

     Location scope is not supported using
     Linux.
   - **Destinations** - The specific applications,
     website classifications, and URLs that this Rule covers.

     The Rule will match if any one application,
     classification, or URL is matched.

     If a rule references a deleted app, the rule will
     stay in the same mode, but the application's FQDNs will not
     be enforced in the browser/PABx/Mobile.

     An alert icon will be displayed in the header and
     in the application field, suggesting that the application be
     removed.

     ![]()
   - **Web Access** - Defines the behavior of the ability
     to access the websites defined in the Rule.
   - **Data controls** - The Data controls that are used
     as part of the Rule. This can include either inline data
     controls set per Rule or preexisting Profiles that can be reused
     in different rules. If the Rule uses a profile, the name of the
     Profile is highlighted in the display.
   - **Hits** - The number of times the Rule was applied
     in the past 7 days. This feature is especially useful when
     examining rules before implementation.
   - **Updated** - The date and name of the person who
     made the most recent update. Hover over the entry to see the
     full timestamp.
   - **Log level** - The type of logging that is applied to the
     Rule.

##### Search and Filter

You have the opportunity to search and filter for particular rules. This helps
you investigate rules that have common components. This makes it easier to check
for rules that might be duplicated or to find rules that might be operating
improperly.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Access & Data Control tab.
3. Search for rules by the rule name.
4. Filter on rules based on specific criteria:

   - **Users** – The Users and User Groups that are
     included in a Rule.
   - **Device group** - The Device groups that are
     included in a Rule.
   - **Applications** - Web applications that are
     included in the Rule.
   - **Web classifications** - The categories of
     applications that are covered by the Rule.
   - **Web access**- The access options that will be
     enforced for this Rule. The options are:

     - **Prompt** - Web access is restricted, but
       there is an option to proceed.
     - **Allow** - Web access is permitted.
     - **Block** - Web access isn't permitted.
   - **Controls** - The Data controls that are used in
     the Rule.
   - **Mode** (available in **Add Filter**) - The
     filter can include the following options:

     - **Monitoring** - Rules that only write an
       entry to the Events Log. See below for more information.
     - **Active** - Rules that are active and are
       used by the Policy Engine.
     - **Disabled** – Inactive rules are skipped by
       the Policy Engine.
   - **Content configured**- The filter can include rules
     that have configured content in the "When contains" section of
     the rule configuration. The options are:

     - **Yes** - Select rules that contain
       configured content.
     - **No** – Select rules that don't contain
       configured content.
   - **Log level**- Select the level of logging that will
     be performed on the Rule. The options are:

     - **Enhanced** - All user actions involving
       this Rule are fully logged with the Prisma Browser
       creating a session recording of the activity. This can
       assist with compliance and regulation requirements, or
       to carefully monitor actions within sensitive
       applications.
     - **On** - All user actions involving this
       Rule are logged.
     - **Anonymized** - Actions involving this Rule
       are logged without personal details.
     - **Off** - User actions involving this Rule
       are not logged.
   - **Profile** - If the Rule uses External Controls (Profiles) as
     part of the Policy Rules, then you can use this filter to assist
     the search.

For example, if you want to see the way that downloads work across
different sites for a particular user, do the following:

1. Filter the list by the username.
2. Filter the resulting list by the Control - **File
   Download**.
3. Manually review the list. The first rule to match the website
   is the behavior for the file download.

<a id="task-create-access-rule_step-content-settings"></a>

<a id="manage-prisma-access-browser-access-and-data-control-rules_task-create-access-rule"></a>

##### Create New Access & Data Control Rules

Adding a new Access & Data Control Rule can be done easily with an
understanding of the way that the rule is going to be used and enforced. Each
Rule needs to be planned carefully, taking into consideration the way that each
element will be configured. This will make sure that the enforcement can be done
effectively.

You can create rules using a wizard interface. This allows you to have
full control over the entire policy.

When you set up a Rule, you can click on the Wizard controls on the left side, or
the **Next** button at the bottom of the page.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Access & Data Control tab and CreateNew RuleAdd Rule.

   ![]()

   1. Enter a Name for the rule.
   2. Enter a Description for the rule.
   3. Select the Mode.

      - **Monitoring** - Rules that only write an
        entry to the Events Log. A Rule set to monitoring can be
        used for testing new rules.
      - **Active** - Rules that are active and are
        used by the Policy Engine. This is the default action.
      - **Disabled** – These are inactive rules that are
        skipped by the Policy Engine.
   4. Select Next: Scope.

      ![]()
3. On the Scope page, enter the following information:

   The Scope combines the selections in Users, User
   Groups, Device Groups, Networks, and Location. This means that the rule
   scope requires that all conditions be met for a match to occur.

   - **Users/User Groups** - Select the [Users](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-users.html) and [User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-users.html) that will be
     covered by the Rule. It's possible to select multiple Users and
     User Groups. The default is **Any user**.
   - **Device groups** - Select the [Device groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html) that will
     be covered by this Rule. It's possible to select multiple device
     groups. The default is **Any device group**.
   - **Networks** - Enter a Public IP address with a
     subnet, if needed, or a CIDR.
   - **Location** – Select the geolocation from which to
     enable the Prisma Browser rule. If the OS Location services
     are not enabled on the device, the PAB will use the GeoIP. For
     more information, refer to [Location-based Policy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/location-based-policy.html)
   - Select Next: Applications.

     ![]()
4. On the Applications page, choose the Destination types for this rule.
   Select from the following options:

   You can select any combination of Internet &
   SaaS applications, Private applications, and Application Groups.

   - **Internet & SaaS applications** - For applications
     stored on Public websites and SaaS applications.
     - **Any internet & SaaS** - Allows you to include any
       Web and SaaS application.
     - **Custom** - Allows you to:
       - Choose Web or SaaS applications directly from a
         list.
       - Select any website falling within specific
         classifications.
         - Select any website/URL falling within a
           specific classification. For example, you can
           select *News* to block access to all news
           sites.
         - The categories can be divided into
           **Malicious** (for example, Phishing sites,
           Ransomware, Grayware) and **Benign** (for
           example, News and Media, Dating, Shopping). Select
           one of these two categories to properly filter the
           list. 

           ![]()
         - You can choose to select benign categories
           based on the URL Risk level; High, Medium, Low.
           When you select this option, all URLs that meet
           the criteria will be filtered. 

           ![]()The classification is divided into two
         categories - Malicious (for example, Phishing sites,
         Ransomware, Grayware) and Benign (for example, News
         and Media, Dating, Shopping).

         For more
         information, refer to [Risk
         Categories](https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-basics/url-categories?otp=risk-categories#risk-categories)
       - Enter a specific URL. You can select specific
         domains, subdomains, ports, and paths to provide
         custom setups to the application.

         The URL can
         contain [punycode](https://en.wikipedia.org/wiki/Punycode) and
         character substitution.
   - **Private applications** - Allows you to include applications
     that are privately maintained within the data center and are not
     publicly accessible.

     Tenants with the Private Application feature
     will be able to create a second default rule to manage access to
     Private apps (under access and data).

     For more information,
     refer to [Private
     Applications](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-applications.html#manage-prisma-access-browser-applications_task-iq1_skt_fcc).
     - **Any private application** - Allows you to include any
       application that is hosted on your internal network.

       This feature only works with:
       - Prisma Browser versions after 1.199.0
       - Prisma Browser Extension versions after
         1.244.0
     - **Specific private application** - Choose private
       applications directly from a list.
   - **Non-web apps** - Allows you to select non-web apps, either
     Admin-defined or any manually connected non-web app.
   - **Application Groups** - Allows you to select Application groups
     that you created.
   - Select Next: Web access. If you selected an
     application that supports multi-tenants, select Next:
     Tenants.

   ![]()
5. This feature is available if you selected a supported application in the
   previous step. The supported applications are:

   - Google Workspace
   - Microsoft 365
   - Slack
   - AWS

   On the Tenants page, you can define tenant-level policy enforcement for
   supported SaaS applications. This allows you to apply different controls
   to different instances (tenants) of the same application. For example,
   you can allow file uploads to your corporate Google Workspace tenant
   while blocking uploads to personal Gmail accounts.
   1. In the Application section (above), select a supported
      application.
   2. Choose the appropriate tenant scope for the application:
      - **Any Tenant:** Applies the rule across all instances
        of the application (default).
      - **Specific Tenant:** Enables an input field to apply
        the rule to a specific tenant using a unique
        identifier.

      To ensure accuracy,
      copy the tenant identifier directly from the Events
      page.
   3. If you selected Specific tenant, enter the unique Tenant
      Identifier based on the application.

      |

      Application | Supported Tenant Identifiers | Comments |

      | --- | --- | --- |

      |  |  |  |
      | --- | --- | --- |
      |

      Google Workspace | Domain Name | Standard domain format example.com |

      |

      Microsoft 365 | Domain Name | Standard domain format example.onmicrosoft.com |

      |

      Slack | Workspace Name | String Match |

      |

      AWS | Account ID Region | Exactly 12 numeric (0-9) characters Validated against AWS Supported Regions list, |

      |

      Open AI chatGPT | Domain Workspace ID | Workspace ID found in local Storage |

   **Considerations:** 
   - Most tenant identifiers require manual free-text input and are
     not populated via a selectable discovery list.
   - Ensure exact string matching, as certain identifiers may be
     case-sensitive. Incorrect formatting, spacing, or capitalization
     may cause the policy to fail to match.
   - If an entered identifier is invalid based on the required
     format, the UI will display an error message.

   ![]()
6. On the Access page, choose the access options that will be enforced for
   this Rule. The options are:

   - **Allow** - allow users to access the applications,
     websites, and URLs.
   - **Prompt** - inform the user that the access is restricted,
     but allow the user the option of continuing. When a user selects
     an option that allows them to **Proceed anyway** or use any
     option that requires **Admin Approval**, an event will be
     written to the log.

     Using **Prompt** grants limited
     access permission depending on how you configure the setting.
     You can set it to be once (one-time access for the account) or
     unlimited access for a limited time frame.

   1. **Warn and allow to proceed anyway** - Users will receive a
      warning, but will be allowed to proceed anyway.
   2. **Warn and allow to proceed anyway with a reason** - Users will
      receive a warning, but will be allowed to proceed anyway if they
      provide a reason.
   3. **Permission request** - Users will be required to provide a
      reason that you must approve before they are allowed to proceed. For
      more information, see [Requests](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-requests.html).

      Mobile rules with this option will result in a Block.
   4. **Block -** Block users from accessing the applications,
      websites, and URLs.
   5. **Require MFA** - Require users to complete an additional
      authentication factor (such as a PIN code, Passkey, or IdP
      authentication) before accessing the scoped websites. Configure the
      authentication factor used under **[Browser Security >
      Browser Hardening > Authentication Factor](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html#configure-browser-hardening_task-ydp_f2l_hcc)**.

      You can configure the length of time between MFA requests so that
      your users don't have to enter their authentication every time.
      The options are:

      - Every time.
      - A configured time between 10 minutes and 90 days.
   6. Enforce Prisma Browser Extension traffic
      redirection to Prisma Browser - Access to
      web apps from the Prisma Browser Extension will trigger an “Open
      in Prisma Browser” dialog. The access is still subject to the
      options selected above. If you select this option, you can use your
      own dialog text to replace the default. To set the text, click Set
      dialog text. This option will be ignored for mobile rules.

      - If you want the redirection to automatically open the Prisma Browser, select the **Redirection will
        automatically open Prisma Browser** checkbox.

        When you
        access web applications through the Prisma Browser,
        you'll see an 'Open in Prisma Browser' message.
        Using the Prisma Browser will still follow the
        Allow/Prompt/Block rules mentioned earlier.
   7. Pick a Label - Select the label to appear in
      the browser address bar. This will display the basic information on
      the site policy. Note: This option will be ignored in the mobile
      rules.
   8. Select Next: Login controls.

      ![]()
7. The Login Controls sub-page allows you to control logging into the
   applications and websites using the Prisma Browser. For more
   information, please refer to [Login Controls](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls.html).
8. On the Data controls page, select the controls that the rule will
   use.
   1. The following search and filter options are available:

      1. **Active only** - Display controls that are
         already in use in the Rule.
      2. **Enterprise browser** - Display only those
         controls that are available for the Enterprise
         browser.
      3. **Mobile browser** - Display only the
         available controls for the Prisma Browser for Mobile.
      4. **Extension** – Display only the available controls
         for the browser extension.
   2. Select and configure the **Data controls** for the rule. The
      rule can contain multiple controls. For information on configuring
      the individual controls, refer to:

      1. Data Leak Prevention
      2. Malware Protection
   3. You can add Controls that you manage outside of the rule. Click
      **Saved Profiles** to select a preconfigured profile in place
      of the Data controls.

      ![]()
9. The When Contains (Content Settings) page allows you to condition the
   configured Data controls. This allows you to create rules that trigger only
   if specific data types occur. You can also create custom data types that can
   condition the rules.

   You can create data pattern combinations (from either the
   predefined values, or the custom values).

   For example, you can set File Download control to Block, and
   add an email content detector to the rule. This means that if a file
   includes an email address, the file download control in the rule will
   activate and block the download. The content types can be incorporated
   into rules containing the following Data control types:

   - File Download
   - File Upload
   - Clipboard
   - Webpage data masking
   - Typing Guard
   - Screen Sharing
   - Webpage Watermarking
   - Print

   You need to be aware of the following
   limitations to the **When contains...**involving DLP scanning for
   file upload and downloads:
   1. If the file size is more than 1GB, File Scanning will not occur.
   2. If the file size is less than 1GB, and the file type is
      supported, thee first 5MB of text is extracted and scanned.
   3. If the file size is less than 1GB, and the file type is not
      supported, the first 5MB of the file is extracted as text, and a
      "best effort" is made to scan it.

   Supported File Types

   |

   File Type | File Extension | File Type | File Extension |

   | --- | --- | --- | --- |

   |  |  |  |  |
   | --- | --- | --- | --- |
   |

   ASM | .s | matlab/obj-c | .m |

   |

   c\_cpp-hdr | .h | PDF | .pdf |

   |

   c\_cpp-src | .c | PL | - .pl - .pm |

   |

   cpp-hdr | - .pl - .pm | Powershell | - .ps1 - .ps2 - .pcs1 - .psd1 - .psm1 - .ps1xml - .ps2xml - .clixml |

   |

   cpp-src | - .cpp - .c++ - .cxx | PPT | - .pptx - .pptm - ,ppex - .ppsm |

   |

   csharp | - .cs - .css | py | .py |

   |

   csv | csv | r | .r |

   |

   docs | - .docx - .docm | RTF | .rtf\* |

   |

   go | .go | Ruby | .rb |

   |

   html | .html | txt | .txt |

   |

   jsva-src | .java | vbe | .vbs |

   |

   js | .js | xlsx | - .xlsx - .xlsm - .xlsb |

   \* Partial support - RTF is a text format, but
   applying formatting to parts of text changes the underlying HTML
   code. For example, if you set a specific color to some of the digits
   of a credit card, there would not be a match.

   1. On the Content Settings page, select **Specific content.**
   2. Select Select in the Content detectors
      field.
   3. Select the preconfigured content detectors from the list.

      In addition, you can [create custom content
      detectors](#manage-prisma-access-browser-access-and-data-control-rules_task-xjq_ptt_fcc) to add to the list, based on regular
      expressions.
   4. Select Next: Tracking.

   Canvas-based applications do not support data
   masking, content-based screenshot control, or content-based
   watermarking. These features rely on the Prisma masking engine, which
   cannot operate on Canvas-rendered content.

   As a result, the following
   applications—and others that use similar rendering methods—may show
   inconsistent or unavailable protection:

   - Google Docs and Google Sheets

     *(Google Slides is supported)*
   - Figma
   - Miro
   - Notion
   - Mural

   To avoid misconfiguration, you need to ensure that you do not
   enable data masking, content-based screenshot control, or
   content-based watermarking for any Canvas-based
   application.
10. The **Tracking** page contains 2 sections. In the first section,
    **Session Recording evidence**, select whether or not to record all
    of the user's browsing activity in the applications specified and, choose
    whether or not to record the user's full browsing activity
11. In the second section, select the level of **Activity Logging** you
    need.

    1. **Enhanced** – The Browser fully logs all user
       actions involving this rule. The Browser fully logs the actions
       with additional visibility enhancements.:

       - **Screenshot evidence** - The issued event will include a
         screenshot of the user's active tab at the time of the
         activity.
       - **Event Recording evidence** - The issued event will
         include a short video recording of the user's screen
         starting before the event until after the activity.

         Session Recording cannot be used
         for RDP apps.

         If there
         is a detected endpoint performance issue, Prisma Browser
         will capture a Screenshot.
    2. **On** – This Rule logs all user actions. You can
       optionally choose to extract the URL query parameters to the
       Activity log.
    3. **Anonymized** – This Rule logs all user actions
       without personal details.
    4. **Off** – There is no logging for this rule.
12. Click Save.

    ![]()

###### Set Rule Monitoring

You can choose to configure some rules for Monitoring purposes only.
Monitoring only writes an entry to the Event Log. This allows you to test
how the Rule affects the browser usage before actually putting it into
regular production. By using Monitoring, you can apply multiple rules to a
single action - one for monitoring purposes and another for executing the
action.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Access & Data Control tab.
3. [Create a new Access & Data Control
   Rule](#manage-prisma-access-browser-access-and-data-control-rules_task-create-access-rule).
4. Save the rule.
5. On the Rule List, click the ellipse, and select
   Set to Monitoring. This can also be done in
   the first step of the wizard, in the Mode option.
6. The rule will be available, but whenever it comes into effect, it will
   ignore actions, and merely write to the Events log.

###### Use Predefined Content Types

The Prisma Browser has some predefined content items included.
These predefined content types can be used when you need to add a specific
content item that isn't included in the database.

The Content Types are divided into two categories - Data Profiles
and Data Patterns. With these features, you now have more control over the
data that you can add.

The content types are grouped into categories. You have the ability
to filter the Patterns to see the information that relates directly to your
requirements.

- Privacy
- Finance
- Healthcare
- Other
- Custom

To select preconfigured Content items:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Access & Data Control tab.
3. [Create a new Access & Data Control
   Rule](#manage-prisma-access-browser-access-and-data-control-rules_task-create-access-rule).
   1. Be sure to configure the When contains information.
   2. Click **Specific content**.
   3. Click the tab for Data Profiles or
      Data Patterns.
   4. If you have any questions regarding a particular data item,
      click the (i) on the side of the list.
      This will open a page containing more information regarding the
      item.
   5. Select the required Content Detectors - either Data
      Profiles or Data
      Patterns.
   6. Select the Content types, then click the appropriate content
      item. The rule can contain any combination of items.
4. Save.

<a id="manage-prisma-access-browser-access-and-data-control-rules_task-xjq_ptt_fcc"></a>

###### Create Custom Content Types for the Prisma Browser Rules

You can define additional Data Patterns to meet your specific
organizational-related needs. The file definitions are based on [ECMAScript (JavaScript)
Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags).

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. When you're configuring your rule, in the [When Contains (Content Settings)](#task-create-access-rule_step-content-settings),
   select **Specific content.**
3. Select the content detectors from the list, either Data Profiles or
   Data Patterns. You can create custom content detectors to add to the
   list, based on regular expressions.

   To add a custom data type:

   1. Select the **Data Patterns** tab. Go to the bottom of the
      list and click **Manage custom content types**.
   2. In the **Custom content types** window, click **Add
      type**.
   3. In the **Add Custom Content Type** window, add the
      appropriate pattern for the content.
   4. “Custom data types” support ECMAScript (JavaScript) Syntax.
   5. Advanced flags (<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags>)
      are currently not supported.
4. The configured custom content types will be matched against the
   configured data controls that support content inspection.

   Configured Data Controls that don't support content
   inspection (e.g. screenshot) will ignore the specific content
   condition and will be applied according to all other rule conditions
   (scope, web application).

   The content types can be incorporated into rules containing
   the following Data control types:

   - File Download
   - File Upload
   - Clipboard
   - Webpage data masking

##### Configure External Controls (Profiles)

Inline profiles should be configured within the rules in the
Controls sections. This allows you to create specialized rules containing
different combinations and configurations of controls.

The [Profiles](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles.html) feature is used
when you want to use legacy profiles and add them to the rules.

Rules can contain either inline data controls or external controls.

The Controls for the Prisma Browser rules are configured
internally, within the body of the individual rule. This means that each rule
contains its own unique set of controls.

There are some use cases when you might want to create multiple rules
using the same list of controls. To accomplish this task, Prisma Browser has
a mechanism to create external controls that are not built into a rule but exist
separately. Each control defines a particular use case containing configurations
for the policy control types.

1. ConfigurationPrisma Browser
   RulesData Access & Control
2. Add rule.
3. Data controls

   These controls access to websites and data, preventing
   organizational data from being accidentally (or maliciously) released.
   For information on configuring the individual controls, refer to [Configure Data Controls](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls.html).

---

<a id="login-controls"></a>

##### Login Controls

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls>*

The new login controls for Access and Data Control Rules

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Login controls page allows you to control logging into applications and websites
using the Prisma Browser.

The form-based login control - manages the way users specified in the scope
of the rule can login to websites using any login form that includes a username
field that needs to be specified by the user.

Select the login method to see the configuration method:

- [Login
  Form](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls/login-form.html)
- [Passkey Login](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls/passkey-login.html)

---

<a id="login-forms"></a>

###### Login Forms

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls/login-form>*

The new login controls for Access and Data Control Rules

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Select Login Form to configure this method:

Use the feature as follows:

1. The Login Controls sub-page allows you to control logging into the applications
   and websites using the Prisma Browser. Use the feature as follows:
   1. Select the **Login Form**.
   2. In the **Control form-based login** page, select the following login
      type:

      1. **Allow** - Allow login to the selected sites
         using any username and password.
      2. **Block** - Block login to the selected
         sites.
      3. **Allow specific email domains** - Allow login
         to the selected sites with usernames that are from specific
         email domains only.
      4. **Block specific email domains** - Block login to the
         selected sites with usernames that are from specific email
         domains only.

      ![]()
   3. In the **Email domains** tab, enter the email domains that will be
      used.

      This step is only available if you selected
      **Allow specific email domains**, or **Block specific email
      domains**.

      1. Enter the email domain in the form "@example.com."
      2. Click **Add email domain**.
      3. Repeat as needed.

      ![]()
   4. In the **Prompt** tab, select one of the following options:

      1. **None:** No prompt is needed for this rule.
      2. **Pop-up notification** - Select one of the
         following options:

         1. **Warn and allow to proceed anyway** -
            Users will receive a warning but they can proceed
            anyway.
         2. **Warn and allow to proceed anyway with a
            reason** - Users will receive a warning but they
            can proceed if they provide a reason.
         3. **Permission Request** – You will
            receive a message requesting permission.
      3. **Bypass timeframe** – Indicate how long any bypass will
         be valid.

      ![]()
   5. **MFA** - Require users to complete an additional authentication
      (such as a PIN code, Passkey, or IdP authentication) before allowing
      form login to the scoped websites. Configure the authentication factor
      used under **[Browser Security >
      Browser Hardening > Authentication Factor](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html#configure-browser-hardening_task-ydp_f2l_hcc)**then select
      this option.

      ![]()
   6. Set the **Account Protection** – Ensure that login is only possible
      from the browser by protecting the password during password reset.

      1. **Enable account protection for shared accounts:** Users will
         be able to use shared accounts without needing to share the same
         actual password All shared accounts will have the same password
         protection.

      ![]()
   7. If you want to configure a custom **Dialog text** that will appear
      when the user is blocked, you can enter the message title and
      description here.

      ![]()
   8. Click **Set**.
   9. Select Next: Data controls.

      ![]()

---

<a id="passkey-login"></a>

###### Passkey Login

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules/login-controls/passkey-login>*

this is information for Passkey login

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Passkeys offer a passwordless, secure, and convenient method for signing
into apps and websites. They use your device's built-in security (like fingerprint,
face scan, or PIN) and public-key cryptography to generate unique,
phishing-resistant credentials that automatically sync across your devices and act
as a Multi-Factor Authenticator.

Some passkeys are managed for corporate access (such as IdP authentication,
or PB [authentication factor](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening?otp=task-ydp_f2l_hcc#task-ydp_f2l_hcc)). However,
users are frequently prompted by third-party websites to create passkeys for
convenience. Consequently, they often generate personal passkeys that are unseen and
outside of IT control.

PB solves this by providing **granular control over passkey login**.
Administrators can apply policies to allow or deny passkey usage based on
application, device posture, network, or location. For example, you can explicitly
allow passkey login for your sanctioned Identity Provider (e.g. Okta), while
blocking passkey usage on other, non-corporate applications.

The Passkey Login control is supported on Prisma Browser and Prisma Browser Extension.

To enable Passkey Login Control:

1. At the Login controls tab, select **Passkey** login.

   ![]()
2. Click on the **Passkey login** tab to open **Control Passkey login**, and
   select one of the following options:
   1. **Allow** - Logins using Passkeys will be permitted.
   2. **Block** - Logins with Passkeys will be blocked.

   ![]()
3. If you select Allow, you can require the use of multi-factor authentication.
   1. Click on the **MFA** tab to open the Multi Factor Authentication.
   2. Select **Require additional MFA prior to login**.

   ![]()

   The Prisma Browser Extension does not support
   Multi Factor Authentication; any configuration for Prisma Browser
   Extension will be ignored.
4. If you select **Block**, you can allow your users to prompt for special
   permission to bypass the negative result. Click the **Prompt** tab.
   1. **Pop-up Notifications**. Select one of the following options.

      - **Warn and allow to proceed anyway** - Users will receive a
        warning but they can proceed anyway.
      - **Warn and allow to proceed anyway with a reason** - Users
        will receive a warning but they can proceed if they provide a
        reason.
      - **Permission Request** – You will receive a message
        requesting permission.
   2. **Bypass timeframe** – Indicate how long any bypass will be
      valid.

      ![]()
5. If you want to configure a custom **Dialog text** that will appear when the
   user is blocked, do the following:
   1. Click **Dialog text**.
   2. Select one of the following options:

      1. **Use default texts** - Do not provide any custom texts for
         your users.
      2. **Customize default texts** - Enter a Title for your message
         and an optional description

      ![]()
6. Click **Set**.

---

<a id="manage-prisma-browser-security-rules"></a>

#### Manage Prisma Browser Security Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-security-rules>*

Learn how to manage security rules for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Browser Security Rules allow you to design a strong and secure browser environment.
Using the different controls, you can consider many potential security issues in
determining the security posture. This will make sure that the enforcement can be
done in a very effective manner.

To view the rules:

The last rule on the list is the **Browser Security -
baseline**, also known as the Default Rule.

The Default Rule is the policy
rule that is used when no other policy rule is applicable. Since this rule must
be available for any given user or device, only certain controls can be edited.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Security tab.

   The Browser Security list displays the following information for
   each rule:

   The information displays changes based on the rule
   type selected.

   - **Priority** - The order in which the Rules are
     enforced. Once a Rule is matched, the Browser stops looking for
     another match.
     1. Select the cog icon to the left of
        Change priorities to modify which of the following fields
        you want to display.
     2. Select Change priorities to reorder
        the rules in the list. The rules are processed in order, and
        once a rule is matched, the processing stops.
   - **Name**- The name of the Rule.
   - **Scope** - The Users and User groups included in the
     Rule.
   - **Browser Security controls** - The Browser security
     controls used as part of the Rule. If the Rule uses a profile, the
     name of the profile is highlighted in the display.
   - **Updated** - The date and name of the person who made the most
     recent update. Hover over the entry to see the full timestamp.

##### Search and Filter

You can search and filter for specific rules.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Security tab.
3. Search for rules by the description.
4. Filter on rules based on specific criteria:

   - **Users** – The Users and User Groups that are
     included in a Rule.
   - **Device group** - The Device groups that are
     included in a Rule.
   - **Controls** - The browser security controls that
     are used in the Rule.
   - **Mode** (available in **Add Filter**) - The
     filter can include the following options:

     - **Active** - Rules that are active and are
       used by the Policy Engine.
     - **Disabled** – Inactive Rules are skipped by
       the Policy Engine.
   - **Profile** - If the Rule uses External Controls (Profiles) as
     part of the Policy Rules, then you can use this filter to assist
     the search.

##### Create New Browser Security Rules

Adding a new Browser Security Rule can be done
easily with an understanding of how the Rule will be used and enforced. Each
Rule needs to be planned very carefully, taking into consideration the way that
each element will be configured. This will make sure that the enforcement can be
done effectively. These controls make sure that the actual Prisma Browser
and the peripherals are protected.

The rule parameters allow you
to have full control over the entire policy.

When setting up a rule, you can
click on the Wizard controls on the left side or click the **Next:** button at
the bottom of the page.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Security tab and + Add
   Rule.
   1. Enter a Name for the rule.
   2. Select the Mode.

      - **Monitoring** - Rules that only write an
        entry to the Events Log. A Rule set to monitoring can be
        used for testing new rules.
      - **Active** - Rules that are active and are
        used by the Policy Engine. This is the default action.
      - **Disabled** – These are inactive Rules that are
        skipped by the Policy Engine.
   3. Select Next: Scope.
3. On the Scope page, enter the following information:
   1. **Users/User Groups** - Select the Users and User Groups that
      will be covered by the Rule. It is possible to select multiple Users
      and User Groups. The default is **Any user**.
   2. **Networks**- Enter a Public IP address with a subnet, if
      needed, or a CIDR and Add.
   3. **Location** – Select the geolocation from which to enable the
      Prisma Browser rule. If the OS Location services are not
      enabled on the device, the PAB will use the GeoIP. For more
      information, refer to [Location-based Policy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/location-based-policy.html)
   4. Select Next: Browser Security
      controls.

   Prisma Browser for Mobile does not support IP
   Network Scope policies.
4. On the Browser Security controls page, select the controls that are used in
   the rule. It can contain multiple controls. For information on configuring
   the individual controls, refer to [Browser Security Controls.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security.html)
5. Save.

##### Configure External Controls

Inline profiles should be configured within the rules in the
Controls sections. This allows you to create specialized rules containing
different combinations and configurations of controls.

The [Profiles](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles.html) feature is used
when you want to use legacy profiles and add them to the rules.

Rules can contain either inline data controls or external controls.

The Controls for the Prisma Browser rules are configured
internally, within the body of the individual rule. This means that each rule
contains its own unique set of controls.

There are some use cases when you might want to create multiple rules
using the same list of controls. To accomplish this task, Prisma Browser has
a mechanism to create external controls that are not built into a rule but exist
separately. Each control defines a particular use case containing configurations
for the policy control types.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Click Add rule.
3. Select Browser Security controls

   These controls block users and malicious actors from exploiting
   the information and accessing the data. For information on configuring
   the individual controls, refer to [Browser Security
   Controls.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security.html)

---

<a id="manage-prisma-browser-customization-rules"></a>

#### Manage Prisma Browser Customization Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-customization-rules>*

Learn how to manage customization rules for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Browser Customization Rules can be used by organizations to help increase
productivity, and to make the browser their own, with a custom look and feel.

To view the rules:

The last rule on the list is the **Browser Customization -
baseline**, also known as the Default Rule.

The Default Rule is the policy
rule that is used when no other policy rule is applicable. Since this rule must
be available for any given user or device, only certain controls can be edited.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Customization tab.

   The Browser Security list displays the following information for
   each rule:

   The information displays changes based on the rule
   type selected.

   - **Priority** - The order in which the Rules are
     enforced. Once a Rule is matched, the Browser stops looking for
     another match.
     1. Select the cog icon to the left of
        Change priorities to modify which of the following fields
        you want to display.
     2. Select Change priorities to reorder
        the rules in the list. The rules are processed in order, and
        once a rule is matched, the processing stops.
   - **Name**- The name of the Rule.
   - **Scope** - The Users and User groups included in the
     Rule.
   - **Browser Customization controls** - The specific
     browser customization controls that are used as part of the Rule. If
     the Rule uses a profile, the name of the profile is highlighted in
     the display.
   - **Updated** - The date and name of the person who made the most
     recent update. Hover over the entry to see the full timestamp.

##### Search and Filter

You can search and filter for specific rules.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Customization tab.
3. Search for rules by the description.
4. Filter on rules based on specific criteria:

   - **Users** – The Users and User Groups that are
     included in a Rule.
   - **Device group** - The Device groups that are
     included in a Rule.
   - **Controls** - The browser security controls that
     are used in the Rule.
   - **Mode** (available in **Add Filter**) - The
     filter can include the following options:

     - **Active** - Rules that are active and are
       used by the Policy Engine.
     - **Disabled** – Inactive Rules are skipped by
       the Policy Engine.
   - **Profile** - If the Rule uses External Controls (Profiles) as
     part of the Policy Rules, then you can use this filter to assist
     the search.

##### Create New Browser Customization Rules

Adding a new Browser customization Rule
can be done easily with an understanding of how the Rule will be used and
enforced. Each Rule needs to be planned very carefully, taking into
consideration the way that each element will be configured.

Browser Customization Rules are used to create a custom look and feel for your
browser installation. These controls allow you to create their own customized
edition of the browser, unique to their organization.

The Rule
parameters allow you to have full control over the entire policy.

When
setting up a Rule, you can click on the Wizard controls on the left side or click
the **Next:** button at the bottom of the page.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Select the Browser Customization tab and
   + Add Rule.
   1. Enter a Name for the rule.
   2. Select the Mode.

      - **Monitoring** - Rules that only write an
        entry to the Events Log. A Rule set to monitoring can be
        used for testing new rules.
      - **Active** - Rules that are active and are
        used by the Policy Engine. This is the default action.
      - **Disabled** – These are inactive Rules that are
        skipped by the Policy Engine.
   3. Select Next: Scope.
3. On the Scope page, enter the following information:
   1. **Users/User Groups** - Select the Users and User Groups that
      will be covered by the Rule. It's possible to select multiple Users
      and User Groups. The default is **Any user**.
   2. **Networks**- Enter a Public IP address with a subnet, if
      needed, or a CIDR and Add.
   3. **Location** – Select the geolocation from which to enable the
      Prisma Browser rule. If the OS Location services are not
      enabled on the device, the Prisma Browser will use the GeoIP.
      For more information, refer to [Location-based Policy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/location-based-policy.html)
   4. Select Next: Browser Customization
      controls.
4. On the Browser Customization controls page, select the controls that are
   used in the rule. It can contain multiple controls. For information on
   configuring the individual controls, refer to [Browser Customization
   Controls](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization.html).
5. Save.

##### Configure External Controls

Inline profiles should be configured within the rules in the
Controls sections. This allows you to create specialized rules containing
different combinations and configurations of controls.

The [Profiles](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles.html) feature is used
when you want to use legacy profiles and add them to the rules.

Rules can contain either inline data controls or external controls.

The Controls for the Prisma Browser rules are configured
internally, within the body of the individual rule. This means that each rule
contains its own unique set of controls.

There are some use cases when you might want to create multiple rules
using the same list of controls. To accomplish this task, Prisma Browser has
a mechanism to create external controls that are not built into a rule but exist
separately. Each control defines a particular use case containing configurations
for the policy control types.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRules.
2. Add rule.
3. Browser Customization controls

   You can use these controls to brand the Prisma Browser,
   customize the homepage, and other components of the user experience.

   - Branding
   - Customization
   - Homepage
   - Upgrade Enforcement

---

<a id="manage-prisma-browser-policy-profiles"></a>

### Manage Prisma Browser Policy Profiles

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles>*

Learn how to manage policy profiles or external controls for Prisma Access Secure Enterprise Browser
(Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Profiles (or external controls) can be used when you want to save reusable (or
legacy) profiles and attach them to the rules later. The controls for the Prisma Browser rules can also be configured within the body of the individual
rule instead when you [manage inline policy rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html).

#### Create a Policy Profile

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyProfiles
2. Select the Profile (Control) type you will be using and click the + next to
   the group.
3. Enter a name for the Profile and Create.
4. Configure the controls that will be included in the Profile.

   It is possible to select more than one control per profile:

   1. [Configure Data
      Controls](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls.html)
   2. [Configure Browser
      Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security.html)
   3. [Configure Browser
      Customization](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization.html)
5. After the Profile Controls are configured, Save X
   changes, located on the lower right of the browser. The
   button will "shake" to remind you to save the changes.

#### Attach a Policy Profile to a Rule

After you create profiles, you can attach them to rules. When you create a new
Profile Rule, you can select a preconfigured Policy Profile instead of using the
Control step in the rule creation Wizard.

1. Create the rule according to the regular procedure, such as [create an Access and Data
   Control Rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html#manage-prisma-access-browser-access-and-data-control-rules_task-create-access-rule).
2. At the Controls step, select the Profile from the Saved profiles
   list.

   ![]()
3. Save.
4. To indicate that the Rule is using a Policy Profile, the name of the
   Profile will be displayed in a highlighted background.

   ![]()

---

<a id="configure-prisma-browser-data-controls"></a>

#### Configure Prisma Browser Data Controls

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls>*

Configure data controls for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

You can configure the controls in the following ways:

- When you're creating a new browser security rule, you can set the controls in
  the [When Contains (Content Settings)
  page](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html#task-create-access-rule_step-content-settings).
- You can [edit an existing rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html#manage-prisma-access-browser-policy-rules_task-edit-rules).
- If you're using an [external control (profile)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html#manage-prisma-access-browser-access-and-data-control-rules_task-scd_w5t_fcc),
  you can select it from Strata Cloud Manager
  ConfigurationPrisma Access BrowserPolicyControlsData Control.

For information on a control, select the group where it is contained:

- [Data Controls – Data Leak Prevention](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention.html)
- [Data Controls – Malware Protection](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-malware-protection.html)

---

<a id="configure-data-leak-prevention"></a>

##### Configure Data Leak Prevention

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention>*

The Data Leak Prevention Controls

###### File Download

Mobile Browser -
**Partial support**

For detailed information in File Downloads using
the Prisma Browser for Mobile, refer to the [Prisma Access Mobile Browser
information](https://docs.paloaltonetworks.com/prisma-access-browser/deployment/prisma-access-mobile-browser?otp=concept-r2j_yym_ldc#concept-r2j_yym_ldc)

File Download control provides multiple
capabilities related to downloading files from websites that match a specified URL,
application, or website classification. To set the File Download control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select File Download.
3. Select one of the following options:

   - Allow - the Prisma Browser
     will allow all downloads.
   - Allow (Protected) – the Prisma Browser
     will allow downloads that can open only in the browser.

     - Allow to open outside of the
       browser - users will be able to
       unprotect the file, allowing viewing and editing of the
       file using external applications. This includes any
       browser and any Desktop application.
     - To unprotect a file:

       1. Click the Download History folder link
          in the Browser bar.
       2. Select the file to open. It will be
          indicated by a folder with a slash.
       3. Click on the icon to unprotect the file.
   - **Save to organizational storage** - Users won't be able to
     download the files directly. Files will be uploaded to the cloud
     storage that you selected.
     - **Select provider** - Select the cloud provider from the
       list. For more information on configuring cloud storage
       items refer to **Configuration→Prisma Browser
       →Integrations→Services→Cloud storage**

       Be sure to configure the
       organizational storage before it becomes available to
       the users. If you did not configure organizational
       storage, the option is not available.
   - Block - the Prisma Browser will block all
     downloads.
   - Apply on:- select between one of the following options:
     - - Any file - the
         download restrictions will apply to all files.
       - Specific files-
         the download restrictions will apply to files that
         meet the selected specifications (the rule can
         contain as many of these specifications as
         needed):
       - File size - set
         the size of the file.
       - File types - set
         the [file
         types](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/file-types-per-category.html) that need to match this rule.
       - File hash - set
         the SHA-256 hash to be matched for this rule.
       - MIP label - set the level of
         the [MIP label](https://docs.paloaltonetworks.com/prisma-access-browser/integrations/integrate-prisma-access-browser-with-microsoft-information-protection)
         that can be used to protect contents with sensitive
         content.
   - Prompt- when there is a restriction, select
     between one of the following options:
     - None - there will be no
       prompts.
     - Before download- inform
       the user that there is a restriction and how to bypass
       it.

       - Warn and allow to proceed
         anyway - informs users about the risk
         or sensitivity of downloading files but allowing
         them to continue.
       - Warn and allow to proceed
         anyway with a reason - informs users
         about the risk or sensitivity of downloading files
         and require them to select a reason to continue.
       - Permission request - allows
         users to send a permission request to the admin. The
         user will be informed once the [request](https://docs.console.talon-sec.com/en/articles/465) is
         approved or denied.
   - Require MFA - Require users to complete an
     additional authentication (PIN code, passkey, or IdP authentication)
     before downloading files. Configure the authentication factor used
     under **[Browser Security >
     Browser Hardening > Authentication Factor](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html#configure-browser-hardening_task-ydp_f2l_hcc)**
4. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
5. Set.

   ![]()

   When downloading PDF files - On
   Android devices, the PDF may briefly appear in the browser viewer before
   the system blocks the download. On iOS, the download is blocked
   immediately, and the viewer does not open.

###### File Upload

Mobile Browser - **Partial support**

For detailed information in File Upload using the Prisma
Browser for Mobile, refer to the [Prisma Access Mobile Browser
information](https://docs.paloaltonetworks.com/prisma-access-browser/deployment/prisma-access-mobile-browser?otp=concept-r2j_yym_ldc#concept-r2j_yym_ldc)

The File Upload policy controls whether users can upload files that come from
websites that match the URL or from a selected application or category.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select File Upload.
3. Select one of the following options:

   - Allow -the Prisma Browser
     will allow all uploads.
   - Allow protected files only between the
     rule’s web applications - Protected files
     sourced from the Web application of this
     rule. Only previously downloaded protected files from the Web
     application of this rule can be uploaded.

     Requires setting the File Download control
     to “Allow (Protected)” .
   - Allow only nonprotected files –
     only nonprotected files from any source can be uploaded.
   - Block - the Prisma Browser will block
     all uploads. You can block uploads from specific file
     extensions. Other extensions will be blocked.
   - Apply on:- select between one of the
     following options:
     - Any file - the download
       restrictions will apply to all files.
     - Specific files- the
       upload restrictions will apply to files that meet the
       selected specifications (the rule can contain as many of
       these specifications as needed):

       - File size - set
         the size of the file.
       - File types - set
         the [file
         types](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/file-types-per-category.html) that need to match this rule.
       - File hash - set
         the SHA-256 hash to be matched for this rule.
       - MIP label - set the level of
         the [MIP label](https://docs.paloaltonetworks.com/prisma-access-browser/integrations/integrate-prisma-access-browser-with-microsoft-information-protection)
         that can be used to protect contents with sensitive
         content. Install the Microsoft Information
         Protection integration to use this feature.
   - Prompt- when there is a restriction, select
     between one of the following options:
     - None - there will be no
       prompts.
     - Before upload- inform
       the user that there is a restriction and how to bypass
       it.

       - Warn and allow to proceed
         anyway - informs users about the risk
         or sensitivity of uploading or downloading files,
         but allowing them to continue.
       - Warn and allow to proceed
         anyway with a reason - informs users
         about the risk or sensitivity of uploading files,
         and require them to select a reason to continue.
       - Permission request - allows
         users to send a permission request to the admin. The
         user will be informed once the request is approved
         or denied.
   - Require MFA - Require users to complete an
     additional authentication (PIN code, passkey, or IdP authentication)
     before uploading files. Configure the authentication factor used
     under **[Browser Security >
     Browser Hardening > Authentication Factor](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html#configure-browser-hardening_task-ydp_f2l_hcc)**.
4. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
5. Click Set.

   ![]()

###### Clipboard

Mobile Browser - **Partial support**

The Clipboard Policy manages copy and paste functions when using the Prisma Browser. This tool allows you to manage Copy & Paste functions.
To configure the Clipboard control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Clipboard.
3. Select the control that you need to configure (both controls can be
   configured):

   - Copy & Paste data out -
     Configure whether users are allowed to copy & paste
     information from the browser to other applications.

     - Allow (anywhere) - Allow
       the copied data to be pasted to any web application or
       external process.
     - Block (permit only within the rule's
       web applications)- Block copy and paste
       data out of the rule's web application.

       - Exclude URL address
         bar – The URL address bar won't be
         considered as part of the webpage.
     - Prompt- Select whether you want to
       display a prompt.

       - None - Don't
         require a prompt.
       - Before pasting dat1a out to
         other web applications(Inform the user
         of the restriction and allow bypassing it).
       - Pop-up
         Notifications

         1. Warn and allow to proceed anyway.
         2. Warn and allow to proceed anyway with
            a reason.
         3. Permission request - select a Bypass
            time frame as well.
   - Copy & Paste data in-
     configure whether or not users are allowed to copy & paste
     information from other web applications or external processes.

     - Allow - allow the copied
       data to be pasted from any web application or external
       process.
     - Block- don't allow the
       copied data to be pasted from any web application or
       external process.
     - Prompt- select whether
       you want to display a prompt before pasting data in.

       - None - don't
         require a prompt.
       - Before pasting data in
         (Inform the user of the restriction
         and allow bypassing it)
       - Pop-up notification -

         1. Warn and allow to proceed anyway.
         2. Warn and allow to proceed anyway with
            a reason.
         3. Permission request - select a Bypass
            time frame as well.
4. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
5. Click Set.

###### Webpage Data Masking

Mobile Browser - **No support**

This control allows you to mask textual content within webpages. The
masking is set according to either predefined information types (PII or PCI) or
a custom regex.

When this is enabled, the browser will inspect and mask any webpage or
frame within the webpage. This will be done only in situations where the URL in
the browser tab or the URL in the frame is matched. To enable Webpage Data
Masking:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Webpage Data Masking.
3. Select one of the following options:

   - Enable - the Prisma Browser
     will mask URLs in tabs or frames that match the conditions.
     Select the masking pattern:

     - Mask all characters.
     - Leave the last characters unmasked.
     - Leave the first characters unmasked.

       You can choose to unmask up to 4
       characters.
   - Disable - the Prisma Browser won't
     mask URLs in tabs or frames that match the conditions.
4. Prompt - Optionally select one of the following
   prompt options:

   - None - Do not use pop-up notifications.
   - Pop-up notifications 
     - Warn and allow to proceed anyway -
       the prompt will freeze the sensitive information until the
       user acknowledges the message.
     - Warn and allow to proceed anyway with a
       reason - the prompt will freeze the
       sensitive information until the user acknowledges the
       message and selects a reason.
     - Permission request - the prompt will
       freeze and mask the sensitive information until permission
       is granted.
5. Click Set.

   ![]()

###### Typing Guard

Mobile Browser - **No support**

Linux/IGEL Browser - **No support**

Scans manual input made by users in real-time within the browser. It operates
based on defined rules that can be customized based on specific organizational
requirements. To set the Typing Guard control:

Typing guard is only compatible with basic HTML form
fields. It may not function on websites that use complex or JavaScript-based
input methods. For complete copy-paste protection, please use the clipboard
control.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Typing Guard.
3. Select one of the following options:

   - Enable - the Prisma Browser
     will enable the Typing Guard, blocking the users from entering
     potentially sensitive data to the policy rule's application.
   - Disable - the Prisma Browser
     will disable the Typing Guard, and won't block potentially
     sensitive data.
4. Prompt - Optionally select one of the following
   pop-up options:

   - Warn and allow to proceed anyway
     - the prompt will freeze the sensitive information until the
     user acknowledges the message.
   - Warn and allow to proceed anyway with a
     reason - the prompt will freeze the sensitive
     information until the user acknowledges the message and selects
     a reason.
   - Permission request - the prompt will freeze
     and mask the sensitive information until permission is granted.
5. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
6. Click Set.

   ![]()

The new control enables you to control users typing activities within the context
of an Access & Data Control rule. This is designed to
restrict the specific content definitions of the rule.

1. In an Access & Data Control rule, go to the
   When contains section.
2. Select Specific content and select the appropriate
   sensitive information for the rules.
3. Additionally, you can set custom content types to add content that might not
   be included in the predefined types.
4. When users try to type in the sensitive information, the sensitive
   information will be sanitized.

###### Webpage Watermarking

Mobile Browser - **Partial support**

Webpage watermarking enhances Data Loss Prevention (DLP) coverage by providing an
additional layer of security. While screenshot restrictions can prevent users
from capturing on-screen content, they do not prevent the use of external
devices, such as smartphones, to take photos of the screen. This feature applies
a visible overlay to webpages, serving as a deterrent against unauthorized
information sharing. For optimal protection, it is recommended to use webpage
watermarking in conjunction with screenshot control.

**Webpage Watermark control** intelligently applies watermarks exclusively to
pages identified as containing **sensitive content**, minimizing user
friction. This control is active only when you configure the ‘When Contains’
parameter.

The watermark places information on the page, including:

- Company Logo (if it's configured in the browser customization)
- Company Name (if it's configured in the browser customization)
- User's Email
- Date and Timestamp

You can also specify the opacity of the watermark.

To set the Webpage Watermarking control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Webpage Watermarking.
3. Select one of the following options:

   - Enable - The Prisma Browser
     will display the watermark information to deter users from
     taking screenshots.

     1. Select the **Opacity level** using the
        slider
     2. Select the Watermark **Rotation** from the
        drop-down list. The options are -45, 0, or 45 degrees.
     3. Select the **Density** of the watermark from
        the drop-down. The options are:
        - Low
        - Standard
        - High
     4. For the Logo Color, select White to display the logo in a
        single color, or Standard, to display the logo in using its
        original color when uploaded.
   - Disable - The Prisma Browser
     won't display the watermark.
4. Click Set.

   ![]()

###### Print

Mobile Browser - **Partial support**

This feature controls whether or not users can print from websites that match the
URL, application, or category in the rule. To set the Print control:

The Print control can also be used to manage File
Downloads by printing to a PDF.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Print.
3. Select one of the following options:

   - Allow - the Prisma Browser
     will permit printing of webpages and files opened in the Prisma
     Access Browser.
   - Block - the Prisma Browser
     will block all printing of webpages and files opened in the
     Prisma Access Browser.
4. If you want to enable Prompting notifications when you allow printing,
   click the down arrow next to Prompt: Pop-up
   notifications.

   The Prompting notifications are not applicable
   for the Prisma Browser for Mobile.

   1. Configure the following options:

      - **Warn and allow to proceed anyway** - Informs users
        about the risk or sensitivity of printing files, but
        allowing them to continue.
      - **Warn and allow to proceed anyway with a reason** -
        Informs users about the risk or sensitivity of printing
        files, and requires them to provide a reason to continue.
      - **Permission request** - Allows users to send a
        permission request to the admin. The user will be informed
        once the [request](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-requests.html)
        is approved or denied.
        - Choose the timeframe for the permission. You can
          configure the permission to be used once, or for a
          timeframe ranging from 10 minutes to 90 days.
5. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
6. Click Set.

   ![]()

###### Screenshot

Mobile Browser - **Partial support**

Linux/IGEL Browser - **No support**

This feature controls whether or not users can take screenshots (using
snipping tools or Print Screen), record the screen, or share the screen with
video conferencing tools from websites that match the URL, application, or
category in the rule. To set the Screenshot control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Screenshot.
3. Select one of the following options:

   - Allow - the Prisma Browser
     will allow screen capture, screen recording, and screen sharing
     using video conference tools.
   - Allow (Protected) – the Prisma Browser will allow screen captures only from the Prisma Browser's built-in snipping tool. Any other tool will
     be blocked.
   - Block - Prisma Browser will block
     screen capture, screen recording, and screen sharing using video
     conference tools. This is the default behavior.

     This will also block sharing when
     using remote session tools.
4. If you want to enable Prompting notifications when you allow screenshots,
   click the down arrow next to Prompt: Pop-up
   notifications.

   The Prompting notifications are not applicable
   for the Prisma Browser for Mobile. Prompting is only available when you
   select **Allow**, and not **Allow (Protected)**.

   1. Configure the following options:

      - **Warn and allow to proceed anyway** - Informs users
        about the risk or sensitivity of the action, but allows them
        to continue.
      - **Warn and allow to proceed anyway with a reason** -
        Informs users about the risk or sensitivity of the action,
        and requires them to provide a reason to continue.
      - **Permission request** - Allows users to send a
        permission request to the admin. The user will be informed
        once the [request](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-requests.html)
        is approved or denied.
        - Choose the timeframe for the permission. You can
          configure the permission to be used once, or for a
          timeframe ranging from 10 minutes to 90 days.
5. Click Set.

   ![]()

The Prisma Browser has a built-in snipping tool that works with the
Secured Screenshot tool. This gives your end-users the ability to take
screenshots only using the built-in snipping tool, especially in situations
where this is the only option for users to take screenshots.

When the tool is set to Allow (Protected), other screenshot, screen
share, or recording tools will be blocked. The only available tool for
screenshots is the built-in tool.

The control for the snipping tool is located at the bottom of the
sidebar. The control for the tool is located at the top of the browser page, in
the Tools and Actions section.

To enable the Snipping tool, enable and display the Sidebar. The
Snipping Tool icon will be displayed.

When you take a screen capture, the image will be sent to the clipboard. A
message to this effect will be displayed for a few seconds.

The file that you save is stored as a protected file - it's stored as an
encrypted file in the Clipboard. If the File Download control is set as
protected, then the screenshot file will be saved as a protected file. If
the Clipboard control is set to block between applications, you won't be
able to paste the screenshot to any unapproved applications.

###### Read-only Webpage

Mobile Browser - **No support**

You can now configure read-only mode for webpages that are contained
within the Rule's scope.

This allows users to browse the information on web applications. Users
can read the information, download files, but can't input data to any editable
element in the page. This control isn't affected by specific content inspection
- the settings in the When contains schedule. To
configure the read-only webpage:

Read-only applies to HTML elements that are not
editable. It does **not** prevent a web application from listening in to
keyboard strokes, paste operations, mouse clicks, and so on.

This means that
apps written in JavaScript, may still be fully editable if they are not
built from standard HTML components such as HTML Forms.

An example
for an app that is not working with Read-only control is Google
Docs.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Read-Only webpage.
3. Select one of the following options:

   - Enable - the Prisma Browser
     will allow users to read and download the information on web
     applications but won't allow users to input information to any
     editable part of the page. Developer tools will be disabled on
     any webpage affected by this control.

     - **Exclude Login Elements** - Exclude username and
       password elements so that the user will be able to log on.
   - Disable - the Prisma Browser does not
     block any user interaction with the web applications, subject to
     other rules.
4. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
5. Click Set.

   ![]()

###### Camera

Mobile Browser - **No support**

This feature controls whether or not websites that match the URL, application, or
category in the rule have access to the device camera. This control isn't
affected by specific content inspection - the settings in the When contains
schedule. To set the Camera control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Camera.
3. Select one of the following options:

   - Allow - the Prisma Browser
     will allow using the camera in specific webpages.
   - Block - the Prisma Browser
     will block using the camera in specific webpages.
4. Click Set.

   ![]()

###### Microphone

Mobile Browser - **No support**

This feature controls whether or not websites that match the URL, application, or
category in the rule have access to the device microphone. this control isn't
affected by specific content inspection - the settings in the When
contains schedule. To set the Microphone control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Microphone.
3. Select one of the following options:

   - Allow - the Prisma Browser
     will allow using the microphone in specific webpages.
   - Block - the Prisma Browser
     will block using the microphone in specific webpages.
4. Click Set.

   ![]()

---

<a id="configure-malware-protection"></a>

##### Configure Malware Protection

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-malware-protection>*

Malware protection configuration rules

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Malicious File Protection

Mobile Browser - **No support**

This feature allows you to configure scanning with malicious file
protection.

Users can select their preferred scanning engines. The Prisma Browser by default uses the Advanced WildFire scanning engine.
Additional third-party scanning engines can be installed at your discretion with
the appropriate [integration](https://docs.paloaltonetworks.com/prisma-access-browser/integrations.html).

To set the Malicious File Protection control:

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsData Controls
2. Select Malicious File Protection.
3. Select one of the following options:

   - Enable - the Prisma Browser
     will enable malicious file protection.

     - Prevent - Blocks the
       action.
     - Detect only - Notify
       only when there is malicious file event.
   - Engine- Select the Engine
     (described above).

     - Optionally select “In case of scan
       availability, file will be blocked”.
   - Disable - the Prisma Browser will
     disable malicious file protection.
4. When you use this control, you can use your own dialog text to replace the
   default. To set the text, click Set dialog text.
5. Click Set.

   ![]()

---

<a id="live-page-scanning"></a>

##### Live Page Scanning

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/live-page-scanning>*

Live Page Scanning - AB

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Browser | - Refer to the Prerequisites and Scope section below. |

Advanced Web Protection (Live Page Scanning) is a new capability
within Prisma Browser’s web protection module. It provides real-time, in-browser
analysis to protect your users against advanced web-based threats, including
patient-zero attacks and evasive "last-mile" assembly attacks. This feature offers
deep browser-level visibility into page runtime and inspects all traffic, including
QUIC and SSL-pinned applications, without requiring decryption.

- Protect users on **managed and unmanaged devices** (BYOD,
  contractor devices)
- Inspect **encrypted traffic** and apps that cannot be decrypted
  via traditional network inspection
- Detect advanced threats that bypass **inline network analysis**,
  including obfuscated scripts, SaaS platform abuse, and browser-in-browser
  attacks
- Reduce the **patient-zero effect**, ensuring malicious sites are
  flagged before users are impacted
- Maintain **end-user productivity** through real-time
  notifications, read-only access, or custom messaging during scanning

LPS leverages **browser-based execution** of detection models to emulate the
endpoint experience, providing superior visibility into dynamic web content that
traditional network-based analysis cannot inspect.

###### Detection and Enforcement Behavior

- **Browser-based detection flow**: The Browser forwards content to the
  AURL Extension for local inspection using pre-trained models.
- Local vs. Cloud Analysis:
  - **High-confidence threats** are blocked locally without cloud
    interaction.
  - **Low-confidence detections** are forwarded to AURL Hex Cloud for
    additional analysis while allowing the page to load asynchronously.
- Enforcement types:
  - **Inline enforcement**: Requests are blocked once LPS determines
    that there is malicious content. until scanning completes.
  - **Async enforcement**: Page loads while scanning occurs in the
    background.
- **Patient-zero mitigation**: All URLs scanned in-browser feed data back
  to the AURL intelligence database to enhance future threat detection.

###### Prerequisites and Scope

- **Supported platforms** - Prisma Browser on Windows, macOS.
- **Browser Support** - Prisma Browser 142.33.4.176or later.
- **Prisma Browser Console** - Access required to configure policies
  and notifications.
- **Network requirements** - Optional cloud communication for
  low-confidence detections, telemetry, and model updates.
- **Whitelist url** - You need to whitelist the following url: <http://hex-prod-us.urlcloud.paloaltonetworks.com/>

###### Admin Console Configuration

Notify users of ongoing scans, display pages in read-only mode if needed, and
maintain workflow continuity.

**Enable LPS**

Once LPS is enabled, it can take up to 24 hours to take
effect for your end-users.

1. Navigate to PolicyControlsAccess & Data Control PoliciesThreat Protection.
2. Locate **Live Page Scanning**.
3. **Enable** Live Page Scanning.
5. Create a new Access & Data Control rule, Include the Live Page Scanning
   Control, and configure the following:
   1. **Scope** - Select the appropriate Users, User Groups, and
      Device Groups. You can also select Networks, Public IP and
      Geolocation.
   2. **Applications** - Select the applications that will be included
      in the Live Page Scan.

###### Event Reporting and Visibility

A new scan engine, **Live Page Scanning**, is now available. This scan type
appears in web access events when users open defined applications. It also shows
up in incidents when the Live Page Scanning engine detects malicious
activity.

- **Immediate incident events**: Include attack type, URL, timestamp, and
  enforcement action.
- Event viewer / dashboards:
  - Displays detections and scan results.
  - Allows filtering by user, URL, category, or threat type.

###### End User Experience

If a threat is detected, the page is fully blocked - even when the user
scrolls.

The policy indicator will display in the omnibox (the address bar).

To ensure maximum security, Live Page Scanning leverages
more system memory for real-time analysis.

---

<a id="webpage-element-removal"></a>

##### Webpage Element Removal

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/webpage-element-removal>*

The **Webpage Element Removal** tool gives you granular control over how web
content is presented to your end-users.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

The **Webpage Element Removal** tool gives you granular control over how web content
is presented to your end-users.

Instead of fully blocking access to a website, this feature allows you to
selectively remove specific HTML elements—such as buttons, menus, generative AI prompts,
or social interaction controls—before the page is rendered. By modifying the page
structure at render time, organizations can reduce risk while preserving access to
essential business functionality.

Webpage Element Removal helps bridge the gap between unrestricted access and complete
site blocking. This helps you maintain safer workflows and tighter data loss prevention
(DLP) without hindering productivity.

###### Typical Use Cases

The following are some typical use cases for Webpage Element Removal:

- **Social Media Risk Management:** Enable analysts to perform due
  diligence on platforms such as X (formerly Twitter) or LinkedIn while
  removing the ability to "Like," "Retweet," or "Comment" by removing the
  buttons. This prevents accidental "virtue signaling" or attribution during
  investigations.
- **GenAI Data Exfiltration Prevention:** Block embedded AI tools—such as
  Grok on X or AI Overviews in Google Search. This will prevent your users
  from inadvertently submitting sensitive information to public models without
  blocking the core search engine or platform ability.
- **Enhanced RBAC for Critical Apps:** Visually enforce Role-Based Access
  Control (RBAC) on sensitive SaaS platforms. For example, remove the "Delete
  Repository" button in GitHub or "Terminate Instance" in AWS Console for
  junior developers.
- **Data Leakage Protection (DLP):** Hide the "Share" button in Google
  Docs/Sheets/Slides or the "Open in Desktop App" option in SharePoint Online
  (SPO) to force users to work within the secure browser environment.

###### The Element Removal Selector Tool

To configure a removal policy, you first need to identify the exact code (CSS
Selector) of the element you wish to hide. The Prisma Browser contains a
user-friendly tool to assist with this procedure.

###### 1. Enable the Selector

The CSS Selector admin tool is available for all end-users. However, the tool will
not be available on websites for users that have an active policy to remove
elements, ensuring users cannot bring elements back. In addition, when a policy to
block developer tools on a website is enabled, the tool will be disabled to reduce
risks of unauthorized data exposure.

###### CSS Selector Tool Availability

To enable the tool:

1. Open the Prisma Browser menu.
2. Navigate to More tools Customize Prisma Browser.

   ![]()
3. Select **Toolbar**. 

   ![]()
4. Toggle on **Element Selector**.
5. The Prisma Browser icon will now appear in your browser toolbar. 

   ![]()

###### Use the Selector

1. Navigate to the website you wish to modify (e.g. google.com).
2. Click the **Element Selector** icon in the toolbar.
3. Hover over the page; elements will highlight as you move your
   cursor.
4. Click the specific element you want to remove.

###### The Selection Popup

Once an element is clicked, a popup will appear offering the following
controls:

- **Copy Snippet:** Copies the specific CSS selector to your
  clipboard (required for Part 2).
- **Hide/Show:** Toggles visibility to preview what the page looks
  like without the element.
- **Trim Selector:** Adjusts the snippet from the beginning or end
  to make the selection more generic (applying to multiple similar items) or
  more specific.
- **Move selector location:** Use the up/down arrows to move the
  selector location from the bottom/top right corners when needed to select
  different elements.

  ![]()

###### 2. Configure the Removal Policy

Once you have your CSS selector(s), you can enforce the removal via the Prisma
Browser Management Console.

1. Enable the Control
   1. Navigate to **Policy Rules** > **Access & data rules** >
      **Controls and data profiles step**.
   2. Locate the **Webpage Element Customization** section.
   3. Switch the mode from **Disabled** (default) to
      **Enabled**.
2. Add Elements
   1. **Click Add element**
   2. Give the element a name.
   3. **CSS Element:** Paste the snippet copied from the Selector Tool.
   4. You can delete CSS elements from the controls by clicking the
      trashcan icon next to them.
3. Save and Deploy - Once saved, the policy is active. If you disable the
   control later, the removal rules will be ignored but saved for future
   use.

###### Webpage Element Removal

![]()

![]()

###### The End-User Experience

**What do your employees see?** 

1. **Seamless Integration** - The targeted elements simply do not render.
   There are no "blocked" placeholders or error messages where the button used
   to be.
2. **Omnibox Indication:**
3. To ensure transparency, an indicator (featuring your company logo) will
   appear in the address bar (Omnibox) to inform the user that the webpage
   layout has been modified by IT policy. 

   ![]()

###### Frequently-Asked Questions

###### **Q: Can I use the Selector Tool on a page where I have already enforced a removal rule?**

A: No, this is prevented to avoid cases where users can unhide elements
while trying to bypass admin policy

###### **Q: Does this block the website entirely?**

A: No. This control is content-agnostic. It only modifies the visual
presentation (HTML/CSS) of the page to remove specific functionality while
keeping the rest of the site accessible.

###### **Q: Can I apply this to specific users?**

A: Yes. Like other Prisma policies, this can be scoped. However,
remember that administrators can exclude themselves from rules to ensure they
can continue using the Selector Tool for maintenance.

---

<a id="configure-prisma-browser-browser-security-controls"></a>

#### Configure Prisma Browser Browser Security Controls

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security>*

Configure browser security controls for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

You can configure the controls in the following ways:

- When you're creating a new browser security rule, you can set the controls in
  the [Browser Security controls
  page](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-security-rules.html#task-wlg_c5t_fcc_step-browser-security).
- You can [edit an existing rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html#manage-prisma-access-browser-policy-rules_task-edit-rules).
- You can [create a policy profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles.html#manage-prisma-access-browser-policy-profiles_task-jfp_rny_fcc) and
  attach it to a rule.
- You can select it from Strata Cloud Manager
  ConfigurationPrisma Browser
  PolicyControlsBrowser Security.

For information on a control, select the group where it is contained:

- [Browser Security – Browser Session](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-session.html)
- [Browser Security – Browser Hardening](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html)
- [Browser Security – Passwords and Autofill](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-saved-data.html)
- [Browser Security – Network Protection](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-network-protection.html)
- [Browser Security – Extensions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-extensions.html)
- [Browser Security – Internet Express
  Compatibility Mode](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-internet-explorer-compatibility-mode.html)
- [Browser Security – Printers](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-printers.html)
- [Browser Security – Privacy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-privacy.html)
- [Browser Security – Protected Browsing – Attack Surface
  Reduction](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-protected-browsing.html)

---

<a id="configure-browser-session"></a>

##### Configure Browser Session

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-session>*

Configure browser security controls for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Browser Lock

Mobile Browser - **Full support**

Prisma Browser includes a browser lock screen feature that adds an extra
layer of security by requiring user authentication when the browser is accessed.
When Browser Lock is enabled, users must either enter a PIN code, authenticate
using a Passkey, or authenticate using their Identity Provider to unlock the
browser:

- When the browser is first opened or after the Operating System is
  unlocked.
- After a configurable period of idle time away from the device.

This feature is especially valuable for unmanaged devices, where device-level
security policies may not be enforced, and for shared devices, where enterprise
data must be protected from unauthorized access by other users of the same
system.

**Platform Behavior**

- **Windows and macOS**: Idle time is determined using the same system
  mechanism that the operating system uses to trigger sleep mode.
- **Mobile Devices**: The feature relies on the device’s native screen
  lock. PIN length and maximum failed attempts settings are ignored.

The Prisma Browser for Mobile relies on the
native device screen lock, and not the lock that is included in the Prisma Browser tool. The PIN length and Maximum Failed Attempts will be
ignored.

The Authentication method is configured in **Browser Security -> Authentication
Factor**.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Browser Lock.
3. Select one of the following options:

   - **Enable** - enable the Browser lock.

     - Select the **Idle time** - 1 minute to 12 hours
       (or never). This is the time that must elapse before the
       Browser Lock screen appears.
   - **Disable** - the Prisma Access Browser will disable the
     Browser Lock.
4. Click Set.

   ![]()

###### Flush Browser Data

Mobile Browser - **Partial support**

This policy creates temporary browser sessions. This means that browser data will
be cleared upon close, or after a configured time period.

The Prisma Browser for Mobile supports flushing data
when the browser closes. Configuring periodic flushing on the mobile browser
will have no impact.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Flush Browser Data.
3. Select one of the following options:

   - **Enable** - the Prisma Browser flush the
     browser data.

     - Select the attributes to clear:

       - Browsing history
       - Download history
       - Cookies and other site data
       - Cached images and files
       - Passwords and Passkeys
       - Autofill
       - Site settings.
       - Host app data
     - Select the trigger for the browser flush
       action:

       - **Browser close** - the data will be
         flushed when the browser is closed.
       - **Time period** - the data will be
         flushed after the configured time elapsed. If this
         option is selected, you can set the flush time
         from 1-24 hours.
   - **Disable** – disable the Browser flush feature.
4. Click Set.

   i

   ![]()

###### Concurrent Browser Sessions

Mobile Browser - **Full support**

This policy allows you to determine the maximum number of devices that a user can
have logged into the browser at one time during the retention period. This
includes both Prisma Browser and Prisma Browser for Mobile.

- The back-end stores session data for 7 days (the retention period).
- Prisma Browser sessions expire after 7 days of inactivity or upon
  manual logout.
- Prisma Browser for Mobile sessions often stay active in the
  background to sync policy updates; this will prevent a session from
  becoming inactive. Mobile browser sessions must be closed
  manually

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Concurrent number of devices.
3. Select one of the following options:

   - **Limit number of devices** - You will be able to
     limit the number of browser session concurrently. You can set
     the maximum to between 1 and 5 concurrent sessions per user.
   - **Unlimited number of devices**  – There is no limit to the
     number of concurrent sessions that users can have.
4. Click Set.

   ![]()

###### Session Refresh

Mobile Browser - **No support**

You can now set a time period after which users must log in again to
re-authenticate. Fifteen minutes before the session expires, users will see a
warning message in their current tab, notifying them that the session is nearing
expiration. They can re-authenticate before the session ends by clicking
**Re-authenticate Now**.

Policy changes only apply after the next logout.

For example, if session refresh was set to 9h, and is turned off,
the user will still be logged out after 9h. They will not be logged out
after their next session.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Session Refresh.
3. Select one of the following:

   - **Enable** to enable Session Refresh, then select **Log the user
     out every**: and select an appropriate time frame, ranging
     from 1 hour to 30 days
   - **Disable** to disable Session Refresh.
4. Click Set.

   ![]()

---

<a id="configure-browser-hardening"></a>

##### Configure Browser Hardening

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening>*

Configure browser security controls for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Cast

Mobile Browser - **No support**

This feature controls the ability to screencast a tab or the desktop via the
Prisma Access Browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Cast.
3. Select **Allow** to permit casting or **Block** to deny casting.
4. Click Set.
5. Restart the browser to apply this feature.

   ![]()

###### Developer Tools

Mobile Browser - **No support**

This feature actively controls users' ability to open Developer Tools
or manually load browser extensions in "Developer Mode" via "load unpack". It
can also assist with preventing users from running unauthorized JavaScript code
in the Developer Tools console.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Developer Tools.
3. Select **Allow** to permit the Developer options, or **Block** to
   deny their use.
4. Click Set.

   Restart the browser to apply this feature.

   ![]()

###### Native Messaging Hosts

Mobile Browser - **No support**

Native Messaging Hosts allows the software installed on the device to communicate
with Prisma Browser and its installed extensions, and vice versa. Enterprise
software that interacts with the browser typically requires you to select "Allow
only hosts installed with admin permissions."

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Native Messaging Hosts.
3. Select one of the following options:

   - **Allow** – the browser will **be** able to
     communicate with Native Messaging Hosts.
   - **Allow only hosts installed with admin permissions**
   - **Block** – the browser’s use of Native Messaging Hosts will
     be restricted.
4. Click Set.

   ![]()

###### JavaScript Running from Omnibox

Mobile Browser - **No
support**

This feature determines whether or not users will be able
to run JavaScript code from the browser omnibox (Address Bar). Users may exploit
this functionality to manipulate web pages using JavaScript.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select JavaScript Running from Onmibox.
3. Select one of the following options:

   - **Allow** – the Prisma Browser will allow
     JavaScript to run from omnibox..
   - **Block** – the Prisma Access Browser will restrict JavaScript
     from running from omnibox.
4. Click Set.

   ![]()

###### Keylogging Protection

Mobile Browser - **No support**

Linux/IGEL Browser - **No support**

This policy allows you to determine if keylogging protection will be enabled.
Keylogging tools can monitor and report a user's actions as they interact with
the computer. As the name suggests, a keylogger records what the user types, and
reports the information back to whoever installed the logger.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Keylogging Protection.
3. Select one of the following options:

   - **Allow** – Keyloggers will be prevented from
     listening to keystrokes typed on Prisma Browser.
   - **Block** – Keylogging protection is turned off.
4. Click Set.

   ![]()

###### Browser self-protection

Mobile Browser - **Support for Windows only.**

The **Browser self-protection** control enhances the security of Prisma
Browser in high-risk environments, particularly on unmanaged or contractor
devices (BYOD). These devices often grant users administrative privileges,
increasing exposure to insider threats and malware.

For additional background information, refer to [Prisma Browser Self-Protection for
Windows](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/prisma-browser-self-protection-fpr-windows.html).

To mitigate these risks, Prisma Browser introduces an advanced **runtime
protection mechanism** based on a Windows kernel-level driver. This
ensures the browser process remains protected from tampering and unauthorized
interference during operation.

You can remotely enable or disable this driver-based protection. This control is
disabled by default, and applied only when Prisma Browser is installed with
Administrative privileges on Windows, and the user is running the browser as
Administrator.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Browser self-protection.
3. Select one of the following options:

   - **Enable** – Browser self-protection will be enabled
     and will run whenever the browser is called. In addition, you
     are able to define the browser's enforcement action when the
     self-protection module cannot be started. The options are:
     - Do not enforce - Browser runs normally.
     - Prompt and proceed anyway - Browser runs normally, but a
       warning is displayed.
     - Block browser access - Browser shuts down and message is
       displayed
   - **Disable** – Browser self-protection will be disabled, and
     will not function.
4. Click Set. 

   ![]()

###### Popups

Mobile Browser - **Support for iOS only.**

With this feature, you can control the display of popups in the
browser.

The popups can be allowed, allowed with exceptions, blocked, or blocked
with exceptions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Popups.
3. Select one of the following options:

   - **Allow** – Popups will be permitted in the browser.
     You can specifically exclude domains from being allowed. This
     will block popups from those domains only.
   - **Block** – Popups will be blocked. You can specifically
     exclude domains from being blocked. This will allow popups from
     those domains only.
4. Click Set.

   ![]()

###### Notifications

Mobile Browser - **No support**

You can use this feature to control notifications being displayed within the
browser. The notifications can be allowed, allowed with exceptions, blocked, or
blocked with exceptions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Notifications.
3. Select one of the following options:

   - **Allow** - Notifications will be permitted in the
     browser. You can specifically exclude specific domains. This
     will block notifications from these domains.
   - **Block** - Notifications will be blocked. You can
     specifically exclude specific domains from the rule. This will
     allow popups from those domains only.
4. Click Set.

   ![]()

###### Authentication Factor

Mobile Browser - **No support**

The Authentication Factor is used to configure the authentication
method used by the Prisma Access Browser to trigger authentication for step-up
MFA authentication, browser lockscreen and unlocking the password manager. A
single authentication factor is used for all actions.

The Authentication factor is triggered by one of the following actions (if
configured):

- Web access > Require MFA
- Login controls . Login Form > MFA
- Data controls > Data Leak Prevention > File Download > Prompt > Require
  MFA
- Data controls > Data Leak Prevention > File Upload > Prompt > Require
  MFA
- Browser Security > Browser Session > Browser Lock

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Authentication Factor.
3. Select one of the following options:

   - **PIN Code**
     - Configure the PIN code length (between 4-6 digits) and
       the number of attempts that can be made before the
       account will be locked out.
     - If the user is locked out, or they forget their PIN
       code, they need to re-authenticate with their identity
       provider to reset the PIN code.

       PIN codes are not synced
       between devices. Users need to create a separate PIN
       code on each device.

       ![]()
   - **Passkey**
     - Select the type of passkey that the users can create:
       - Internal authenticator - Passkeys stored locally
         on the device such as Windows Hello or macOS
         keychain
       - External authenticator - Passkeys stored
         externally, on other devices, such as the user’s
         mobile phone, security key (for example, a
         yubikey), or smartcard

         Passkeys are not synced between devices. Users
         need to create a separate Passkey on each
         device.

         ![]()
   - **IdP Authentication**
     - Prisma Browser authentication profile – Re-authenticates
       the user with the same IdP authentication profile they used
       to log in to Prisma Browser.
     - Choose profile – Gives admins flexibility by allowing them
       to choose a dedicated authentication profile with different
       IdP authentication factors from the standard Prisma Browser login process (e.g. require Microsoft
       Authenticator).

       All
       Prisma Browser users must be provisioned in the
       identity provider and assigned to the application in the
       selected authentication profile. Otherwise, they will be
       unable to complete actions that require MFA.

   To configure a dedicated profile:
   - Follow the instructions to create a new application in the
     identity provider that will be used to authenticate users (Entra
     ID, Okta, Other IdP)

     When
     creating an authentication type in CIE, select **Dynamic
     service provider metadata**

     ![]()
   - Create a SAML authentication profile in CIE associated to the
     application you created in the identity provider.
   - Choose the newly created profile in the Authentication Factor
     control.
   - **Use isolated browser session (incognito)** - Starts each
     authentication attempt in a clean and isolated session, without
     cookies or cache. Admins can turn it off if they need to retain
     other cookies during IdP MFA. Turning this option off is
     required to enable *pass-through* authentication via
     Microsoft SSO - as an isolated browser session doesn't support
     it. This feature is enabled by default.
   - Force Re-authentication - Prevents silent re-authentication by
     requiring users to enter credentials each time.they have an
     active IdP session
     - Asks the identity provider to forcibly re authenticate
       (ForceAuthn=true) the user even if they had a
       pre-existing session with the IdP.**Important:** When creating an authentication type in CIE,
   select “Dynamic service provider metadata”

   ![]()
4. Click Set.

###### Advanced Browser Protection

Stops zero-day WebAssembly attacks in real time by monitoring in-browser memory
behavior and terminating malicious execution before any impact occurs.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Advanced Browser Protection.
3. Select one of the following options:

   - **Enable** – Enable Advanced Browser Protection.
   - **Disable** – Disable Advanced Browser Protection.
4. Click **Set**.

###### Cookies Protection

Mobile Browser - **No Support**

This feature strengthens Prisma Browser’s isolation from the underlying host
device, significantly mitigating the risk of cookie hijacking via malware or
physical access. Once enabled, cookies are encrypted both **at-rest
(on-disk)** and **in-memory**, protecting against memory dump exploits
and unauthorized access via Developer Tools.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Cookies Protection.
3. Select one of the following options:

   - **Enable:** Enable this feature.
   - **Disable:** Disable this feature.
4. Click **Save**.

   ![]()

   To maintain a seamless user experience, Prisma Browser automatically decrypts **"Allowed"** or
   **"Force-installed"** extensions. This ensures full functionality
   and management compatibility while maintaining robust encryption for all
   underlying data to protect against external threats.

###### End Process via Task Manager

Mobile Browser - **No Support**

Choose whether end users can end browser processes via the browser task
manager.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select End Process via Task Manager.
3. Select one of the following options:

   - **Allow** – Allow users to end browser processes via
     the browser Task Manager.
   - **Block** – Block users from being able to end browser
     processes via the browser Task Manager.
4. Click **Save**.

   ![]()

###### Open Links in External Apps

Mobile Browser - **Mobile only**

While most of the time we want to keep the Prisma Browser as a secure bubble,
that all work is done only in the browser. This is not possible for a few
reasons. First of all, some applications can't be opened in a browser, such as
Zoom, Teams, Slack, among others. Blocking these apps would result in a terrible
user experience. Second, most mobile devices are BYOD. Third, Some URLs can only
be opened in a native app.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Open Links in External Apps.
3. Select one of the following options:

   - **Always** – External apps will always open in
     native applications.
   - **Only for specific apps** – Only selected links will open in
     external apps. The following apps can be selected:
     - MS Teams
     - MS Outlook
     - Microsoft 365
     - Slack
     - Zoom
     - Salesforce
     - Gmail
     - Google Workspace (Sheets, Docs, Slides)
     - Google Drive.
   - **Never** - External apps will never open in native
     applications.
   - **Users decide when to open links in native apps** - End users
     will be able to decide when to open links in Prisma Browser
     and when to use a native app.
4. Click **Save**.

   ![]()

---

<a id="configure-saved-data"></a>

##### Configure Saved Data

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-saved-data>*

Saved Data Security Controls

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Password Manager

This control allows you to enable the Prisma Browser Enterprise Password Manager to manage and secure company passwords and logins.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Password Manager.
3. Select one of the following options:

   - **Enable** - Enable the Password Manager to manage
     users passwords and logins.

     - **Require MFA to obtain or autofill logins** - Select
       this option to determine how often your users will need to
       re-enter their MFA for a new login. You can require that the
       MFA be entered every time the information from the Password
       manager is accessed, or they will need to enter their MFA
       for a new login every selected time period. The current
       range is between 1 and 30 minutes.
   - **Disable** - Do not enable the Password Manager .

     ![]()

###### Password Saving

Mobile Browser - **Full
support**

This feature determines whether the browser will be able
to save passwords for websites.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Password Saving.
3. Select one of the following options:

   - **Allow** - Users will be able to save passwords in
     the browser.
   - **Block** - Users will be restricted to save passwords in the
     browser.
4. Click Set.

   ![]()

###### Autofill of Forms

Mobile Browser - **No support**

This feature determines whether or not the browser will store
information to autofill forms.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyProfilesBrowser Security
2. Select Autofill of Forms.
3. Select one of the following options:

   - **Allow** – The browser will save information to
     autofill forms in the future.
   - **Block** – The browser will not save form information to be
     filled automatically in the future.
4. Click Set.

   ![]()

###### Autofill of Credit Cards

Mobile Browser - **No support**

This feature determines whether or not the browser will allow users to store
credit card information.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Autofill of Credit Cards.
3. Select one of the following options:

   - **Allow** – Prisma Browser will be able to save
     credit card details.
   - **Block** – Prisma Browser will be restricted from saving
     credit card details for future use.
4. Click Set.

   ![]()

---

<a id="configure-network-protection"></a>

##### Configure Network Protection

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-network-protection>*

Configure Network Protection.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Pages with SSL Errors

Mobile Browser - **Full support**

This feature manages how the Prisma Browser will react when it
encounters a page with an SSL error. In general, most browsers ask for
permission to "Proceed to [FQDN] (unsafe)".

Since SSL errors can occur during an SSL MitM attack, you can use this
control to block the "Proceed..." functionality.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Pages with SSL Errors.
3. Select one of the following options:

   - **Allow** - Allow users to bypass the blocking page
     when an SSL issue is identified.
   - **Block** – The Prisma Browser will block the "Proceed..."
     option when an SSL issue is identified.
4. Click Set.

   ![]()

###### DNS-Over-HTTPS

Mobile Browser - **No support**

This feature manages the DNS resolution over the HTTPS protocol. It is
used for encrypting requests.

This assists in preventing MitM attacks.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select DNS-Over-HTTPS.
3. Select one of the following options:

   - **Enable** - Enter the following information:

     **Upon DNS over HTTPS resolve failure:**

     - **Fail-open:** Resolve using plain DNS.
     - **Fail-close:** Do not resolve.
   - Enter the **DNS-over-HTTPS resolver's** URL.
   - **Disable** – Prisma Browser will not enable DNS over
     HTTPS resolution.
4. Click Set.

   ![]()

###### Trusted Certificate Authorities

Mobile Browser - **Partial support**

This feature manages how the Prisma Browser manages
certificates.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Trusted Certificate Authorities.
3. Select the certificate authorities that are to be trusted by the Prisma Browser (this limits the trust to certificates that are already
   trusted):

   - **Device trust store** - Trust the certificate
     authorities installed in the device's certificate store.
   - **Prisma Access Browser trust store** - Trust only
     certificate authorities that are trusted by Palo Alto Networks,
     and ignores certificates installed in the Device trust store.
   - **None** - Do not trust certificates in any trust store.

     Prisma Browser for Mobile rules using
     this control **must** use one of the Trust Stores. The
     **None** option is ignored.
4. **Additional trusted certificate authorities**- Add customer-provided
   certificates not already trusted by the Prisma Browser.

   1. Enter a name for the certificate.
   2. Drag or Browse a certificate in .pem, .der, .crt, or
      .cer formats.

      ![]()
5. Click Set.

   ![]()

###### Basic Authentication over HTTP

Mobile Browser - **Full support**

This feature controls whether the Prisma Browser can use Basic
Authentication over HTTP websites.

Since Basic Authentication sends authentication tokens in clear text,
sending them over HTTP can be visible to attackers as part of a MitM attack.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Basic Authentication over HTTP.
3. Select one of the following options:

   - **Allow** - allow Prisma Browser to use Basic
     Authentication over HTTP websites.
   - **Block** – block Prisma Browser from using Basic
     Authentication over HTTP websites.
4. Click Set.

   ![]()

###### Pages with Insecure Content

Mobile Browser - **No support**

This feature controls whether users can load insecure content (data
located on HTTP servers) to secure websites (located on HTTPS servers).

You can choose to exclude specific domains from this feature when there
are specific applications that need an exception to the rule.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Pages with Insecure Content.
3. Select one of the following options:

   - **Allow**- Prisma Browser will allow insecure
     content.

     1. **Exclude specific domains** - list domains
        that will receive an exception to the rule.
   - **Block** – Prisma Browser will not allow
     insecure content.

     1. **Exclude specific domains** - list domains that will
        receive an exception to the rule.
4. Click Set.

   ![]()

###### Force HTTPS

Mobile Browser - **Partial support**

You can force the use of the **HTTPS protocol**, minimizing the risk
of [MitM attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

You will be able to force HTTPS for all domains, force HTTPS but
exclude certain domains, or disable forced HTTPS and work without any
restrictions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Force HTTPS.
3. Select one of the following options:

   - **Enable**- Prisma Browser will require use of
     the HTTPS protocol.

     You can enter specific domains that will be excluded
     from this requirement in the **Exclude specific Domains**field.

     **Exclude specific
     domains** is not available for the for Prisma Browser
     for Mobile.
   - **Disable** – Prisma Browser will not require
     use of the HTTPS protocol.
4. Click Set.

   ![]()

###### Post-Quantum Key Support

Mobile Browser - **No support**

This feature manages the ability to enable or disable the use of post-quantum key
agreement protocols within TLS (Transport Layer Security). Post-quantum
cryptography refers to algorithms designed to be secure against quantum computer
attacks, which could potentially break traditional cryptographic methods. While
enabling this feature enhances security by preparing for future quantum threats,
it may cause compatibility issues with existing network security products that
do not yet support or recognize post-quantum algorithms. Disabling it may help
avoid these conflicts, but it reduces future-proofing against emerging
quantum-based vulnerabilities.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select **Post-Quantum Key Security**.
3. Select one of the following options:
   1. **Enable** - Permits the use of Post Quantum Key Security.
   2. **Disable** - Disables the use of Post Quantum Key Security.
   3. **Not set** - The feature is not enabled. This is the default
      setting.
4. Click **Set**.

   ![]()

###### Kerberos Delegation Allowlist

Mobile Browser - **No support**

List the hosts that may forward a user’s Kerberos ticket to downstream services.
When this is enabled, the Kerberos ticket is used in place of your SSO so that
back-end services are easier yo use.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select **Kerberos Delegation Allowlist** .
3. Select one of the following options:
   1. **Enable** - Activates real-time host scanning of the selected
      hosts. For information on specifying hosts in the correct pattern,
      refer to [this page](https://chromeenterprise.google/policies/url-patterns/). of t.
   2. **Disable** - Disables the use of the real-time host scanning.
4. Click **Set**.

   ![]()

###### Remote Host Firewall Traversal.

Mobile Browser - **No support**

This policy controls whether the Remote Desktop can bypass firewalls. When
enabled, users can connect remotely from any network. When disabled, access is
limited to the same local network or VPN, enhancing security by restricting
remote access.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select **Remote Host Firewall Traversal** .
3. Select one of the following options:
   1. **Allow** - Allow users to connect remotely from any network.
   2. **Block** - Remote connection is only permitted from the same
      local network or VPN.
4. Click **Set**.

   ![]()

###### Authentication Server Allowlist

Mobile Browser - **No support**

**Authentication Server Allowlist** allows you to create a comprehensive
inventory of servers that are explicitly configured and permitted to utilize
Integrated Authentication (IA) protocols, such as Kerberos, for secure access to
protected resources.

For more information, refer to [AuthServerAllowlist on the Chrome Enterprise
site](https://chromeenterprise.google/policies/#AuthServerAllowlist)

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyProfilesBrowser Security
2. Select **Authentication Server Allowlist** .
3. Select one of the following options:

   - **Set server allowlist:**
     - Enter the list of specific domains and hosts. Click here for
       more information on the [domain syntax.](https://chromeenterprise.google/policies/url-patterns/)
   - **Unset** - Remove the list of domains.
4. Click **Set**.

   ![]()

###### Local Network Access Restrictions

Mobile Browser - **No support**

The local network access permission prompt and
restrictions feature is targeted to affect browsers versioned 146.xx and above.

**Local Network Access Restrictions** is a security control that allows you to
govern how websites interact with devices located on your users local networks.
This manages the underlying *[LocalNetworkAccessRestrictionsEnabled](https://chromeenterprise.google/policies/#LocalNetworkAccessRestrictionsEnabled)*, *[LocalNetworkAccessAllowedForUrls](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)*, *[LocalNetworkAccessBlockedForUrls](https://chromeenterprise.google/policies/#LocalNetworkAccessBlockedForUrls)* policies for Chromium-based
browsers.

The default value for desktop devices is 'Use default restrictions' meaning, a
user will be prompted to manage all local network access.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyProfilesBrowser Security
2. Select **Local Network Access Restrictions** .
3. Select one of the following options:
   1. **Configure Restrictions** - Decide where to allow or block
      local network access requests. You will then need to enter the
      **Auto Allow Local Network Access List**
      *or* the **Block Local Network Access List**.

      If a Local Network is configured to be
      blocked and allowed, the block takes precedence.
   2. **Use default restrictions** - Users will be prompted for all
      local network access.
4. Click **Set**.

   ![]()

---

<a id="configure-extensions"></a>

##### Configure Extensions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-extensions>*

Configure Browser Security Extensions

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Allowed or Blocked Extensions

Mobile Browser - **No support**

Allowed or Blocked Extensions give you control over which extensions are
permitted in the Prisma Browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Allowed or Blocked Extensions.
3. Select one of the following options:

   - **Allow all** - Allow all extensions.
   - **Block specific extensions by ID or Risk** - You
     can select specific extensions to block. The extension must be
     identified either by its **ID** or its **Risk**.
   - **Allow specific extensions by ID** - You can
     select specific extensions to permit. The extension must be
     identified by its ID.
   - **Block all** - block all extensions.
4. Click Set.

   ![]()

###### Block Extensions by Permission

Mobile Browser - **No support**

This control allows you to block extensions based on their required
permissions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Block Extensions by Permission.
3. Select one of the following options:

   - **Grant all permissions** - permit running
     extensions without regard to their required permissions.
   - **Block extensions that use specific permissions** - block
     that requires specific permissions. Permissions that were not
     selected will be permitted. You can select as many permissions
     as required.
4. Click Set.

   ![]()

###### Restrict Extension Host Permissions

Mobile Browser - **No support**

This control allows you to restrict Host permissions for extensions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Restrict Extension Host Permissions.
3. Select one of the following options:

   - **Enable** - Enable restricting Extension Host
     Permissions.
   - **Enable for specific domains** - Enable restricting host
     permissions for specified domains only.
   - **Disable** - Disable restricting Extension Host Permissions.
4. Click Set.

   ![]()

###### Restrict Extension Host Permissions

Mobile Browser - **No support**

This control allows you to hide sensitive data - any data that can compromise
user information and be used for illicit logins - from extensions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Restrict Extension Host Permissions.
3. Select one of the following options:

   - **Enable** - prevent extensions from running scripts
     and accessing content.
   - **Enable for specific domains** - prevent extensions
     from running scripts and accessing content from specific
     domains. Click [here](https://developer.chrome.com/docs/extensions/mv3/match_patterns/) to see
     information regarding domain syntax.
   - **Disable** - do not prevent extensions from running scripts
     and accessing content.
4. Click Set.

   ![]()

---

<a id="configure-internet-explorer-compatibility-mode"></a>

##### Configure Internet Explorer Compatibility Mode

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-internet-explorer-compatibility-mode>*

PAB Internet Explorer Compatibility

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Internet Explorer Compatibility Mode

Mobile Browser - **No support**

Internet Explorer Compatibility Mode does not support
Private Apps.

Microsoft has announced end-of-support dates for different versions of
IE. For more information, refer to [Microsoft's Lifecycle FAQ](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge).

Organizations may require compatibility with Internet Explorer, as they
are running internal legacy websites.

You can select these particular sites and allow users to access them in
the Prisma Browser using Internet Explorer Compatibility Mode. This will
render the application or site as if it were being accessed via Internet
Explorer.

The Prisma Browser Internet Explorer ~Compatibility
Mode is compatible with the Internet Explorer browser version 11.

Click [here](https://chromeenterprise.google/policies/url-patterns/) for more information regarding
entering URLs.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyProfilesBrowser Security
2. Select Internet Explorer Compatibility Mode.
3. Select one of the following options:

   - **Enable compatibility mode** - You need to add the
     target URLs that need Internet Explorer Compatibility.
   - **No compatibility mode support** - Users will not be able to
     use sites that require IE Compatibility.
4. Click Set.

   ![]()

---

<a id="configure-printers"></a>

##### Configure Printers

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-printers>*

The is the Browser Security Network configuration

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Allowed Printers

Mobile Browser - **No support**

The Prisma Browser allows you to configure particular printers for
users who need to print from the browser. This provides an additional level of
security, where end-users will only be able to print to permitted devices, such
as printers in the office.

This feature does not preclude users from printing from other devices
when using applications not managed through the Prisma Browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Allowed Printers.
3. Select one of the following options:

   - **No printers** – end-users cannot print from the
     browser.
   - **Set printers** - Click **Add Printer** to enter the
     network location of each printer that end users will be able to
     select when printing is required.
4. Click Set.

   ![]()

---

<a id="configure-privacy"></a>

##### Configure Privacy

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-privacy>*

Browser Security Privacy configuration

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Third-party Cookies

Mobile Browser - **No support**

The Prisma Browser allows you to configure whether or not you will
accept cookies from web pages that are not from the domain that's in the address
bar.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Third-party Cookies.
3. Select one of the following options:

   - **Allow** - Third-party elements can set
     cookies.
   - **Block** - Third-party elements cannot set cookies.
4. Click Set.

   ![]()

###### Browser History

Mobile Browser - **No support**

The Prisma Access Browser allows you manage the ability to delete the
browser history.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Browser History.
3. Select one of the following options:

   - **Enable** - browser history is saved.
   - **Disable** - browser history is not saved, and tab
     syncing is disabled. This setting cannot be changed by
     users.
   - **Block Deletion** - browser history and download history
     cannot be deleted.
4. Click Set.

   ![]()

###### Cookies

Mobile Browser - **No support**

This policy controls the ability to store cookies on the browser. It allows
companies to keep the data only for the session to avoid theft of the
credentials.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Cookies.
3. Select one of the following options:

   - **Allow** - default cookies behavior, as controlled
     by the end-user.

     After choosing this option, you can select specific
     domains to exclude. This means that the selected domains will
     not be able to set cookies.
   - **Block** - do not allow any websites to set the
     local data.

     Blocking cookies can
     cause issues with loading websites.

     After choosing this option, you can select specific
     domains to include. This means that the selected domains will be
     able to set cookies.
   - **Session only** - keep cookies for the duration of the
     session. After choosing this option, you can select the URLs
     that will keep cookies for the duration of the session.
4. Click Set.

   ![]()

---

<a id="configure-protected-browsing"></a>

##### Configure Protected Browsing

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-protected-browsing>*

Attack Surface reduction

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Anti-exploitation controls enable you to reduce the potential attack
surface of the browser. These controls effectively limit usage of browser components
that are complex and are occasionally found to contain vulnerabilities. While the
latest version of the browser would never include known vulnerabilities, disabling
unnecessary components limits the potential exposure between when a vulnerability is
found and the time it is fixed.

You should be aware that by disabling these components, you may impact some
web page functionality. To minimize the impact on end-users, a non-intrusive dialog
will be displayed if a capability is canceled. You need to be aware of these dialogs
and the corresponding events in case users report issues with web pages. For
example, disabling WebGL may impact functionality of an online maps website. When
the users complain, you can identify the issue by looking for corresponding events
and dialogs when users browse to these sites.

When a web page is affected by a disabled component, an abbreviated message
is shown. The message will pop up again every 2 hours if you revisit the website.
The system will also generate a log event.

###### **JavaScript v8 JIT & WebAssembly (WASM)**

Mobile Browser - **No support**

You can strengthen browser security by blocking JavaScript V8 JIT &
WebAssembly (WASM) to reduce the risk of exploitation.

- **Block JavaScript v8 JIT** to reduce the risk of exploitation and to
  enable advanced mitigation techniques such as Control Flow Guard (CFG),
  Control-flow Enforcement Technology (CET), and Arbitrary Code Guard
  (ACG).

  Blocking JIT may
  impact overall browser performance.
- **Block WebAssembly (WASM)** to lower the attack surface for modern
  exploitation techniques.

Disabling the JavaScript V8 Just-In-Time (JIT) compiler helps reduce
exploitation risks and enables additional security mitigation techniques,
including Control Flow Guard (CFG), Control-flow Technology (CET), and Arbitrary
Code Guard (ACG).

Blocking WASM may limit
functionality in advanced web applications.

Use this configuration if your security posture prioritizes reduces vulnerability
exposure over performance or feature compatibility.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select JavaScript v8 JIT.
3. Select one of the following options:

   - **Enable** - Enable use of JavaScript v8 JIT and WebAssembly.
   - **Disable JavaScript advanced optimization** - Disable use of
     JavaScript v8 JIT. You can optionally select specific domains to
     exclude.
   - **Disable JavaScript JIT, including WebAssembly**- Disable the
     use of JavaScript JIT and WebAssembly. You can optionally select
     specific domains to exclude.

     To exclude
     specific applications, enter their domains into the exclusion
     list. Click [here](https://chromeenterprise.google/policies/url-patterns/) for more
     information regarding entering URLs.
4. Click Set.

   ![]()

###### WebRTC

Mobile Browser - **No support**

Web Real-Time Communication (WebRTC) is an open-source project that
enables real-time voice, text, and video communication capabilities between web
browsers and devices.

This anti-exploitation policy controls the use of the WebRTC protocol,
which can be potentially exploited.

Disabling WebRTC will prevent some video
conferencing tools, such as Microsoft Teams, Google Meet, Zoom, and WebEx from
working. To overcome this issue, add their domains to the exclusion list as
described below.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebRTC.
3. Select one of the following options:

   - 1. **Allow** - Allow the use of WebRTC.
     2. **Block**- Block the use of WebRTC.
     3. To exclude specific applications, enter their domains
        into the exclusion list. Click [here](https://chromeenterprise.google/policies/url-patterns/) for more
        information regarding entering URLs.
4. Click Set.

   ![]()

###### PDFium

Mobile Browser - **No support**

The PDFium library is used to render PDF files in Chromium
browsers.

This anti-exploitation policy controls the use of the PDFium library,
which can be potentially exploited.

When PDFium is disabled, the Prisma Access Browser will not be able to
open regular or protected PDF files.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select PDFium.
3. Select one of the following options:

   - 1. **Allow** - Permit use of the PDFium library
        to render PDF files.
     2. **Block**- Block use of the PDFium library
        to render PDF files.
4. Click Set.

   ![]()

###### WebGL API

Mobile Browser - **No support**

WebGL is a JavaScript-based API that is used for rendering high
performance interactive 2-and 3D graphics using hardware graphics acceleration
features provided in the user's device.

This anti-exploitation policy controls the use of the WebGL API, which
can be potentially exploited.

**Note:** Disabling WebGL API may impact different websites using it
in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebGL API.
3. Select one of the following options:

   - 1. **Allow** - Permit use of the WebGL API.
     2. **Block**- Block use of the WebGL API.
4. Click Set.

   ![]()

###### File System API

Mobile Browser - **No support**

The File System Access API (formerly known as the Native File System
API and Writable Files API) enables developers to build powerful web apps that
interact with files on the user's local device, such as IDEs, photos, video
editors, text editors, and more. After a user grants a web app access, this API
allows them to read or save changes directly to files and folders on the user's
device. Beyond reading and writing files, the File System Access API allows
opening a directory and enumerating its contents.

This anti-exploitation policy controls the use of the File System API,
which can be potentially exploited.

**Note:** Disabling File System API may impact different websites
using it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select File System API.
3. Select one of the following options:

   - 1. **Allow** - Permit use of the File System
        API.
     2. **Block**- Block use of the File System
        API.
4. Click Set.

   ![]()

###### Sensors API

Mobile Browser - **No support**

The Sensors API controls access to several different low-level and
high-level device sensor types.

This anti-exploitation policy controls the use of the Sensors API,
which can be potentially exploited.

**Note**: Disabling Sensors API may impact different websites using
it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Sensors API.
3. Select one of the following options:

   - **Allow** - Permit use of the Sensors API.
   - **Block** - Block use of the Sensors API.
4. Click Set.

   ![]()

###### WebSerial API

Mobile Browser - **No support**

The WebSerial API provides a method for websites to read from and write
to serial devices. The devices can be connected via serial port, or by USB or
Bluetooth devices that emulate a serial port.

This anti-exploitation policy controls the use of the WebSerial API,
which can be potentially exploited.

Disabling WebSerial API may impact different
websites using it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebSerial API.
3. Select one of the following options:

   - **Allow** - Permit use of the WebSerial API.
   - **Block** - Block use of the WebSerial API.
4. Click Set.

   ![]()

###### WebBluetooth API

Mobile Browser - **No support**

The WebBluetooth API provides a way for websites to communicate over
GATT (Generic ATTribute Profile) with nearby user-selected Bluetooth devices in
a secure and privacy-preserving way.

This anti-exploitation policy controls the use of the WebBluetooth API,
which can be potentially exploited.

Disabling WebBluetooth API may impact different
websites using it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebBluetooth API.
3. Select one of the following options:

   - **Allow** - Permit use of the WebBluetooth API.
   - **Block** - Block use of the WebBluetooth API.
4. Click Set.

   ![]()

###### WebUSB API

Mobile Browser - **No support**

The WebUSB API is a JavaScript specification for providing secure
access from web pages to USB devices.

This anti-exploitation policy controls the use of the WebUSB API, which
can be potentially exploited.

Disabling WebUSB API may impact different websites
using it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebUSB API.
3. Select one of the following options:

   - **Allow** - Permit use of the WebUSB API.
   - **Block** - Block use of the WebUSB API.
4. Click Set.

   ![]()

###### WebHID API

Mobile Browser - **No support**

The WebHID API is used for providing access for Human Interface
Devices. This feature permits access to alternative auxiliary devices, such as
secondary keyboards and mouse-pointing devices.

This anti-exploitation policy controls the use of the WebHID API, which
can be potentially exploited.

Disabling WebHID API may impact different websites
using it in a legitimate way.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select WebHID API.
3. Select one of the following options:

   - **Allow** - Permit use of the WebHID API.
   - **Block** - Block use of the WebHID API.
4. Click Set.

   ![]()

###### Print Preview

Mobile Browser - **No support**

Print Preview displays the print preview in a new tab, a DOM UI page.
The print preview page consists of a left pane that allows for printer selection
and printer options and a right pane for displaying the preview and page
thumbnails.

This anti-exploitation policy controls the use of the print preview,
which can be potentially exploited.

If this is disabled, users will not see a preview of the page or
file.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Print Preview.
3. Select one of the following options:

   - **Allow** - Permit use of the Print Preview.
   - **Block** - Block use of the Preview.
4. Click Set.

   ![]()

###### Google Cloud Print

Mobile Browser - **No support**

Google Cloud Print is a discontinued Google service that allows users
to print from any Cloud Print-aware application (web, desktop, mobile) on any
device in the network cloud to any printer with native support for connecting to
Cloud Print services.

This anti-exploitation policy controls the use of the Google Cloud
Print API, which can be potentially exploited.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Google Cloud Print.
3. Select one of the following options:

   - **Allow** - Permit use of Google Cloud Print.
   - **Block** - Block use of Google Cloud Print.
4. Click Set.

   ![]()

###### QUIC Protocol

Mobile Browser - **No support**

QUIC (Quick UDP Internet Connections) is a new internet transport
protocol developed by Google. QUIC solves several application-layer issues
experienced by modern web applications while requiring little or no change from
application writers. QUIC is very similar to TCP+TLS+HTTP2 but implemented on
top of UDP.

This anti-exploitation policy controls the use of the QUIC protocol,
which can be potentially exploited.

**Note**: Disabling QUIC protocol may impact different websites using it in a
legitimate way.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select QUIC Protocol.
3. Select one of the following options:

   - **Allow** - Permit use of the QUIC Protocol
   - **Block** - Block use of the QUIC Protocol.
4. Click Set.

   ![]()

###### Web Clipboard API

Mobile Browser - **No support**

The Clipboard API empowers applications to handle clipboard commands
and engage in asynchronous reading from and writing to the system clipboard.
This control manages use of the Clipboard API which may be exploited.

When a user attempts to access a domain that is blocked, they will
receive an on-screen notification, and a Log event will be created.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Web Clipboard API.
3. Select one of the following options:

   - **Allow** - Permit the Web Clipboard API to access
     the clipboard.
   - **Block** - Block the Web Clipboard API from accessing the
     clipboard.
4. Click Set.

   ![]()

###### Local Fonts

Mobile Browser - **No support**

The Local Fonts provides access to the local fonts installed on the device which
may be exploited.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Local Fonts.
3. Select one of the following options:

   - **Allow** - Permit the Prisma Access Browser to
     access local fonts installed on the device.
   - **Block** - Block the Prisma Access Browser from accessing
     local fonts installed on the device.
4. Click Set.

   ![]()

###### Strict Origin Isolation

Mobile Browser - **No support**

Isolates every origin in its own agent-cluster, preventing scripts on one
sub-domain from interacting with another.

The Prisma Browser uses a security model called **agent clustering**,
which isolates each browser tab. When **Site Isolation** is enabled, the
browser places each unique origin into its own cluster (eTLD), improving
security by preventing cross-domain scripting. This change disables older
techniques like document.domain.

If Site Isolation is **disabled**, Prisma Browser allows pages with the
same eTLD+1 to share a cluster—supporting legacy features but weakening
security.

Enable Site Isolation
for stronger protection; use the legacy mode only when necessary for older
applications.

**eTLD**: The effective public suffix. The eTLD
of docs.google.com is google.com.

**eTLD+1**: The eTLD plus the next
suffix to the left. The eTLD+1 of google.com can be
mail.google.com.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Security
2. Select Strict Origin Isolation.
3. Select one of the following options:

   - **Enable** - Enabling stricter cross-origin isolation
     strengthens defenses against Spectre and XS-Leak attacks and is a
     necessary step for features like high-resolution
     SharedArrayBuffer. However, it may break legacy
     applications that rely on document.domain for
     cross-subdomain communication.
   - **Disable** - All pages that share the same eTLD+1 can still join
     one cluster. While this works for older, multi sub-domain apps, it
     provides more chance data leaks between sub-domains.
4. Click Set.

   ![]()

---

<a id="configure-prisma-browser-browser-customization-controls"></a>

#### Configure Prisma Browser Browser Customization Controls

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization>*

Configure browser customization controls for Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

When you're creating a browser customization rule, you can configure the controls in
the following ways:

- When you're creating a new browser customization rule, you can set the controls
  in the [Browser Customization
  page](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-customization-rules.html#task-tsj_k5t_fcc_step-browser-customization).
- You can [edit an existing rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules.html#manage-prisma-access-browser-policy-rules_task-edit-rules).
- When you [create a policy profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles.html#manage-prisma-access-browser-policy-profiles_task-jfp_rny_fcc), you
  can configure browser security to control user security settings in the Prisma Browser.
- You can select it from Strata Cloud Manager
  ConfigurationPrisma BrowserPolicyControlsBrowser Customization.

For information on a control, select the group where it is contained:

- [Browser Customization - Branding](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html)
- [Browser Customization –
  Autonomous Digital Experience Management (ADEM)](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-autonomous-digital-experience-management-adem.html)
- [Browser Customization - Customization](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-customization.html)
- [Browser Customization - Routing](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-routing.html)
- [Browser Customization – New Tab and Home Page](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-new-tab-and-home-page.html)
- [Browser Customization - Upgrade Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-upgrade-management.html)

---

<a id="configure-branding"></a>

##### Configure Branding

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding>*

PAB controls for Browser customization - Branding

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Theme Color

Mobile Browser - **Partial support**

The Prisma Browser allows users to modify the browser theme color.
You can choose to let users select their own favorite color if they desire.
Choose a specific color from a color palette, or enter colors based on the
following color codes:

- R G B
- H S L
- HEX

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Theme Color.
3. Select one of the following options:

   - **Users choose their own** - allows users to select
     their own color.
   - **Custom color** - allows you to set the color scheme.
4. Click Set.

   ![]()

###### Brand Color

Mobile Browser - **Partial support**

You can select a color that will be applied according to all user-facing browser
elements. This includes dialogs, block pages, and other elements.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Brand Color.
3. Select one of the following options:

   - **Default color** – Prisma Browser will use the
     default color for browser elements.
   - **Custom color** - You can select a custom color for browser
     elements.

     When selecting an accessible color,
     You should avoid indicative colors, such as red or green.

     For more information on accessible colors, refer to [WebAIM](https://webaim.org/resources/contrastchecker/).
4. Click Set.

   ![]()

###### Company Logo

Mobile Browser - **Full support**

The Prisma Browser allows you to select your own logo to increase
branding awareness. The logo appears on the homepage, in messages sent to the
users, and in the Browser Control Pane.

You can add a company logo, or no logo to leave the default Prisma Browser Logo.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Company Logo.
3. Select one of the following options:

   - **No Company Logo** - The default Prisma Browser
     logo will be displayed.
   - **Set Company Logo**- Drag the logo image or browse
     for it.

     The logo image must conform to the following
     requirements.

     - File format - PNG or SVG only
     - Recommended width - 600 px
     - File size - up to 1 MB
     - The logo should be transparent (no background).
4. Click Set.
5. The logo will now be displayed on the homepage and all places where the
   logo is used.

   ![]()

###### Company Name

Mobile Browser - **Full support**

You can use the Company Name feature to add the organization's name to the top
line of the browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Company Name.
3. Select one of the following options:

   - **Set name** - Enter the name that is to be
     displayed on the top of the homepage. It will appear as The
     **<company name> browser - Powered by Palo Alto
     Networks**.
   - **Display no name** - the display will show -
     **Secure Browser - Powered by Palo Alto Networks**.
4. Click Set.
5. The name will now be displayed on the homepage and elsewhere.

   ![]()

###### Custom Texts

Mobile Browser - **No support**

You can modify the default texts that appear in user-facing dialogs and
other pages. This can help describe additional information regarding policies -
for example - why a particular policy isn't allowed, and if there is anything
that can be done to allow for special permission.

This feature can also be used for localizing the information if
required.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Custom Texts.
3. Select one of the following options:

   - **Use default dialog text** - the dialog texts will
     be the default, preconfigured texts.
   - **Customize and edit dialog texts** - Select the
     dialog that you want to edit, and click the pencil icon. In the
     **Edit Text** window, edit the **Title** and
     **Description**. If needed, add new line characters to
     provide some formatting.

     There are three tabs for this option:
     - **Dialog texts -** Customize the text in the various
       dialogs.
     - **Security texts -**Customize the text in the
       security dialogs.
     - **Other -**  Customize the link and title in the PABX
       **About** section.

       The **Other** tab is limited to the
       PABX.
   - **Add link** - Enter the information for the Link name (up to
     30 characters), and add the URL.
4. Save.
5. Repeat and edit or customize as many additional dialogs as needed.
6. Click Save when all dialogs are modified.

   ![]()

   ![]()

   ![]()

###### Browser Icon

Mobile Browser - **No support**

This feature is
only available on macOS.

Organizations that use the Prisma Browser can use their own internally
designed icon if they so desire. If not, you can make sure that only the default
Prisma Browser icon is used.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Browser Icon.
3. Select one of the following options:

   - **Use Prisma Browser icon** - The Prisma Browser will use the default icon.
   - **Set browser icon** - You can select a custom icon.
4. Click Set.

   ![]()

---

<a id="configure-autonomous-digital-experience-management-adem"></a>

##### Configure Autonomous Digital Experience Management (ADEM)

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-autonomous-digital-experience-management-adem>*

Adem configuration for PAB

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Real User Monitoring (RUM)

This feature controls the ability to install or uninstall the ADEM plugin.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser PolicyControlsBrowser Customization
2. Select Autonomous Digital Experience
   Management.
3. Select one of the following options:

   - **Activate** - Allow the ADEM plugin to install.
   - **Deactivate** - Allow the ADEM plugin to uninstall.
4. Click Set.

   ![]()

---

<a id="configure-customization"></a>

##### Configure Customization

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-customization>*

PAB Customization controls and policies

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Incognito

Mobile Browser - **Full support**

This feature allows you to control whether or not the Prisma Browser can be
opened in Incognito mode. A user in Incognito mode is anonymized from the Web
only. Admin visibility and Browser Policies are not affected by this feature.
You can set Access & Data Control rules to allow access to personal websites
without logging.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Incognito.
3. Select one of the following options:

   - **Allow** - Permit use of Incognito mode in Prisma Browser.
   - **Block** - Block use of Incognito mode in The Prisma Browser.
   - **Force** - Force use of Incognito mode in the Prisma Browser.
4. Click Set.

   ![]()

###### Extension Force Install

Mobile Browser - **No support**

This feature allows you to configure specific extensions that are to be installed
automatically in the Prisma Browser.

If there
are multiple rules that have the Extension Force Install control applied,
**all** the applicable extensions will be installed.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Extension Force Install.
3. Click **Add Extension**. 

   ![]()
4. Select the Store that is the source of the extension. The options are:

   - **Chrome Web Store**.
   - **Custom URL**. Enter the URL.
5. Select whether the extension will be **pinned to the toolbar** for the
   end users.
6. Select whether the extension will be **automatically installed in
   Incognito mode**.
7. If applicable, enter the **Custom Configuration**.

   The system supports JSON format. Custom
   configuration depends on your extension vendor; contact your vendor or
   support partner for assistance.
8. Click Add.

   ![]()

###### User-Agent

Mobile Browser - **Full support**

The User-Agent feature allows you to add additional Agent components to the
default User-Agent string to identify the Prisma Browser HTTP/S requests.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select User-Agent .
3. Select one of the following options:

   - **Use default User-Agent** - Use the default
     User-Agent string when identifying requests from the Prisma Browser. This is the same as the Chrome User-Agent
   - **Set an additional User-Agent component** - Configure an
     additional User-Agent for the Prisma Browser by entering the
     component name in the appropriate field.
   - **User-Agent desktop mode** - Allows you to ensure that
     applications that do not function properly in mobile browsers
     open in desktop mode.
4. Click Set.

   ![]()

###### Custom HTTP Header

Mobile Browser - **No support**

Custom HTTP headers let the browser pass additional information along with HTTP/S
requests. An HTTP header consists of its case-insensitive name followed by a
colon (:), then by its value.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Custom HTTP Header.
3. Select one of the following options:

   - **Keep default header** - Use the default setting,
     without any custom HTTP headers.
   - **Add a custom header** - Configure a custom HTTP header that
     will identify the Prisma Browser HTTP/S requests.

     - **Custom Header Name** - Add a name to identify the
       custom header.
     - **Custom Header Value** - Add a custom value for the
       header.
4. Click Set.

   ![]()

###### Profile Sync

Mobile Browser - **Full support**

Linux/IGEL Browser - **No support**

In some organizations, employees use the Prisma Browser on multiple
devices. This feature enables you to synchronize profiles across all Prisma Browser installations on different devices.

You have the option of customizing the browser settings to sync
everything - all information that is associated with the user - or selecting
specific information that will be included in the sync.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Profile Sync.
3. Select one of the following options:

   - **Enable**- Allow a Profile Sync. You can select the
     following sync options:

     - **Sync everything** - Select all the
       information that can be synchronized.
     - **Customize sync** - Select the components
       that will be synchronized across multiple devices.
   - **Disable** - Don't perform profile sync.
4. Click Set.

   ![]()

###### Default Browser

Mobile Browser - **Full support**

Linux/IGEL Browser - **No support**

This feature allows you to control whether Prisma Browser will be the default
browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Default Browser.
3. Select one of the following options:

   - **Suggest user** - Suggest that users select the Prisma Browser.
   - **Don't suggest user** - don't suggest using the Prisma Browser.
4. Click Set.

   ![]()

###### **Onboarding Wizard**

Mobile Browser - **No support**

This feature allows you to configure the Onboarding Wizard that is displayed to
all new Prisma Browser users when they install the browser. The wizard
assists end users in installing and configuring the Prisma Access Browser, and
at the same time - displays a brief tutorial of some of the more popular
features.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Onboarding Wizard.
3. Select one of the following options:

   - **Enabled** - the Onboarding Wizard will be enabled
     for use. You will be able to select the steps that will be made
     available to the users.

     By default, all steps are enabled.

     1. **Step 1: Welcome and language selection
        (Editable)** allows you to select either the
        default welcome message or create a custom message for
        your users. The custom content allows 160 characters for
        a title and 320 characters as the message.
     2. In **Step 2: Customize**, users can add
        their picture. If you did not configure the [Brand
        Color](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-rtz_jcr_hcc), users will be able to configure their
        own preferred color. If the Brand Color was configured,
        the color option won't be displayed.
     3. **Step 3: Import** allows users to import
        their existing resources including:

        - Browsing History
        - Favorites / Bookmarks
        - Saved Passwords
        - Cookies
        - Extensions
        - Extension Data
        - Tabs and Tab Groups
     4. **Step 4: Labels & Policy indicator**
        provides a brief description on how users can benefit
        from the displayed labels.
     5. **Step 5: Popup extensions &
        Notifications** encourages users to use the Prisma Browser icon to help manage their account.
     6. **Step 6: Restrictions** describes to users
        the way that Prisma Browser uses the restrictions in
        the browser.
     7. **Step 7: Mobile & Sync** informs users
        that the mobile application is a seamless extension of
        the desktop browser.
     8. **Step 8: Feedback** invites users to send
        their comments and suggestions.
   - **Disabled** - the Onboarding Wizard won't be enabled.
4. Click Set.

   ![]()

###### Search Engine Content Filtering

Mobile Browser - **Full support**

When you enable the Safe Search feature, you extend the URL filtering to include
the selected search engines. .

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Search Engine Content Filtering.
3. Select one of the following options:

   - **Enable**-Enable the feature. You also need to select
     at least one of the available search engines to be used for safe
     search.
   - **Disable**- Disable the feature.
4. Click Set.

   ![]()

###### Microsoft Auto-SSO (Windows only)

Mobile Browser - **No support**

This feature enables automatic web-application user sign-in for Microsoft Entra
ID accounts, based on the device signed-in account.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Microsoft Auto-SSO.
3. Select one of the following options:

   - **Enable** - Enable the automatic user sign-in for Microsoft
     Entra accounts.
   - **Disable** - Disable the Microsoft auto-sso feature.

   It is strongly recommended that this feature be
   limited to managed devices only.
4. Click **Set**.

   ![]()

###### Automatic Client Certificate Selection

Mobile Browser - **No support**

This control allows you to configure matching client certificates for specified
URLs to facilitate seamless authentication. When you configure this control, it
acts as an override to any lower priority rule definitions.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select **Automatic Client Certificate Selection**.
3. Select one of the following options:

   - **Enable:** Allows you to bypass manual certificate selection.
     Specified URLs will operate seamlessly. Enter the following
     information in the **Certificate criteria for specific URLs section**
     1. Enter A URL pattern that will use the certificate. Click
        here for more information about the[URL pattern
        syntax](https://chromeenterprise.google/policies/url-patterns/).
     2. From the drop-down list, select a **criteria** for the
        certificate.
     3. Enter the name of the certificate's **issuer
        organization**.
        - You can add multiple criteria and issuer
          organization for each URL.
        - Additionally, you can add as many URLs as needed.
   - **Disable:** Users will be required to manually choose the
     certificate they need when browsing the URL
4. Click **Set**.

   If you enable Google Workspace
   Integration, Automatic Client Certificate Selection for Google URLs may
   not function properly.

   ![]()

###### History Collection

This Policy only supports **Prisma Browser
Extension.**

This feature allows you to create a History Collection that allows you to
identify browsing trends and behavior patterns of your users.

You need to be aware of the following limitations
regarding this feature:

- The information is collected from Prisma Access Browser Extension
  users **only**.
- The historical information will be collected beginning up to 30 days
  before the installation.
- The Scope of a rule containing History Collection is **50**
  users.

For more information, refer to [Prisma Browser Extension History Collection](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-access-browser-extension-history-collection.html)

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select History Collection.

   If you do not see the History Collection, make
   sure that the Browser Extension controls are visible.
3. Select one of the following options:

   - **Enable** - Enable the History Collection.
   - **Disable** - Disable the History Collection.
4. Click **Set.**

   ![]()

###### On Browser Startup

Mobile Browser - **No support**

This feature allows you to control the Prisma Browser's "On-Startup"
routine.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select On Browser Startup.
3. Select one of the following options:

   - **Configured by the user**  - Users will be able to determine
     exactly how the browser will open.
   - **Restore the Last Session (Continue where the user left
     off** - Restore the last set of browser tabs, allowing the
     users to continue working.
   - **Restore the last session and open a list of URLs** - Allows
     the user to reopen the last set of browser tabs. This option
     will also open an additional list of (predefined) apps. When you
     select this field, you will be able to add additional web pages
     to open.
   - **Open a New Tab Page** - Opens a generic new tab page.
   - **Web pages to open on startup** - Enter a list of web pages
     that will open on startup.
4. Click **Set**.

   ![]()

###### Default Search Provider

Mobile Browser - **Full support**

This feature allows you to set up the way the browser search engine works.
This feature allows you to either configure a search engine, allow your
users to select their preferred browser, or disable searching entirely on
the Prisma Browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Default Search Provider.
3. Select one of the following options:

   - **Enable** - You can select the search provider that will
     serve as the default for all users. To configure default search
     engine, provide the following information:
     - **Search Provider** - Select a search provider from
       the list. You can also select a customized provider. If
       you use a custom provider, enter a **Search Provider
       Name**, and the **url** for the engine.
   - **Disable** - Do not allow searching.
   - **User Choice** - Allow users t select their own search
     provider .
4. Click **Set**.

   ![]()

###### Auto-Launch External Applications

Support for Prisma Browser Extension only.

The Prisma Browser Extension
provides an auto-login feature that offers users a seamless and automatic
sign-in experience, eliminating the need for manual authentication. The feature
is available only when you integrate it with the following Identity Providers
(IdP):

- Okta
- Azure Active Directory
- Google Workspace

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Auto-Launch External Applications.
3. Select one of the following options:

   - **Allow** - Permit the use of Auto-Launch External
     Applications.
     - **Protocol** - Enter the protocol in the proper
       format. The format is displayed on the control.
     - **Add Origin** - Enter the Origin patterns for the
       protocol. The format is displayed on the top of the
       page.
   - **Block** - Do not allow Auto-Launching External
     Applications.
4. Click **Set**. 

   ![]()

###### Desktop Sharing

Mobile Browser - **No
support**

When this feature is enabled, users will be granted
the ability to share their screens when they are using the sharing tools from
within a browser.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Desktop Sharing.
3. Select one of the following options:

   - **Allow** - Allows you to enable end-users to share their
     desktop screens or desktop applications.
   - **Block** - Block end-users from sharing their desktop
     screens or desktop applications.
4. Click **Set**.

   ![]()

###### Built-in DNS Client

Mobile Browser - **No
support**

Choose whether DNS is resolved in the Prisma Browser built-in client, or by the operating system.

For more information, refer
to [BuiltInDnsClientEnabled on the Chrome
Enterprise site.](https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled)

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Built-in DNS Client.
3. Select one of the following options:

   - **Always use the built-in DNS client.**
   - **Never use the built-in DNS client.**
4. Click **Set**.

   ![]()

###### Page Translation (Google Translate)

Mobile Browser - **No
support**

This control allows you to manage the Google
Translation banner on foreign-language pages.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Page Translation (Google
   Translate).
3. Select one of the following options:

   - **Always offer translation.**
   - **Never offer translation.**
   - **Allow the user to decide.**
4. Click **Set**.

   ![]()

###### Search Suggestions

Mobile Browser - **No support**

Implement a dynamic real-time prediction feature within the address bar,
displaying relevant search suggestions and direct navigation links as the
user inputs their query. This functionality is designed to significantly
enhance the user experience by reducing the number of keystrokes required,
accelerating search and navigation, and proactively guiding the user to the
most pertinent results or destinations as quickly and efficiently as
possible.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Search Suggestions.
3. Select one of the following options:

   - **Enabled** - The browser will always offer search
     suggestions.
   - **Disabled** - The browser will not offer search suggestions.
   - **Allow the user to decide** - Users will decide whether or
     not to enable this feature. This is the default.
4. Click **Set**.

   ![]()

---

<a id="configure-routing"></a>

##### Configure Routing

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-routing>*

PAB Customization Routing controls

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Proxy Auto-Configuration (PAC)File

Mobile Browser - **No support**

This feature allows you to configure the Prisma Browser to use a Proxy
Auto-Configuration (PAC) file to pass some of the web traffic through a proxy or
gateway. This feature overrides the system PAC file.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Proxy Auto-Configuration (PAC) File.
3. Select one of the following options:

   - **Set PAC File** - Configure the Prisma Browser
     to use a PAC file.
   - **No PAC File** - Do not require a PAC file.
4. Click Set.

   ![]()

###### Traffic Flow

Mobile Browser - **Partial support**

The Traffic Flow control allows you to manage the way that the Prisma Access
Browser handles network traffic.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Traffic Flow.
3. Select one of the following options:

   - **Only route private application traffic through
     Prisma Access.**
   - **Route all traffic through Prisma Access.** 

     Mobile Devices: To ensure an optimal
     experience with Network Detection and Prisma Access, either
     route only Private App traffic, or exclude the Mobile Device
     group from routing.
   - **Do not route traffic through Prisma Access**
4. Click Set.

   ![]()

###### Internal Network Detection

Mobile Browser - **No support**

This feature allows you to configure internal network detection to ensure that
traffic is routed in an optimal way

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Internal Network Detection.
3. Click **Add Extension**.
4. Select one of the following options:

   - Enable - Enable Internal Network Detection.
     Select and configure the methods.
     - **Internal Host Detection** - Identify the internal
       network by establishing a connection with a host that is
       only available inside the network. Enter the following
       information:
       - FQDN to resolve
       - Expected IP addresses
     - **Agent detection** - Identify the internal network by
       detecting whether the Global Protect or the Prisma Access
       agent is running on the device.
   - Disable - Disable Internal Network Detection.
5. Click Set.

   ![]()

---

<a id="configure-new-tab-and-home-page"></a>

##### Configure New Tab and Home Page

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-new-tab-and-home-page>*

New tab and home page configuration

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Browser Customization – New Tab and Home Page

###### New Tab Page

Mobile Browser - **Full support**

This feature allows you to set the type of page that is displayed whenever a
user opens the Prisma Browser or a new tab. This will help you create a
unified look and feel across company resources.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select New Tab Page.
3. Select one of the following options:

   - **Prisma Browser New Tab** - Use the default
     page that is included with the browser when it installs.
   - **Custom URL**- Enter the URL of the selected new tab in
     the format

     https://www.example.com.

   ![]()
4. Click Set.

###### Home Page

Mobile Browser - **Full support**

This feature allows you to set a default homepage for the browser. This page
will appear whenever a user opens the Prisma Browser home page. This
will help you create a unified look and feel across company resources.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Home Page.
3. Select one of the following options:

   - **Configured by user** - Allow the users to
     select their own home page.
   - **Prisma Browser New Tab Page** - Use the
     default homepage that is included with the browser when it
     installs.
   - **Custom URL**- Enter the URL of the selected homepage in
     the format

     https://www.example.com.
4. Optionally, select the option to **Show home button on toolbar**.

   ![]()
5. Click Set.

###### Managed Shortcuts

Mobile Browser - **Full support**

To improve the efficiency for the users, the Prisma Browser
allows you to configure applications and URLs that will appear on the
homepage. In most cases, these will be applications that will be the ones
most commonly needed by users in their day-to-day routine. You have the
ability to enter a specific URL, a name, and a customized icon, if
desired.

These links will also appear on the browser bookmark under **Company
Shortcuts**.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Managed Shortcuts.
3. Select one of the following options:

   - **No Shortcuts** - Do not include any managed
     shortcuts on the homepage.
   - **Set Shortcuts** - Click Add shortcut to add
     managed shortcuts to the homepage.

     1. Enter the URL.
     2. Enter a Name for the shortcut.
     3. Optionally select an icon for the shortcut. If no
        icon is selected, the website’s Favicon will be
        used.
4. Click Set.

   ![]()

###### Background Image

Mobile Browser - **Partial support**

This feature allows you to select a custom background image for the Prisma
Access Browser homepage.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Background Image.
3. Select one of the following options:

   - **Default background** - Use the default
     background image that is included with the browser when it
     installs.
   - **Dark background** - Use a dark background
     image.
   - **Light background** - Use a light background image.

     The light background is not
     supported in the Prisma Browser for Mobile.
4. If you do not want to use a background image, select **No Background
   Image**.
5. **Set Background image**- Drag and Drop the Enter the URL of the
   selected homepage in the format.

   1. Select a file to use as the background image. The
      image should best conform to the following guidelines:

      - File format - PNG or JPEG.
      - Image size 2560 px wide x 1440 px height.
      - Maximum file size - 3 MB
6. If you want to see how the Background image will be displayed on
   different devices, click the appropriate device in the **Image
   preview** section..
7. You can either use the default filter option, or select a custom
   filter.
8. Select the checkbox if you want to use the Color White Logo option.
   This will make the logo stand out on the homepage.
9. Click Set.

   ![]()

###### Admin Messages

Mobile Browser - **No support**

In many organizations, there is a challenge getting a message to all
employees. The Prisma Browser offers a system for displaying messages on
the homepage. The messages are displayed in a carousel - type display.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Admin Messages.
3. Select one of the following options:

   - **No admin messages** - Do not display admin
     messages.
   - **Set admin message**- Click **Add Admin
     Message** and enter the following information:

     - Select a **Title** for the message.
     - Enter the **Message** text. The message
       size is limited to 1000 characters, and can also
       include links.
     - **Add Link** - Optionally, add a link that will
       display on top of the message
     - Click **Add**.
4. On the main page, click **Set**. The message will be displayed on
   the homepage.

   ![]()

###### Custom Notice

Mobile Browser - **Full support**

Only Prisma Browser for Mobile supports this feature.

Similar to Admin messages, this control allows you to send a message to all
users who are using the Prisma Browser for Mobile.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select Custom Notice.
3. Select one of the following options:

   - **Show notice** - Display a custom notice for
     Prisma Browser for Mobile users.

     - Select the frequency of the notice, ranging
       from **Only once** to **Every 30 days**. The
       default is **Every 7 days**.

       **Note:** If you uninstall and reinstall
       the browser, the frequency count restarts.
     - Enter a **Title** for the message.
     - Enter a **Description** for the message.
       The message is limited to 360 characters.
   - **Don’t Show Notice** - Do not display a custom message to
     Prisma Browser for Mobile users.
   - **Set admin message**- Click **Add Admin
     Message** and enter the following information:
4. Click Set.

   ![]()

---

<a id="configure-upgrade-management"></a>

##### Configure Upgrade Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-upgrade-management>*

PAB Browser Customization Upgrade Management

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

###### Deployment Upgrade

Mobile Browser - **Partial support**

Linux/IGEL Browser - **No support**

In the ever-changing world of cybersecurity, it is essential that the
Prisma Browser be kept up to date, as updates and upgrades are added
regularly. Upgrades are released weekly.

Some organizations manage their upgrades using
offline installers. For more information, please see The Prisma Browser
Offline MSI Installer.

When an update is available, a button will be displayed on the browser.
A user can click the button or restart the browser to update the Prisma Browser. You can configure a Grace Period to allow end users some
time to finish a task before running an upgrade. See below for more
information.

- You can select the version to be installed by configuring the registry
  key (Windows).
- There is no option to downgrade the browser.
- Customers using offline installers won't be affected by
  this control.

Prisma Browser for Mobile are automatically locked
out after 90 days if their browser is not updated. Users receive updated
application versions for both Android and iOS through the respective
operating systems. The specific timing of these updates is governed by each
user's individual app upgrade settings.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyControlsBrowser Customization
2. Select .

   **Deployment Upgrade**
3. Select one of the following options:

   - **Default channel** - The browser will be upgraded to
     the latest version when it is available. This is the default
     behavior.
     - **Delay options** - You can decide to delay the actual
       deployment for up to 7 days. This is based on the settings
       for the flag. Contact Support for more information.
   - **Long-term Support channel** - This channel allows you to keep
     your users on a major release, but receive weekly security patches
     without new features. The new features will be available to your
     users in the next LTS major update. Bug fixes and security updates
     will be available on a weekly basis. You also have the ability to
     delay these patches.
     - **Delay options** - You can choose to delay the next
       major version for up to one month. If you select this
       deployment option, you will not get any bug fixes or
       security patches that are normally released on a weekly
       basis.
     - **Security and Bug patches** - You can choose to delay
       the deployment of the security and bug patches for up to 3
       days. In the *rare* case when there is an
       exploit-in-the-wild, you can click **Expedite critical
       security updates**, and the delay will be ignored.
   - **Pinned version** - The browser will upgrade to the selected
     version. You can select a pinned version for Windows, and a version
     for macOS. You decide which versions become the pinned version.

     When the pinned version reaches its
     end-of-life (usually after one month), the pinned version will
     be reset to a version released within the past 7 days.
   - **No auto-updates** - As the administrator, you will
     be responsible for managing the upgrade deployments manually.
     There will be no automatic updates.

     If you select this option, your environment
     might be exposed to security vulnerabilities and
     compatibility issues.
4. **Update grace period** - Allow your users to defer the forced upgrade
   relaunch by the selected amount of time.
5. Click **Set**.

   ![]()

---

<a id="new-tab-page"></a>

#### New Tab Page

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/new-tab-page>*

A description of the new tab page.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

The New Tab Page serves as a central point for users during their daily browser usage.
This document outlines the structural components of the page, user-facing customizations
and administrative configurations.

![]()

##### New Tab Page Components

**Search and Web Navigation Omnibox**

The central search bar allows users to perform web searches or navigate directly to
URLs.

This component adheres to the Default Search Provider control.

**User Customizable Shortcuts**

![]()

The shortcut grid is customizable, allowing users to select which types of
links are displayed through the Customization menu.

Available display options include:

- **Administrator-Pinned Applications:** A selection of up to 16
  essential tools curated by the organization to guarantee consistent access
  for all users.

  - *(Refer to the* ***Managed Shortcuts Control
    Documentation*** *for instructions on pinning these
    applications).*
- **User-Defined Shortcuts:** A personalized collection of up to 8
  links manually managed by the individual user.
- **Frequent Sites:** Dynamically generated links to the user's
  most-visited websites based on their browsing history.

The grid supports a maximum of 16 shortcuts. When both organizational and
user-managed shortcuts are enabled, the organizational pins take precedence. Any
remaining slots in the 16-slot grid are filled by the user's curated shortcuts and
frequent sites.

**Admin Messages** 

![]()

The New Tab Page serves as a central hub for distributing
organizational updates and administrative notifications.

- **Prominent Visibility:** Alerts are presented as clear
  badges or banners to capture user attention.
- **Mandatory Engagement:** Critical updates remain
  persistent until the user opens the message, ensuring essential
  information is acknowledged.

Settings for these broadcasts are located within *Browser Customization
-> New Tab page -> Admin messages* (refer to the control
documentation).

**Customization Button**

This feature is located at the lower right corner of the Focus area. When clicked,
this feature allows users to configure appearance, toolbar settings, and shortcut
settingl

##### Company Application Section

![]()

The Company Applications section eliminates the need to bookmark dozens of internal
tools. Users can seamlessly transition to this view by **scrolling down** from
the top section or by clicking the **"Company Apps"** button. This ensures that
even the most complex application portfolios are just a click or a scroll away. A
dedicated search filter allows users to find applications by name.

###### Sections

**Company shortcuts:** Shortcuts configured using the *Managed Shortcuts
Control*.

**Identity Synced Shortcuts:** Applications assigned to users based on their
IDP profile. Can be configured in *Browser Customization -> New Tab page
->**Identity Provider Synced Shortcuts Control.*

Private Applications

Desktop Applications

Remote Connections

**Private Applications:** Desktop Applications and Remote connections will
automatically appear in the company applications section for users who have
access to them.

---

<a id="manage-prisma-browser-sign-in-rules"></a>

### Manage Prisma Browser Sign-in Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-sign-in-rules>*

Learn how to create browser sign-in rules as a first level of securing your Prisma Browser deployment.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Use sign-in rules to determine which users and devices have access to Prisma Browser. The Sign-in rules page displays information about existing
sign-in rules:

To view the rules:

The last rule on the
list is the **Default rule**.

The Default rule is the policy rule that is used
when no other policy rule is applicable. Since this rule must be available for
any given user or device, only certain controls can be edited.

- **Priority**—The priority order for rule enforcement.
- **Mode**—Indicates whether the rule is active or disabled.
- **Name**—Identifies and describes the rule.
- **Users**—The users and user groups associated the each rule.
- **Device groups**—The device group associated the each rule.
- **Network & Location**—The specific networks and geolocations associated
  with the rule.
- **Action**—The action Prisma Browser takes for users and devices matching
  the rule: Allow, Block, or
  Prompt the user.
- **Updated**—Last updated date for the rule; hover to see the full
  timestamp.

![]()

When you create a sign-in rule, you define the scope of the rule. When a user
attempts to access Prisma Browser, the browser compares the scope of the rules
in order until it finds a rule match for the user or device or network or
geolocation, and then it enforces the corresponding access rule. In some cases, you
may want the sign-in rules you define to block Prisma Browser if they match the
scope of the rule. For example, suppose the scope of the rule is set to match a
device group for devices with a specific OS and you don’t want to allow access to
devices that are still running that OS. In that case, you would set the sign-in rule
to block access for users who match to it. In other cases, you might want to allow
users who match the sign-in rule access to Prisma Browser. For example, suppose
the scope of the rule allows users in a specific user group and in a device group
that only allows devices running a specific OS version, a specific client
certificate, and has active endpoint protection. In this case, you might want the
matching sign-in rule to allow access to Prisma Browser. The way you create your
user groups and device groups (including the corresponding device posture rules you
enforce at the device group level) informs how you will want to create your sign-in
rules.

When a user attempts to access the browser, Prisma Browser
evaluates the sign-in rules in top-down order until it finds a match for the user
and device and then it enforces the corresponding sign-in rule. If the user or
device don’t match any of the defined sign-in rules, Prisma Browser enforces the
Default sign-in rule allow rule.

There are two
ways to create sign-in rules: one for managed devices and one for unmanaged devices,
as described in the following sections.

#### Create a Sign-in Rule

To create a sign in rule for users:

1. Select ConfigurationPrisma BrowserPolicySign-in Rules and click Add rule.
2. Enter a Name for the rule.
3. Set an Action, which can be
   Active or Disabled.

   You can change the Action at any time. You may want
   to keep the rule disabled until you're ready to launch the new rule
   base.
4. Click Next: Scope and then define the match criteria
   for the rule.

   Select one or more values to define the scope of the sign-in rule. You
   can select one or more of the following options:

   - Users/User groups—Select the [users and user groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-users.html) that
     you want to match this sign-in rule to access Prisma Browser.
   - Device groups—Select the [device groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices.html#manage-prisma-access-browser-devices_task-hns_lt1_gcc) to
     match this sign-in rule for access to .. The
     device groups can contain posture attributes that are either
     positive or negative. For more information, refer to [Device Posture
     Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-device-posture-attributes.html).
   - Networks—Select the public networks the
     device must be attached to in order to access Prisma Browser.
     Use one of the following formats to specify the network:
     94.45.21.1 or
     129.144.9.8/29
   - **Location** – Select the geolocation from which to
     enable the Prisma Browser rule. If the OS Location services
     are not enabled on the device, the PAB will use the GeoIP. For
     more information, refer to [Location-based Policy](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/location-based-policy.html)

   ![]()
5. Click Next: Action.
6. Set the action for the sign-in rule:

   - Allow—Allow access to Prisma Browser for
     users and devices that match the defined rule scope.
   - Block—Block access to Prisma Browser for
     users and devices that match the defined rule scope.
   - Prompt—Notify users that match the sign-in
     rule scope that their Prisma Browser is blocked by default, but
     allow them to bypass the block and continue to the browser.

     While the Prisma Browser for Mobile's
     Sign-in rules are configured the same way as the Sign-in rules
     for the Prisma Browser, be aware of the following
     exception:Starting with *iOS* browser version 1.4259 and
     *Android* browser version 1.4260, the **Prompt**action functions as **Block**. For all earlier versions,
     it functions as **Allow**.

   ![]()
7. Optional) [Create a browser customization rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-customization-rules.html)
   for the device group.

   Provide text in the customization rule to help the user understand the
   posture errors (on the Security checks tab).

   ![]()
8. Save the rule.

---

<a id="manage-prisma-browser-requests-to-bypass-policy-rules"></a>

### Manage Prisma Browser Requests to Bypass Policy Rules

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-requests>*

Learn how to manage end user requests to bypass Prisma Browser rules for access
to otherwise blocked sites and apps.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

In some cases, end users may find that the Prisma Browser rules are too strict to
allow users to access the resources they need. For example, a user might need to
download a file that is restricted based on a browser rule, or may need access to a
website that is normally off limits.

To address this issue, Prisma Browser allows you to set up temporarily bypass
rules conditions. For each supported control, you can configure a policy that allows
your users to bypass the rule.

There are three ways to allow users to bypass the rules:

- **Warn and allow to proceed anyway**—Notifies users that the web
  application they are trying to access is restricted, but allow them to
  proceed anyway.
- **Warn and allow the user to proceed anyway with a reason**—Notifies
  users that the web application they are trying to access is restricted, but
  allows them to proceed after supplying a reason they need access.
- **Permission request**—Notify users that the web application they are
  trying to access is restricted, and prompt them to submit a request for
  access. In this case, you must review and approve the request before the
  user can access the app.

The following controls allow you to set up a rule bypass:

- Web Access
- Login Control
- File Download
- File Upload
- Screenshot
- Print
- Typing Guard

You can also set the bypass window to allow users to bypass the restrictions for a
specified amount of time.

You can examine the Event Logs
to see controls that may be too restrictive and tune them up so that they are
more useful.

![]()

#### How are bypass requests configured in policy?

You [define
the bypass conditions within the policy rules](#manage-prisma-access-browser-requests_task-xgg_w5y_fcc). Then, when users
attempt to perform an action or visit a site blocked by the corresponding rule,
they can submit a bypass request. Bypass requests are an extension of
Prompt actions where Prisma Browser prompts the
user with a message indicating that the action or site is blocked and allowing
them to continue anyway. To set bypass conditions, you configure the prompt
action to enable permission requests. With bypass conditions you must [review and
approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before Prisma Browser allows the user to
perform the blocked action or access the blocked site.

<a id="manage-prisma-access-browser-requests_task-xgg_w5y_fcc"></a>

#### Configure the Bypass Conditions

Configure the conditions for bypass rules when you [create or edit an Access and Data
Control rule](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html). The way you configure the conditions depends on the
type of user activity for which you want to allow bypass.

#### Set Bypass Conditions for Web Access Rules

![]()

1. In the Policy Rules - Edit ruleWeb access page, select Prompt.
2. Define the bypass conditions for the web access rule by selecting one of
   the following options:

   - Warn and allow to proceed anyway—notifies
     users that the web application they are trying to access is
     restricted, but allow them to proceed anyway. You will receive an
     event.
   - Warn and allow the user to proceed anyway with a
     reason—notifies users that the web application they
     are trying to access is restricted, but allow them to proceed after
     supplying a reason they need access. You will receive an event.
   - Permission request—notify users that the web
     application they are trying to access is restricted, and prompt them
     to submit a request for access. In this case, you must [review and approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can
     access the app.

#### Set Bypass Conditions for Login Controls

The Login restriction section in Access & Data Control rules enables you to
restrict login to specific email domains.

![]()

1. In the **Policy Rules - Edit rule→Login controls** page, select
   **Prompt**.
2. Define the bypass conditions for the login restriction rule by selecting
   one of the following options:
   1. **Allow** - Allow all domains.
   2. **Block** - Block all domains.
   3. **Allow specific email domains** - Allows access only to the
      domains you specify.
   4. **Block specific email domains** - Blocks access only to the
      domains you specify.
3. Specify the email domains that this rule governs.
4. Select **Prompt when the login is blocked** - With this setting enabled,
   when users attempt to login using a restricted email, Prisma Browser
   notifies them. You can set the following bypass conditions:
   1. Warn and allow to proceed anyway—notifies
      users that the web application they are trying to access is
      restricted, but allow them to proceed anyway. You will receive an
      event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that the web application they
      are trying to access is restricted, but allow them to proceed after
      supplying a reason they need access. You will receive an event.
   3. Permission request—notify users that the web
      application they are trying to access is restricted, and prompt them
      to submit a request for access. In this case, you must [review and approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can
      access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single download.

#### Set Bypass Conditions for File Download

The File Download profile in [Access & Data Control rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html) allows
you to restrict file downloads. This option is available from either the
Profiles or from the Data controls, but we recommend using the Data controls to
manage policies

![]()

1. In the **Policy Rules - Edit rule-Data controls** page, select **File
   Download**.
2. Select either **Allow** or **Allow (Protected)**.
3. Click **Prompt Before download** and select **Before
   download**.
4. Select **Popup notification** and define the bypass conditions for file
   downloads by selecting one of the following options.:
   1. Warn and allow to proceed anyway—notifies
      users that the web application they are trying to access is
      restricted, but allow them to proceed anyway. You will receive an
      event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that the web application they
      are trying to access is restricted, but allow them to proceed after
      supplying a reason they need access. You will receive an event.
   3. Permission request—notify users that the web
      application they are trying to access is restricted, and prompt them
      to submit a request for access. In this case, you must [review and approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can
      access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single download.

#### Set Bypass Conditions for File Upload

The File Upload profile in [Access & Data Control rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html) allows
you to restrict file uploads. This option is available from either the Profiles
or from the Data controls, but we recommend using the Data controls to manage
policies.

![]()

1. In the **Policy Rules - Edit rule-Data controls** page, select **File
   Upload**.
2. Select either **Allow** or **Allow (Protected)**.
3. Click **Prompt Before upload** and select **Before upload**.
4. Select **Popup notification** and define the bypass conditions for file
   upload by selecting one of the following options.:
   1. Warn and allow to proceed anyway—notifies
      users that the web application they are trying to access is
      restricted, but allow them to proceed anyway. You will receive an
      event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that the web application they
      are trying to access is restricted, but allow them to proceed after
      supplying a reason they need access. You will receive an event.
   3. Permission request—notify users that the web
      application they are trying to access is restricted, and prompt them
      to submit a request for access. In this case, you must [review and approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can
      access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single upload.

#### Set Bypass Conditions for Typing Guard

- The typing guard control in [Access & Data Control
  rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html) allows you to restrict the ability of users to
  type. This option is available from either the Profiles or from the
  Data controls, but we recommend using the Data controls to manage
  policies. 

  ![]()

1. In the **Policy Rules - Edit rule-Data controls** page, select **Typing
   Guard**.
2. Select **Enable**.
3. Select **Prompt**.
4. Select **Popup notification** and define the bypass conditions for file
   upload by selecting one of the following options.:
   1. Warn and allow to proceed anyway—notifies
      users that the web application they are trying to access is
      restricted, but allow them to proceed anyway. You will receive an
      event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that the web application they
      are trying to access is restricted, but allow them to proceed after
      supplying a reason they need access. You will receive an event.
   3. Permission request—notify users that the web
      application they are trying to access is restricted, and prompt them
      to submit a request for access. In this case, you must [review and approve the request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can
      access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single upload.

#### Set Bypass Conditions for Screenshot Protection

The screenshot control in [Access & Data Control rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html) allows
you to restrict the ability of users to take screenshots. This option is
available from either the Profiles or from the Data controls, but we recommend
using the Data controls to manage policies.

![]()

1. In the **Policy Rules - Edit rule-Data controls** page, select
   **Screenshot**.
2. Select either **Allow** or **Allow (Protected)**.
3. Click **Prompt** .
4. Select **Popup notification** and define the bypass conditions for file
   upload by selecting one of the following options.:
   1. Warn and allow to proceed anyway—notifies
      users that screenshots are restricted, but allow them to proceed
      anyway. You will receive an event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that screenshots are
      restricted, but allow them to proceed after supplying a reason they
      need access. You will receive an event.
   3. Permission request—notify users that
      screenshots are restricted, and prompt them to submit a request for
      access. In this case, you must [review and approve the
      request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single upload.

#### Set Bypass Conditions for Printing Controls

The print control in [Access & Data Control rules](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html) allows
you to restrict the ability of users to print. This option is available from
either the Profiles or from the Data controls, but we recommend using the Data
controls to manage policies.

![]()

1. In the **Policy Rules - Edit rule-Data controls** page, select
   **Print**.
2. Select **Allow**.
3. Select **Prompt**.
4. Select **Popup notification** and define the bypass conditions for file
   upload by selecting one of the following options.:
   1. Warn and allow to proceed anyway—notifies
      users that printing is restricted, but allow them to proceed anyway.
      You will receive an event.
   2. Warn and allow the user to proceed anyway with a
      reason—notifies users that printing is restricted,
      but allow them to proceed after supplying a reason they need access.
      You will receive an event.
   3. Permission request—notify users that
      printing is restricted, and prompt them to submit a request for
      access. In this case, you must [review and approve the
      request](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc) before the user can access the app.
5. Set the duration of the Bypass timeframe, ranging from 10 minutes to 90
   days. Select once to allow a single upload.

<a id="manage-prisma-access-browser-requests_task-mcm_hvy_fcc"></a>

#### Manage Permission Requests

After you set bypass request conditions on policy rules, you must review incoming
requests and decide whether or not to allow the requests.

1. From Strata Cloud Manager, select ConfigurationPrisma Browser
   PolicyRequests.
2. Select the request you want to review and click
   Reply.

   ![]()
3. Review the request and then select one of the following responses:

   - Approve—Grants approval for the request for
     the pre-configured duration, or select a different duration.
   - Decline—Rejects the request. Prisma Browser continues to block the requested action or site access.

   ![]()
4. Choose the timeframe for the request. This overrides the default setting in
   the rule with a specific timeframe for the approval.
5. (Optional) Add a comment for the user.
6. Submit your response.

The user will get a notification that there is a
response for their request.

You can also manage
permission requests via API and connect them to external systems.

#### Investigate Bypass Requests

If you have [configured bypass conditions](#manage-prisma-access-browser-requests_task-xgg_w5y_fcc) on your policy rules and
you find that you are [approving similar requests](#manage-prisma-access-browser-requests_task-mcm_hvy_fcc), this might indicate that
you need to tune your policy rules. You can investigate current and past bypass
rules to assess whether you need to make some adjustments to your policy on the ConfigurationPrisma Browser
PolicyRequests page.

- Search for specific bypass requests by URL.
- Filter requests based on the following
  parameters:

  - Request type—Filter on the type of bypass:
    Web access, File upload, File download, or App login.
  - Status—Filter on requests that are
    Pending, Approved,
    or Declined.
  - Created at—Filter on requests made during a
    specific time frame.
  - User—Filter on specific users making
    requests.
  - Policy rule—Filter on the rule that trigged
    the bypass requests.
  - URL—Filter based on the URL of the web
    application that generated the request.

---

<a id="manage-rollback-control-for-the-prisma-browser"></a>

### Manage Rollback Control for the Prisma Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/rollback-control-for-the-prisma-access-browser>*

This is the Rollback Control

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

#### Rollback Control - Overview

The Rollback Control feature in the Administration Console allows you to revert
browsers to a specific version using the existing upgrade control interface
(rollback is currently supported only for Windows). This capability ensures a
stable and controlled browser environment by enabling quick rollbacks in case of
compatibility issues, performance regressions, or unexpected errors after an
update.

#### Managing Rollbacks

To manage rollbacks, you need to use the **Pinned Version** update option.
When you select a compatible device, the feature will display a check box,
**"Force rollback to this version."** Enabling this option will force
newer browser versions to downgrade to the selected versions, after browser
relaunch by the end users.

#### Rollback Workflow

1. Open an existing upgrade policy or create a new one with a higher rule.
2. Navigate to the **Pinned Version** section.
3. Select the target version for rollbacl (Only version 134.x and above support
   rollback).
4. Enable the check box labeled **"Force Windows instances to rollback to
   selected version.**
5. A warning message will appear:“*Using the browser rollback feature will
   restore browsers to the selected version. This might result in loss of
   data, customizations, or recent settings. Proceed at your own risk.*”
6. Apply the policy to execute the rollback.

#### Rollback Behavior

- Browsers with a **higher version** than the pinned version are rolled
  back to the selected version.
- Browsers with an **older version** than the pinned version update to the
  pinned version.

By implementing rollback control, you gain the flexibility to quickly revert
browser versions across managed devices, ensuring stability and minimizing
disruptions caused by unintended updates.

#### Known Limitations

When you select the rollback version for Windows, you
also need to select a pinned version for Mac devices. This allows you to select a
specific version for the Mac machines to remain on.

#### Potential Data Loss Risks

Rolling back to an earlier version of the Prisma® Access Browser might lead to
data loss due to changes in how newer versions store and manage data. You need
to carefully consider the following risks before proceeding:

1. **Loss of Browser Data:** Newer versions of the Prisma Browser could
   update the formats used to store:

   - History
   - Bookmarks
   - Cookies
   - Cached files

   Rolling back could render some of
   this data unreadable or incompatible, leading to loss.
2. **Loss of Security Features** 

   - Newer versions typically include **security patches** and
     updates.
   - Rolling back to an earlier version could expose systems to
     **vulnerabilities** that were patched in later versions.
3. **Compatibility Issues:** 

   - Some **websites and applications** only support newer versions of
     browsers.
   - Older browser versions can impact functionality and prevent access
     to some services.
4. **Extension/Plugin Incompatibility**

   - Updated extensions and plugins could only work with newer browser
     versions.
   - Rolling back could result in some extensions becoming
     **nonfunctional**.

#### Recommendations

Before enforcing a rollback, administrators should carefully evaluate
whether the need to revert outweighs the risks associated with data loss and
security vulnerabilities. We recommend testing the rollback in a controlled
environment before applying it to all managed devices.

By understanding the Rollback Control feature effectively, you can
maintain a stable and secure browsing environment while minimizing disruptions
for users.

---

<a id="prisma-browser-remote-connections"></a>

### Prisma Browser Remote Connections

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/prisma-access-browser-remote-connections>*

How to use Remote connections and PRA

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Prisma Access (Managed by Panorama or Strata Cloud   Manager) - Prisma Access 5.2.1 - Prisma Access Dataplane - minimum version 11.2.4 - Privileged Remote Access (PRA) Add-On License - Prisma Access License with a Mobile User Subscription - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Remote Connections in Prisma Browser enable secure, browser-based access to RDP,
SSH, or VNC sessions for both unmanaged and managed devices. This document explains
how to enable and configure Remote Connections, manage policies, and set up user
access.

#### Remote Connection Overview

Enterprises often host critical infrastructure—including desktops, servers, and
databases—within private networks, restricting access to IT-managed devices via
RDP or SSH. However, employees and contractors may require secure access from
unmanaged or personal devices. Prisma Browser’s Remote Connections enable
controlled RDP, SSH, or VNC access directly from the browser, enforcing security
through Prisma Browser policies.

**Key Benefits**

- Browser-based access to remote hosts via RDP, SSH, or VNC.
- No need to distribute or expose host credentials (when needed).
- Seamless integration with Prisma Access for secure data transfer and traffic
  inspection.
- Granular policy controls (e.g., watermarks, clipboard, device posture
  checks).

#### Main Use Cases

1. **Credential-Protected Access:** Organizations require a secure method
   for granting contractors access to specific remote hosts without exposing
   host credentials. Administrators must configure remote connections—whether
   credential-based or credential-free—and assign them to designated user
   groups while enforcing appropriate data controls and monitoring measures.
2. **BYOD for IT Teams:** IT personnel often need to connect to various
   hosts from their personal devices. To accommodate this while maintaining
   security, administrators establish policies that allow designated user
   groups to access necessary destinations while ensuring compliance with
   security controls.
3. **Sensitive OT Machines:** In critical environments, such as operational
   technology (OT) systems, administrators must enforce restricted access for
   contractors while continuously monitoring their activities. By configuring
   secure remote connections, enabling real-time session monitoring via Live
   Sessions, and retaining the ability to take control when necessary,
   organizations can ensure both security and operational integrity.

#### Configure Remote Connections

1. Go to **Configuration** → **Prisma Browser** → **Remote
   Connections**.
2. Click **Enable.**
   - If you don’t have any Mobile Users (MU) already deployed, ensure you
     configure traffic flow properly in Prisma Access.
3. Modify additional parameters as needed:
   - **Maximum Concurrent Sessions**: Maximum number of remote
     connections a user can open simultaneously.
   - **Session Inactivity Timeout (minutes)**: Automatically ends a
     session after the specified idle period.
4. Click **Save.**

After you first enable the Remote
connection, a new policy is added with a lower priority (above the baseline
rule) that **blocks all users** from using remote connections. Add new policy
rules to allow required user groups to access remote hosts.

#### Update Prisma Access Security Rules

Follow the instructions in the UI and add the relevant rules in Prisma
Access to allow traffic destined for your remote hosts.

If you are using Global Protect in full tunnel mode, please add both
rules.

![]()

#### Configure Applications for Privileged Remote Access

**Add Remote Connections**

Remote Connections let your users access Windows desktops (RDP),
servers (SSH), or other machines (VNC). You can optionally provide credentials
so users don’t need to know them.

1. Go to **Configuration** → **Prisma Browser** →
   **Applications** → **Remote Connections**.
2. Click **Add Remote Connection**.
3. Enter basic information:

   - **Name** and (optional) **Description**
   - **Destination FQDN/IP** (must be reachable via your Service
     Connection/ZTNA)
   - **Protocol (RDP, SSH, or VNC)**
   - **Port** (if different from default)
4. (Optional) Configure authentication:
   - **RDP**: Provide *User Name* and *Password*, or leave
     both empty.
   - **SSH**: Provide *User Name* and
     *Password* or use a *Private Key* (and
     *Passphrase* if encrypted). Optionally, provide a list
     of *Host Key* entries for server fingerprint
     verification.
   - **VNC**: Optionally provide *User Name* and
     *Password*.
5. (Optional) **Enable File Transfer** (for VNC) to allow
   SFTP-based file upload and download.

   - Provide SFTP user credentials, SFTP port, or SFTP key details as
     appropriate.
6. Click **Save**.

You can group multiple remote connections and other Saas/Private applications
into **Application Groups** to streamline policy enforcement and assignment
to user groups.

![]()

![]()

#### Policy Management

Configure remote connections policies just like you do for SaaS and
private applications.

1. Go to **Rules** → **Add a New Rule**.
2. In **Destination**, select **Remote Connections**.
3. Define which remote connections to **Allow** or **Block**
   for a given scope:

   - **Admin-defined connections** (specific or any).
   - **Manual connections** (allowing end users to create their own
     connections).
   - Any combination of the above.

##### How Does Policy Work for Remote Connections?

- **URL Parsing vs. IP/Protocol**: PAB enforces RDP/SSH/VNC
  connections based on extracted IP, port, and protocol, *not* the
  standard URL pattern used for SaaS apps.
- **Rule Prioritization**: Higher priority rules take
  precedence.
- **Example**
  - Rule 1: *Allow* Remote Connection A,
    **enable** watermark, **allow** clipboard.
  - Rule 2: *Allow* all manual connections but
    **block** clipboard.
  - **Outcome**: Remote Connection A uses Rule 1’s settings
    (clipboard allowed, watermark on). Manual connections not
    covered by Rule 1 fall under Rule 2 (clipboard blocked).

    ![]()

###### Policy Limitations

- **Unsupported Data Controls** for remote
  sessions:
  - Data masking
  - Typing Guard
  - Read-only mode
- **Clipboard Controls**: If policy blocks clipboard,
  users only see a blocking notice once at session start. No
  events are generated for each clipboard use attempt.

#### Manual Connections

**Why use Manual Connections?**

You might need flexible access to many hosts, or you may not want to configure
each server individually in Prisma Browser.

**How this works?**

- You grant *Manual Connection* permissions via policy.
- Users can create, edit, and delete their own connections.
- Users **cannot** share these connections; the link is user-specific.
- If the policy later revokes *Manual Connection*, all user-defined apps
  become inaccessible.

  An admin sets a policy allowing
  certain user groups to create their own RDP/SSH/VNC connections
  without pre-registering them in the console.

  **What if I need to restrict the access to a specific
  protocol or an IP range?**

  You can create a rule
  in the PA Security Policy to allow the specific user group only a
  specific protocol (defined applications) or a defined IP range (in the
  Destination of the rule).

#### Visibility

- **Event Page Display:** 
  - The **URL column** displays IP:Port (Protocol) for remote
    sessions.
  - *Admin-Defined Connections*: These appear with a clickable link
    to a defined application.
  - *User-Defined Connections*: Displayed without a link to a
    defined application.
- **Event Recording & Live Streaming**:
  - Remote sessions support event recording and real-time monitoring via
    **Live Sessions**.

#### Just-in-Time Control (User Requests)

- **Requests Page**: The URL column shows IP:Port (Protocol) for the
  requested connection.
- **Approved Request**: Grants access to the specific remote connection
  only.
- **Manual Connection Behavior**: If you select “Approval Required” for
  manual connections, the user must request approval for each new app they
  create .

#### Permissions

- **Remote Connections Page**
  - Requires “Application” permission. If you can create
    applications, you can also create remote connections.
- **Remote Connections Settings Page**
  - Same permissions as other settings.
- **Policy, User Requests, and Visibility**
  - No additional special permissions beyond existing
    mechanisms.

#### End-Users

- **Accessing Assigned Connections:** Users can access their
  assigned remote connections from the Home Page or the Remote Connections
  page within the browser. Additionally, they have the option to bookmark any
  assigned or manually created connections for quick access.
- **Logging In:** If administrator-provided credentials are available,
  users are logged in automatically. Otherwise, they will be prompted to enter
  their credentials manually.
- **Manual Connections:** If permitted, users can create, edit, and delete
  their own remote connections. These manually created connections remain
  private and cannot be shared with other users.

If your organization doesn’t use the standard
Prisma Browser homepage, users can still access the portal from the
extension’s menu.

![]()

![]()

![]()

![]()

---

<a id="prisma-browser-self-protection-for-windows"></a>

### Prisma Browser Self-Protection for Windows

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/prisma-browser-self-protection-fpr-windows>*

Self protection for windows

The **Prisma Browser Self-Protection** feature provides advanced runtime
protection for Prisma Browser processes on Windows devices. It integrates a **Windows
kernel-mode driver** that prevents interference from malicious software or
unauthorized system changes.

The self-protection capability delivers kernel-level defense for Windows
systems, protecting Prisma Browser’s runtime integrity.

This feature is **available only on Windows 10 22H2 and
later** and is **not supported on macOS**

For macOS devices, **System Integrity Protection (SIP)** and existing posture controls
continue to serve as the primary mechanisms for protecting the browser environment.

Supported Platforms

|

Category | Supported | Not Supported |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Operating System | Windows 10 22H2 and newer (physical or virtual machines) | Windows versions before Windows 10 22H2 |

|

Installation Type | Admin level installation | User level installation |

#### Use Cases and Risk Profiles

The Self-Protection feature focuses on protecting Prisma Browser in **high-risk
environments**, particularly where administrator privileges or unmanaged
systems increase the attack surface.

|

Device Type | OS User Role | Risk Profile | Driver Requirement |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

Unmanageed devices (BYOD / Contractors | Admin | **High risk** (insider threats, malware exposure) | **Driver required** to enforce kernel-level integrity protection |

|

**Managed Corporate Devices** | Non-Admin | **Low risk** (centrally managed and policy-secured) | Driver supported, but not critical |

#### Installation Modes

Prisma Browser supports both **user-level** and **admin-level**
installation modes.

The self-protection driver is only available in the **admin-level**
installation.

|

Installation Types | Permissions | Driver Component |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

User Level | User permissions | Driver **cannot** be installed |

|

Admin level | Administrator permissions | Driver protection can be installed and activated |

- The driver is **not installed by default**.
- The **administrator must explicitly enable** the self-protection policy
  before the driver is installed and activated.
- After installation, Prisma Browser can run under a **non-admin user
  account**, and the protection driver will remain active under policy
  control.

#### Policy Configuration and Control

A new policy control named **Browser self-protection** is available under browser
security policies.

This setting enables administrators to remotely control the activation state of the
protection driver.

**Policy characteristics:**

- Applies only to **Windows** systems where Prisma Browser is
  **installed as admin**.
- Disabled by default
- Managed centrally through enterprise policy distribution.

![]()

#### Enforcement for Inactive Protection

If Prisma Browser cannot start the protection driver (for example, when installed as
a user or running on unsupported ARM hardware), the administrator can define an
**enforcement response** using the *Enforcement for Inactive Protection*
setting.

|

Enforcement Option | Administrator Action | End-User Impact |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Do not Enforce | Allow browser to run anyway | No message appears |

|

Prompt and Proceed anyway | Display warning, and continue the browser session | User sees a warning dialog, but the browser runs normally |

|

Block Browser Access | Prevent browser from starting | Browser shuts down and the user sees the warning dialog |

![]()

#### End User Experience

When self-protection is properly installed and policy-enabled:

- The protection driver runs silently with **no performance
  impact**.
- The browser operates normally; no UI change or notification is
  shown.
- The feature automatically activates at runtime under the active Prisma Browser policy.

#### Multi-Profile Sessions

Prisma Browser’s **multi-profile policy** ensures consistent protection across all
profiles.

If any profile activates the protection driver during a session, the driver remains
active and safeguards all profiles for the remainder of that session.

#### Device Reporting and Troubleshooting

Device and browser diagnostics display protection information to assist
administrators in verifying the feature’s status.

Reported attributes include:

- Browser installed as admin (Yes / No)
- OS user is admin (Yes / No)
- Device architecture
- Browser self-protection status

|

Status | Description |

| --- | --- |

|  |  |
| --- | --- |
|

Protected | Prisma Browser installed as Admin Policy enabled |

|

Not Protected | Policy enabled, but driver failed to start |

|

Inactive | Policy not set or disabled |

|

Unknown | Status undetermined (possible old Prisma Browser version) |

#### Deployment Lifecycle

- **Driver upgrade:** Managed seamlessly during standard Prisma Browser update
  flow.
- **Uninstallation:** Removes driver and associated services automatically with
  Prisma Browser.
- **Reinstallation guidance:** When reinstalling Prisma Browser to enable
  driver protection, users should **not delete browsing data**.

#### **Compatibility and Limitations**

The following configurations are **unsupported** or have **limited
protection**:

|

Limitation | Description |

| --- | --- |

|  |  |
| --- | --- |
|

User-Level Installation | Driver not installed; self-protection inactive |

|

Windows ARM Architecture | Kernel driver not supported |

|

Older Windows Version | Driver not compatible; feature unavailable. |

---

<a id="prisma-browser-guest-mode"></a>

### Prisma Browser Guest Mode

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/prisma-browser-guest-mode>*

Prisma Browser Guest Mode

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

| - Windows deployment - Prisma Browser v149 or later |

This article discusses the following topics:

- Overview - What Guest Mode is, and when it applies.
- Configuration - Enabling Guest Mode via registry keys
- Behavior - User experience in a Guest session
- Security Consideration - Risks of unauthorized activation and recommended
  guardrails to protect your environment

**:** Guest Mode bypasses all Prisma Browser security controls by design. Before enabling Guest Mode, review
the Security Considerations section to understand the risks and consider deploying
the recommendations.

In exclusive browser environments where Prisma Browser is the only installed browser,
users who cannot log in to the managed environment are unable to access the internet.
Guest Mode addresses this by providing an ephemeral solution for unmanaged web access
directly from the login page.

Guest Mode
bypasses all Prisma Browser security controls by design. When enabled, it opens
an unmanaged browser window with no DLP, URL filtering, threat prevention, or policy
enforcement.

#### Guest Mode Configuration

Guest Mode is only supported in Microsoft Windows.

Guest Mode is enabled via a local registry key. Administrators should deploy this key
to target endpoints where emergency internet access is required.

**Registry Path:**HKLM\SOFTWARE\Policies\PaloAltoNetworks\PrismaAccessBrowser

|  |  |
| --- | --- |
|

**Property** | **Value** |

|

Value Name | GuestModeAccessibility |

|

Value Type | REG\_DWORD |

|

Value Data | **1** (Enabled) or **0** (Disabled) |

#### Guest Session Behavior

When a user selects "Continue as Guest" on the login screen, the browser
initiates an ephemeral session with the following characteristics:

- An unmanaged Chromium window opens, visually distinct from managed
  sessions.
- No security policies (DLP, URL filtering, threat prevention) are
  enforced.
- All session data (history, cookies, cache) is discarded immediately
  upon closing the window.

#### Guest Mode Limitations

- **Private Applications:** Applications accessed via Prisma Browser
  tunneling are unavailable.
- **IdP Enforcement:** Guest Mode does not bypass identity-based access
  controls at the application layer; IdP-protected apps remain inaccessible.

#### Security Considerations

#### Risk: Authorized Guest Mode Activation

Any entity with write access to the registry can enable Guest Mode, potentially
allowing local administrators or malware to bypass enterprise security policies or
establish exfiltration channels.

#### Recommendations

#### 1. Restrict Registry Key Write Access

Harden registry ACLs to limit write access strictly to SYSTEM and Domain Admins,
explicitly removing write permissions for the local Administrators group.

#### 2. Monitor for Unauthorized Changes

Utilize SIEM or EDR solutions to alert on modifications to the Guest Mode registry
key, specifically monitoring for Event ID 4657 when the subject is not a trusted
service account.

#### 3. Use Group Policy to Enforce Key Values

Deploy the configuration as a GPO Policy rather than a Preference. This ensures the
value is re-applied every 90 minutes, automatically reverting local tampering.

#### 4. Endpoint Detection Rules

Configure Cortex XDR or similar platforms to flag any process other than approved
management tools (e.g., gpupdate.exe) writing to the PaloAltoNetworks registry
path.

##### Summary - Defense in Depth Approach

|  |  |
| --- | --- |
|

**Condition** | **Action** |

|

Key set to 1 by a local user account | High-priority alert |

|

Key set to 1 outside approved change window | Medium-priority alert |

|

Key set to 1 on endpoints not in the approved Guest Mode OU | High-priority alert |

##### Use Group Policy to Enforce Key Value

Deploy the key as a **Policy** (not a Preference) via GPO.
Policy-based registry values are re-applied at every Group Policy refresh
interval (default: 90 minutes), automatically reverting any local tampering.

**Steps:**

1. Create a policy that sets GuestModeAccessibility = 0
2. Link it to all OUs except those where Guest Mode is explicitly
   needed during outages
3. Any local modification will be overwritten at the next GP
   refresh cycle

##### Endpoint Detection Rules

Create detection rules in your EDR/XDR platform (e.g., Cortex XDR) to
flag processes writing to the PaloAltoNetworks\PrismaAccessBrowser registry path
that are not:

- gpupdate.exe or svchost.exe (Group Policy client)
- Your approved configuration management tool

**Summary of Defense-in-Depth Approach**

|  |  |  |
| --- | --- | --- |
|

**Layer** | **Control** | **Purpose** |

|

**Preventive** | Registry ACLs | Block unauthorized writes |

|

**Detective** | SIEM/EDR alerts | Detect unauthorized activation |

|

**Corrective** | GPO refresh cycle | Restore correct state |

---

<a id="the-prisma-browser-enterprise-password-manager"></a>

### The Prisma Browser Enterprise Password Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-enterprise-password-manager>*

The information that everyone needs about the browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Password-related breaches remain a major risk in enterprise environments. The
Prisma Browser introduces centralized password management to enforce secure
handling of credentials.

Built-in browser managers lack enterprise features like policy rule controls,
access management, encryption, and audit logging. Extensions add functionality but
increase the attack surface and are vulnerable to user tampering.

Integrating password management with existing identity and access systems adds
complexity and cost. As a result, many organizations avoid standardization, leading to
insecure practices such as password reuse, and unauthorized credential sharing.

#### The Prisma Browser Enterprise Password Manager

To address these challenges, we developed the Enterprise Password Manager as a
first-party solution, purpose-built to meet the needs, and tightly integrated with
Prisma Browser. The solution supports complex enterprise requirements by
enabling robust security controls, seamless policy rule enforcement, and a
streamlined user experience.

#### Key Features

![]()

#### Password Manager - User Guide

[Click here to go directly to the Admin Guide](#concept-mmv_gmh_jfc_adminguide).

#### Password Manager Inventory

The Password Manager in Prisma Browser enables users to securely store,
manage, and use credentials for applications not integrated with the organization's
identity provider.

The main page of the Password Manager is the Inventory page, where you can
manage, create, edit, or remove logins.

You can open the inventory in the following ways:

- Click the Prisma Browser icon → Password Manager.
- Click Settings → Password and Autofill → Password Manager.
- Open the Password Manager from one of the dialogs opened by the Browser when
  saving and updating or viewing passwords on a website.
- Click on the Password Manager key icon on the Browser sidebar.
- Navigate to prisma://password-manager/

When you open the Password Manager, it displays the list of available logins. 

![]()

If you previously used the Legacy Password Manager in Prisma Browser,
the system migrates your logins automatically to the Enterprise Password
Manager.

If no logins exist, the Password Manager shows an empty state screen.

![]()

#### Create a Login

You can manually create logins through the Password Manager Inventory.

To create a login manually, open the Inventory and click “Create login.”
Enter the required details:

- **Username** for the application (optional).
- **Password** for the application (mandatory).
- **URL** of the application that triggers the Password Manager to suggest this
  login (mandatory).
- **Note** describing the login (optional). 

  ![]()

#### Manage Logins in the Inventory

Click a login to open its details pane, where you can view, edit, and manage the
entry.

The browser may prompt you for a step-up MFA (PIN code or
passkey) based on your admin policy rule before revealing login details.

![]()

![]()

You can view the details of a login using the available options:

- Click the **reveal** or **copy** icons to view or copy the username or
  password (if allowed).
- Click the **arrow** icon to open the URL associated with the login.
- Click **Edit** to change the login details. 

  ![]()
- Click **Delete** to remove the login from the inventory (if allowed).
  **Make sure you have another way to access the website before deleting
  a login**.

#### Password Generator

The Enterprise Password Manager includes a built-in password generator, accessible
from the inventory page. This tool helps create strong, difficult-to-crack
passwords.

1. Navigate to the Inventory and click **Password Generator**. 

   ![]()
2. Choose your desired password characteristics. 

   ![]()
3. The generated password is displayed. Click to copy it to your clipboard.
4. Paste the password when creating or updating account passwords or
   websites.

#### Import Logins

You can import logins from a third-party browser or password manager by following
these steps:

1. Navigate to the Inventory and click **Import**. 

   ![]()
2. Select the source for the import. 

   ![]()
3. Export your logins from the source as a CSV file, following the provided
   instructions. 

   ![]()
4. Choose the CSV file to import your logins into the Prisma Browser
   Password Manager.

#### Export Logins

You can export your stored passwords so that you can import them to another
machine.

1. Click on the Prisma Browser icon on the toolbar and click to open the
   **Control Pane**.
2. Click **Password Manager**. 

   ![]()
3. In thee Password Manager, click **Export**.

   ![]()
4. Exporting content from the Password Manager requires you to enter your MFA
   method. 

   ![]()
5. Export your logins from the source as a CSV file, and save it to your
   preferred location. 

   ![]()
6. Click **Save**. Choose the CSV file to import your logins into the Prisma Browser Password Manager.

#### Settings

Click the **Settings** tab to enable or disable the Password Manager for your
browser or to import logins from another browser or third-party Password Managers.

![]()

#### Password Manager Interactions

The Password Manager automatically appears when it detects an available login for a
URL or when you save or update a password for that URL.

#### Save a Login

When you register on a site or log in to a URL that the Password Manager does not
recognize, it prompts you to save a new login to the Prisma Browser Enterprise
Password Manager. 

![]()

Click **Login details** to add more information to the login. 

![]()

If you missed or closed the dialog by mistake, you can get back to it by clicking the
key icon.

#### Update a Login

When you update a password in the Prisma Browser Enterprise Password Manager, the
system prompts you to save the changes.

If you miss the prompt, click the key icon in the omnibox to reopen it. 

![]()

#### Use a Login

If there is a key icon in the omnibox, this means that there are saved logins for
the current site. 

![]()

Click on the icon to view the logins. You can drill down to see the details. 

![]()

The browser
might prompt you for a step-up MFA when you reveal login details.(PIN code,
Passkey, or IdP authentication) based on your admin policy rule configured in
[Browser Security > Browser Hardening >
Authentication Factor](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-browser-hardening.html#configure-browser-hardening_task-ydp_f2l_hcc).

When you focus on an input field in a
login form on a URL with an available login, the Password Manager suggests matching
logins and enables you to autofill them.

To autofill the
login, the browser can also require a step-up MFA based on your admin policy
rule.

![]()

#### Profile Sync

The Password Manager automatically syncs personal logins across user
devices when you sign in with the same credentials.

This sync functionality works only if you enable profile
sync in the **Browser Customization → Profile sync** policy rule settings.

The Password Manager officially supports desktop devices
(Windows and macOS). It also syncs passwords to the mobile Password Manager where
sync is supported.

<a id="concept-mmv_gmh_jfc_adminguide"></a>

#### Prisma Browser Enterprise Password Manager - Admin Guide

#### Policy Rule

The Password Manager is managed in the **Browser Security -> Saved Data ->
Password Manager** control.

The default value of the control is **Enabled,** with MFA enabled on a 5-minute
timeout. 

![]()

The Password Manager can be enabled or disabled.

When it is disabled, the Password Manager pop-ups do not display, and the
inventory will be disabled. 

![]()

#### Multi-factor Authentication

The system can require users to complete a step-up MFA based on policy rule
when performing actions that involve retrieving a login, such as:

- Opening a login from the Inventory
- Viewing login details through the omnibox pop-up
- Autofilling a login form

After a successful step-up MFA, the system won’t prompt again for a defined
interval (5 minutes by default).

Administrators can enable or disable step-up MFA for all logins stored in the
Password Manager by configuring the **Password Manager** policy rule control.
They can also adjust the MFA Prompt Interval setting it to always prompt, or to a
shorter or longer interval than the default.

You can configure the MFA factor in **Browser Security →
Authentication Factor**. PAB currently supports local PIN and Passkey
authentication. [Click here for more information.](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security?otp=task-ydp_f2l_hcc#task-ydp_f2l_hcc)

#### Events

The Prisma Browser Enterprise Password Manager logs all actions that users
perform within the manager, including:

- **Login created** - The system logs when a user adds a login through the
  Inventory or the Save Login pop-up.
- **Login deleted** - The system logs when a user deletes a login through
  the Inventory.
- **Login details changed** - The system logs changes to a login’s details,
  including metadata or the password value.
- **Login retrieved** - The system logs when a user retrieves a login by
  autofilling it or by using the **eye** icon or **copy** button to view
  or copy the credentials.

You can view these events in the Prisma Browser Event log under the new
Password Manager category.

![]()

The system can forward these events to your organization's SIEM/SOC. You can then
correlate them with other activity – such as login attempts, failed logins, or
browsing events – to build a complete timeline around credential usage.

---

<a id="location-based-policy"></a>

### Location-based Policy

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/location-based-policy>*

The location-based policy can be used to limit access to the Prisma Browser based
on location.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone - Prisma Browser Mobile - Prisma Browser Extension | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Linux/IGEL browser - **No support**

This feature requires Prisma Browser version **129.90.2910.2** and later.

You now have the ability to apply policies based on the device's location in addition to
the other Scope parameters that can be used for all policy rules.

The policy engine evaluates the location of the device every 60 minutes and reports the
location back to the server. For macOS and Windows devices, the policy engine will use
the OS Location Services, if enabled. Otherwise the engine will use Geo IP location.

#### Important Information for Admins

1. End-users who use VPN services can change their public IP by selecting a
   different location for their connection. For example, a user in Germany can
   decide to connect to the company network from a location in the United States,
   depending on the VPN provider.
   - To reduce the risk of location bypass, you can use MDM (for managed
     devices) and enable OS location services to the browser, as well as to
     browsers that use the Prisma Browser Extension.

   The location may not be accurate around
   national borders for both OS Location Service and Geo IP.
2. The Prisma Browser for Mobile currently uses only Geo IP.
3. macOS Location Services are temporarily unavailable in Israel. See here for
   more information. [Why have Apple and Google disabled map
   features in Israel and Gaza?](https://www.govtech.com/question-of-the-day/why-have-apple-and-google-disabled-map-features-in-israel-and-gaza)

Older versions of the Prisma Browser can only use Geo
IP. If you want to use OS Location Service, you need to upgrade.

Prisma Browser for Mobile supports Geo IP only.

Linux/IGEL Browser - **No Support**

---

<a id="the-prisma-browser-extension"></a>

### The Prisma Browser Extension

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-extension>*

The Prisma Browser Extension is a tool that allows organizations to apply some of
the Prisma Access Secure Enterprise Browser functionality without installing the full browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser Extension is a tool that you can install on consumer browsers such
as Google Chrome and Microsoft Edge browsers, running on Windows, macOS, and ChromeOS
Operating Systems

IT and security teams can enhance organizational security by implementing Prisma Browser with a hybrid strategy, using the Prisma Browser Extension to
bridge current browsing practices with advanced protections. This approach enables
employees to continue using familiar browsers while administrators gain greater
visibility and control over all browsers across the enterprise.

The extension actively monitors user activity on commercial browsers, helping
to mitigate Shadow IT risks and providing real-time phishing protection. By centralizing
visibility and allowing consistent enforcement of security policies, the Prisma Browser Extension integrates smoothly with existing tools while guiding users
to the enterprise browser when accessing sensitive applications.

Designed as a foundational layer in a phased deployment, the Prisma Browser
Extension supports a secure transition toward full adoption of the Prisma Browser.
For scenarios requiring heightened protection, such as critical applications or
high-risk users, a full enterprise browser deployment offers unparalleled control and
functionality, setting a gold standard for security. This hybrid solution thus delivers
immediate security benefits while preparing organizations for comprehensive,
enterprise-grade browser security. 

![]()

#### Deploy the Prisma Browser Extension

The Prisma Browser Extension can be installed on chromium-based
browsers (Chrome, Edge, Arc, Brave), running on Windows, macOS, and ChromeOS
Operating System.

The extension deployment is based on the operating system, the IdP, and the
browser type. The supported IdP types are:

- Entra ID
- Okta
- Google
- PingOne
- PingFed

  The Automatic Login mechanism is
  currently supported for Okta, Azure, and Google.

For more information regarding Prisma Browser Extension Deployment, see
[Deploy the Prisma Access Browser
Extension](https://docs.paloaltonetworks.com/prisma-access-browser/deployment/deploy-the-prisma-access-browser-extension).

#### Prisma Browser Extension Login Enforcement

Currently, the Prisma Browser Extension utilizes an automatic login
feature that detects the user names from the most recent login to a web Identity
Provider (IdP) application before applying Prisma Browser Extension policies. In
some cases, the user name may not be recognized, preventing the Browser Extension
from logging in and enforcing the admin policy. This occurs mainly in cases where
the user has not yet logged into any IdP applications on their browser.

To avoid situations like this, the Prisma Browser Extension includes a
feature that you can configure that requires logging into the Prisma Browser
Extension before accessing specified sites. This prevents users from bypassing the
administrative policies by using applications without the proper login.

To configure the Login Enforcement Policy, follow the procedures for
creating a new [Data Control](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-rules/manage-prisma-access-browser-access-and-data-control-rules.html#manage-prisma-access-browser-access-and-data-control-rules_task-create-access-rule) rule. Take note of
the following requirements:

1. In the **Scope** section, select the user ***Anonymous PABX.*** 

   When you select the Anonymous PABX user, several
   sections in the Add rule wizard will be unavailable. Some of the options in
   the available sections will also be unavailable.

   ![]()
2. In the **Destinations** section, configure the applications and URLs that
   users will be *allowed* to access without being logged in to the IdP.
3. In the **Web Access** section, select **Allow**.

   Now you will create
   the second part of the Login Enforcement:
4. In the **Scope** section, select the user ***Anonymous PABX.***
5. In the **Destinations** section, configure the applications and URLs that
   users will be *not be allowed* to access without being logged in to the
   IdP.
6. In the **Web Access** section, select **Block**

Please **do not** block the IdP URLs in the Web
application step. This will prevent users from logging into the Prisma Browser
Extension.

#### Prisma Browser Extension Posture Attributes

The Prisma Browser Extension allows you to configure the posture requirements for
your devices running the Prisma Browser Extension in the same way that it
configures posture for your desktop and laptop devices running the Prisma Browser.

For more information on the available Posture attributes, refer to [Configure Prisma Browser Extension Posture Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-extension-device-posture-attributes.html).

#### Prisma Browser Extension Policy

##### Access & Data Control Rules

Features of supported Access & Data Control policies are supported for
devices running the Prisma Browser Extension. The following exceptions
should be noted:

- The **Set dialog text** feature, that permits you to customize your own
  text for a particular feature, is supported for the extension.
- Note the following feature functionality in the Web Access section:
  - Prompt options:
    - Permission request - Acts as **Block.**
    - Warn and allow to proceed anyway - **Supported.**
    - Warn and allow to proceed anyway with reason -
      **Supported.**
  - Require MFA - **Not supported.**
  - Pick A Label - **Not supported (skipped)**.
  - **Enforce Prisma Browser Extension traffic redirection to Prisma Browser** allows you to redirect users to the Prisma Browser when accessing web applications. The
    Allow/Prompt/Block settings will still be enforced, regardless.
- Login restrictions - **Not supported (skipped)**.
- When contains... - **Not supported (skipped)**.

#### Data Controls - Data Leak Prevention

You need to be aware of the differences
between the Prisma Browser and the Prisma Browser Extension policies.

#### **File Download**

For more information, see [File Download](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention.html#configure-data-leak-prevention_task-wcx_qv3_hcc).

File Download control provides multiple capabilities related to
downloading files from websites that match a specified URL, application or
website classification.

To set the File Download control:

- **Allow** - the Prisma Browser Extension will allow all
  downloads.
- **Allow (Protected)**) - Will be treated as
  **Block**.
- **Block** - The Prisma Browser Extension will block all
  downloads.
- Apply on:- Select between one of the following options:

  - **Any file** - the download restrictions will apply to all files.
  - **Specific files**- the download restrictions will apply to files
    that meet the selected specifications (the rule can contain as many
    of these specifications as needed):
    - **File size** - set the size of the file.
    - **File types** - set the [file types](https://docs.console.talon-sec.com/en/articles/346) that
      need to match this rule.
    - **File hash** - Not supported.
    - **MIP label** - Not supported.
  - **Prompt**- when there is a restriction, select between one of
    the following options:
    - **None** - there will be no prompts.
    - **Before download** - Not supported; treated as
      **Block**.
  - **Require MFA** - Not supported.

#### **File Upload**

For more information, see [File Upload.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention.html#configure-data-leak-prevention_task-bm2_fz3_hcc) .

File Download control provides multiple capabilities related to
downloading files from websites that match a specified URL, application or
website classification.

To set the File Download control:

- **Allow** - the Prisma Browser Extension will allow all
  downloads.
- ****Allow protected files only between the rule’s web
  applications****) - Treated as **Block**.
- **Allow only non-protected files** - Treated as **Block**.
- **Block** - The Prisma Browser Extension will block all
  downloads.
- Apply on:- Select between one of the following options:

  - **Any file** - the download restrictions will apply to all files.
  - **Specific files**- the download restrictions will apply to files
    that meet the selected specifications (the rule can contain as many
    of these specifications as needed):
    - **File size** - set the size of the file.
    - **File types** - set the [file types](https://docs.console.talon-sec.com/en/articles/346) that
      need to match this rule.
    - **File hash** - Not supported.
    - **MIP label** - Not supported.
  - **Prompt**- when there is a restriction, select between one of
    the following options:
    - **None** - there will be no prompts.
    - **Before Upload** - Not supported; treated as
      **Block**.
  - **Require MFA** - Not supported.

[Clipboard](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention.html#configure-data-leak-prevention_task-krf_31j_hcc) - Only works for visibility in
the selected Scope

#### Browser Security - Extensions

The following policies are supported:

[Allowed or Blocked Extensions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-extensions.html#configure-extensions_task-ydr_5hl_hcc)

[Block Extensions by Permission](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-extensions.html#configure-extensions_task-tff_23l_hcc)

#### Browser Customization - Branding

The following policies are supported:

[Theme Color](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-qgz_hxk_hcc)

[Brand Color](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-rtz_jcr_hcc)

[Company Logo](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-edc_qcr_hcc)

[Company Name](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-q3r_3dr_hcc)

[Custom Texts](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-ijb_4dr_hcc)

[Browser Icon](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-branding.html#configure-branding_task-zvj_c2r_hcc)

#### Browser Customization - Customization

The following policy is supported:

[Search Engine Content Filtering](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-customization.html#configure-customization_task-rl2_gfn_2dc)

---

<a id="prisma-browser-extension-history-collection"></a>

#### Prisma Browser Extension History Collection

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-access-browser-extension-history-collection>*

Describes the PABX history collection

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser Extension - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

##### History Collection Overview

Installing the extension is simple, and it operates transparently for end users. The
tool allows efficient collection of valuable data without disrupting workflows. The
extension retrieves and presents historical data, providing customers with immediate
insights into security risks based on past application usage and download history.
These insights encourage Prisma® Access Browser adoption and support broader
deployment.

During the proof of concept (PoC), the immediate goal is to deliver instant security
insights as soon as you install the Strata™ Cloud Manager tenant. This ensures that
security gaps and the value of Prisma Browser are demonstrated in the initial
customer conversation without delays.

##### How Does the Extension History Collection Function?

The History Collection rule enables gathering URLs and downloaded files accessed by
users on all devices within the defined scope. Key functionalities include:

- Collecting history data only from logged-in PABX devices.
- Retrieving historical data from the 30 days preceding PABX
  installation.
- Updating history data in the dashboards and events section within
  minutes.

###### History Collection Use Cases

The Prisma Browser History Collection allows you to see information on the
different dashboards. This allows you to examine how certain key elements are
operating.

- **Access to Malicious Sites:** Use the overview dashboard to highlight
  incidents involving access to malicious websites.
- **Access to Risky Categories:** Display visits to potentially risky
  website categories, such as AI, gambling, and gaming, in the Web Security
  dashboard under “Top 10 Most Visited Web Classifications.”
- **Data Downloaded from Top Applications:** Use the Data Leakage
  Prevention dashboard to showcase the volume of data downloaded from the top
  five SaaS applications, ensuring there are no insider risks.
- **Downloads from Unknown websites:** Highlight downloads from unfamiliar
  or rarely used websites within the organization in the Data Leakage
  Prevention dashboard under ‘Top 10 Most Active Apps on websites.’

###### Demonstrating the Extension’s Capabilities

To conduct a successful demo:

- Install the extension for the first time within a designated
  profile.
- The order of configuring the rule or installing the extension does
  not affect the functionality.

If the rule's scope includes more than 50 users, you
will not be able to save it. You will receive a warning explaining the
reason why.

---

<a id="prisma-browser-extension-best-practices"></a>

#### Prisma Browser Extension - Best Practices

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-browser-extension-best-practices>*

The definitivve best proactices guide

##### Starting Point - Choose Your Baseline

Before creating any specific rules, we recommend that you decide the
organizational posture that best fits your needs. This choice changes how subsequent
security filters (like **Block by Permission**) behave.

- **Block-First Strategy (Recommended for High Security):** Start with a
  **Block All** rule, then. You then explicitly grant exceptions via an
  **Allow List**. This is the most restrictive and secure approach.
- **Allow-First Strategy (Recommended for User Flexibility):** Start with an
  **Allow All** rule,. You then layer **Block by Risk** or specific
  **Block Lists** to remove dangerous items.

##### Core Mental Model - The Two Stage Resolution

Policies are applied in two separate and distinct stages:

- **Stage 1: Identity Resolution (The Stack):** The system resolves the
  extension's status based on its specific ID or broad type (Allow All, Block
  All, Allow List, or Block List).
- **Stage 2: The Security Vetoes:** Once the identity is resolved, the
  system applies the "Security Filters" (**Block by Risk** and **Block by
  Permission**) and the "Operational Mandate" (**Force
  Install**).

##### Stage 1: Identity and Risk (The Policy Stack)

Rules are processed from the **Bottom** (lowest priority) to the **Top**
(Highest Priority).

**A. The "Set Subtraction" Logic**

When specific lists conflict, they modify the set of allowed extensions through
mathematical subtraction:

|

Starting Rule | Higher Priority Rule | Resulting Logic | Real-Life Example |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

**Allow List (Set A)** | **Block List (Set B)** | **Allow List (A minus B):** The Block List removes its items from the allowed set. | **Scenario**: You allow 3 productivity extensions (A, B, C). A new security policy blocks extension B. **Result**: Only A and C remain allowed. |

|

**Block List (Set B)** | **Allow List (Set C)** | **Block List (B minus C):** The Allow List creates exceptions, removing its items from the blocked set. | **Scenario**: You block all File Sharing extensions(X, Y). Finance specifically needs App X. **Result**: App Y remains blocked, but App X is now an exception and allowed. |

**B, Integrating Block by Risk**

**Block by Risk** acts as a filter that sits on top of the
Identity resolution:

- **The Filter Rule:** If an extension is 'Allowed' by its identity
  in Stage 1, the system checks for any active **Block by Risk**
  rules. If the extension matches the risk level defined in the
  highest-priority rule, it is **Blocked**.
- **The Escape Hatch:** A high-priority **Allow List / Allow by
  ID** rule is the only way to "rescue" a specific extension
  that has been caught by a broad **Block by Risk** policy.

|

Feature | Mechanism | Real-Life Example |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**The Filter Rule** | **Block by Risk** acts as a security gate for extensions allowed by the stack. | **Scenario:** You have a **Block-First** strategy. You add a **Translation App** to your **Allow List**. (in higher priority) However, the app is later flagged as **High Risk** (in higher priority) because of excessive data collection.  Final structure: High risk rule **on top**of allow list **on top of** block all **Result:** The extension is **Blocked** because the Risk Rule (Stage 2) overrides the Allow List (Stage 1). |

|

**The Escape Hatch** | A high-priority **Allow List** rule can specifically "rescue" a risky extension. | **Scenario:** You have a broad policy to **Block High Risk** extensions. Your developers need a specific **Debugging Tool** that is flagged as High Risk due to its deep browser access. **Result:** You place the **Debugging Tool ID** on an **Allow List** with a higher priority than the Risk rule. The tool is **Installed**, effectively bypassing the broad risk block for that specific case. |

##### Stage 2: The High Priority Vetoes

These rules generally sit outside the standard Stack and can override the results of
Stage 1.

**A. Force Install: The operational mandate:**

Force Install ensures an extension is present and enabled,
regardless of most blocking rules:

- **Force Install vs. Block All:**
  **Force Install Wins.**
- **Force Install vs. Block by Permission:**
  **Force Install Wins.**
- **Force Install vs. Block by Risk: Force Install
  Wins**
- **Force Install vs. Block List:**
  **Block List Wins (Critical Deviation).** An explicit ID-based
  block removes even a Force Installed extension. When the Block List
  rule is removed, the extension is re-installed.

|

When Force Install meets... | The Winner is... | Real-Life Example |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**A "Block All" Strategy** | **Force Install** | **Scenario:** You have a strict "Default Deny" policy that blocks all extensions. However, you **Force Install** the corporate password manager. **Result:** The password manager stays installed and working, even though everything else is blocked. |

|

**A "Block by Permission" Security Gate** | **Force Install** | **Scenario:** You block all extensions that request "Access to all websites" for security. You then **Force Install** a security agent that needs that exact permission. **Result:** The security agent bypasses the gate and stays active. |

|

**A specific "Block List" Rule** | **Block List (The Exception)** | **Scenario:** You **Force Install** a specific browser Extension. Later, you discover a bug and add that Extension ID to a **Block List** to stop its use. **Result:** The Block List rule "wins" and removes the extension. If you later delete that Block List rule, the extension will automatically re-install. |

|

**Force Install meets Block by Risk** | **Force Install** | The extension remains active regardless of its risk score. |

##### Known Limitation: Identity-based Blocking with Force Install

**Current Behavior:** There is a known limitation regarding the "Kill
Switch" functionality when using a **Block All** strategy alongside **Force
Install** mandates. Currently, if a global **Block All** rule is active, a
specific **Block List** (Identity-based block) may fail to remove an extension
that is also present in a **Force Install** policy.

**Impact:** In this specific configuration, the **Force Install**
mandate maintains the highest authority, preventing the surgical removal of a forced
extension via its specific ID. Broad security filters, such as **Block by
Permission** and **Block by Risk**, also remain bypassed by the **Force
Install** mandate as intended.

**Workaround:** You can To successfully remove or disable a **Force Installed**
extension while this limitation exists; You need to manually remove the extension's
ID from the **Force Install** policy list.

**B. Block By Permission: The Security Veto**

The Power of the Block by Permission rule depends son the initial strategy selected
in Section I:

|

Strategy | Rule Precedence | Functional Impact | Real-Life Example |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

**Block-First Strategy** | **Allow List Wins** | Extensions specifically allowed via an Allow List bypass the **Block by Permission** check. | **Scenario:** You block all extensions by default. To be extra safe, you also block the "Access to all website data" permission. Your Finance team needs a specific **Legacy Reporting Tool** that requires that exact permission. **Result:** You add the tool’s ID to your **Allow List**. The extension **installs and runs**. The system assumes that because you manually vetted it in a strict environment, you trust its permissions. |

|

**Allow-First Strategy** | **Block by Permission Wins.** | **Block by Permission** acts as a final gate and disables extensions even if they are on an Allow List. | **Scenario:** You allow all extensions by default. To prevent data theft, you set a **Block by Permission** for "Access to File System". A user wants to install a **Photo Editor** that is on your "Approved Apps" **Allow List** but requires that forbidden permission. **Result:** The **Block by Permission rule wins**. The extension is **disabled**. The system treats the permission block as a "final safety gate" because your overall environment is permissive. |

Notes on Block by Permission Behavior:

- If a forbidden permission **required**, the extension is
  **disabled**.
- If a forbidden permission is **optional**, the extension runs but the
  **permission is revoked**.

##### Summary Precedence Matrix (Final Lookup)

|

**Policy A (Lower Priority)** | **Policy B (Higher Priority)** | Result | Reasoning |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

Block All | Allow All | Allow List | Standard exception handling |

|

Allow All | Block by Risk | Risk Filtered | Block by Risk restricts the permissive Allow AI baseline |

|

Block by Risk | Allow List | Allow List Wins | Allow List "rescues an extension from a risk block |

|

Force Install | Block List | Removed | Deviation: Specific block removes thhe forced install |

|

Block by Permission | Force Install | Installed | Force Install is the highest authority over Permission Blocks |

|

Block by Permission | Allow List | Varies | Allow List wins in Block-First; Block by Permission wins in Allow-First. |

|

Block by Risk | Force Install | Force Install Wins | An operational mandate to install an extension ignores automated risk filters. |

##### Frequently Asked Questions

1. **What is the difference between "Block-First" and "Allow-First"
   strategies?**
   - **Block-First (Default Deny):** You start by blocking all extensions
     and then create specific "Allow List" exceptions. This is the most
     secure posture and changes how security gates (like permissions)
     behave.
   - **Allow-First (Default Permit):** You allow all extensions by default
     and use "Block by Risk" or "Block Lists" to filter out the bad ones.
     This is more flexible but requires stronger automated security
     gates.
2. **Why is my "Force Installed" extension being removed?**
   - **The Specificity Rule:** While Force Install is a high-authority
     mandate, an explicit **Block List** rule for that specific extension
     ID will remove it.
   - **Self-Healing:** If you remove the ID from the Block List, the
     extension will automatically re-install because the Force Install
     mandate is still active.
3. **How does "Block by Permission" actually affect the extension?**

   It
   depends on how the extension was coded by the developer.
   - **Mandatory Permissions:** If you block a permission the
     extension **requires** to function, the extension is
     **Disabled**.
   - **Optional Permissions:** If you block an **optional**
     permission, the extension stays **Enabled**, but that specific
     feature is **Revoked** and will not work.
4. **Can I allow an extension that is flagged as "High Risk"?** 

   **Yes (The
   Escape Hatch):** You can "rescue" a specific extension by adding its
   ID to an **Allow List** with a higher priority than your Block by Risk
   rule. This allows you to manually vet and approve a tool that the system
   would otherwise block.
5. **Why did my Allow List override the Permission Block in one group but not the
   other?** 

   It depends on your strategy:
   - In a **Block-First** setup, an **Allow List** is treated as a
     manual administrative vetting and **Wins** over permission
     blocks.
   - In an **Allow-First** setup, the **Block by Permission** gate
     is treated as a final safety net and **Wins** over the Allow
     List.
6. What happens if I have an Allow List and a Block List for the same IDs?

   **Identity Subtraction:** The system uses "Set Subtraction." A
   higher-priority Block List will "carve out" its items from a lower-priority
   Allow List.
   - *Example:* If you allow "Tools A, B, and C" but block "Tool B"
     at a higher priority, only A and C remain allowed.
7. **Does Force Install bypass the "Block by Permission" gate?**

   **Yes:** An operational **Force Install** mandate is considered a
   higher authority than a security permission gate. If you force an extension,
   the system assumes you have already reviewed and accepted its
   permissions.

---

<a id="prisma-browser-extension-bulk-extension-id-import"></a>

#### Prisma Browser Extension Bulk Extension ID Import

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-browser-extension-bulk-extension-id-import>*

Bulk Extension ID import

You can import multiple browser extension IDs at the same time to configure Allow and
Block rules in [Allowed or Blocked Extensions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-security/configure-extensions.html#configure-extensions_task-ydr_5hl_hcc) control.

In large-scale environments with hundreds or thousands of extensions, adding IDs manually
is inefficient and error-prone. This enhancement streamlines bulk configuration and
policy management by enabling CSV or plain-text uploads.

This feature provides a simple and scalable way for you to upload and manage
lists of browser extension IDs used in *Block Specific Extensions* or *Allow
Specific Extensions* policies.

The feature supports file uploads, validation, deduplication, and real-time
feedback to enhance policy accuracy and usability.

##### Requirements and Implementation Details

**Input methods**

You can add multiple extension IDs in eirher .csv or .txt formats. You can also add
extensions manually..

- **.csv file** - One extension ID per cell, one cell per row.
  - No header row
- **.txt file** - One extension per line, OR separated by commas or
  semicolons.
- **Manual input** - You can paste a list of extensions directly into the
  control field.

**File Uploader Behavior**

- Accepts files in .csv or .txt only.
- Automatically parses and displays valid entries.
- Displays validation feedback for errors, duplicates, or formatting
  issues

##### Validation Rules

Each extension ID needs to meet the standard Chrome ID format.

|

Validation Type | Rule |

| --- | --- |

|  |  |
| --- | --- |
|

Format Check | 32- character, lowercase alphanumeric string. |

|

Duplicates | Duplicate IDs are flagged with a warning and automatically deduplicated. |

|

Multiple Errors | IDs can trigger multiple validation errors (e.g., invalid + duplicate). |

|

File Errors | Invalid file type or parse failure. |

###### Actions

The following actions are supported, as part of the **Add List of Serial
Numbers** feature:

- **Clear all** - Remove all entered or parsed extension IDs.
- **Clear Individual Row** - Delete a single entry from the list.
- **Extension search**
  - Search for an extension ID before adding it to confirm validity
    or view details.
  - Display results including:
    - Extension name
    - Icon (if available)

###### Audit Logging

All bulk updates using this feature generate entries in the Audit Logs page.

|

Log Type | Description |

| --- | --- |

|  |  |
| --- | --- |
|

Rule Created/Updated | Lists all extension IDs added or modified in the policy rule for blocking or allowing extensions. |

###### Downloadable Sample Files

You can download sample files to understand the required format for uploads.

**Available Sample Files**

- **Sample csv file** - sample\_extensions.csv
- **Sample txt file**  - sample\_extensions.txt

**Included Example Data** 

|

Extension ID | Description |

| --- | --- |

|  |  |
| --- | --- |
|

aapbdbdomjkkjkaonfhkkikfgjllcleb | Google Translate |

|

kgjfgplpablkjnlkjmjdecgdpfankdle | Zoom |

---

<a id="file-types-per-category"></a>

### File Types per Category

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/administration/file-types-per-category>*

The following categories show the fie types that can be allowed or blocked when File
Upload or File Download use specific file types.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

The following categories show the fie types that can be allowed or blocked when File
Upload or File Download use specific file types.

File Types per Category

|  |  |
| --- | --- |
|

**Documents** | doc, docm, docx, dot, dotm, dotx, odt, rtf, pdf, txt, wps, xps, csv, dbf, dif, ods, prn, slk, xls, xlam, xls, xlsb, xlsm, xlsx, xlt, xltm, xltx, xlw, odp, pot, potm, potx, ppa, ppam, pps, ppsm, ppsx, ppt, pptm, pptx, thmx |

|

**Multimedia** | jpg, jpeg, bmp, png, gif, tif, svg, webp, wmf, wmv, emf, mp3, mp4, mov, m4a, m4v, mpg, mpeg, avi, flv, 3gp, 3gpp, 3g2, 3gp2 |

|

**Source Code** | a, asm, asp, awk, bat, c, class, cmd, cpp, cxx, db, def, des, dlg, dpc, dpj, dxp, h, hpp, hrc, hxx, idl, ilb, inc, java, js, jsp, l, ll, pl, pm, ps, s, scp, sh, src, y, yxx |

|

**Web Pages** | htm, html, mht, mhtml, xml, xps, xhtml, xht, shtml |

|

**Archives** | a, ar, tar, bz2, gz, lz, lz4, lzma, z, 7z, s7z, ace, b6z, kgb, lzh, lha, pea, rar, war, xar, zip, zipx, zz |

---

<a id="deploy-the-prisma-browser-via-mdm"></a>

## Deploy the Prisma Browser via MDM

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment>*

Learn about deployment methods for the Prisma Access Secure Enterprise Browser (Prisma Browser)
based on your organization’s policies and preferences. You can use self-service, MSI
installer, Jamf, or Intune.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

You can choose from a variety of deployment methods for the Prisma Browser based on your organization’s policies and preferences.

Select the method that you prefer for deployment:

- [Jamf](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-jamf.html#deploy-prisma-access-browser-using-jamf)
- [Intune](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-intune.html#deploy-prisma-access-browser-using-intune)
- [Workspace ONE](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-workplace-one.html#deploy-prisma-access-browser-using-workplace-one)
- [IGEL](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-igel.html#deploy-using-igel)
- [Linux](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-linux.html#deploy-using-linux)

## Deploy Prisma Browser Using Jamf

deploy Prisma Browser using Jamf

Jamf is a comprehensive management system for Apple macOS and iOS
devices. With Jamf, you can proactively manage the entire lifecycle of Apple
devices. This includes deploying and maintaining software, responding to
security threats, distributing settings, and analyzing inventory data.

Deploying the Prisma Browser using Jamf is easy - just follow these 2
steps.

1. Open the Jamf Dashboard and select Settings.
   1. Select Computer ManagementScripts.
   2. On the Scripts page, select New.
   3. On the New Script page, on the General tab, enter the
      Display Name - a name for the script. Use
      any name that meets your organizational requirements.
   4. Select the Script tab.

      1. Download and edit the [Installomator
         script](https://github.com/Installomator/Installomator/blob/main/Installomator.sh).
      2. Locate the line: 
         DEBUG=1, and change it to: 
         DEBUG=0.

         .
      3. Locate the label:  "owncloud".
         Enter the following script *after* this label:

         ```
         pabrowser)
             name="Prisma Access Browser"
             type="pkg"
             if [[ $(arch) != "i386" ]]; then
                 printlog "Architecture: arm64 (not i386)"
                 _archParam="arm64"
             else
                 printlog "Architecture: i386"
                 _archParam="x64"
             fi
             _appcast=$(curl -s "https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=${_archParam}&channel=packaged")
             downloadURL=$(echo "$_appcast" | grep -Eo 'url="(.*)"' | cut -d '"' -f2 | tail -n1)
             appNewVersion=$(echo "$_appcast" | grep -Eo 'sparkle:shortVersionString="(.*)"' | cut -d '"' -f2 | tail -n1)
             expectedTeamID="XZMH593AYG"
             ;;
         ```

         .
      4. Click the Options tab. Under
         Parameter 4, enter the Application
         name. Select Save.
      5. The script is saved; you can now create a new Policy.
2. Create the Policy.
   1. In the Jamf Dashboard, select ComputersPoliciesNew.
   2. On the Policies page, select New.
   3. On the New Policy page, enter the
      Display Name for the policy.
   4. Select Scripts.
   5. In the Configure Scripts field, click
      Configure.
   6. On the New Policy page, select the
      Script and click
      Add.
   7. In the Parameter Values section, select the
      Application Name field, and enter
       pabrowser.
   8. Save.

      The Script is added to the policy.

## Deploy Prisma Browser Using Intune

Learn how to deploy Prisma Access Secure Enterprise Browser (Prisma Browser) using
Intune.

Microsoft Intune is a cloud-based endpoint management solution. It manages user
access to organizational resources and simplifies app and device management
across your many devices, including mobile devices, desktop computers, and
virtual endpoints.

1. Open the Microsoft Intune Admin Center.
2. Select AppsAll apps.
3. Click + Add.
4. In the Select app type window, select Line-of-business
   app.
5. Click Select.
6. In the App information step, click Select app package
   file.
7. In the App package file window, browse to the MSI installation file, named
   *PrismaAccessBrowserSetup.msi*.
8. Click Ok.
9. Enter all the needed properties.

   1. Enter a name for the app. This will be visible
      in the Intune list and in the Company Portal.
   2. Provide a brief description of the app and its benefits
      for users. This description will be available in the Company
      Portal, where you can use rich text formatting to enhance
      it.
   3. Enter the name of the app’s publisher, which
      appears in the Company Portal.
   4. App install context – Select the Device.
   5. Show this as a featured app in the Company
      Portal – we recommend that you select Yes so that it
      will be easier for your users to find.
   6. Select the appropriate Logo for the application.

      ![]()
10. Click Next.
11. Select the Assignments for this app.

    1. For Available for enrolled devices, select Add group, and select the
       required Entra groups assigned to the application.
    2. If you select Add all users, then the Entra assignment will include
       all Entra users in your organization.
12. Click Next.
13. Review all the settings and click Create to create the new app, or
    Previous to make changes.

    Creating the app might take a few additional minutes. The application will be
    available for use after this step.

### Set Prisma Browser Mobile as the Default Browser for Intune-managed Apps

If you are using Intune to manage your deployment, you can set Prisma Browser Mobile as the default browser. Intune empowers you to set a
default browser for organization-managed apps. This can be applied globally
through App Protection Policies, or selectively for specific, critical
applications. This is particularly relevant for mobile devices (iOS and
Android), as they are often employee-owned. However, enforcing a company browser
as the default for all apps might raise employee concerns.

This requires an [Intune Plan 1](https://learn.microsoft.com/en-us/mem/intune/fundamentals/licenses#microsoft-intune-plan-1) license.

1. Browse to the Intune Admin Portal → [App Protection Policies](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/~/appProtection) → Select
   the policy you want to modify or create.
2. At the Data Protection step, select "Restrict web
   content transfer with other apps", and enter Unmanaged browser
3. (Optional) For iOS devices: In the Unmanaged browser
   protocol field, enter prisma.

   This requires Prisma Browser iOS version 1.4046 or later.
4. (Optional) For Android devices:
   1. In the Unmanaged Browser ID field, enter
      com.talonsec.talon.
   2. In the Unmanaged Browser Name field, enter
      PA Browser.
5. [More information on Intune's App
   Protection Policies](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy).

## Deploy Prisma Browser Using Workspace ONE

How to deploy the Prisma Access Browser in a Workspace ONE environment.

Workspace ONE is a digital platform that delivers and manages any app on
any device by integrating access control, application management, and unified
endpoint management. The platform allows IT to deliver a digital workspace that
includes the devices and apps of the business's choice, without sacrificing the
security and control that IT professionals need.

To deploy the Prisma Browser, follow the appropriate steps for your
operating system.

### Deploy for Windows

Create an Internal Application using the Windows Installer.

1. Download the Windows MSI Installer. The installer can be downloaded using
   the following link: [Windows Prisma Access Browser
   Installer](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsMsi).
2. In the Workspace One application, add an Internal Application with the MSI
   file.
3. In the **Details** section, enter the following:
   1. **Custom Processor Architecture** - 64-bit.
4. In the **Add Application - PrismaAccessBrowserSetup.exe v n.n.n.n**
   window, select the **Deployment Options****.**
5. Enter the following information:

   1. **Admin Privileges** - Select Yes.
6. **Save and Assign**.

### Deploy for Mac

Create an Internal Application using the macOS installer. You can download the
installer, found here: [Latest macOS Prisma Access Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller).

Using the VMware Workspace ONE Admin Assistant tool, create a package as follows
on a machine running macOS:

1. Download the latest Mac Browser from the URL ([Latest macOS Prisma Access
   Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller))
2. Use the VMware Workspace ONE Admin Assistant tool to create a
   package.
   1. On a Mac machine, download the tool from this URL: [Admin
      Assistant](https://getwsone.com/AdminAssistant/VMwareWorkspaceONEAdminAssistant.dmg)
   2. Run the tool, and drag and drop the latest Prisma Browser into
      the app.
   3. After “Parsing”, the app should produce a package containing a .DMG
      and .PLIST file.
3. Create an Internal Application using the output of the previous step.

## Deploy using IGEL

deploy PAB using IGEL

Prisma Browser installation and update over IGEL OS is performed via the **IGEL App
Portal**. For more information, refer to the [IGEL App Portal](https://app.igel.com/).

![]()

## Deploy using Linux

+---directions on deploying PAB using Linux

### Distribution Agnostic Installation

Installation of the latest version on either Ubuntu/Fedora (MD5):

eaeb2552cdffe5842debb6c8b7f5cffd):

```
curl -fsS https://updates.talon-sec.com/linux/prisma-access-browser/install.sh | sudo bash
```

### Ubuntu

Dynamic list of Prisma Browser Linux (.deb) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_deb&architecture=x64&channel=stable) . New stable versions are released on
a weekly basis and will be reflected in the list

.

**Manual/One-time Installation**

Install the package using the downloaded .deb file.

```
sudo apt install prisma-access-browser-stable_<version_number>-1_amd64.deb
```

**Package Repository (via MDM/Local)**

Create a new repository file under /etc/apt/sources.list.d

```
echo "deb [arch=amd64] https://updates.talon-sec.com/linux/prisma-access-browser/deb/ stable main" | sudo tee /etc/apt/sources.list.d/prisma-access-browser.list
```

**Import the GPG key (before using the
repository)**

```
wget -q -O - https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub | sudo tee /etc/apt/trusted.gpg.d/pab.asc >/dev/null
```

Update the package
list

```
sudo apt update
```

**Install Prisma Browser**

```
sudo apt install prisma-access-browser-stable
```

**Remove Prisma Browser**

```
sudo apt remove prisma-access-browser-stable
```

### Fedora

Dynamic list of Prisma Browser Linux (.rpm) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_rpm&architecture=x64&channel=stable) . New stable versions are released
weekly and are reflected in the list.

**Manual/One time Installation**

Install the package using the download rpm file.

```
sudo dnf install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

If
you are using sudo yum -

```
sudo yum install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

**Package Repository**

- **Create a new repository file under
  */etc/yum.repos.d/package-name.repo* with the following
  content:**

  ```
  [prisma-access-browser]
  name=prisma-access-browser
  baseurl=https://updates.talon-sec.com/linux/prisma-access-browser/rpm/stable/x86_64
  enabled=1
  gpgcheck=1
  gpgkey=https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Optionally - you can manually import the key (as is mentioned in the repo
  file**.

  ```
  sudo rpm --import https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Clear cache**

  ```
  sudo dnf clean all
  ```
- **Install the
  Package**

  ```
  sudo dnf install prisma-access-browser-stable
  ```
- **Remove the
  Package**

  ```
  sudo dnf remove prisma-access-browser-stable
  ```

---

<a id="deploy-the-prisma-browser-via-mdm-1"></a>

### Deploy the Prisma Browser via MDM

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser>*

Learn about deployment methods for the Prisma Access Secure Enterprise Browser (Prisma Browser)
based on your organization’s policies and preferences. You can use self-service, MSI
installer, Jamf, or Intune.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

You can choose from a variety of deployment methods for the Prisma Browser based on your organization’s policies and preferences.

Select the method that you prefer for deployment:

- [Jamf](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-jamf.html#deploy-prisma-access-browser-using-jamf)
- [Intune](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-intune.html#deploy-prisma-access-browser-using-intune)
- [Workspace ONE](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-workplace-one.html#deploy-prisma-access-browser-using-workplace-one)
- [IGEL](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-igel.html#deploy-using-igel)
- [Linux](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-linux.html#deploy-using-linux)

### Deploy Prisma Browser Using Jamf

deploy Prisma Browser using Jamf

Jamf is a comprehensive management system for Apple macOS and iOS
devices. With Jamf, you can proactively manage the entire lifecycle of Apple
devices. This includes deploying and maintaining software, responding to
security threats, distributing settings, and analyzing inventory data.

Deploying the Prisma Browser using Jamf is easy - just follow these 2
steps.

1. Open the Jamf Dashboard and select Settings.
   1. Select Computer ManagementScripts.
   2. On the Scripts page, select New.
   3. On the New Script page, on the General tab, enter the
      Display Name - a name for the script. Use
      any name that meets your organizational requirements.
   4. Select the Script tab.

      1. Download and edit the [Installomator
         script](https://github.com/Installomator/Installomator/blob/main/Installomator.sh).
      2. Locate the line: 
         DEBUG=1, and change it to: 
         DEBUG=0.

         .
      3. Locate the label:  "owncloud".
         Enter the following script *after* this label:

         ```
         pabrowser)
             name="Prisma Access Browser"
             type="pkg"
             if [[ $(arch) != "i386" ]]; then
                 printlog "Architecture: arm64 (not i386)"
                 _archParam="arm64"
             else
                 printlog "Architecture: i386"
                 _archParam="x64"
             fi
             _appcast=$(curl -s "https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=${_archParam}&channel=packaged")
             downloadURL=$(echo "$_appcast" | grep -Eo 'url="(.*)"' | cut -d '"' -f2 | tail -n1)
             appNewVersion=$(echo "$_appcast" | grep -Eo 'sparkle:shortVersionString="(.*)"' | cut -d '"' -f2 | tail -n1)
             expectedTeamID="XZMH593AYG"
             ;;
         ```

         .
      4. Click the Options tab. Under
         Parameter 4, enter the Application
         name. Select Save.
      5. The script is saved; you can now create a new Policy.
2. Create the Policy.
   1. In the Jamf Dashboard, select ComputersPoliciesNew.
   2. On the Policies page, select New.
   3. On the New Policy page, enter the
      Display Name for the policy.
   4. Select Scripts.
   5. In the Configure Scripts field, click
      Configure.
   6. On the New Policy page, select the
      Script and click
      Add.
   7. In the Parameter Values section, select the
      Application Name field, and enter
       pabrowser.
   8. Save.

      The Script is added to the policy.

### Deploy Prisma Browser Using Intune

Learn how to deploy Prisma Access Secure Enterprise Browser (Prisma Browser) using
Intune.

Microsoft Intune is a cloud-based endpoint management solution. It manages user
access to organizational resources and simplifies app and device management
across your many devices, including mobile devices, desktop computers, and
virtual endpoints.

1. Open the Microsoft Intune Admin Center.
2. Select AppsAll apps.
3. Click + Add.
4. In the Select app type window, select Line-of-business
   app.
5. Click Select.
6. In the App information step, click Select app package
   file.
7. In the App package file window, browse to the MSI installation file, named
   *PrismaAccessBrowserSetup.msi*.
8. Click Ok.
9. Enter all the needed properties.

   1. Enter a name for the app. This will be visible
      in the Intune list and in the Company Portal.
   2. Provide a brief description of the app and its benefits
      for users. This description will be available in the Company
      Portal, where you can use rich text formatting to enhance
      it.
   3. Enter the name of the app’s publisher, which
      appears in the Company Portal.
   4. App install context – Select the Device.
   5. Show this as a featured app in the Company
      Portal – we recommend that you select Yes so that it
      will be easier for your users to find.
   6. Select the appropriate Logo for the application.

      ![]()
10. Click Next.
11. Select the Assignments for this app.

    1. For Available for enrolled devices, select Add group, and select the
       required Entra groups assigned to the application.
    2. If you select Add all users, then the Entra assignment will include
       all Entra users in your organization.
12. Click Next.
13. Review all the settings and click Create to create the new app, or
    Previous to make changes.

    Creating the app might take a few additional minutes. The application will be
    available for use after this step.

#### Set Prisma Browser Mobile as the Default Browser for Intune-managed Apps

If you are using Intune to manage your deployment, you can set Prisma Browser Mobile as the default browser. Intune empowers you to set a
default browser for organization-managed apps. This can be applied globally
through App Protection Policies, or selectively for specific, critical
applications. This is particularly relevant for mobile devices (iOS and
Android), as they are often employee-owned. However, enforcing a company browser
as the default for all apps might raise employee concerns.

This requires an [Intune Plan 1](https://learn.microsoft.com/en-us/mem/intune/fundamentals/licenses#microsoft-intune-plan-1) license.

1. Browse to the Intune Admin Portal → [App Protection Policies](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/~/appProtection) → Select
   the policy you want to modify or create.
2. At the Data Protection step, select "Restrict web
   content transfer with other apps", and enter Unmanaged browser
3. (Optional) For iOS devices: In the Unmanaged browser
   protocol field, enter prisma.

   This requires Prisma Browser iOS version 1.4046 or later.
4. (Optional) For Android devices:
   1. In the Unmanaged Browser ID field, enter
      com.talonsec.talon.
   2. In the Unmanaged Browser Name field, enter
      PA Browser.
5. [More information on Intune's App
   Protection Policies](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy).

### Deploy Prisma Browser Using Workspace ONE

How to deploy the Prisma Access Browser in a Workspace ONE environment.

Workspace ONE is a digital platform that delivers and manages any app on
any device by integrating access control, application management, and unified
endpoint management. The platform allows IT to deliver a digital workspace that
includes the devices and apps of the business's choice, without sacrificing the
security and control that IT professionals need.

To deploy the Prisma Browser, follow the appropriate steps for your
operating system.

#### Deploy for Windows

Create an Internal Application using the Windows Installer.

1. Download the Windows MSI Installer. The installer can be downloaded using
   the following link: [Windows Prisma Access Browser
   Installer](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsMsi).
2. In the Workspace One application, add an Internal Application with the MSI
   file.
3. In the **Details** section, enter the following:
   1. **Custom Processor Architecture** - 64-bit.
4. In the **Add Application - PrismaAccessBrowserSetup.exe v n.n.n.n**
   window, select the **Deployment Options****.**
5. Enter the following information:

   1. **Admin Privileges** - Select Yes.
6. **Save and Assign**.

#### Deploy for Mac

Create an Internal Application using the macOS installer. You can download the
installer, found here: [Latest macOS Prisma Access Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller).

Using the VMware Workspace ONE Admin Assistant tool, create a package as follows
on a machine running macOS:

1. Download the latest Mac Browser from the URL ([Latest macOS Prisma Access
   Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller))
2. Use the VMware Workspace ONE Admin Assistant tool to create a
   package.
   1. On a Mac machine, download the tool from this URL: [Admin
      Assistant](https://getwsone.com/AdminAssistant/VMwareWorkspaceONEAdminAssistant.dmg)
   2. Run the tool, and drag and drop the latest Prisma Browser into
      the app.
   3. After “Parsing”, the app should produce a package containing a .DMG
      and .PLIST file.
3. Create an Internal Application using the output of the previous step.

### Deploy using IGEL

deploy PAB using IGEL

Prisma Browser installation and update over IGEL OS is performed via the **IGEL App
Portal**. For more information, refer to the [IGEL App Portal](https://app.igel.com/).

![]()

### Deploy using Linux

+---directions on deploying PAB using Linux

#### Distribution Agnostic Installation

Installation of the latest version on either Ubuntu/Fedora (MD5):

eaeb2552cdffe5842debb6c8b7f5cffd):

```
curl -fsS https://updates.talon-sec.com/linux/prisma-access-browser/install.sh | sudo bash
```

#### Ubuntu

Dynamic list of Prisma Browser Linux (.deb) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_deb&architecture=x64&channel=stable) . New stable versions are released on
a weekly basis and will be reflected in the list

.

**Manual/One-time Installation**

Install the package using the downloaded .deb file.

```
sudo apt install prisma-access-browser-stable_<version_number>-1_amd64.deb
```

**Package Repository (via MDM/Local)**

Create a new repository file under /etc/apt/sources.list.d

```
echo "deb [arch=amd64] https://updates.talon-sec.com/linux/prisma-access-browser/deb/ stable main" | sudo tee /etc/apt/sources.list.d/prisma-access-browser.list
```

**Import the GPG key (before using the
repository)**

```
wget -q -O - https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub | sudo tee /etc/apt/trusted.gpg.d/pab.asc >/dev/null
```

Update the package
list

```
sudo apt update
```

**Install Prisma Browser**

```
sudo apt install prisma-access-browser-stable
```

**Remove Prisma Browser**

```
sudo apt remove prisma-access-browser-stable
```

#### Fedora

Dynamic list of Prisma Browser Linux (.rpm) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_rpm&architecture=x64&channel=stable) . New stable versions are released
weekly and are reflected in the list.

**Manual/One time Installation**

Install the package using the download rpm file.

```
sudo dnf install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

If
you are using sudo yum -

```
sudo yum install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

**Package Repository**

- **Create a new repository file under
  */etc/yum.repos.d/package-name.repo* with the following
  content:**

  ```
  [prisma-access-browser]
  name=prisma-access-browser
  baseurl=https://updates.talon-sec.com/linux/prisma-access-browser/rpm/stable/x86_64
  enabled=1
  gpgcheck=1
  gpgkey=https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Optionally - you can manually import the key (as is mentioned in the repo
  file**.

  ```
  sudo rpm --import https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Clear cache**

  ```
  sudo dnf clean all
  ```
- **Install the
  Package**

  ```
  sudo dnf install prisma-access-browser-stable
  ```
- **Remove the
  Package**

  ```
  sudo dnf remove prisma-access-browser-stable
  ```

---

<a id="deploy-prisma-browser-using-jamf"></a>

#### Deploy Prisma Browser Using Jamf

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-jamf>*

deploy Prisma Browser using Jamf

Jamf is a comprehensive management system for Apple macOS and iOS
devices. With Jamf, you can proactively manage the entire lifecycle of Apple
devices. This includes deploying and maintaining software, responding to
security threats, distributing settings, and analyzing inventory data.

Deploying the Prisma Browser using Jamf is easy - just follow these 2
steps.

1. Open the Jamf Dashboard and select Settings.
   1. Select Computer ManagementScripts.
   2. On the Scripts page, select New.
   3. On the New Script page, on the General tab, enter the
      Display Name - a name for the script. Use
      any name that meets your organizational requirements.
   4. Select the Script tab.

      1. Download and edit the [Installomator
         script](https://github.com/Installomator/Installomator/blob/main/Installomator.sh).
      2. Locate the line: 
         DEBUG=1, and change it to: 
         DEBUG=0.

         .
      3. Locate the label:  "owncloud".
         Enter the following script *after* this label:

         ```
         pabrowser)
             name="Prisma Access Browser"
             type="pkg"
             if [[ $(arch) != "i386" ]]; then
                 printlog "Architecture: arm64 (not i386)"
                 _archParam="arm64"
             else
                 printlog "Architecture: i386"
                 _archParam="x64"
             fi
             _appcast=$(curl -s "https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=${_archParam}&channel=packaged")
             downloadURL=$(echo "$_appcast" | grep -Eo 'url="(.*)"' | cut -d '"' -f2 | tail -n1)
             appNewVersion=$(echo "$_appcast" | grep -Eo 'sparkle:shortVersionString="(.*)"' | cut -d '"' -f2 | tail -n1)
             expectedTeamID="XZMH593AYG"
             ;;
         ```

         .
      4. Click the Options tab. Under
         Parameter 4, enter the Application
         name. Select Save.
      5. The script is saved; you can now create a new Policy.
2. Create the Policy.
   1. In the Jamf Dashboard, select ComputersPoliciesNew.
   2. On the Policies page, select New.
   3. On the New Policy page, enter the
      Display Name for the policy.
   4. Select Scripts.
   5. In the Configure Scripts field, click
      Configure.
   6. On the New Policy page, select the
      Script and click
      Add.
   7. In the Parameter Values section, select the
      Application Name field, and enter
       pabrowser.
   8. Save.

      The Script is added to the policy.

---

<a id="deploy-prisma-browser-using-intune"></a>

#### Deploy Prisma Browser Using Intune

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-intune>*

Learn how to deploy Prisma Access Secure Enterprise Browser (Prisma Browser) using
Intune.

Microsoft Intune is a cloud-based endpoint management solution. It manages user
access to organizational resources and simplifies app and device management
across your many devices, including mobile devices, desktop computers, and
virtual endpoints.

1. Open the Microsoft Intune Admin Center.
2. Select AppsAll apps.
3. Click + Add.
4. In the Select app type window, select Line-of-business
   app.
5. Click Select.
6. In the App information step, click Select app package
   file.
7. In the App package file window, browse to the MSI installation file, named
   *PrismaAccessBrowserSetup.msi*.
8. Click Ok.
9. Enter all the needed properties.

   1. Enter a name for the app. This will be visible
      in the Intune list and in the Company Portal.
   2. Provide a brief description of the app and its benefits
      for users. This description will be available in the Company
      Portal, where you can use rich text formatting to enhance
      it.
   3. Enter the name of the app’s publisher, which
      appears in the Company Portal.
   4. App install context – Select the Device.
   5. Show this as a featured app in the Company
      Portal – we recommend that you select Yes so that it
      will be easier for your users to find.
   6. Select the appropriate Logo for the application.

      ![]()
10. Click Next.
11. Select the Assignments for this app.

    1. For Available for enrolled devices, select Add group, and select the
       required Entra groups assigned to the application.
    2. If you select Add all users, then the Entra assignment will include
       all Entra users in your organization.
12. Click Next.
13. Review all the settings and click Create to create the new app, or
    Previous to make changes.

    Creating the app might take a few additional minutes. The application will be
    available for use after this step.

##### Set Prisma Browser Mobile as the Default Browser for Intune-managed Apps

If you are using Intune to manage your deployment, you can set Prisma Browser Mobile as the default browser. Intune empowers you to set a
default browser for organization-managed apps. This can be applied globally
through App Protection Policies, or selectively for specific, critical
applications. This is particularly relevant for mobile devices (iOS and
Android), as they are often employee-owned. However, enforcing a company browser
as the default for all apps might raise employee concerns.

This requires an [Intune Plan 1](https://learn.microsoft.com/en-us/mem/intune/fundamentals/licenses#microsoft-intune-plan-1) license.

1. Browse to the Intune Admin Portal → [App Protection Policies](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/~/appProtection) → Select
   the policy you want to modify or create.
2. At the Data Protection step, select "Restrict web
   content transfer with other apps", and enter Unmanaged browser
3. (Optional) For iOS devices: In the Unmanaged browser
   protocol field, enter prisma.

   This requires Prisma Browser iOS version 1.4046 or later.
4. (Optional) For Android devices:
   1. In the Unmanaged Browser ID field, enter
      com.talonsec.talon.
   2. In the Unmanaged Browser Name field, enter
      PA Browser.
5. [More information on Intune's App
   Protection Policies](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy).

---

<a id="deploy-prisma-browser-using-workspace-one"></a>

#### Deploy Prisma Browser Using Workspace ONE

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-prisma-access-browser-using-workplace-one>*

How to deploy the Prisma Access Browser in a Workspace ONE environment.

Workspace ONE is a digital platform that delivers and manages any app on
any device by integrating access control, application management, and unified
endpoint management. The platform allows IT to deliver a digital workspace that
includes the devices and apps of the business's choice, without sacrificing the
security and control that IT professionals need.

To deploy the Prisma Browser, follow the appropriate steps for your
operating system.

##### Deploy for Windows

Create an Internal Application using the Windows Installer.

1. Download the Windows MSI Installer. The installer can be downloaded using
   the following link: [Windows Prisma Access Browser
   Installer](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsMsi).
2. In the Workspace One application, add an Internal Application with the MSI
   file.
3. In the **Details** section, enter the following:
   1. **Custom Processor Architecture** - 64-bit.
4. In the **Add Application - PrismaAccessBrowserSetup.exe v n.n.n.n**
   window, select the **Deployment Options****.**
5. Enter the following information:

   1. **Admin Privileges** - Select Yes.
6. **Save and Assign**.

##### Deploy for Mac

Create an Internal Application using the macOS installer. You can download the
installer, found here: [Latest macOS Prisma Access Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller).

Using the VMware Workspace ONE Admin Assistant tool, create a package as follows
on a machine running macOS:

1. Download the latest Mac Browser from the URL ([Latest macOS Prisma Access
   Browser](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=macInstaller))
2. Use the VMware Workspace ONE Admin Assistant tool to create a
   package.
   1. On a Mac machine, download the tool from this URL: [Admin
      Assistant](https://getwsone.com/AdminAssistant/VMwareWorkspaceONEAdminAssistant.dmg)
   2. Run the tool, and drag and drop the latest Prisma Browser into
      the app.
   3. After “Parsing”, the app should produce a package containing a .DMG
      and .PLIST file.
3. Create an Internal Application using the output of the previous step.

---

<a id="deploy-using-igel"></a>

#### Deploy using IGEL

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-igel>*

deploy PAB using IGEL

Prisma Browser installation and update over IGEL OS is performed via the **IGEL App
Portal**. For more information, refer to the [IGEL App Portal](https://app.igel.com/).

![]()

---

<a id="deploy-using-linux"></a>

#### Deploy using Linux

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-prisma-access-browser/deploy-using-linux>*

+---directions on deploying PAB using Linux

##### Distribution Agnostic Installation

Installation of the latest version on either Ubuntu/Fedora (MD5):

eaeb2552cdffe5842debb6c8b7f5cffd):

```
curl -fsS https://updates.talon-sec.com/linux/prisma-access-browser/install.sh | sudo bash
```

##### Ubuntu

Dynamic list of Prisma Browser Linux (.deb) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_deb&architecture=x64&channel=stable) . New stable versions are released on
a weekly basis and will be reflected in the list

.

**Manual/One-time Installation**

Install the package using the downloaded .deb file.

```
sudo apt install prisma-access-browser-stable_<version_number>-1_amd64.deb
```

**Package Repository (via MDM/Local)**

Create a new repository file under /etc/apt/sources.list.d

```
echo "deb [arch=amd64] https://updates.talon-sec.com/linux/prisma-access-browser/deb/ stable main" | sudo tee /etc/apt/sources.list.d/prisma-access-browser.list
```

**Import the GPG key (before using the
repository)**

```
wget -q -O - https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub | sudo tee /etc/apt/trusted.gpg.d/pab.asc >/dev/null
```

Update the package
list

```
sudo apt update
```

**Install Prisma Browser**

```
sudo apt install prisma-access-browser-stable
```

**Remove Prisma Browser**

```
sudo apt remove prisma-access-browser-stable
```

##### Fedora

Dynamic list of Prisma Browser Linux (.rpm) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_rpm&architecture=x64&channel=stable) . New stable versions are released
weekly and are reflected in the list.

**Manual/One time Installation**

Install the package using the download rpm file.

```
sudo dnf install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

If
you are using sudo yum -

```
sudo yum install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

**Package Repository**

- **Create a new repository file under
  */etc/yum.repos.d/package-name.repo* with the following
  content:**

  ```
  [prisma-access-browser]
  name=prisma-access-browser
  baseurl=https://updates.talon-sec.com/linux/prisma-access-browser/rpm/stable/x86_64
  enabled=1
  gpgcheck=1
  gpgkey=https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Optionally - you can manually import the key (as is mentioned in the repo
  file**.

  ```
  sudo rpm --import https://updates.talon-sec.com/linux/prisma-access-browser/linux_signing_key.pub
  ```
- **Clear cache**

  ```
  sudo dnf clean all
  ```
- **Install the
  Package**

  ```
  sudo dnf install prisma-access-browser-stable
  ```
- **Remove the
  Package**

  ```
  sudo dnf remove prisma-access-browser-stable
  ```

---

<a id="installers-and-updates"></a>

### Installers and Updates

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics>*

Learn about the Prisma Browser update mechanics.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

#### Self Service Installation

You can direct users to the self-service installer. They will need to sign in using
their SSO credentials. The self service installer is found at [http://getpabrowser.com](https://get.pabrowser.com/)

This option is available for both Windows and macOS devices.

#### Installers

The Prisma Browser supports online and offline installers for Windows, macOS, and
Linux devices. Select the operating system to search for the most appropriate
installer:cx

- [Windows](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/windows-deployment.html#windows-deployment)
- [macOS](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/macos-deployment.html#macos-deployment)
- [IGEL](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/igel-deployment.html#igel-deployment)
- [Linux](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/linux-deployment.html#linux-deployment)

### Windows Deployment

These are the Windows deployment methods

The following deployment methods are available for Windows devices:

#### 

**Online installer** is a stub lightweight stub installer that
automatically retrieves the latest version of the browser from either the Default
channel or Long-Term Support (LTS) channel, depending on the type of installer
downloaded.

**Offline installer** consists of a standalone installation file that enables
browser installation on systems without an internet connection.

|  |  |  |
| --- | --- | --- |
|

**Architecture** | **Online Installers (MSI)** | **Offline Installers (MSI)** |

|

**x64** | [Latest](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsMsi) | [Latest LTS](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsLtsMsi) | [Latest](https://releases.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=x64&channel=packaged&redirect=true) | [Version Feed](https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=x64&channel=packaged) |

|

**ARM64** | [Latest](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsArmMsi) | [Latest LTS](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsArmLtsMsi) | [Latest](https://releases.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=arm64&channel=packaged&redirect=true) | [Version Feed](https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=arm64&channel=packaged) |

#### Browser Updates

The browser follows a weekly update schedule aligned with Chrome’s release
cycle, which includes weekly security patches and a major version update with new
features approximately every month.

Administrators can select between two release channels through the
**deployment** policy:

- **Default Channel**: Receives weekly updates that include both new features
  and security patches.
- **Long-Term Support (LTS) Channel**: Receives weekly security patches and new
  Prisma Access Browser and Chromium features only during the monthly major
  version updates.

The **Deployment** policy in the management console allows customization
of the deployment delay for new features and configuration of the update enforcement
schedule.

Updates downloaded during the update process are applied at the next
browser start or restart. Active browser sessions will display a notification
prompting users to restart their browsers to apply the update.

**WINDOWS - Windows Installations with Auto-Update**

Windows installations configured with auto-update include both the browser
and an updater service agent. This agent operates independently of the browser and
is triggered by a system-level scheduled task.

- **Background Updates**: When the machine is powered on, the scheduled task
  periodically checks for new browser versions, even if no user is logged in.
- **Manual Update Check**: Users can manually trigger an update check by
  navigating to the **About** page at prisma://settings/help. If an update is
  available, the update service will notify the user and provide the option to
  install it.

### macOS Deployment

These are the macOS deployment methods

#### 

Prisma Browser supports two installation variations for macOS environments. Both
variations can be installed offline, and include a self-updating component.

|

File Type | Primary Use Case |

| --- | --- |

|  |  |
| --- | --- |
|

**PKG** | Automated deployments via MDM solutions or local admins. Preferred for enterprise environments. |

|

**DMG** | Manual installations by unprivileged end-users, BYOD. |

|

Architecture | Latest Installation | Version Feed |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**Universal** | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=standalone) |

|

**Apple Silicon** (ARM64) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=standalone) |

|

**Intel** (x64) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=standalone) |

#### Browser Updates

The browser follows a weekly update schedule aligned with Chrome’s release
cycle, which includes weekly security patches and a major version update with new
features approximately every month.

Administrators can select between two release channels through the
**deployment** policy:

- **Stable Channel** (default): Receives weekly updates that include both new
  features and security patches.
- **Long-Term Support (LTS) Channel**: Receives weekly security patches and new
  Prisma Browser and Chromium features only during the monthly major
  version updates.

The **Deployment** policy in the management console allows customization
of the deployment delay for new features and configuration of the update enforcement
schedule.

Updates downloaded during the update process are applied at the next
browser start or restart. Active browser sessions will display a notification
prompting users to restart their browsers to apply the update.

**macOS**

For macOS devices, browser updates are currently managed within the browser
context. The update process initiates only while the browser is running and operates
using the active user's permissions.

This process will be updated with the upcoming introduction of the Prisma Browser Updater for macOS.

### IGEL Deployment

This is the IGEL deployment information

Prisma Browser installation and update over IGEL OS is performed via the **IGEL App
Portal**. For more information, refer to the [IGEL App Portal](https://app.igel.com/).

![]()

### Linux Deployment

These are the Linux deployment methods

#### Distribution Agnostic Installation

Installation of the latest version on either Ubuntu/Fedora (MD5):

eaeb2552cdffe5842debb6c8b7f5cffd):

```
curl -fsS https://updates.talon-sec.com/linux/prisma-access-browser/install.sh | sudo bash
```

#### Ubuntu

Dynamic list of Prisma Browser Linux (.deb) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_deb&architecture=x64&channel=stable) . New stable versions are released on
a weekly basis and will be reflected in the list

.

**Manual/One-time Installation**

Install the package using the downloaded .deb file.

```
sudo apt install prisma-access-browser-stable_<version_number>-1_amd64.deb
```

**Remove Prisma Browser**

```
sudo apt remove prisma-access-browser-stable
```

#### Fedora

Dynamic list of Prisma Browser Linux (.rpm) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_rpm&architecture=x64&channel=stable) . New stable versions are released
weekly and are reflected in the list.

**Manual/One time Installation**

Install the package using the download rpm file.

```
sudo dnf install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

If
you are using sudo yum -

```
sudo yum install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

- **Remove the
  Package**

  ```
  sudo dnf rvemove prisma-access-browser-stable
  ```

#### Engine Updates

All versions of the browser will update the engine component automatically. These are
rolled out gradually to the entire user-base and are not configurable by policy.
This is required for browser functionality and to get the latest updates, fixes, and
policies.

---

<a id="windows-deployment"></a>

#### Windows Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/windows-deployment>*

These are the Windows deployment methods

The following deployment methods are available for Windows devices:

##### 

**Online installer** is a stub lightweight stub installer that
automatically retrieves the latest version of the browser from either the Default
channel or Long-Term Support (LTS) channel, depending on the type of installer
downloaded.

**Offline installer** consists of a standalone installation file that enables
browser installation on systems without an internet connection.

|  |  |  |
| --- | --- | --- |
|

**Architecture** | **Online Installers (MSI)** | **Offline Installers (MSI)** |

|

**x64** | [Latest](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsMsi) | [Latest LTS](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsLtsMsi) | [Latest](https://releases.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=x64&channel=packaged&redirect=true) | [Version Feed](https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=x64&channel=packaged) |

|

**ARM64** | [Latest](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsArmMsi) | [Latest LTS](https://installer.talon-sec.com/8c502beb44024f8582ed89b2a25501a6/PAB?os=windowsArmLtsMsi) | [Latest](https://releases.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=arm64&channel=packaged&redirect=true) | [Version Feed](https://releases.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=win&architecture=arm64&channel=packaged) |

##### Browser Updates

The browser follows a weekly update schedule aligned with Chrome’s release
cycle, which includes weekly security patches and a major version update with new
features approximately every month.

Administrators can select between two release channels through the
**deployment** policy:

- **Default Channel**: Receives weekly updates that include both new features
  and security patches.
- **Long-Term Support (LTS) Channel**: Receives weekly security patches and new
  Prisma Access Browser and Chromium features only during the monthly major
  version updates.

The **Deployment** policy in the management console allows customization
of the deployment delay for new features and configuration of the update enforcement
schedule.

Updates downloaded during the update process are applied at the next
browser start or restart. Active browser sessions will display a notification
prompting users to restart their browsers to apply the update.

**WINDOWS - Windows Installations with Auto-Update**

Windows installations configured with auto-update include both the browser
and an updater service agent. This agent operates independently of the browser and
is triggered by a system-level scheduled task.

- **Background Updates**: When the machine is powered on, the scheduled task
  periodically checks for new browser versions, even if no user is logged in.
- **Manual Update Check**: Users can manually trigger an update check by
  navigating to the **About** page at prisma://settings/help. If an update is
  available, the update service will notify the user and provide the option to
  install it.

---

<a id="macos-deployment"></a>

#### macOS Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/macos-deployment>*

These are the macOS deployment methods

##### 

Prisma Browser supports two installation variations for macOS environments. Both
variations can be installed offline, and include a self-updating component.

|

File Type | Primary Use Case |

| --- | --- |

|  |  |
| --- | --- |
|

**PKG** | Automated deployments via MDM solutions or local admins. Preferred for enterprise environments. |

|

**DMG** | Manual installations by unprivileged end-users, BYOD. |

|

Architecture | Latest Installation | Version Feed |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

**Universal** | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=universal&channel=standalone) |

|

**Apple Silicon** (ARM64) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=arm64&channel=standalone) |

|

**Intel** (x64) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=packaged&redirect=true) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/latest?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=standalone&redirect=true) | [PKG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=packaged) | [DMG](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=mac&architecture=x64&channel=standalone) |

##### Browser Updates

The browser follows a weekly update schedule aligned with Chrome’s release
cycle, which includes weekly security patches and a major version update with new
features approximately every month.

Administrators can select between two release channels through the
**deployment** policy:

- **Stable Channel** (default): Receives weekly updates that include both new
  features and security patches.
- **Long-Term Support (LTS) Channel**: Receives weekly security patches and new
  Prisma Browser and Chromium features only during the monthly major
  version updates.

The **Deployment** policy in the management console allows customization
of the deployment delay for new features and configuration of the update enforcement
schedule.

Updates downloaded during the update process are applied at the next
browser start or restart. Active browser sessions will display a notification
prompting users to restart their browsers to apply the update.

**macOS**

For macOS devices, browser updates are currently managed within the browser
context. The update process initiates only while the browser is running and operates
using the active user's permissions.

This process will be updated with the upcoming introduction of the Prisma Browser Updater for macOS.

---

<a id="igel-deployment"></a>

#### IGEL Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/igel-deployment>*

This is the IGEL deployment information

Prisma Browser installation and update over IGEL OS is performed via the **IGEL App
Portal**. For more information, refer to the [IGEL App Portal](https://app.igel.com/).

![]()

---

<a id="linux-deployment"></a>

#### Linux Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-update-mechanics/linux-deployment>*

These are the Linux deployment methods

##### Distribution Agnostic Installation

Installation of the latest version on either Ubuntu/Fedora (MD5):

eaeb2552cdffe5842debb6c8b7f5cffd):

```
curl -fsS https://updates.talon-sec.com/linux/prisma-access-browser/install.sh | sudo bash
```

##### Ubuntu

Dynamic list of Prisma Browser Linux (.deb) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_deb&architecture=x64&channel=stable) . New stable versions are released on
a weekly basis and will be reflected in the list

.

**Manual/One-time Installation**

Install the package using the downloaded .deb file.

```
sudo apt install prisma-access-browser-stable_<version_number>-1_amd64.deb
```

**Remove Prisma Browser**

```
sudo apt remove prisma-access-browser-stable
```

##### Fedora

Dynamic list of Prisma Browser Linux (.rpm) stable versions can be found [here](https://release-manager.us.gs.talon-sec.com/api/v1/appcast.xml?appid=%7Bdfef2477-4f0e-454b-bc0d-03ce61074e4c%7D&platform=linux_rpm&architecture=x64&channel=stable) . New stable versions are released
weekly and are reflected in the list.

**Manual/One time Installation**

Install the package using the download rpm file.

```
sudo dnf install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

If
you are using sudo yum -

```
sudo yum install prisma-access-browser-stable <version_number>-10x86_64.rpm
```

- **Remove the
  Package**

  ```
  sudo dnf rvemove prisma-access-browser-stable
  ```

---

<a id="prisma-browser-for-mobile"></a>

### Prisma Browser for Mobile

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-mobile-browser>*

This provides the information regarding the Prisma Browser for Mobile

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Prisma Browser for Mobile works with both Android and iOS devices. The
browser easily integrates with the Prisma Browser and console, allowing you and your
end users to include mobile devices in the tool sets.

The Prisma Browser and the Prisma Browser for Mobile share policy rules.
However, some controls within the policy rules can operate differently, or are not
available. For example, the **File Download** control skips the setting for specific
file extensions because it's not supported for mobile use. As a result, enabling this
setting causes the Prisma Browser for Mobile to block all file downloads.

The Prisma Browser for Mobile enables you to use the most common
functionality from the regular browser. We recommend that you create rules with the
appropriate device groups in the Scope. This will allow you to properly manage the
Mobile device users. By defining device groups for mobile devices, you can set different
rule sets to apply for all mobile devices.

#### Onboard Prisma Browser for Mobile from the Strata Cloud Manager

In the onboarding phase, you can install the Android and iOS Prisma Browser for
Mobile apps to test on your own devices before sending the links out to your users.
Once you're satisfied with your tests, you can install the relevant Android and iOS
apps and distribute the links to your users via your mobile device management (MDM)
application.

#### Install the Prisma Browser for Mobile

You can download the Prisma Browser for Mobile from the following
locations:

- iOS [App Store](https://apps.apple.com/us/app/talon-mobile/id1644868543)
- Android [Google Play](https://play.google.com/store/apps/details?id=com.talonsec.talon&pcampaignid=web_share)
- Intune for iOS [Intune for iOS](https://apps.apple.com/be/app/prisma-browser-for-intune/id6755684242)

Additionally, when you access the regular download link <https://get.pabrowser.com/> from a mobile device, the URL
directs you to the relevant app store. This means that you can send a single link to
your users, even when you don't know their particular device.

#### Create Prisma Browser for Mobile Device Groups

The Prisma Browser has a device group function that allows you to create
different groups for different devices. Groups are dynamic. For example, you can set
up groups for specific managed devices, different subsidiary devices, or
contractors. As an administrator, you can exercise a considerable amount of
flexibility in configuring the mobile device groups you need within your
organization. For example, groups meet changing business, operational, and
organizational circumstances. You can use device groups either with sign-in rules to
set the security bar for accessing Prisma Browser for Mobile, or with
posture-focused scoping for policy rules.

For more information, see [Manage Device Groups](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-devices?otp=task-hns_lt1_gcc#task-hns_lt1_gcc).

#### Configure Mobile Browser Posture Attributes

The Prisma Browser for Mobile allows you to configure the posture
requirements for your devices running the Mobile Browser in the same way that it
configures posture for your desktop and laptop devices running the Prisma Browser.

For more information on the available Mobile Browser attributes, refer to
[Configure Prisma Browser for Mobile Device
Posture Attributes](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-devices/prisma-access-browser-mobile-device-posture-attributes).

#### Configure Prisma Browser for Mobile Sign-In Rules

Along with the various policy rules, the Sign-in rules act as a security
measures. Before relying on the policy rules, the Sign-in rules serve as the first
access gatekeeper for Users and Devices.

When you create a Sign-in rule, make sure that the Scope contains the Users and User
Groups and Device Groups that are designed for the Mobile Browser.

While the Prisma Browser for Mobile's Sign-in rules are
configured the same way as the Sign-in rules for the Prisma Browser, be aware of
the following exception:

Starting with *iOS* browser version 1.4259 and
*Android* browser version 1.4260, the **Prompt** action functions as
**Block**. For all earlier versions, it functions as
**Allow**.

#### Configure Prisma Browser for Mobile Policy Rules

The Prisma Browser for Mobile has various policy rules that you can configure to
create rules as you require. The configuration process is exactly the same as for
the Prisma Browser. Some of the policy rules contain different functionality due
to the restrictions in mobile browsers.

#### Mobile Access & Data Control

Mobile Devices support Access & Data Control rules with the
following exceptions:

- The Mobile Browser does not support the **Set dialog text**
  feature that permits you to customize your text for a particular
  feature.
- The Web Access section of the rule creation process does not
  support the following features:

  - **Permission request** (a “Prompt” option) becomes a
    **Block**.
  - **Require MFA** becomes a **Block**.
  - **Pick a Label** is skipped.
- **Login restrictions** - Not supported and can be
  skipped.
- **When contains** - Not supported and can be skipped.

To see the policy rules that you can use for creating rules in the Prisma Browser
for Mobile, open the Controls page, select **Data Control**, and click
**Mobile**.

![]()

For more information on the available Control sets, refer to the following
articles:

- [File Download](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention?otp=task-wcx_qv3_hcc#task-wcx_qv3_hcc)

  The following File Download controls operate differently in the
  Prisma Browser for Mobile:
  - ∫**Allow (Protected)** - The Prisma Browser for Mobile
    will block all downloads.
  - **Block**  - The Prisma Browser for Mobile will block all
    downloads.
  - **Apply on -** When applied on specific files the Prisma
    Browser for Mobile will block all downloads.
  - **Prompt -** Selecting any prompt will block downloads.
- [File Upload](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention?otp=task-bm2_fz3_hcc#task-bm2_fz3_hcc)

  The following
  File Upload controls operate differently in the Prisma Browser for
  Mobile:

  - **Allow** - The Prisma Browser for Mobile will allow all
    uploads.
  - **Allow protected files only between the rule’s web
    applications** - The Prisma Browser for Mobile will block
    all file uploads.
  - **Allow only non-protected files** – The Prisma Browser for
    Mobile will block all file uploads.
  - **Block** – The Prisma Browser for Mobile will block all file
    uploads.
  - **Apply on:** - Select one of the following options:
    - **Any file** - The upload restrictions will apply to
      all files.
    - **Specific Files** - The Prisma Browser for Mobile
      supports file specification only for the following
      Microsoft web-apps:
      - Teams
      - Outlook
      - OneDrive for Business
      - SharePoint online

        For all other applications
        and URLs, the action will block file uploads for
        both blocking specific file uploads and allowing
        specific file uploads.

        Additionally, only
        **File size** and **File type** are
        supported. The upload restrictions will apply to
        files that meet the selected specifications (the
        rule can contain as many of these specifications
        as needed):

        - **File size** - Set the size of the
          file.
        - **File types** - set the that need to match
          this rule.
        - **File hash** - The Prisma Browser for
          Mobile will block all file uploads using File
          Hash.
        - **MIP label** - The Prisma Browser for
          Mobile will block all file uploads requiring an
          MIP label.

          - **Prompt** - Selecting any prompt will
            block all downloads.
- [Clipboard](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention?otp=task-krf_31j_hcc#task-krf_31j_hcc)

  The following Clipboard commands operate differently in the Prisma
  Browser for Mobile.

  - Cut & Paste Data out:
    - **Block (Permit only within the rule's web
      applications)** - The Prisma Browser for Mobile
      will block Copy and Paste Data out.
      - **Exclude URL address bar** – Not supported
        in Prisma Browser for Mobile. If selected, it will
        be skipped.
    - **Prompt** - The Prisma Browser for Mobile will treat
      this as **Block**. All Copy & Paste Data Out will
      be blocked.
  - Copy & Paste Data in:
    - **Prompt** - The Prisma Browser for Mobile will treat
      this as **Block**. All Copy & Paste Data In will
      be blocked.
- [Print](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention?otp=task-lql_5lj_hcc#task-lql_5lj_hcc)

  The Print control can also be used to manage
  File Downloads by printing to a PDF.
- [Screenshot](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls?otp=task-s4m_xwj_hcc#task-s4m_xwj_hcc)

  The following screenshot control operates differently in the Prisma Browser:

  - **Allow** (Protected) – The Prisma Browser for Mobile will
    block screen capture, screen recording, and screen sharing using
    video conference tools.

#### Mobile Browser Security

To see the policy rules that you can use for creating rules in the Prisma Browser
for Mobile, open the Controls page, select **Browser Security**, and click
**Mobile Browser**.

![]()

#### Mobile Browser Customization

To see the policy rules that you can use for creating rules in the Prisma Browser
for Mobile, open the Controls page, select **Browser Customization**, and
click **Mobile Browser**.

![]()

##### Prisma Browser for Mobile Troubleshooting

There is a Troubleshooting page for the Prisma Browser for Mobile. You can
find it at the following location:

- **Android** - Click 3 dots → Settings → Scroll down to Troubleshoot →
  Click Prisma Access Integration.
- **iOS** - Click 3 dots → Settings → Scroll down to Troubleshoot →
  Click Prisma Access Integration.

There are two common SSL-related issues on iOS devices:

- **Outdated Certificates**: iOS enforces certificate validity limits.
  Certificates valid for more than one year may cause SSL errors. These
  issues typically affect internal websites, not public ones. [Apple Certificate Requirements](https://support.apple.com/en-il/102028).
- **Traffic Routing with Decryption**: Routing all traffic through
  Prisma Access while SSL decryption is enabled is **not** supported.

![]()

---

<a id="prisma-browser-for-mobile-setup-using-intune"></a>

#### Prisma Browser for Mobile Setup Using Intune

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-mobile-browser/prisma-access-browser-setup-using-intune>*

This is a guide on how to set Prisma Browser mobile as a default browser for
applications that are managed by Intune MaM

This discusses how to set up Prisma Browser for Mobile using Intune.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

| - Admin access to the Intune console - : [Intune Admin   Center.](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/%7E/overview) - Existing Intune users that are part of a group |

##### Set Prisma Browser for Mobile as the Default Browser for Intune-Managed Applications

Intune enables you to set a default browser for organization-managed
apps. You can apply this globally through App Protection policy rules, or
selectively for specific, critical applications. This is relevant for mobile
devices (iOS and Android), as they are often employee-owned. However, enforcing
a company browser as the default for all apps might raise employee concerns.

Enforcing the Prisma Browser for Mobile for your Intune-managed
apps significantly enhances your organization's Data Security. You can safeguard
against phishing and identity theft by limiting how URLs are opened. You will be
minimizing the risk of exposure to malicious links by enforcing the use of the
Prisma Browser for Mobile.

Furthermore, Intune’s clipboard control adds another layer of
protection. It prevents users from copying and pasting links into unmanaged
apps. This ensures that organizational data is always accessible through trusted
and controlled applications.

In essence, designating the Prisma Browser for Mobile for Intune
apps mitigates the risks associated with phishing and other identity-based
attacks, along with data leak exposure.

##### Android Setup

###### Before you start:

Before you begin, you need the following prerequisites:

- Admin access to the Intune Console (in this document - the access
  belongs to admin@pabsandbox.com.
- Access to the [Intune Admin Center.](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/%7E/overview)

###### Setup in the Admin Center

The first step is to set the Android Enrolment profile (If it wasn’t done
previously):

1. In the Admin Center, click **Devices > Android > Android Enrolment**.
   - Set Managed Google Play.
   - For the Admin user, in the examples, we are using the name
     John.Smith@pab-lab.com.
2. Click **Apps → Android**, and then add the application that you would
   like the users to have:
   - Prisma Browser - Managed Google Play Store app.
   - Outlook - Managed Google Play Store app.
   - In the Properties section, assign the Mobile Test group so that
     the apps will be included for the user.
3. Create the default Browser policy:
   - Select **Apps →App Protection Policies → Create Policy →
     Android**
   - Target policy.
   - In the Data Protection tab, define the browser.

     The Unmanaged Browser ID should be
     com.talonsec.talon

     The Unmanaged Browser Name should be
     **prisma**.

     ![]()
   - Assign this policy to your group.

###### Android Device Setup

1. Using Google Play, download the application **Company Portal** and
   login using the user credentials.
2. In the Company Portal, select the **Device** tab, click on your
   device, and complete the work profile (You may need to do this several
   times). Your device will now have a new tab entitled **Work**. 

   ![]()
3. The **Work** tab will include all applications that were added in the
   console.
4. To test the feature, click the Outlook link. The app should open using
   the Prisma Browser.

##### Android Troubleshooting

1. If the application you added in the Admin center doesn't exist in the Play
   Store or isn't installed on the device, try syncing from the company portal
   settings.
2. If Outlook is not able to log in, try deleting the application and
   reinstalling it.
3. If the Prisma Browser does not open when you click the link and suggests
   opening another browser, reinstall the Prisma Browser Module.

##### iOS Setup

###### Before you start:

Before you begin, you need the following prerequisites:

- Admin access to the Intune Console (in this document - the access
  belongs to admin@pabsandbox.com.
- Access to the [Intune Admin Center:](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/%7E/overview)

##### Setup in the Admin Center

**Create the default Browser Policy:**

1. In the Admin Center, click **Apps > App Protection Policies > Create Policy
   > iOS**.
2. In the Data Protection tab set the Unmanaged browser protocol to
   **prisma**. 

   ![]()

   ![]()
3. Assign the policy to your groups.

###### iOS Troubleshooting

- If the application that you added in the Admin Center does not exist in
  the Apple Store or isn't installed on the device, try syncing from the
  company portal settings.
- If the Prisma Browser does not open when you click the link, and
  another browser is suggested, reinstall the Prisma Browser for
  Mobile.
- There is a Troubleshooting page for Prisma Browser for Mobile. You
  can find it at the following location - Click the three dots → Settings
  → Scroll down to Troubleshoot → click Prisma Access Integration.

There are two common SSL-related issues on iOS devices:

- **Outdated Certificates**: iOS enforces certificate validity
  limits. Certificates valid for more than one year may cause SSL
  errors. These issues typically affect internal websites, not public
  ones. Apple Certificate Requirements.
- **Traffic Routing with Decryption**: Routing all traffic through
  the enforcement point (EP) while SSL decryption is enabled is
  **not** supported.

  Since the
  Prisma Browser provides network and CDSS, SSL issues (usually
  related to decryption) are rare.

---

<a id="deploy-the-prisma-browser-extension"></a>

### Deploy the Prisma Browser Extension

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-the-prisma-access-browser-extension>*

This article describes how to deploy the popular Prisma Access Browser
Extension.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser Extension is a tool that you can install on commercial
browsers such as Google Chrome and Microsoft Edge browsers, running on Windows,
macOS, and ChromeOS Operating Systems.

IT and security teams can enhance organizational security by implementing
Prisma Browser with a hybrid strategy, using the Prisma Browser
Extension to bridge current browsing practices with advanced protections. This
approach enables employees to continue using familiar browsers while administrators
gain greater visibility and control over all browsers across the enterprise.

The extension actively monitors user activity on commercial browsers,
helping to mitigate Shadow IT risks and providing real-time phishing protection. By
centralizing visibility and allowing consistent enforcement of Security policy
rules, the Prisma Browser Extension integrates smoothly with existing tools
while guiding users to the enterprise browser when accessing sensitive
applications.

#### Supported Installation and Deployment

**Mobile device management (MDM)**

- Intune
- Jamf
- Google Workspace

**Manual installation with the supplied extension files for macOS and
Windows**

- The primary uses for manual installations are PoC and
  Installation on managed Windows devices.

##### Prisma Browser Extension Software Download

You can download the Prisma Browser Extension from the Strata Cloud Manager.

1. Open the Strata Cloud Manager, and select Workflows -> Prisma Access Setup -> Prisma
   Access BrowserConfiguration → Onboarding.
   .
2. In the **Onboard Users** section, locate Prisma Browser and
   click **View**.
3. Click Step 5 Download and Distribute.
4. Click **Deploy PABX (Prisma Browser Extension) for Streamline
   Visibility & PA Browser Enforcement**.
5. In the Generate Configurationsection, select the
   following information from the drop-downs:
   1. Identity provider (IdP) - Select the IdP
      that you use in your environment. This is the tool that
      authenticates your users. The available identity providers (IdP)
      are:

      - Okta
      - Azure
      - Google
   2. Device Management - Select the mobile
      device management (MDM) that you will use to deploy the Prisma
      Access Browser Extension to managed devices. The available MDMs
      are:

      - Jamf
      - Google Workspace
      - Windows Registry
      - Manual Deployment (local)
   3. Browser - Select the browser where the
      Prisma Browser Extension will be installed. The
      available browsers are (you can select any combination of the
      browsers listed):

      - Chrome
      - Edge
      - Safari
      - Brave
      - Arc
      - AI Browsers
        - Comet
        - Dia
        - ChatGPT Atlas

      The proper combination of these three controls will create the
      necessary files for the selected deployment method.
6. Click **Generate**.

   ![]()

##### Deploy the Prisma Browser Using PowerShell

If you need to deploy Prisma Access Browser Extension using a PowerShell
script, you need to make the following changes to the above steps.

- In Step 4, select the following options:
  - **Identity provider:** Azure.
  - **Device management:** Windows MDM.
  - **Browser:** Select the relevant browser from the list.
- Click **Generate.**

  ![]()
- Click **Download .ps1 file.**

  ![]()
- Click **Done.**
- Open Step 2 and follow the directions to set the hostname.

##### Deploy the Prisma Access Browser Extension Using Intune

Microsoft Intune™ is a cloud-based endpoint management solution. It manages
user access to organizational resources app and device management across
your many devices, including desktop and laptop computers, mobile devices,
and virtual endpoints.

For this example, we will generate a configuration with the following
parameters:

- Identity provider - Okta
- Device Management - Windows Registry
- Browser - Chrome, Edge

1. Select the parameters from the dropdown lists.
   1. Click Generate.
   2. Click Download .reg file
   3. Click Done.

   ![]()
2. Copy the generated script, and run it in Intune to identify the devices
   by hostname. Click Done.

   The script is generated according to the
   selections that you made. If you change the parameters (for example,
   adding a new browser) you will need to generate a new script and
   rerun it in Intune.

   ![]()
3. Optionally, go to the [Device Management](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-devices?otp=task-yrh_lp1_gcc#task-yrh_lp1_gcc) page to make
   sure that the new devices are displayed.

##### Manually Deploy the Prisma Browser Extension

Manual installations of Prisma Browser Extension
are primarily intended for proof of concept (PoC) purposes. The primary Prisma Browser Extension deployment will be on managed devices via a
mobile device management (MDM) platform, enabling scalable distribution to a
large number of users.

###### macOS Deployment

To manually install the Extension for iOS, follow these steps:

1. Go to System Settings, and search for
   Profiles. Approve the Profile (It will have a warning mark beside
   it) .
2. Download the extension configuration file to the extension
   PAB-install-locally.mobile.confif.
3. Go to System Settings, and search for
   Profiles. Approve the Profile (It will have a warning mark beside
   it) .
4. Restart the browser to apply the settings.
5. To install, navigate to your Download folder. Right-click and
   select Open with > Profile
   Installer.appi

   ![]()
6. Go to System Settings, and search for
   Profiles. 

   ![]()
7. Double-click the object to open the installation option. 

   ![]()
8. Click Install...
9. Follow the instructions to verify the installation. You may be
   asked to authenticate as part of the installation.
10. You will need to restart after the installation is complete. 

    ![]()
11. The Prisma Browser Extension will be visible in the browser.
    Click the extension to Connect Before Logon. 

    ![]()

###### Windows Deployment

To manually install the Extension for Windows, follow these steps:

1. Download the generated registry file. 

   ![]()
2. Install the registry file on Windows 10 or Windows 11.
   1. Double-click on the .reg file.
   2. If User Account Control is enabled, you might be asked if
      you want to allow the program to make changes to your
      computer. If it does, click **Yes**.
   3. You will be asked "Are you sure you want to continue?"
      Click **Yes**.
3. You can also manually deploy the Prisma Browser Extension by
   doing the following:
   1. Send the registry file to your users via email.
   2. Save the registry file on a shared network location.
   3. Add a command to your users' login script.
   4. Add the registry command to your command prompt.
   5. Specify the name and path of the registry file that needs
      to be copied into the registry.

   After importing the registry file on Windows machines,
   users will need to restart their browser to make sure that the
   Prisma Browser Extension installed on their browser.

---

<a id="prisma-access-browser-extension-auto-login"></a>

#### Prisma Access Browser Extension Auto Login

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-the-prisma-access-browser-extension/prisma-access-browser-extension-auto-login>*

Configure Auto Login for PABX

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The Prisma Browser Extension automatically logs users in without requiring manual
sign-ins. This feature works by integrating with supported identity providers (IdP) and
using the existing session cookies from those IdPs.

##### Prisma Browser Extension Auto-Login

The Prisma Browser Extension provides an auto-login feature that automatically
and seamlessly logs users into the system, eliminating the need for manual sign-ins.
Prisma Browser Extension achieves this by integrating with supported
Identity Providers (IdPs) and leveraging their existing session cookies. This method
significantly reduces sign-in effort for users and enhances security by centralizing
credential management at the IdP level through single sign-on (SSO).

##### How the Prisma Access Browser Extension Works

PABX initiates a login attempt every few minutes or when it detects a
change in the existing IdP session cookie. The process includes the following
steps:

- **IdP session Detection**: When a user signs in to a business
  application (such as a CRM) that integrates with their IdP, the browser
  receives a session cookie that confirms the active session.
- **Active session Verification**: During each login attempt, Prisma Browser Extension checks for valid session cookies from supported
  IdPs.
- **Domain Matching**: If Prisma Browser Extension detects an
  active session, it checks whether the user’s domain (for example,
  company.com in user@company.com)
  exists in the PABX loginDomains configuration.
- **Silent Background Login**: If the domain matches, Prisma Browser Extension silently attempts to authenticate in the
  background by accessing a configured Prisma Browser application that
  integrates with the IdP. This typically occurs when you set up the Cloud
  Identity Engine (CIE) during on-boarding.
- **Local Session Establishment**: After successful authentication, Prisma Browser Extension creates a local session and enforces policy rules
  associated with the logged-in user.

By using single sign-on (SSO), Prisma Browser Extension enables users
to access multiple systems through a single login. This reduces sign-in effort and
improves security by centralizing credential management at the IdP level.

##### Auto-Login Prerequisites

To properly enable the Auto-login feature, you need to ensure the following
configurations:

- **IdP Integration:** Integrate Prisma Browser Extension with one of
  the currently supported Identity Providers:
  - Okta
  - Azure Active Directory
  - Google Workspace

    If your organization
    uses an IdP not listed above, users must sign in manually. In
    such cases, you can enforce manual login requirements to prevent
    users from bypassing policy rule enforcement.
- **Login Domains Configuration:** Accurately configure login domains in
  Prisma Browser Extension to precisely match your users' IdP domains.
- **PAB (CIE) Application Setup:** Properly set up the Prisma Browser
  application (Cloud Identity Engine) within your chosen IdP.

###### Login Domains

Prisma Browser Extension automatically retrieves and populates login domains
from the integrated IdP. These domains (such as company.com
from user@company.com) appear under **Login Domains** on the
Prisma Browser Extension onboarding page. Confirm that these
automatically populated domains accurately match your users' email domains. If
discrepancies exist, update them directly within the onboarding tool.

###### Deploying Prisma Browser Extension

![]()

To deploy Prisma Browser Extension, follow the detailed instructions provided
in the onboarding section of the Prisma Browser management console. You can
also refer to the full deployment documentation available directly within the
console for more information.

---

<a id="removing-the-prisma-browser-extension"></a>

#### Removing the Prisma Browser Extension

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/deploy-the-prisma-access-browser-extension/removing-the-prisma-access-browser-extension>*

Instructions on removing the Prisma Access Browser Extension

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

There are times when you may need to remove the Prisma Browser Extension from
your browser. If you need to remove the extension, please refer to the following
detailed instructions:

1. JAMF Installations
   1. Open the JAMF application.
   2. Select **Configuration Profiles**.
   3. Locate the appropriate profile - it should be called **Prisma Browser Extension** profile.
2. Google Workspace Installations
   1. Navigate to **Devices → Chrome → Settings → Users and
      Browsers**.
   2. Click Organizational Units.
   3. Select the organizational unit to install the extension.
   4. Navigate to **Devices → Chrome → Apps & Extensions**.
   5. Search for *Prisma Browser Extension ID*
      (`dbpnkcjkchadgbgihmmolkjcgjkodoaf`), click it and move it using the
      Trash icon.
   6. In the confirmation pop-up, click **Delete**.
   7. Wait for the **Application deleted** message at the bottom of the
      screen for confirmation.
3. Windows MDM and Manual Installations
   1. Run the following commands:

      - Remove-Item -Path
        "HKLM:\Software\Policies\Google\Chrome\ExtensionSettings\dbpnkcjkchadgbgihmmolkjcgjkodoaf"
        -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\Google\Chrome\3rdparty\extensions\dbpnkcjkchadgbgihmmolkjcgjkodoaf"
        -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\Microsoft\Edge\ExtensionSettings
        {PABX\_EXTENSION\_ID}" -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\BraveSoftware\Brave\ExtensionSettings{PABX\_EXTENSION\_ID}"
        -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\BraveSoftware\Brave\3rdparty\extensions\dbpnkcjkchadgbgihmmolkjcgjkodoaf"
        -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\Chromium\ExtensionSettings
        {PABX\_EXTENSION\_ID}" -Force -Recurse
      - Remove-Item -Path
        "HKLM:\Software\Policies\Chromium\ExtensionSettings
        {PABX\_EXTENSION\_ID}" -Force -Recurse
4. macOS Manual Installation
   1. Go to **Settings**.
   2. Search the **Profiles**.
   3. Delete the Prisma Browser Profile (PABX)
5. For all Installation types, once you are done, please restart the browser. When
   you restart the browser, any internal files on the local system will be totally
   removed.

---

<a id="prisma-browser-end-of-life-policy"></a>

### Prisma Browser End-of-Life Policy

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-end-of-life-policy>*

Learn about the end-of-life policy for the Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

#### Release Cadence

Prisma Browser follows a structured release cycle to provide timely
updates, enhancements, and bug fixes:

The browser follows a weekly update schedule aligned with Chrome’s release cycle,
which includes weekly security patches and a major version update with new features
approximately every month.

Administrators can select between two release channels through the **deployment**
policy:

- **Stable Channel** (default): Receives weekly updates that include both
  new features and security patches.
- **Long-Term Support (LTS) Channel**: Receives weekly security patches and
  new Prisma Browser and Chromium features only during the monthly major
  version updates.

The **Deployment** policy in the management console allows customization of
the deployment delay for new features and configuration of the update enforcement
schedule.

Updates downloaded during the update process are applied at the next browser start or
restart. Active browser sessions will display a notification prompting users to
restart their browsers to apply the update.

#### End-of-Life (EoL) Policy

- Each major version of our product is supported for ninety (90) days
  from its official release date. After this period, functionality is no
  longer guaranteed and technical support might be limited. Note: The release
  date remains unchanged for customers using customized gradual releases.
- End users with EoL versions might encounter issues and difficulties
  upgrading to newer versions. To maintain security, compliance, and
  functionality, customers should plan for upgrades before the EoL stage.
- We aim to ensure the security, stability, and functionality of our
  platform. Our EoL policy is designed to help customers plan transitions and
  upgrades effectively.

  For more information, please see [Palo Alto Networks End-of-Life
  Policy](https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-policy) and [Palo Alto Networks End-of-Life
  Summary](https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary).

#### Security Updates and Functionality Guarantee

- Security Updates: We provide security patches only for the latest
  version of Prisma Browser. All nonlatest versions, regardless of age,
  don't receive security updates.
- Functionality Guarantee: We ensure that Prisma Browser core
  functionalities remain operational for versions up to 90 days from their
  official release date.
- Risks and Limitations: Customers using versions beyond the 90-day
  support period might face increased security vulnerabilities, including
  risks of malware, data breaches, and other cyberthreats. Additionally, new
  features in the management console might not function or be accessible on
  older versions.
- We strongly advise customers to regularly upgrade their browsers to
  the latest version using our autoupgrade policy. Staying informed about
  releases and maintaining the most recent version ensures your organization
  benefits from the latest security enhancements and feature improvements

#### Browser Versions

A few features in the admin management console can help administrators to
view the browser version breakdown and history:

- Homepage: The Devices widget in the management console landing page
  presents the browser versions deploy in the tenant: 

  ![]()
- Devices screen: under the Browser Version field, the devices with the EoL
  browser version marked in red: 

  ![]()
- A version breakdown exists inside the device screen.

---

<a id="prisma-browser-localization-guide"></a>

### Prisma Browser Localization Guide

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-access-browser-localization-guide>*

This document provides you with the information on switching languages where
available.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle   license or Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

This guide ensures you can configure the Prisma Browser to the language of your
choice based on the available localization support.

1. Localization Support

   The Prisma Browser supports two levels of localization.

   1. **Full Localization Support** -

      The following components are translated for languages that have full
      support:

      1. **Chromium Elements** - This includes the following elements:
         - Browser menus
         - Settings
         - Other base components
      2. **Prisma Browser-specific Elements** - This includes the
         following elements:
         - Prompts
         - Dialog
         - Policy indicators
         - Other browser-specific components
   2. **Partial Localization Support** - The translations are mostly
      automated, with limited human intervention. The following components are
      translated:

      1. Many browser elements will be in the selected language.
      2. Components specific to Prisma Browser will default to
         English (US).

      RTL languages are not supported.
2. **Fully Supported Languages** - The following languages are fully
   supported:

   Prisma Browser Supported Languages

   |

   Language | Code |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Chinese (simplified) | CN\_zh |

   |

   Chinese (traditional) | CN\_tw |

   |

   Danish | DA\_dK |

   |

   Dutch | NL\_nl |

   |

   French | FR\_fr |

   |

   German | DE\_de |

   |

   Italian | IT\_it |

   |

   Japanese | JA\_Jp |

   |

   Korean | KO\_kr |

   |

   Norwegian | NO\_nb |

   |

   Polish | PL\_pl |

   |

   Portuguese | PT\_pt |

   |

   Portuguese (Brazil) | PT\_br |

   |

   Russian | RU\_ru |

   |

   Spanish (Spain) | ES\_es |

   |

   Spanish (Latin America) | ES\_419 |

   |

   Swedish | SV\_se |

   |

   Ukrainian | UK\_ua |

   |

   Vietnamese | VI\_vn |

   ![]()

   ![]()
3. **Default Behavior**

   **If the device language is fully supported**: The browser will default to
   this language.

   **If the device language isn't fully supported**: The browser will default
   to English (US).
4. **Changing the Browser Language** 

   For **Windows**

   1. Open the Prisma Browser.
   2. Navigate to prisma://settings/languages.
   3. Under the **Browsers** section, click **Select Language**.
   4. Choose your desired language.
   5. Click **Relaunch the Browser**.

      Language changes will take effect after
      browser relaunch.

      ![]()

   For **macOS**

   1. Open the Prisma Browser.
   2. Navigate to prisma://settings/languages.
   3. Review the list of supported languages.

      - To enable partially supported languages:
        - Toggle **Allow the browser to be displayed in languages
          that are not fully supported**.
        - If the device is already set in the desired language,
          relaunch the browser. Language changes will take place
          after the relaunch.
      - To switch to a fully supported language:
        - Open your Mac device's **System Settings**.
          - Navigate to System Settings > General >
            Language and Region.
          - Alternatively, you can click **Open your
            computer's Language Settings** from the browser.
        - Scroll to the **Applications** section.
        - Click **+** to add the browser and set your preferred
          language.
        - Relaunch the browser to apply the changes.

      Language changes will take effect after
      browser relaunch.

      ![]()

---

<a id="prisma-browser-guide-to-performance-and-security-exclusions"></a>

### Prisma Browser Guide to Performance and Security Exclusions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/prisma-browser-guide-to-performance-and-security-exclusions>*

Guide to Performance and Security Exclusion

Prisma Browser operates using multiple processes and continuous read/write
operations within its profile directory. Consequently, antivirus and Endpoint Detection
and Response (EDR) tools that scan every file access or hook every process can lead to
performance degradation, such as high CPU/Disk I/O and UI lag. In some instances, these
security tools may also cause installation or update failures by blocking legitimate
browser binaries.

This guide provides IT administrators with optional exclusion paths for
Windows, macOS, and Linux. Applying these exclusions selectively can reduce scanning
overhead and improve overall browser performance.

#### Windows

Paths use environment variables: `%PROGRAMFILES%` is typically `C:\Program Files`,
and `%LOCALAPPDATA%` is the current user’s AppData Local folder. Installations may
be **system-wide** (elevated) or **per-user**; use the column that matches
your deployment.

Directories often considered for performance-oriented scan reduction

|

Area | System Level Installation | Per-user installation | Notes |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

User profile | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowser\User Data | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowser\User Data | **C**onfigurations, caches, databases; very high I/O. Strong performance impact if heavily scanned |

|

Application | %PROGRAMFILES%\Palo Alto Networks\PrismaAccessBrowser | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowser\Application |  |

|

Updated | %PROGRAMFILES%\Palo Alto Networks\PrismaAccessBrowserUpdater | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowserUpdater |  |

**Extension storage** under the profile (for example paths under `User Data` that
include `Extensions`) may be excluded for performance in some designs; that
**further reduces** visibility into extension-related files—evaluate
carefully.

Executables commonly allowlisted or trusted by path (examples)

|

Component | System-level | Per-user |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Browser | %PROGRAMFILES%\Palo Alto Networks\PrismaAccessBrowser\Application\PrismaAccessBrowser.exe | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowser\Application\PrismaAccessBrowser.exe |

|

Anti-tamper | %PROGRAMFILES%\Palo Alto Networks\PrismaAccessBrowser\Application\\*\PrismaAccessBrowserGuard.exe | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowser\Application\\*\PrismaAccessBrowserGuard.exe |

|

Update | %PROGRAMFILES%\Palo Alto Networks\PrismaAccessBrowserUpdater\<VERSION>\updater.exe | %LOCALAPPDATA%\Palo Alto Networks\PrismaAccessBrowserUpdater\<VERSION>\updater.exe |

`<VERSION>` changes with updates; where your security product allows, a **parent
directory** rule may be easier to maintain than per-version paths.
Alternatively you can use \* to target all versions.

#### macOS

|

Area | system-wide | Per-user | Notes |

| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
|

Application | /Applications/Prisma Access Browser.app/ | /Users/<user>/Library/Applications/Prisma Access Browser.app/ | Many organizations scope trust or reduced scanning to the **signed application bundle**. |

|

User-profile | /Users/<user>/Library/Application Support/PAB/Prisma Access Browser/ | /Users/<user>/Library/Application Support/PAB/Prisma Access Browser/ | Strong performance impact if heavily scanned. |

|

Updater | /Library/Application Support/PAB/PrismaAccessBrowserUpdater | ~/Library/Application Support/PAB/PrismaAccessBrowserUpdater |  |

<user> changes based on the logged in user. You can use \* to target all
versions.

#### Linux

|

Area | System-wide | Per-user |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Application | `/opt/paloaltonetworks/pab/` | Not applicable for typical system package layout |

|

User Profile | `~/.config/Palo Alto Networks/PrismaAccessBrowser` | `~/.config/Palo Alto Networks/PrismaAccessBrowser` |

---

<a id="privacy-datasheet"></a>

### Privacy Datasheet

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/privacy-datasheet>*

This topic provides a link to the Privacy Datasheet.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

The purpose of the Prisma Browser Privacy Datasheet is to provide customers of Palo
Alto Networks with information needed to assess the impact of this service on their
overall privacy posture by detailing how Personal Data is captured, processed, and
stored by and within the service.

For more information, and to see the whole document, please refer to the [Prisma Browser Privacy Datasheet](https://www.paloaltonetworks.com/resources/datasheets/prisma-browser-privacy-datasheet).

---

<a id="troubleshoot-the-prisma-browser"></a>

### Troubleshoot the Prisma Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/deployment/troubleshoot-the-prisma-access-browser>*

Troubleshoot a problematic browser installation/update

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Occasionally, some errors and issues occur when using the Prisma Browser. This
article will provide you with some common solutions to issues that may arise.

#### Installation Failures

If the Prisma Browser does not install, follow these steps to troubleshoot the
issue:

**Latest Installer Version**

- Make sure that you are using the latest version of the Prisma Browser
  Installer:
  - Visit [the Prisma Access Browser Official Download
    page](https://get.pabrowser.com).
  - Compare the version number of the installer that you have with the
    installer on the download page.
  - If the version on the download page is newer, download that installer
    and use it for installation.

**Disk Space**

- Make sure that there is sufficient disk space on the device:
  - **Windows devices:** Open File Explorer, right-click on the drive
    where you want to install Prisma Browser and select "Properties."
    Check the "Free space" section.
  - **macOS:** Click the Apple menu, select "About This Mac," and then
    click on the "Storage" tab.
- Ensure that there is sufficient space for the Prisma Browser installation
  requirements.
- If necessary, free up enough space by deleting unneeded files or moving them to
  an external memory.

**Network Accessibility**

- Make sure that the following URLs can be reached:
  - updates.talon-sec.com
  - bfe078e7921507bb.talon-sec.com
  - Check your firewall settings to make sure that these URLs are not
    blocked.
- Go to prisma/troubleshoot, open Diagnostics, and ensure that the Update service
  is up and running.

**User Privileges**

- Make sure that the active user has the correct privileges to install software.
  - If you are not sure that the installation privileges are available, try
    installing a different software package (for example Firefox, Brave,
    Chrome).

**Root Certificates (Windows only)**

Verify that the system has all required root certificates installed, mainly DigiCert
and GlobalSign:

- Open an Admin Powershell.
- Run the following
  command:

  ```
  Get-ChildItem -Path Cert:\LocalMachine\Root | Where-Object {$.Subject -like "*DigiCert Trusted Root G4*" -or $.Subject -like "*DigiCert Trusted G4 Code Signing*" -or $_.Subject -like "*GlobalSign Root R6*"} | Format-Table Subject, Thumbprint -AutoSize
  ```
- Verify the outputs of the two certificates.
- If either certificate is missing, download and install them from the official
  DigiCert and GlobalSign websites:
  - [DigiCert Root Certificates](https://www.digicert.com/kb/digicert-root-certificates.htm)
  - [GlobalSign Root Certificates](https://support.globalsign.com/ca-certificates/root-certificates/globalsign-root-certificates)
- Follow the instructions on the sites to install the certificates on your system.

  **If there are still issues, perform the following checks:** 
  - **Residual Installation Files:** Check for residues of previous
    or failed installations and delete them:
    - Terminate any running PrismaAccessBrowser processes:
      - Press CTRL+SHIFT+ESC to open the Task Manager.
      - Look for any processes named PrismaAccessBrowser\*.
      - Right-click on the process and select **End
        Task**.
    - Remove the following directories from the File Explorer:
      - %LOCALAPPDATA%\Palo Alto Networks\
      - %PROGRAMFILES(x86)%\Palo Alto Networks
      - %PROGRAMFILES%\Palo Alto Networks
    - If these directories exist, delete them.
    - Empty the Recycle Bin to ensure all residual files are
      completely removed.

**Active Security Products**

- Check the security product's logs for any entries related to Prisma Browser
  or its components.
- If any entries indicate that the installation is being blocked, follow these
  steps:
  - Open the security product's control panel.
  - Navigate to the settings or exceptions/whitelist section.
  - Add the following executables and directories to the whitelist:
  - %LOCALAPPDATA%\Palo Alto Networks\
  - %PROGRAMFILES(x86)%\Palo Alto Networks
  - %PROGRAMFILES%\Palo Alto Networks
  - Temporarily disable the security product and attempt the installation
    again to see if the issue is resolved.
  - If the installation succeeds with the security product disabled,
    re-enable the security and ensure the necessary whitelisting is in place
    to prevent future issues.

**Active Group Policies**

- Open the Group Policy Management Console"
  - Press Win + R, type gpedit.msc, and click **Enter**.
- Navigate to the following path to check for software restriction policies:
  - Computer Configuration\Administrative Templates\System
  - User Configuration\Administrative Templates\System
- Look for any policies related to software restrictions or installation
  restrictions.
- If you find any relevant policies, you should:
  - Review the policies and understand their purpose.
  - Once the installation is successful, make sure that any necessary
    exceptions are properly documented and maintained.

#### Update Issues

If Prisma Browser does not update, follow these steps to troubleshoot the
issue:

**Current Version**

- Open the Prisma Browser and navigate to prisma://settings/help.
- Check the displayed version number and compare it to the latest version number
  on the download page.
- If the numbers are the same, no update is needed.

**Network Accessibility**

- Open a web browser and try to navigate to these URLs:
  - updates.talon-sec.com
  - bfe078e7921507bb.talon-sec.com
  - Go to prisma://troubleshoot, open Diagnostics, and make sure that the
    Update service is up and running.
- If the URLs cannot be reached:
  - Check your internet connection to make sure that it s stable.
  - Check your firewall to make sure that these URLs are bot blocked. If you
    are in a corporate environment, make sure that the URLs are whitelisted.

**Omaha Client (Windows Only)**

- If the “About” page shows: "An error occurred while checking for updates: Update
  check failed to start (error code 3: 0x80040154)":
  - Open the Task Scheduler.
    - Run the command *taskschd.msc* and check for the following
      taskd:
      - PANWUpdateTaskMachineCore
      - PANWUpdateTaskMachineUA
    - If these tasks are not present, the Omaha client may not be
      installed correctly.
    - Check the following directories to see if the Omaha client
      exists:
      - %PROGRAMFILES(x86)%\Palo Alto Networks\Update
      - %LOCALAPPDATA%\Palo Alto Networks\Update
    - If the tasks or files are missing, reinstall the Omaha
      client.

**Root Certificate (Windows Only)**

- Verify that the system has all required root certificates
  installed:
  - Open the Microsoft Management Console:
    - Run the command *mmc*.
    - In MMC, go to "File" > "Add/Remove Snap-in."
    - Select "Certificates" and click "Add."
    - Choose "Computer account" and click "Next," then "Finish."
  - In the MMC console, expand "Certificates" under "Trusted Root
    Certificate Authorities."
  - Check for the following certificates:
    - DigiCert Trusted Root G4 (requires 05:9b)
    - DigiCert Trusted G4 Code Signing (requires 08)
    - GlobalSign Root R6 (starts with 45)
  - If either certificate is missing, download and install them from the
    official DigiCert and GlobalSign websites:
    - [DigiCert Root
      Certificates](https://www.digicert.com/kb/digicert-root-certificates.htm)
    - [GlobalSign Root Certificates](https://support.globalsign.com/ca-certificates/root-certificates/globalsign-root-certificates)
  - Follow the instructions on the websites to install the certificates on
    your system.

**New Version Directory**

- Open the File Explorer and navigate to the Prisma Browser Installation
  directory:
  - %PROGRAMFILES(x86)%\Palo Alto Networks
  - %LOCALAPPDATA%\Palo Alto Networks
- Look for a directory corresponding to the new version number.
- Make sure that the executables in the new version directory are properly signed.
  - Right-click on an executable.
  - Select Properties, then go to the Digital Signatures tab.
  - Ensure that the signatures are valid.
- - If files are unsigned, check for possible issues such as
    download corruption, disk errors, or security product
    interference.

**Active Security Product**

- Check the security product's logs for any entries related to Prisma Browser
  or its components.
- If any entries indicate that the update is being blocked, follow these steps:
  - Open the security product's control panel.
  - Navigate to the settings or exceptions/whitelist section.
  - Add the following executables and directories to the whitelist:
    - - Executables related to Prisma Browser.
      - Directories
        - %LOCALAPPDATA%\Palo Alto Networks\
        - %PROGRAMFILES(x86)%\Palo Alto Networks
        - %PROGRAMFILES%\Palo Alto Networks
- Temporarily disable the security product and attempt the update again to see if
  the issue is resolved.
- If the update succeeds with the security product disabled, re-enable it and
  ensure the necessary whitelisting is in place to prevent future issues.

**Network Connection**

- Test your network speed using an online speed test tool (e.g., speedtest.net).
- If the network speed is significantly lower than expected:
  - Restart your routers or modem.
  - Check to make sure that other devices on the network are not consuming
    excessive bandwidth,
  - If the issues persist, contact your Internet Service Provider.

#### Performance Issues

Extension crashes or extension settings resetting to default are frequently caused by
security products, such as Endpoint Detection and Response (EDR) or Antivirus tools,
interfering with the browser's local file operations.

**Symptoms:** 

- Extension crashes
- Extension crashes resetting to default
- Extension deployment failures due to an environmental block restricting
  write access to the local profile
- Tab crashes potentially caused by an extension

**Potential Cause (Troubleshooting Focus)**

EDR or similar tools are scanning the **extension storage paths** within the user
profile, which can block necessary read or write operations. The user profile
directories (which contain configurations, caches, and databases) have very high I/O
and can be strongly impacted if heavily scanned.

**Resolution / Mitigation**

- Evaluate excluding the extension storage paths from EDR scanning for
  improved performance and stability.
- If an environmental block is restricting write access to the local profile
  directory (%LOCALAPPDATA% on Windows), consider:
  - Removing the EDR/environment block.
  - Using the --user-data-dir flag to redirect the
    browser to a directory with guaranteed write permissions.

**Troubleshooting Version and Profile Integrity Issues**

Issues related to the browser version or session integrity can prevent successful
launch or operation.

|

Symptom | Root Cause | Action/Notes |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Startup failure on clean installation | A critical issue in a specific browser version can affect fresh (not previously installed) installations. | This requires deploying gradually and having an earlier log service. |

|

Browser re-login or user profile loss | An environmental issue is preventing the browser from verifying its internal engine, leading to a session failure or re-login. | This requires addressing the environmental read block preventing engine verification. |

|

Silent auto-update failure or installer blockages | Active security products (EDR/Antivirus) are blocking the installer or updater executables. | Refer to EDR Exclusion guidelines for updater paths. When allowing executables like updater.exe, you may need to use a **parent directory** rule or \* to target all versions, as the <VERSION> component in the path changes with updates. |

#### Browsing Issues

if there are issues when browsing using the Prisma Browser, follow thee steps to
troubleshoot the issue:

- **All Websites** 
  - **Site Functionality in Other Browsers** 
    - Open a different browser (Chrome / Edge).
    - Navigate tot he websites that are experiencing issues in Prisma Browser.
    - See if the sites load and function correctly.
    - If they do not function correctly, the issue is likely a problem
      with the websites themselves or a broader network problem.

**Firewall and Whitelisting**

- Open the firewall settings on your device:
  - **Windows:** Control Panel > System and Security > Windows Defender
    Firewall
  - **macOS:** System Preferences > Security & Privacy >
    Firewall
- Check the list of allowed applications and processes.
- Ensure that Executables related to the Prisma Browser, as well as the
  following directories are allowed through the firewall:
  - %LOCALAPPDATA%\Palo Alto Networks\
  - %PROGRAMFILES(x86)%\Palo Alto Networks
  - %PROGRAMFILES%\Palo Alto Networks
- If necessary, manually add Prisma Browser to the firewall's list of allowed
  applications.
- Examine firewall logs to find relevant clues for a block and possibly whitelist
  Prisma Browser executables and directories.

**Problematic Extensions**

- Open Prisma Browser and navigate to the extensions page:
  prisma://extensions/
- Disable all extensions.
- Try accessing the problematic websites again. If the sites work, enable the
  extensions one at a time to identify the problematic one.

#### Specific Websites

**Site Functionality in Other Browsers**

- Open a different browser (Chrome / Edge).
- Navigate tot he websites that are experiencing issues in Prisma Browser.
- See if the sites load and function correctly.
- If they do not function correctly, the issue is likely a problem with the
  websites themselves or a broader network problem.

**Filewall and Whitelisting**

- Open the firewall settings on your device:
  - **Windows:** Control Panel > System and Security > Windows Defender
    Firewall
  - **macOS:** System Preferences > Security & Privacy >
    Firewall
- Check the list of allowed applications and processes.
- Ensure that Executables related to the Prisma Browser, as well as the
  following directories are allowed through the firewall:
  - %LOCALAPPDATA%\Palo Alto Networks\
  - %PROGRAMFILES(x86)%\Palo Alto Networks
  - %PROGRAMFILES%\Palo Alto Networks
- If necessary, manually add Prisma Browser to the firewall's list of allowed
  applications.
- Examine firewall logs to find relevant clues for a block and possibly whitelist
  Prisma Browser executables and directories.

**Cross-Site Cookies**

- Open the developer tools in Prisma Browser (press Ctrl+Shift+I or F12).
- Navigate to the "Application" tab.
- Expand the "Cookies" section and check for any cross-site cookies used by the
  website.
- Ensure that Prisma Browser is configured to allow cross-site cookies:
  - Go to prisma://settings/cookies and ensure that "Block third-party
    cookies" is disabled.
- If cross-site cookies are required, add the specific sites to the list of
  allowed cookies.

**Site-Specific Configuration**

- Open the developer tools in Prisma Browser (press Ctrl+Shift+I or F12).
- Navigate to the "Network" tab.
- Reload the website and observe the network requests.
- Look for any blocked resources and note their URLs.
- Ensure that the website's configuration does not blacklist any necessary
  resources:
  - Go to prisma://settings/security and check for any site-specific
    configurations.
  - Add any necessary resources to the whitelist.

**Problematic Extensions**

- Open Prisma Browser and navigate to the extensions page:
  prisma://extensions/
- Disable all extensions.
- Try accessing the problematic websites again. If the sites work, enable the
  extensions one at a time to identify the problematic one.

**IE Mode**

- Open Prisma Browser and navigate to the problematic site.
- Check if the site is being accessed in IE mode.
- If it only works in IE but not in Prisma Browser IE mode, a feature may be
  missing.

#### Extension Issues

If there are issues with the browser extensions in the Prisma Browser, follow
these steps to troubleshoot the issue:

**Extension Functionality in Other Browsers**

- Install the extension in Chrome and Edge browsers.
- Verify that the extension functionality is consistent across both browsers.
- Note any specific differenced or issues encountered.

**NaCl Dependency**

- Open the Development Console (usually accessed by right-clicking the web page
  and selecting *Inspect* or by pressing CTRL+Shift+I).
- Look for any errors or warnings related to NaCl.
- In Chrome, some extensions may explicitly mention NaCl errors or dependencies in
  the console output.

**Desktop-Installed Services**

- Review the extension's documentation or support resources.
- Check if the extension requires any desktop-installed services or applications
  to function correctly.
- Test the extension's functionality both with and without any associated desktop
  services installed.

#### PWA Issues

If there are issues with Progressive Web Apps (PWAs) in Prisma Browser, follow
these steps to troubleshoot the issue.

**Browser Version**

- Ensure the user is running the latest version of Prisma Browser.
- Guide the user to update Prisma Browser to the latest available version if
  necessary.
- Verify if the issue persists after updating.

**PWA Installation in Other Browsers**

- Attempt to install the PWA in both Chrome and Edge browsers.
- Make sure that the installation process completes successfully without any
  errors.
- Compare the installation behavior with Prisma Browser to identify any
  discrepancies.

**Multiple Profiles**

- Inform users about the Chromium limitation affecting PWAs when there are
  multiple profiles in use.
- Explain that only one profile can utilize PWAs due to how Chromium handles app
  installations and storage.
- Advise your users to check if multiple profiles are active and recommend using
  PWAs in the profile where it is most needed.

By following these steps, you should be able to identify and resolve the most common
issues related to installation, updating, browsing, extensions, and PRWs in the Prisma Browser.

If the errors still persist, please contact Support for further assistance.

#### Authentication Issues

In some cases, the browser was not authenticating because the device ID was missing.

Chek to see that the authenticator app must be installed on the same device (iPad) ad
the Prisma Browser. If they are on the same device, the apps can communicate and
pass the Entra ID that is needed for authentication.

---

<a id="overview-what-is-the-prisma-browser"></a>

#### Overview: What is the Prisma Browser?

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-overview>*

#### **Overview: What is the Prisma Browser?**

Prisma Access Secure Enterprise Browser (Prisma Browser) secures both managed and unmanaged
devices by placing the security directly in the browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Prisma Browser standalone | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Prisma Browser is designed to enhance security for both managed and
unmanaged devices. It provides a natively integrated enterprise browser that extends
protection to unmanaged devices, helping safeguard business applications and data by
implementing security directly within the browser.

Prisma Browser supports various use-cases, including:

- **Third-Party Access:** Enables secure access to SaaS or private web applications
  for contractors, partners, consumers, or students using unmanaged devices.
- **Bring Your Own Device (BYOD) Access:** Enables secure access to SaaS or private
  web applications for contractors, partners, consumers, or students using unmanaged
  devices.
- **Temporary Secure Access:** Facilitates access to critical applications such as
  Human Resources and Payroll during system transitions like agent rollouts or network
  mergers.
- **Secure Access for Managed Devices:** Ensures protection for employees
  using work devices to handle highly sensitive data.

Designed specifically for enterprise environments, Prisma Browser incorporates
security features aimed at mitigating risks such as phishing, Malware, eavesdropping,
and data exfiltration. It retains the familiar interface and functionality of Google
Chrome while integrating additional security measures to address potential
vulnerabilities, offering a balance between usability and protection.

For more information, please see [the Prisma Access Browser page for more information.](https://www.paloaltonetworks.com/sase/prisma-access-browser)

---

<a id="prisma-browser-prerequisites"></a>

#### Prisma Browser Prerequisites

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites>*

Learn about the prerequisites for Prisma Access Secure Enterprise Browser (Prisma Browser),
including: system requirements, domains to allow, and IdP proxy requirements.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Superuser or Prisma Browser   [role](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

##### System Requirements

**Windows**

- Windows 10 64-bit - ARM (A64) is supported.

  Effective October 14, 2025, Microsoft will
  discontinue support for Windows 10. After this date, they will no longer
  provide security updates, bug fixes, technical support, or feature
  enhancements.
- Windows 11 64-bit - ARM (A64) is supported.
- No admin privileges are required

**macOS**

- macOS Monterey 12.0 or later.
- Intel x86 or Apple M1 and above
- No admin privileges are required

**Linux**

- Ubuntu 22.04.5 LTS or later
- Fedora 41 or later
- IGEL OS12 or later
- Architecture - x64

  Prisma Browser Linux
  deployment requires installation with Sudo permissions

**Android**

- Android 12 and above with all security updates

**iOS**

- iOS 18 and above.

##### For Prisma Access Customers

- Dataplane (PANOS): 10.2.9-h7, 10.2.4-h17, 10.2.10, 11.2.1
- PA Infrastructure: 5.1.1
- Panorama: 10.2.4 and above
- Cloud Services Plugin: 5.1.0-h15

##### Domains to Allow

The Prisma Browser communicates with several domains.

**SSL/TLS Inspection Requirement**

**DO NOT** enable SSL/TLS inspection for domains communicating
with the Prisma Browser.

Prisma Browser uses certificate
pinning for critical security. Network security infrastructure (Firewalls,
Proxies, VPNs) that attempts to inspect traffic acts as a
"Man-in-the-middle" by stripping the authentic Prisma Browser
certificate and replacing it with its own external certificate.

Prisma Browser is designed to immediately detect and verify
this behavior, resulting in the **termination of the connection to the
browser** to prevent a potential security breach. This action is
mandatory to maintain the integrity and security of the
browser.

**Required Action:**

These domains must be added to your SSL Decryption Exclusion list. (SSL/TLS
Bypass)

Please select your region:

- [US Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-us.html#us-region)
- [EU
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-eu.html#eu-region)
- [UK
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domain-to-allow-uk.html#uk-region)
- [JP
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-jp.html#jp-region)
- [AU
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-au.html#au-region)
- [SGP Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-sgp.html#sgp-region)
- [CA
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ca.html#ca-region)
- [CH
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ch.html#domains-to-allow-ch)
- [IN
  Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-in.html#in-region)
- [ID Region](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ind.html#ind-region)
- [Fedramp Moderate](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-fedramp-moderate.html#domains-to-allow-fedramp-moderate)

#### US Region

The following domains are for clients in the US region.

The following domains are for clients in the US region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- api.wildfire.paloaltonetworks.com
- wildfire.paloaltonetworks.com
- cie-api-proxy.us.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.talon-sec.com
- login.talon-sec.com
- ext-proxy.talon-sec.com
- classifier-auf.talon-sec.com
- assets.talon-sec.com
- auth.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-us-central1.urlcloud.paloaltonetworks.com

#### EU Region

The following domains are for clients in the EU region.

The following domains are for clients in the EU region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- de.api.wildfire.paloaltonetworks.com
- de.wildfire.paloaltonetworks.com
- cie-api-proxy.eu.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.eu.talon-sec.com
- login.eu.talon-sec.com
- ext-proxy.eu.talon-sec.com
- classifier-auf.talon-sec.com
- assets.talon-sec.com
- auth.eu.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-europe-west3.urlcloud.paloaltonetworks.com

#### UK Region

The following domains are for clients in the UK region.

The following domains are for clients in the UK region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- uk.api.wildfire.paloaltonetworks.com
- uk.wildfire.paloaltonetworks.com
- cie-api-proxy.uk.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.uk.talon-sec.com
- classifier-auf.talon-sec.com
- assets.uk.talon-sec.com
- users-assets.uk.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- https://hex-prod-europe-west2.urlcloud.paloaltonetworks.com

#### JP Region

The following domains are for clients in the JP region.

The following domains are for clients in the JP region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- jp.api.wildfire.paloaltonetworks.com
- jp.wildfire.paloaltonetworks.com
- cie-api-proxy.jp.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.jp.talon-sec.com
- classifier-auf.talon-sec.com
- assets.jp.talon-sec.com
- users-assets.jp.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-northeast1.urlcloud.paloaltonetworks.com

#### AU Region

The following domains are for clients in the AU region.

The following domains are for clients in the AU region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- au.api.wildfire.paloaltonetworks.com
- au.wildfire.paloaltonetworks.com
- cie-api-proxy.au.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.au.talon-sec.com
- classifier-auf.talon-sec.com
- assets.au.talon-sec.com
- users-assets.au.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-australia-southeast1.urlcloud.paloaltonetworks.com

#### SGP Region

The following domains are for clients in the SGP region.

The following domains are for clients in the SGP region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- sg.api.wildfire.paloaltonetworks.com
- sg.wildfire.paloaltonetworks.com
- cie-api-proxy.sg.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.sgp.talon-sec.com
- classifier-auf.talon-sec.com
- assets.sgp.talon-sec.com
- users-assets.sgp.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-southeast1.urlcloud.paloaltonetworks.com

#### CA Region

The following domains are for clients in the CA region.

The following domains are for clients in the CA region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- ca.api.wildfire.paloaltonetworks.com
- ca.wildfire.paloaltonetworks.com
- cie-api-proxy.ca.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.ca.talon-sec.com
- classifier-auf.talon-sec.com
- assets.ca.talon-sec.com
- users-assets.ca.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-northamerica-northeast1.urlcloud.paloaltonetworks.com

#### Domains to Allow-CH

Domains to allow CH region

The following domains are for clients in the CH region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- ch.api.wildfire.paloaltonetworks.com
- ch.wildfire.paloaltonetworks.com
- cie-api-proxy.ch.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.ch.talon-sec.com
- classifier-auf.talon-sec.com
- assets.ch.talon-sec.com
- users-assets..talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-europe-west1.urlcloud.paloaltonetworks.com

#### IN Region

The following domains are for clients in the IN region.

The following domains are for clients in the IN region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- in.api.wildfire.paloaltonetworks.com
- in.wildfire.paloaltonetworks.com
- cie-api-proxy.in.apps.paloaltonetworks.com
- hex-prod-asia-south1.urlcloud.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.in.talon-sec.com
- classifier-auf.talon-sec.com
- assets.in.talon-sec.com
- users-assets.in.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com

#### ID Region

The following domains are for clients in the ID region.

The following domains are for clients in the ID region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- id.api.wildfire.paloaltonetworks.com
- id.wildfire.paloaltonetworks.com
- cie-api-proxy.id.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.id.talon-sec.com
- classifier-auf.talon-sec.com
- assets.id.talon-sec.com
- users-assets.id.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-southeast2.urlcloud.paloaltonetworks.com

#### FedRAMP Moderate

The following domains are for clients in the FedRAMP Moderate domain.

The following domains are for clients in the FedRAMP Moderate domain only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- api.pubsec-cloud.wildfire.paloaltonetworks.com
- pubsec-cloud.wildfire.paloaltonetworks.com
- cie-api-proxy.gov.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.gov.talon-sec.com
- assets.gov.talon-sec.com
- users-assets.gov.talon-sec.com
- releases.talon-sec.com

Refer to the FedRAMP documentation for a complete list of
supported [FedRAMP Moderate and High FQDNs](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/fedramp-moderate-and-high-fqdns).

##### For SSO Enforcement or Private App Access

For SSO Enforcement or Private App Access, you need to white-list
**\*.prismaaccess.com**.

For SSO Enforcement, refer to [IP-Based Enforcement Using an Authentication
Gateway](https://docs.paloaltonetworks.com/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway).

##### For Prisma Access Customers Leveraging SSH/RDP/VNC Connections

\*.panwpra.com

##### Prisma Browser Ecosystem and Identity Providers

The Prisma Browser ecosystem is designed to integrate with all modern Identity
Providers (IdP), including:

- **Microsoft Entra ID**
- **Okta**
- **Google Workspace**
- **PingOne**
- **PingFederate**

The Prisma Browser does not support older
versions of ADFS. Authentication may fail if the ADFS server blocks calls to the
IdP page.

##### Required Attributes for IdP Integration

For successful synchronization of users and groups, the IdP must populate specific
attributes into the **Cloud Identity Engine (CIE)**. The following attributes are
mandatory:

- For Group Synchronization:
  - **Common-Name:** The group's display name.
  - **Unique Identifier:** The group's ObjectGUID.
- For User Synchronization:
  - **Common-Name:** The user's display name.
  - **Unique Identifier:** The user's ObjectGUID.
  - **Mail:** The user's email address.
  - **User Principal Name (UPN):** The user's UPN.

---

<a id="uk-region"></a>

##### UK Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domain-to-allow-uk>*

The following domains are for clients in the UK region.

The following domains are for clients in the UK region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- uk.api.wildfire.paloaltonetworks.com
- uk.wildfire.paloaltonetworks.com
- cie-api-proxy.uk.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.uk.talon-sec.com
- classifier-auf.talon-sec.com
- assets.uk.talon-sec.com
- users-assets.uk.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- https://hex-prod-europe-west2.urlcloud.paloaltonetworks.com

---

<a id="au-region"></a>

##### AU Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-au>*

The following domains are for clients in the AU region.

The following domains are for clients in the AU region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- au.api.wildfire.paloaltonetworks.com
- au.wildfire.paloaltonetworks.com
- cie-api-proxy.au.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.au.talon-sec.com
- classifier-auf.talon-sec.com
- assets.au.talon-sec.com
- users-assets.au.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-australia-southeast1.urlcloud.paloaltonetworks.com

---

<a id="ca-region"></a>

##### CA Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ca>*

The following domains are for clients in the CA region.

The following domains are for clients in the CA region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- ca.api.wildfire.paloaltonetworks.com
- ca.wildfire.paloaltonetworks.com
- cie-api-proxy.ca.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.ca.talon-sec.com
- classifier-auf.talon-sec.com
- assets.ca.talon-sec.com
- users-assets.ca.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-northamerica-northeast1.urlcloud.paloaltonetworks.com

---

<a id="domains-to-allow-ch"></a>

##### Domains to Allow-CH

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ch>*

Domains to allow CH region

The following domains are for clients in the CH region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- ch.api.wildfire.paloaltonetworks.com
- ch.wildfire.paloaltonetworks.com
- cie-api-proxy.ch.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.ch.talon-sec.com
- classifier-auf.talon-sec.com
- assets.ch.talon-sec.com
- users-assets..talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-europe-west1.urlcloud.paloaltonetworks.com

---

<a id="eu-region"></a>

##### EU Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-eu>*

The following domains are for clients in the EU region.

The following domains are for clients in the EU region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- de.api.wildfire.paloaltonetworks.com
- de.wildfire.paloaltonetworks.com
- cie-api-proxy.eu.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.eu.talon-sec.com
- login.eu.talon-sec.com
- ext-proxy.eu.talon-sec.com
- classifier-auf.talon-sec.com
- assets.talon-sec.com
- auth.eu.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-europe-west3.urlcloud.paloaltonetworks.com

---

<a id="fedramp-moderate"></a>

##### FedRAMP Moderate

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-fedramp-moderate>*

The following domains are for clients in the FedRAMP Moderate domain.

The following domains are for clients in the FedRAMP Moderate domain only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- api.pubsec-cloud.wildfire.paloaltonetworks.com
- pubsec-cloud.wildfire.paloaltonetworks.com
- cie-api-proxy.gov.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.gov.talon-sec.com
- assets.gov.talon-sec.com
- users-assets.gov.talon-sec.com
- releases.talon-sec.com

Refer to the FedRAMP documentation for a complete list of
supported [FedRAMP Moderate and High FQDNs](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/fedramp-moderate-and-high-fqdns).

---

<a id="in-region"></a>

##### IN Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-in>*

The following domains are for clients in the IN region.

The following domains are for clients in the IN region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- in.api.wildfire.paloaltonetworks.com
- in.wildfire.paloaltonetworks.com
- cie-api-proxy.in.apps.paloaltonetworks.com
- hex-prod-asia-south1.urlcloud.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.in.talon-sec.com
- classifier-auf.talon-sec.com
- assets.in.talon-sec.com
- users-assets.in.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com

---

<a id="id-region"></a>

##### ID Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-ind>*

The following domains are for clients in the ID region.

The following domains are for clients in the ID region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- id.api.wildfire.paloaltonetworks.com
- id.wildfire.paloaltonetworks.com
- cie-api-proxy.id.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.id.talon-sec.com
- classifier-auf.talon-sec.com
- assets.id.talon-sec.com
- users-assets.id.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-southeast2.urlcloud.paloaltonetworks.com

---

<a id="jp-region"></a>

##### JP Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-jp>*

The following domains are for clients in the JP region.

The following domains are for clients in the JP region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- jp.api.wildfire.paloaltonetworks.com
- jp.wildfire.paloaltonetworks.com
- cie-api-proxy.jp.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.jp.talon-sec.com
- classifier-auf.talon-sec.com
- assets.jp.talon-sec.com
- users-assets.jp.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-northeast1.urlcloud.paloaltonetworks.com

---

<a id="sgp-region"></a>

##### SGP Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-sgp>*

The following domains are for clients in the SGP region.

The following domains are for clients in the SGP region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- sg.api.wildfire.paloaltonetworks.com
- sg.wildfire.paloaltonetworks.com
- cie-api-proxy.sg.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.sgp.talon-sec.com
- classifier-auf.talon-sec.com
- assets.sgp.talon-sec.com
- users-assets.sgp.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-asia-southeast1.urlcloud.paloaltonetworks.com

---

<a id="us-region"></a>

##### US Region

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/prisma-access-browser-prerequisites/domains-to-allow-us>*

The following domains are for clients in the US region.

The following domains are for clients in the US region only:

- \*.talon-sec.com
- pabrowser.com
- get.pabrowser.com
- api.wildfire.paloaltonetworks.com
- wildfire.paloaltonetworks.com
- cie-api-proxy.us.apps.paloaltonetworks.com

Palo Alto Networks highly recommends that \*.talon-sec.com be
used as a network requirement. If you need to exclude specific domains, please use
the following list:

- gateway.talon-sec.com
- login.talon-sec.com
- ext-proxy.talon-sec.com
- classifier-auf.talon-sec.com
- assets.talon-sec.com
- auth.talon-sec.com
- installer.talon-sec.com
- updates.talon-sec.com
- bfe078e7921507bb.talon-sec.com
- prod.talon-sec.com
- releases.talon-sec.com
- \*.dss.paloaltonetworks.com
- hex-prod-us-central1.urlcloud.paloaltonetworks.com

---

<a id="roaming-profiles-ensuring-a-consistent-browser-experience-1"></a>

#### Roaming Profiles: Ensuring a Consistent Browser Experience

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/getting-started/set-up-roaming-profiles_0>*

Set up roaming profiles

Roaming profiles are a fundamental Windows feature that delivers a consistent
and personalized computing environment, allowing a user's browser data to follow them
across various domain-joined computers. This mechanism is network-centric, providing
data persistence without needing cloud synchronization or active internet access, which
is especially beneficial in high-security or air-gapped corporate and educational
settings.Profile Components

A roaming profile synchronizes essential user-specific browser data, ensuring
continuity regardless of the physical machine used:

- **Bookmarks and Favorites:** Web links and folder structures are
  preserved.
- **Browser Settings:** Custom configurations, including the default
  homepage, display options, and security settings, remain consistent.
- **Saved Passwords:** Encrypted login credentials are securely
  synchronized for easy access.
- **Extensions:** Installed browser add-ons are maintained to ensure
  customized functionality.
- **History:** Core browsing history is typically included, though
  caching may be managed separately for optimal performance.

##### The Local Network Synchronization Mechanism

The process by which a roaming profile enables user mobility relies on
local network server interaction:

1. **Login:** Upon signing into any Windows domain machine, the
   system identifies the user's roaming profile path on the central network
   server.
2. **Download:** The complete copy of the user's profile data is
   transferred from the server to the local computer's hard drive.
3. **Usage:** The user works with and modifies this local copy of
   the data.
4. **Logoff:** When the session ends, the operating system copies
   all changes (e.g., new bookmarks, setting modifications) back to the central
   network server, ensuring the profile is up-to-date for the next login.

##### Prisma Browser Implementation

Prisma Browser leverages this feature by storing its user-specific data in
a portable file named profile.pb. This file is located within the Windows roaming
profile folder. When a user logs onto a new machine, Windows synchronizes the entire
folder, including the profile.pb file, which allows Prisma Browser to seamlessly
restore the user's complete data.

For detailed
information on setting up Windows Roaming Profiles, see [Folder Redirection and Roaming User
Profiles overview](https://learn.microsoft.com/en-us/windows-server/storage/folder-redirection/folder-redirection-rup-overview). For step-by-step directions, see [Deploy Roaming User
Profiles](https://learn.microsoft.com/en-us/windows-server/storage/folder-redirection/deploy-roaming-user-profiles).

**Prerequisites**

To use roaming profiles, the following conditions must be met:

- Support is limited to Windows environments only
- A Windows domain environment with [Roaming User Profiles](https://learn.microsoft.com/en-us/windows-server/storage/folder-redirection/deploy-roaming-user-profiles) must
  be present
- Prisma Browser must be deployed either via MDM or local
  installation
- Users must sign in using an Active Directory account.

**Prisma Browser SetupEnable Roaming Profiles**

Set the following registry key on every machine to enable the feature:

|  |  |  |
| --- | --- | --- |
|

**\*\*Registry Path\*\*** | **\*\*Value Name\*\*** | **\*\*Value Data\*\*** |

|

Software\\Policies\\Palo Alto Networks\\PrismaAccessBrowser | RoamingProfileSupportEnabled | 1 (DWORD) |

**Change Roaming Profile Location (Optional)**[1](https://docs.google.com/document/d/1ywMGSoF7L2sJMYz0Ox624_qdbkAMEt3ThL_cCaOb74s/edit)

The user's roaming profile is stored in a file named
profile.pb. By default, this file is located in
%APPDATA%\Palo Alto Networks\PrismaAccessBrowser\User
Data\Default\profile.pb within the Windows Roaming Profile
directory.

To specify a non-default location for profile.pb,
configure the RoamingProfileLocation registry key. Any [supported path variables](https://www.chromium.org/administrators/policy-list-3/user-data-directory-variables) can be
used.

If you set the RoamingProfileLocation
policy, you must avoid setting the UserDataDir

or

DiskCacheDir

policies to the same directory.
Conflicting settings can interfere with roaming profiles and negate the
feature's benefits.

Alternatively, you can direct
RoamingProfileLocation to a network share (e.g.,
\\Server\Profiles\${user\_name}). In this configuration,
Prisma Browser reads and writes profile.pb directly to the
network, **Windows Roaming User Profiles is not required**.

**Example setup - What Syncs**

|  |  |
| --- | --- |
|

\*\* Syncs\*\* | \*\* Does Not Sync\*\* |

|

Bookmarks | Cookies |

|

Saved passwords | Active sessions |

|

Autofill data | Cached files |

|

Browser settings | Downloads |

|

Extensions | Temporary data |

|

Browsing history (partial) |  |

**Important Limitations**

|  |  |
| --- | --- |
|

\*\*Limitation\*\* | \*\*Details\*\* |

|

\*\*No simultaneous sessions\*\* | Users cannot run Prisma Browser on two machines at the same time. The profile file is locked during use. |

|

\*\*Mutually exclusive with cloud sync\*\* | Roaming profiles and browser cloud sync cannot be used together. Choose one. |

|

\*\*Single profile recommended\*\* | Multiple browser profiles may not map correctly across machines. |

|

\*\*Large profiles slow login\*\* | Thousands of bookmarks/extensions increase Windows login time. |

---

<a id="certificate-based-enforcement"></a>

#### Certificate-Based Enforcement

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/certificate-based-enforcement>*

Ensure that access to Certificate-enabled applications is only possible from the Prisma Browser

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or Prisma   Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

##### Google Workspace Certificate Enforcement

This feature ensures that access to applications
integrated with Google Workspace is only possible using the Prisma Browser.

Prisma Access comes with a dedicated Public Key Infrastructure (PKI)
used for enforcement. Once enabled, each browser is provisioned with a
dedicated, unique client certificate issued by the PKI (each tenant has a unique
root CA used to sign the client certificates). Certificate enforcement ensures
login to the identity provider is only allowed when the client certificate
signed by the dedicated root CA is provided. Renewals are generated in the
browser using a private key dedicated to each tenant. The certificate renews
automatically.

You need to set up the following prerequisites before
configuring this option:

- Google Workspace Context-Aware Access feature, available for Enterprise or
  Education accounts, or with Cloud Identity Premium.
- Setting up SSO Authentication for Prisma Access with Group.

1. Obtain the Prisma Browser Access root Certificate

   1. Go to the Prisma Browser Management Console and select
      **Administration > Integration**.
   2. Select and Enable **Google Workspace Integration**.
   3. In the first section, click **Prisma Access Certificate** to
      download the unique tenant root certificate.
2. Add the Prisma Browser Certificate to Google Workspace

   1. Go to [Google Admin Console > Devices >
      Networks](https://admin.google.com/ac/networks).
   2. Click on **Certificates**, then **Add Certificate** and upload
      the Prisma Access certificate.
   3. Check the **Endpoint Verification** option and click
      **Add**.
3. Add the Prisma Browser Certificate to Google Workspace

   1. Go to **Google Admin Console -> Security -> Access and data control
      -> Context-Aware Access**.
   2. Make sure that **Turn On** is selected.
   3. Click **Access levels**, then select **Create new access
      level.**
   4. Enter a Name for the Access Level. We recommend that you call it
      **Prisma Browsers**.
   5. Click the **Advanced** tab and paste the text found at the end of
      section 2 on the instructions on the page. The following is
      **sample**text.

      ```
      device.certificates.exists(cert,
      ```

      ```
      cert.is_valid && cert.root_ca_fingerprint ==
      ```

      ```
      "3HiBH90JUEGvo6kwGJxbkfKeD7pQAcqTzQLbCGH+t0s")
      ```
4. Assign the New Access Level to Apps

   1. Go to **Google Admin Console -> Security -> Access and data control
      -> Context-Aware Access**.
   2. Click **Assign access levels**.
   3. Select one or more apps from the list and click **Assign**.
   4. Check the newly-created **Prisma Browsers** access level (the
      name that you created in step 2, above).
5. Validation

   1. Install the Prisma Browser.
   2. Wait while the new Google Workspace configuration occurs; this
      usually takes approximately 5 minutes.
   3. Perform a successful sign-in to an assigned app from Prisma Browser. Attempt to sign - in to the same application
      from a different browser. It shouldn't succeed.

---

<a id="cloud-storage-integrations"></a>

#### Cloud Storage Integrations

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/cloud-storage-integrations>*

Describes how to integrate Microsoft One drive and Google Drive

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

| Refer to the cloud providers for their specific requirements. |

The **Save to Cloud** capability enables you to block direct file downloads to
user endpoints and instead redirect downloads to organization-managed cloud storage,
such as Microsoft OneDrive or Google Drive. This approach not only aligns with data
protection policy rules but also improves user productivity by offering smooth
access to files across devices.

##### Select between Cloud Storage and Encrypted Downloads

This section provides the guidance for selecting the appropriate method - cloud
storage or encrypted downloads - for securely distributing and accessing files,
based on specific operational and security requirements,

Cloud storage and encrypted downloads both support secure file distribution, but
each serves different use cases. The appropriate choice depends on many
different factors.

**RECOMMENDED USE CASES**

Use **Cloud Storage** when:

- **Frequent Access Is Required —** Multiple users or devices need
  regular access to the files.
- **Real-time Collaboration Is Needed —** Multiple users must view,
  edit, or comment on files simultaneously.
- **Version Control Is Required —** You need to track changes and
  maintain a history of file versions.
- **Centralized Access Control Is Important —** You can manage
  permissions and user access directly within the cloud environment.
- **Mobile or Remote Access Is Necessary —** Users require access from
  multiple locations or devices, including mobile endpoints.

Use **Encrypted Downloads** when:

- **One-Time or Limited Access Is Sufficient —** Files are intended for
  single-use or short-term local access.
- **High Security is a Priority —** Files contain sensitive information
  that must be stored locally with encryption. The files can only be
  downloaded using the browser.
- **Offline Access Is Required —** Users need to access files in
  environments without reliable internet connectivity.
- **Collaboration Isn’t Needed —** Files don’t require editing or
  sharing across users or devices.
- **Regulatory Compliance Requires Local Storage —** Certain policy
  rules or legal frameworks mandate storage outside of cloud
  platforms.

Encrypted downloads allow you to determine
where the files will exist locally, and can only be opened using the Prisma Browser. Save to Cloud allow you to move the files to any
location and is not encrypted.

You need
to configure the Cloud Storage Integrations before you select the cloud
storage providers.

The following cloud providers can be configured:

- [Microsoft
  OneDrive](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/cloud-storage-integrations/cloud-provider-microsoft-onedrive.html#cloud-provider-microsoft-onedrive)
- [Google Drive](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/cloud-storage-integrations/cloud-provider-google-drive.html#cloud-provider-google-drive)

#### Cloud Provider - Microsoft OneDrive

This document contains the directions for integrating Microsoft OneDrive as the cloud
provider

##### Microsoft OneDrive Prerequisites

These are the prerequisites for configuring Microsoft OneDrive as your cloud
provider:

- Global Administrator access in Azure Active Directory (AD)

End users require a valid Microsoft 365 license:

- Microsoft 365 Business Basic /Standard / Premium
- Microsoft 365 Apps for Business
- Microsoft 365 E3 / E5

##### Configure Microsoft OneDrive as the Cloud Provider

1. Register a new app in Azure.
   1. Sign in to the [Azure Portal](https://portal.azure.com/).
   2. Go to **Azure Active Directory → App registrations → + New
      registration**.
   3. Enter a descriptive name (for example, *Prisma Browser Cloud
      Storage for M365*)
   4. Choose **Single tenant**
      (Accounts in this organizational directory
      only).
   5. Under **Redirect URI**, select **Single-page application
      (SPA)** and use this URI:
      https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org/
   6. Click **Register**.

      ![]()
2. Add Permissions to the New App.
   1. Open the new app **→ App permissions → + Add a
      permission**.
   2. Choose **Microsoft Graph**.
   3. Add the following Application permissions:

      - Application.Read.All
      - DelegatedPermissionGrant.Read.All
   4. Click **+Add a permission → Microsoft Graph → Delegated
      permissions**.
   5. Add the following permission:

      - Files.ReadWrite.All
   6. Click **Grant admin consent for <your tenant name>** Click
      **Yes** in the consent confirmation pop-up.

      User.Read
      permission (delegated) is added by default by the
      application. DO NOT REMOVE THIS PERMISSION.

      ![]()

      ![]()

   WHY ARE THESE PERMISSIONS NEEDED?

   **Prisma Browser** requires specific permissions. These are the
   minimum necessary to ensure proper connection and to manage file
   downloads to your organization's cloud storage. This
   **least-privilege** approach minimizes security risks by only
   requesting access essential for its operation.

   |  |  |  |
   | --- | --- | --- |
   |

   **Permission Type** | **Permission Name** | **Reason** |

   |

   Delegated | User.Read | Confirms that the user connected to the browser is the same user that is connected to Microsoft. |

   |

   Delegated | Files.ReadWrite.All | Saving files to the user's OneDrive on their behalf. |

   |

   Application | Application.Read.All DelegatedPermissionGrant.Read.All | Verifies the integration configured by the Microsoft admin. |

   Admins always consent to application
   permissions. In contrast, end users consent to delegated permissions.
   Granting admin consent for delegated permissions is required. It
   prevents users from mistakenly denying permissions, which would block
   them from downloading and saving files to OneDrive when a Security
   policy is triggered.

   Verifying the onboarding status of the
   integration is critical. Improper configuration will prevent Prisma Browser from saving files to OneDrive. This will block end
   users from downloading and saving files when their download action
   matches a policy rule.
3. Generate Client Secret.
   1. Go to **Certificates & Secrets → New client secret**.
   2. In the Add a client secret tab, do the following:

      1. Enter a **description** for the secret, for example -
         Microsoft secret 01. (this field is optional.
      2. In the **Expires** field, select **730 days (24
         months)**.
   3. Click **Add**.
   4. Copy the value of the new client secret. You will need it for the
      next step when you connect the cloud storage to the Prisma Browser. We recommend that you save it in a safe place.

   ![]()
4. Connect to the Prisma Browser.
   1. Go to the Prisma Browser admin console and select
      **Integrations**.
   2. Select **Cloud Storage**.
   3. Click on either **+add provider** or **Connect your first
      provider**.

      ![]()
   4. Select the provider - **Microsoft**.
   5. Insert a descriptive **Storage name** for the connection, for
      example - *Microsoft Cloud Storage*.

      ![]()
   6. Paste the **Client secret** that you generated in the previous
      step.
   7. Enter the Application (client) ID and the Directory (tenant) ID
      from the Application Overview in the Azure Portal.
   8. Click **Test provider connection** to verify the connection with
      Azure.
   9. Once the test is successful, click **Add Provider**.
5. Create the Save to Cloud Rule
   1. Open the **Access & Data Control** rules and create a new
      rule.
   2. At the **Data Control** step, select **File Download**.
   3. Select **Save to organization storage** and choose the provider
      that you configured in the previous step.
   4. Add any additional details, and click **Set**.

##### Known Limitations and Requirements

To successfully use Save to Cloud, users must meet the following conditions:

- **Microsoft 365 Licensing:** The policy must apply only to users who
  hold a valid Microsoft 365 license that includes access to OneDrive and
  the Office suite.
- **Email Consistency:** The email address used to sign into the
  browser must match the Microsoft account associated with the user’s
  OneDrive. This prevents accidental data leakage or cross-account DLP
  violations.
- **Microsoft Sign-In Required:** Users must be signed into their
  Microsoft account. If not already authenticated, they will be prompted
  to log in, with the browser providing a username hint to streamline the
  process.

HTML sites will be compressed using zip format and saved
in a folder. The Prisma Browser does not support unzipping files. As a result,
this is not recommended.

#### Cloud Provider - Google Drive

This document contains the directions for integrating Google Drive as the cloud
provider

##### Google Drive Prerequisites

These are the prerequisites for configuring Google Drive as your cloud provider:

- Super Admin role in the Google Workspace Admin Console.
- Role on a Google Cloud Platform (GCP) project. You need one of the following
  toles:
  - **Service Account Creator**
    (roles/iam.serviceAccountCreator)
  - **Service Account Key Admin**
    (roles/iam.serviceAccountKeyAdmin)
  - **Service Usage Admin**
    (roles/serviceusage.serviceUsageAdmin)
  - **Project Editor** role (roles/editor)

End users require a valid Google Workspace License. The supported SKUs include:

- Google Workspace Business Starter
- Google Workspace Business Standard
- Google Workspace Business Plus
- Google Workspace Enterprise Standard
- Google Workspace Enterprise Plus

##### Configure Google Drive as the Cloud Provider

This document outlines the steps required to onboard Google Drive as a cloud
Storage Provider for use with Prisma Browser’s **Save to Cloud** feature.
This process involves configuring access through Google Cloud Platform (GCP) and
delegating domain-wide authority in the Google Workspace Admin Console.

1. Enable the Google Drive API in GCP.
   1. Open a browser tab and navigate to the Google Cloud Console.
   2. **Select or create** a project that will be used for the
      integration.
   3. In the left side menu, go to **APIs & Services → Enabled APIs
      and Services**.
   4. Click Enable **APIs & Services**.

      ![]()
   5. Select **Google Drive API** and click **Enable** on the
      details page. 

      ![]()
2. The Service Account allows the browser to upload
   files by generating a one-time token per upload, eliminating the need for
   the user to log in each time.

   Create a Service Account.
   1. In the **Google Cloud Console**, go to the project you selected
      in the previous step.
   2. Navigate to **IAM & Admin** and select **Service
      Accounts**.
   3. Click **+ Create service account**.

      1. Enter a Service account name. This name will be displayed in
         the Google Cloud Console.
      2. Click **Create** and continue to generate the Service
         account ID. You can edit it, if needed.
      3. Optionally, enter a Service Account description.
      4. Click **Done**.

         ![]()
   4. Continue through the steps until the service account is created.
3. Generate a Private Key (JSON)
   1. Locate your newly-created service account in the list.
   2. Click the  **More (⋮)** icon under the Actions field, and select
      Manage Keys. 

      ![]()
   3. Click **ADD KEY** → **Create new key**. 

      ![]()
   4. Choose **JSON** as the key type and click **Create**.

      ![]()
   5. The system downloads a private key file to your computer. **Store
      this file securely**; it authenticates the service
      account.
4. Retrieve the Client ID
   1. Go back to the **Service Accounts** page in the Cloud
      Console.
   2. Click the name of your service account to open its details.
   3. Under the **Details** tab, locate the **Client ID** and copy
      it. You will use this in the next step.

      ![]()
5. Delegate Domain-Wide Authority in Google Workspace.
   1. Open a browser and navigate to the[**Google Admin Console**](https://admin.google.com).
   2. Sign in using a **Super Admin** account.
   3. From the left-hand menu, go to **Security** → **API
      Controls**.
   4. Scroll to the **Domain-wide delegation** section and click
      **Manage Domain Wide Delegation**. 

      ![]()
   5. Click **Add new** to add a new Client ID.
   6. In the **Client ID** field, paste the ID you copied from your
      service account.

      In the **OAuth Scopes** field (comma-delimited), enter the
      following scopes:
      - https://www.googleapis.com/auth/drive.file
      - https://www.googleapis.com/auth/drive.metadata.readonly
   7. These scopes allow the service account to access and manage Google
      Drive files on behalf of users within the domain. 

      ![]()
   8. Click **Authorize** to complete the delegation process.

      **Why are the Scopes required?**

      ​​These scopes adhere to the principle of least privilege,
      ensuring the application only has the permissions required to
      perform its core functions — securing connections and managing
      file downloads effectively to the organizational cloud.
   9. These scopes allow the service account to access and manage Drive
      files on behalf of users within the domain.

      |  |  |
      | --- | --- |
      |

      drive.metadata.readonly | Used to list folders in the user's drive |

      |

      drive.file | Used to upload files to the user's drive |

      By using **domain-wide delegation**,
      Prisma Browser can upload files to an end-user's Google
      Drive without any user interaction. This process leverages the
      user's browser sign-in context, eliminating the need for them to
      be actively signed into Google.

      For security, Prisma Browser uses a
      **short-lived access token** to upload files to Google
      Drive. This token is created only when a file download triggers
      a matching cloud storage rule and is strictly scoped to the
      signed-in user, which prevents extensive access.
6. Create the integration with the Prisma Browser Console.
   1. Go to the Prisma Browser admin console and select
      **Integrations**.
   2. Select **Cloud Storage**.
   3. Click on either **+add provider** or **Connect your first
      provider**.

      ![]()
   4. Select **Google**.
   5. Insert a descriptive name for connection; for example, your Google
      tenant name.
   6. Upload the JSON file.
   7. Enter an email to verify permissions.

      - This step secures your organization’s data and enhances
        user productivity by integrating with your managed cloud
        storage services. Instead of allowing direct file
        downloads to user devices, our **'Save to Cloud'**
        feature automatically redirects them to your
        organization’s cloud storage.

        This method ensures that you can enforce your data
        protection policies and give users seamless access to
        their files across all their devices, which supports
        better collaboration and a smoother workflow.
      - To ensure that you have configured the permissions
        correctly, you must use the email of an active, licensed
        user in your organization. The system uses this email solely
        for a permissions check; it **will not** send emails or
        upload any files to the account.
   8. Click **Test provider connection** to verify the connection with
      Google.
   9. Once the test is successful, click **Add Provider**.

##### Known Limitation

HTML sites will be compressed using zip format and saved
in a folder. The Prisma Browser does not support unzipping files. As a result,
this is not recommended.

---

<a id="cloud-provider-google-drive"></a>

##### Cloud Provider - Google Drive

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/cloud-storage-integrations/cloud-provider-google-drive>*

This document contains the directions for integrating Google Drive as the cloud
provider

###### Google Drive Prerequisites

These are the prerequisites for configuring Google Drive as your cloud provider:

- Super Admin role in the Google Workspace Admin Console.
- Role on a Google Cloud Platform (GCP) project. You need one of the following
  toles:
  - **Service Account Creator**
    (roles/iam.serviceAccountCreator)
  - **Service Account Key Admin**
    (roles/iam.serviceAccountKeyAdmin)
  - **Service Usage Admin**
    (roles/serviceusage.serviceUsageAdmin)
  - **Project Editor** role (roles/editor)

End users require a valid Google Workspace License. The supported SKUs include:

- Google Workspace Business Starter
- Google Workspace Business Standard
- Google Workspace Business Plus
- Google Workspace Enterprise Standard
- Google Workspace Enterprise Plus

###### Configure Google Drive as the Cloud Provider

This document outlines the steps required to onboard Google Drive as a cloud
Storage Provider for use with Prisma Browser’s **Save to Cloud** feature.
This process involves configuring access through Google Cloud Platform (GCP) and
delegating domain-wide authority in the Google Workspace Admin Console.

1. Enable the Google Drive API in GCP.
   1. Open a browser tab and navigate to the Google Cloud Console.
   2. **Select or create** a project that will be used for the
      integration.
   3. In the left side menu, go to **APIs & Services → Enabled APIs
      and Services**.
   4. Click Enable **APIs & Services**.

      ![]()
   5. Select **Google Drive API** and click **Enable** on the
      details page. 

      ![]()
2. The Service Account allows the browser to upload
   files by generating a one-time token per upload, eliminating the need for
   the user to log in each time.

   Create a Service Account.
   1. In the **Google Cloud Console**, go to the project you selected
      in the previous step.
   2. Navigate to **IAM & Admin** and select **Service
      Accounts**.
   3. Click **+ Create service account**.

      1. Enter a Service account name. This name will be displayed in
         the Google Cloud Console.
      2. Click **Create** and continue to generate the Service
         account ID. You can edit it, if needed.
      3. Optionally, enter a Service Account description.
      4. Click **Done**.

         ![]()
   4. Continue through the steps until the service account is created.
3. Generate a Private Key (JSON)
   1. Locate your newly-created service account in the list.
   2. Click the  **More (⋮)** icon under the Actions field, and select
      Manage Keys. 

      ![]()
   3. Click **ADD KEY** → **Create new key**. 

      ![]()
   4. Choose **JSON** as the key type and click **Create**.

      ![]()
   5. The system downloads a private key file to your computer. **Store
      this file securely**; it authenticates the service
      account.
4. Retrieve the Client ID
   1. Go back to the **Service Accounts** page in the Cloud
      Console.
   2. Click the name of your service account to open its details.
   3. Under the **Details** tab, locate the **Client ID** and copy
      it. You will use this in the next step.

      ![]()
5. Delegate Domain-Wide Authority in Google Workspace.
   1. Open a browser and navigate to the[**Google Admin Console**](https://admin.google.com).
   2. Sign in using a **Super Admin** account.
   3. From the left-hand menu, go to **Security** → **API
      Controls**.
   4. Scroll to the **Domain-wide delegation** section and click
      **Manage Domain Wide Delegation**. 

      ![]()
   5. Click **Add new** to add a new Client ID.
   6. In the **Client ID** field, paste the ID you copied from your
      service account.

      In the **OAuth Scopes** field (comma-delimited), enter the
      following scopes:
      - https://www.googleapis.com/auth/drive.file
      - https://www.googleapis.com/auth/drive.metadata.readonly
   7. These scopes allow the service account to access and manage Google
      Drive files on behalf of users within the domain. 

      ![]()
   8. Click **Authorize** to complete the delegation process.

      **Why are the Scopes required?**

      ​​These scopes adhere to the principle of least privilege,
      ensuring the application only has the permissions required to
      perform its core functions — securing connections and managing
      file downloads effectively to the organizational cloud.
   9. These scopes allow the service account to access and manage Drive
      files on behalf of users within the domain.

      |  |  |
      | --- | --- |
      |

      drive.metadata.readonly | Used to list folders in the user's drive |

      |

      drive.file | Used to upload files to the user's drive |

      By using **domain-wide delegation**,
      Prisma Browser can upload files to an end-user's Google
      Drive without any user interaction. This process leverages the
      user's browser sign-in context, eliminating the need for them to
      be actively signed into Google.

      For security, Prisma Browser uses a
      **short-lived access token** to upload files to Google
      Drive. This token is created only when a file download triggers
      a matching cloud storage rule and is strictly scoped to the
      signed-in user, which prevents extensive access.
6. Create the integration with the Prisma Browser Console.
   1. Go to the Prisma Browser admin console and select
      **Integrations**.
   2. Select **Cloud Storage**.
   3. Click on either **+add provider** or **Connect your first
      provider**.

      ![]()
   4. Select **Google**.
   5. Insert a descriptive name for connection; for example, your Google
      tenant name.
   6. Upload the JSON file.
   7. Enter an email to verify permissions.

      - This step secures your organization’s data and enhances
        user productivity by integrating with your managed cloud
        storage services. Instead of allowing direct file
        downloads to user devices, our **'Save to Cloud'**
        feature automatically redirects them to your
        organization’s cloud storage.

        This method ensures that you can enforce your data
        protection policies and give users seamless access to
        their files across all their devices, which supports
        better collaboration and a smoother workflow.
      - To ensure that you have configured the permissions
        correctly, you must use the email of an active, licensed
        user in your organization. The system uses this email solely
        for a permissions check; it **will not** send emails or
        upload any files to the account.
   8. Click **Test provider connection** to verify the connection with
      Google.
   9. Once the test is successful, click **Add Provider**.

###### Known Limitation

HTML sites will be compressed using zip format and saved
in a folder. The Prisma Browser does not support unzipping files. As a result,
this is not recommended.

---

<a id="cloud-provider-microsoft-onedrive"></a>

##### Cloud Provider - Microsoft OneDrive

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/cloud-storage-integrations/cloud-provider-microsoft-onedrive>*

This document contains the directions for integrating Microsoft OneDrive as the cloud
provider

###### Microsoft OneDrive Prerequisites

These are the prerequisites for configuring Microsoft OneDrive as your cloud
provider:

- Global Administrator access in Azure Active Directory (AD)

End users require a valid Microsoft 365 license:

- Microsoft 365 Business Basic /Standard / Premium
- Microsoft 365 Apps for Business
- Microsoft 365 E3 / E5

###### Configure Microsoft OneDrive as the Cloud Provider

1. Register a new app in Azure.
   1. Sign in to the [Azure Portal](https://portal.azure.com/).
   2. Go to **Azure Active Directory → App registrations → + New
      registration**.
   3. Enter a descriptive name (for example, *Prisma Browser Cloud
      Storage for M365*)
   4. Choose **Single tenant**
      (Accounts in this organizational directory
      only).
   5. Under **Redirect URI**, select **Single-page application
      (SPA)** and use this URI:
      https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org/
   6. Click **Register**.

      ![]()
2. Add Permissions to the New App.
   1. Open the new app **→ App permissions → + Add a
      permission**.
   2. Choose **Microsoft Graph**.
   3. Add the following Application permissions:

      - Application.Read.All
      - DelegatedPermissionGrant.Read.All
   4. Click **+Add a permission → Microsoft Graph → Delegated
      permissions**.
   5. Add the following permission:

      - Files.ReadWrite.All
   6. Click **Grant admin consent for <your tenant name>** Click
      **Yes** in the consent confirmation pop-up.

      User.Read
      permission (delegated) is added by default by the
      application. DO NOT REMOVE THIS PERMISSION.

      ![]()

      ![]()

   WHY ARE THESE PERMISSIONS NEEDED?

   **Prisma Browser** requires specific permissions. These are the
   minimum necessary to ensure proper connection and to manage file
   downloads to your organization's cloud storage. This
   **least-privilege** approach minimizes security risks by only
   requesting access essential for its operation.

   |  |  |  |
   | --- | --- | --- |
   |

   **Permission Type** | **Permission Name** | **Reason** |

   |

   Delegated | User.Read | Confirms that the user connected to the browser is the same user that is connected to Microsoft. |

   |

   Delegated | Files.ReadWrite.All | Saving files to the user's OneDrive on their behalf. |

   |

   Application | Application.Read.All DelegatedPermissionGrant.Read.All | Verifies the integration configured by the Microsoft admin. |

   Admins always consent to application
   permissions. In contrast, end users consent to delegated permissions.
   Granting admin consent for delegated permissions is required. It
   prevents users from mistakenly denying permissions, which would block
   them from downloading and saving files to OneDrive when a Security
   policy is triggered.

   Verifying the onboarding status of the
   integration is critical. Improper configuration will prevent Prisma Browser from saving files to OneDrive. This will block end
   users from downloading and saving files when their download action
   matches a policy rule.
3. Generate Client Secret.
   1. Go to **Certificates & Secrets → New client secret**.
   2. In the Add a client secret tab, do the following:

      1. Enter a **description** for the secret, for example -
         Microsoft secret 01. (this field is optional.
      2. In the **Expires** field, select **730 days (24
         months)**.
   3. Click **Add**.
   4. Copy the value of the new client secret. You will need it for the
      next step when you connect the cloud storage to the Prisma Browser. We recommend that you save it in a safe place.

   ![]()
4. Connect to the Prisma Browser.
   1. Go to the Prisma Browser admin console and select
      **Integrations**.
   2. Select **Cloud Storage**.
   3. Click on either **+add provider** or **Connect your first
      provider**.

      ![]()
   4. Select the provider - **Microsoft**.
   5. Insert a descriptive **Storage name** for the connection, for
      example - *Microsoft Cloud Storage*.

      ![]()
   6. Paste the **Client secret** that you generated in the previous
      step.
   7. Enter the Application (client) ID and the Directory (tenant) ID
      from the Application Overview in the Azure Portal.
   8. Click **Test provider connection** to verify the connection with
      Azure.
   9. Once the test is successful, click **Add Provider**.
5. Create the Save to Cloud Rule
   1. Open the **Access & Data Control** rules and create a new
      rule.
   2. At the **Data Control** step, select **File Download**.
   3. Select **Save to organization storage** and choose the provider
      that you configured in the previous step.
   4. Add any additional details, and click **Set**.

###### Known Limitations and Requirements

To successfully use Save to Cloud, users must meet the following conditions:

- **Microsoft 365 Licensing:** The policy must apply only to users who
  hold a valid Microsoft 365 license that includes access to OneDrive and
  the Office suite.
- **Email Consistency:** The email address used to sign into the
  browser must match the Microsoft account associated with the user’s
  OneDrive. This prevents accidental data leakage or cross-account DLP
  violations.
- **Microsoft Sign-In Required:** Users must be signed into their
  Microsoft account. If not already authenticated, they will be prompted
  to log in, with the browser providing a username hint to streamline the
  process.

HTML sites will be compressed using zip format and saved
in a folder. The Prisma Browser does not support unzipping files. As a result,
this is not recommended.

---

<a id="first-party-integrations"></a>

#### First-Party Integrations

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations>*

A link to the first-party integrations

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

Prisma Access Browser works with the following Prisma Access services:

- [File Handling and Analysis in Advanced
  WildFire](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/file-handling-and-analysis-in-advanced-wildfire.html)
- [IP Based Enforcement Using an
  Authentication Gateway](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway.html)

---

<a id="enterprise-data-loss-prevention"></a>

##### Enterprise Data Loss Prevention

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/enterprise-data-loss-prevention_0>*

Enterprise Data Loss Prevention - Prisma Browser (ES)

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

Palo Alto Networks’ **Enterprise Data Loss Prevention (EDLP)** is a cloud-native
security service that safeguards sensitive data from loss, theft, and misuse.
Traditional on-premise solutions cannot effectively protect data distributed across
cloud apps, remote workforces, and diverse devices. EDLP addresses these challenges with
a unified, scalable, and intelligent approach.

This article explains EDLP’s core concepts, key features, integration with the Palo Alto
Networks security ecosystem, and configuration in the **Prisma Browser**.

###### Core Concepts

These are the core concepts behind EDLP:

- **Unified, Cloud-delivered Approach** - EDLP is a single, centralized
  service that integrates natively with Palo Alto Networks products such as
  NGFWs, Prisma Access, Prisma Browser).
- **Data Classification as the Foundation** - EDLP identifies sensitive
  data using advanced classification methods that extend beyond simple keyword
  matching.
- **Multi-channel Protection** - EDLP protects data **in motion**
  (network traffic, email, file uploads), **at rest** (SaaS and cloud
  storage), and **in use** (endpoints and browsers).
- **Centralized Policy Engine** - EDLP provides one console for managing
  data control sets, classifiers, and incidents, ensuring consistent policy
  enforcement across network, cloud, and endpoint controls.

###### Key Features

**Advanced Data Classification**

- **Machine Learning & Trainable Classifiers** — Detect complex,
  unstructured data like source code; trainable on proprietary datasets.
- **Exact Data Matching (EDM)** — Match against encrypted datasets (e.g.,
  employee records).
- **Indexed Document Matching (IDM)** — Detects partial or full document
  copies regardless of format.
- **Optical Character Recognition (OCR)** — Extracts and scans text from
  images and PDFs.

**Incident Management & Remediation**

- **Centralized Visibility** — Unified incident logging across all
  channels.
- **Detailed Context** — Each incident record includes the user,
  application, data profile, and policy violated.

**Platform Integration and Policy Enforcement**

- **Centralized Data Sets** — Manage classifiers and data profiles from a
  single console.
- **Prisma Access & Prisma Browser Integration** — EDLP applies the
  same classifiers to remote workers and browser-based activity, enforcing
  last-mile controls.
- **Consistent Enforcement** — Enforcement points (NGFW, Prisma Access,
  Prisma Browser) send content for inspection, apply the policy action, and
  log incidents centrally.

###### Configure EDLP in Prisma Browser

This section outlines how to configure EDLP in Prisma Browser by defining data
profiles, applying them in rules, and monitoring incidents.

###### Before You Begin

Before you begin - make sure you understand the following concepts:

- EDLP integrates with **Access & Data Control rules** in Prisma Browser.
- You can create a new rule or modify an existing one.
- Data Profiles must be defined in the **central EDLP console** before they
  can be applied in Prisma Browser.
- To support rapid deployment, the system includes 24 predefined Data profiles
  that cover commonly required use cases.. These predefined Profiles include:
  - GDPR
  - HIPPA
  - Malware
  - Secrets and credentials
  - CommonweralthAustralia-PrivAct88

EDLP can operate using OCR information, however it
is only supported for Cloud-assisted profiles with File Download and File Upload
controls.

###### Step 1: Define Data

###### Check for existing profiles

Review the predefined profiles in the EDLP console before creating a new one.

###### Configure Data Profiles

1. In the **Controls and Data Profiles** page, click **+ Set data
   profile**. 

   ![]()
2. Choose one of the following:
   - **Not set (Any Content)** — Applies selected controls to all
     content.
   - **Specific data profile (Specific content)** — Applies
     controls only to content matched by a selected profile.
     - Supports both on-device and cloud-assisted
       scanning.

       Cloud-assisted
       scanning adds latency.

     ![]()
3. If you select **Specific data profile**, the **Select data
   profile** field appears. 

   ![]()
4. Select an existing profile or scroll to the bottom and click **Create
   new profile**.

   ![]()

   All profiles work with the Prisma Browser. Profiles marked with the **Prisma Browser
   logo** can also run locally inside the browser and support
   last-mile controls for actions other than upload, download, and
   print. 

   ![]()
5. Click New Data Profile to begin adding a new profile. For details, see
   the **EDLP Profile Creation Help**.

When you create a Profile using Data Masking, it is
strongly recommended that you rely on simple logic. Complex logic may run
incorrectly, as once some information is displayed, the system may need to
go back and mask it based on the logic. This can result in inconsistencies
and significant latencies.

###### Step 2. Understand Profile Types

- On-device Profiles
  - *Purpose*: Low-latency scanning.
  - *Classifiers*: Regex, dictionaries, basic types.
  - *Processing*: All scanning occurs locally.
- Cloud-Assisted Profiles
  - *Purpose*: High-accuracy scanning
  - *Classifiers*: EDM, IDM, ML.
  - *Processing*: Content is sent to EDLP cloud service.

  Using Cloud-assisted profiles will
  result in latency.

###### Step 3. Review Control Support

Not all Access & Data Controls support all profile types. Use
the **Controls Support Chart** to verify the support level for each
control.

- **Supported by the scan** — Fully supported.
- **Not supported by the scan, but can be applied** — Not
  supported but can be added to the rule, ignoring the data profile
  selection,
- **Not supported and cannot be used with other controls** — Control
  unavailable with selected profile.

![]()

**Examples**

- **File Download** — Supports any data profile selection.
- **Webpage Data Masking** — Requires on-device data profile
- **Clipboard** — Supported for On-device data profiles, not
  supported in cloud-assisted scans (but can still be applied ignoring
  the data profile selection).

###### Step 4. Apply Profiles in Prisma Browser Rules

1. **Select Profile** — When creating or editing a rule,
   choose a data profile. The console indicates whether it is On-Device or
   Cloud-Assisted.
2. **Set Controls** — Apply the profile to data controls such
   as File Upload, File Download, Clipboard, or Screen Share.
3. **Override Confidence (On-Device only)** — Adjust
   confidence level. You can change the confidence levels defined in the
   data profile for changing scan results. Be aware of the following:
   - **Recommended confidence levels** - Results in more
     matches, as the scanning will take every possible positive,
     without cross-checking the data. For example, any combination
     that looks like an SSN will be flagged as an SSN.
     1. This only impacts Clipboard, Screenshot, Data masking,
        Typing Guard, and Watermark controls. File upload, File
        download, and Print controls will not be impacted by
        this configuration.
   - **Adhere to Original Confidence** — Results in
     fewer matches, as the browser will look for additional evidence
     before flagging a positive. For example, a combination of
     numbers that look like an SSN will need the indicator SSN before
     it will flag anything.

     this may miss some positives
     matches

**To override the Profile settings:**

1. After you select an on-device data profile, you will have the option
   to override profile settings.
2. Click **+Override profile settings**.
3. In the window, select the confidence level that you want to
   use.
4. Click **Save changes**.

![]()

###### Step 5. Monitor and Analyze Incidents

- **Unified Visibility** — Prisma Browser logs all DLP
  events in the central EDLP console. This gives you a single dashboard to
  view all incidents across your network, cloud, and browser.
- **Incident Details** — You can investigate each incident to
  see which Prisma Browser policy triggered it. The platform provides
  **data snippets** (a preview of the sensitive data) and can save
  the full file as **evidence**.

###### No Support for Secondary Data Profiles

When you use **Data Profiles**—which allow administrators to set highly
specific security responses (like blocking high-risk data but only alerting on
low-risk data)—the system doesn't use the **Secondary Rule** option.

The Prisma Browser rules handle all the blocking and alerting actions.
To avoid confusion and conflict, the profile setup strictly requires that all its
component parts only use the **Primary Rule** setting. This ensures that the
fine-tuned, complex policy works exactly as the administrator designed it.

Any secondary rules are ignored.

There is a known limitation when using OCR; it is only
supported for Cloud-assisted profiles with File Download and File Upload
controls.

###### Data Snippets and Evidence Storage - Locating Security Incident Details

When either the Prisma Browser local scanning or the EDLP detects
sensitive data that violates a policy, two critical types of forensic data are
generated:

- **Data Snippets**
- **Evidence Storage**

These provide security administrators with details about the incident.

###### Data Snippets - The When and the Where

Data snippets are short, masked **fragments of text** that trigger
security violation. They show ***what** (including 200 characters before
and after the trigger, if it exists)* content caused the alert without
exposing the entire sensitive file or document.

These snippets are often masked to maintain privacy. The snippets are
visible in the **Prisma Browser Events**.

###### Configuring Snippets

Snippets are globally enabled in the EDLP settings.

1. In the **Controls and Data Profiles** tab, click **Set data
   profile**.
2. In the Data profile window, select **Specific data profile**, and
   select a data profile.
3. Click **Save**. 

   ![]()
4. In the **Tracking** tab, select **Content scanning (EDLP)**
   from either On or Enhanced.
5. Select **Data Snippet**.

Snippets are supported for all
content-supporting controls.

###### Evidence Storage

Evidence storage is the repository for the **full file or complete
data** that triggered the policy violation. This provides the entire
context needed for thorough forensic investigation. The Evidence Storage is
available in two places:

- The customer-configured storage (for example, an AWS S3
  bucket).
- Within the DLP Incident details, where it is ready for
  administrator review.

###### Configuring Evidence Storage

Evidence storage is globally enabled in the EDLP settings.

1. In the Controls and Data tab, click Set Data profile.
2. In the Data profile window, select Specific data profile, and select
   a data profile.
3. Click **Save**.
4. In the Tracking tab, you will be able to select **Content scanning
   (EDLP)** from either **On** or **Enhanced**.
5. Select Evidence Storage

Evidence storage is supported for File
Download, File Upload, and Print controls.

###### Unified Incident Management

The integration between E-DLP and the Prisma Browser
streamlines investigation for security teams:

- **Prisma Browser events** ( or local administrators)
  **include a direct link to the corresponding E-DLP
  incident**.
- This link allows security administrators to jump straight into the
  **Unified Incident Manager** for full investigation, where they
  can view the data snippet, examine the surrounding PAB event details,
  and access the full evidence file.

###### Cloud Scanning Thresholds

When using Enterprise DLP (EDLP) with Prisma Browser, some data profiles
are classified as *Cloud-Assisted*. These profiles rely on advanced detection
techniques—such as Exact Data Matching (EDM), Indexed Data Matching (IDM), and
machine-learning–based analysis—that require files to be uploaded to the EDLP cloud
service for inspection and analysis.

Since cloud-based scanning introduces additional latency from file upload
and processing, you can configure threshold settings to balance robust data
protection with an optimal end-user experience.

###### Configure Thresholds

You can manage thresholds in the Strata Cloud Manager under ConfigurationData Loss PreventionSettingData TransferFile Based Settings.

![]()

###### Key Threshold Limits

- **File Size:** Maximum file size for scanning. You can define the maximum
  file size eligible for scanning, between 1 MB to 100 MB.

  Files exceeding this size skip scanning.
- **Scan Time:** Maximum duration for a scan to complete. You can define the
  maximum duration between 1 to 240 seconds.

###### Enforcement Logic

Prisma Browser follows specific logic when multiple DLP components are present or
when thresholds are exceeded:

- If both **Endpoint DLP** and **Network DLP** are
  available, Prisma Browser will use the **Network DLP
  thresholds**.
- **Threshold Action:** You can define what happens when a
  scan cannot be completed (e.g., if the file is too large or the scan
  times out).
  - **Fail Unmatch:** If the EDLP settings action is set to
    **Allow**, a failed scan (due to threshold) results in a
    file action policy in Prisma Browser to be skipped (i.e,
    treated as "no match").
  - **Fail Block:** If the EDLP action is set to **Block**,
    any scan that fails to complete within the threshold is treated
    as a "fail block," and the file is prevented from being
    uploaded/downloaded/printed, even if the Prisma Browser
    policy is set to allow the file action upon a match.

---

<a id="file-handling-and-analysis-in-advanced-wildfire"></a>

##### File Handling and Analysis in Advanced WildFire

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/file-handling-and-analysis-in-advanced-wildfire>*

How to Manage WildFire

Advanced WildFire is a cloud-delivered malware analysis service that uses a tiered
approach to file inspection. This design prioritizes both strong security controls
and optimal performance, especially in terms of latency

###### File Size Thresholds and Reputation Checks

Wildfire is also able to scan documents via the Prisma
Access Browser Extension (PABX).

Advanced WildFire evaluates all submitted files against a maximum size threshold
of **300 MB**

- **Files over 300 MB**
  - These files bypass reputation-based scanning and never enter the
    WildFire knowledge base.
  - The system applies the fall back **policy rule** configured
    by the administrator, which determines whether to **enable
    (permissive)** or **block (protective)** the file.
- **Files 300 MB or smaller**
  - WildFire checks the file's hash against the reputation database.
    - If the reputation database indicates that the file is
      **benign**, then the system enables it.
    - If the reputation database indicates that the file is
      **malicious**, then the system blocks it.
  - For **files 20 MB or smaller**, the browser waits for a
    **Static Analysis verdict** before proceeding. This step
    mitigates security risks while minimizing end-user latency.
  - For **unknown files between 20 MB and 300 MB**, the system
    defers to the administrator’s fall back policy rule to determine
    access, as waiting for analysis results could degrade
    performance.

###### Dynamic Analysis of Unknown Files

The system submits all **unknown files under 300 MB** to **Dynamic
Analysis**, which executes the files in a controlled environment to detect
advanced threats. Although this enhances the accuracy of the WildFire reputation
database, **Dynamic Analysis currently does not support file quarantine-**a
capability planned for a future release.

By integrating multiple analysis layers, Advanced WildFire enables
organizations to maintain robust security while minimizing disruption to end
users.

###### Password-Protected File Handling

Advanced WildFire attempts to scan password-protected files using a
**brute-force unlocking mechanism**, subject to format compatibility and
defined limitations.

###### Supported File Types for Brute-Force Unlocking

The brute-force process supports the following password-protected formats:

- .rar archive files
- .pdf document files
- Microsoft Office files (2007 or later), including
  - .docx
  - .xlsx
  - .pptx

The system blocks scanning for password-protected files that fall outside of
these formats under all circumstances.

**Brute Force Failure Handling**

If the brute-force attempt **fails** to unlock the file:

- The file won't be scanned.
- The returned scan verdict will be "Unknown."
  - This ‘Unknown’ status is currently treated as **benign**,
    enabling the file to pass without further inspection.

###### Administrator-Defined Fallbacks

You can set your own fallback policy rule when one of the following events
occurs:

- File size exceeded
- Connection error or service unavailable
- Unsupported file type

In all of these cases, you can decide whether to treat the file as Benign and
enable it, or as Malicious and block it.

###### Supported File Types

Supported File Types

|  |  |  |  |
| --- | --- | --- | --- |
|

**Extension** | **File Type** | **Extension** | **File Type** |

|

**.7z** | 7zip Archive | **.pptx** | Microsoft PowerPoint Document |

|

**.swf** | Adobe Flash File | **.slk** | Microsoft Symbolic Link |

|

**.apk** | Android APK | **.iqy** | Microsoft Web query |

|

**.dex** | Android DEX.bat | **.doc** | Microsoft Word 97-2003 Document |

|

**.bz** | bzip2 archive | .**docx** | Microsoft Word Document |

|

**.csv** | comma separated values | **.ods** | OpenDocument Spreadsheet Document |

|

**.dll** | DLL/DLL64 | **.odf** | Open~Document Text Document |

|

**.elf** | ELF | **.pdf** | Portable Document Format |

|

**.gz** | Gzip archive | **.exe** | PE/PE64 |

|

**.hta** | HTML application | **.pl** | Perl script |

|

**.iso** | ISO | **.png** | Portable Network Graphics |

|

**.class** | JAVA class | **.ps1** | PowerShell |

|

**.jar** | JAVA jar | **.py** | Python Script |

|

**.js/.jse/.wsf** | Javascript/Scipt | **.pap** | RAR Archive |

|

**.jpg** | Joint Photographic Experts Group | **.rtf** | Rich Text Format |

|

**.elink** | Link | **.sh** | Shell Script |

|

**.macho** | Mach-o | **.tar** | TAR Archive |

|

**.pkg** | macOS App Installer | **.vbs/.vbe** | VBScript |

|

**.zbundle** | macOS App Bundle in ZIP Archive | **.msi** | Windows Installer Package |

|

**.fat** | macOS Universal Binary File | **.Inl** | Windows Link File |

|

**.dmg** | macOS Disk Image | **.wsf** | Windows Script |

|

**.xls** | Microsoft Excel 97-2003 | **.zip** | ZIP Archive |

|

**.xlsx** | Microsoft Excel | **.asp** | Active Server Pages |

|

**.one** | Microsoft One Note Document | **.aspx** | Active Server Packages Extended |

|

**.ppt** | Microsoft PowerePoint 97-2003 | **.xml** | Extensible Markup Language |

|

**.html** | HyperText Markup Language |  |  |

Nested Archives are supported in zip, rar, 7z, bzip2,
iso, gz, tar, vhd, docx, pptx, xlsx, jar.

###### Known Limitations Wildfire and Prisma Browser Extension

The following files cannot be scanned:

- Local files opened directly in the browser (e.g., file:// paths).
- Full page saves (Ctrl+S / Cmd+S) cannot be intercepted.
- Certain browser-internal URLs (extension blobs, untrusted contexts,
  null-origin blobs).
- Domains excluded via configuration are skipped entirely.

Only the Advanced Wildfire scanning provider is
supported. Other providers configured in the policy are silently skipped --
the file transfer proceeds without scanning.

**Policy Effects Not Yet Supported**

The following effects are configured in policy but not yet enforced. In all
cases, the transfer is blocked rather than applying the intended effect:

|

Effect | Applies to |

| --- | --- |

|  |  |
| --- | --- |
|

Allow Protected | Downloads |

|

Save to Organizational Storage | Downloads |

|

Encrypt | Downloads and Uploads |

|

Non-encrypt (allow only non-encrypted) | Uploads |

**Policy Options Not Yet Supported**

The following interactive options are not yet implemented. When
configured, the transfer is blocked instead:

- Bypass ("Proceed Anyway")
- Bypass with reason ("Require Reason")
- MFA challenge
- Admin approval (downloads only)
- Content filters / DLP pattern inspection

**Metadata Filters**

|

Filter | Status |

| --- | --- |

|  |  |
| --- | --- |
|

File size | Supported |

|

File type / extension | Supported |

|

File Hash | Not currently supported |

**Upload-Specific Limitations**

- Folders dragged and dropped - are not scanned. There are silently
  allowed.
- Folder upload via directory picker is not intercepted.
- File path and file type may not always be identifiable

**Download-Specific Limitations**

- When the file cannot be fetched for scanning or a mismatch
  is detected between the scanned copy and the actual download, the
  download currently proceeds unscanned
- File size may briefly display as 0 during scanning
- A long-running scan on a download that opened in a new tab
  may delay the tab from closing

---

<a id="ip-based-enforcement-using-an-authentication-gateway"></a>

##### IP-Based Enforcement Using an Authentication Gateway

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/first-party-integrations/ip-based-enforcement-using-an-authentication-gateway>*

IP-based enforcement Using the Authentication Gateway.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser paid and production   tenants only - Role: Superuser, with full read-write access. [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

IP-based enforcement enables you to restrict access to your applications by
ensuring that authentication traffic originates only from authorized Prisma Access
Browser egress IP addresses.

Existing customers using the shared Authentication Gateway,
refer to the Migration Guide for existing Customers, below.

###### Platform Support

IP-based enforcement supports both Prisma Access Browser (PAB) and Prisma Access
Mobile Browser, providing consistent protection across desktop and mobile
platforms.

###### How it Works

The IP-based enforcement feature works through a simple yet effective
mechanism:

1. **The Authentication Gateways serves as a forward proxy**: The
   Authentication Gateways functions as a forward proxy with a set of
   predictable, dedicated IP addresses specific to your tenant.
2. **Configured traffic routing**: The browser’s configuration routes IdP
   authentication traffic through the Prisma Access Browser gateway.
3. **IdP conditional access**: You establish conditional access rules in
   your identity provider to only enable authentication from your dedicated
   Authentication Gateway egress IP addresses.
4. **Enforced access control**: As a result, authentication attempts from
   browsers other than PAB will fail, effectively restricting access to your
   protected applications.

###### Key Benefits

- **Dedicated tenant-specific egress IPs**: Your tenant receives unique
  IP addresses not shared with other customers.
- **Multitenant validation**: Easily verify traffic from specific
  tenants, even when managing multiple tenants.
- **Regional availability**: Available in strategic global locations
  with automatic failover protection.

###### Supported Regions

IP-based enforcement is available in the following GCP compute regions:

- us-east4 (Ashburn, Virginia)
- us-west1 (Portland)
- europe-west2 (London)
- europe-west3 (Frankfurt)
- Asia-south1 (Mumbai)

  IP-based enforcement
  operates across all five regions by default, and the system doesn’t
  allow selecting individual regions.

###### Configuration Steps

1. Configure dedicated Egress IP Addresses
   1. From the Strata Cloud Manager, go to Workflow → Prisma Browser → SSO Enforcement.**Configuration → Onboarding → Prisma
      Access Browser → View**.
   2. Click **Create Dedicated Egress IP Addresses**.

      This process can take a few minutes
      until the IP Addresses are available in all regions.
   3. Copy the list of generated IP addresses for use in your IdP
      configuration,

   ![]()
2. Configure your Identity Provider (IdP)
   1. Select your IdP provider from the list of supported providers
      and click **Save**:

      - [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement.html#ip-based-enforcement_task-qhf_wv4_tcc)
      - [Microsoft
        Azure Active Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement.html#ip-based-enforcement_task-sy5_wqp_tcc)
      - [PingID](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement.html#ip-based-enforcement_task-cl4_xw1_vcc)
      - [VMware
        Workspace One Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement.html#ip-based-enforcement_task-i4k_jfg_vcc)
      - [OneLogin](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement.html#ip-based-enforcement_task-sbh_jls_5cc)
   2. In case your IdP does not appear on the list or you're using a
      custom IdP, contact Support or your Account team to configure
      your custom IdP URL. If you use multiple identity providers, you
      can select more than one from the list.
   3. Follow the specific instructions for your selected IdP to
      configure conditional access with your dedicated egress IP
      addresses.

   ![]()
3. Enable Authentication Traffic Routing
   1. Toggle the **Authentication Traffic Routing** switch to
      enable the feature.

      If you use **Shared Authentication
      Gateway**, continue with the Migration Guide for
      existing Customers (below).
   2. Validate the configuration by logging into an enforced
      application in your IdP:

      - Test using a commercial browser - the system should deny
        access.
      - Test using the Prisma Access Browser - the system should
        grant access.

###### Migration Guide for Existing Customers

If you're already using IP address-based enforcement with shared IP
addresses, follow these steps to migrate to dedicated IP addresses:

1. **Access the New Interface**: The Admin Console will display a
   new dedicated IP address tab.
2. **Create Unique IP addresses**: Generate your tenant-specific
   dedicated IP addresses. 

   ![]()
3. **Update IdP**: Add the new IP addresses to your IdP's
   conditional access policy rule.
4. **Switch Enforcement Method**: Change to “Dedicated IP addresses”
   in the web interface, and click **Save**.

![]()

**Important Migration Notes:**

- When migrating, keep the original shared IP addresses in your IdP's
  configuration as a fall back.
- If you encounter issues with the new configuration, you can
  temporarily switch back to shared IP addresses in the admin console.

  Mobile browsers with versions older
  than [1.5093 for iOS, 1.5096 for Android] will continue using
  the old shared IP addresses until upgraded to the minimum
  supported version.

###### Troubleshooting

If you encounter issues with IP-based enforcement:

- Check your browser's troubleshooting page. :
  - Click the Prisma Access Browser Extension icon in the menu
    bar.

    ![]()
  - Click the shield icon. 

    ![]()
  - Open the **Authentication Gateway** section.
  - Ensure that the **Status** shows **Configured**, and
    that no errors appear.
  - Click **Test Connectivity**. Follow the instructions as
    needed. 

    ![]()
- Ensure that you have correctly configured the IP addresses in your
  IdP.
- Turn on the Authentication Traffic Routing toggle.
- If the issues persist, contact **Support**.

###### Frequently Asked Questions (FAQ)

**Q: How long does it take for
dedicated IP addresses to become available?**

A: The
process typically takes a few minutes to complete across all supported
regions.

**Q: Can I use the same IP addresses across
multiple tenants?**

A: No, each tenant receives unique
dedicated IP addresses to ensure proper isolation and security. For
organizations managing multiple tenants, including all relevant IP addresses
in the conditional access configuration is crucial.

**Q:
How long will the IP addresses remain reserved?**

A:
The system allocates your dedicated IP address to your tenant for as long as
your tenant remains active as long as the **Dedicated IP Addresses**
feature is enabled.

**Q: Which platforms support the
Authentication Gateway?**

A: The feature is available
for both Prisma Access Browser for desktop and mobile.

**Q:
What is the expected behavior if the dedicated Authentication Gateways
is configured, but the user has an old browser version?**

A: Old browser versions will keep sending traffic to the legacy
Authentication Gateway (“shared proxy”) until the browser is up to date. For
desktop browsers, the extension version should be automatically updated
immediately after the next browser launch. For the Mobile Browser, ensure
that users update to a supported version.

**Q: What does
the traffic flow look like if I configure “route all traffic to Prisma
Access”?**

A: When you enable the authentication
routing, the authentication traffic will be routed through the
authentication proxy regardless of the general traffic routing to Prisma
Access.

**Q: What happens if a region becomes
unavailable?**

A: The system or browser automatically
routes users to the second-nearest available region to maintain service
continuity.

**Q: Can I see all the Traffic logs in
SLS?**

A: Currently this isn’t available.

**Q: My tenant is in a different region than the Authentication
Gateways. What will happen?**

A: Authentication
traffic will be routed through the region nearest to the user.

**Q: Can
I use a dedicated authenticated gateway with an Eval/Lab license?**A:
The creation of dedicated egress IP addresses is a feature of paid
subscriptions. If you're on a trial or require access through a different
arrangement, contact your account team.

---

<a id="how-is-synched-data-stored"></a>

#### How Is Synched Data Stored?

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/how-is-synched-data-stored>*

This is a legacy topic that needs to be included

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

Syncing with Prisma Access Browser's sync service is automatic. Every user's identity is
assigned a unique key that encrypts the data that is sent and stored.

Neither Palo Alto employees nor console administrators have access to these keys.
Encryption keys are stored in a secret store that is only accessible with a token
associated with the user account.

A record of each access to the encryption key is maintained.

---

<a id="integrate-prisma-browser-and-okta-with-the-device-posture-provider"></a>

#### Integrate Prisma Browser and Okta with the Device Posture Provider

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/integrate-prisma-browser-aand-okta-with-the-device-posture-provider>*

Describes the integration between PB/Okta and DPP

By integrating Okta with Prisma Browser, you can use [device posture data](https://help.okta.com/oie/en-us/content/topics/identity-engine/devices/device-assurance-device-posture-idp.htm) from Prisma Browser to
configure detailed device assurance and app sign-in policies. This integration helps you
enforce stronger security requirements and ensure that only compliant devices can access
Okta-protected resources.

The Device Posture Provider feature uses a SAML-based integration for secure
communication. Okta sends a SAML request to PAB, and PAB responds with a SAML assertion
containing device posture attributes. These attributes allow you to create granular
sign-in policies based on your organization’s security standards.

##### Prerequisites

You need to enable the following features from the Okta Admin Console:

- Device Posture Claims Mapping
- Device Posture Provider

For more information refer to [Enable self-service features](https://help.okta.com/oie/en-us/content/topics/security/manage-ea-and-beta-features.htm).

![]()

##### Configure the Device Posture IdP in Okta

**Open the Prisma Browser Onboarding screen**

From the Strata Cloud Manager, select Configuration Onboarding

1. Navigate to the **Enforce SSO Applications** step.
2. Copy the Issuer URI and Single Sign-On URL.
3. Download the Prisma Browser certificate. 

   ![]()

In the Okta Admin Console, go to SecurityIdentity Providers.

1. Click **Add Identity Provider**.
2. Select **SAML 2.0**
3. Configure the Prisma Browser as an IdP. For more information, refer to
   [Add a SAML Identity
   Provider](https://help.okta.com/oie/en-us/content/topics/security/idp-add-saml.htm).

   ![]()

   - IdP Usage: Select Device Posture Provider.
   - IdP Issuer URI: Paste the Issuer URI from the Prisma Browser.
   - IdP Single Sign-On URL: Enter the sign-on URL from Prisma Browser.
   - IdP Signature Certificate: Upload the certificate from Prisma Browser.
   - Destination: Paste the Single Sign-On URL path that you copied from
     Prisma Browser.
   - Click **Save**.
   - From the Summary screen, download the SAML Metadata. 

     ![]()
4. Return to the Prisma Browser Onboarding screen and upload the SAML
   Metadata file.

   ![]()
5. Enable the Integration

##### Enable the Device Posture IdP as Provider for Device Assurance

You can create or modify the device assurance policies to incorporate additional
signals from your IdP due to its integration with the Device Posture Provider. See
[Add a device assurance policy](https://help.okta.com/oie/en-us/content/topics/identity-engine/devices/device-assurance-add.htm).

1. In the Okta Admin Console, go to SecurityDevice integration.
2. On the **Endpoint Security tab**, click **Add endpoint
   integration**.
3. Select **Device posture provider**.
4. Select the Platform.
5. Save the configuration. 

   ![]()

##### Configure a Device Assurance Policy

1. Go to SecurityDevice Assurance Policy.
2. Click **Add Policy**.
3. Click **Create Policy**.
4. Define a Policy Name.
5. Select the Platform.
6. In the Device attribute provider(s) section, select: **Device Posture
   Provider**.
7. In **Device management**, select **Device must be managed**. **see note
   below**
8. Click **Save**.

   ![]()

   ![]()

Device must be Managed - Okta defines **Managed** as
follows: The device is under the organization's IT or security team's control and
oversight, as indicated by installed management agents or software.

##### Integrate the Policy into an App Sign-in Policy

After you create a device assurance policy, integrate it into an app sign-in policy
to ensure enforcement before users access protected resources. For detailed steps,
see **[Add device assurance to an app sign-in
policy](https://help.okta.com/oie/en-us/content/topics/identity-engine/devices/device-assurance-policy-rule.htm)**.

If the global session policy requires a password, the **Okta Sign-In Widget**
prompts users to enter their username and password before redirecting them to the
device posture Identity Provider (IdP).

To verify compliance first, configure the app sign-in policy rule that requires
device posture claims with the highest priority. You can also apply conditions such
as **Group**, **Platform**, or **Network Zone** to target specific
users.

###### Configure an Authentication Policy to use Device Posture IdP Signals

1. Go to SecurityAuthentication Policies sectionApp sign-in
2. Click **Add Rule**
3. Define a Policy Name.
4. In the **Device Assurance policy is**, select **Any of the following
   device assurance policies**.
5. Select the Device Assurance policy you created in the previous step.
6. Click ∫**Save**.

![]()

##### Modify the Catch-All Rule, and Set it to Deny All

1. Go to SecurityAuthentication Policies sectionApp sign-in
2. Find the Catch-All rule.
3. Click ActionsEdit.
4. At the bottom, set the rule to **Deny All**.

   ![]()

---

<a id="ip-based-enforcement"></a>

#### IP Based Enforcement

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/ip-based-enforcement>*

Ensure that access to SSO-enabled applications is only possible from the Prisma Browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) |

IP-based enforcement ensures that access to SSO-enabled applications is
only possible from the Prisma Browser. Authentication traffic to your IdP flows
through a special proxy with a set of known egress IP addresses.

The Prisma Browser uses the Authentication Proxy for
the SSO login pages only. It does not use the proxy for any other traffic.

The Prisma Access Gateway acts as a forward proxy with a set of predictable
IP addresses. You then need to configure the browser to route the IdP authentication
traffic through the Prisma Browser gateway.

You then need to create and establish a conditional access rule in the IdP,
making a requirement to only use the Prisma Browser Gateway for authentication.
This means that any attempt to authenticate via a different browser will fail.

To begin the process, perform the following actions:

1. Open the Strata Cloud Manager.
2. Open the Cloud Identity Engine.
3. Select Authentication Types
4. Click **Add New Authentication Type.**

   ![]()
5. Under **SAML 2.0**, click **Set Up**.

   ![]()
6. Set up your IdP. To properly configure the IdP, refer to [Cloud Identity Engine Getting Started](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine).
7. In the Prisma Browser Setup page, click step 4: **Enforce SSO
   Applications**.

   ![]()
8. Choose the appropriate IdP. All Prisma Browserauthentication traffic to
   those identity provider tunnels through the Prisma Browser gateway. The
   options are:

   - Okta
   - PingID
   - VMware ONE Workspace Access
   - Microsoft Azure Active Directory
   - OneLogin

   To integrate the Prisma Access Browser and Okta with
   the device Posture provider, [see here](https://docs.paloaltonetworks.com/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-browser-aand-okta-with-the-device-posture-provider).

##### Configure Okta IP-Based Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use Okta.

1. Configure the Prisma Browser Application Enforcement IP Addresses
   1. Configure the Application Enforcement IP Addresses. In the Okta app
      go to **Security > Networks > Add zone > IP zone**.

      ![]()
   2. Set the name of the zone to the **Prisma Access Authentication
      Proxy**.
   3. In the **Gateway IP**field, paste the **egress IP
      Addresses**.
   4. Click **Save**.

      ![]()
   5. Confirm that the new zone appears in the list.

      ![]()
2. Select Applications and User Groups to Adhere to the Policy
   1. You need to create a new conditional access; Choose **Applications
      -> Applications** and click on the app that you want to
      restrict.
   2. Go to the **Sign On** tab, scroll down to the User
      Authentication and click **View policy details**.

      ![]()
   3. Click **Add rule** and enter the following information:

      - **Name:** Allow access only from the Prisma Browser.
      - **Users:** Select the users or user groups to
        enforce:
      - **User's group membership includes** - make sure that you
        configure this setting for groups.
      - **User is** - Allows you to apply rules to some specific
        users, but not to other specific users.

        ![]()
      - **Device Platform is** - Make sure you select both
        Windows and macOS.
      - **User IP is**  Select **Not in any of the following
        zones**, and select **Prisma Access Authentication
        Proxy**.
      - **Access is** - Select *Denied*.

      - Click **Save**.
3. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click **Okta**.

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser

##### Configure Microsoft Azure Active Directory IP-Based Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use Microsoft Azure Active Directory.

The Prisma Browser uses the Authentication Proxy for
the SSO login pages only. It does not use the proxy for any other
traffic.

You need Microsoft P2 Premium
licenses at a minimum, including Microsoft 365 business to enable this
enforcement.

##### Configure the Prisma Browser Application Enforcement IP Addresses

1. Create a new **Named Location** from the Azure Active Directory Admin
   Center.
   1. Search for the **Named Locations** from the Admin Center. If
      available, select the *New and improved Named Location*.

      ![]()
   2. Click **IP range location**.

      ![]()
   3. In the **New Location <IP> Ranges** section, enter the name
      of the Prisma Browser IP Range.
   4. Paste the egress IP Addresses into a text file.
   5. **Upload** the file.

      ![]()
   6. Click **Create**.
   7. Confirm that the new Named Location appears on the list.

      ![]()
2. Select Applications and User Groups to Adhere to Policy
   1. Navigate to the Azure Conditional Access Portal.
   2. Select **New Policy → Create New Policy** , and enter the
      following information:

      - **Name -** Enter a name. For example, *Block access not
        from Prisma Browser*.
      - **Assignments -** Assign the policy to users or groups.
        Be sure to include all users who need to connect to
        applications using the Prisma Browser only.
      - **Target Resources -** Make sure that the **Control
        access** includes cloud apps.
      - **Conditions -** Apply any needed conditions. Include at
        least one local condition.
      - **Grant -** Select *Block access*.
      - **Cloud apps or actions -** Select *Cloud apps*,
        then include selected applications.

      The Prisma Browser can't be a
      required application for enforcement.

      If you select **All
      apps**, be sure to *exclude* the Prisma Browser.

      - **Enable policy -**  Set this to *On*.
   3. Click **Create**.

   ![]()
3. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click **Microsoft Azure
      Active Directory**.

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser

##### Configure OneLogin IP-Based Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use OneLogin.

1. Configure the Prisma Browser Application Enforcement IP Addresses
   1. In the OneLogin toolbar go to **Security -> Policy** .
   2. Click **New App Policy**.

      ![]()
   3. Enter a name to identify the policy. For example, *Enforce Access
      from the Prisma Browser only*.
   4. In the **IP Address Whitelist**, copy and paste the egress IP
      Addresses.
   5. Click **Save**.
2. Click Select Applications and User Groups to Adhere to Policy
   1. On the OneLogin toolbar go to **Application →
      Applications**.
   2. Click **Add App**.

      ![]()
   3. In the **Found Applications** field. search for the application
      that you need to add.
   4. Click **Save**.
   5. Select **Access**.
   6. In the drop down before the Policy Title, select **Enforce Access
      from the Prisma Browser only**.
   7. Repeat steps b-f for each application that you want to add
      enforcement access.

      The Prisma Browser can't be a
      required application for enforcement.
   8. Select **Users**.
   9. Select the Users or Groups that must adhere to the **Enforce
      Access from the Prisma Browser only** policy.

      ![]()
3. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click **v** .

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser

##### Configure PingOne IP Based Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use PingOne.

1. Configure the Prisma Browser Application Enforcement. In the PingOne
   Admin Console, perform the following steps:
   1. Select **Connection → Application**, select the Prisma Browser application, and click the vertical ellipse.

      ![]()
   2. Click **View**.

      ![]()
   3. Select the **Policy Rules** tab and click the pencil icon.
   4. Click **Add Policy Rules**.
   5. In the Edit Policies window, select **Multi\_Factor**, and click
      **Save**.

      ![]()
   6. Select **Overview** and click **PingID**.

      1. Click on the **Services +** and add the **PingID**
         service.

         ![]()
      2. Click on **PingID** and continue the process. 

         ![]()
      3. Select the **Policy** tab and click **Add Policy**.

         ![]()
   7. In the **New Policy** page, enter the following information:

      1. In the **Name** field, enter an identifying name.
      2. In the **Application** section, select the applications
         that you want to apply conditional access enforcement.
      3. In the **Groups** section, select **All Groups**.

         ![]()
      4. If an application does not appear on the list:
      1. Make sure that the application has multi-factor
         authentication enabled.
      2. Under *PingFederate Applications*, click **Add
         Application** to add the application to the list.
   8. In the Rules section, click **Add Rule**.

      1. For **Select a Condition**, choose **Accessing from a
         company network**.

         ![]()
      2. For **Action** select **Approve**.
      3. For the IP addresses, manually copy and paste the egress IP
         addresses as comma-separated-values.
      4. In the **Default Action** section, choose **Deny**.
      5. Click **Save**.
   9. Click the **Configuration** tab and scroll down to the
      **Policy** section.

      1. Enable **Enforce Policy**.
      2. Enable **Policy for Windows Login**.
      3. Click **Save**. 

         ![]()
2. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click
      **PingOne**.

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser

##### Configure JumpCloud Based IP Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use JumpCloud.

1. Configure the Prisma Browser Application Enforcement. In the JumpCloud
   Admin Portal, perform the following steps:
   1. Select **Security Management -> Conditional Lists** and click
      the **+**.

      ![]()
   2. In the **New IP List**, enter the following information:

      1. **List Name -** Prisma Access Authentication Proxy.
      2. **Description -** Enter an optional description for the
         list.
      3. **IP Addresses -** Enter the list of egress IP
         addresses.

      Click **Save**. 

      ![]()

      A message will display indicating that the list was created. 

      ![]()
   3. Select **Security Management -> Conditional Policies** and click
      the **+**.

      ![]()
   4. Click **User Portal**.

      ![]()
   5. In the **General Info** section, enter the following
      information:

      - **Policy Name -** Enter a name for the policy, for
        example - *Allow access only from the Prisma Browser*.
      - **Description -** Enter an optional description.
      - **Policy Status -** Make sure that this is set to
        'On'.

      ![]()
   6. In the **Assignments** section, click **All Users** or
      **Select User Groups**.

      ![]()

      Admins can select All Users or individual user groups.
      Additionally, admins can select groups that are to be excluded
      from the policy.

      For example, the policy can be applied to all users, but the
      admins can be excluded.
   7. In the **Conditions** section, do the following:

      - Click **Add conditions**  and select **IP
        addresses**.
      - IP address**:** Select **not on list**, and for the
        list - select **Prisma Access Authentication
        Proxy**.
   8. In the **Action** section, enter the following information:

      - For **Access**, select **Denied**.
      - For **Authentication**, select based on your corporate
        policy.

      ![]()
2. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click
      **JumpCloud**.

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser

##### Configure VMware Workspace ONE IP Based Enforcement

Follow these steps to limit access to all or specific
apps to the Prisma Browser when you use VMware Workspace ONE.

1. Configure the Prisma Browser Application Enforcement. In the Main
   Access Portal page, perform the following steps:
   1. On the main Access Portal page, select **Resources ->
      Policies,** and click **Network Ranges**.

      ![]()
   2. Click **Add Network Range**.

      ![]()
   3. Enter a **Name** and **Description** for the Network
      Range.
   4. manualle enter each row of the egress IP addresses.

      The values must be entered as "from -to"
      without including the subnet mask.

      ![]()
   5. Click **Save**. The new Network Range will be added to the list.

      ![]()
2. Select Applications and User Group to Adhere to Policy
   1. On the main Access Portal page, select **Resources ->
      Policies,** and click **Add Policy**.

      ![]()
   2. On the **Definition** page, enter a name and a description for
      the **Policy**.
   3. Select the relevant application in the **Applies to**
      field.

      ![]()

      The Prisma Browser cannot be a
      required application for enforcement.
   4. Click **Next**.
   5. On the **Configuration** page, click **Add Policy Rule**, and
      provide the following information:

      1. **If a user's network range is -** Select the
         **Range Name** defined in the previous step.**If a
         user's network range is** – Select the **Range
         Name** defined in the previous step.
      2. **and the user accessing content from** – All Device
         Types.
      3. **and the user belongs to a group** – Select the affected
         group (optional).
      4. **Then perform this action** – Authenticate using…
      5. **then the user may authenticate using** – Password
         (Local Directory)

      ![]()
   6. Click **Save**. The new policy will be displayed,
   7. Click **Next** and review the **New Access Policy
      Summary**.
   8. Click **Save**. The new policy will be added to the policy
      list.
3. Enable IdP Enforcement in the Prisma Access Console
   1. In the Strata Cloud Manager, navigate to **Workflows → Prisma Access Setup → Prisma Browser****Configuration → Prisma Browser →
      Onboarding** .
   2. In the **Onboard Users** section, Locate Prisma Browser and
      click **View**.
   3. In the Prisma Browser Setup page, click **Step 4: Enforce SSO
      Applications.**
   4. Select the appropriate IdP. In this case, click **VMware Workspace
      ONE**.

      From this point on, users will only be able to access the SSO
      applications via the Prisma Browser.

---

<a id="third-party-integrations"></a>

#### Third-Party Integrations

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations>*

A link to all the third-party integration apps.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

Prisma Access Browser works with the following third-party services:

- [Microsoft 365](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-microsoft-365.html) This feature will be
  deprecated in March 2026.
- [Microsoft Information
  Protection](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-microsoft-information-protection.html)
- [Windows Account-Based SSO Authentication](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/windows-account-based-sso-authentication.html)
- [Google Workspace](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-google-workspace.html)
- [Votiro](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-votiro.html)
- [CrowdStrike Falcon
  Intelligence](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-crowdstrike-falcon-intelligence.html)
- [OPSWAT MetaDefender](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-opswat-metadefender.html)
- [Enforce PAB Mobile Access on
  Managed Devices Using MDM App Configuration](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/enforcing-prisma-access-browser-mobile-access-on-managed-devices-usiing-mdm-app-configuration.html)

---

<a id="enforce-prisma-access-browser-mobile-access-on-managed-devices-using-mdm-app-configuration"></a>

##### Enforce Prisma Access Browser Mobile Access on Managed Devices Using MDM App Configuration

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/enforcing-prisma-access-browser-mobile-access-on-managed-devices-usiing-mdm-app-configuration>*

Enforcing PAB Mobile Access on Managed Devices Using MDM App
Configuration

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or Prisma Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Symantec DLP |

###### Overview

This feature allows you to ensure that only MDM-managed mobile devices can sign in to
Prisma Access Browser (PAB) Mobile. By integrating with your existing MDM (Mobile
Device Management) solution, you can enforce PAB sign-in policies based on device
management status and reuse existing MDM compliance rules.

###### Key Benefits

- **Secure Access**: Enforce that only MDM-enrolled, compliant devices can
  access PAB.
- **Reuse Compliance Rules**: No need to redefine device posture separately in
  PAB—leverage what’s already set in your MDM.
- **MDM-Agnostic**: Works with all major MDM vendors (e.g., Intune, Jamf,
  Workspace ONE) via standard AppConfig.

###### Deployment Considerations

To implement this feature, ensure that your MDM solution is configured to enforce the
necessary compliance checks and that Prisma Access Browser Mobile is deployed with
AppConfig support enabled. Review your organization's compliance policies and verify
that they align with your access requirements.

This
feature is MDM-agnostic. For the purposes of this article, the examples are made
using Microsoft Intune.

###### How to Configure the Feature

###### Configure the MDM for iOS Browsers

You can configure Microsoft Intune as the MDM that will be used to enforce
Prisma Access Browser Mobile access on iOS-devices. Configure Microsoft Intune as
follows:

1. Log into the [Intune application](https://intune.microsoft.com).and click **Add** from
   the menu. 

   ![]()
2. On te Overview page, select the platform that you need. If you are using iOS or
   iPadOS, click **iOS/iPadOS**.

   ![]()
3. On the iOS/iPadOD apps page, do the following:
   1. Click **Create.**
   2. In the **Select app type drawer**, locate the App type list, and
      select **iOS store app.**
   3. Click **Select.**

      ![]()
4. In the **Add App** page, click **Search the App Store.**
5. In the **Search the App Store** window, begin typing the name of the
   application, *PA Browser*, and click **Search**. When it appears in the
   list, click **PA Browser**, the click **Next**. 

   ![]()
6. On the **Add App - App Information** page, verify the following information:
   1. **Name**: The name of the app. This name will be visible in the
      Intune apps list and to users in the Company Portal.​. We recommend that
      you use the default - PA Browser, although you can change it if needed.
   2. **Description:** Help your device users understand what the app is
      and/or what they can do in the app. This description will be visible to
      them in the Company Portal. We recommend that you use the default text.
   3. **Minimum operating system**: Select the earliest operating system
      version on which the app can be installed. If you assign the app to a
      device with an earlier operating system, it will not be installed.
   4. **Applicable device types**: Select the device types that can install
      the app. - the options are:
      1. iPad
      2. iPhone and iPod

         You can select or
         remove either of the selections as needed. For example, if
         you do not want your users to install on iPad devices, clear
         the field.
   5. The rest of the fields can be left blank, or left with the default
      data.
   6. Click **Next**. 

      ![]()
7. On the **Add App - Assignments** page, you can set any specific assignments
   that you need. There are 4 assignment types:
   1. **Required**

      Select the user groups for which this app should be required. When an
      app is marked as required, the system automatically installs it on
      all devices enrolled under those selected groups.

      This
      automation ensures that users receive the app without needing to
      manually install it, helping maintain consistency and compliance
      across the organization.

      Be aware that some device platforms
      (such as iOS or Android) may display system-level prompts to the
      user before the installation begins. These prompts can include
      installation consent, permission requests, or security warnings that
      must be acknowledged before the app is fully
      installed.

      **Available Assignments:**
      1. **Add group**: Select an Microsoft Entra group to assign
         the application to a group containing licensed users or
         managed devices.
      2. **Add all users**: Selecting “Add all users” creates an
         assignment for all Intune licensed users in your
         organization. You can only use “All users” for one type of
         assignment. Additionally “All users” can not be excluded.
      3. **Add All devices**: Choosing 'Add all devices' assigns
         the app to every device enrolled in Intune. You can apply
         this option to only one assignment type—such as Required,
         Available, or Uninstall.

         **All
         devices** cannot be excluded from any assignment
         configuration.
   2. **Available for enrolled devices**

      When configuring app assignments in Intune, you can choose to make
      the app **available** rather than required. This option gives
      users the flexibility to install the app from the **Company Portal
      app or website** on their enrolled devices, based on their
      individual needs.

      To do this, select the appropriate **user
      groups** that should have access to the app. Members of these
      groups will see the app listed in their Company Portal but will not
      have it automatically installed. This approach is ideal for
      non-critical apps, productivity tools, or department-specific
      software that may not be relevant to all users.

      The **‘Available for
      enrolled devices’** assignment only supports **User
      Groups**. You **cannot** assign apps in this mode to
      Device Groups. If you attempt to assign to a Device Group, the
      app will not appear in the Company Portal for
      users.

      **Available Assignments**
      1. **Add group**: Select an Microsoft Entra group to assign
         the application to a group containing licensed users or
         managed devices.
      2. **Add all users**: Selecting “Add all users” creates an
         assignment for all Intune licensed users in your
         organization. You can only use “All users” for one type of
         assignment. Additionally “All users” can not be excluded.
   3. **Available with or without enrollment** 

      When configuring app
      availability in Intune, you have the option to offer an app to users
      **with or without requiring device enrollment**. This setting
      provides flexibility for organizations that want to enable app
      access without enforcing full device management—particularly useful
      in BYOD (Bring Your Own Device) scenarios or for users accessing
      services on personally owned devices.

      **Available
      Assignments**
      1. **Add group**: Select an Microsoft Entra group to assign
         the application to a group containing licensed users or
         managed devices.
      2. **Add all users**: Selecting “Add all users” creates an
         assignment for all Intune licensed users in your
         organization. You can only use “All users” for one type of
         assignment. Additionally “All users” can not be excluded.
   4. **Uninstall**

      ​​Choose the user groups from which you want to remove the app.
      Intune will uninstall the app from managed devices in these
      groups—provided the app was initially installed via a 'Required' or
      'Available for enrolled devices' assignment within the same
      deployment.

      **Available Assignments:**
      1. **Add group**: Select an Microsoft Entra group to assign
         the application to a group containing licensed users or
         managed devices.
      2. **Add all users**: Selecting “Add all users” creates an
         assignment for all Intune licensed users in your
         organization. You can only use “All users” for one type of
         assignment. Additionally “All users” can not be excluded.
      3. **Add All devices**: Choosing 'Add all devices' assigns
         the app to every device enrolled in Intune. You can apply
         this option to only one assignment type—such as Required,
         Available, or Uninstall.

         **All
         devices** cannot be excluded from any assignment
         configuration.
   5. Click **Next**. 

      ![]()
8. On the **Add App - Review + create** carefully review the information for the
   app and make sure that it is correct. When you are certain that the information
   is correct, click **Create**. 

   ![]()
9. The application dashboards are displayed. 

   ![]()

###### Configure the MDM for Android Browsers

You can configure Microsoft Intune as the MDM that will be used to enforce Prisma
Access Browser Mobile access on Android devices. The method is very similar to the
method for iOS, with a few changes. This section will cover the differences.
Configure Microsoft Intune as follows:

1. Log into the [Intune application](https://intune.microsoft.com).and click **Add** from
   the menu. 

   ![]()
2. On the Overview page, select the platform that you need. If you are using
   Android devices, click **Android**. 

   ![]()
3. On the **Android apps** page, do the following:
   1. Click **Create**.
   2. In the Select app type drawer, locate the App type list, and select the
      **Android store app**
   3. Click **Select.**
4. In a separate browser window, open the Google Play store, and search for the P A
   Browser, and copy the URL (currently <https://play.google.com/store/apps/details?id=com.talonsec.talon&hl=en>).
5. On the **Add App - App Information** page, you need to enter the following
   information:
   1. **Name**: Add a name for the app. This name will be visible in the
      Intune apps list and to users in the Company Portal.​. We recommend that
      you use *PA Browser*.
   2. **Description**: Help your device users understand what the app is
      and/or what they can do in the app. Add a short description that will be
      visible to them in the Company Portal.
   3. **Application URL**: Paste the URL from the Google Play Store. This
      is the URL from step 4 above.
   4. **Minimum operating system**: Select the earliest operating system
      version on which the app can be installed. If you assign the app to a
      device with an earlier operating system, it will not be installed.
   5. The rest of the information can be left blank.
   6. Click **Next**. 

      ![]()
6. On the **Add App - Assignments** page, you can set any specific assignments
   that you need. See above for more information.
7. On the **Add App - Review + create** carefully review the information for the
   app and make sure that it is correct.

When you are certain that the information is correct, click **Create**.

###### Configure the Prisma Access Browser

**1. Create a Device group with MDM Posture**

1. In the Prisma Access Browser, navigate to **Directories → Devices**.
2. Click the **Device Groups** tab.
3. Click **Add device group.**
4. In the Group name and platform, enter a **name** for the group and click
   **Mobile Browser**.
5. Click **Device group attributes.**

   ![]()
6. In the Device group attribute page, select **Mobile Device Management**
   and click **Configure**. 

   ![]()
7. Select the mobile device management vendor that is relevant for your
   organization and click **Set**. 

   ![]()
8. The system will generate a unique management key (Configuration value) for
   each selected MDM vendor. 

   ![]()
9. Copy the Configuration value.
   - Click the Copy icon to copy the configuration value. The
     configuration value is the management key that must be passed to the
     Prisma Access Mobile Browser application via the MDM AppConfig.

**2. Open the MDM Console**

Use the following process to push the management key to the Prisma Access mobile
Browser via AppConfig.

1. Search and add the PA Browser to your Managed Apps. 

   ![]()
2. Configure the App configuration policy.
   1. In the MDM, go to **Apps → Configuration → Create → Managed
      device**.
   2. Select the appropriate platform, either **iOS** or
      **Android**.
   3. Target the PA Browser app.
   4. Under the Configuration settings format, select **Use configuration
      designer**.
   5. Click **Add → Select MDM configuration key → OK**.
3. Define the App Configuration Settings. This is where you will add the
   key-value pair in the configuration:
   - **Value**: Enter the Configuration value from the Prisma Access
     Browser console.

     To avoid
     accidentally mistyping this value, we recommend that you copy
     the value and paste.

     ![]()
   - Click **Next**.

   Ensure that this configuration is only applied to devices that meet
   your compliance criteria,

For other MDMs, such as Jamf or Workspace ONE, the
process is similar—create an AppConfig with the pab\_management\_key and assign it
to relevant devices/groups.

###### Test the Rule Configuration

You can easily test the configuration that you created here:

1. Create two sign-in rules:
   1. A sign-in rule that blocks all (unmanaged) mobile devices.
   2. A sign-in rule for the device group you created above, and allow
      that group.
2. Attempt to sign in from an unmanaged device and a managed device with the
   Intune key.
   - If the unmanaged device is denied access, and the managed device is
     allowed access, then the policy works as expected.

###### What Happens on the Device

- On start-up, the PAB app reads the configuration value using platform-native
  AppConfig APIs.
- The key is matched against SHA256 hashes of valid configuration value from the
  console.
- If there's a match, the device is allowed into the relevant device group, and
  sign-in proceeds according to your policy.
- **If there's no match, access is denied**.

###### Platform Notes

###### -iOS

- Uses com.apple.configuration.managed via
  UserDefaults.
- Requires no entitlements or special permissions.
- Works as long as the app is managed and installed via MDM.

###### -Android

- Requires defining
  res/xml/managed\_configurations.xml in the app and
  referencing it in AndroidManifest.xml.
- MDM will use this definition to show editable keys.
- The PAB app reads the configuration from the
  RestrictionsManager system service.

###### Security Considerations

- Only managed apps can read the managed key.
- End users and other apps cannot access the key unless the device is
  rooted or jailbroken.
- Keys can be rotated anytime in the MDM and PAB console.
- Security is at least equivalent to PAB Desktop/Mac MDM
  detection.

---

<a id="integrate-prisma-browser-with-crowdstrike-falcon-intelligence"></a>

##### Integrate Prisma Browser with CrowdStrike Falcon Intelligence

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-crowdstrike-falcon-intelligence>*

Integrate Prisma Browser with CrowdStrike Falcon Intelligence to scan files and
URLs for malicious actors.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - CrowdStrike Falcon Intelligence |

You can integrate the Prisma Browser with CrowdStrike Falcon Intelligence to
enable you to scan files and URLs for malicious actors by using the Falcon
Intelligence API.

After you integrate the Prisma Browser with CrowdStrike Falcon Intelligence, your
Prisma Browser users will be able to use it as a file scanning engine. For
more information, refer to [Malicious File Protection](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls).

The Falcon Intelligence Quick Scan will scan only the
following file types. It will ignore other file types.

- doc, docx
- pdf
- xls, xlsx, xlsm
- ppt, pptx, pptm
- exe
- dll
- mach-0

Before you begin, ensure that you have access to the Falcon user interface with an
Administrator role.

1. To enable the CrowdStrike Falcon Intelligence integration in Strata Cloud Manager.
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to CrowdStrike Falcon Intelligence
      Integration and expand it.
   3. Click Enabled, then enter the following
      information (obtained from CrowdStrike):

      - Client ID
      - Client Secret
      - Gateway API URL
   4. Click Save.
   5. If Falcon CrowdStrike Intelligence does not recognize a file, you can
      optionally submit the file to Falcon CrowdsStrike Intelligence Quick
      Scan and Sample Uploads. To enable this option, select If the
      file is unknown to Indicators (Falcon Intelligence), submit it to
      Falcon Intelligence QuickScan.

---

<a id="integrate-prisma-browser-with-google-workspace"></a>

##### Integrate Prisma Browser with Google Workspace

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-google-workspace>*

Learn how to integrate the Prisma Browser with Google Workspace.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Google Workspace |

You can use Google Workspace with custom or third-party applications to enrich
existing Google Workspace services or to use new features with Google Workspace.
After you integrate Prisma Browser with Google Workspace, your users will be
able to open only the applications that you’ve assigned to the Prisma Browser.

Before you begin, ensure that you complete the following tasks:

- Deploy the Context-Aware Access feature in Google Workspace, which is
  available for Enterprise and Education accounts or with Cloud Identity
  Premium.
- Set up SSO authentication to Prisma Browser with Google.

1. Enable the Google Workspace integration in Strata Cloud Manager and obtain the
   Prisma Browser certificate:
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to Google Workspace Integration and
      expand it.
   3. Click Enabled.
   4. In part 1, select Prisma Browser
      Certificate. The certificate will download.

      ![]()
2. Add the certificate for Prisma Browser in the Google Admin console.
   1. Go to [Google Admin consoleDevicesNetworks](https://admin.google.com/ac/networks).
   2. Click Certificates, then ADD
      CERTIFICATE, and upload the Prisma Browser
      certificate that you downloaded.
   3. Select Endpoint Verification and click
      ADD.
3. Create a new access level in the Google Admin console.
   1. Go to [Google Admin ConsoleSecurityAccess and data controlContext-Aware Access](https://admin.google.com/ac/security/context-aware).
   2. If Context-Aware Access is disabled, enable it.
   3. Click Access levels, then CREATE NEW ACCESS
      LEVEL.
   4. Name the new access level Prisma Browser or any other name of your choice.
   5. Select ADVANCED and paste the following
      text:

      device.certificates.exists(cert, cert.is\_valid &&
      cert.root\_ca\_fingerprint ==
      "kiLbsQhDpeCsDkM6ox2oHiaxOiQQ45u8FV1AmeQxc9E")
4. Assign the new access level to your apps.
   1. Go to [Google Admin ConsoleSecurityAccess and data controlContext-Aware Access](https://admin.google.com/ac/security/context-aware).
   2. Click Assign access levels.
   3. Select one or more apps in the list and click
      Assign.
   4. Select the newly Prisma Browser access level that you created in
      Step [3](#integrate-prisma-browser-with-google-workspace).
5. Validate the integration on an endpoint.
   1. Install the Prisma Browser on an endpoint.
   2. Wait for the new Google Workspace configuration to complete, usually 5
      minutes.
   3. From the Prisma Browser, sign in to an assigned app and test the
      following:

      - Make sure that you can successfully sign in to an application
        that uses the Google Workspace SSO.
      - Make sure that you can't sign in to the application from a
        different browser.

      After you complete the validation, and your users will be able to
      open only the applications that you’ve assigned to the new access
      level using the Prisma Browser.

---

<a id="integrate-prisma-browser-with-microsoft-365"></a>

##### Integrate Prisma Browser with Microsoft 365

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-microsoft-365>*

Integrate Prisma Browser with Microsoft 365 (formerly Office 365) to enable your
users to open encrypted documents in the Prisma Browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Microsoft 365 |

**This feature will be deprecated in
March 2026.**

You can integrate Prisma Browser with Microsoft 365 (formerly Office 365)
to allow your users to open encrypted documents in the Prisma Browser.

To integrate with Microsoft 365, you will need to obtain the tenant ID and client ID
from the Microsoft Azure portal, and then enable the integration in Strata Cloud Manager.

1. Find your tenant ID.
   1. Sign in to the [Azure portal](https://portal.azure.com/).
   2. Make sure you're signed in to the tenant you want to find the ID for.
      If you're not in the correct tenant, [switch directories](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences#switch-and-manage-directories) .
   3. Under Azure services, select Microsoft Entra ID.
      If you don't see Microsoft Entra ID, use the search function to find
      it.
   4. Locate the Tenant ID in the
      Overview page.
2. Obtain your Microsoft 365 application (client) ID.
   1. Log in to the [Azure portal](https://portal.azure.com/).
   2. Make sure you're signed in to the correct tenant If you're not in the
      correct tenant, [switch directories](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences#switch-and-manage-directories) .
   3. Under Azure services, select Microsoft Entra ID.
      If you don't see Microsoft Entra ID, use the search function to find
      it.
   4. Under Manage, select App registrationsNew registration.
   5. Enter a display Name for your application. Your
      users will see the display name when they interact with the app.

      You can change the display name at any time or use it for multiple
      app registrations. It doesn't affect the automatically generated
      Application (client) ID, which uniquely identifies your app.
   6. Specify which users can use the application.
   7. For Redirect URI, select Single Page
      Application (SPA) and provide the following URI: [Microsoft 365](https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org/).
   8. Click Register.

      When registration finishes, you can find the Application
      (client) ID in the app registration's Overview
      page.
3. Enable the integration in Strata Cloud Manager.
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to Office 365 Integration and expand
      it.
   3. Click Enabled, then enter the Microsoft 356
      Tenant ID and Client
      ID.
   4. Click Save.

   The following file types are supported:
   - doc, dot, docx, dotx, dotm, docm
   - xls, xlt, xla , xlsx, xltx, xlsm, xltm, xlam, xlsb
   - ppt, pot, pps, pptx, potx, ppsx, ppam, pptm, potm, ppsm
   - mdb

---

<a id="integrate-prisma-browser-with-microsoft-information-protection"></a>

##### Integrate Prisma Browser with Microsoft Information Protection

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-microsoft-information-protection>*

Integrate Prisma Browser with Microsoft Information Protection to enable Prisma Browser to read the labels when downloading and uploading files and enforce an
appropriate policy.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Microsoft Information Protection |

The Microsoft Information Protection (also known as Microsoft Purview) is an external
system that classifies and labels files. By integrating with Microsoft Information
Protection, you enable the Prisma Browser to read the labels when downloading
and uploading files and enforce an appropriate policy.

1. Find your tenant ID.
   1. Sign in to the [Azure portal](https://portal.azure.com/).
   2. Make sure you're signed in to the correct tenant. If you're not in the
      correct tenant, [switch directories](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences#switch-and-manage-directories) .
   3. Under Azure services, select Microsoft Entra ID.
      If you don't see Microsoft Entra ID, use the search function to find
      it.
   4. Locate the Tenant ID in the
      Overview page.
2. Obtain your client ID.
   1. Sign in to the [Azure portal](https://portal.azure.com/).
   2. Make sure you're signed in to the correct tenant. If you're not in the
      correct tenant, [switch directories](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences#switch-and-manage-directories) .
   3. Under Azure services, select Microsoft Entra ID.
      If you don't see Microsoft Entra ID, use the search function to find
      it.
   4. Under Manage, select App registrationsNew registration.
   5. Enter a display Name for your application. Your
      users will see the display name when they interact with the app.

      You can change the display name at any time or use it for multiple
      app registrations. It doesn't affect the automatically generated
      Application (client) ID, which uniquely identifies your app.
   6. Specify which users can use the application.
   7. For Redirect URI, select Single Page
      Application (SPA) and provide the following URI: [https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org](https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org/).
   8. Click Register.

      When registration finishes, you can find the Application
      (client) ID in the app registration's Overview
      page.
3. Configure the required permissions for the app.
   1. After the registration, under Manage, select
      Authentication. Under Implicit
      grant, select both Access tokens
      and ID tokens.
   2. Under API permissions, select Add a
      permission. Select APIs my organization
      uses, and search for Microsoft Information Protection
      Sync Service. Select Delegated permissions and
      add the UnifiedPolicy.User.Read permission.
   3. Under API permissions, select Add a
      permission. Select Microsoft
      APIs, and select Microsoft Graph.
      Choose Delegated permissions and add the email
      and openid permissions.
   4. Under API permissions, select Grant
      admin consent for <Organization Name>.
   5. Under Token configuration, select Add
      optional claim. Select ID, and
      add email.
4. Enable the integration in Strata Cloud Manager.
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to Microsoft Information Protection
      Integration and expand it.
   3. Click Enabled, then enter the Tenant
      ID and Client ID.
   4. Click Save.

---

<a id="integrate-prisma-browser-with-opswat-metadefender"></a>

##### Integrate Prisma Browser with OPSWAT MetaDefender

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-opswat-metadefender>*

Integrate the Prisma Browser with the OPSWAT MetaDefender to prevent and detect
cybersecurity threats in file downloads.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Browser bundle license or   Prisma Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - OPSWAT MetaDefender |

The OPSWAT MetaDefender uses a Zero Trust policy to scan and sanitize files.
Integrate the Prisma Browser with MetaDefender to prevent and detect
cybersecurity threats across multiple data channels. MetaDefender uses Content
Disarm and Reconstruction (CDR) to remove threats from files by scanning, removing
malicious content and scripts from the files, and reconstructing them.

After you integrate the Prisma Browser with the OPSWAT MetaDefender, your Prisma Browser will be able to use it as a file scanning engine. For more
information, refer to [Malicious File Protection](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls).

1. Obtain an API key from MetaDefender.
   1. Sign in to the OPSWAT MetaDefender interface using the Administrator
      role.
   2. Go to User Management.
   3. ClickAdd User, define the user, and generate the
      API Key.
   4. Copy the API Key and save it to a text file or
      another location.
2. Enable the OPSWAT MetaDefender integration in Strata Cloud Manager.
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to OPSWAT MetaDefender Integration and
      expand it.
   3. Click Enabled, then enter the
      MetaDefender URL and API
      Key that you saved earlier.
   4. Click Save.

---

<a id="integrate-prisma-browser-with-votiro"></a>

##### Integrate Prisma Browser with Votiro

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/integrate-prisma-access-browser-with-votiro>*

Integrate the Prisma Browser with Votiro to scan and sanitize files that your
users download or upload using the Prisma Browser.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Votiro |

You can integrate the Prisma Browser with Votiro to protect your organization
from zero-day and undisclosed attacks by sanitizing files that your Prisma Browser users download or upload. Using Votiro's file sanitization technology, you can
ensure that every downloaded or upload file in the Prisma Browser is free from
threats.

After you configure the Vitiro integration, your Prisma Browser users will be
able to use it as a file scanning engine. For more information, refer to [Malicious File Protection](https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls).

1. Obtain the Votiro token.
   1. Sign in to the Votiro management UI as the administrator.
   2. Go to ConfigurationService Tokens.
   3. Create a new integration and copy the generated token to the
      clipboard.
2. Enable the Votiro integration in Strata Cloud Manager.
   1. Go to ConfigurationPrisma BrowserAdministrationIntegrationsServices.
   2. Scroll to Votiro Integration and expand
      it.
   3. Click Enabled, then enter the Votiro
      URL and Votiro Token that you
      obtained.
   4. Click Save.

---

<a id="windows-account-based-sso-authentication"></a>

##### Windows Account Based SSO Authentication

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/integrations/third-party-integrations/windows-account-based-sso-authentication>*

This article discusses using the new Account based sso Authentication

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - Standalone Prisma Browser | - Prisma Access with Prisma Access Browser bundle license or   Prisma Access Browser standalone license - Role: [Prisma Access Browser   Roles](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-roles.html) - Microsoft 365 |

This feature is available for Microsoft Windows and macOS
devices.

Because this feature uses local logged in users for
authentication against web applications, we advise that you use this feature on managed
devices only, to avoid unexpected logins from unmanaged domains.

This update supports local account-based authentication via Microsoft Single
Sign-On (SSO) and Active Directory (AD) integration, addressing key needs:

- **Passwordless Authentication** - Enables secure access for users without
  traditional passwords, improving accessibility and reducing friction.
- **Stronger Admin Controls** - Allows IT admins to enforce authentication through
  corporate-managed SSO accounts, minimizing unauthorized access and reducing reliance
  on passwords.

Taking advantage of this new capability, Prisma Access Browser now has a method
for incorporating the Microsoft solution into our commitment to secure solutions that
align with modern enterprise needs, especially as hybrid and remote work models
grow.

###### Login to Browsers with Local Windows Accounts

You can enable browser logins using local Windows accounts linked to Active
Directory.

**How It Works:**

You need to set a local registry key on managed devices to configure this
feature. The key is

```
reg add "HKLM\Software\Policies\Palo Alto Networks\PrismaAccessBrowser" /v
          ForceEnableMsSSO /t REG_DWORD /d 1 /f
```

![]()

Using this, your users only need to enter their username (e.g.,
richarddorlinger@example.com). When they log in, their credentials are authenticated
against the local machine. This ensures that the enter username matches the locally
logged-in user.

###### Automatic Web Application Sign-In Using Microsoft Entra ID

You can leverage Prisma Access Browser’s capabilities to enable
seamless authentication during Microsoft SSO flows for web applications.

**How It Works:**

Enable the Microsoft SSO control when you create a Browser
Customization rule. From Strata Cloud Manager, select **Configuration**>**Prisma Access Browser**>
**Policy**>**Profiles**>**Browser Customization**, and select
**Microsoft Auto-SSO**.

Once this is done, your users will be able to navigate to web
applications and experience automatic sign-in using Microsoft SSO, authenticated
via corporate Active Directory connections.

###### Support for Microsoft Entra on macOS Devices

Prisma Browser now supports Microsoft Enterprise SSO plug-in for Apple
devices. This allows users to seamlessly authenticate to Microsoft Entra web
apps.

**What you need to do:**

1. Deploy and configure the Enterprise Single Sign On plug-in for Apple
   configured on macOs devices. The information can be found on the [Microsoft Entra site](https://learn.microsoft.com/en-us/entra/identity-platform/apple-sso-plugin).
2. Make sure that the device is enrolled and has the Intune Company Portal,
   version **5.2504.0** or higher.
3. Make sure that the minimum Prisma Browser version is
   **136**.

---

<a id="captive-portal-experience"></a>

#### Captive Portal Experience

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/captive-portal-experience>*

Prisma Browser Captive Portal Experience

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

Prisma Browser provides a captive portal experience that maintains security
posture while giving users a reliable way to connect to networks that require sign-in.
The browser aims to deliver a seamless captive portal experience and enforce
enterprise-grade security controls. It replicates familiar browser behaviors where
possible but introduces additional safeguards to prevent policy bypass in untrusted
network states.

When a device connects to a new network (for example, public Wi-Fi), most
browsers and operating systems try to detect captive portals by performing lightweight
connectivity checks (e.g.,
http://connectivitycheck.gstatic.com/generate\_204).

If the request is redirected instead of returning a “no content” (HTTP
204) response, the browser infers that a captive portal is present. It then
opens a Wi-Fi sign-in window automatically to direct the user to authenticate or accept
terms. Once authenticated, the connection becomes unrestricted and normal browsing
resumes.

In some cases, the automatic captive portal detection flow is not
sufficient.

Common recovery actions include:

- Manually visiting known captive portal domains (for example,
  wifi.airline.com).
- Navigating to a popular website (for example, example.com) to
  trigger a redirection from the default gateway.

If your organization routes all traffic through Prisma Access
and the automatic captive portal detection does not open a sign-in window, use the
**Secure Wi-Fi Sign-In** window described below to complete network
authentication.

##### The Secure Wi-Fi Sign-in Window

To accommodate restricted network states, Prisma Browser provides a
dedicated Wi-Fi Sign-In Window. This window allows users to safely reach captive
portal pages in situations where existing security policies or conditions prevent
standard recovery patterns from working. Examples include:

- A strict policy that only allows navigation to specific websites.
- Stale or outdated policy states that temporarily block navigation in the
  main browser window.

**Manual Trigger**

If automatic detection and normal recovery paths fail, users can open the Wi-Fi
Sign-In Window manually:

**Path**

Menu (…)More ToolsWi-Fi Sign-In Window

![]()

**Window features:**

- The address bar is editable, allowing users to navigate directly to captive
  portal pages (for example, wifi.airline.com or a hotel
  login page).

  If you do not know
  the captive URL, navigate to a public domain (such as google.com). This
  triggers the network's Captive Portal redirect. This allows you to
  complete the sign-in process.
- All browsing occurs in a secure, sandboxed session to ensure that no user
  data is exposed and no security policies are bypassed.

![]()

****After authentication and restored connectivity:****

- Prisma Browser detects that the internet connection is active.
- The browser displays a notification informing the user that the Wi-Fi
  Sign-In Window is no longer needed.
- The user is prompted to close the Wi-Fi Sign-In Window and return to the main
  browser window, which now operates under validated Prisma Access
  policies.

  ![]()

---

<a id="set-up-and-use-the-prisma-browser"></a>

#### Set Up and Use the Prisma Browser

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-setup-and-use>*

Learn how to set up and use your Cloud managed Prisma Access Secure Enterprise Browser (Prisma Browser).

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Browser | - [Set up and   use](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-setup-and-use.html) |

1. Install the Prisma Browser.

   Your organization can select to deploy the Prisma Browser in several
   different ways:

   1. It can be deployed by your administrators in a silent mode - that is -
      without any need for end-user intervention.
   2. Your administrator can send you a link to the internal version of the
      application that was tested and customized by your administrators.
   3. Your administrator can direct you to the Prisma Browser download
      site https://get.pabrowser.com
2. Verify that the Prisma Browser is Installed.

   After the browser has been deployed to your computer, you will see the
   browser icon on your desktop. Double-click it to
   launch the Prisma Browser. If you don't see the Prisma Browser icon
   on your desktop:

   1. If the Prisma Browser does not appear on your desktop, use the
      taskbar search function and search for Prisma Browser. If it
      appears, the Prisma Browser is installed on your computer.
   2. In the search results, right-click on the Prisma Browser icon, and
      select Pin to Taskbar.
   3. If you still can't locate the Prisma Browser on your computer,
      contact IT and provide them with the information they require.
3. Sign in.
   1. After the Prisma Browser launches, enter your work email address,
      then click Continue.
   2. Reenter your email password for your work address, then click
      Sign in.
   3. (Optional) If your organization has configured your account
      with two-factor authentication enabled, you will need to enter a
      PIN code or your biometric authentication to
      unlock the Prisma Browser every time you open it. If you use a
      PIN code, be sure to keep it safe.
4. Set Prisma Browser as your default browser.
   1. After you sign into your account, the Prisma Browser will relaunch
      with a welcome message.
   2. At the top of the homepage, select the link called Set as
      default browser to make sure that the Prisma Browser
      will be your default browser.
   3. This option sets Prisma Browser as the program associated with Web
      documents or links. Whenever a browser is needed, Prisma Browser
      will be the browser that opens.
5. Import data from your previous Prisma Browser.

   You can migrate your settings, data, and bookmarks from your previous browser
   to the Prisma Browser

   1. At the top of the homepage, select the link called Import
      browser data to make sure that the Prisma Browser
      will be your default browser.
   2. In the Import bookmarks and settings window,
      select the browser and profile to import. You will see a list of
      available settings that you can import. Settings from non-Chrome
      browsers may be limited.

      The available profiles and items to import are based on the
      browsers that are currently installed on your computer. If there
      are multiple profiles for the same browser, we recommend that
      you select the one that is your default profile on the browser
      that you use for your day-to-day work.
   3. All your bookmarks as well as other supported items should now be
      accessible through the Prisma Browser.

      After you import your bookmarks and other settings, all your
      browser-based work needs to be done using the Prisma Browser
      only.
6. Start work with the Prisma Browser.
   1. After the Prisma Browser is installed and configured on your
      system, you can start using it for your work.
   2. The browser has the same look and feel as the Chrome browser, so there
      are no complex features you need to learn, or keyboard shortcuts you
      need to unlearn. Switching to this tool is a seamless and easy
      experience.
7. Update the Prisma Browser.

   The Prisma Browser automatically checks for and installs
   updates in the background. When an update is ready, you may need to restart
   the browser. When this happens, you will receive an indication. In some
   cases, your IT department will monitor the updates and push the update to
   you when it's ready.

   1. In the upper-right corner of the browser, select
      Update.
   2. Select **Relaunch** to update the Prisma Browser. The browser
      will shut down, and restart. It will keep all open tabs.

   **How is Synced Data
   Stored?**

   Syncing with Prisma Access Browser's sync service is
   automatic. Every user's identity is assigned a unique key that encrypts
   the data that is sent and stored.

   Neither Palo Alto employees nor
   console administrators have access to these keys. Encryption keys are
   stored in a secret store that is only accessible with a token associated
   with the user account.

   A record of each access to the encryption
   key is maintained.

---

<a id="use-the-prisma-browser-control-pane"></a>

#### Use the Prisma Browser Control Pane

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-use-the-control-pane>*

Learn how to set up and use your Cloud managed Prisma Access Secure Enterprise Browser (Prisma Browser) control pane.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Browser | - [Set up and   use](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-setup-and-use.html) |

The Prisma Browser Control Pane provides additional tools and features that can
provide some information and tools for you as well as for end users.

1. Click on the Prisma Browser icon to open the pane.
2. If there are any issues, open the Troubleshoot page by clicking the
   shield icon next to the personal image. See
   Troubleshoot the Prisma Browser for more information on opening the page.
   The Troubleshooting page provides information on the status and diagnostics of
   the browser.
3. Use the following tools and features:
   1. Posture – Displays the Troubleshoot page, where
      you can see if there are any errors or issues with the Browser. This is
      accesses by clicking on the shield icon.
   2. Lock – Locks the Prisma Access Browser. It can
      only be unlocked with the PIN code, biometric authentication, or a
      passkey.
   3. Manage profiles – Applicable if you have
      multiple profiles. For example, you have multiple profiles over
      different Prisma Access Browser tenants.
   4. Logout – Logs out of the browser. You need to
      fully sign in again to access the browser.
   5. Getting started and customization – Provides
      some quick end-user information about the Prisma Access Browser and
      allows end users to customize their accounts with their picture and to
      import their bookmarks. For more information. See Getting Started and
      Customization.
   6. Show sidebar – Toggles the display of the
      sidebar. Your administrator must have the sidebar enabled to use this
      feature.

---

<a id="prisma-browser-user-guide-overview"></a>

#### Prisma Browser User Guide Overview

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-user-guide-overview>*

Learn about Prisma Access Secure Enterprise Browser (Prisma Browser), what it is, how data is
synced, the functionality, and the messages.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

|  |

##### Prisma Browser Overview

Prisma Browser is a browser designed specifically for enterprise use,
built on the Chromium platform and fortified with security features to protect users
and organizations against cyberthreats like phishing, malware, eavesdropping, and
data exfiltration.

The Prisma Browser combines the user-friendly interface and core
features of Google Chrome with enhanced security measures to provide a secure
browsing experience that maintains Chrome's simplicity and speed. This allows users
to enjoy the familiarity and convenience of Chrome while addressing its various
security weaknesses.

##### Prisma Browser Synced Data Storage

Syncing with Prisma Browser’s sync service is automatic. Every user's
identity is assigned a unique key that encrypts the data that is sent and
stored.

Neither Palo Alto Networks employees nor Prisma Browser console
administrators have access to these keys. Encryption keys are stored in a secret
store that is only accessible with a token associated with the user account.

A record of each access to the encryption key is maintained.

##### Prisma Browser Functionality

The Prisma Browser contains an impressive array of built-in security
features, including:

- Phishing protection
- Malware protection
- Network security capabilities

Even though Prisma Browser offers powerful and comprehensive protection
from online threats, no security solution is completely foolproof. We strongly
encourage you to always remain vigilant when browsing and to exercise discretion and
vigilance when sharing information online.

The Prisma Browser logs web traffic and browser activities that are
appropriate for data protection and organizational security.

The Prisma Browser does not record keystrokes, user passwords, or user
inputs on forms.

The Prisma Browser does allow users to save login credentials for
websites, similar to Google Chrome. This data is saved locally and cannot be
accessed outside of your computer.

Prisma Browser should be used for any web browsing defined by the company.
Depending on company policy, you may be allowed to use another browser for other
purposes.

See [Palo Alto Network’s Privacy Policy](https://www.paloaltonetworks.com/resources/datasheets/prisma-access-browser-privacy-datasheet).

##### Prisma Browser Troubleshooting

Some Prisma Browser messages can seem like issues, but are for safety
or compliance purposes. Some messages can be issues.

- A Restricted website message means that this website is identified as being
  unsafe, vulnerable, fraudulent, or malicious.
- The ”Your connection is not private” message often occurs due to a
  website misconfiguration or certificate issue. If you believe a website was
  blocked in error, please contact IT. Until IT approves the site, do not
  proceed.
- If you receive an error when you attempt to sign into a website with a username
  that is set to your company email address, please contact IT for assistance. Be
  sure to include the URL of the website and your computer’s hostname/IP address
  in the Description.
- See [use the control pane](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access-browser/user-guide/prisma-access-browser-setup-and-use.html) for specific info
  about troubleshooting the control pane.

---

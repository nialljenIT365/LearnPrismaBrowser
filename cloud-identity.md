# Cloud Identity Engine - Documentation

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity on 2026-06-27. 82 pages. Absolute URLs.

## Table of Contents

    - [Get Started with Cloud Identity Engine](#get-started-with-cloud-identity-engine)
      - [Cloud Identity Engine Overview](#cloud-identity-engine-overview)
      - [Plan Your Cloud Identity Engine Deployment](#plan-your-cloud-identity-engine-deployment)
        - [Configure Your Network to Allow Cloud Identity Agent Traffic](#configure-your-network-to-allow-cloud-identity-agent-traffic)
        - [Configure Domains for the Cloud Identity Engine](#configure-domains-for-the-cloud-identity-engine)
      - [Activate the Cloud Identity Engine](#activate-the-cloud-identity-engine)
      - [Manage Cloud Identity Engine App Roles](#manage-cloud-identity-engine-app-roles)
      - [Configure the Cloud Identity Engine Visibility Scope](#configure-the-cloud-identity-engine-visibility-scope)
      - [Cloud Identity Engine Overview](#cloud-identity-engine-overview-1)
    - [Configure Directories for User Identification](#configure-directories-for-user-identification)
      - [Configure an On-Premises Directory](#configure-an-on-premises-directory)
        - [Install the Cloud Identity Agent](#install-the-cloud-identity-agent)
        - [Configure the Cloud Identity Agent](#configure-the-cloud-identity-agent)
        - [Authenticate the Agent and the Cloud Identity Engine](#authenticate-the-agent-and-the-cloud-identity-engine)
        - [Configure an On-Premises Directory](#configure-an-on-premises-directory-1)
      - [Configure a Cloud-Based Directory](#configure-a-cloud-based-directory)
        - [Set Up an Entra ID Directory](#set-up-an-entra-id-directory)
        - [Set Up an Entra ID Directory](#set-up-an-entra-id-directory-1)
        - [Set Up an Entra ID Directory](#set-up-an-entra-id-directory-2)
        - [Set Up an Entra ID Directory](#set-up-an-entra-id-directory-3)
        - [Configure a Cloud-Based Directory](#configure-a-cloud-based-directory-1)
        - [Manage Your Azure Directory](#manage-your-azure-directory)
        - [Configure Okta Directory](#configure-okta-directory)
        - [Manage Your Okta Directory](#manage-your-okta-directory)
        - [Manage Your Okta Directory](#manage-your-okta-directory-1)
        - [Configure Okta Directory](#configure-okta-directory-1)
        - [Configure Google Directory](#configure-google-directory)
        - [Manage Your Google Directory](#manage-your-google-directory)
        - [Manage Your Google Directory](#manage-your-google-directory-1)
        - [Configure SCIM Connector for the Cloud Identity Engine](#configure-scim-connector-for-the-cloud-identity-engine)
      - [Configure a CIE Directory](#configure-a-cie-directory)
    - [Manage the Cloud Identity Engine App](#manage-the-cloud-identity-engine-app)
      - [Cloud Identity Engine Tenants](#cloud-identity-engine-tenants)
        - [Create Cloud Identity Engine Tenants](#create-cloud-identity-engine-tenants)
        - [View Cloud Identity Engine Tenants](#view-cloud-identity-engine-tenants)
        - [Synchronize Cloud Identity Engine Tenants](#synchronize-cloud-identity-engine-tenants)
        - [Rename Cloud Identity Engine Tenants](#rename-cloud-identity-engine-tenants)
        - [Delete Cloud Identity Engine Tenants](#delete-cloud-identity-engine-tenants)
        - [Delete Domains or Directories from Cloud Identity Engine Tenants](#delete-domains-or-directories-from-cloud-identity-engine-tenants)
      - [Cloud Identity Engine Attributes](#cloud-identity-engine-attributes)
      - [Collect Custom Attributes with the Cloud Identity Engine](#collect-custom-attributes-with-the-cloud-identity-engine)
      - [View Directory Data](#view-directory-data)
      - [Cloud Identity Engine User Context](#cloud-identity-engine-user-context)
      - [Create a Cloud Dynamic User Group](#create-a-cloud-dynamic-user-group)
      - [Configure Third-Party Device-ID](#configure-third-party-device-id)
      - [Configure an IP Tag Cloud Connection](#configure-an-ip-tag-cloud-connection)
      - [View Mappings and Tags](#view-mappings-and-tags)
      - [Configure Dynamic Privilege Access in the Cloud Identity Engine](#configure-dynamic-privilege-access-in-the-cloud-identity-engine)
      - [Configure the Secrets Vault](#configure-the-secrets-vault)
    - [Manage the Cloud Identity Agent](#manage-the-cloud-identity-agent)
      - [Configure Cloud Identity Agent Logs](#configure-cloud-identity-agent-logs)
        - [Search Cloud Identity Agent Logs](#search-cloud-identity-agent-logs)
        - [Clear Cloud Identity Agent Logs](#clear-cloud-identity-agent-logs)
      - [Update the Cloud Identity Agent](#update-the-cloud-identity-agent)
      - [Start or Stop the Connection to the Cloud Identity Engine](#start-or-stop-the-connection-to-the-cloud-identity-engine)
      - [Remove the Cloud Identity Agent](#remove-the-cloud-identity-agent)
      - [Manage Cloud Identity Engine Certificates](#manage-cloud-identity-engine-certificates)
        - [Remove Cloud Identity Agent Certificates](#remove-cloud-identity-agent-certificates)
        - [Delete Obsolete Cloud Identity Agent Certificates](#delete-obsolete-cloud-identity-agent-certificates)
    - [Associate the Cloud Identity Engine with Palo Alto Networks Apps](#associate-the-cloud-identity-engine-with-palo-alto-networks-apps)
      - [Associate the Cloud Identity Engine with Palo Alto Networks Apps](#associate-the-cloud-identity-engine-with-palo-alto-networks-apps-1)
      - [Associate the Cloud Identity Engine with Palo Alto Networks Apps](#associate-the-cloud-identity-engine-with-palo-alto-networks-apps-2)
    - [Authenticate Users with the Cloud Identity Engine](#authenticate-users-with-the-cloud-identity-engine)
      - [Set Up Password Authentication](#set-up-password-authentication)
      - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-1)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-2)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-3)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-4)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-5)
        - [Set Up a SAML 2.0 Authentication Type](#set-up-a-saml-20-authentication-type-6)
      - [Set Up a Client Certificate](#set-up-a-client-certificate)
      - [Configure an OIDC Authentication Type](#configure-an-oidc-authentication-type)
      - [Set Up an Authentication Profile](#set-up-an-authentication-profile)
      - [Set Up an Authentication Profile](#set-up-an-authentication-profile-1)
      - [Configure the Cloud Identity Engine as a Mapping Source](#configure-the-cloud-identity-engine-as-a-mapping-source)
    - [Troubleshoot the Cloud Identity Engine](#troubleshoot-the-cloud-identity-engine)
      - [Cloud Identity Engine Troubleshooting Checklist](#cloud-identity-engine-troubleshooting-checklist)
      - [Troubleshoot Cloud Identity Engine Issues](#troubleshoot-cloud-identity-engine-issues)
      - [Cloud Identity Engine Getting Started](#cloud-identity-engine-getting-started)
      - [Monitor Cloud Identity Engine Status](#monitor-cloud-identity-engine-status)
    - [Cloud Identity Agent Help](#cloud-identity-agent-help)

---

<a id="get-started-with-cloud-identity-engine"></a>

#### Get Started with Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine>*

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

<a id="cloud-identity-engine-overview"></a>

##### Cloud Identity Engine Overview

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/learn-about-the-cloud-identity-engine>*

Learn about how the Cloud Identity Engine helps organize user identification and
authentication to keep your network safe and secure.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

In the past, securing a company’s data was relatively simple because everyone worked in
the same building, connected to the same network, and used the same system to log in.
Today, however, employees work from home, coffee shops, and branch offices, using a
variety of devices and cloud-based applications. This shift has made it difficult for
security teams to keep track of who is accessing what. Typically, user information is
scattered across different systems—some kept on servers in the office (like Active
Directory) and others in the cloud (like Google or Microsoft Azure).

The Cloud Identity Engine (CIE) solves this problem by acting as a central translation
layer for user identity. Instead of forcing your security devices to connect
individually to every different list of users you have, the Cloud Identity Engine
collects all those user lists and combines them into a single, unified view. Think of it
as a master contact list that is always up to date. It allows your security system to
verify exactly who a person is and what they are allowed to do, regardless of where they
are located or which system holds their account information.

By centralizing this information, the Cloud Identity Engine ensures that your security
rules are applied consistently everywhere. If an employee joins the company, moves to a
new department, or leaves, the Cloud Identity Engine detects this change immediately and
updates your security devices automatically. This capability helps organizations move
toward a "Zero Trust" security model—a strategy where no one is trusted by default and
everyone must be verified—without the headache of managing complex connections between
dozens of different systems.

For a deeper understanding of the system's architecture and its core security functions,
explore the [Cloud Identity Engine Topology](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/cloud-identity-engine-topology.html), [User Identification with Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/user-identification-with-cloud-identity-engine.html), and [User Authentication with Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/user-authentication-with-cloud-identity-engine.html).

If you have not yet activated the Cloud Identity Engine, click
here.

---

<a id="plan-your-cloud-identity-engine-deployment"></a>

##### Plan Your Cloud Identity Engine Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment>*

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

<a id="configure-your-network-to-allow-cloud-identity-agent-traffic"></a>

###### Configure Your Network to Allow Cloud Identity Agent Traffic

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-your-network-to-allow-cloud-identity-engine-traffic>*

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

<a id="configure-domains-for-the-cloud-identity-engine"></a>

###### Configure Domains for the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-multiple-domains-for-the-cloud-identity-engine>*

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

<a id="activate-the-cloud-identity-engine"></a>

##### Activate the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine>*

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

<a id="manage-cloud-identity-engine-app-roles"></a>

##### Manage Cloud Identity Engine App Roles

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/manage-cloud-identity-engine-app-roles>*

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

<a id="configure-the-cloud-identity-engine-visibility-scope"></a>

##### Configure the Cloud Identity Engine Visibility Scope

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/configure-the-cloud-identity-engine-visibility-scope>*

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

<a id="cloud-identity-engine-overview-1"></a>

##### Cloud Identity Engine Overview

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/set-up-the-cloud-identity-engine>*

Learn about how the Cloud Identity Engine helps organize user identification and
authentication to keep your network safe and secure.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

In the past, securing a company’s data was relatively simple because everyone worked in
the same building, connected to the same network, and used the same system to log in.
Today, however, employees work from home, coffee shops, and branch offices, using a
variety of devices and cloud-based applications. This shift has made it difficult for
security teams to keep track of who is accessing what. Typically, user information is
scattered across different systems—some kept on servers in the office (like Active
Directory) and others in the cloud (like Google or Microsoft Azure).

The Cloud Identity Engine (CIE) solves this problem by acting as a central translation
layer for user identity. Instead of forcing your security devices to connect
individually to every different list of users you have, the Cloud Identity Engine
collects all those user lists and combines them into a single, unified view. Think of it
as a master contact list that is always up to date. It allows your security system to
verify exactly who a person is and what they are allowed to do, regardless of where they
are located or which system holds their account information.

By centralizing this information, the Cloud Identity Engine ensures that your security
rules are applied consistently everywhere. If an employee joins the company, moves to a
new department, or leaves, the Cloud Identity Engine detects this change immediately and
updates your security devices automatically. This capability helps organizations move
toward a "Zero Trust" security model—a strategy where no one is trusted by default and
everyone must be verified—without the headache of managing complex connections between
dozens of different systems.

For a deeper understanding of the system's architecture and its core security functions,
explore the [Cloud Identity Engine Topology](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/cloud-identity-engine-topology.html), [User Identification with Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/user-identification-with-cloud-identity-engine.html), and [User Authentication with Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-overview/user-authentication-with-cloud-identity-engine.html).

If you have not yet activated the Cloud Identity Engine, click
here.

---

<a id="configure-directories-for-user-identification"></a>

#### Configure Directories for User Identification

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type>*

Learn about the types of directories that the Cloud Identity
Engine supports and how to configure them.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configuring directories is the foundational step for establishing accurate user identification
across your network. By connecting the Cloud Identity Engine to your organization's
directory services—whether [on-premises Active Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory.html), [cloud-based providers](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory.html) like Microsoft Entra ID (Azure AD) and Okta, or
a[local CIE directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html)—you enable the engine to synchronize user, group, and
device attributes.

This synchronization creates a unified view of identity, allowing you to enforce security
policies based on actual users and their roles rather than static IP addresses. For
on-premises environments, this involves installing the Cloud Identity Agent to securely
collect attributes, while cloud directories connect directly via APIs or the SCIM
protocol. Once configured, the engine continuously updates this data, ensuring that
access controls automatically adapt as users move departments or change roles within
your organization.

---

<a id="configure-an-on-premises-directory"></a>

##### Configure an On-Premises Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory>*

Learn more about how to configure the Cloud Identity
agent to communicate with your on-premises Active Directory or OpenLDAP-based
directory.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configuring an on-premises directory allows the Cloud Identity Engine to synchronize
user, group, and computer attributes from your internal Active Directory or OpenLDAP
infrastructure. This integration relies on the **Cloud Identity Agent**, a
service installed on a Windows server within your network that functions as a secure
bridge between your local directory and the cloud service.

To establish this connection, you must [install the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/install-the-cloud-identity-agent.html) on a supported server that
meets specific network and system requirements. Once installed, you [configure the agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent.html) to communicate with your directory
using standard protocols (LDAP or LDAPS) and define which domains or specific
attributes the agent should collect.

Security is maintained through mutual authentication between the agent and the
service. You must [authenticate the agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html) by
generating a unique certificate within the Cloud Identity Engine application and
installing it on the agent host. This process establishes a trusted, encrypted
Transport Layer Security (TLS) channel, ensuring that your directory data is
securely synchronized with the cloud.

Beyond basic connectivity, the setup allows for granular control over data
synchronization. You can configure specific filters using attributes—such as group
names or unique identifiers—to ensure the engine only collects relevant directory
objects, optimizing the data flow. Once deployed, the agent provides a local user
interface for monitoring the connection status, viewing the timestamps of the last
successful directory fetch, and reviewing logs to troubleshoot connectivity or
synchronization issues.

---

<a id="install-the-cloud-identity-agent"></a>

###### Install the Cloud Identity Agent

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/install-the-cloud-identity-agent>*

Learn how to download the Cloud Identity agent and install
it on a supported Active Directory or OpenLDAP-based directory server.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Before installing the Cloud Identity agent,
verify that the time on the agent host is correct and synced to
a valid NTP server. If the time on the server host is incorrect,
the Cloud Identity Engine may not be able to sync your directory
attributes successfully.

After you [activate](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) your Cloud Identity Engine
tenant, download the Cloud Identity agent from the Cloud Identity Engine app on the
hub and install it on a supported directory server. Palo Alto Networks strongly
recommends using TLS 1.3. If TLS 1.2 is not already [enabled](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls#support-for-tls-12) on the Windows server that will
host the agent, install the [update](https://support.microsoft.com/en-us/help/3140245/update-to-enable-tls-1-1-and-tls-1-2-as-a-default-secure-protocols-in) to enable TLS 1.2 before you
install the agent.

Because the [User-ID agent](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-using-the-windows-user-id-agent.html) and the
Cloud Identity agent require the same port, you must use a dedicated
host for each agent type. Do not install both agent types on the
same host.

1. Log in to the [hub](https://apps.paloaltonetworks.com) and select the Cloud
   Identity Engine app.
2. Select Directories then click Add
   New Directory.

   ![]()
3. Set Up an On-Premises Directory.

   ![]()
4. Click Download Agent.

   ![]()
5. When the download is complete, open the DaInstall.msi
   installation file for the agent on the Windows server where you
   plan to install the agent.

   For a list of supported servers, see the [Cloud Identity Engine system
   requirements](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-release-notes/cloud-identity-engine-release-notes-welcome/cloud-identity-engine-release-notes-system-requirements.html).

   If you are also using the Terminal Server
   (TS) agent, we recommend that you do not install the Cloud Identity
   agent on the same host as the TS agent. If you must install both
   agents on the same host, you must [change](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/user-id/map-ip-addresses-to-users/configure-user-mapping-for-terminal-server-users/configure-the-palo-alto-networks-terminal-services-agent-for-user-mapping.html) the default listening
   port on the TS agent.
6. Follow the prompts in the installation wizard to install
   the agent.
7. Navigate to the location of the Cloud Identity agent.

   The default location is C:\Program Files (x86)\Palo Alto
   Networks\Cloud Identity Agent\.
8. Double-click the CloudIdAgentController.exe file
   to launch the Cloud Identity agent.

   Starting the agent also starts the Cloud Identity Engine,
   which runs in the background on the server hosting the Cloud Identity
   agent until you [stop the connection
   to the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service.html#id1818J060VBD).

###### Next Steps

- After you have installed the Cloud Identity
  agent on the host, [Configure the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent.html#id17CFA0ZN0XI) to communicate
  with both your directory and the Cloud Identity Engine.
- After configuring the agent, make sure to [Authenticate the Agent and the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html#id17CKFM00EIA) to enable
  communication between the agent and the Cloud Identity Engine.
- For a comprehensive user identity and authentication solution,
  learn how to [Authenticate Users with the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine.html#id05626c4b-2f90-47b4-b9f4-c72fce41de02).

---

<a id="configure-the-cloud-identity-agent"></a>

###### Configure the Cloud Identity Agent

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent>*

After you download the agent and install it on a Windows server, configure the agent to
connect to your supported on-premises directory and to the Cloud Identity
Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Avoid configuring the agent for the first time during the daily certificate revocation list
(CRL) reload time (9:00-10:00 PM/21:00-22:00 CDT for US or CEST for EU). If you
configure the agent and the initial attribute sync occurs at this time but isn’t
successful, wait a few minutes, then [Synchronize All Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances.html#idfaa1ba0a-aa4f-4803-be87-4f23783b8c9b_id5306eb05-1718-4e8f-9062-53d4ac69bdae) to ensure the attributes are
synchronized with your tenant.

After you download the agent from the Cloud Identity Engine app and [Install the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/install-the-cloud-identity-agent.html#id17CFA0U0B4X) on a supported Windows server, configure the agent
to establish a connection with your Active Directory or OpenLDAP-based directory and
the Cloud Identity Engine so that it can collect all of the attributes from the
Active Directory during the initial setup.

OpenLDAP requires specific attributes. For more information,
refer to the [Cloud Identity Engine Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes.html) attributes.

In the Cloud Identity Engine app, you can optionally [Synchronize Cloud Identity Engine Tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances.html#idfaa1ba0a-aa4f-4803-be87-4f23783b8c9b) instantly to ensure attribute and
other directory changes are available in the Cloud Identity Engine.

The minimum required permissions
for the service account are the ability to create LDAP bind requests
(LDAP protocol version, the DN for the account, and the account
credentials) and the IP address or domain for the directory.

1. If you haven’t already done so, configure your network to allow Cloud Identity
   Engine traffic.
2. Install the certificate authority (CA) certificate used to sign the certificate
   used by the directory in the Local Computer Trusted root CA certificate store of
   the agent host.

   You must complete this step if the server that hosts the agent doesn’t
   already have the CA certificate of the domain controller or the CA
   certificate from the issue of the domain controller’s certificate.
3. On the agent host, launch the Cloud Identity agent (StartPalo Alto NetworksCloud Identity Agent).

   Don’t manually edit configuration files for the agent.
   Manually editing the agent configuration files might cause unexpected
   behavior.
4. Select Cloud Identity Configuration and
   enter the regional agent configuration endpoint for the Cloud
   Identity Engine that matches the region that the corresponding
   Cloud Identity Engine tenant uses.

   ![]()

   |

   Region | Agent Configuration |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   United States (US) | agent-directory-sync.us.paloaltonetworks.com |

   |

   European Union (EU) | agent-directory-sync.eu.paloaltonetworks.com |

   |

   United Kingdom (UK) | agent-directory-sync.uk.paloaltonetworks.com |

   |

   Singapore (SG) | agent-directory-sync.sg.paloaltonetworks.com |

   |

   Canada (CA) | agent-directory-sync.ca.apps.paloaltonetworks.com |

   |

   Japan (JP) | agent-directory-sync.jp.apps.paloaltonetworks.com |

   |

   Australia (AU) | agent-directory-sync.au.apps.paloaltonetworks.com |

   |

   Germany (DE) | agent-directory-sync.de.apps.paloaltonetworks.com |

   |

   United States - Government | agent-directory-sync.gov.apps.paloaltonetworks.com |

   |

   India (IN) | agent-directory-sync.in.apps.paloaltonetworks.com |

   |

   Switzerland (CH) | agent-directory-sync.ch.apps.paloaltonetworks.com |

   |

   Spain (ES) | agent-directory-sync.es.apps.paloaltonetworks.com |

   |

   Italy (IT) | agent-directory-sync.it.apps.paloaltonetworks.com |

   |

   France (FR) | agent-directory-sync.fr.apps.paloaltonetworks.com |

   |

   China (CN) | agent-directory-sync.cn.apps.prismaaccess.cn This region is only accessible in the Cloud Identity Engine within the specified region. |

   |

   Poland (PL) | agent-directory-sync.pl.apps.paloaltonetworks.com |

   |

   Qatar (QA) | agent-directory-sync.qa.apps.paloaltonetworks.com |

   |

   Taiwan (TW) | agent-directory-sync.tw.apps.paloaltonetworks.com |

   |

   Israel (IL) | agent-directory-sync.il.apps.paloaltonetworks.com |

   |

   Indonesia (ID) | agent-directory-sync.id.apps.paloaltonetworks.com |

   |

   South Korea (KR) | agent-directory-sync.kr.apps.paloaltonetworks.com |

   |

   Saudi Arabia (SA) | agent-directory-sync.sa.apps.paloaltonetworks.com |

   |

   South Africa (ZA) | agent-directory-sync.za.apps.paloaltonetworks.com |
5. (Optional) If your network configuration uses a proxy
   server, enter the Proxy IP Server and Port (optional) to
   allow the Cloud Identity agent to use a secure mTLS connection to
   tunnel the agent traffic through the proxy server.

   Enter the proxy server’s IP address in <IP\_Address>:<Port> format,
   where <IP\_Address> represents the IP address
   of the proxy server and <Port> represents
   the port number.
6. Configure the LDAP Configuration to
   allow the agent to communicate with your on-premises directory.

   To learn how to collect attributes from multiple domains, see Configure Domains for the Cloud
   Identity Engine. 

   ![]()

   1. Enter the Bind DN for
      the service account you want to bind to your directory (for example, CN=admin,OU=IT,DC=domain1,DC=example,DC=com).

      If you don’t know the DN of the service account, enter
      the following command in the command prompt on the Active Directory
      server: dsquery user -name username (where username is
      the service account login name). Be sure to delete the quotation
      marks if you copy the DN from the command output.
   2. Enter the Bind Password to
      authenticate the session.

      The Bind Password is saved in encrypted format in the Windows credential store, not the
      configuration file. If you delete the LDAP configuration for the server
      and commit the changes, you must re-enter the password.
   3. Select a Protocol:

      - LDAP—Connect to the directory
        using the default unencrypted LDAP protocol on port 389.
      - LDAPS—(Default) Connect to the directory
        server using LDAP over SSL (LDAPS) on port 636. This option requires
        a CA certificate in the Local Computer certificate store on the agent
        host or in the Trusted Root CA store for your directory.
      - LDAP with STARTTLS—Connect to the
        directory server using LDAPv3 Transport Layer Security (TLS) on
        port 389. This option requires a CA certificate in the Local Computer certificate
        store on the agent host or in the Trusted Root CA store for your
        directory.
7. Verify that the Bind Timeout value
   will allow enough time for the agent to connect to your on-premises
   directory.

   The default is 30 seconds and the range is from 1-60 seconds.
   When the timeout limit is reached, the agent attempts to connect
   to the next domain controller in the sequence for that domain.
8. Verify that the Search Timeout value
   will allow enough time for the LDAP query to complete.

   The default is 15 seconds and the range is 1-120 seconds. If the timeout occurs, the search
   stops and the timeout error is included in the debug logs. If you [Configure Cloud Identity Agent Logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs.html#id1818I0S0N5S) to Information, any partial results retrieved
   by the Cloud Identity Engine are deleted. If the log level is set to Debug or
   higher, the results might not be deleted, but they aren’t used by the
   agent.
9. Add your on-premises directory.

   To ensure that the Cloud Identity Engine can calculate group membership correctly, use a value
   that doesn’t end in 65 if you must use a custom value
   for the MaxValRange attribute in your LDAP query
   policy rule.

   ![]()

   1. (Optional) Enter the Name (optional) for
      your directory.
   2. Enter the fully qualified Domain name
      for your directory.

      You can configure up to 20 domains for each agent.
   3. Enter the IP address or fully qualified domain name
      (FQDN) as the Network Address for your directory.

      If you enter an FQDN, it must be the complete original
      FQDN for that IP address (for example, if the FQDN is example.hr.com,
      you must enter example.hr.com, not just example.com).
   4. (Optional) Enter the Port (optional) number
      for your directory.

      Don’t configure the agent to use the Global Catalog port (3268 for LDAP or 3269 for
      LDAPS).

      If you don’t enter a port number, the agent uses the following default ports:

      - 636
        for LDAPS
      - 389 for LDAP or LDAP with STARTTLS
   5. (Required for OpenLDAP) Enter the Base
      DN (base Distinguished Name) for your directory.

      ![]()

      OpenLDAP requires the Base DN; without the Base DN, directory
      searches can’t complete successfully.

      When you enter the
      Base DN, use the domainComponent format (for example,
      DC=example, DC=com).
   6. Select your directory Type.

      - OpenLDAP—Configure the agent
        to use an OpenLDAP-based directory server.

        The Cloud Identity
        Engine supports OpenLDAP groups with the following ObjectClass: groupsOfUniqueNames.
        When configuring another application (for example, GlobalProtect)
        with the Cloud Identity Engine for an OpenLDAP-based directory,
        specify the Common-Name as the Primary Name.
        By default, the Cloud Identity Engine uses the sAMAccountName.
      - Active Directory—Configure the agent
        to use an Active Directory directory server.
   7. (Optional but recommended) To confirm the agent can
      successfully connect to your Active Directory, you can Test
      Connectivity to Directory. The agent verifies that it
      can successfully connect to the domain and validates the NetBIOS
      name based on the domain.
   8. Click OK.

      When you add an on-premises directory, the Cloud Identity
      agent automatically attempts to complete a full synchronization
      of all domains, including existing domains, so confirm the agents
      are active and all configured domains are active before adding a
      new domain to the agent. If an inactive domain is no longer necessary, [delete](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/delete-domains-or-directories-from-cloud-identity-engine-instances.html#id32517175-335d-4dd7-a5ea-b4bfb5948d0a) the
      domain from your configuration.
10. Commit the changes to restart
    the agent and apply the configuration.

    The agent will connect to your directory to collect the
    attributes and to the Cloud Identity Engine to share the attributes
    with the Palo Alto Networks cloud-based apps.
11. To confirm the agent is able to connect to your on-premises
    directory and the Cloud Identity Engine, log in to the Cloud Identity
    Engine app, select the tenant, then select Directories to
    verify the following information:

    - The domains currently monitored by the Cloud Identity
      Engine and each domain’s NetBIOS name.
    - The sync status of the most recent attribute collection update
      from the directory (for example, In Progress or Successful).
    - When the last successful attribute collection update from the
      directory occurred.
    - The number of users, computers, groups, containers, and organizational units (OUs) in the
      domains monitored by the Cloud Identity Engine.
12. (Optional but recommended) Configure an additional agent
    for high availability (HA).

    You can configure HA for the Cloud Identity Engine by configuring two or more agents to
    collect attributes from the same domain in the same tenant. The configuration
    for each agent must be identical. We recommend this configuration to ensure that
    if an agent is temporarily unavailable, any in-progress syncs complete
    successfully and service isn’t interrupted. If the Cloud Identity Engine fails
    to connect to an agent, it searches for the next available agent. The Cloud
    Identity Engine communicates with only one agent at a time and the agents don’t
    communicate with each other.
13. (Optional but recommended) To enhance security, you can optionally update the
    bind password at regular intervals (also known as password rotation). To
    automate this process, you can create a script to enter the command instead of
    manually updating the agent configuration.
    1. To update the bind password, update the password on the LDAP server
       then enter the following command on the agent host:
       CloudIdAgentCLI.exe
       ldap\_bind\_password:<password>
       (where <password> represents the new password).

       If the password contains any of the following non-alphanumeric
       characters, use an escape character to interpret it as a literal
       character:`\*\~;(%?.:@/$%^\*()!''"

       The escape character depends on the shell or programming language you
       use to enter the command.

       For example, if you are using Powershell version 7.4.2:

       - If the password contains the specified non-alphanumeric
         characters, use quotation marks ( " ) before and after the
         password.
       - If the password contains quotation marks or escape characters,
         use the escape character ( ` ) before the character. You must
         also use quotation marks before and after the password.

       For example, if the new password is
       `\*\~;(%?.:@/$%^\*()!''" and you are using
       Powershell version 7.4.2, enter the following command:
       .\CloudIdAgentCLI.exe
       ldap\_bind\_password:"``\*\~;(%?.:@/$%^\*()!''`""

       ![]()

       For more information on using non-alphanumeric characters in
       passwords, refer to the [Microsoft
       documentation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements).
    2. To troubleshoot any issues, check the log file
       (CloudIdAgentCLIDebug.log).

       The log file location is the same as the installation location for the
       agent (C:\Program Files (x86)\Palo Alto Networks\Cloud
       Identity Agent.

###### Next Steps

- After you’ve configured the agent, you can optionally [Configure Cloud Identity Agent Logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs.html#id1818I0S0N5S) to track the agent events you want to
  monitor.
- For a comprehensive user identity and authentication solution,
  learn how to [Authenticate Users with the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine.html#id05626c4b-2f90-47b4-b9f4-c72fce41de02).

---

<a id="authenticate-the-agent-and-the-cloud-identity-engine"></a>

###### Authenticate the Agent and the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine>*

Generate certificates to authenticate communication between
the Cloud Identity agent and the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine and the Cloud Identity
agent use a certificate for mutual authentication (i.e., the agent
authenticates the service and the service authenticates the agent)
over Transport Layer Security (TLS). If the certificate is valid,
the agent connects to the Cloud Identity Engine. If the certificate
is not valid, the Cloud Identity Engine rejects the connection.

To
authenticate the Cloud Identity Engine and the Cloud Identity agent,
generate a Cloud Identity Engine certificate using the Cloud Identity
Engine app and import it to the Local Computer certificate store
on the Windows server that hosts the agent. Each certificate expires
three months from the issuance date. The Cloud Identity agent version
1.5.0 and later versions automatically renews the certificate before
it expires.

Each agent must use a unique certificate to authenticate
with the service. Only use the certificate for the agent in the
selected tenant. Generate certificates on an as-needed basis and
do not use the certificate for other services or share them between
agents. You can generate up to 5 unused certificates and up to 100
total certificates per tenant. You can only use the certificate
for the specified tenant and you can only associate the certificate
with one agent.

1. Enter a unique Certificate Name.

   The name must be between 5 and 128 alphanumeric characters.
2. Enter a secure password in the Create Password and Re-enter
   Password fields.

   The password must be between 12 to 25 characters. You will
   need to enter this password when you install the certificate on
   the agent host.
3. Click Download Certificate.

   ![]()
4. Store the certificate in the Local Computer Personal
   certificate store on the agent host.

   For more information on how to store certificates, see the following [link](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores).

   After the agent authenticates
   with the Cloud Identity Engine, it provides the directory attributes to
   the service. The service then shares the attributes with the apps
   that you with the Cloud Identity Engine for visibility and policy
   enforcement. For more information, refer to [Manage Cloud Identity Engine Certificates](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates.html#id2dfe3086-e8f1-45e8-80c7-221d428a7766).

###### Next Steps

- [Use the Cloud Identity
  Engine app](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine.html#id183LG00I0JB) to create, view, delete, rename, or synchronize
  tenants and to view or customize the attributes that the Cloud Identity
  Engine collects.
- Learn how to [manage the Cloud
  Identity agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent.html#id183LG0X08T5) by logging agent events, managing the certificates
  that the agent uses, starting or stopping the agent’s connection
  to the Cloud Identity Engine, and updating or removing the agent.

---

<a id="configure-an-on-premises-directory-1"></a>

###### Configure an On-Premises Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory/configure-on-premises-filter>*

Learn more about how to configure the Cloud Identity
agent to communicate with your on-premises Active Directory or OpenLDAP-based
directory.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configuring an on-premises directory allows the Cloud Identity Engine to synchronize
user, group, and computer attributes from your internal Active Directory or OpenLDAP
infrastructure. This integration relies on the **Cloud Identity Agent**, a
service installed on a Windows server within your network that functions as a secure
bridge between your local directory and the cloud service.

To establish this connection, you must [install the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/install-the-cloud-identity-agent.html) on a supported server that
meets specific network and system requirements. Once installed, you [configure the agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent.html) to communicate with your directory
using standard protocols (LDAP or LDAPS) and define which domains or specific
attributes the agent should collect.

Security is maintained through mutual authentication between the agent and the
service. You must [authenticate the agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html) by
generating a unique certificate within the Cloud Identity Engine application and
installing it on the agent host. This process establishes a trusted, encrypted
Transport Layer Security (TLS) channel, ensuring that your directory data is
securely synchronized with the cloud.

Beyond basic connectivity, the setup allows for granular control over data
synchronization. You can configure specific filters using attributes—such as group
names or unique identifiers—to ensure the engine only collects relevant directory
objects, optimizing the data flow. Once deployed, the agent provides a local user
interface for monitoring the connection status, viewing the timestamps of the last
successful directory fetch, and reviewing logs to troubleshoot connectivity or
synchronization issues.

---

<a id="configure-a-cloud-based-directory"></a>

##### Configure a Cloud-Based Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

After you activate your Cloud Identity Engine tenant,
configure a cloud-based directory, such as Azure Active Directory
(Azure AD), Okta Directory, or Google Directory, to communicate
with the Cloud Identity Engine.

Configuring a cloud-based directory in the Cloud Identity Engine enables
your network security infrastructure to identify users and enforce
policies based on identity rather than IP addresses. By granting the
Cloud Identity Engine read-only access to your organization's
directory data, you establish a centralized source of truth that
synchronizes user, group, and device attributes across your entire
deployment.

For [Microsoft Entra ID (Azure AD)](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory.html), you can
establish a connection using the recommended CIE Enterprise App or a
client credential flow, with options to collect advanced data like
user risk signals for dynamic policy adjustments. [Okta
integrations](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html) offer similar flexibility, allowing you
to connect via an OpenID Connect (OIDC) app using either an
authorization code or client credential flow to sync user and group
attributes. For organizations using [Google
Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-google-directory-in-the-cloud-identity-engine.html), the engine connects directly via the
Google Admin API to retrieve organizational units and user
details.

If your organization requires a more customized approach or uses a
different provider, the [SCIM
Connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) allows you to ingest identity data from any
SCIM-compliant source—such as PingFederate or customized Entra ID
setups—giving you granular control over which attributes are shared.
Additionally, for scenarios where an external identity provider is
not available or necessary, you can configure a [CIE Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html). This
cloud-native, local directory lets you create and manage users
directly within the engine, offering a quick solution for testing or
specific user segments without requiring external
infrastructure.

To use the System for Cross-domain Identity Management (SCIM)
provisioning to customize which attributes your Azure AD shares
with the Cloud Identity Engine, you can configure the SCIM Connector.

If the connection between your directory and the Cloud Identity
Engine is not active, you can reconnect your directory. If you no
longer want to associate a directory with the Cloud Identity Engine,
learn how to revoke the permissions for that directory.

---

<a id="set-up-an-entra-id-directory"></a>

###### Set Up an Entra ID Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure>*

Learn how to set up an Entra ID directory in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configure Microsoft Entra ID (formerly Azure AD) in the Cloud Identity Engine to
allow the Cloud Identity Engine to collect directory data for policy rule
enforcement and user visibility.

To configure directory sync with an Entra ID tenant using
the Cloud Identity Engine Enterprise app, you must be an Entra ID Global
Administrator or have a Global Administrator available to complete the app
registration using the onboarding URL.

As an alternative, you can [configure the SCIM connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) to select and
synchronize the Entra ID attribute data you want to collect with the Cloud Identity
Engine.

To further reduce sync time and minimize the amount of data collected by the Cloud
Identity Engine, you can configure the Cloud Identity Engine to sync only specific
groups from your directory by filtering the groups. Because SCIM is most suitable
for small and frequent data requests, Microsoft restricts directory update intervals
to once every 40 minutes. If you filter the groups instead, directory updates can
occur as often as every 5 minutes. Choose the best option for your deployment based
on your organizational and regulatory requirements.

The Cloud Identity Engine retrieves updates from your Entra ID tenant using the
following schedule:

- Users, Groups, and Devices—When the Cloud Identity Engine syncs
  changes.
- Apps—Every x hours (where x is either a
  maximum of 3 hours or the duration necessary to complete the previous apps
  sync).
- Role Assignments—Every x hours (where x is
  either a maximum of 24 hours or the duration necessary to complete the previous
  role assignment sync).

When you configure Entra ID for the Cloud
Identity Engine, log in, and grant the necessary permissions, Microsoft
automatically onboards the Cloud Identity Engine Enterprise App into Entra ID.

- [Cloud Identity Engine Enterprise
  App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/configure-azure-using-the-cie-enterprise-app.html#configure-azure-using-the-cie-enterprise-app)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad.html#id945b497c-f690-4c49-bc26-ed15f4118cbc)

<a id="configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb"></a>

###### Configure Entra ID Using the CIE Enterprise App

Learn how to configure Microsoft Entra ID in the Cloud Identity Engine using the CIE
Enterprise app.

1. Copy the Directory ID for your Entra ID tenant.
   1. Log in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or the Azure
      administrator portal using the credentials of the account you want to
      use to connect to the Cloud Identity Engine (for example, a service
      account) and select Overview.
   2. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
2. Set up your Entra ID tenant in the Cloud Identity Engine.
   1. In the Cloud Identity Engine app, select
      Directories, then click Add New
      Directory.
   2. Set Up an Entra ID Cloud
      Directory.

      ![]()
3. (Optional) Select additional information types to collect from Entra
   ID.

   The CIE Enterprise app automatically requests the privileges necessary to
   retrieve directory information, user risk information, and any other
   additional info you choose to collect. If you enable an option that
   requires additional privileges, you must reconnect the directory. For
   configurations that use the [CIE Enterprise app](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc),
   use the CIE Enterprise App onboarding URL in step
   [4.2](#configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc) to grant the
   necessary privileges.

   After onboarding the app into Entra ID, you can [revoke privileges](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions?pivots=portal#review-and-revoke-permissions) if they are
   not necessary for your configuration. Do not revoke privileges for
   options you select. If you revoke a privilege required for an option you
   select or for the Cloud Identity Engine by default, the sync cannot
   complete.

   To restore revoked permissions, edit the directory configuration and
   complete steps [4.1](#configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc) through [4.5](#configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc).

   The following list provides the permissions for each additional
   information type.

   - Collect user risk information from Entra ID Identity
     Protection:
     - IdentityRiskyUser.Read.All
     - IdentityRiskEvent.Read.All

     For more information, refer to [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
   - Collect Roles and Administrators (Administrative
     roles): Directory.Read.All or
     RoleManagement.Read.Directory
   - Collect enterprise applications:
     Application.Read.All
   - Collect device information:
     Device.Read.All

   1. Collect user risk information from Entra ID Identity
      Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

      ![]()
   2. Collect Roles and Administrators (Administrative
      roles) to retrieve
      roleAssignments attribute information for
      users and groups.

      Allowing the Cloud Identity Engine to include this information for
      analysis helps to prevent role-based malicious attacks.

      By default, the Cloud Identity Engine
      enables this option for tenants who are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex
      XDR.

      ![]()
   3. Collect enterprise applications data so that it
      displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If you don't want to collect the
      application data or you don't use application data in your Security
      policy, deselect the check box to decrease the sync time.

      ![]()
   4. Collect device information.

      This data is used by Cortex XDR and Device Security.
4. Configure your Entra ID information in the Cloud Identity Engine.
   1. Enter the directory ID you copied in step [1.2](#configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb) as the
      Directory ID.

      ![]()
   2. Generate the CIE Enterprise App onboarding URL
      to register the CIE Enterprise App in your Entra ID tenant.

      Registering the app in Microsoft Entra ID requires the Global
      Administrator role.

      If you do not have Global Administrator privileges in Entra ID,
      you must generate the URL and share it with an Entra ID
      administrator with Global Administrator privileges (Global
      Administrator role).

      1. Click Generate URL.
      2. Copy the resulting URL.
      3. Depending on your Entra ID role, perform one of the following
         actions:

         - (Global Administrator) Open the URL in a
           new tab or window to register the app
           instantly.
         - (Non-Global Administrator) Share the URL
           with an Entra ID administrator (Global
           Administrator) to complete the registration
           offline, then return to the Cloud Identity
           Engine.

      ![]()
   3. Enter the email address or phone number for the Global Administrator
      Role account you use to connect to the Cloud Identity Engine then click
      Next.

      ![]()
   4. Enter your password and Sign in.

      ![]()
   5. Click Accept to grant the necessary permissions
      for your Entra ID directory.

      When you accept, Entra ID automatically
      enables the following required permissions, as well as the
      additional information type permissions listed in step [3](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc):
      - Device.Read.All—Application, Read all
        devices
      - Group.Read.All—Application, Read all
        groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      ![]()
   6. Click Test Connection to confirm that the Cloud
      Identity Engine can successfully connect to your Entra ID tenant.

      ![]()
   7. (Optional) Enter a custom Directory Name
      (Optional) to use in the Cloud Identity Engine.

      ![]()
5. (Optional) Upload a .CSV file to use as a [filter for groups](#configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc).
   1. Click Upload CSV to upload a comma-separated
      value (CSV) file to use as a filter.

      ![]()
   2. Drag and drop the .CSV file or click Browse
      files to select the .CSV file you want to use as a
      filter.

      ![]()
   3. Select the Upload Type for the filter.

      - Update Filters—Update the existing
        filters with the .CSV data.
      - Replace Existing Filters—Replace the
        existing filters with the .CSV data.

      ![]()
   4. Select the Attribute Name you want to use for
      the filter (Name or Unique
      Identifier).
   5. Click Apply to confirm the changes.

      ![]()
6. (Optional) Filter Entra ID Groups.
   1. Select the group attribute you want to use as a filter.

      - Name—Filter the groups based on the group
        name.
      - Unique Identifier—Filter the groups based
        on the unique identifier for the group.

      ![]()
   2. Select how you want to filter the groups.

      - (for Name attribute only)
        begins with—Filter the groups based on a
        partial match for the text you enter.

        The filter supports spaces in the
        search query.
      - is equal to—Filter the groups based on an
        exact match for the text you enter.

      ![]()
   3. Enter the search query you want to use to filter the groups (either
      alphanumeric characters for a name or numeric characters for a unique
      identifier).

      ![]()
   4. (Optional) Configure an additional filter by clicking
      Add
      ORAdd
      Filter and repeating the previous three steps for each
      filter you want to include.

      If you select additional attributes as match conditions, the Cloud
      Identity Engine initially attempts to find a match for the first
      condition, then continues to match based on the additional conditions
      you specify. 

      ![]()
7. Submit your changes and verify your directory
   information when the Directories page displays.

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins"></a>

###### Configure Azure Using the Client Credential Flow

The Client Credential Flow option for Azure Active Directory (AD) in the Cloud Identity Engine
allows you to use a service account to log in to your Azure AD in the Cloud Identity
Engine. Using a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to be associated with a
specific user.

If this is the first
time you have created a Cloud Identity Engine tenant, the Cloud
Identity Engine app is not available in the Azure app gallery, so
you must create a custom app.

If you already have an existing
Azure AD configuration in the Cloud Identity Engine, you can easily migrate
the existing configuration to use the client credential flow option
by reconnecting your Azure AD to the Cloud Identity Engine, selecting
the Client Credential Flow option, and testing the connection to
verify the configuration.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity Engine
   tenant.
2. Grant the required read-only permissions in the Azure
   Portal.
   1. In the Azure Portal, select HomeAzure Active DirectoryApp Registrations.
   2. Click New registration.

      ![]()
   3. Enter a Name then click Register.

      ![]()
   4. Select API permissions then
      click Add a permission.

      ![]()
   5. Click Microsoft Graph then
      select Application permissions.

      ![]()
   6. Select the following permissions then click Add
      permissions:

      - Device.Read.All—Application, Read all
        devices
      - GroupMember.Read.All—Application, Read
        all groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      The permissions listed above represent the
      minimum required permissions that use least privilege access. If you
      prefer a less granular scope that is simpler to implement, you can
      use these permissions instead:
      - Directory.Read.All
      - Organization.Read.All

      - If you want to use user risk information in attribute-based
        [Cloud Dynamic User
        Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb), you must grant additional permissions.
        For more information, refer to the documentation on how to
        [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
      - If you want to collect information on roles and
        administrators, if you have already granted the 
        Directory.Read.All scope, no further
        permissions are required. If you are using the scopes listed
        above, you must also grant the 
        RoleManagement.Read.Directory scope to
        collect role and administrator information. For more
        information, refer to step [6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins).
      - If you want to collect enterprise application data, you must
        also grant the Application.Read.All
        scope. For more information, refer to step [7](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps).
   7. Click Grant admin consent for DirectoryName (where DirectoryName represents
      the name of your Azure AD).

      ![]()
   8. Click Yes to confirm.

      ![]()
3. Collect the necessary configuration information from
   the Azure Portal.
   1. In the Azure dashboard, select your Azure AD, then select
      App Registrations and select the app you
      created.
   2. Select Certificates & secrets then click
      New client secret.

      ![]()
   3. Enter a Description and Add the secret.

      When you add the secret, make sure to keep track of when the secret
      Expires. When the secret expires, you
      must configure the new secret in the Azure Portal and update the
      configuration in the Cloud Identity Engine app to replace the
      expired secret. Keep this in mind when selecting the expiry value
      for the secret. If you prioritize ease of configuration, select a
      longer expiration for the secret (the maximum value is 2 years). If
      security is of greater concern, select a shorter value for the
      secret’s expiration (the default is 6 months).

      ![]()
   4. Copy the Value of the secret and store it in a
      secure location.

      ![]()
   5. Click Overview then copy the
      Application (client) ID and store it in a
      secure location.

      ![]()
   6. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
4. Add your Azure AD directory in the Cloud Identity Engine.

   (Required for migration) If you are migrating an existing Azure AD
   configuration, select ActionsReconnect on the Directories page for the Azure AD
   you want to migrate. The Cloud Identity Engine automatically populates the
   necessary information so you can continue to step [9](#id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb) (testing the connection).

   1. In the Cloud Identity Engine app, select
      Directories then click Add New
      Directory.
   2. Set Up an Azure
      directory.

      ![]()
5. Select whether you want to Collect user risk information from Azure
   AD Identity Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to the documentation for [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb).

   ![]()
6. Select whether you want to Collect Roles and Administrators
   (Administrative roles) to retrieve
   roleAssignments attribute information for users and
   groups. Allowing the Cloud Identity Engine to include this information for
   analysis helps to prevent role-based malicious attacks.

   By default, the Cloud Identity Engine enables this
   option for tenants that are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex XDR.

   ![]()

   If you do not see the Collect Roles and
   Administrators (Administrative roles) option, [reconnect](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/reconnect-directory) your directory to select
   the option.
7. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If
   you don't want to collect the application data or you don't use application data
   in your security policy, deselect the checkbox to decrease the sync time. If you
   select this option, you must enable additional permissions for the Cloud
   Identity Engine (see step [2.6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c)).

   For beta users of this feature, the Cloud Identity
   Engine continues collecting enterprise application data for any directories
   configured in your tenant during the beta and no further configuration is
   required. If you configure a new directory, you must select whether you want
   to collect enterprise application data from the new directory.

   ![]()
8. Enter your directory information as indicated, using the information you copied
   from the Azure Portal in steps [3.4](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb):

   During migration of an existing Azure AD
   configuration to the client credential flow, the Cloud Identity Engine
   automatically populates the Directory ID.

   |

   Copy from Azure Portal | Enter in Cloud Identity Engine |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Directory (tenant) ID | Directory ID |

   |

   Application (client) ID | Client ID |

   ![]()
9. (Required) Confirm the Cloud Identity Engine app can successfully
   communicate with your directory.
   1. In the Cloud Identity Engine, click Test
      Connection to confirm that the Cloud Identity Engine can
      successfully connect to your Azure AD.

      ![]()
   2. (Optional) Enter a new name to Customize Directory
      Name in the Cloud Identity Engine.

      ![]()
10. (Optional) Select whether you want to Filter Azure Active Directory
    Groups.

    To reduce sync time and minimize the amount of data collected by the Cloud
    Identity Engine, you can configure the Cloud Identity Engine to sync only
    specific groups from your directory. To do this, you can [Configure SCIM Connector for the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) or you can filter the groups.
    Because SCIM is most suitable for small and frequent data requests, directory
    update intervals are restricted to once every 40 minutes. If you choose to
    filter the groups instead, directory updates can be as often as every 5 minutes.
    Choose the best option for your deployment based on your organizational and
    regulatory requirements.

    1. Select the group attribute you want to use as a filter.

       - Name—Filter the groups based on the group
         name.
       - Unique Identifier—Filter the groups based
         on the unique identifier for the group.

       ![]()
    2. Select how you want to filter the groups.

       - (for Name attribute
         only)begins with—Filter the
         groups based on a partial match for the text you enter.
       - is equal to—Filter the groups based on an
         exact match for text you enter.

       ![]()
    3. Enter the text you want to use to filter the groups.

       ![]()
    4. (Optional) Configure an additional filter by clicking Add
       OR and repeating the previous three steps for each
       filter you want to include.

       When you configure additional attributes, the Cloud Identity Engine
       initially attempts to find a match for the first criteria in the
       configuration, then continues to attempt to match based on the
       additional criteria you specify. 

       ![]()
11. Submit your changes and verify your directory information
    when the Directories page displays.

    You can now use your Azure AD to enforce group-based policy with the Cloud
    Identity Engine.

---

<a id="set-up-an-entra-id-directory-1"></a>

###### Set Up an Entra ID Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/set-up-azure-directory>*

Learn how to set up an Entra ID directory in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configure Microsoft Entra ID (formerly Azure AD) in the Cloud Identity Engine to
allow the Cloud Identity Engine to collect directory data for policy rule
enforcement and user visibility.

To configure directory sync with an Entra ID tenant using
the Cloud Identity Engine Enterprise app, you must be an Entra ID Global
Administrator or have a Global Administrator available to complete the app
registration using the onboarding URL.

As an alternative, you can [configure the SCIM connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) to select and
synchronize the Entra ID attribute data you want to collect with the Cloud Identity
Engine.

To further reduce sync time and minimize the amount of data collected by the Cloud
Identity Engine, you can configure the Cloud Identity Engine to sync only specific
groups from your directory by filtering the groups. Because SCIM is most suitable
for small and frequent data requests, Microsoft restricts directory update intervals
to once every 40 minutes. If you filter the groups instead, directory updates can
occur as often as every 5 minutes. Choose the best option for your deployment based
on your organizational and regulatory requirements.

The Cloud Identity Engine retrieves updates from your Entra ID tenant using the
following schedule:

- Users, Groups, and Devices—When the Cloud Identity Engine syncs
  changes.
- Apps—Every x hours (where x is either a
  maximum of 3 hours or the duration necessary to complete the previous apps
  sync).
- Role Assignments—Every x hours (where x is
  either a maximum of 24 hours or the duration necessary to complete the previous
  role assignment sync).

When you configure Entra ID for the Cloud
Identity Engine, log in, and grant the necessary permissions, Microsoft
automatically onboards the Cloud Identity Engine Enterprise App into Entra ID.

- [Cloud Identity Engine Enterprise
  App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/configure-azure-using-the-cie-enterprise-app.html#configure-azure-using-the-cie-enterprise-app)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad.html#id945b497c-f690-4c49-bc26-ed15f4118cbc)

<a id="configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb"></a>

###### Configure Entra ID Using the CIE Enterprise App

Learn how to configure Microsoft Entra ID in the Cloud Identity Engine using the CIE
Enterprise app.

1. Copy the Directory ID for your Entra ID tenant.
   1. Log in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or the Azure
      administrator portal using the credentials of the account you want to
      use to connect to the Cloud Identity Engine (for example, a service
      account) and select Overview.
   2. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
2. Set up your Entra ID tenant in the Cloud Identity Engine.
   1. In the Cloud Identity Engine app, select
      Directories, then click Add New
      Directory.
   2. Set Up an Entra ID Cloud
      Directory.

      ![]()
3. (Optional) Select additional information types to collect from Entra
   ID.

   The CIE Enterprise app automatically requests the privileges necessary to
   retrieve directory information, user risk information, and any other
   additional info you choose to collect. If you enable an option that
   requires additional privileges, you must reconnect the directory. For
   configurations that use the [CIE Enterprise app](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc),
   use the CIE Enterprise App onboarding URL in step
   [4.2](#configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc) to grant the
   necessary privileges.

   After onboarding the app into Entra ID, you can [revoke privileges](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions?pivots=portal#review-and-revoke-permissions) if they are
   not necessary for your configuration. Do not revoke privileges for
   options you select. If you revoke a privilege required for an option you
   select or for the Cloud Identity Engine by default, the sync cannot
   complete.

   To restore revoked permissions, edit the directory configuration and
   complete steps [4.1](#configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc) through [4.5](#configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc).

   The following list provides the permissions for each additional
   information type.

   - Collect user risk information from Entra ID Identity
     Protection:
     - IdentityRiskyUser.Read.All
     - IdentityRiskEvent.Read.All

     For more information, refer to [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
   - Collect Roles and Administrators (Administrative
     roles): Directory.Read.All or
     RoleManagement.Read.Directory
   - Collect enterprise applications:
     Application.Read.All
   - Collect device information:
     Device.Read.All

   1. Collect user risk information from Entra ID Identity
      Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

      ![]()
   2. Collect Roles and Administrators (Administrative
      roles) to retrieve
      roleAssignments attribute information for
      users and groups.

      Allowing the Cloud Identity Engine to include this information for
      analysis helps to prevent role-based malicious attacks.

      By default, the Cloud Identity Engine
      enables this option for tenants who are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex
      XDR.

      ![]()
   3. Collect enterprise applications data so that it
      displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If you don't want to collect the
      application data or you don't use application data in your Security
      policy, deselect the check box to decrease the sync time.

      ![]()
   4. Collect device information.

      This data is used by Cortex XDR and Device Security.
4. Configure your Entra ID information in the Cloud Identity Engine.
   1. Enter the directory ID you copied in step [1.2](#configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb) as the
      Directory ID.

      ![]()
   2. Generate the CIE Enterprise App onboarding URL
      to register the CIE Enterprise App in your Entra ID tenant.

      Registering the app in Microsoft Entra ID requires the Global
      Administrator role.

      If you do not have Global Administrator privileges in Entra ID,
      you must generate the URL and share it with an Entra ID
      administrator with Global Administrator privileges (Global
      Administrator role).

      1. Click Generate URL.
      2. Copy the resulting URL.
      3. Depending on your Entra ID role, perform one of the following
         actions:

         - (Global Administrator) Open the URL in a
           new tab or window to register the app
           instantly.
         - (Non-Global Administrator) Share the URL
           with an Entra ID administrator (Global
           Administrator) to complete the registration
           offline, then return to the Cloud Identity
           Engine.

      ![]()
   3. Enter the email address or phone number for the Global Administrator
      Role account you use to connect to the Cloud Identity Engine then click
      Next.

      ![]()
   4. Enter your password and Sign in.

      ![]()
   5. Click Accept to grant the necessary permissions
      for your Entra ID directory.

      When you accept, Entra ID automatically
      enables the following required permissions, as well as the
      additional information type permissions listed in step [3](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc):
      - Device.Read.All—Application, Read all
        devices
      - Group.Read.All—Application, Read all
        groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      ![]()
   6. Click Test Connection to confirm that the Cloud
      Identity Engine can successfully connect to your Entra ID tenant.

      ![]()
   7. (Optional) Enter a custom Directory Name
      (Optional) to use in the Cloud Identity Engine.

      ![]()
5. (Optional) Upload a .CSV file to use as a [filter for groups](#configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc).
   1. Click Upload CSV to upload a comma-separated
      value (CSV) file to use as a filter.

      ![]()
   2. Drag and drop the .CSV file or click Browse
      files to select the .CSV file you want to use as a
      filter.

      ![]()
   3. Select the Upload Type for the filter.

      - Update Filters—Update the existing
        filters with the .CSV data.
      - Replace Existing Filters—Replace the
        existing filters with the .CSV data.

      ![]()
   4. Select the Attribute Name you want to use for
      the filter (Name or Unique
      Identifier).
   5. Click Apply to confirm the changes.

      ![]()
6. (Optional) Filter Entra ID Groups.
   1. Select the group attribute you want to use as a filter.

      - Name—Filter the groups based on the group
        name.
      - Unique Identifier—Filter the groups based
        on the unique identifier for the group.

      ![]()
   2. Select how you want to filter the groups.

      - (for Name attribute only)
        begins with—Filter the groups based on a
        partial match for the text you enter.

        The filter supports spaces in the
        search query.
      - is equal to—Filter the groups based on an
        exact match for the text you enter.

      ![]()
   3. Enter the search query you want to use to filter the groups (either
      alphanumeric characters for a name or numeric characters for a unique
      identifier).

      ![]()
   4. (Optional) Configure an additional filter by clicking
      Add
      ORAdd
      Filter and repeating the previous three steps for each
      filter you want to include.

      If you select additional attributes as match conditions, the Cloud
      Identity Engine initially attempts to find a match for the first
      condition, then continues to match based on the additional conditions
      you specify. 

      ![]()
7. Submit your changes and verify your directory
   information when the Directories page displays.

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins"></a>

###### Configure Azure Using the Client Credential Flow

The Client Credential Flow option for Azure Active Directory (AD) in the Cloud Identity Engine
allows you to use a service account to log in to your Azure AD in the Cloud Identity
Engine. Using a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to be associated with a
specific user.

If this is the first
time you have created a Cloud Identity Engine tenant, the Cloud
Identity Engine app is not available in the Azure app gallery, so
you must create a custom app.

If you already have an existing
Azure AD configuration in the Cloud Identity Engine, you can easily migrate
the existing configuration to use the client credential flow option
by reconnecting your Azure AD to the Cloud Identity Engine, selecting
the Client Credential Flow option, and testing the connection to
verify the configuration.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity Engine
   tenant.
2. Grant the required read-only permissions in the Azure
   Portal.
   1. In the Azure Portal, select HomeAzure Active DirectoryApp Registrations.
   2. Click New registration.

      ![]()
   3. Enter a Name then click Register.

      ![]()
   4. Select API permissions then
      click Add a permission.

      ![]()
   5. Click Microsoft Graph then
      select Application permissions.

      ![]()
   6. Select the following permissions then click Add
      permissions:

      - Device.Read.All—Application, Read all
        devices
      - GroupMember.Read.All—Application, Read
        all groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      The permissions listed above represent the
      minimum required permissions that use least privilege access. If you
      prefer a less granular scope that is simpler to implement, you can
      use these permissions instead:
      - Directory.Read.All
      - Organization.Read.All

      - If you want to use user risk information in attribute-based
        [Cloud Dynamic User
        Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb), you must grant additional permissions.
        For more information, refer to the documentation on how to
        [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
      - If you want to collect information on roles and
        administrators, if you have already granted the 
        Directory.Read.All scope, no further
        permissions are required. If you are using the scopes listed
        above, you must also grant the 
        RoleManagement.Read.Directory scope to
        collect role and administrator information. For more
        information, refer to step [6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins).
      - If you want to collect enterprise application data, you must
        also grant the Application.Read.All
        scope. For more information, refer to step [7](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps).
   7. Click Grant admin consent for DirectoryName (where DirectoryName represents
      the name of your Azure AD).

      ![]()
   8. Click Yes to confirm.

      ![]()
3. Collect the necessary configuration information from
   the Azure Portal.
   1. In the Azure dashboard, select your Azure AD, then select
      App Registrations and select the app you
      created.
   2. Select Certificates & secrets then click
      New client secret.

      ![]()
   3. Enter a Description and Add the secret.

      When you add the secret, make sure to keep track of when the secret
      Expires. When the secret expires, you
      must configure the new secret in the Azure Portal and update the
      configuration in the Cloud Identity Engine app to replace the
      expired secret. Keep this in mind when selecting the expiry value
      for the secret. If you prioritize ease of configuration, select a
      longer expiration for the secret (the maximum value is 2 years). If
      security is of greater concern, select a shorter value for the
      secret’s expiration (the default is 6 months).

      ![]()
   4. Copy the Value of the secret and store it in a
      secure location.

      ![]()
   5. Click Overview then copy the
      Application (client) ID and store it in a
      secure location.

      ![]()
   6. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
4. Add your Azure AD directory in the Cloud Identity Engine.

   (Required for migration) If you are migrating an existing Azure AD
   configuration, select ActionsReconnect on the Directories page for the Azure AD
   you want to migrate. The Cloud Identity Engine automatically populates the
   necessary information so you can continue to step [9](#id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb) (testing the connection).

   1. In the Cloud Identity Engine app, select
      Directories then click Add New
      Directory.
   2. Set Up an Azure
      directory.

      ![]()
5. Select whether you want to Collect user risk information from Azure
   AD Identity Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to the documentation for [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb).

   ![]()
6. Select whether you want to Collect Roles and Administrators
   (Administrative roles) to retrieve
   roleAssignments attribute information for users and
   groups. Allowing the Cloud Identity Engine to include this information for
   analysis helps to prevent role-based malicious attacks.

   By default, the Cloud Identity Engine enables this
   option for tenants that are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex XDR.

   ![]()

   If you do not see the Collect Roles and
   Administrators (Administrative roles) option, [reconnect](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/reconnect-directory) your directory to select
   the option.
7. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If
   you don't want to collect the application data or you don't use application data
   in your security policy, deselect the checkbox to decrease the sync time. If you
   select this option, you must enable additional permissions for the Cloud
   Identity Engine (see step [2.6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c)).

   For beta users of this feature, the Cloud Identity
   Engine continues collecting enterprise application data for any directories
   configured in your tenant during the beta and no further configuration is
   required. If you configure a new directory, you must select whether you want
   to collect enterprise application data from the new directory.

   ![]()
8. Enter your directory information as indicated, using the information you copied
   from the Azure Portal in steps [3.4](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb):

   During migration of an existing Azure AD
   configuration to the client credential flow, the Cloud Identity Engine
   automatically populates the Directory ID.

   |

   Copy from Azure Portal | Enter in Cloud Identity Engine |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Directory (tenant) ID | Directory ID |

   |

   Application (client) ID | Client ID |

   ![]()
9. (Required) Confirm the Cloud Identity Engine app can successfully
   communicate with your directory.
   1. In the Cloud Identity Engine, click Test
      Connection to confirm that the Cloud Identity Engine can
      successfully connect to your Azure AD.

      ![]()
   2. (Optional) Enter a new name to Customize Directory
      Name in the Cloud Identity Engine.

      ![]()
10. (Optional) Select whether you want to Filter Azure Active Directory
    Groups.

    To reduce sync time and minimize the amount of data collected by the Cloud
    Identity Engine, you can configure the Cloud Identity Engine to sync only
    specific groups from your directory. To do this, you can [Configure SCIM Connector for the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) or you can filter the groups.
    Because SCIM is most suitable for small and frequent data requests, directory
    update intervals are restricted to once every 40 minutes. If you choose to
    filter the groups instead, directory updates can be as often as every 5 minutes.
    Choose the best option for your deployment based on your organizational and
    regulatory requirements.

    1. Select the group attribute you want to use as a filter.

       - Name—Filter the groups based on the group
         name.
       - Unique Identifier—Filter the groups based
         on the unique identifier for the group.

       ![]()
    2. Select how you want to filter the groups.

       - (for Name attribute
         only)begins with—Filter the
         groups based on a partial match for the text you enter.
       - is equal to—Filter the groups based on an
         exact match for text you enter.

       ![]()
    3. Enter the text you want to use to filter the groups.

       ![]()
    4. (Optional) Configure an additional filter by clicking Add
       OR and repeating the previous three steps for each
       filter you want to include.

       When you configure additional attributes, the Cloud Identity Engine
       initially attempts to find a match for the first criteria in the
       configuration, then continues to attempt to match based on the
       additional criteria you specify. 

       ![]()
11. Submit your changes and verify your directory information
    when the Directories page displays.

    You can now use your Azure AD to enforce group-based policy with the Cloud
    Identity Engine.

---

<a id="set-up-an-entra-id-directory-2"></a>

###### Set Up an Entra ID Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/set-up-azure-directory/configure-azure-using-the-cie-enterprise-app>*

Learn how to set up an Entra ID directory in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configure Microsoft Entra ID (formerly Azure AD) in the Cloud Identity Engine to
allow the Cloud Identity Engine to collect directory data for policy rule
enforcement and user visibility.

To configure directory sync with an Entra ID tenant using
the Cloud Identity Engine Enterprise app, you must be an Entra ID Global
Administrator or have a Global Administrator available to complete the app
registration using the onboarding URL.

As an alternative, you can [configure the SCIM connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) to select and
synchronize the Entra ID attribute data you want to collect with the Cloud Identity
Engine.

To further reduce sync time and minimize the amount of data collected by the Cloud
Identity Engine, you can configure the Cloud Identity Engine to sync only specific
groups from your directory by filtering the groups. Because SCIM is most suitable
for small and frequent data requests, Microsoft restricts directory update intervals
to once every 40 minutes. If you filter the groups instead, directory updates can
occur as often as every 5 minutes. Choose the best option for your deployment based
on your organizational and regulatory requirements.

The Cloud Identity Engine retrieves updates from your Entra ID tenant using the
following schedule:

- Users, Groups, and Devices—When the Cloud Identity Engine syncs
  changes.
- Apps—Every x hours (where x is either a
  maximum of 3 hours or the duration necessary to complete the previous apps
  sync).
- Role Assignments—Every x hours (where x is
  either a maximum of 24 hours or the duration necessary to complete the previous
  role assignment sync).

When you configure Entra ID for the Cloud
Identity Engine, log in, and grant the necessary permissions, Microsoft
automatically onboards the Cloud Identity Engine Enterprise App into Entra ID.

- [Cloud Identity Engine Enterprise
  App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/configure-azure-using-the-cie-enterprise-app.html#configure-azure-using-the-cie-enterprise-app)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad.html#id945b497c-f690-4c49-bc26-ed15f4118cbc)

<a id="configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb"></a>

###### Configure Entra ID Using the CIE Enterprise App

Learn how to configure Microsoft Entra ID in the Cloud Identity Engine using the CIE
Enterprise app.

1. Copy the Directory ID for your Entra ID tenant.
   1. Log in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or the Azure
      administrator portal using the credentials of the account you want to
      use to connect to the Cloud Identity Engine (for example, a service
      account) and select Overview.
   2. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
2. Set up your Entra ID tenant in the Cloud Identity Engine.
   1. In the Cloud Identity Engine app, select
      Directories, then click Add New
      Directory.
   2. Set Up an Entra ID Cloud
      Directory.

      ![]()
3. (Optional) Select additional information types to collect from Entra
   ID.

   The CIE Enterprise app automatically requests the privileges necessary to
   retrieve directory information, user risk information, and any other
   additional info you choose to collect. If you enable an option that
   requires additional privileges, you must reconnect the directory. For
   configurations that use the [CIE Enterprise app](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc),
   use the CIE Enterprise App onboarding URL in step
   [4.2](#configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc) to grant the
   necessary privileges.

   After onboarding the app into Entra ID, you can [revoke privileges](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions?pivots=portal#review-and-revoke-permissions) if they are
   not necessary for your configuration. Do not revoke privileges for
   options you select. If you revoke a privilege required for an option you
   select or for the Cloud Identity Engine by default, the sync cannot
   complete.

   To restore revoked permissions, edit the directory configuration and
   complete steps [4.1](#configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc) through [4.5](#configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc).

   The following list provides the permissions for each additional
   information type.

   - Collect user risk information from Entra ID Identity
     Protection:
     - IdentityRiskyUser.Read.All
     - IdentityRiskEvent.Read.All

     For more information, refer to [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
   - Collect Roles and Administrators (Administrative
     roles): Directory.Read.All or
     RoleManagement.Read.Directory
   - Collect enterprise applications:
     Application.Read.All
   - Collect device information:
     Device.Read.All

   1. Collect user risk information from Entra ID Identity
      Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

      ![]()
   2. Collect Roles and Administrators (Administrative
      roles) to retrieve
      roleAssignments attribute information for
      users and groups.

      Allowing the Cloud Identity Engine to include this information for
      analysis helps to prevent role-based malicious attacks.

      By default, the Cloud Identity Engine
      enables this option for tenants who are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex
      XDR.

      ![]()
   3. Collect enterprise applications data so that it
      displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If you don't want to collect the
      application data or you don't use application data in your Security
      policy, deselect the check box to decrease the sync time.

      ![]()
   4. Collect device information.

      This data is used by Cortex XDR and Device Security.
4. Configure your Entra ID information in the Cloud Identity Engine.
   1. Enter the directory ID you copied in step [1.2](#configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb) as the
      Directory ID.

      ![]()
   2. Generate the CIE Enterprise App onboarding URL
      to register the CIE Enterprise App in your Entra ID tenant.

      Registering the app in Microsoft Entra ID requires the Global
      Administrator role.

      If you do not have Global Administrator privileges in Entra ID,
      you must generate the URL and share it with an Entra ID
      administrator with Global Administrator privileges (Global
      Administrator role).

      1. Click Generate URL.
      2. Copy the resulting URL.
      3. Depending on your Entra ID role, perform one of the following
         actions:

         - (Global Administrator) Open the URL in a
           new tab or window to register the app
           instantly.
         - (Non-Global Administrator) Share the URL
           with an Entra ID administrator (Global
           Administrator) to complete the registration
           offline, then return to the Cloud Identity
           Engine.

      ![]()
   3. Enter the email address or phone number for the Global Administrator
      Role account you use to connect to the Cloud Identity Engine then click
      Next.

      ![]()
   4. Enter your password and Sign in.

      ![]()
   5. Click Accept to grant the necessary permissions
      for your Entra ID directory.

      When you accept, Entra ID automatically
      enables the following required permissions, as well as the
      additional information type permissions listed in step [3](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc):
      - Device.Read.All—Application, Read all
        devices
      - Group.Read.All—Application, Read all
        groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      ![]()
   6. Click Test Connection to confirm that the Cloud
      Identity Engine can successfully connect to your Entra ID tenant.

      ![]()
   7. (Optional) Enter a custom Directory Name
      (Optional) to use in the Cloud Identity Engine.

      ![]()
5. (Optional) Upload a .CSV file to use as a [filter for groups](#configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc).
   1. Click Upload CSV to upload a comma-separated
      value (CSV) file to use as a filter.

      ![]()
   2. Drag and drop the .CSV file or click Browse
      files to select the .CSV file you want to use as a
      filter.

      ![]()
   3. Select the Upload Type for the filter.

      - Update Filters—Update the existing
        filters with the .CSV data.
      - Replace Existing Filters—Replace the
        existing filters with the .CSV data.

      ![]()
   4. Select the Attribute Name you want to use for
      the filter (Name or Unique
      Identifier).
   5. Click Apply to confirm the changes.

      ![]()
6. (Optional) Filter Entra ID Groups.
   1. Select the group attribute you want to use as a filter.

      - Name—Filter the groups based on the group
        name.
      - Unique Identifier—Filter the groups based
        on the unique identifier for the group.

      ![]()
   2. Select how you want to filter the groups.

      - (for Name attribute only)
        begins with—Filter the groups based on a
        partial match for the text you enter.

        The filter supports spaces in the
        search query.
      - is equal to—Filter the groups based on an
        exact match for the text you enter.

      ![]()
   3. Enter the search query you want to use to filter the groups (either
      alphanumeric characters for a name or numeric characters for a unique
      identifier).

      ![]()
   4. (Optional) Configure an additional filter by clicking
      Add
      ORAdd
      Filter and repeating the previous three steps for each
      filter you want to include.

      If you select additional attributes as match conditions, the Cloud
      Identity Engine initially attempts to find a match for the first
      condition, then continues to match based on the additional conditions
      you specify. 

      ![]()
7. Submit your changes and verify your directory
   information when the Directories page displays.

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins"></a>

###### Configure Azure Using the Client Credential Flow

The Client Credential Flow option for Azure Active Directory (AD) in the Cloud Identity Engine
allows you to use a service account to log in to your Azure AD in the Cloud Identity
Engine. Using a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to be associated with a
specific user.

If this is the first
time you have created a Cloud Identity Engine tenant, the Cloud
Identity Engine app is not available in the Azure app gallery, so
you must create a custom app.

If you already have an existing
Azure AD configuration in the Cloud Identity Engine, you can easily migrate
the existing configuration to use the client credential flow option
by reconnecting your Azure AD to the Cloud Identity Engine, selecting
the Client Credential Flow option, and testing the connection to
verify the configuration.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity Engine
   tenant.
2. Grant the required read-only permissions in the Azure
   Portal.
   1. In the Azure Portal, select HomeAzure Active DirectoryApp Registrations.
   2. Click New registration.

      ![]()
   3. Enter a Name then click Register.

      ![]()
   4. Select API permissions then
      click Add a permission.

      ![]()
   5. Click Microsoft Graph then
      select Application permissions.

      ![]()
   6. Select the following permissions then click Add
      permissions:

      - Device.Read.All—Application, Read all
        devices
      - GroupMember.Read.All—Application, Read
        all groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      The permissions listed above represent the
      minimum required permissions that use least privilege access. If you
      prefer a less granular scope that is simpler to implement, you can
      use these permissions instead:
      - Directory.Read.All
      - Organization.Read.All

      - If you want to use user risk information in attribute-based
        [Cloud Dynamic User
        Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb), you must grant additional permissions.
        For more information, refer to the documentation on how to
        [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
      - If you want to collect information on roles and
        administrators, if you have already granted the 
        Directory.Read.All scope, no further
        permissions are required. If you are using the scopes listed
        above, you must also grant the 
        RoleManagement.Read.Directory scope to
        collect role and administrator information. For more
        information, refer to step [6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins).
      - If you want to collect enterprise application data, you must
        also grant the Application.Read.All
        scope. For more information, refer to step [7](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps).
   7. Click Grant admin consent for DirectoryName (where DirectoryName represents
      the name of your Azure AD).

      ![]()
   8. Click Yes to confirm.

      ![]()
3. Collect the necessary configuration information from
   the Azure Portal.
   1. In the Azure dashboard, select your Azure AD, then select
      App Registrations and select the app you
      created.
   2. Select Certificates & secrets then click
      New client secret.

      ![]()
   3. Enter a Description and Add the secret.

      When you add the secret, make sure to keep track of when the secret
      Expires. When the secret expires, you
      must configure the new secret in the Azure Portal and update the
      configuration in the Cloud Identity Engine app to replace the
      expired secret. Keep this in mind when selecting the expiry value
      for the secret. If you prioritize ease of configuration, select a
      longer expiration for the secret (the maximum value is 2 years). If
      security is of greater concern, select a shorter value for the
      secret’s expiration (the default is 6 months).

      ![]()
   4. Copy the Value of the secret and store it in a
      secure location.

      ![]()
   5. Click Overview then copy the
      Application (client) ID and store it in a
      secure location.

      ![]()
   6. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
4. Add your Azure AD directory in the Cloud Identity Engine.

   (Required for migration) If you are migrating an existing Azure AD
   configuration, select ActionsReconnect on the Directories page for the Azure AD
   you want to migrate. The Cloud Identity Engine automatically populates the
   necessary information so you can continue to step [9](#id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb) (testing the connection).

   1. In the Cloud Identity Engine app, select
      Directories then click Add New
      Directory.
   2. Set Up an Azure
      directory.

      ![]()
5. Select whether you want to Collect user risk information from Azure
   AD Identity Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to the documentation for [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb).

   ![]()
6. Select whether you want to Collect Roles and Administrators
   (Administrative roles) to retrieve
   roleAssignments attribute information for users and
   groups. Allowing the Cloud Identity Engine to include this information for
   analysis helps to prevent role-based malicious attacks.

   By default, the Cloud Identity Engine enables this
   option for tenants that are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex XDR.

   ![]()

   If you do not see the Collect Roles and
   Administrators (Administrative roles) option, [reconnect](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/reconnect-directory) your directory to select
   the option.
7. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If
   you don't want to collect the application data or you don't use application data
   in your security policy, deselect the checkbox to decrease the sync time. If you
   select this option, you must enable additional permissions for the Cloud
   Identity Engine (see step [2.6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c)).

   For beta users of this feature, the Cloud Identity
   Engine continues collecting enterprise application data for any directories
   configured in your tenant during the beta and no further configuration is
   required. If you configure a new directory, you must select whether you want
   to collect enterprise application data from the new directory.

   ![]()
8. Enter your directory information as indicated, using the information you copied
   from the Azure Portal in steps [3.4](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb):

   During migration of an existing Azure AD
   configuration to the client credential flow, the Cloud Identity Engine
   automatically populates the Directory ID.

   |

   Copy from Azure Portal | Enter in Cloud Identity Engine |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Directory (tenant) ID | Directory ID |

   |

   Application (client) ID | Client ID |

   ![]()
9. (Required) Confirm the Cloud Identity Engine app can successfully
   communicate with your directory.
   1. In the Cloud Identity Engine, click Test
      Connection to confirm that the Cloud Identity Engine can
      successfully connect to your Azure AD.

      ![]()
   2. (Optional) Enter a new name to Customize Directory
      Name in the Cloud Identity Engine.

      ![]()
10. (Optional) Select whether you want to Filter Azure Active Directory
    Groups.

    To reduce sync time and minimize the amount of data collected by the Cloud
    Identity Engine, you can configure the Cloud Identity Engine to sync only
    specific groups from your directory. To do this, you can [Configure SCIM Connector for the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) or you can filter the groups.
    Because SCIM is most suitable for small and frequent data requests, directory
    update intervals are restricted to once every 40 minutes. If you choose to
    filter the groups instead, directory updates can be as often as every 5 minutes.
    Choose the best option for your deployment based on your organizational and
    regulatory requirements.

    1. Select the group attribute you want to use as a filter.

       - Name—Filter the groups based on the group
         name.
       - Unique Identifier—Filter the groups based
         on the unique identifier for the group.

       ![]()
    2. Select how you want to filter the groups.

       - (for Name attribute
         only)begins with—Filter the
         groups based on a partial match for the text you enter.
       - is equal to—Filter the groups based on an
         exact match for text you enter.

       ![]()
    3. Enter the text you want to use to filter the groups.

       ![]()
    4. (Optional) Configure an additional filter by clicking Add
       OR and repeating the previous three steps for each
       filter you want to include.

       When you configure additional attributes, the Cloud Identity Engine
       initially attempts to find a match for the first criteria in the
       configuration, then continues to attempt to match based on the
       additional criteria you specify. 

       ![]()
11. Submit your changes and verify your directory information
    when the Directories page displays.

    You can now use your Azure AD to enforce group-based policy with the Cloud
    Identity Engine.

---

<a id="set-up-an-entra-id-directory-3"></a>

###### Set Up an Entra ID Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad>*

Learn how to set up an Entra ID directory in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Configure Microsoft Entra ID (formerly Azure AD) in the Cloud Identity Engine to
allow the Cloud Identity Engine to collect directory data for policy rule
enforcement and user visibility.

To configure directory sync with an Entra ID tenant using
the Cloud Identity Engine Enterprise app, you must be an Entra ID Global
Administrator or have a Global Administrator available to complete the app
registration using the onboarding URL.

As an alternative, you can [configure the SCIM connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) to select and
synchronize the Entra ID attribute data you want to collect with the Cloud Identity
Engine.

To further reduce sync time and minimize the amount of data collected by the Cloud
Identity Engine, you can configure the Cloud Identity Engine to sync only specific
groups from your directory by filtering the groups. Because SCIM is most suitable
for small and frequent data requests, Microsoft restricts directory update intervals
to once every 40 minutes. If you filter the groups instead, directory updates can
occur as often as every 5 minutes. Choose the best option for your deployment based
on your organizational and regulatory requirements.

The Cloud Identity Engine retrieves updates from your Entra ID tenant using the
following schedule:

- Users, Groups, and Devices—When the Cloud Identity Engine syncs
  changes.
- Apps—Every x hours (where x is either a
  maximum of 3 hours or the duration necessary to complete the previous apps
  sync).
- Role Assignments—Every x hours (where x is
  either a maximum of 24 hours or the duration necessary to complete the previous
  role assignment sync).

When you configure Entra ID for the Cloud
Identity Engine, log in, and grant the necessary permissions, Microsoft
automatically onboards the Cloud Identity Engine Enterprise App into Entra ID.

- [Cloud Identity Engine Enterprise
  App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/configure-azure-using-the-cie-enterprise-app.html#configure-azure-using-the-cie-enterprise-app)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad.html#id945b497c-f690-4c49-bc26-ed15f4118cbc)

<a id="configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc"></a>

<a id="configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb"></a>

###### Configure Entra ID Using the CIE Enterprise App

Learn how to configure Microsoft Entra ID in the Cloud Identity Engine using the CIE
Enterprise app.

1. Copy the Directory ID for your Entra ID tenant.
   1. Log in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or the Azure
      administrator portal using the credentials of the account you want to
      use to connect to the Cloud Identity Engine (for example, a service
      account) and select Overview.
   2. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
2. Set up your Entra ID tenant in the Cloud Identity Engine.
   1. In the Cloud Identity Engine app, select
      Directories, then click Add New
      Directory.
   2. Set Up an Entra ID Cloud
      Directory.

      ![]()
3. (Optional) Select additional information types to collect from Entra
   ID.

   The CIE Enterprise app automatically requests the privileges necessary to
   retrieve directory information, user risk information, and any other
   additional info you choose to collect. If you enable an option that
   requires additional privileges, you must reconnect the directory. For
   configurations that use the [CIE Enterprise app](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc),
   use the CIE Enterprise App onboarding URL in step
   [4.2](#configure-azure-using-the-cie-enterprise-app_substep-gbl_rtr_tcc) to grant the
   necessary privileges.

   After onboarding the app into Entra ID, you can [revoke privileges](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions?pivots=portal#review-and-revoke-permissions) if they are
   not necessary for your configuration. Do not revoke privileges for
   options you select. If you revoke a privilege required for an option you
   select or for the Cloud Identity Engine by default, the sync cannot
   complete.

   To restore revoked permissions, edit the directory configuration and
   complete steps [4.1](#configure-azure-using-the-cie-enterprise-app_substep-hrm_rns_tcc) through [4.5](#configure-azure-using-the-cie-enterprise-app_substep-dsr_tns_tcc).

   The following list provides the permissions for each additional
   information type.

   - Collect user risk information from Entra ID Identity
     Protection:
     - IdentityRiskyUser.Read.All
     - IdentityRiskEvent.Read.All

     For more information, refer to [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
   - Collect Roles and Administrators (Administrative
     roles): Directory.Read.All or
     RoleManagement.Read.Directory
   - Collect enterprise applications:
     Application.Read.All
   - Collect device information:
     Device.Read.All

   1. Collect user risk information from Entra ID Identity
      Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

      ![]()
   2. Collect Roles and Administrators (Administrative
      roles) to retrieve
      roleAssignments attribute information for
      users and groups.

      Allowing the Cloud Identity Engine to include this information for
      analysis helps to prevent role-based malicious attacks.

      By default, the Cloud Identity Engine
      enables this option for tenants who are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex
      XDR.

      ![]()
   3. Collect enterprise applications data so that it
      displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If you don't want to collect the
      application data or you don't use application data in your Security
      policy, deselect the check box to decrease the sync time.

      ![]()
   4. Collect device information.

      This data is used by Cortex XDR and Device Security.
4. Configure your Entra ID information in the Cloud Identity Engine.
   1. Enter the directory ID you copied in step [1.2](#configure-azure-using-the-cie-enterprise-app_substep_ccy_cpy_txb) as the
      Directory ID.

      ![]()
   2. Generate the CIE Enterprise App onboarding URL
      to register the CIE Enterprise App in your Entra ID tenant.

      Registering the app in Microsoft Entra ID requires the Global
      Administrator role.

      If you do not have Global Administrator privileges in Entra ID,
      you must generate the URL and share it with an Entra ID
      administrator with Global Administrator privileges (Global
      Administrator role).

      1. Click Generate URL.
      2. Copy the resulting URL.
      3. Depending on your Entra ID role, perform one of the following
         actions:

         - (Global Administrator) Open the URL in a
           new tab or window to register the app
           instantly.
         - (Non-Global Administrator) Share the URL
           with an Entra ID administrator (Global
           Administrator) to complete the registration
           offline, then return to the Cloud Identity
           Engine.

      ![]()
   3. Enter the email address or phone number for the Global Administrator
      Role account you use to connect to the Cloud Identity Engine then click
      Next.

      ![]()
   4. Enter your password and Sign in.

      ![]()
   5. Click Accept to grant the necessary permissions
      for your Entra ID directory.

      When you accept, Entra ID automatically
      enables the following required permissions, as well as the
      additional information type permissions listed in step [3](#configure-azure-using-the-cie-enterprise-app_step-bjz_n45_wbc):
      - Device.Read.All—Application, Read all
        devices
      - Group.Read.All—Application, Read all
        groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      ![]()
   6. Click Test Connection to confirm that the Cloud
      Identity Engine can successfully connect to your Entra ID tenant.

      ![]()
   7. (Optional) Enter a custom Directory Name
      (Optional) to use in the Cloud Identity Engine.

      ![]()
5. (Optional) Upload a .CSV file to use as a [filter for groups](#configure-azure-using-the-cie-enterprise-app_step-o3m_2p5_wbc).
   1. Click Upload CSV to upload a comma-separated
      value (CSV) file to use as a filter.

      ![]()
   2. Drag and drop the .CSV file or click Browse
      files to select the .CSV file you want to use as a
      filter.

      ![]()
   3. Select the Upload Type for the filter.

      - Update Filters—Update the existing
        filters with the .CSV data.
      - Replace Existing Filters—Replace the
        existing filters with the .CSV data.

      ![]()
   4. Select the Attribute Name you want to use for
      the filter (Name or Unique
      Identifier).
   5. Click Apply to confirm the changes.

      ![]()
6. (Optional) Filter Entra ID Groups.
   1. Select the group attribute you want to use as a filter.

      - Name—Filter the groups based on the group
        name.
      - Unique Identifier—Filter the groups based
        on the unique identifier for the group.

      ![]()
   2. Select how you want to filter the groups.

      - (for Name attribute only)
        begins with—Filter the groups based on a
        partial match for the text you enter.

        The filter supports spaces in the
        search query.
      - is equal to—Filter the groups based on an
        exact match for the text you enter.

      ![]()
   3. Enter the search query you want to use to filter the groups (either
      alphanumeric characters for a name or numeric characters for a unique
      identifier).

      ![]()
   4. (Optional) Configure an additional filter by clicking
      Add
      ORAdd
      Filter and repeating the previous three steps for each
      filter you want to include.

      If you select additional attributes as match conditions, the Cloud
      Identity Engine initially attempts to find a match for the first
      condition, then continues to match based on the additional conditions
      you specify. 

      ![]()
7. Submit your changes and verify your directory
   information when the Directories page displays.

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps"></a>

<a id="id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins"></a>

###### Configure Azure Using the Client Credential Flow

The Client Credential Flow option for Azure Active Directory (AD) in the Cloud Identity Engine
allows you to use a service account to log in to your Azure AD in the Cloud Identity
Engine. Using a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to be associated with a
specific user.

If this is the first
time you have created a Cloud Identity Engine tenant, the Cloud
Identity Engine app is not available in the Azure app gallery, so
you must create a custom app.

If you already have an existing
Azure AD configuration in the Cloud Identity Engine, you can easily migrate
the existing configuration to use the client credential flow option
by reconnecting your Azure AD to the Cloud Identity Engine, selecting
the Client Credential Flow option, and testing the connection to
verify the configuration.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity Engine
   tenant.
2. Grant the required read-only permissions in the Azure
   Portal.
   1. In the Azure Portal, select HomeAzure Active DirectoryApp Registrations.
   2. Click New registration.

      ![]()
   3. Enter a Name then click Register.

      ![]()
   4. Select API permissions then
      click Add a permission.

      ![]()
   5. Click Microsoft Graph then
      select Application permissions.

      ![]()
   6. Select the following permissions then click Add
      permissions:

      - Device.Read.All—Application, Read all
        devices
      - GroupMember.Read.All—Application, Read
        all groups
      - User.Read.All—Application, Read all
        users' full profiles
      - User.Read—Delegated, Sign in and read
        user profile

      The permissions listed above represent the
      minimum required permissions that use least privilege access. If you
      prefer a less granular scope that is simpler to implement, you can
      use these permissions instead:
      - Directory.Read.All
      - Organization.Read.All

      - If you want to use user risk information in attribute-based
        [Cloud Dynamic User
        Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb), you must grant additional permissions.
        For more information, refer to the documentation on how to
        [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
      - If you want to collect information on roles and
        administrators, if you have already granted the 
        Directory.Read.All scope, no further
        permissions are required. If you are using the scopes listed
        above, you must also grant the 
        RoleManagement.Read.Directory scope to
        collect role and administrator information. For more
        information, refer to step [6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-roles-admins).
      - If you want to collect enterprise application data, you must
        also grant the Application.Read.All
        scope. For more information, refer to step [7](#id945b497c-f690-4c49-bc26-ed15f4118cbc_collect-enterprise-apps).
   7. Click Grant admin consent for DirectoryName (where DirectoryName represents
      the name of your Azure AD).

      ![]()
   8. Click Yes to confirm.

      ![]()
3. Collect the necessary configuration information from
   the Azure Portal.
   1. In the Azure dashboard, select your Azure AD, then select
      App Registrations and select the app you
      created.
   2. Select Certificates & secrets then click
      New client secret.

      ![]()
   3. Enter a Description and Add the secret.

      When you add the secret, make sure to keep track of when the secret
      Expires. When the secret expires, you
      must configure the new secret in the Azure Portal and update the
      configuration in the Cloud Identity Engine app to replace the
      expired secret. Keep this in mind when selecting the expiry value
      for the secret. If you prioritize ease of configuration, select a
      longer expiration for the secret (the maximum value is 2 years). If
      security is of greater concern, select a shorter value for the
      secret’s expiration (the default is 6 months).

      ![]()
   4. Copy the Value of the secret and store it in a
      secure location.

      ![]()
   5. Click Overview then copy the
      Application (client) ID and store it in a
      secure location.

      ![]()
   6. Copy the Directory (tenant) ID and store it in a
      secure location.

      ![]()
4. Add your Azure AD directory in the Cloud Identity Engine.

   (Required for migration) If you are migrating an existing Azure AD
   configuration, select ActionsReconnect on the Directories page for the Azure AD
   you want to migrate. The Cloud Identity Engine automatically populates the
   necessary information so you can continue to step [9](#id945b497c-f690-4c49-bc26-ed15f4118cbc_step_n4y_t4y_txb) (testing the connection).

   1. In the Cloud Identity Engine app, select
      Directories then click Add New
      Directory.
   2. Set Up an Azure
      directory.

      ![]()
5. Select whether you want to Collect user risk information from Azure
   AD Identity Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to the documentation for [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb).

   ![]()
6. Select whether you want to Collect Roles and Administrators
   (Administrative roles) to retrieve
   roleAssignments attribute information for users and
   groups. Allowing the Cloud Identity Engine to include this information for
   analysis helps to prevent role-based malicious attacks.

   By default, the Cloud Identity Engine enables this
   option for tenants that are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex XDR.

   ![]()

   If you do not see the Collect Roles and
   Administrators (Administrative roles) option, [reconnect](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/reconnect-directory) your directory to select
   the option.
7. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If
   you don't want to collect the application data or you don't use application data
   in your security policy, deselect the checkbox to decrease the sync time. If you
   select this option, you must enable additional permissions for the Cloud
   Identity Engine (see step [2.6](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep-pkk_rxq_q1c)).

   For beta users of this feature, the Cloud Identity
   Engine continues collecting enterprise application data for any directories
   configured in your tenant during the beta and no further configuration is
   required. If you configure a new directory, you must select whether you want
   to collect enterprise application data from the new directory.

   ![]()
8. Enter your directory information as indicated, using the information you copied
   from the Azure Portal in steps [3.4](#id945b497c-f690-4c49-bc26-ed15f4118cbc_substep_s4c_cpy_txb):

   During migration of an existing Azure AD
   configuration to the client credential flow, the Cloud Identity Engine
   automatically populates the Directory ID.

   |

   Copy from Azure Portal | Enter in Cloud Identity Engine |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Directory (tenant) ID | Directory ID |

   |

   Application (client) ID | Client ID |

   ![]()
9. (Required) Confirm the Cloud Identity Engine app can successfully
   communicate with your directory.
   1. In the Cloud Identity Engine, click Test
      Connection to confirm that the Cloud Identity Engine can
      successfully connect to your Azure AD.

      ![]()
   2. (Optional) Enter a new name to Customize Directory
      Name in the Cloud Identity Engine.

      ![]()
10. (Optional) Select whether you want to Filter Azure Active Directory
    Groups.

    To reduce sync time and minimize the amount of data collected by the Cloud
    Identity Engine, you can configure the Cloud Identity Engine to sync only
    specific groups from your directory. To do this, you can [Configure SCIM Connector for the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) or you can filter the groups.
    Because SCIM is most suitable for small and frequent data requests, directory
    update intervals are restricted to once every 40 minutes. If you choose to
    filter the groups instead, directory updates can be as often as every 5 minutes.
    Choose the best option for your deployment based on your organizational and
    regulatory requirements.

    1. Select the group attribute you want to use as a filter.

       - Name—Filter the groups based on the group
         name.
       - Unique Identifier—Filter the groups based
         on the unique identifier for the group.

       ![]()
    2. Select how you want to filter the groups.

       - (for Name attribute
         only)begins with—Filter the
         groups based on a partial match for the text you enter.
       - is equal to—Filter the groups based on an
         exact match for text you enter.

       ![]()
    3. Enter the text you want to use to filter the groups.

       ![]()
    4. (Optional) Configure an additional filter by clicking Add
       OR and repeating the previous three steps for each
       filter you want to include.

       When you configure additional attributes, the Cloud Identity Engine
       initially attempts to find a match for the first criteria in the
       configuration, then continues to attempt to match based on the
       additional criteria you specify. 

       ![]()
11. Submit your changes and verify your directory information
    when the Directories page displays.

    You can now use your Azure AD to enforce group-based policy with the Cloud
    Identity Engine.

---

<a id="configure-a-cloud-based-directory-1"></a>

###### Configure a Cloud-Based Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/reconnect-directory>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

After you activate your Cloud Identity Engine tenant,
configure a cloud-based directory, such as Azure Active Directory
(Azure AD), Okta Directory, or Google Directory, to communicate
with the Cloud Identity Engine.

Configuring a cloud-based directory in the Cloud Identity Engine enables
your network security infrastructure to identify users and enforce
policies based on identity rather than IP addresses. By granting the
Cloud Identity Engine read-only access to your organization's
directory data, you establish a centralized source of truth that
synchronizes user, group, and device attributes across your entire
deployment.

For [Microsoft Entra ID (Azure AD)](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory.html), you can
establish a connection using the recommended CIE Enterprise App or a
client credential flow, with options to collect advanced data like
user risk signals for dynamic policy adjustments. [Okta
integrations](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html) offer similar flexibility, allowing you
to connect via an OpenID Connect (OIDC) app using either an
authorization code or client credential flow to sync user and group
attributes. For organizations using [Google
Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-google-directory-in-the-cloud-identity-engine.html), the engine connects directly via the
Google Admin API to retrieve organizational units and user
details.

If your organization requires a more customized approach or uses a
different provider, the [SCIM
Connector](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) allows you to ingest identity data from any
SCIM-compliant source—such as PingFederate or customized Entra ID
setups—giving you granular control over which attributes are shared.
Additionally, for scenarios where an external identity provider is
not available or necessary, you can configure a [CIE Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html). This
cloud-native, local directory lets you create and manage users
directly within the engine, offering a quick solution for testing or
specific user segments without requiring external
infrastructure.

To use the System for Cross-domain Identity Management (SCIM)
provisioning to customize which attributes your Azure AD shares
with the Cloud Identity Engine, you can configure the SCIM Connector.

If the connection between your directory and the Cloud Identity
Engine is not active, you can reconnect your directory. If you no
longer want to associate a directory with the Cloud Identity Engine,
learn how to revoke the permissions for that directory.

---

<a id="manage-your-azure-directory"></a>

###### Manage Your Azure Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure/revoke-cloud-identity-engine-permissions-for-azure-ad>*

Learn about managing your Azure directory for CIE.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Managing your Microsoft Entra ID (Azure AD) integration is critical for ensuring that
the Cloud Identity Engine maintains a valid, secure connection to collect user
attributes for consistent policy enforcement. Ongoing management tasks typically
involve troubleshooting connection issues or updating configuration settings to
leverage new features, such as switching from the CIE Enterprise App to the Client
Credential Flow or enabling the collection of user risk information.

If your directory disconnects or requires configuration updates, you can **reconnect
or edit** the directory directly within the Cloud Identity Engine application.
This process allows you to re-authenticate and modify settings without deleting the
tenant. However, if you need to permanently stop the Cloud Identity Engine from
accessing your data, you must **revoke permissions** entirely. This is a two-step
process: you must first delete the directory from your Cloud Identity Engine tenant
and then delete the enterprise application from the Azure Portal to ensure the
service can no longer query your directory data.

- [Reconnect or Edit](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-azure-directory/reconnect-directory.html#idb99373f7-aa27-449f-969a-0b2649b58666)
- [Revoke Permissions](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-azure-directory/revoke-cloud-identity-engine-permissions-for-azure-ad.html#id620f0db5-3c6e-4330-aea4-6af2c01b1c71)

<a id="idb99373f7-aa27-449f-969a-0b2649b58666_step-srv_zwh_s1c"></a>

<a id="idb99373f7-aa27-449f-969a-0b2649b58666_step-emg_lxh_s1c"></a>

###### Reconnect or Edit Azure Active Directory

Learn how to reconnect or edit your Azure Active Directory (Azure AD) configuration for
the Cloud Identity Engine.

The auth code flow
method has been deprecated and is not available for new configurations, only
existing configurations. For new configurations, [configure Entra ID using the Cloud Identity Engine app](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory.html).

1. Log in to the hub and select the Cloud Identity Engine app.
2. In the Cloud Identity Engine app, select DirectoriesReconnect.

   ![]()

   If this Azure AD configuration has never
   successfully connected to the Cloud Identity Engine, select ActionsEdit.

   ![]()
3. Select the method you want to use to log in to your Azure AD.

   ![]()

   Palo Alto Networks strongly recommends the CIE Enterprise
   App connection flow type. Using the client credential connection
   flow type requires you to configure your Azure AD with the necessary
   permissions, so ensure you’ve completed all of the predeployment steps necessary
   to [configure Azure using the Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory.html) before
   you configure this option.
   - CIE Enterprise App
     (Recommended) (Default) — This option requires Global
     Administrator privileges but you only need to enter the directory ID.
   - Client Credential Flow—By granting the required
     permissions in advance, you do not need to log in to the Azure AD to
     make changes to that directory in the Cloud Identity Engine.
4. Select whether you want to Collect user risk information from Azure
   AD Identity Protection to use in attribute-based [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to the documentation for [Cloud Dynamic User Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb).

   ![]()
5. Select whether you want to Collect Roles and Administrators
   (Administrative roles) to retrieve
   roleAssignments attribute information for users and
   groups. Allowing the Cloud Identity Engine to include this information for
   analysis helps to prevent role-based malicious attacks. By default, the Cloud
   Identity Engine enables this option for tenants that are [associated](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance) with Cortex XDR.

   If you select this option, you must grant additional
   permissions for the Cloud Identity Engine in the Azure AD Portal. For more
   information, refer to step 9.

   ![]()
6. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html). If
   you don't want to collect the application data or you don't use application data
   in your security policy, deselect the checkbox to decrease the sync time.

   ![]()
7. Sign in with Azureor Restore
   the connection using your Azure administrator credentials and grant
   permissions for the Cloud Identity Engine to access the directory
   information.

   You must have an administrative account for the
   directory to grant the following required permissions.
   - Access Azure Service Management
   - View your basic profile
   - Maintain access to data you have given it access to
   - Read directory data
   - View your email address

   ![]()

   If this Azure AD configuration has never
   successfully connected to the Cloud Identity Engine, select Sign
   in with Azure. 

   ![]()

   1. Enter your email address or phone number then click
      Next.

      ![]()
   2. Enter your password and Sign in.

      ![]()
   3. Consent on behalf your organization to grant the
      permissions that the Cloud Identity Engine requires to get the metadata
      with the list of directories and Accept to
      confirm.

      ![]()

      The button displays Logged In when the
      authentication is successful.
8. Click Test Connection to confirm that the Cloud Identity
   Engine tenant can successfully communicate with the Azure directory.

   ![]()

   - The Cloud Identity Engine checks for the primary directory, which may
     not be the same as initial directory.
   - While the test is in progress, the button displays
     Testing.
   - When the Cloud Identity Engine verifies the connection, the button
     displays Success and lists the domain name
     and ID for the directory.
   - If the connection is not successful, the button displays
     Failed and a red exclamation point. If
     this occurs, confirm you have entered your Azure credentials correctly.
   - If you have more than one directory in your Azure AD, select the radio
     button for each directory and Test Connection.
     Submit each directory individually.
9. Consent on behalf your organization to grant the
   permissions the Cloud Identity Engine requires to access the directory data and
   Accept to confirm.

   - If you want to use user risk information in attribute-based [Cloud Dynamic User
     Groups](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html#create-a-cloud-dynamic-user-group_ul_w3p_pgp_sxb), you must grant additional permissions. For more
     information, refer to the documentation on how to [Create a Cloud Dynamic User Group](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/create-a-cloud-dynamic-user-group.html).
   - If you select the Collect Roles and Administrators
     (Administrative roles) option in step [5](#idb99373f7-aa27-449f-969a-0b2649b58666_step-srv_zwh_s1c) and you have
     already granted the  Directory.Read.All
     scope, no further permissions are required. Otherwise, you must also
     grant the  RoleManagement.Read.Directory
     scope to collect role and administrator information.
   - If you select the Collect enterprise
     applications option in step [6](#idb99373f7-aa27-449f-969a-0b2649b58666_step-emg_lxh_s1c), you must grant the
      Application.Read.All scope.

   ![]()
10. (Optional) Enter a unique name as the  Directory Name
    (optional) field to use a customized name for the directory in
    the Cloud Identity Engine app.

    You can use up to 15 lowercase alphanumeric
    characters (including hyphens, periods, and underscores) for the directory
    name in the Cloud Identity Engine. You don't need to change the name of the
    directory itself, only the name of the directory in the Cloud Identity
    Engine app.

    ![]()

    If you are collecting data for the same domain from
    both an on-premises Active Directory (AD) and an Azure AD, Palo Alto
    Networks recommends that you create a separate Cloud Identity Engine tenant
    for each directory type. If you must use the same Cloud Identity Engine
    tenant and want to collect data from both an on-premises AD and an Azure AD,
    you must customize the directory name for the Azure AD (for example, by
    adding .aad to Customize Directory
    Name) then reconnect or edit your Azure directory. Any
    applications that you [associate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) with the Cloud Identity
    Engine use the custom directory name.

    - The custom directory name is the alias for your Azure AD in your Cloud
      Identity Engine tenant; it does not change the name of your directory.
      If you do not enter a custom directory name, the Cloud Identity Engine
      uses the default domain name.
    - The Cloud Identity Engine supports lowercase alphanumeric characters,
      periods (.), hyphens (-), and underscores (\_).
    - If you associate the Cloud Identity Engine with Cortex XDR, the
      customized directory name must be identical to the
      Domain you [select in Cortex XDR](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-pro-admin/get-started-with-cortex-xdr-pro/set-up-cloud-identity-engine).

    The custom directory name must match the
    corresponding directory name in any app that you associate with the Cloud
    Identity Engine. For example, if you are using the Cloud Identity Engine
    with Cortex XDR, the custom directory name in the Cloud Identity Engine must
    be the same as the directory name in Cortex XDR.
11. (Optional) Select whether you want to Filter Azure Active Directory
    Groups.

    To reduce sync time and minimize the amount of data collected by the Cloud
    Identity Engine, you can configure the Cloud Identity Engine to sync only
    specific groups from your directory. To do this, you can [Configure SCIM Connector for the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine.html) or you can filter the groups.
    Because SCIM is most suitable for small and frequent data requests, directory
    update intervals are restricted to once every 40 minutes. If you choose to
    filter the groups instead, directory updates can be as often as every 5 minutes.
    Choose the best option for your deployment based on your organizational and
    regulatory requirements.

    1. Select the group attribute you want to use as a filter.

       - Name—Filter the groups based on the group
         name.
       - Unique Identifier—Filter the groups based
         on the unique identifier for the group.

       ![]()
    2. Select how you want to filter the groups.

       - (for Name attribute
         only)begins with—Filter the
         groups based on a partial match for the text you enter.
       - is equal to—Filter the groups based on an
         exact match for text you enter.

       ![]()
    3. Enter the text you want to use to filter the groups.

       ![]()
    4. (Optional) Configure an additional filter by clicking Add
       OR and repeating the previous three steps for each
       filter you want to include.

       When you configure additional attributes, the Cloud Identity Engine
       initially attempts to find a match for the first criteria in the
       configuration, then continues to attempt to match based on the
       additional criteria you specify. 

       ![]()
12. When the configuration is complete, Submit the
    configuration.

    When you submit the configuration, the Cloud Identity Engine connects to your
    Azure AD and begins synchronizing attributes. The Sync
    Status column displays In Progress while
    the Cloud Identity Engine collects the attributes.

###### Revoke Cloud Identity Engine Permissions for Azure Active Directory

Learn how to revoke permissions for the Cloud Identity
Engine to access your Azure Active Directory (AD).

If you want to revoke the permissions for
the Cloud Identity Engine to access your Azure Active Directory
(AD), delete the directory in your Cloud Identity Engine tenant
and delete the application from the Azure Portal.

To revoke
permissions for an Azure AD from the Cloud Identity Engine, you
must have at least the following role privileges in Azure AD: Application
Administrator and Cloud Application Administrator. For more information about
roles in Azure AD, refer to the following [link](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference).

1. [Delete](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/delete-domains-or-directories-from-cloud-identity-engine-instances.html#id32517175-335d-4dd7-a5ea-b4bfb5948d0a) the
   directory from your Cloud Identity Engine tenant.
2. Log in to the [Azure Portal](https://portal.azure.com) with your
   administrator credentials.
3. Select Azure Active Directory.

   ![]()
4. In the Manage section, select Enterprise
   applications.

   ![]()
5. In the Manage section, select All
   applications then select Palo Alto Networks
   Cloud Identity Engine.
6. In the Manage section, select Properties.
7. Delete the application and click Yes to
   confirm.

   When
   you confirm, the Cloud Identity Engine can no longer access this
   Azure AD.

---

<a id="configure-okta-directory"></a>

###### Configure Okta Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine can integrate Okta Directory information. When you
configure your Okta Directory as part of the Cloud Identity Engine, the Cloud
Identity Engine uses Okta Directory to collect user and group attribute information
for Security policy enforcement and for visibility into the users who access your
network.

You must create a separate OpenID Connect (OIDC) app integration to configure an
Okta directory for the Cloud Identity Engine, even if you’ve configured Okta as
an [identity provider](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html) for SAML.
If you try to use the SAML app to configure an Okta directory instead of
creating a new OIDC app, the initial sync might be successful, but any
subsequent syncs fail because the refresh token from the gallery application
does not support this configuration.

You can select one of two methods for the Cloud Identity Engine to use to connect to
your Okta Directory:

- The Auth Code Flow, which requires you to log in to make changes to the
  directory configuration in the Cloud Identity Engine.
- (Recommended) The Client Credential Flow, which initially requires
  additional permissions but does not require you to log in to change the
  directory configuration in the Cloud Identity Engine.

For an Okta directory, the Cloud Identity Engine retrieves updates from the directory
using the following schedule:

- **Users, Groups, and Devices**—When the Cloud Identity Engine syncs
  changes.
- **Apps**—Every x hours (where x is
  either a maximum of three hours or the duration necessary to complete the
  previous apps sync).

- [Auth Code Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-auth-code-for-okta-directory.html#deploy-auth-code-for-okta-directory)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html#idce7fa5eb-95db-4fa5-8514-cddfbd1763ff)

<a id="deploy-auth-code-for-okta-directory_substep-ucn_gtd_jhc"></a>

###### Deploy Auth Code for Okta Directory

Learn about configuring your Okta directory using the auth code deployment
method.

Deploying the Auth Code Flow for Okta Directory requires
you to log in using administrator privileges to change the configuration for the Okta
directory in the Cloud Identity Engine and that you [reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html) the Okta directory every 90 days to avoid sync failure.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine and
   obtain the Sign-in redirect URI for Okta.
   1. After activating the Cloud Identity Engine, log in to the hub and
      select the Cloud Identity Engine app.
   2. Copy the URL for your Cloud Identity Engine tenant and edit it to
      obtain the Sign-in redirect URI that Okta requires. To edit the URL,
      replace the text after the domain with
      /authorize. For example, if your Cloud Identity
      Engine tenant URL is
      https://directory-sync.us.paloaltonetworks.com/directory?instance=<InstanceId>,
      your Redirect URL is
      https://directory-sync.us.paloaltonetworks.com/authorize.
2. Using the Okta Administrator Dashboard, prepare to add your Okta Directory in
   the Cloud Identity Engine.

   To set up an Okta Directory in the Cloud Identity
   Engine, you must create a user then assign Admin
   Roles to that user to grant privileges for the Okta
   Directory in the Okta Administrator Dashboard (SecurityAdministratorsAdminsAdd Administrator). 

   ![]()

   This is the account you’ll assign to the app in step 2.6. This is also
   the same account you'll use to log in for step 8 when using the Auth Code
   Flow for your Okta Directory.

   1. [Create an app integration](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm) for
      the Cloud Identity Engine app in Okta.

      ![]()
   2. Select OIDC - OpenID Connect as the
      Sign-in method.
   3. Select Web Application as the
      Application type then click
      Next.

      ![]()
   4. Click the X button to clear the current entry
      and replace the existing Sign-in redirect URIs
      with the edited URL from step 1.2.

      ![]()

      Palo Alto Networks recommends separating regions by aligning
      region-specific tenants with region-specific Okta accounts.
      However, for testing, if you have Cloud Identity Engine tenants
      in more than one region, add Sign-in redirect URIs for each
      region where you have a tenant.
   5. Skip the steps for Sign-out redirect URIs and
      Base URIs as these aren't required.
   6. Since you will assign Controlled Access later in
      this procedure, Skip group assignment for now
      then Save the configuration.

      When you assign the app in
      step [5.a](#deploy-auth-code-for-okta-directory_substep-ucn_gtd_jhc), be sure to assign the app only to
      the administrator you created in the first step.
3. Configure the Okta app integration.
   1. Edit the General Settings
      for the app you just created.

      ![]()
   2. Select Refresh token as the Grant
      type.

      Using the refresh token is
      mandatory.

      ![]()
   3. Select Use persistent token.

      ![]()

      If you select the Auth Code
      Flow configuration, you must [reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html) the Okta directory every 90 days
      to prevent sync failure. If you don't want to reconnect the Okta
      directory every 90 days, reconnect the directory and select the
      [Client Credential
      Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html) option.
   4. Save your changes.
4. Obtain the information about your Okta app integration that you need to
   configure in the Cloud Identity Engine.
   1. At the top of the page, select
      General (if it is not already selected), then
      [copy](https://developer.okta.com/docs/guides/find-your-app-credentials/findcreds/) your Client
      ID and Secret.

      ![]()
   2. Select your username in the upper right to [copy](https://developer.okta.com/docs/guides/find-your-domain/findorg/) your Okta domain.

      ![]()
5. Assign the app and grant the required permissions for the Cloud Identity Engine
   to access your Okta directory information.
   1. Select Assignments, then [assign](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_Apps_Page.htm) the Cloud Identity
      Engine app to the administrator who configures the Okta integration in
      the Cloud Identity Engine.

      ![]()
   2. Select Okta API Scopes and [grant consent](https://developer.okta.com/docs/guides/implement-oauth-for-okta/scopes/) to the following
      scopes:

      - okta.authorizationServers.read
        (Required only if you have more than one Okta authorization
        server)
      - okta.groups.read
      - okta.logs.read

        The Cloud Identity Engine requires this scope to read the
        following log events only:
        - user.lifecycle.delete.initiated
        - group.lifecycle.delete
        - user.lifecycle.activate
        - user.lifecycle.deactivateThe Cloud Identity Engine uses a filter to retrieve
        only these events, it does not receive any other events for
        this scope.
      - okta.users.read
      - okta.users.read.self

      If you want the Cloud Identity Engine to
      collect enterprise application data so that it is included when you
      [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html), you must grant consent to the
      okta.apps.read scope before you select
      the option in step 9.

      ![]()

      If all the scopes display Not
      granted and you cannot view the Grant
       option, scroll to the bottom of the page and scroll
      over within the table to view the option. 

      ![]()
6. In the Cloud Identity Engine app, select DirectoriesAdd Directory.
7. Set Up a Cloud Directory and
   select Okta.

   ![]()
8. Select Auth Code Flow as the method you want to use to
   log in to the Okta directory.

   ![]()
9. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html).

   ![]()
10. (Strata Logging Service only) Select whether you want to
    Collect authentication logs and forward to Strata Logging
    Service.

    If you select this option, the Cloud Identity Engine forwards the Okta
    authentication logs from the previous 24 hours to the [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service) for storage,
    auditing purposes, and use by [Autonomous Digital Experience Management
    (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem/administration/autonomous-dem).

    ![]()
11. Specify your Okta Directory information to allow the Cloud Identity Engine to
    connect to your Okta Directory.

    ![]()

    1. Paste your Okta Directory Domain that you copied
       in step 4.2.
    2. Paste your Okta Directory Client ID and
       Client Secret that you copied in step 4.1.

       The Client
       ID must begin with 0.
12. Click to Sign in with Okta and enter your Okta Directory
    credentials.

    When the login is successful, Logged In displays. Palo
    Alto Networks recommends using the built-in authorization server. If you have
    more than one Okta authorization server, repeat the previous steps for each
    additional Okta Directory you want to add. 

    ![]()
13. Click Test Connection to verify your configuration.

    When the test is successful, Success displays.
14. (Optional) Customize the name the Cloud Identity Engine displays for your Okta
    Directory.

    By default, the Cloud Identity Engine uses the default domain name.

    You can use up to 15 lowercase alphanumeric characters
    (including hyphens, periods, and underscores) for the directory name in the
    Cloud Identity Engine. You don't need to change the name of the directory
    itself, only the name of the directory in the Cloud Identity Engine app.
15. Submit the configuration.

    You can now use information from your Okta Directory in the Cloud Identity
    Engine when you configure a user- or group-based Security policy rule or with
    other Palo Alto Networks applications.

    For optimal
    performance, the Cloud Identity Engine does not support the default Okta
    group "[Everyone](https://support.okta.com/help/s/article/The-Everyone-Group-in-Okta?language=en_US)" because Okta does not
    recommend using this group to define policy rules.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="idce7fa5eb-95db-4fa5-8514-cddfbd1763ff_substep-nmj_2pk_jhc"></a>

###### Deploy Client Credential Flow for Okta

By granting a few read-only permissions for
your Okta directory in advance, the Client Credential Flow option
for Okta in the Cloud Identity Engine allows you to use a service account
to log in to your Okta directory in the Cloud Identity Engine. Using
a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to
be associated with a specific user.

You must obtain a
new client ID and secret if you have an existing Okta directory
configuration. The client ID and secret for the Okta directory auth
code flow (the existing method) are not compatible with the API
service integration that the client credential flow method uses.

1. Download the Okta integration app from the [Okta Integration Network](https://www.okta.com/integrations/).
   1. In the Okta Administrator Portal, select Applications API Service Integrations.

      ![]()
   2. Click Add Integration.

      ![]()
   3. Search for Palo Alto Networks Cloud Identity
      Engine.

      ![]()
   4. Select the app integration you want to use based on whether you want to
      enable app data and click Next.

      To ensure that you select
      the correct app, either use Find in your
      browser (Ctrl+ F) to
      search for the app you want to use or hover over the app to display
      the full app name.

      - If you use application data in your security policy, select the
        Palo Alto Networks Cloud Identity Engine
        (Application-enabled) app. For more information
        on collecting application data, see Step 9 in [Configure Okta Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html). 

        ![]()
      - If you do not use application data in your security policy,
        select the Palo Alto Networks Cloud Identity
        Engine app. 

        ![]()
2. Install and configure the API service integration.
3. Install & Authorize the API
   service integration.

   ![]()

   The
   Okta API service integration automatically configures the following
   required API scopes:

   - Users and groups—Read existing users’ profiles and credentials. Read
     about groups and their members. Read the signed-in user's profile and
     credentials.
   - Authorization servers—Read about authorization
     servers.
   - (Application-enabled app
     only)Apps—Read about apps.
   - Logs—Read about system log entries.
4. Click Copy to clipboard to copy the client secret and
   store it in a secure location, then click Done.

   ![]()

   The client secret displays only once,
   so make sure to copy it and store it securely before clicking
   Done.
5. Copy the Okta Domain and the Client
   ID and store them in a secure location.

   You must edit the domain by removing
   the https:// before pasting it.

   ![]()
6. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity
   Engine tenant.
7. Set up a Cloud Directory and
   select Okta.
8. Under Select Connection Flow,
   select Client Credential Flow.

   ![]()
9. Select Collect enterprise applications to display
   application data when you view directory data.

   If you select this option, you must
   use the Palo Alto Networks Cloud Identity Engine
   (Application-enabled) app to ensure the correct permissions.
   For more information, see step [1.d](#idce7fa5eb-95db-4fa5-8514-cddfbd1763ff_substep-nmj_2pk_jhc).

   ![]()
10. (Strata Logging Service only) Select whether you want to
    Collect authentication logs and forward to Strata Logging
    Service for retention and further analysis.

    ![]()
11. Paste the information you copied from the Okta management console into the
    fields as indicated in the following table.

    |

    Okta Managment Console Field | Cloud Identity Engine App Field |

    | --- | --- |

    |  |  |
    | --- | --- |
    |

    Okta Domain | Domain |

    |

    Client ID | Client ID |

    |

    Client Secret | Client Secret |

    ![]()
12. Click Test Connection to verify
    the Cloud Identity Engine can successfully communicate with your
    Okta directory.

    You must test the connection to submit the configuration.
13. (Optional) Customize the name of the directory that displays
    in the Cloud Identity Engine.

    If you want to use a custom name for this directory in
    the Cloud Identity Engine, enter the custom name as the Directory
    Name (Optional).
14. Submit your changes and verify
    your directory information when the Directories page
    displays.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

---

<a id="manage-your-okta-directory"></a>

###### Manage Your Okta Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/reconnect-okta-directory>*

Learn about managing your Okta directory for CIE.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Managing your Okta directory involves maintaining the secure connection established
via the Okta Integration Network to ensure continuous user attribute
synchronization. If your deployment utilizes the Auth Code Flow, you must
**reconnect** the directory every 90 days to refresh authentication tokens
and prevent synchronization failures. Alternatively, reconfiguration to the Client
Credential Flow allows you to use a service account, which eliminates the need for
frequent re-authentication and is recommended for long-term stability.

You can also edit your configuration to enable advanced features, such as forwarding
authentication logs to the Strata Logging Service or collecting enterprise
application data for broader visibility. To permanently **remove** the directory,
you must first delete the Cloud Identity Engine integration from the Okta Admin
Dashboard to revoke privileges, and then remove the directory from the Cloud
Identity Engine tenant.

- [Reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html#iddd9bd2f4-bc70-427f-89b7-5573dfdefdfb)
- [Remove](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/remove-okta-directory.html#id14a6a875-36e7-40f3-a16b-95aec63934bf)

###### Reconnect Okta Directory

If there’s a connection loss between the Cloud Identity Engine and your Okta Directory,
follow these steps to reconnect your directory.

If the connection between your Okta directory and the Cloud Identity Engine isn’t active or if
you want to make changes to your Okta directory configuration, you can reconnect
your Okta directory to the Cloud Identity Engine.

1. Log in to the hub and select the Cloud Identity Engine tenant that contains the
   Okta directory you want to reconnect.
2. Select Directories.
3. Select ActionsReconnect for the directory
   you want to reconnect.

   ![]()
4. Select whether you want to make any changes to your configuration.

   - If you want to use a service account to log in to the Okta directory,
     select the Client Credential Flow. For more
     information, refer to [Deploy Client Credential Flow for Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html).
   - If you want the Cloud Identity Engine to Collect enterprise
     applications data so that it is included when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html), select the checkbox. If you don't use enterprise
     application data in your security policy or you don't want to collect
     the data, deselect the checkbox.
   - If you want the Cloud Identity Engine to Collect
     authentication logs and forward to Strata Logging
     Service, select the checkbox. If you don't want to
     forward logs or you don't use [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service),
     deselect the checkbox.

   ![]()
5. (Auth Code Flow only) Sign in with Okta using
   your Okta administrator credentials and grant permissions for the Cloud Identity
   Engine to access the directory information.
6. (Client credential flow only) Enter the Client
   ID and Client Secret (or click
   Restore to restore the current client secret).

   You cannot change the Domain.
   If you need to change the domain, you must [create](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html) a new Okta
   directory configuration in the Cloud Identity Engine.
7. Click Test Connection to confirm the Cloud Identity
   Engine can access your Okta directory.
8. (Optional) Customize Directory Name if you want
   to change the name that the Cloud Identity Engine displays for this directory in
   your tenant.

   You can use up to 15 lowercase alphanumeric
   characters (including hyphens, periods, and underscores) for the directory
   name in the Cloud Identity Engine. You don't need to change the name of the
   directory itself, only the name of the directory in the Cloud Identity
   Engine app. If your directory name contains more than 15 characters, you
   must change the directory name to contain a maximum of 15 characters.
9. Submit your configuration.

###### Remove Okta Directory

If you no longer need to sync your Okta Directory, learn
how to remove it from the Cloud Identity Engine.

If you no longer need to sync your Okta Directory
with the Cloud Identity Engine, you can remove it from the Cloud
Identity Engine.

1. Remove the Cloud Identity Engine integration from Okta.
   1. Log in to the Okta Admin Dashboard.
   2. Select ApplicationsApplications.

      ![]()
   3. Select the Cloud Identity Engine integration you want
      to remove.
   4. Select InactiveDelete.

      ![]()
   5. Click Delete Application to
      confirm that you want to remove the Cloud Identity Engine integration
      from Okta.

      ![]()
2. Remove the Okta Directory from the Cloud Identity Engine app.
   1. In the Cloud Identity Engine app, select Directories.
   2. Select ActionsRemove.

      ![]()
   3. Click Yes to confirm removal
      of the directory.

---

<a id="manage-your-okta-directory-1"></a>

###### Manage Your Okta Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/remove-okta-directory>*

Learn about managing your Okta directory for CIE.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Managing your Okta directory involves maintaining the secure connection established
via the Okta Integration Network to ensure continuous user attribute
synchronization. If your deployment utilizes the Auth Code Flow, you must
**reconnect** the directory every 90 days to refresh authentication tokens
and prevent synchronization failures. Alternatively, reconfiguration to the Client
Credential Flow allows you to use a service account, which eliminates the need for
frequent re-authentication and is recommended for long-term stability.

You can also edit your configuration to enable advanced features, such as forwarding
authentication logs to the Strata Logging Service or collecting enterprise
application data for broader visibility. To permanently **remove** the directory,
you must first delete the Cloud Identity Engine integration from the Okta Admin
Dashboard to revoke privileges, and then remove the directory from the Cloud
Identity Engine tenant.

- [Reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html#iddd9bd2f4-bc70-427f-89b7-5573dfdefdfb)
- [Remove](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/remove-okta-directory.html#id14a6a875-36e7-40f3-a16b-95aec63934bf)

###### Reconnect Okta Directory

If there’s a connection loss between the Cloud Identity Engine and your Okta Directory,
follow these steps to reconnect your directory.

If the connection between your Okta directory and the Cloud Identity Engine isn’t active or if
you want to make changes to your Okta directory configuration, you can reconnect
your Okta directory to the Cloud Identity Engine.

1. Log in to the hub and select the Cloud Identity Engine tenant that contains the
   Okta directory you want to reconnect.
2. Select Directories.
3. Select ActionsReconnect for the directory
   you want to reconnect.

   ![]()
4. Select whether you want to make any changes to your configuration.

   - If you want to use a service account to log in to the Okta directory,
     select the Client Credential Flow. For more
     information, refer to [Deploy Client Credential Flow for Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html).
   - If you want the Cloud Identity Engine to Collect enterprise
     applications data so that it is included when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html), select the checkbox. If you don't use enterprise
     application data in your security policy or you don't want to collect
     the data, deselect the checkbox.
   - If you want the Cloud Identity Engine to Collect
     authentication logs and forward to Strata Logging
     Service, select the checkbox. If you don't want to
     forward logs or you don't use [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service),
     deselect the checkbox.

   ![]()
5. (Auth Code Flow only) Sign in with Okta using
   your Okta administrator credentials and grant permissions for the Cloud Identity
   Engine to access the directory information.
6. (Client credential flow only) Enter the Client
   ID and Client Secret (or click
   Restore to restore the current client secret).

   You cannot change the Domain.
   If you need to change the domain, you must [create](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html) a new Okta
   directory configuration in the Cloud Identity Engine.
7. Click Test Connection to confirm the Cloud Identity
   Engine can access your Okta directory.
8. (Optional) Customize Directory Name if you want
   to change the name that the Cloud Identity Engine displays for this directory in
   your tenant.

   You can use up to 15 lowercase alphanumeric
   characters (including hyphens, periods, and underscores) for the directory
   name in the Cloud Identity Engine. You don't need to change the name of the
   directory itself, only the name of the directory in the Cloud Identity
   Engine app. If your directory name contains more than 15 characters, you
   must change the directory name to contain a maximum of 15 characters.
9. Submit your configuration.

###### Remove Okta Directory

If you no longer need to sync your Okta Directory, learn
how to remove it from the Cloud Identity Engine.

If you no longer need to sync your Okta Directory
with the Cloud Identity Engine, you can remove it from the Cloud
Identity Engine.

1. Remove the Cloud Identity Engine integration from Okta.
   1. Log in to the Okta Admin Dashboard.
   2. Select ApplicationsApplications.

      ![]()
   3. Select the Cloud Identity Engine integration you want
      to remove.
   4. Select InactiveDelete.

      ![]()
   5. Click Delete Application to
      confirm that you want to remove the Cloud Identity Engine integration
      from Okta.

      ![]()
2. Remove the Okta Directory from the Cloud Identity Engine app.
   1. In the Cloud Identity Engine app, select Directories.
   2. Select ActionsRemove.

      ![]()
   3. Click Yes to confirm removal
      of the directory.

---

<a id="configure-okta-directory-1"></a>

###### Configure Okta Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine can integrate Okta Directory information. When you
configure your Okta Directory as part of the Cloud Identity Engine, the Cloud
Identity Engine uses Okta Directory to collect user and group attribute information
for Security policy enforcement and for visibility into the users who access your
network.

You must create a separate OpenID Connect (OIDC) app integration to configure an
Okta directory for the Cloud Identity Engine, even if you’ve configured Okta as
an [identity provider](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html) for SAML.
If you try to use the SAML app to configure an Okta directory instead of
creating a new OIDC app, the initial sync might be successful, but any
subsequent syncs fail because the refresh token from the gallery application
does not support this configuration.

You can select one of two methods for the Cloud Identity Engine to use to connect to
your Okta Directory:

- The Auth Code Flow, which requires you to log in to make changes to the
  directory configuration in the Cloud Identity Engine.
- (Recommended) The Client Credential Flow, which initially requires
  additional permissions but does not require you to log in to change the
  directory configuration in the Cloud Identity Engine.

For an Okta directory, the Cloud Identity Engine retrieves updates from the directory
using the following schedule:

- **Users, Groups, and Devices**—When the Cloud Identity Engine syncs
  changes.
- **Apps**—Every x hours (where x is
  either a maximum of three hours or the duration necessary to complete the
  previous apps sync).

- [Auth Code Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-auth-code-for-okta-directory.html#deploy-auth-code-for-okta-directory)
- [Client Credential Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html#idce7fa5eb-95db-4fa5-8514-cddfbd1763ff)

<a id="deploy-auth-code-for-okta-directory_substep-ucn_gtd_jhc"></a>

###### Deploy Auth Code for Okta Directory

Learn about configuring your Okta directory using the auth code deployment
method.

Deploying the Auth Code Flow for Okta Directory requires
you to log in using administrator privileges to change the configuration for the Okta
directory in the Cloud Identity Engine and that you [reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html) the Okta directory every 90 days to avoid sync failure.

1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine and
   obtain the Sign-in redirect URI for Okta.
   1. After activating the Cloud Identity Engine, log in to the hub and
      select the Cloud Identity Engine app.
   2. Copy the URL for your Cloud Identity Engine tenant and edit it to
      obtain the Sign-in redirect URI that Okta requires. To edit the URL,
      replace the text after the domain with
      /authorize. For example, if your Cloud Identity
      Engine tenant URL is
      https://directory-sync.us.paloaltonetworks.com/directory?instance=<InstanceId>,
      your Redirect URL is
      https://directory-sync.us.paloaltonetworks.com/authorize.
2. Using the Okta Administrator Dashboard, prepare to add your Okta Directory in
   the Cloud Identity Engine.

   To set up an Okta Directory in the Cloud Identity
   Engine, you must create a user then assign Admin
   Roles to that user to grant privileges for the Okta
   Directory in the Okta Administrator Dashboard (SecurityAdministratorsAdminsAdd Administrator). 

   ![]()

   This is the account you’ll assign to the app in step 2.6. This is also
   the same account you'll use to log in for step 8 when using the Auth Code
   Flow for your Okta Directory.

   1. [Create an app integration](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm) for
      the Cloud Identity Engine app in Okta.

      ![]()
   2. Select OIDC - OpenID Connect as the
      Sign-in method.
   3. Select Web Application as the
      Application type then click
      Next.

      ![]()
   4. Click the X button to clear the current entry
      and replace the existing Sign-in redirect URIs
      with the edited URL from step 1.2.

      ![]()

      Palo Alto Networks recommends separating regions by aligning
      region-specific tenants with region-specific Okta accounts.
      However, for testing, if you have Cloud Identity Engine tenants
      in more than one region, add Sign-in redirect URIs for each
      region where you have a tenant.
   5. Skip the steps for Sign-out redirect URIs and
      Base URIs as these aren't required.
   6. Since you will assign Controlled Access later in
      this procedure, Skip group assignment for now
      then Save the configuration.

      When you assign the app in
      step [5.a](#deploy-auth-code-for-okta-directory_substep-ucn_gtd_jhc), be sure to assign the app only to
      the administrator you created in the first step.
3. Configure the Okta app integration.
   1. Edit the General Settings
      for the app you just created.

      ![]()
   2. Select Refresh token as the Grant
      type.

      Using the refresh token is
      mandatory.

      ![]()
   3. Select Use persistent token.

      ![]()

      If you select the Auth Code
      Flow configuration, you must [reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-okta-directory/reconnect-okta-directory.html) the Okta directory every 90 days
      to prevent sync failure. If you don't want to reconnect the Okta
      directory every 90 days, reconnect the directory and select the
      [Client Credential
      Flow](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine/deploy-client-credential-flow-for-okta.html) option.
   4. Save your changes.
4. Obtain the information about your Okta app integration that you need to
   configure in the Cloud Identity Engine.
   1. At the top of the page, select
      General (if it is not already selected), then
      [copy](https://developer.okta.com/docs/guides/find-your-app-credentials/findcreds/) your Client
      ID and Secret.

      ![]()
   2. Select your username in the upper right to [copy](https://developer.okta.com/docs/guides/find-your-domain/findorg/) your Okta domain.

      ![]()
5. Assign the app and grant the required permissions for the Cloud Identity Engine
   to access your Okta directory information.
   1. Select Assignments, then [assign](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_Apps_Page.htm) the Cloud Identity
      Engine app to the administrator who configures the Okta integration in
      the Cloud Identity Engine.

      ![]()
   2. Select Okta API Scopes and [grant consent](https://developer.okta.com/docs/guides/implement-oauth-for-okta/scopes/) to the following
      scopes:

      - okta.authorizationServers.read
        (Required only if you have more than one Okta authorization
        server)
      - okta.groups.read
      - okta.logs.read

        The Cloud Identity Engine requires this scope to read the
        following log events only:
        - user.lifecycle.delete.initiated
        - group.lifecycle.delete
        - user.lifecycle.activate
        - user.lifecycle.deactivateThe Cloud Identity Engine uses a filter to retrieve
        only these events, it does not receive any other events for
        this scope.
      - okta.users.read
      - okta.users.read.self

      If you want the Cloud Identity Engine to
      collect enterprise application data so that it is included when you
      [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html), you must grant consent to the
      okta.apps.read scope before you select
      the option in step 9.

      ![]()

      If all the scopes display Not
      granted and you cannot view the Grant
       option, scroll to the bottom of the page and scroll
      over within the table to view the option. 

      ![]()
6. In the Cloud Identity Engine app, select DirectoriesAdd Directory.
7. Set Up a Cloud Directory and
   select Okta.

   ![]()
8. Select Auth Code Flow as the method you want to use to
   log in to the Okta directory.

   ![]()
9. Select whether you want to Collect enterprise
   applications data so that it displays when you [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html).

   ![]()
10. (Strata Logging Service only) Select whether you want to
    Collect authentication logs and forward to Strata Logging
    Service.

    If you select this option, the Cloud Identity Engine forwards the Okta
    authentication logs from the previous 24 hours to the [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service) for storage,
    auditing purposes, and use by [Autonomous Digital Experience Management
    (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem/administration/autonomous-dem).

    ![]()
11. Specify your Okta Directory information to allow the Cloud Identity Engine to
    connect to your Okta Directory.

    ![]()

    1. Paste your Okta Directory Domain that you copied
       in step 4.2.
    2. Paste your Okta Directory Client ID and
       Client Secret that you copied in step 4.1.

       The Client
       ID must begin with 0.
12. Click to Sign in with Okta and enter your Okta Directory
    credentials.

    When the login is successful, Logged In displays. Palo
    Alto Networks recommends using the built-in authorization server. If you have
    more than one Okta authorization server, repeat the previous steps for each
    additional Okta Directory you want to add. 

    ![]()
13. Click Test Connection to verify your configuration.

    When the test is successful, Success displays.
14. (Optional) Customize the name the Cloud Identity Engine displays for your Okta
    Directory.

    By default, the Cloud Identity Engine uses the default domain name.

    You can use up to 15 lowercase alphanumeric characters
    (including hyphens, periods, and underscores) for the directory name in the
    Cloud Identity Engine. You don't need to change the name of the directory
    itself, only the name of the directory in the Cloud Identity Engine app.
15. Submit the configuration.

    You can now use information from your Okta Directory in the Cloud Identity
    Engine when you configure a user- or group-based Security policy rule or with
    other Palo Alto Networks applications.

    For optimal
    performance, the Cloud Identity Engine does not support the default Okta
    group "[Everyone](https://support.okta.com/help/s/article/The-Everyone-Group-in-Okta?language=en_US)" because Okta does not
    recommend using this group to define policy rules.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="idce7fa5eb-95db-4fa5-8514-cddfbd1763ff_substep-nmj_2pk_jhc"></a>

###### Deploy Client Credential Flow for Okta

By granting a few read-only permissions for
your Okta directory in advance, the Client Credential Flow option
for Okta in the Cloud Identity Engine allows you to use a service account
to log in to your Okta directory in the Cloud Identity Engine. Using
a service account is strongly recommended, as this is a more secure
method for directory access and does not require the account to
be associated with a specific user.

You must obtain a
new client ID and secret if you have an existing Okta directory
configuration. The client ID and secret for the Okta directory auth
code flow (the existing method) are not compatible with the API
service integration that the client credential flow method uses.

1. Download the Okta integration app from the [Okta Integration Network](https://www.okta.com/integrations/).
   1. In the Okta Administrator Portal, select Applications API Service Integrations.

      ![]()
   2. Click Add Integration.

      ![]()
   3. Search for Palo Alto Networks Cloud Identity
      Engine.

      ![]()
   4. Select the app integration you want to use based on whether you want to
      enable app data and click Next.

      To ensure that you select
      the correct app, either use Find in your
      browser (Ctrl+ F) to
      search for the app you want to use or hover over the app to display
      the full app name.

      - If you use application data in your security policy, select the
        Palo Alto Networks Cloud Identity Engine
        (Application-enabled) app. For more information
        on collecting application data, see Step 9 in [Configure Okta Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-okta-directory-in-the-cloud-identity-engine.html). 

        ![]()
      - If you do not use application data in your security policy,
        select the Palo Alto Networks Cloud Identity
        Engine app. 

        ![]()
2. Install and configure the API service integration.
3. Install & Authorize the API
   service integration.

   ![]()

   The
   Okta API service integration automatically configures the following
   required API scopes:

   - Users and groups—Read existing users’ profiles and credentials. Read
     about groups and their members. Read the signed-in user's profile and
     credentials.
   - Authorization servers—Read about authorization
     servers.
   - (Application-enabled app
     only)Apps—Read about apps.
   - Logs—Read about system log entries.
4. Click Copy to clipboard to copy the client secret and
   store it in a secure location, then click Done.

   ![]()

   The client secret displays only once,
   so make sure to copy it and store it securely before clicking
   Done.
5. Copy the Okta Domain and the Client
   ID and store them in a secure location.

   You must edit the domain by removing
   the https:// before pasting it.

   ![]()
6. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) your Cloud Identity
   Engine tenant.
7. Set up a Cloud Directory and
   select Okta.
8. Under Select Connection Flow,
   select Client Credential Flow.

   ![]()
9. Select Collect enterprise applications to display
   application data when you view directory data.

   If you select this option, you must
   use the Palo Alto Networks Cloud Identity Engine
   (Application-enabled) app to ensure the correct permissions.
   For more information, see step [1.d](#idce7fa5eb-95db-4fa5-8514-cddfbd1763ff_substep-nmj_2pk_jhc).

   ![]()
10. (Strata Logging Service only) Select whether you want to
    Collect authentication logs and forward to Strata Logging
    Service for retention and further analysis.

    ![]()
11. Paste the information you copied from the Okta management console into the
    fields as indicated in the following table.

    |

    Okta Managment Console Field | Cloud Identity Engine App Field |

    | --- | --- |

    |  |  |
    | --- | --- |
    |

    Okta Domain | Domain |

    |

    Client ID | Client ID |

    |

    Client Secret | Client Secret |

    ![]()
12. Click Test Connection to verify
    the Cloud Identity Engine can successfully communicate with your
    Okta directory.

    You must test the connection to submit the configuration.
13. (Optional) Customize the name of the directory that displays
    in the Cloud Identity Engine.

    If you want to use a custom name for this directory in
    the Cloud Identity Engine, enter the custom name as the Directory
    Name (Optional).
14. Submit your changes and verify
    your directory information when the Directories page
    displays.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

---

<a id="configure-google-directory"></a>

###### Configure Google Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-google-directory-in-the-cloud-identity-engine>*

Learn how to set up Google Directory in the Cloud Identity Engine for user identification
and Security policy enforcement.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

When you configure your Google Directory in the Cloud Identity Engine, the Cloud Identity Engine
can access your Google Directory information to identify users and enforce Security
policy.

1. If you haven’t already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity Engine.
2. Grant the necessary administrator rights in the Google
   Admin console for the Cloud Identity Engine.
   1. In the Google Admin console, select Admin roles.
   2. Select a role then click Privileges.
   3. Select the following privileges then Save your changes:

      - **Admin console privileges**
        - Organizational
          Units > Read
        - Users > Read
        - Groups
        - Services > Mobile Device Management > Manage Devices and Settings
        - Services > Chrome Management > Settings > Manage Chrome OS > Devices > Manage Chrome OS Devices
          (read-only)
        - Domain Settings
      - **Admin API privileges**
        - Organization Units > Read
        - Users > Read
        - Groups
        - Groups > Create
        - Groups > Read
        - Groups > Update
        - Groups > Delete
        - Billing Management > Billing Read
        - Domain Management

      ![]()
3. Log in to the Google Admin console and configure the
   Cloud Identity Engine app in the Google Admin console.
   1. Select SecurityAPI controls and click Manage
      Third-Party App Access.

      ![]()
   2. Select Configure new appOAuth App Name Or Client ID.

      ![]()
   3. Enter Palo Alto Networks Cloud Identity Engine Directory Sync and
      click Search.

      ![]()
   4. Select the Palo Alto Networks Cloud Identity Engine
      Directory Sync app.
   5. Select the OAuth Client ID option if it isn’t
      already selected then click Select.

      ![]()
   6. Select Trusted: Can access all Google services as
      the App access option then Configure the
      app.

      ![]()
4. Collect the necessary information from the Google Admin console to configure
   the Google Directory in the Cloud Identity Engine.
   1. Select AccountAccount Settings.
   2. Copy the Customer ID and store it in a secure
      location.

      ![]()
5. In the Cloud Identity Engine app, select DirectoriesAdd Directory.
6. Set Up a Cloud Directory and
   select Google.

   ![]()
7. Enter your Customer ID that you copied in step 4.

   ![]()
8. Sign in with Google by entering
   the Google Admin credentials for the account associated with the
   Customer ID.

   ![]()

   When the
   login is successful, Signed In displays.
9. Click Test Connection to verify
   your configuration.

   When the test is successful, Success displays.
10. (Optional) Customize the name the Cloud Identity Engine
    displays for your Google Directory.

    By default, the Cloud Identity Engine uses the default domain name.

    You can use up to 15 lowercase alphanumeric characters
    (including hyphens, periods, and underscores) for the directory name in the
    Cloud Identity Engine.
11. Submit the configuration.

    When you submit the configuration successfully, the Cloud Identity Engine displays the
    Directories page. 

    ![]()

    You can now use information from your Google Directory in the Cloud
    Identity Engine when you configure a user- or group-based security policy rule
    or with other Palo Alto Networks applications.

---

<a id="manage-your-google-directory"></a>

###### Manage Your Google Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-google-directory-in-the-cloud-identity-engine/reconnect-google-directory>*

Learn about managing your Google directory with CIE.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Managing your Google Directory integration ensures that the Cloud Identity Engine
retains valid access to the organizational units, users, and groups defined in your
Google Workspace. If the connection status indicates a failure or becomes inactive,
you must **reconnect** the directory by re-authenticating with your Google Admin
credentials and testing the connection to restore synchronization.

To stop synchronization and **remove** the directory entirely, you must perform a
two-step revocation process to ensure security. Once access is blocked at the
source, you can safely remove the Google Directory from the Cloud Identity Engine
application.

- [Reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-google-directory/reconnect-google-directory.html#id7a9e02ed-33d8-477c-9530-90c81c66c820)
- [Remove](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-google-directory/remove-google-directory.html#idb22406cd-a11f-49bd-a8da-49638bb80048)

###### Reconnect Google Directory

If the connection between the Cloud Identity
Engine and your Google Directory is inactive, reconnect the Google
Directory to the Cloud Identity Engine.

1. Log in to the hub and select the Cloud Identity
   Engine tenant that contains the Google Directory you want to reconnect.
2. Select Directories.
3. Select ActionsReconnect.

   ![]()
4. Log in to Google and Test Connection to
   confirm the Cloud Identity Engine can access your Google Directory.
5. (Optional) Customize Directory Name if you want
   to change the name that the Cloud Identity Engine displays for this directory in
   your tenant.

   You can use up to 15 lowercase alphanumeric
   characters (including hyphens, periods, and underscores) for the directory
   name in the Cloud Identity Engine. You don't need to change the name of the
   directory itself, only the name of the directory in the Cloud Identity
   Engine app. If your directory name contains more than 15 characters, you
   must change the directory name to contain a maximum of 15 characters.
6. Submit your configuration.

###### Remove Google Directory

If you no longer need to use Google Directory
with the Cloud Identity Engine app, revoke permissions for the Cloud
Identity Engine app and remove the Google Directory from the Cloud
Identity Engine app.

1. Revoke permissions for the Cloud Identity Engine
   app in the Google Admin Dashboard.
   1. Log in to the Google Admin Dashboard.
   2. Select SecurityAPI ControlsApp Access Control.
   3. Select the Cloud Identity Engine app and Change
      access to Blocked: Can’t access any Google
      service.

      ![]()
   4. Click Change to confirm your changes.
2. Remove the Google Directory from the Cloud Identity Engine app.
   1. Log in to the hub and select the Cloud Identity Engine
      app.
   2. Select Directories then select ActionsRemove.

      ![]()
   3. Click Yes to confirm removal
      of the directory.

---

<a id="manage-your-google-directory-1"></a>

###### Manage Your Google Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-google-directory-in-the-cloud-identity-engine/remove-google-directory>*

Learn about managing your Google directory with CIE.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Managing your Google Directory integration ensures that the Cloud Identity Engine
retains valid access to the organizational units, users, and groups defined in your
Google Workspace. If the connection status indicates a failure or becomes inactive,
you must **reconnect** the directory by re-authenticating with your Google Admin
credentials and testing the connection to restore synchronization.

To stop synchronization and **remove** the directory entirely, you must perform a
two-step revocation process to ensure security. Once access is blocked at the
source, you can safely remove the Google Directory from the Cloud Identity Engine
application.

- [Reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-google-directory/reconnect-google-directory.html#id7a9e02ed-33d8-477c-9530-90c81c66c820)
- [Remove](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-google-directory/remove-google-directory.html#idb22406cd-a11f-49bd-a8da-49638bb80048)

###### Reconnect Google Directory

If the connection between the Cloud Identity
Engine and your Google Directory is inactive, reconnect the Google
Directory to the Cloud Identity Engine.

1. Log in to the hub and select the Cloud Identity
   Engine tenant that contains the Google Directory you want to reconnect.
2. Select Directories.
3. Select ActionsReconnect.

   ![]()
4. Log in to Google and Test Connection to
   confirm the Cloud Identity Engine can access your Google Directory.
5. (Optional) Customize Directory Name if you want
   to change the name that the Cloud Identity Engine displays for this directory in
   your tenant.

   You can use up to 15 lowercase alphanumeric
   characters (including hyphens, periods, and underscores) for the directory
   name in the Cloud Identity Engine. You don't need to change the name of the
   directory itself, only the name of the directory in the Cloud Identity
   Engine app. If your directory name contains more than 15 characters, you
   must change the directory name to contain a maximum of 15 characters.
6. Submit your configuration.

###### Remove Google Directory

If you no longer need to use Google Directory
with the Cloud Identity Engine app, revoke permissions for the Cloud
Identity Engine app and remove the Google Directory from the Cloud
Identity Engine app.

1. Revoke permissions for the Cloud Identity Engine
   app in the Google Admin Dashboard.
   1. Log in to the Google Admin Dashboard.
   2. Select SecurityAPI ControlsApp Access Control.
   3. Select the Cloud Identity Engine app and Change
      access to Blocked: Can’t access any Google
      service.

      ![]()
   4. Click Change to confirm your changes.
2. Remove the Google Directory from the Cloud Identity Engine app.
   1. Log in to the hub and select the Cloud Identity Engine
      app.
   2. Select Directories then select ActionsRemove.

      ![]()
   3. Click Yes to confirm removal
      of the directory.

---

<a id="configure-scim-connector-for-the-cloud-identity-engine"></a>

###### Configure SCIM Connector for the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/configure-scim-connector-for-the-cloud-identity-engine>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

As part of the Cloud Identity Engine, Directory Sync connects to your directory to
obtain user and group information for user identification and enforcement for
group-based and user-based Security policy.

Configuring the System for Cross-Domain Identity Management ([SCIM](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/sync-scim)) protocol for Directory Sync in the
Cloud Identity Engine allows you to customize the attributes Directory Sync collects
from your directory. You can add or remove attributes in your directory portal to
customize which attributes you want to share with the Cloud Identity Engine for user
and group identification. When you configure the SCIM Connector, you choose an
authorization method — either a static bearer token or OIDC/OAuth 2.0 token-based
authentication — to control how your SCIM client authenticates with the Cloud
Identity Engine.

The SCIM gallery app does not support the userType
attribute.

Configuring your directory to use the SCIM Connector with the Cloud Identity Engine
requires completing all necessary steps in both the Cloud Identity Engine and in the
portal for your specific SCIM client. If you encounter any issues with the SCIM
Connector setup, learn how to [Troubleshoot Cloud Identity Engine Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5).

1. Complete any predeployment steps for your SCIM client:

   - [Microsoft Entra ID (formerly Azure
     Active Directory)](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_idd9a61289-0340-418b-a2e5-c6da85fc703d)
   - [PingFederate](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_id72911bc1-be92-4f42-81aa-30874588cfe4)
   - [Okta Directory](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task_hwm_zhf_3xb)
   - [Idira](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_cyberark-scim-connector)
   - [SASE 5G](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task-p2g_xk1_bhc)
2. Set up SCIM Connector in the Cloud Identity Engine app.
   1. Log in to the Cloud Identity Engine.
   2. Select Directory SyncDirectories, and then click Add New
      Directory.
   3. On the Set Up Directory page, select Cloud DirectorySet UpSCIM.

      ![]()
   4. Select a SCIM Client:

      - Entra ID
      - PingFederate
      - Okta
      - Idira
      - PingOne
      - SASE 5G
      - Others
3. (Specific SCIM clients) In the portals for the following SCIM clients,
   obtain the directory details required to configure the SCIM Connector:

   - [Configure Microsoft Entra ID for SCIM Connector](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_idd9a61289-0340-418b-a2e5-c6da85fc703d)
   - [Configure PingFederate for SCIM Connector](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_id72911bc1-be92-4f42-81aa-30874588cfe4)
   - [Configure Okta Directory for SCIM Connector](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task_hwm_zhf_3xb)
4. On the Configure Directory Sync for SCIM page, enter the directory details,
   obtain the Base URL, and specify the Authorization Method.
   1. For Directory ID, enter the specified value from
      your directory portal or create a unique ID (maximum 40 alphanumeric
      characters, including hyphens):

      - For Entra ID, use the Tenant ID.
      - For Ping, use the System ID.
      - For Okta, use the Directory Name.

        For Okta, Palo Alto Networks
        recommends using the Directory Name, but you can enter any
        name.
      - For Idira, enter IdiraSCIM or a similar
        ID.
      - For SASE 5G, use the Directory ID.

      ![]()
   2. For the Directory Name, enter the specified
      value from your directory portal or create a unique name (maximum 50
      lowercase alphanumeric characters including periods, hyphens, and
      underscores):

      - For Entra ID, use the Primary
        Domain.
      - For Ping, use the User.
      - For Okta, use the Okta Domain.
      - For Idira, enter idiradirectoryscim
        or a similar name.
      - For SASE 5G, use the Primary Domain
        Name.
   3. Copy the Base URL and save it in a secure
      location.

      You need this URL to configure provisioning settings in your
      directory portal.

      ![]()
   4. For Authorization Method, choose how your SCIM client authenticates
      with the Cloud Identity Engine:

      1. If you choose Static Bearer Token, Click
         Generate Token. Copy the bearer token
         and save it in a secure location.

         Before continuing to the next step and submitting the
         changes, make sure to save the token where you can easily
         retrieve it to enter in your SCIM client directory portal.
         If you submit the changes in the Cloud Identity Engine
         before you generate and save the token, you must generate a
         new token and enter the new token in the directory
         portal.
      2. If you choose OIDC Token, click the
         link to open Common Services identity
         and access management in a new tab. Create a service
         account, then download the CSV file containing your
         **Client ID** and **Client Secret** for use on the
         IDP connection side. Save both values in a secure
         location.

         Return to the Cloud Identity Engine and enter the **Service
         Account Name** for the service account you
         created.

         The associated service account
         requires Deployment Administrator
         access.

         Your SCIM client uses the Client ID
         and Client Secret to request short-lived access tokens from
         Common Services. The Cloud Identity Engine validates each
         token's signature, expiration, issuer, and audience claims
         on every API call and rejects expired tokens. Tokens are
         designed to refresh every 15 minutes, limiting the window of
         exposure if a token is ever compromised.

      ![]()
   5. Click Submit.

      You must Submit the
      configuration in the Cloud Identity Engine before continuing the
      configuration in the IdP. After you finish the IdP configuration,
      return to the Cloud Identity Engine and complete a [full sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) of the entire
      directory to complete the process.
5. Acknowledge the postconfiguration requirements.

   Select the check box, click OK, and then return to the
   portal for your SCIM client to complete the postconfiguration steps:

   - [Microsoft Entra ID (formerly Azure
     Active Directory)](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_idd9a61289-0340-418b-a2e5-c6da85fc703d)
   - [PingFederate](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_id72911bc1-be92-4f42-81aa-30874588cfe4)
   - [Okta Directory](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task_hwm_zhf_3xb)
   - [Idira](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_cyberark-scim-connector)
   - [SASE 5G](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task-p2g_xk1_bhc)

   ![]()

   After completing the steps in both the Cloud Identity Engine app and your
   directory portal, you can use the SCIM Connector to collect attributes from
   your directory.

   **Next Steps:**
   - Learn which [Cloud Identity Engine
     Attributes](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-attributes) the SCIM Collector collects.
   - [View directory data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html).
   - To extend the capabilities of the Cloud Identity Engine, [associate the Cloud
     Identity Engine with Palo Alto Networks apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) you use in
     your network.

<a id="id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_idd9a61289-0340-418b-a2e5-c6da85fc703d"></a>

<a id="idd9a61289-0340-418b-a2e5-c6da85fc703d_substep-qtb_rkc_n2c"></a>

###### Configure Microsoft Entra ID for SCIM Connector

Complete the required steps in the Microsoft Entra admin center to complete the
SCIM Connector configuration. For more information, refer to the [Microsoft Entra ID SCIM Connector](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-scim-connector-provisioning-tutorial)
documentation.

1. Add the Palo Alto Networks SCIM Connector app to your Microsoft Entra
   tenant, and then obtain the necessary information to configure SCIM for
   Directory Sync.

   Microsoft Entra ID SCIM provisioning requires that the group attribute
   displayName is unique. If more than one group
   uses the displayName attribute, the initial sync
   isn't successful and the data for the duplicate group names might only
   be partially retrievable. If you don't use the duplicate groups in
   Security policy, then you can proceed. If you use the duplicate group
   names in Security policy, you must resolve the issue by modifying the
   displayName attribute in Microsoft Entra ID
   to ensure that it’s unique.

   1. Log in to the [Microsoft Entra admin
      center](https://entra.microsoft.com/).
   2. Select Overview (if not already selected),
      copy the Tenant ID, and save it in a secure
      location.

      ![]()
   3. Copy the Primary domain and save it in a
      secure location.

      ![]()
   4. Select ApplicationsEnterprise applications, and then click New
      application.
   5. In the Microsoft Entra gallery, Search for
      Palo Alto Networks SCIM Connector.

      ![]()
   6. Select Palo Alto Networks SCIM Connector,
      enter a Name, and then
      Create the application.

      ![]()

      If you encounter an error when creating the application, refer to
      [Troubleshoot Cloud Identity Engine Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5).
   7. Return to the Cloud Identity Engine app to continue the SCIM
      Connector setup.

      You must complete the setup in the Cloud Identity Engine
      before you can successfully Test
      Connection in the Microsoft Entra admin
      center.
   8. After you submit the SCIM Connector configuration in the Cloud
      Identity Engine app, continue to the next step.
2. Configure Microsoft Entra ID to use SCIM Connector to connect to the Cloud
   Identity Engine.
   1. Log in to the [Microsoft Entra admin
      center](https://entra.microsoft.com/).
   2. Select ApplicationsEnterprise applications, and then select the Palo Alto Networks
      SCIM Connector application.
   3. Select Provisioning, and then click
      Get Started.

      ![]()
   4. Set the Provisioning Mode to
      Automatic.

      ![]()
   5. In the Admin Credentials section, enter the information from steps
      [4.c](#configure-scim-connector-for-the-cloud-identity-engine) and [4.c](#configure-scim-connector-for-the-cloud-identity-engine) in the fields as
      indicated in the following table:

      |

      Copy from Cloud Identity Engine | Enter in Microsoft Entra admin center |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Base URL | Tenant URL |

      |

      Authorization Method Bearer token | Secret Token |

      ![]()
   6. Save your changes.

      ![]()
   7. (Optional but recommended) Click Test
      Connection to confirm that Microsoft Entra ID can
      communicate with the Cloud Identity Engine app.

      You must complete the setup in the Cloud Identity Engine
      before you can successfully Test
      Connection in the Microsoft Entra admin
      center.

      ![]()
3. Manage the users, groups, and attributes that Microsoft Entra ID provisions
   to the Cloud Identity Engine app.

   If you choose to [sync only specific
   groups](#idd9a61289-0340-418b-a2e5-c6da85fc703d_substep-qtb_rkc_n2c) and those groups contain subgroups, add the parent
   group first, then add any child groups. If you do not manually add the
   child groups of any parent groups, the Cloud Identity Engine syncs only
   the parent group. You do not need to manually add users as the Cloud
   Identity Engine sync users in groups, just any child groups of parent
   groups where you want to sync both groups.

   1. In the Microsoft Entra admin center, select ProvisioningEdit Provisioning.
   2. Select Mappings, and then select either
      Provision Microsoft Entra ID Groups or
      Provision Microsoft Entra ID Users.

      For optimal performance, Palo Alto
      Networks strongly recommends provisioning only the groups that
      you want to use the SCIM Connector. If you're using Prisma®
      Access with the Cloud Identity Engine, make sure that you
      provision any groups that you use in your Security policy to
      ensure it applies your Security policy correctly.

      ![]()
   3. Delete any attributes you do not want to
      provide to the Cloud Identity Engine app.

      ![]()
   4. (Optional) Click Add New Mapping to
      create a new attribute mapping.

      ![]()
   5. (Optional) In the Settings section, set
      Scope to Sync all users and
      groups.

      By default, the Cloud Identity Engine only synchronizes the users
      and groups you assign to this app (Sync only assigned
      users and groups) in the Microsoft Entra admin
      center.

      ![]()
   6. In the Settings section, set the Provisioning
      Status to On.

      This enables the Microsoft Entra provisioning service for Palo
      Alto Networks SCIM Connector.
   7. Save your changes.
4. Allow Microsoft Entra ID to provide the information to the Cloud Identity
   Engine, and verify that the Cloud Identity Engine uses SCIM to obtain the
   Microsoft Entra ID information.
   1. In the Microsoft Entra admin center, verify you’ve completed all
      the provisioning steps in the [Microsoft Entra ID SCIM
      Connector](https://learn.microsoft.com/en-us/entra/identity/saas-apps/palo-alto-networks-scim-connector-provisioning-tutorial) documentation.
   2. Select the name of the app that you configured in the first step,
      and then select ManageProvisioningStart Provisioning to begin providing attributes to the Cloud Identity
      Engine.

      ![]()
   3. Wait until the sync is complete (Initial cycle
      completed), and then View provisioning
      details.

      ![]()
   4. Verify that the synchronization was successful by confirming the
      timestamps (Completed and Steady
      state achieved) and verifying that the number of
      Users and Groups
      displays.

      ![]()

      If the number of users and groups does not display, refer to
      [Troubleshoot Cloud Identity Engine Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5).
   5. In the Cloud Identity Engine app, verify that the SCIM
      Change Timestamp for your Entra ID SCIM directory
      populates on the Directories page.
   6. Select ActionsFull Sync to complete a full synchronization of Microsoft Entra
      ID users and groups with Directory Sync for the Cloud Identity
      Engine.

      You must successfully complete a full sync in the Cloud
      Identity Engine app to complete the SCIM Connector setup.

<a id="id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_id72911bc1-be92-4f42-81aa-30874588cfe4"></a>

###### Configure PingFederate for SCIM Connector

Complete the following steps to configure the Cloud Identity Engine to use the
SCIM Connector to connect to your PingFederate server. Be sure to complete all
the steps in the [PingFederate SCIM Connector](https://docs.pingidentity.com/bundle/pingfederate-scim-connector/page/igd1563995051118.html)
documentation as well.

1. Set up the directory for SCIM Connector.
   1. Log in to the PingFederate portal and select Data
      Stores then click Add New Data
      Store.
   2. Enter a Data Store Name and select
      Directory (LDAP) as the
      Type.
   3. Enter the Hostname(s) (including the port
      number).
   4. Enter a valid email address as the User
      DN.
   5. Click Test Connection to verify the
      connection is successful.

      If the connection test isn't successful, verify that the
      hostname and email address are valid. Some directories, such as
      PingDirectory, format the User DN as
      cn=administrator. In this case,
      select Use LDAPS and use a different port
      number, such as 1636, instead of the default port number of
      389.

      ![]()
   6. Copy and edit the System ID then paste the
      edited value in the Cloud Identity Engine app as the
      Directory ID.

      You must edit the System ID to remove
      the LDAP- that precedes the
      Directory ID value before entering
      the value as the Directory ID in the
      Cloud Identity Engine app.

      ![]()
   7. Copy and edit the User value and edit the
      edited value in the Cloud Identity Engine app as the
      Directory Name.

      For the Directory Name, use the domain
      name that follows the username in the
      User column (for the example below,
      the Directory Name is the value after
      Administrator@).

      ![]()
2. Provision the SCIM connection.
   1. Select SP ConnectionsCreate Connection.
   2. Select Do not use a template for this
      connection.
   3. Select Outbound provisioning.
   4. Select SCIM Connector.

      If the SCIM Connector option isn’t available, confirm that you
      completed all substeps in the previous step correctly.

      ![]()
   5. Select General Info and enter a
      Partner’s Entity ID (Connection ID) and a
      Connection Name.
   6. (Optional but recommended) To decrease the amount of time necessary
      for the initial sync, select Outbound ProvisioningConfigure ProvisioningManage ChannelsChannel ConfigurationChannel Info and increase the value for Max
      Threads.

      The range is recommended range is 1–5; for optimal sync time,
      Palo Alto Networks recommends 5 as the value for Max
      Threads.

      ![]()
3. Specify the information from the Cloud Identity Engine for the SCIM
   connection provisioning.
   1. Select Outbound ProvisioningConfigure Provisioning.
   2. Select the SP Connections Target tab and
      enter the Base URL that you copied from the
      Cloud Identity Engine.

      ![]()
   3. Select ApplicationsSP ConnectionsSP ConnectionConfigure ChannelsManage Channels.
   4. Select OAuth 2 Bearer Token as the
      Authentication Method and enter the
      Bearer Token that you copied from the
      Cloud Identity Engine as the Access
      Token.

      ![]()
   5. Select Common Name as the Group
      Name Source.

      ![]()
   6. Select Use patch for group updates.

      ![]()
4. Configure the channels for the SCIM connection.
   1. Select Configure Channels and
      Create a channel.
   2. Enter a Name for the channel and select the
      directory you want to configure in the Cloud Identity Engine as the
      Active Data Store.
   3. Select Source Location and enter the
      Base DN for your directory.
   4. Enter the Group DN for the source of the
      user and group mappings or create a filter that specifies which
      entries to use. For example, Group
      DN:CN=Chicago,OU=Illinois,DC=example,DC=com syncs
      all users and groups in the Chicago group.
   5. If you use a Group DN and your directory contains nested groups,
      select Nested Search.

      Retention of nested group hierarchies from PingFederate
      servers through the SCIM Connector isn’t available. If your
      directory contains nested groups and you want to sync all of the
      child users and groups, you must select the method you want to
      use to ensure the Cloud Identity Engine correctly collects all
      users and groups in the parent group.
      - Add the parent group as a member of a different group
        and use that container group as the Group DN. For
        example, configure the parent group in a directory with
        the name root in an OU with the
        name location and use the value
        CN=root,OU=location,DC=paloaltonetworks,DC=com
        for the Group DN.
      - Add a filter that includes all members of the parent
        group (for example,
        (objectClass=user),(objectClass=group)
        includes all users and groups in the Base DN
        DC=paloaltonetworks,DC=com).
   6. Select Attribute Mapping and
      Edit the userName\*
      to userPrincipalName.

      ![]()
   7. Save the connection and continue the
      configuration in the Cloud Identity Engine.
5. Complete the postdeployment steps to configure the PingFederate server for
   the SCIM Connector.
   1. Verify that you’ve completed all of the [provisioning steps](https://docs.pingidentity.com/bundle/pingfederate-scim-connector/page/igd1563995051118.html).
   2. In the PingFederate Portal, either commit a directory change or
      enter the following command: pingfederate/bin/provmgr.sh
      --reset-all -c [channel number] command.

      To determine the channel number, use the
      ./provmgr.sh --show-channels
      command.
   3. In the Cloud Identity Engine, verify the app populates the
      SCIM Change Timestamp then complete a
      full sync (ActionsFull Sync).

<a id="id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task_hwm_zhf_3xb"></a>

###### Configure Okta Directory for SCIM Connector

You must also complete the required steps in the Okta Administrator Dashboard to
complete the SCIM Connector configuration. For more information, refer to the
documentation for the [Okta Directory](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SCIM.htm).

The SCIM Connector for Okta directory supports the following capabilities:

- Create users
- Update user attributes
- Deactivate users
- Import users
- Import groups
- Sync password
- Group push

1. Log in to your Okta Administrator Dashboard and add the integration using
   the [Okta Integration Network](https://www.okta.com/integrations/).
   1. Log in to the Okta Administrator Dashboard, select
      Applications, and click Browse
      App Catalog.

      ![]()
   2. Enter Palo Alto Networks SCIM as the search
      query.

      ![]()
   3. Select the app and click Add Integration.

      ![]()
   4. Optionally change any settings, such as the Application
      Label, then click Done.

      ![]()
   5. [Copy](https://developer.okta.com/docs/guides/find-your-domain/findorg/) your Okta domain
      name.
2. Configure the Okta integration to communicate with the Cloud Identity
   Engine.
   1. Select Provisioning.

      ![]()
   2. Click Configure API Integration.

      ![]()
   3. Select Enable API integration.

      ![]()
   4. Enter the URL you copied in step [4.c](#configure-scim-connector-for-the-cloud-identity-engine) as the
      Base URL.

      ![]()
   5. Enter the token you copied in step [4.d](#configure-scim-connector-for-the-cloud-identity-engine) as the
      API Token.

      ![]()
   6. Click Test API Credentials to verify the
      Okta Directory can successfully communicate with the Palo Alto
      Networks SCIM integration then click
      Save.

      ![]()

      If the test is not successful, verify
      that you successfully submitted your configuration in the Cloud
      Identity Engine app in step [4.e](#configure-scim-connector-for-the-cloud-identity-engine).
3. Assign the Okta integration to the users you want to include in your
   Security policy.
   1. Edit the settings to assign
      Provisioning to App.

      ![]()
   2. Enable all the options and
      Save your changes.

      ![]()
   3. Select the Push Groups tab then click the
      Find Groups button to Find
      groups by name.

      ![]()
   4. Type the name of a group to Push groups by
      name.

      ![]()
   5. Select the group and Save your
      changes.

      ![]()
4. Verify the configuration.
   1. In the Cloud Identity Engine app, select
      Directories and verify that the timestamp
      displays in the SCIM Change Timestamp column
      for the Okta SCIM directory.

      ![]()
   2. Select Actions Full Sync for the directory.

      The configuration isn’t complete until
      you’ve successfully completed a [full sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) for the
      entire directory.

      ![]()

###### Configure a Custom Okta App Integration for SCIM Connector

Palo Alto Networks strongly recommends using the Okta gallery app to [Configure Okta Directory for SCIM Connector](#id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task_hwm_zhf_3xb). If you
want to use a custom Okta app integration, complete the following steps.

1. Log in to your Okta Administrator Dashboard and [Create an app integration](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm).
   1. Select SAML 2.0 as the Sign-in
      method and click Next.

      ![]()
   2. Enter a unique App Name and optionally enter
      any other information (such as an App Logo or
      App Visibility) then click
      Next.

      ![]()
   3. Enter the Single-sign on URL where you want
      to redirect users to sign in and the Audience URI (SP
      Entity ID) then click Next.

      ![]()
   4. Select the option that best reflects your use of the SCIM Connector
      app integration and click Finish.

      ![]()
2. Configure the Okta SCIM Connector app integration.
   1. Select General (if it is not already
      selected) and Edit the App
      Settings.

      ![]()
   2. Select SCIM as the
      Provisioning method and
      Save your changes.

      ![]()
3. Configure provisioning for the Okta SCIM Connector app integration.
   1. Select Provisioning and
      Edit the SCIM Connection settings.

      ![]()
   2. Enter the Base URL you copied from the Cloud
      Identity Engine app in step [4.c](#configure-scim-connector-for-the-cloud-identity-engine) as the
      SCIM connector base URL.

      ![]()
   3. Enter userName as the Unique
      identifier field for users.

      ![]()
   4. Select the Supported provisioning actions
      you want to use to allow users to authenticate.

      ![]()
   5. Select HTTP Header as the
      Authentication Mode.

      ![]()
   6. Enter the Bearer Token you copied from the
      Cloud Identity Engine app in step [4.d](#configure-scim-connector-for-the-cloud-identity-engine) and
      Save your changes.

      ![]()
   7. Select Provisioning and
      Edit the settings.

      ![]()
   8. Select at least one of the options for Provisioning to
      App and Save your
      changes.

      ![]()
4. Assign the users and groups that you want to use the Okta SCIM Connector
   app integration.
   1. Select AssignmentsAssignAssign to People to assign the users you want to use Okta SCIM.

      ![]()
   2. Select the users for whom you want to Assign
      this app.

      ![]()
   3. Review and edit the information as needed then click
      Save and Go Back.

      ![]()
   4. Verify the users you added display on the
      Assignments tab.

      ![]()
   5. Select Push Groups then Find
      groups by name to assign groups to this app.

      ![]()
   6. Select the group you want to assign to this app then click
      Save and add another. Repeat as needed
      until all the groups you want to assign to this app have been
      selected then click Save.

      ![]()
5. Verify the configuration.
   1. Select Reports System Log.

      ![]()
   2. Verify that log results display to confirm that the SCIM Connector
      can successfully communicate with your directory. If no results
      populate, the SCIM Connector cannot communicate with your directory;
      verify the configuration and make any needed changes, then check the
      log results again.

      ![]()

      Verify that this step is complete before
      continuing to the next step. Until the log results display in
      the Okta Administrator Dashboard, a full sync cannot
      successfully complete for the directory in the Cloud Identity
      Engine app.
   3. In the Cloud Identity Engine app, select
      Directories and verify that the timestamp
      displays in the SCIM Change Timestamp column
      for the Okta SCIM directory.

      ![]()
   4. Select Actions Full Sync for the directory.

      The configuration is not complete until
      you have successfully completed a [full sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) for the
      entire directory.

      ![]()

<a id="id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_task-p2g_xk1_bhc"></a>

<a id="task-p2g_xk1_bhc_substep-krd_thv_dhc"></a>

<a id="task-p2g_xk1_bhc_substep-qpq_b3v_dhc"></a>

###### Configure SASE 5G for SCIM Connector

To configure a [Prisma SASE 5G](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-sase-5g) to share directory
attributes with the Cloud Identity Engine using the SCIM connector, complete the
following steps.

1. Create the Prisma SASE 5G configuration.

   For more information, refer to step 9 in the [Prisma SASE 5G documentation](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-sase-5g).

   1. Select DirectoriesAdd New DirectoryCloud DirectorySet UpSCIM.
   2. Select SASE 5G as the Client
      Type.
   3. Enter the Directory ID of the SASE 5G
      directory.
   4. Enter the primary domain name of the SASE 5G directory as the
      Directory Name.
   5. Copy the Base URL and
      save it in a secure location.
   6. For the Authorization Method, click
      Generate Token.
   7. Copy the Bearer Token
      and store it in a secure location.
   8. Submit the configuration.
2. Create the SCIM connector configuration for Prisma SASE 5G.
   1. On the Strata Multitenant Cloud Manager, select Manage5G Integrated SASEService ProviderTenantNameCIE Management. (where TenantName is the name
      of your tenant).
   2. Enter the CIE Directory Name.

      The directory name must match the
      primary domain name from step [1.d](#task-p2g_xk1_bhc_substep-krd_thv_dhc).
   3. Enter the bearer token from step [1.g](#task-p2g_xk1_bhc_substep-qpq_b3v_dhc) as the CIE Token.
   4. Complete the remaining steps to add mobile user identities and
      identity groups as described in the [Prisma SASE 5G
      documentation](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-sase-5g).
   5. Commit the changes.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a Next-Generation Firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your
  security posture.

<a id="id32a816f0-0f84-4d6a-8300-ff5e9e3646a9_cyberark-scim-connector"></a>

###### Configure Idira for SCIM Connector

Enable SCIM provisioning and map Idira Identity portal roles to groups or roles
defined in the Cloud Identity Engine.

1. Log in to the Idira Identity Administration portal.
2. Select Apps & WidgetsWeb Apps, and then click Add Web Apps.
3. Search for Palo Alto Networks
   CIE.
4. Add the application, and then click
   Yes to confirm.
5. Configure general provisioning settings.
   1. On the sidebar, click Provisioning, and then
      Enable provisioning for this
      application.
   2. Click Yes to acknowledge the SCIM
      provisioning prompt.
   3. Select a provisioning mode:

      - Preview Mode (changes will not be
        committed)—Use this mode to test
        application provisioning or configuration changes. The
        identity platform performs a test run to show you the
        changes it would make but does not save the changes.
      - Live Mode—Use this to apply
        application provisioning to your production environment.
        The identity platform performs a provisioning run and
        saves the changes to both the identity platform and the
        application’s account information.
   4. For SCIM Service URL, enter the Base URL
      from the Cloud Identity Engine.
   5. For Authorization Type, select
      Authorization Header.
   6. For Header Type, select Bearer
      Token, and then enter the Bearer Token from the
      Cloud Identity Engine.
   7. To test the connection and save the provisioning details, click
      Verify.

      After Idira verifies the connection to the SCIM Connector,
      additional settings display.
6. Define how Idira Identity handles automatic provisioning of accounts.

   Idira identifies duplicate accounts by matching attributes in the source
   directory to unique Cloud Identity Engine user attributes. This is
   typically the user's email address or the Active Directory
   userPrincipalName.

   Review the provisioning script for the Cloud Identity Engine to see the
   fields that Idira Identity uses to match user accounts.

   1. Configure Sync Options:

      - Sync (overwrite) users to target application
        when existing users are found with the same
        principal name—Updates account
        information in the Cloud Identity Engine. This includes
        removing data if the target account has a value for a
        user attribute that is not available from Idira
        Identity.
      - Do not sync (no overwrite) users to target
        application when existing users are found with the
        same principal name—Keeps the target
        user account as is; Idira Identity skips and does not
        update duplicate user accounts in the Cloud Identity
        Engine.
      - Do not de-provision (deactivate or delete)
        users in target application when the users are
        removed from mapped role—The user's
        account in the Cloud Identity Engine is not
        de-provisioned when a role membership change that would
        trigger a de-provisioning event occurs.
      - Sync groups from Active Directory to target
        application (this option overrides any destination
        group selection in Role
        Mappings)—Provisions groups and group
        members from the local directory to the Cloud Identity
        Engine. You may filter AD groups through the
        provisioning script using the reject function.
      - Sync roles from Idira Identity to target
        application—Provisions roles from Idira
        Identity to the Cloud Identity Engine. You can filter
        roles using the [Role
        Filter](https://docs.cyberark.com/identity/latest/en/content/applications/appsovw/scim-provisioning.htm?tocpath=Administrator%7CManage%20identity%20lifecycles%7COutbound%20provisioning%7C_____5#EnableIdiraIdentityrolefiltering).
   2. (Optional) Configure User Deprovisioning
      Options:

      - Disable user—Deactivates the user
        account in the Cloud Identity Engine but retains the account
        data.
      - Delete user—Deletes the user account
        and all its data in the Cloud Identity Engine.
      - Deprovision (deactivate or delete) users in this
        application when they are disabled in the source
        directory—If a user account is disabled in
        Idira Identity, Idira performs the specified deprovisioning
        action in the Cloud Identity Engine
7. (Optional) Configure role mappings to define the users Idira
   provisions to the Cloud Identity Engine.

   Idira Identity runs a synchronization automatically whenever you
   update the provisioning role mapping. You can also run a preview
   synchronization or a real synchronization, if desired.

   To provision Active Directory user group membership, see [Provision Active Directory Groups
   with SCIM](https://docs.cyberark.com/identity/latest/en/content/applications/appsovw/scim-provisioning.htm?tocpath=Administrator%7CManage%20identity%20lifecycles%7COutbound%20provisioning%7C_____5#ProvisionActiveDirectoryGroupswithSCIM).

   To learn the different ways that Idira Identity synchronizes provisioned
   accounts, see [Synchronize provisioned
   accounts](https://docs.cyberark.com/identity/latest/en/content/applications/appsovw/provsynchoptions.htm).

   1. In the Role Mappings section, click
      Add.
   2. Select a Role.
   3. Click Add, and then select a
      Destination Group or enter a new group
      name.

      A Destination Group named for the selected Idira role
      automatically populates in the list of groups available from the
      drop-down.

      - If you select that Destination Group, a group with that
        name is created in the Cloud Identity Engine.
      - If the Destination Group already exists in the Cloud
        Identity Engine, provisioned users that are members of
        the selected role are added as members of the existing
        Destination Group.
      - If you enter a new group name, the newly created
        Destination Group is also created in the Cloud Identity
        Engine.
   4. To save the role mappings and return to the Provisioning settings,
      click Done.
   5. Save the provisioning details.
8. Synchronize provisioned accounts.
   1. Select SettingsUsersOutbound Provisioning.
   2. (Optional) Enter an Email address for report
      delivery.
   3. (Optional) Configure Reporting
      Options:

      A report is always sent if an error
      occurs during synchronization.

      - Send report on full sync—Select
        this option to receive a synchronization report even if
        no errors occur. If you clear this option, you receive a
        report only if errors occur.
      - Send report on individual
        sync—Select this option to receive a
        separate report for each synchronized user. Otherwise,
        Idira sends you a consolidated user report.
      - Include debug trace in the
        report—Select this option to receive more
        detailed information in your report. The additional
        details are intended for debugging purposes only.
   4. In the Synchronization section, for Provisioning Enabled
      Applications, select Palo Alto Networks
      CIE, and then click Start
      Sync.

      A message prompts you for confirmation.
   5. (Optional) To re-synchronize all objects instead of only
      changed objects, select bypass caching and re-sync all
      objects.

      Select this option if many users or objects such as groups,
      contacts, or resources were changed in the Cloud Identity Engine
      that manually re-syncing every object would be difficult.
      Bypassing caching and re-syncing all objects increases
      synchronization time.
   6. Click Yes to continue.

      A message informs you that the synchronization has begun.
   7. Click OK.

---

<a id="configure-a-cie-directory"></a>

##### Configure a CIE Directory

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cie-directory>*

Learn how to configure a local directory for the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

To configure a local directory for the Cloud Identity Engine, use the CIE Directory
by completing the following steps.

The following security measures apply for CIE Directory users:

- Users must change their passwords after their first login.
- If a user fails to log in successfully after five attempts, the user's
  account is locked for five minutes or until it's unlocked by an
  administrator. The time that the account is locked is based on the number of
  unsuccessful attempts; for example, after 20 failed attempts, the account is
  locked for 20 minutes or until it's unlocked by an administrator.
- If a user fails to log in successfully after 24 attempts, the user's account
  is disabled until it's enabled by an administrator.

1. Add the CIE Directory in the Cloud Identity Engine.
   1. Select Directory Add a new directory.
   2. Set Up a CIE
      Directory.

      ![]()
   3. Enter a unique Directory Name.

      The Cloud Identity Engine supports
      lowercase alphabetic characters, numeric characters, hyphens,
      periods, and underscores for the directory name. If you're using a
      NetBIOS name, the directory name must contain fewer than 16
      characters.

      ![]()
   4. Click Submit to create the CIE Directory.

      Creating the directory takes some time, so
      wait until the Directories page displays before proceeding.
2. Add users to the CIE Directory.
   1. On the Directories page, click Add
      User.

      The Cloud Identity Engine supports up to 200
      users for the CIE Directory.

      ![]()
   2. Enter the user's First Name, Last
      Name, and Email.

      ![]()
   3. Enter a Password for the user or click
      Generate Password to generate a password.

      ![]()

      You can also optionally copy (

      ![]()

      ) the
      password.

      You must enter a password for the
      user before you can add the user to the directory.
   4. Click Create to add the user or users.

      If you have a .CSV file that contains the user information, click
      Bulk Import to import the .CSV file.
3. Manage the directory and its users as necessary.

   As your directory needs change, manage and update the directory information.
   - To update user information, select Edit in the
     Actions column. Update the information for a
     user then click Update to confirm. 

     ![]()
   - To require users to reset their passwords on their next login, select
     Force Password Reset from the
     Actions column. 

     ![]()
   - To unlock a user's account, click the Unlock
     button in the Actions column. 

     ![]()
   - If you no longer need to keep a user's information, select the user (or
     users) and click Delete and confirm the deletion.
     You can also select Delete User in the
     Actions column. 

     ![]()
   - To ensure you have the latest directory information, select the
     Directories page and
     Refresh the specified directory from the
     Actions column. 

     ![]()
   - If you no longer need a CIE Directory, select the
     Directories page,
     Remove the directory from the
     Actions column, and click
     Yes to confirm the deletion. 

     ![]()

   **Next Steps:**
   - Learn how to [Authenticate Users with the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine.html).
   - Find out how to [View Directory Data](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-directory-data.html).

---

<a id="manage-the-cloud-identity-engine-app"></a>

#### Manage the Cloud Identity Engine App

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine>*

Learn how to manage your Cloud Identity Engine tenants
and how to collect customized directory attributes.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

After you have configured the Cloud Identity Engine, you can add, rename, or delete tenants and
collect any custom attributes in your directory, as well as view a list of the default
attribute formats. You can also view the comprehensive information that the Cloud
Identity Engine collects.

To ensure consistent security policy enforcement, you can configure segments for granular
data sharing across your network You can also configure context-based groups that
update membership automatically based on criteria that you select.

If you use [Device-ID](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-id/device-id-overview) and third-party devices to identify
IoT devices on your network, you can use the Cloud Identity Engine to share device
mappings with your Prisma Access Nodes.

If you use [dynamic address groups for your tag-based security
policy](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/monitor-changes-in-the-virtual-environment/use-dynamic-address-groups-in-policy), you can use the Cloud Identity Engine to collect and redistribute
mappings across your network to help ensure consistent policy enforcement.

---

<a id="cloud-identity-engine-tenants"></a>

##### Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

When you activate the Cloud Identity Engine, it automatically creates a [tenant](#). A
tenant acts as a secure container for your directory information. While a default tenant
is created automatically when you first activate the service, many organizations find it
necessary to create additional tenants. This is often done to keep data separate for
different geographic regions or to isolate information between distinct business units,
ensuring that sensitive user data remains within specific boundaries to meet data
residency laws and internal compliance requirements.

Managing your tenants includes:

- **Creating Tenants:** You can add new tenants to support operations in
  different geographic regions or to isolate data between distinct
  departments.
- **Viewing Tenants:** The management interface provides a consolidated list
  where you can see all your active tenants and their specific configuration
  details at a glance.
- **Renaming Tenants:** You can update the display name of a tenant to ensure
  it accurately reflects its current purpose or location as your organization
  evolves.
- **Synchronizing Tenants:** You can manually trigger an immediate update to
  ensure that the user information in your tenant matches the latest changes in
  your source directory.
- **Deleting Tenants:** If a specific tenant is no longer needed and is not
  being used by other applications, you can permanently remove it from the
  system.
- **Deleting Domains or Directories:** You can remove specific domain
  connections or entire directories from a tenant without deleting the tenant
  itself.

You must have an [App Administrator role](https://docs.paloaltonetworks.com/cortex/cortex-hub/cortex-hub-getting-started/manage-app-roles/assign-app-admin-role.html) to create,
rename, or delete tenants.

---

<a id="create-cloud-identity-engine-tenants"></a>

###### Create Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/create-cloud-identity-engine-instances>*

Learn how to use tenants to isolate directory data or
to allow apps to access different directory data.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you want to isolate your directory data,
or allow different Palo Alto Networks cloud applications and services
to access different sets of directory data, you can create multiple
Cloud Identity Engine tenants in the hub.

1. Log in to the hub.
2. Select Tenant Management.

   ![]()
3. Select Add Tenant.

   ![]()
4. Enter a Name for the tenant and
   select a Business Vertical.

   ![]()
5. (Optional) To enter custom support contact information,
   select Use custom and enter the contact information.

   You can enter up to 255 alphanumeric characters.
6. Click Add Tenant.

   The Hub lists new tenants at the bottom of the list of
   tenants.

   ![]()

---

<a id="view-cloud-identity-engine-tenants"></a>

###### View Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/view-cloud-identity-engine-instances>*

Learn how to view your Cloud Identity Engine tenants
in the hub.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Tenants display in the order in which they
were created, with the most recently created tenant at the bottom
of the list.

1. Log in to the hub.
2. Select Tenant Management.

   ![]()
3. By default, the list of tenants displays as collapsed;
   click the arrow to display the full tenant list.

   ![]()
4. Select the tenant you want to view.

   ![]()

---

<a id="synchronize-cloud-identity-engine-tenants"></a>

###### Synchronize Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances>*

Learn how to synchronize changes to your directory attributes
in your Cloud Identity Engine tenants.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

There are two ways that the Cloud Identity
Engine synchronizes changes to your directory attributes:

- A
  full sync, which is a complete sync of the entire directory.
- A sync of just the changes to the directory since the last successful
  sync, which takes much less time to complete (Not supported
  with Google Directory).

By default, the Cloud Identity
Engine app synchronizes the directory attributes:

- Every five minutes with the changes since the last successful sync (Not supported with
  Google Directory) unless a sync is already in progress.
- Weekly with a complete sync of all configured directories (Not
  supported with Google Directory).
- Based on the schedule you select (Google Directory only).

The time to synchronize data depends significantly on the
number of changes, the size of the directory, and the amount of group nesting.

To
refresh your Cloud Identity Engine tenant with any recent changes
in your directory before that time, you can select how you want
to synchronize changes to the attributes for your configured domains.

<a id="idfaa1ba0a-aa4f-4803-be87-4f23783b8c9b_id5306eb05-1718-4e8f-9062-53d4ac69bdae"></a>

###### Synchronize All Attributes

Synchronizing all attributes (a full sync) is
recommended if you are experiencing issues or lose connectivity.

For
on-premises directories, all agents and domains for the tenant must
be active for the sync to complete successfully.

1. Log in to the hub and select the Cloud
   Identity Engine app.
2. Select the directory you want to synchronize, then select Directories.
3. Select ActionsFull Sync to initialize the
   synchronization for the directory type you want to synchronize instantly.

   ![]()

   For
   an on-premises Active Directory, click Full Sync. 

   ![]()

   The synchronization starts immediately and a confirmation
   message (Sync started) displays. The
   sync may take some time to complete, so make sure you click Full Sync only
   once. If a synchronization is currently in progress when you try
   to synchronize, a warning message (Sync in progress)
   displays at the top of the screen.

   After completing a full sync, you must wait at
   least 90 seconds before initiating another full sync.
4. To confirm the synchronization is complete, verify the Sync
   Status is Success.

###### Synchronize Directory Changes

You can sync just the changes to your directory, which is much faster than a full sync of your
directory. By default, the Cloud Identity Engine syncs changes for most
attributes every five minutes unless a sync is already in progress.

The Sync Status on the Directories page may
incorrectly indicate Success while an incremental sync is still in progress.
The synchronization automatically captures any changes made in the directory
but it is not possible to initiate another sync while a sync is currently in
progress.

For Azure Active Directory (Azure AD) and Okta, the Cloud Identity Engine syncs
attributes for users and groups every five minutes; for Azure AD, a sync for
devices occurs daily if the previous device sync required less than 24 hours to
complete. If completing the device sync required more than 24 hours, the next
sync occurs at the interval of the duration for the previous device sync (for
example, if the previous device sync required 26 hours, then the next sync would
occur 26 hours from the previous successful sync).

The Sync Changes option is not available for Google
Directory.

1. If you have not already done so, [configure a directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type.html#id0c385168-da26-44ec-bba8-149bbb64092f).
2. After making changes to your directory, select ActionsSync Changes to
   sync the changes for your directory.

   ![]()

   For
   an on-premises Active Directory, click Sync Changes. 

   ![]()

   The
   sync may take some time to complete, so make sure you click Sync Changes only
   once. We recommend a full sync of your directory if you lose connectivity
   or are experiencing issues. To sync the entire directory, [Synchronize All Attributes](#idfaa1ba0a-aa4f-4803-be87-4f23783b8c9b_id5306eb05-1718-4e8f-9062-53d4ac69bdae) in a full sync. If a full
   sync is in progress, you cannot sync changes. After a full sync
   completes in the Cloud Identity Engine app, the firewall must also
   complete a full sync.

###### Set Synchronization Interval

This sync option is available for Google
Directory only.

1. Log in to the hub and select the Cloud
   Identity Engine app.
2. Select the tenant you want to synchronize, then select Directories.
3. Click Sync Every: for the directory
   type interval that you want to change and select the interval.
   - 6 Hours
   - 12 Hours
   - 24 Hours (Default)

   ![]()

   After
   you select an interval, a confirmation message displays at the top
   of the screen.

###### Synchronize CDUG Changes

This sync option is available for Google
Directory only.

1. Log in to the hub and select the Cloud
   Identity Engine app.
2. Select the tenant you want to synchronize, then select Directories.
3. Sync CDUG Changes to initialize the synchronization
   of the cloud dynamic user group information.

   The synchronization starts immediately and a confirmation message
   (Sync started) displays. If a
   synchronization is currently in progress when you try to synchronize, a
   warning message (Sync in progress) displays
   at the top of the screen.

   ![]()
4. To confirm the synchronization is complete, verify the Sync
   Status is Success.

---

<a id="rename-cloud-identity-engine-tenants"></a>

###### Rename Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/rename-cloud-identity-engine-instances>*

Learn how to rename Cloud Identity Engine tenants.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you want to change the name of a Cloud
Identity Engine tenant after you create it, you can rename it in
the Cloud Identity Engine app.

1. Log in to the [hub](https://apps.paloaltonetworks.com).
2. Select Common ServicesTenant Management.
3. Select the tenant you want to rename then click Edit
   Tenant.

   ![]()

   A pop-up
   displays to allow you to edit the name of the tenant.

   You
   cannot change the region. If you need to change the region for an
   tenant, [create a new tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/create-cloud-identity-engine-instances.html#id17CLJB00HR1).
4. Enter the new Name and confirm
   the change by clicking Save.

   ![]()

   A confirmation
   message displays to indicate that the tenant was successfully renamed.

---

<a id="delete-cloud-identity-engine-tenants"></a>

###### Delete Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/delete-cloud-identity-engine-instances>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you no longer need to use an tenant, you
can delete it as long as no other application is using it. If the
tenant is currently used by another app, an error message displays
when you try to delete the tenant.

1. (On-premises Active Directory only)[Stop](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service.html#id1818J060VBD) the agent’s
   connection with the Cloud Identity Engine and [Remove the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/remove-the-cloud-identity-agent.html#ide32f74ea-6dad-4d31-b5c0-651cdf2d2ae8).
2. Log in to the [hub](https://apps.paloaltonetworks.com).
3. Select Common ServicesTenant Management.
4. Select the tenant and click Delete Tenant.

   ![]()
5. Confirm that you want to delete the tenant.

   ![]()

---

<a id="delete-domains-or-directories-from-cloud-identity-engine-tenants"></a>

###### Delete Domains or Directories from Cloud Identity Engine Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/delete-domains-or-directories-from-cloud-identity-engine-instances>*

Learn how to delete Active Directory domains or Azure
AD directories from your Cloud Identity Engine tenant.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The procedure for deleting a domain from the Cloud Identity Engine varies
depending on whether you are deleting a domain for an Active Directory (AD)
configuration or for a cloud-based directory.

- [Delete Active Directory Domains](#id32517175-335d-4dd7-a5ea-b4bfb5948d0a_ida2a5c575-8ce8-4fa3-bdc2-d7f36244b176)
- [Delete Cloud-Based Directories](#id32517175-335d-4dd7-a5ea-b4bfb5948d0a_idadc11422-5ac5-48dc-abdc-5df8371b2fd6)

<a id="id32517175-335d-4dd7-a5ea-b4bfb5948d0a_ida2a5c575-8ce8-4fa3-bdc2-d7f36244b176"></a>

###### Delete Active Directory Domains

To delete a domain from your Cloud Identity
Engine tenant, first delete it from the agent configuration then
delete it from the Cloud Identity Engine app on the hub.

1. Launch the agent and select LDAP Configuration.
2. From the list of Servers, select
   the domain you want to delete and Delete it.

   ![]()
3. Commit the changes.

   You must delete the domain from the Cloud Identity agent
   configuration before you delete it from the Cloud Identity Engine
   app. Otherwise, it will be re-added on the next synchronization.
4. Log in to the hub and select the Cloud Identity Engine app.
5. Select the tenant with the domain you want to delete,
   then select Directory.
6. Remove the domain then Confirm the
   deletion of the domain.

   ![]()

<a id="id32517175-335d-4dd7-a5ea-b4bfb5948d0a_idadc11422-5ac5-48dc-abdc-5df8371b2fd6"></a>

###### Delete Cloud-Based Directories

1. Log in to the hub and select the Cloud
   Identity Engine app.
2. Select the tenant with the domain you want to delete,
   then select Directory.
3. Select Actions then Remove the
   directory.

   ![]()
4. Click Yes to confirm the deletion
   of the directory.

   ![]()

---

<a id="cloud-identity-engine-attributes"></a>

##### Cloud Identity Engine Attributes

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-attributes>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

An attribute is a unique identifier, such as a Distinguished Name, that correlates to a
specific object in the directory, which can be a user, a computer, or another network
entity. If your directory uses custom attributes that don’t use the following formats,
specify the custom formats in the Cloud Identity Engine app (see [Collect Custom Attributes with the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/collect-custom-attributes-with-the-cloud-identity-engine.html#id181TGN0B05P)).

To provide granular context for security policies and event logging, the Cloud Identity
Engine automatically collects a comprehensive set of default attributes from your
configured directories. For on-premises solutions like Active Directory and OpenLDAP,
this includes standard identifiers such as sAMAccountName,
userPrincipalName, mail, and group memberships
defined by memberOf. OpenLDAP specifically requires the
entryUUID attribute to successfully identify objects.

Cloud-based directories offer similar attribute mappings tailored to their specific
schemas. For instance, Microsoft Entra ID (formerly Azure AD) synchronizes extensive
user details, device compliance states, and role assignments to help prevent privilege
escalation. Similarly, Okta and Google Directory integrations map fields like
primaryEmail or nickName to standard Cloud
Identity Engine attributes to ensure consistency across different identity providers. If
you utilize the SCIM Connector, you gain further control by customizing exactly which
attributes—such as enterprise\_department—are provisioned to the engine.
You can verify that these attributes are populating correctly by viewing the raw
directory data within the Cloud Identity Engine app.

Verify that your attributes are valid before attempting to sync
the attributes. If one or more attributes are not valid, the initial sync isn’t
successful.

- [On-Premise Active
  Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-active-directory.html#cloud-identity-engine-attributes-active-directory)
- [On-Premise OpenLDAP](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-openldap.html#cloud-identity-engine-attributes-openldap)
- [Azure](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-azure.html#cloud-identity-engine-attributes-azure)
- [SCIM](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-scim.html#cloud-identity-engine-attributes-scim)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-okta.html#cloud-identity-engine-attributes-okta)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes/cloud-identity-engine-attributes-google.html#cloud-identity-engine-attributes-google)

##### Cloud Identity Engine Attributes (Active Directory)

Learn about On-Premise Active Directory attributes.

You can collect the following types of default attributes and their associated On-Premise
Active Directory fields:

###### User Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Admin Count | adminCount |

|

Common-Name | cn |

|

CompanyName | companyName |

|

Country | co |

|

Department | department |

|

Distinguished Name | dn |

|

Groups | memberOf |

|

Last Login | lastLogon |

|

LastLogonTime | lastLogonTimestamp |

|

Location | l |

|

MSDSAllowedDelegatedTo | msDS-AllowedToDelegateTo |

|

MSDSAllowedToActOnBehalfOfOtherIdentity | msDS-AllowedToActOnBehalfOfOtherIdentity |

|

MSDSSupportedEncryptionTypes | msDS-SupportedEncryptionTypes |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | mail |

|

Manager | manager |

|

NETBIOS Name | nETBIOSName |

|

Name | displayName |

|

Object Class | objectClass |

|

Primary Group ID | primaryGroupID |

|

SAM Account Name | sAMAccountName |

|

SID | objectSid |

|

SID History | sIDHistory |

|

Service Principal Name | servicePrincipalName |

|

Title | title |

|

Unique Identifier | objectGUID |

|

User Principal Name | userPrincipalName |

|

UserAccountControl | userAccountControl |

|

WhenChanged | whenChanged |

|

WhenCreated | whenCreated |

###### Organizational Unit (OU) Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Canonical Name | canonicalName |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Name | displayName |

|

Object Class | objectClass |

|

Unique Identifier | objectGUID |

|

When Changed | whenChanged |

|

WhenCreated | whenCreated |

###### Group Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Admin Count | adminCount |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Group Type | groupType |

|

Groups | memberOf |

|

Mail | mail |

|

Member | member |

|

Name | name |

|

Object Class | objectClass |

|

SAM Account Name | sAMAccountName |

|

SID | objectSid |

|

Unique Identifier | objectGUID |

|

WhenChanged | whenChanged |

|

WhenCreated | whenCreated |

###### Container Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Canonical Name | canonicalName |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Domain | domain |

|

Name | displayName |

|

Object Class | objectClass |

|

Unique Identifier | objectGUID |

|

WhenChanged | whenChanged |

|

WhenCreated | whenCreated |

###### Computer Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Admin Count | adminCount |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Groups | memberOf |

|

HostID | \_hostId |

|

Host Name | dNSHostName |

|

Last Login | lastLogon |

|

LastActiveDaysAgo | lastActiveDaysAgo |

|

LastLogonTime | lastLogonTimestamp |

|

MSDSAllowedDelegatedTo | msDS-AllowedToDelegateTo |

|

MSDSAllowedToActOnBehalfOfOtherIdentity | msDS-AllowedToActOnBehalfOfOtherIdentity |

|

MSDSSupportedEncryptionTypes | msDS-SupportedEncryptionTypes |

|

NETBIOS Name | nETBIOSName |

|

Name | displayName |

|

OS | operatingSystem |

|

OSServicePack | operatingSystemServicePack |

|

OSVersion | operatingSystemVersion |

|

Object Class | objectClass |

|

Primary Group ID | primaryGroupID |

|

SAM Account Name | sAMAccountName |

|

SID | objectSid |

|

SID History | sIDHistory |

|

Serial Number | serialNumber |

|

Service Principal Name | servicePrincipalName |

|

Unique Identifier | objectGUID |

|

User Principal Name | userPrincipalName |

|

UserAccountControl | userAccountControl |

|

WhenChanged | whenChanged |

|

WhenCreated | whenCreated |

##### Cloud Identity Engine Attributes (OpenLDAP)

Learn about OpenLDAP attributes.

You can collect the following types of default attributes and their associated Active
Directory fields:

###### User Attributes

|

Directory Sync Attribute | OpenLDAP Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Common-Name | cn |

|

Country | co |

|

Department | department |

|

Distinguished Name | dn |

|

Groups | memberOf |

|

Last Login | lastLogon |

|

LastLogonTime | lastLogonTimestamp |

|

Location | l |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | mail |

|

Manager | manager |

|

Name | displayName |

|

Object Class | objectClass |

|

SAM Account Name | sAMAccountName |

|

SID | objectSid |

|

Title | title |

|

Unique Identifier | entryUUID  OpenLDAP requires this attribute. |

|

User Principal Name | userPrincipalName |

|

WhenChanged | modifyTimestamp |

|

WhenCreated | createTimestamp |

###### Organizational Unit (OU) Attributes

|

Directory Sync Attribute | OpenLDAP Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Canonical Name | canonicalName |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Name | displayName |

|

Object Class | objectClass |

|

Unique Identifier | entryUUID |

|

WhenChanged | modifyTimestamp |

|

WhenCreated | createTimestamp |

###### Group Attributes

|

Directory Sync Attribute | OpenLDAP Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Common-Name | cn |

|

Distinguished Name | dn |

|

Group Type | groupType |

|

Groups | memberOf |

|

Mail | mail |

|

Member | uniqueMember |

|

Name | name |

|

Object Class | objectClass  For OpenLDAP, the groups' objectClass must be groupOfUniqueNames. |

|

Unique Identifier | entryUUID |

|

WhenChanged | modifyTimestamp |

|

WhenCreated | createTimestamp |

###### Container Attributes

|

Directory Sync Attribute | OpenLDAP Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Canonical Name | canonicalName |

|

Common-Name | cn |

|

Distinguished Name | dn |

|

Domain | domain |

|

Name | displayName |

|

Object Class | objectClass |

|

Unique Identifier | entryUUID |

|

WhenChanged | modifyTimestamp |

|

WhenCreated | createTimestamp |

###### Computer Attributes

|

Directory Sync Attribute | OpenLDAP Field |

| --- | --- |

|  |  |
| --- | --- |
|

Common-Name | cn |

|

Distinguished Name | dn |

|

Groups | memberOf |

|

HostName | dNSHostName |

|

Last Login | lastLogon |

|

LastLogonTime | lastLogonTimestamp |

|

NETBIOS Name | nETBIOSName |

|

Name | displayName |

|

OS | operatingSystem |

|

OSServicePack | operatingSystemServicePack |

|

OSVersion | operatingSystemVersion |

|

Object Class | objectClass |

|

Primary Group ID | primaryGroupID |

|

SAM Account Name | sAMAccountName |

|

SID | objectSid |

|

Serial Number | serialNumber |

|

Unique Identifier | entryUUID |

|

User Principal Name | userPrincipalName |

|

User Account Control | userAccountControl |

|

WhenChanged | modifyTimestamp |

|

WhenCreated | createTimestamp |

##### Cloud Identity Engine Attributes (Azure)

Learn about Entra-ID / Azure attributes.

You can collect the following types of default attributes and their associated Active
Directory fields:

###### User Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

BusinessPhones | businessPhones |

|

CompanyName | companyName |

|

Country | country |

|

Department | department |

|

EmployeeId | employeeId |

|

FaxNumber | faxNumber |

|

Given Name | givenName |

|

Groups | memberOf |

|

IsResourceAccount | isResourceAccount |

|

LastPasswordChangeDateTime | lastPasswordChangeDateTime |

|

Location | officeLocation |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | mail |

|

Manager | manager |

|

MobilePhone | mobilePhone |

|

Name | displayName |

|

OnPremisesDistinguishedName | onPremisesDistinguishedName |

|

OnPremisesDomainName | onPremisesDomainName |

|

OnPremisesExtensionAttributes | onPremisesExtensionAttributes |

|

OnPremisesImmutableId | onPremisesImmutableId |

|

OnPremisesLastSyncDataTime | onPremisesLastSyncDateTime |

|

OnPremisesProvisioningErrors | onPremisesProvisioningErrors |

|

OnPremisesSamAccountName | onPremisesSamAccountName |

|

OnPremisesSyncEnabled | onPremisesSyncEnabled |

|

OtherMails | otherMails |

|

PasswordPolicies | passwordPolicies |

|

PasswordProfile | passwordProfile |

|

PostalCode | postalCode |

|

PreferredLanguage | preferredLanguage |

|

SignInSessionsValidFromDateTime | signInSessionsValidFromDateTime |

|

State | state |

|

StreetAddress | streetAddress |

|

Sur Name | surname |

|

Title | jobTitle |

|

Unique Identifier | objectGUID |

|

UsageLocation | usageLocation |

|

User Principal Name | userPrincipalName |

|

UserAccountControl | accountEnabled |

|

UserType | userType |

|

createdDateTime | createdDateTime |

|

onPremisesSecurityIdentifier | onPremisesSecurityIdentifier |

|

onPremisesUserPrincipalName | onPremisesUserPrincipalName |

###### Role Assignments Attributes

The Cloud Identity Engine only collects these attributes if
you select the Collect Roles and Administrators (Administrative
roles) option when you set up your Azure directory.

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Description | description |

|

Is Builtin | isBuiltIn |

|

Is Enabled | isEnabled |

|

Name | displayName |

|

Role Permissions | rolePermissions |

|

Template Id | templateId |

|

Unique Identifier | objectGUID |

###### Group Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Classification | classification |

|

DeletedDateTime | deletedDateTime |

|

Description | description |

|

Group Type | groupTypes |

|

Groups | memberOf |

|

Mail | mail |

|

Mail Nick Name | mailNickname |

|

MailEnabled | mailEnabled |

|

Member | member |

|

Name | displayName |

|

OnPremisesDomainName | onPremisesDomainName |

|

OnPremisesLastSyncDateTime | onPremisesLastSyncDateTime |

|

OnPremisesProvisioningErrors | onPremisesProvisioningErrors |

|

OnPremisesSecurityIdentifier | onPremisesSecurityIdentifier |

|

OnPremisesSyncEnabled | onPremisesSyncEnabled |

|

RenewedDateTime | renewedDateTime |

|

SAM Account Name | onPremisesSamAccountName |

|

SID | securityIdentifier |

|

SecurityEnabled | securityEnabled |

|

Unique Identifier | objectGUID |

|

Visibility | visibility |

|

createdDateTime | createdDateTime |

###### Computer Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

ComplianceExpirationDateTime | complianceExpirationDateTime |

|

Device ID | deviceId |

|

Groups | memberOf |

|

IsCompliant | isCompliant |

|

IsManaged | isManaged |

|

LastLogonTime | approximateLastSignInDateTime |

|

Manufacturer | manufacturer |

|

MdmAppId | mdmAppId |

|

Model | model |

|

Name | displayName |

|

OS | operatingSystem |

|

OSVersion | operatingSystemVersion |

|

ProfileType | profileType |

|

Serial Number | deviceId |

|

SystemLabels | systemLabels |

|

TrustType | trustType |

|

Unique Identifier | objectGUID |

|

UserAccountControl | accountEnabled |

|

createdDateTime | createdDateTime |

###### Application Attributes

|

Directory Sync Attribute | Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

App Id | appId |

|

App Roles | appRoles |

|

Application TemplateId | applicationTemplateId |

|

Description | description |

|

DisabledByMicrosoftStatus | disabledByMicrosoftStatus |

|

Identifier Uris | identifierUris |

|

Name | displayName |

|

Unique Identifier | objectGUID |

|

createdDateTime | createdDateTime |

|

web | web |

##### Cloud Identity Engine Attributes (SCIM)

Learn about SCIM attributes.

You can collect the following types of default attributes and their associated SCIM
Connector fields:

###### User Attributes

The following section lists the default attributes for users that the directory
provisions to Directory Sync using SCIM.

|

Directory Sync Attribute | SCIM Field |

| --- | --- |

|  |  |
| --- | --- |
|

Common-Name | name\_formatted |

|

CompanyName | addresses\_work\_formatted |

|

Country | addresses\_work\_country |

|

Department | enterprise\_department |

|

EmployeeId | enterprise\_employeeNumber |

|

FaxNumber | phoneNumbers\_fax\_value |

|

Given Name | name\_firstName |

|

Groups | groups |

|

Location | addresses\_work\_locality |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | emails\_work\_value |

|

MobilePhone | phoneNumbers\_mobile\_value |

|

Name | displayName |

|

PostalCode | addresses\_work\_postalCode |

|

PreferredLanguage | preferredLanguage |

|

PreferredName | nickName |

|

StreetAddress | addresses\_work\_streetAddress |

|

Sur Name | name\_familyName |

|

Title | title |

|

Unique Identifier | objectGUID |

|

User Principal Name | userName |

|

UserType | userType The SCIM gallery app does not support the userType attribute. |

|

createdDateTime | meta\_created |

###### Group Attributes

The following section lists the default attributes for groups that the directory
provisions to Directory Sync using SCIM.

Group names for the displayName
attribute must be unique. For more information, refer to [Troubleshoot Cloud Identity Engine Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5).

|

Directory Sync Attribute | SCIM Field |

| --- | --- |

|  |  |
| --- | --- |
|

Description | displayName |

|

Group Type | groupTypes |

|

Member | members |

|

Name | displayName |

|

Unique Identifier | objectGUID |

|

createdDateTime | meta\_created |

##### Cloud Identity Engine Attributes (Okta)

Learn about Okta attributes.

You can collect the following types of default attributes and their associated Okta
Directory fields:

###### User Attributes

|

Directory Sync Attribute | Okta Directory Fields |

| --- | --- |

|  |  |
| --- | --- |
|

City | city |

|

CompanyName | companyName |

|

Country | countryCode |

|

Department | department |

|

Distinguished Name | dn |

|

EmployeeId | employeeNumber |

|

Given Name | firstName |

|

Groups | memberOf |

|

Last Login | lastLogin |

|

LastPasswordChangeDateTime | passwordChanged |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | email |

|

Manager | managerDN |

|

MobilePhone | mobilePhone |

|

Name | displayName |

|

PostalCode | zipCode |

|

PreferredLanguage | preferredlanguage |

|

PreferredName | nickName |

|

Primary Group ID | primaryGroupID |

|

SID | objectSid |

|

State | state |

|

StreetAddress | streetAddress |

|

Sur Name | lastName |

|

Title | title |

|

Unique Identifier | objectGUID |

|

User Principal Name | userName |

|

UserAccountControl | status |

|

UserType | userType |

|

createdDateTime | created |

###### Group Attributes

|

Directory Sync Attribute | Okta Directory Fields |

| --- | --- |

|  |  |
| --- | --- |
|

Description | description |

|

Group Type | groupTypes |

|

Groups | memberOf |

|

Member | member |

|

Name | name |

|

SAM Account Name | samAccountName |

|

SID | objectSid |

|

Unique Identifier | objectGUID |

|

createdDateTime | created |

###### Application Attributes

|

Directory Sync Attribute | Okta Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

App Id | appId |

|

Client Uri | client\_uri |

|

Description | description |

|

Name | displayName |

|

Unique Identifier | objectGUID |

##### Cloud Identity Engine Attributes (Google)

Learn about Google attributes.

To identify users and apply security policy, the Cloud Identity Engine collects the
following attributes from Google Directory:

###### User Attributes

|

Directory Sync Attribute | Google Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

BusinessPhones | phones |

|

Country | country |

|

Given Name | givenName |

|

Groups | memberOf |

|

LastLogonTime | lastLoginTime |

|

Location | locations.area |

|

Mail If you do not configure a value for the Mail attribute, the Cloud Identity Engine uses the value of the User Principal Name. | primaryEmail |

|

Name | fullName |

|

OtherMails | emails |

|

PreferredLanguage | languages |

|

SID | id |

|

State | state |

|

StreetAddress | streetAddress |

|

Sur Name | familyName |

|

Title | title |

|

Unique Identifier | objectGUID |

|

User Principal Name | userName |

|

UserAccountControl | suspended |

|

UserType | isAdmin |

|

createdDateTime | creationTime |

###### Organizational Unit (OU) Attributes

|

Directory Sync Attribute | Google Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Description | description |

|

Name | name |

|

Unique Identifier | objectGUID |

###### Group Attributes

|

Directory Sync Attribute | Google Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Group Type | kind |

|

Groups | memberOf |

|

Mail | email |

|

Member | member |

|

Name | name |

|

SID | id |

|

Unique Identifier | objectGUID |

###### Computer Attributes

|

Directory Sync Attribute | Google Directory Field |

| --- | --- |

|  |  |
| --- | --- |
|

Groups | memberOf |

|

HostName | dNSHostName |

|

Last Login | lastLogon |

|

LastLogonTime | lastLogonTimestamp |

|

NETBIOS Name | nETBIOSName |

|

OS | operatingSystem |

|

OSServicePack | operatingSystemServicePack |

|

OSVersion | operatingSystemVersion |

|

Primary Group ID | primaryGroupID |

|

SID | deviceId |

|

SID History | sIDHistory |

|

Serial Number | serialNumber |

|

Service Principal Name | servicePrincipalName |

|

Unique Identifier | objectGUID |

|

User Principal Name | userPrincipalName |

|

UserAccountControl | status |

---

<a id="collect-custom-attributes-with-the-cloud-identity-engine"></a>

##### Collect Custom Attributes with the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/collect-custom-attributes-with-the-cloud-identity-engine>*

If you have custom directory attribute formats, you can customize the attributes that
the Cloud Identity Engine collects.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If your directory uses custom attributes, you must specify the custom attribute so
that the Cloud Identity Engine can collect it. To view the default attribute
formats, see [Cloud Identity Engine Attributes](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/cloud-identity-engine-attributes.html).

You can filter criteria for attribute-based Cloud
Dynamic User Groups (CDUGs) and can create groups based on selective attributes.
This allows you to specify all applicable (scalar, non time-based, and non id-based)
attributes in the filter criteria.

1. Log in to the hub and select the Cloud Identity Engine tenant that uses custom
   attributes.
2. Select Attributes then select the directory type that
   uses the custom attribute.
3. Select a custom attribute in your directory.

   The field is now editable.

   ![]()
4. Enter the new value in the field and confirm the change by clicking the
   checkmark.

   Custom attributes cannot begin with an underscore ( \_ ).

   A green
   triangle displays in the upper left corner of the row to indicate the changes. 

   ![]()

   To use the original attribute value, select the custom attribute and
   Restore Default.

   ![]()

---

<a id="view-directory-data"></a>

##### View Directory Data

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/view-directory-data>*

Learn how to view detailed information about your directory
data in the Cloud Identity Engine.

In the Cloud Identity Engine app, you can
use the Directory Data page to view data (depending on your directory
type) about users, computers, groups, devices, containers, and organizational
units that are collected from your directory. You can also use keywords
to search the data for specific objects (such as users or groups)
and view all the attributes of those objects to validate the data.

The
Directories page provides a total count for the objects that the
Cloud Identity Engine has collected from your directory. To review
details for an object, click the total count in the column for the
object to view the Directory Data page.

![]()

When
you select an object, the number of results for that object displays below
the domain name at the top of the page.

![]()

By
default, up to 25 results display for the object. To view the rest
of the data or a specific result, use the following methods.

- Search for data in the search bar by
  entering a partial or complete keyword, then press Enter or click Search to
  see the results.

  Search terms are not case-sensitive.

  ![]()
- To refine the search results, select a search type:

  Search results include delimiter characters for [MongoDB](https://www.mongodb.com/docs/manual/core/index-text/) and [Unicode](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt). For example,
  entering test-user as a search term includes
  results for test-user and test user but
  not testuser because the hyphen is
  a delimiter character.

  - Text search—Displays
    results that match the entire search term. 

    ![]()
  - Substring match—Displays results that
    match the entire search term or that partially match the search
    term. 

    ![]()
- Browse the data using the page navigation buttons or
  use the drop-down list to select the number of rows to display.

  ![]()
- To view selected details for an object, select Details
  (

  ![]()

  ) in the first
  column.

  - When you select a group, the app displays the first 2000 flattened
    users in the group below the Member
    attribute. If the group doesn’t contain any members, this attribute
    does not display any information.
  - When you select a user, the app displays the first 2000 groups to
    which the user belongs below the Groups
    attribute. If the user doesn’t belong to any groups, this attribute
    does not display any information.

  ![]()

  The Cloud Identity Engine currently supports retrieval of inventory
  information for enterprise applications, such as Name, Redirect URIs,
  and IDs. Viewing the membership assignment relationships between the
  retrieved apps and their corresponding users and groups is currently a
  beta feature.

  - To view the all data for this object, click View Raw
    Data in the upper right corner. 

    ![]()
  - To copy the details for the data, click Copy
    (

    ![]()

    ) to copy the
    details to the clipboard.
  - To switch the view between Direct and
    Direct and Nested, select the toggle. 

    ![]()

    If the directory contains nested groups, they display after you select
    the toggle. To restore the original Direct view,
    select the toggle again. 

    ![]()

    Nested group information is not available
    for attribute-based Cloud Dynamic User Groups.
  - To query the data, enter a search term and click Apply
    Search to display the results. 

    ![]()
- To return to the Directory page, select Go
  Back to Directory in the upper right.

  ![]()

---

<a id="cloud-identity-engine-user-context"></a>

##### Cloud Identity Engine User Context

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

As large enterprise networks continue to become increasingly distributed across
cities, regions, and countries, enforcing least-privilege user access becomes
increasingly challenging, especially as scale increases. User Context for the Cloud
Identity Engine provides simplified granular control over the data that is shared
across your security devices. It provides administrators with the flexibility to
specify the data types (such as mappings and quarantine lists) each device sends and
receives.

The simplified deployment of User Context for information such as user mappings and
tags minimizes time to enforcement. Centralizing visibility for users, tags, and
mappings makes it easier to segment the data types based on user access needs. This
method also increases scalability for Virtual Desktop users (VDI) using the Terminal
Server agent.

To enforce policy, User Context provides IP address-to-username[mappings](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/user-id-concepts/user-mapping), IP port to username mappings,
user [tags](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-tags-to-group-and-visually-distinguish-objects) IP address tags, Host IDs, and
quarantine list information to other NGFWs and devices in your network through
segments, which consist of firewalls that you specify. A [segment](#) can
collect information as well as share information. A [publishing segment](#)
sends the data from the firewalls and devices in that segment to the firewalls in
the [subscribed segment](#), which contains the firewalls that receive the
data from the publishing segments.

NGFWs and Panorama can share multiple data types to one segment. On a firewall or
Panorama, each data type can only be shared in one segment. Each Firewall or
Panorama can receive data from up to 100 segments.

By selecting the data that is collected by a segment and where that data is shared,
you have full control in ensuring that the information required to enforce
least-privilege access is available on each enforcement device.

If you associate a firewall that you [configure as a User-ID hub](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/deploy-user-id-in-a-large-scale-network/share-user-id-mappings-across-vsys) with a segment,
the Cloud Identity Engine provides the data types based on the firewall that is
subscribed or publishing the segment, not based on the virtual system. To ensure
that both locally learned data and data that the User Context Cloud Service provides
are available to all virtual systems, configure the User-ID hub firewall as a
subscriber in the segment.

- [PAN-OS & Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/cloud-identity-engine-user-context/cloud-identity-user-cointext-pan-os.html#cloud-identity-user-cointext-pan-os)

##### Cloud Identity User Context (PAN-OS)

Learn about user context for PAN-OS & Panorama with CIE.

To control data shared over your network with User Context:

1. Onboard your Cloud Identity Engine instance.
   1. Obtain the serial number for the firewall you want to onboard, and
      [Register the firewall](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/getting-started/register-the-firewall) with the
      Palo Alto Networks Customer Support Portal (CSP).
   2. Click the magic link provided by Palo Alto Networks to begin onboarding
      your Cloud Identity Engine tenant.

      The magic link is provided by Palo Alto Networks by email.
   3. Click MSP Cloud Management.

      ![]()
   4. Continue the onboarding process.

      ![]()
   5. Claim the license for the tenant you want to
      onboard.

      ![]()
   6. Select the Customer Support Account you want to
      use.

      ![]()
   7. Select the Parent Tenant you want to use or
      click Create New to create a new tenant.

      ![]()
   8. Click Claim and continue to continue the
      onboarding process.

      ![]()
   9. Click Add Licensed Product to continue the
      onboarding process.

      ![]()
   10. Select the contract you want to use.

       ![]()
   11. Select the Region for your Cloud Identity Engine
       instance.

       ![]()
   12. Click Activate Now to complete the onboarding
       process.

       ![]()
   13. Confirm that the Status for the Cloud
       Identity Engine is
       Complete.

       You can access your Cloud Identity Engine instance by selecting
       Cloud Identity Engine.

       ![]()
   14. In the bottom left of the window, select the icon for your tenant and
       select Device Associations.

       ![]()
   15. Select Add Device.

       ![]()
   16. Select your Customer Support Account and enter your firewall serial
       number.
   17. Select the firewall Save your changes.
   18. Select Associate Apps.
   19. Select the firewall, select the Cloud Identity
       Engine, and Save your
       selections.

       ![]()
2. In the Cloud Identity Engine, activate sharing for mappings.
   1. Log in to the Cloud Identity Engine app and select User ContextSegments
   2. Activate sharing for mappings.

      ![]()
3. Configure the default segment as a publishing segment.
   1. Select the Firewalls tab and select one or more
      firewalls.

      ![]()
   2. After selecting the firewalls that you want to include in this segment,
      Assign Segments to the selected firewalls.

      Assigning a segment to a firewall allows you to define which data the
      Cloud Identity Engine receives from or provides to that firewall.
      You can only assign segments to a firewall that uses PAN-OS 11.0;
      User Context does not support other source types.

      ![]()
   3. (Optional) If you want to include additional firewalls in the segment,
      Add Firewalls to the segment to specify the
      firewalls you want to include.

      ![]()
   4. For each Data Type that you want to share,
      select the Segment where you want to publish the
      data type.

      Firewalls publish each data type to one
      segment. To share data between firewalls, you will need to configure
      a segment for each data type you want share.

      You can select the following data types:

      - IP User Mappings—(GlobalProtect,
        Authentication Portal, XFF Headers, Username Header
        Insertion, XML APIs, Syslog, Server Monitoring, Panorama
        TrustSec plugin) Maps the IP address to a username.
      - IP Tag Mappings—([Dynamic Address Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically)
        only) Maps the IP address to a tag.
      - User Tag Mappings—([Dynamic User Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-dynamic-user-groups-in-policy)
        only) Maps the tag to a user.
      - Quarantine List—(GlobalProtect only)
        Lists the firewalls that GlobalProtect has in quarantine.
      - IP Port Mappings—(Terminal Server agent
        only) Maps the IP address to the port range allocated to a
        Windows-based terminal server user.

      ![]()
   5. Click Review Changes to review your
      configuration before submitting the changes.

      ![]()
   6. Save the changes to confirm the
      configuration.

      ![]()
4. Create a segment to subscribe to the publishing segment you created in the
   previous step.

   Publishing segments provide the specified data type that the Cloud Identity
   Engine collects from other firewalls to the segment containing the firewalls
   that you select.

   You can subscribe up to 100 segments per
   firewall.

   1. Select User ContextSegments and click Add New Segment.

      ![]()
   2. Enter a unique Segment Name and optionally a
      Description for the segment.

      ![]()
   3. Click Add New Segment to save the changes.
   4. Click Segments to add the segments you want to
      receive data.

      ![]()
   5. Select the segments that you want to include and
      Add the segments.

      ![]()
5. (Optional) Edit segments as needed to customize how the Cloud Identity Engine
   provides mappings to the firewalls.
   1. If sharing for data type is Enabled and you do
      not want to share this data type in this segment, select it to change
      the setting to Disabled.

      ![]()
   2. If you no longer need a segment, delete it from the configuration.

      ![]()
6. When your configuration is complete, Review Changes and
   Save the configuration.
7. On your firewall, enable the service that the Cloud Identity Engine uses to
   communicate with your firewall.
   1. Ensure that you have configured a device certificate.
   2. Log in to the firewall and Edit the
      PAN-OS Edge Service Settings (DeviceManagementSetupPAN-OS Edge Service Settings).

      ![]()
   3. Enable User Context Cloud Service and click
      OK to confirm the changes.

      If the firewall traffic uses a management interface, create
      security policy rules to allow connectivity between the firewall
      and the User Context Cloud Service.

      ![]()
   4. Commit your changes on the firewall.
8. Verify the User Context configuration is successful and view the mappings and
   tags that the Cloud Identity Engine collects from the firewall.
   1. On the firewall, verify the User Context Cloud Service
      Connection Status is active.

      ![]()
   2. In the Cloud Identity Engine app, select User ContextMappings & Tags to review the information for the data types.

      You can review the following data types:

      - User-ID—Search User-ID mappings by
        Username or IP
        address.
      - User Tags—Search [Dynamic User Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-dynamic-user-groups-in-policy)
        tags by Username or by
        Tag.
      - IP Tags—Search [Dynamic Address Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically)
        tags by IP address or by
        Tag.
      - IP-Port User—(Terminal Server agent only)
        Search Terminal Server agent mappings by
        IP address.
      - Host IDs—(GlobalProtect only) Search
        devices (both quarantined and not quarantined) by
        Host ID.

      ![]()

      Now that you’ve configured segments, you can use them to [enable user- and group-based
      policy](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/enable-user-and-group-based-policy), [authentication](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/authentication/configure-an-authentication-profile-and-sequence) profiles
      and sequences, and other firewall-based tasks.

---

<a id="create-a-cloud-dynamic-user-group"></a>

##### Create a Cloud Dynamic User Group

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/create-a-cloud-dynamic-user-group>*

Learn how to create a Cloud Dynamic User Group in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Cloud Dynamic User Groups simplify the creation of group-based Security policy by
providing adaptable and granular group membership that updates automatically based
on the criteria (also known as context or attributes) you specify. This allows you
to create a policy that adapts to changes in user behavior, location, and other
conditions where context plays a key role in determining access.

As work locations change and users take on different roles in an organization,
determining user privileges based on attributes such as department or location is no
longer sufficient. Cloud Dynamic User Groups provide a simplified and automated
solution by allowing you to specify the context for group membership based on
attributes that can change (such as location, department, or title), allowing you to
create more responsive group-based policy.

If you're using a Cloud Dynamic User Group to [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html), you must add the users in the Cloud Dynamic User Group to the
SAML app integration in the Azure Portal. For more information, refer to step 3 in
[Configure Azure as an IdP in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html).

You can also create static groups where membership remains constant until you
manually add or remove members. For example, you can use static groups to quickly
assign privileges or to isolate an account that’s exhibiting unusual or risky
behavior based on specific events.

If you're using [Microsoft Active Directory Identity
Protection](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection), you can use the risk assessment information to create Cloud
Dynamic User Groups based on a user's risk level or anomalous user behavior, such as
an unusual login location.

Using risk assessment information to create Cloud Dynamic
User Groups requires the [client credential flow for Azure
AD](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory/set-up-azure-directory/deploy-client-credential-flow-for-azure-ad.html). You must
allow the following permissions in the Azure Portal to enable support for risk-based
attributes:

- IdentityRiskyUser.Read.All
- IdentityRiskEvent.Read.All

1. If you have not already done so, configure your directory for the type of Cloud
   Dynamic User Group you want to create.
   1. Configure an [on-premises directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-an-on-premises-directory.html) or a
      [cloud-based directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory.html).
   2. (User Risk Information with Azure AD only) To allow the Cloud
      Identity Engine to collect user risk information from your [Microsoft Active Directory Identity
      Protection](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection), select Collect user risk information
      from Azure AD Identity Protection.

      For an existing Azure Active Directory (AD)
      configuration in the Cloud Identity, [reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-azure-directory/reconnect-directory.html) your directory to enable user
      risk information collection.

      ![]()
   3. [Sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) the groups for the
      directory.
2. In the Cloud Identity Engine app, select Directories and
   click on the number in the Groups column.

   ![]()
3. On the Directory Data page, click Create New Dynamic User
   Group.

   ![]()
4. Select the Category for the group.

   - Attribute Based—Specify the criteria for the
     Dynamic User Group using attributes.
   - On Demand Assignment—Assign specific users to a
     static group.

   ![]()
5. Enter the Common Name for the group.

   This automatically generates a Distinguished Name for
   the group that the Cloud Identity Engine, Prisma Access, and your firewalls
   use to identify the group. The Cloud Identity Engine appends
   \_cdug to the name you enter to indicate
   that the group is a Cloud Dynamic User Group.

   ![]()
6. (Optional) Enter a Group Email for the group.

   ![]()
7. (Optional) Enter a Description for the group.

   ![]()
8. Depending on the group Category you selected in step
   [4](#create-a-cloud-dynamic-user-group), select either the attributes you want to use
   to define the group or the users you want to add to the group.
   1. (Attribute Based only) Select whether you want the group members to
      match Any of the criteria or if you want them to
      match All of the criteria you select.

      ![]()
   2. (Attribute Based only) Click Select context or
      attribute to select the criteria (also known as context
      or attribute) that you want to use to define the group.

      ![]()

      ![]()
   3. (Attribute Based only) Click Select operator to
      select the type of operand.

      The operators that are available depend on
      your context or attribute selection in the previous step.

      - is equal to—Adds members to the group who
        are an exact match for a single attribute or context.
      - is equal to ANY of the following—Adds
        members to the group who are an exact match for one or more
        attributes or contexts.
      - is not equal to—Adds members to the group
        results who don't match the attribute or context.
      - contains—Adds members to the group when
        they contain the term you enter.
      - starts with—Adds members to the group
        when they begin with the characters you enter.

      ![]()
   4. (Attribute Based only) Click Select value to
      select the value (if the operand is is equal to)
      or values (if the operand is is equal to ANY of the
      following) for the group members. If the operand is
      contains or starts
      with, enter the value.

      ![]()
   5. (Optional) If you want to include additional criteria for the Cloud
      Dynamic User Group, select the type of operand and repeat the previous
      steps as needed to add the necessary criteria for the group.

      - Add OR—Adds members to the group when at
        least one of the criteria applies.
      - Add AND—Adds members to the group only
        when all criteria apply.

      ![]()
   6. (On Demand Assignment only) Click Add Users to
      view the list of possible group members.

      ![]()
   7. (On Demand Assignment only) Select the users you want and
      Add them to the group.

      ![]()

      To filter the list of possible group members, enter a search term
      and Apply Search and optionally select either
      Text Search or Substring
      Search. 

      ![]()
9. (Optional) If you want to delete one of the contexts or attributes, click
   Delete in the row that contains the context or
   attribute you want to remove.

   ![]()
10. (Optional) To remove a user from a cloud Dynamic User Group, select the check
    box in the row for the user and click Remove User then
    click Continue to confirm.

    The Add User button changes to Remove
    User when you select a user. 

    ![]()
11. Click Submit to create the Cloud Dynamic User
    Group.

    You can now use the Cloud Dynamic User Group to [create group-based Security policy](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/user-id/enable-user-and-group-based-policy).
12. (User Risk Information with Azure AD only) If you enabled user risk
    information collection in step [1.b](#create-a-cloud-dynamic-user-group), verify that the Cloud Identity Engine can
    successfully collect the information by clicking the locked user icon and
    verifying that Collect User Risk displays with a
    green check mark.

    ![]()
13. To remove a Cloud Dynamic User Group, select the ellipses button then select
    Remove.

    ![]()

    If a sync for the removed group is currently in
    progress, the removed group could still display on the page. If this occurs,
    refresh the page and confirm the removed group no longer displays.

---

<a id="configure-third-party-device-id"></a>

##### Configure Third-Party Device-ID

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/configure-third-party-device-id>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Third-Party Device-ID allows you to leverage information from third-party IoT detection sources
to simplify the task of identifying and closing security gaps for devices in your
network. Third-Party Device-ID enables [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/configure-third-party-device-id-in-prisma-access) to obtain and use
information from third-party IoT visibility solutions through the Cloud Identity
Engine for device visibility and control.

When you configure Third-Party Device-ID, the third-party IoT solutions can use an API to provide
the [Device-ID](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-id) verdicts to a secure cloud-based
infrastructure, the Third-Party Device-ID service, that provides the information to
the Prisma Access Security Processing Nodes (SPNs).

The same verdicts display as IP address-to-device mappings in the Cloud Identity
Engine, allowing you to confirm that the Device-ID verdicts are available to your
Palo Alto Networks applications. After the Prisma Access SPNs receive the IP
address-to-device mappings and the third-party IoT solution information is available
in the Cloud Identity Engine, any matching device-based policy rules defined in
Prisma Access are enforced.

The following diagram depicts
how the Third-Party Device-ID service receives the device information
from the third-party IoT solutions, which it then transmits as IP
address-to-device mappings to the Cloud Identity Engine and the
Prisma Access SPNs.

![]()

Before
you begin the procedure, obtain a certificate signing request and
its key for the vendor of each third-party IoT solution you want
to use with Third-Party Device-ID from your network administrator.

1. Activate Third-Party Device-ID in the Cloud Identity
   Engine.

   If you have not already done so, configure the [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/set-up-the-cloud-identity-engine).

   1. Log in to the hub and select the Cloud Identity
      Engine tenant you want to use, then select User
      ContextThird-Party Device-ID.

      ![]()
   2. Select the Location of your tenant.

      Because you can only select the region once
      and you can't change it after making a selection, verify your region
      before selecting it during Third-Party Device-ID activation.

      ![]()
   3. Click Add New Management System.

      ![]()
2. Upload the certificate signing request (CSR) from the
   third-party IoT solution.
   1. Enter a unique Configuration Name (for example,
      the vendor of the third-party IoT solution).

      ![]()
   2. Click Browse Files or drag and drop to upload
      the certificate signing request (CSR) file from the third-party IoT
      solution.

      Contact the administrator of the third-party IoT solution to obtain
      the CSR file.

      You can only upload a CSR
      once for each configuration. If you need to update or change the
      configuration, you must create a new CSR.

      ![]()
3. Obtain the signed certificate and the API key to import
   to the management system for your third-party IoT solution.
   1. Click Sign CSR and Export to
      download the certificate that you must import to the third-party
      IoT solution management system.

      To help prevent any security risk for the certificate
      or the API key, be sure to store both the signed certificate and the
      API key in a secure location.

      ![]()
   2. Click Generate New API Key to
      generate an API token to authenticate the third-party IoT solution.

      The API key is a token that contains information about
      the third-party IoT solution and other required information, such
      as the identifier for the tenant and the token’s expiration.

      If
      the API key becomes compromised, you must generate a new API key
      and import the new key to the third-party IoT solution management
      system.

      ![]()
   3. Copy the API key then import
      both the signed certificate that you downloaded and the API key
      that you generated to the management system for your third-party
      IoT solution and configure the IoT solution to use these files to
      communicate with the Third-Party Device-ID.

      To ensure that the third-party IoT solution can successfully communicate with the Third-Party
      Device-ID, you must upload both the signed certificate from the
      previous step and the API key. Create a configuration for each
      third-party vendor in your network that you want to use with
      Third-Party Device-ID. The configuration for each vendor must have a
      unique signed certificate and API key; don't use the same
      certificate or API key in more than one configuration.

      ![]()
4. Review the information to verify the configuration is
   correct.

   ![]()
5. After you use the API commands to obtain the information
   from the third-party IoT solutions, select Mappings to
   view information about the devices that the Third-Party Device-ID
   has detected and their IP address-to-device mappings.

   You can search the IP address-to-device mappings by IP
   address by entering the IP address and clicking Apply Search.

   ![]()
6. Select Management Systems to view information about your
   management systems, such as certificate expiration date and API key.
7. (Optional) Edit the management system configuration.
   1. In the row for the management system you want to edit, select ActionsEdit.

      ![]()
   2. Make the necessary changes to the configuration, such as uploading a
      new CSR or vendor authentication certificate or generating a new API
      key.

      You can't change the name of the
      configuration.

      ![]()
8. (Optional) Remove the management system configuration.
   1. In the row for the management system you want to remove, select ActionsRemove.

      ![]()
   2. Click Yes to confirm that you want to remove the
      configuration.

      ![]()

Now that your Third-Party Device-ID configuration is complete, you can:

- Use the [APIs](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/third-party-device-id-apis) to manage how your third-party
  IoT solutions share information with Third-Party Device-ID.
- Use [Device-ID](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-id) features such as the
  [Device Dictionary](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-id/manage-device-id) to manage and
  edit device information.

For more information, refer to the [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/configure-third-party-device-id-in-prisma-access) documentation.

---

<a id="configure-an-ip-tag-cloud-connection"></a>

##### Configure an IP Tag Cloud Connection

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/configure-an-ip-tag-cloud-connection>*

Learn how to configure the Cloud Identity Engine to collect IP-Tags for rule
enforcement.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

An IP-Tag Cloud Connection enables the Cloud Identity Engine to collect IP
address-to-tag information from cloud service providers. To enforce a tag-based
Security policy that adapts to IP address changes, configure [Dynamic Address Groups](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/monitor-changes-in-the-virtual-environment/use-dynamic-address-groups-in-policy) using the IP
address-to-tag information.

To configure the Cloud Identity Engine to collect IP address-to-tag (also known as
IP-tag) information for policy rule enforcement, configure a connection to your
cloud service provider to [synchronize](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) the mappings. The identity
management system provides the IP-tag information to the Cloud Identity Engine for
processing, which then provides the information to the firewalls for policy rule
enforcement.

To collect IP-tag information from your cloud service provider, you must grant the
Cloud Identity Engine the required permissions.

- **Azure**—Grant the read permissions as
  described in the Azure Monitoring section in the [VM-Series documentation](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-azure/about-the-vm-series-firewall-on-azure/vm-series-on-azure-service-principal-permissions) to the
  service account.
- **Amazon Web Services (AWS)**—Grant the service account the Amazon Role
  Name (ARN) roles as described in the IAM Roles and Permissions for Panorama
  section as shown in the JSON example in the [VM-Series documentation](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/about-aws-vm-monitoring/set-up-vm-monitoring-on-aws). For more
  information on the ARN, refer to the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html).
- **Google Cloud Platform (GCP)**—Grant the IAM roles as described in the
  [VM-Series documentation](https://docs.paloaltonetworks.com/vm-series/9-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/vm-monitoring-with-the-google-cloud-platform-plugin/configure-vm-monitoring) to the
  service account.

If you use [Strata Cloud Manager](https://docs.paloaltonetworks.com/cloud-management), you can view your
IP-tag information using the unified interface and use it to create your [tag-based Security policy](https://docs.paloaltonetworks.com/cloud-ngfw/aws/cloud-ngfw-on-aws/panorama-integration-overview/tag_based_policies).

For each region, you can synchronize up to 60,000 IP-tag mappings from a
cloud service in a monitoring configuration at one time. The Cloud Identity
Engine sync only the new or modified mappings each time. You can view up to
32,000 IP-tag mappings per page.

You can also view all IP-tag information in the Cloud Identity Engine (User ContextMappings and tags).

1. If you have not already done so, activate User Context and use the default
   segment or configure a new [segment](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context) to receive the mapping
   information.
2. Select User ContextIP-Tag Collection.

   ![]()
3. Select the Credential Configuration tab (if it does not
   already display).
4. To Set Up a New Credential Configuration, select the
   cloud service provider you want to use.

   - [AWS](#configure-an-ip-tag-cloud-connection)—Connect to an
     Amazon Web Services (AWS) instance.
   - [Azure](#configure-an-ip-tag-cloud-connection)—Connect to a
     Microsoft Azure Active Directory instance.
   - [Google Cloud
     Platform](#configure-an-ip-tag-cloud-connection)—Connect to a Google Cloud Platform (GCP)
     instance.

   ![]()
5. Enter a unique and descriptive Name for the
   configuration.
6. (AWS only) Configure your AWS connection.

   To open your AWS administrator portal in a new window so you can create or
   edit any necessary ARNs, select the type of CloudFormation template (CFT)
   you want to configure and log in with your AWS credentials.

   - Open CFT (Application Account
     Prerequisites)—Configure the Application Account
     prerequisites.
   - Open CFT (Security Account
     Prerequisites)—Configure the Application Account
     prerequisites.

   To enable monitoring using the current account, you
   only need to configure the application account prerequisites. If you want to
   use a different account, such as a service account or a [cross-account role](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) to collect the
   data, you must configure the application account prerequisites, the security
   account prerequisites, and a role ARN for the account. For more information,
   refer to the [Amazon](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) documentation.

   ![]()

   1. Enter your Access Key ID.

      To learn how to obtain your access key ID and secret access key, refer
      to the [AWS documentation.](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)
   2. Enter your Secret Access Key.
   3. Reenter your secret access key to Confirm Secret Access
      Key.
   4. (Optional) Enter a Role ARN Name and
      Role ARN Value.

      To configure additional Role ARNs, click Add Role
      ARN for each Role ARN you want to include.
7. (Azure only) Configure your Azure connection.
   1. Enter your Client ID.

      To learn how to obtain the client ID and client secret, refer to the
      [Azure documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#get-tenant-and-app-id-values-for-signing-in). 

      ![]()
   2. Enter your Client Secret.
   3. Enter your Tenant ID.

      To learn how to obtain the tenant ID and subscription ID, refer to the
      [Azure documentation.](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)
   4. Enter your Subscription ID.
8. (Google Cloud Platform only) Configure your GCP connection.
   1. [Create credentials](https://developers.google.com/workspace/guides/create-credentials)  for a
      service account in your Google Cloud console, and then download and save
      the JSON file in a safe location.
   2. Click Browse files and click
      Open to navigate to the JSON file or drag and
      drop the GCP credential JSON file.

      ![]()
   3. (Optional) Select the Region for the
      instance.

      You can optionally Search for a region. If you
      don't select a region, the Cloud Identity Engine uses the
      us-west-2 region. You can select one region
      per instance. 

      ![]()
9. Verify the connection by clicking the Test Connection
   button.

   (AWS and Google Cloud Platform only) You can optionally select the
   Region before testing the connection. By default,
   the Cloud Identity Engine selects the US West
   region; if this region does not enable API requests, select a region that
   can enable API requests.

   Even if the connection test isn't successful, you
   can still submit your configuration; until you resolve the connectivity
   issues, the configuration status is Not
   connected. You must resolve the connection issues for the
   configuration to successfully retrieve the IP address-to-tag
   mappings.
10. Submit the configuration.

    To collect and view your IP-Tag mappings, you must configure an [IP-Tag monitor
    configuration](#configure-an-ip-tag-cloud-connection).
11. (Strata Cloud Manager only) If you're using [Strata Cloud Manager](https://docs.paloaltonetworks.com/cloud-management), view the tags that the Cloud
    Identity Engine shares with Strata Cloud Manager by selecting an [address group](https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/objects/addresses-and-address-groups) then select the
    Tags from CIE tab when you [add match criteria](https://docs.paloaltonetworks.com/network-security/security-policy/administration/objects/address-groups/use-dynamic-address-groups-in-policy).

    ![]()
12. To configure a connection to your cloud service provider for monitoring
    purposes (such as audits) or to share the IP address-to-tag mapping information
    using a [segment](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context), select the Monitor
    & Status tab.

    There are four states for the connection to the cloud service provider:
    - Connected—The Cloud Identity Engine has
      successfully established a connection with the cloud service
      provider and can collect IP-tag mapping information.
    - Partially connected—The Cloud Identity Engine
      could successfully establish a connection to some aspects of the
      configuration, such as the region for AWS, but not all of them. The
      Cloud Identity Engine receives IP-tag mappings from connected
      sources; it does not receive them from unconnected sources.
    - Connection pending—The Cloud Identity Engine
      has successfully established a connection but has not completed the
      sync for the IP tag mappings from one or more regions.

      For more information on the connection
      status, select Click to see details.
    - Not connected—The Cloud Identity Engine
      couldn’t successfully establish a connection with a cloud service
      provider using the current configuration.

    ![]()

    1. Set Up a New Monitor Configuration and select
       the monitor configuration for the cloud service provider that you
       configured for credential configuration in step [4](#configure-an-ip-tag-cloud-connection).

       ![]()
    2. Enter a unique and descriptive Name for the
       configuration.

       ![]()
    3. Select the Credential Configuration that you
       configured in step [4](#configure-an-ip-tag-cloud-connection).
    4. (AWS only) Optionally select the Role
       ARN you want to use.
    5. Select if you want to configure the connection for All
       Regions , All VPCs (AWS only) or
       All Project IDs (GCP only).

       To select a specific region or virtual private cloud (VPC), deselect
       the All Regions or All
       VPCs check box and wait for the list of regions or VPCs
       to populate, and then select the region or VPC you want to include. To
       select a specific VPC, you must first select one or more regions or
       select all regions.
    6. (Azure only) Select whether you want to Fetch
       Service Tags.

       Azure Service tags simplify security for
       Azure virtual machines and Azure virtual networks because you can
       restrict network access to just the Azure services you want to use.
       A service tag represents a group of IP address prefixes for a
       particular Azure service. For example, a tag can represent all
       storage IP addresses.
    7. Define the Polling Interval (in seconds) to
       specify how frequently the Cloud Identity Engine checks for new data.

       The default is 60 seconds and the range is 60–1800 seconds.
    8. If you want to share the mappings, select the [segment](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context) you configured in step
       1. Otherwise, if you want to create this configuration only for
       monitoring without sending mappings to any firewalls, select
       None.

       If you need to change the segment after
       you submit the configuration, you must create a new configuration
       and select the segment you want to use.
    9. Submit the configuration.
13. Search and monitor your configurations in the Cloud Identity Engine.
    1. Select the Monitor & Status tab.
    2. Use the filters to highlight the information you want to find.

       - Name—Enter the name of a configuration to
         filter results to this configuration.

         The search query does not need to be
         an exact match for the name.
       - Vendor—Select the vendor type of the
         cloud service provider to filter the results to this vendor
         type.
       - Status— Select the status type (such as
         Connected or Partially
         Connected) to filter the results to this status
         type.
       - Segment— Select the
         Segment name to view the monitor
         segments that send mappings to the segment you select.
       - Associated Credential— Select the name of
         the Associated Credential configuration
         to view monitor segments that use the credential configuration
         type you select.

       ![]()
    3. (Optional) To remove the filter, click Reset.
14. Manage your IP-Tag Collection configuration.
    1. (Optional) To sync all new IP-tag mappings and use them in the Security
       policy immediately or to resolve any discrepancies in the IP-tag
       mappings, click Full Sync.

       ![]()

       The Sync Status displays the time and date of
       the last sync.

       ![]()
    2. (Optional) To change the IP-Tag Collection configuration, click
       Edit.

       ![]()
    3. (Optional) To remove the IP-Tag Collection configuration, click
       Delete and confirm the deletion.

       When you confirm the deletion, the Cloud
       Identity Engine removes all IP-tag mappings from the cloud service
       provider and from any firewalls that collect the IP-tag mappings to
       enforce Security policy.

       ![]()
15. View more details for a specific configuration.
    1. Select the name of the configuration that you want to view from the
       IP-Tag Collection page.

       ![]()
    2. On the Monitor & Status page, review the
       Connection Details to view information such
       as the connection status.

       ![]()
16. View the IP address-to-tag mapping information.

    Options vary depending on your configuration
    type.

    1. (AWS only) On the VPC tab,
       Search by VPC ID to view information for a
       specific VPC or select the number in the IPs
       column to view the IP addresses associated with the VPC
       ID in that row.

       ![]()
    2. Select the Tag To IP tab and Search
       by Tag to view all IP addresses that contain the tag you
       specify.

       You can view the results for an exact or partial match for your query.
       You can optionally limit the search to a specific region or select
       All Regions. 

       ![]()
    3. Select the number in the IPs column to view the
       IP addresses that the Cloud Identity Engine has collected for the
       selected Tag.
    4. Search by IP Address then close the window or
       click Cancel after reviewing the IP addresses.

       ![]()
    5. Select the IP To Tag tab to Search by
       IP Address.

       For an AWS-based configuration, you can also
       search by VPC ID.

       ![]()
    6. Click the number in the Tags column to view the
       tags associated with the IP Address of that
       row.
    7. Search by Tag then close the window or click
       Cancel after reviewing the tags.

       ![]()

       **Next Steps:** 
       - [View Mappings and Tags](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/view-data-collected-by-cloud-identity-engine/view-mappings-and-tags.html) that the Cloud Identity
         Engine collects.
       - Use Strata Cloud Manager, PAN-OS, or Panorama to
         automatically tag IP addresses for [dynamic tag
         management](https://docs.paloaltonetworks.com/network-security/security-policy/administration/objects/addresses/register-ip-addresses-and-tags-dynamically).

---

<a id="view-mappings-and-tags"></a>

##### View Mappings and Tags

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/view-mappings-and-tags>*

Learn how you can use the Cloud Identity Engine to view mappings and tags from your
firewalls.

After you activate and configure User Context, you can view the mappings and tags
that the Cloud Identity Engine collects from the firewalls that you assign to the
segments. Being able to view all of the mapping and tag information that the Cloud
Identity Engine collects from across your network allows you to quickly locate
specific information for remediation or troubleshooting. By giving you a single
source where you can view all the identity information that your firewalls provide,
as well as efficiently search to find the data you need, you can identify and
address issues more quickly.

1. Select User ContextMappings and Tags.

   You must activate and configure User Context before you can view mappings and
   tags.
2. Select the type of mapping or tag that you want to view.

   - User-ID—View User-ID IP address-to-username
     mappings by Username or IP
     address.
   - User Tags—View [Dynamic User Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-dynamic-user-groups-in-policy) tags by
     Username or by
     Tag.
   - IP Tags—View [Dynamic Address Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically) tags by
     IP address or by
     Tag.
   - IP-Port User—(Terminal Server agent only) View
     Terminal Server agent port range-to-username mappings by
     IP address.
   - Host IDs—(GlobalProtect only) View devices (both
     quarantined and not quarantined) by Host ID.

   ![]()
3. Filter the search results to highlight the information you want to find.

   - Search for specific information you want to find
     by entering a keyword or keywords and pressing Enter or clicking
     Apply Search. 

     ![]()
   - Select a segment from the list to search only that segment or search all
     segments by selecting Segments: All. 

     ![]()
   - Toggle how the column information displays (in
     ascending or descending order).

     ![]()

---

<a id="configure-dynamic-privilege-access-in-the-cloud-identity-engine"></a>

##### Configure Dynamic Privilege Access in the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine>*

Learn how to configure the Dynamic Privilege Access (DPA) capability in the Cloud
Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Enabling Dynamic Privilege Access (DPA) allows you to isolate network resources so
they are only accessible to users on a per-project basis.

Contact your Palo Alto Networks account representative to
activate this functionality.

Complete the following steps to enable and configure DPA in the Cloud Identity
Engine. For more information, refer to the [Prisma Access documentation](https://docs.paloaltonetworks.com/prisma-access/administration/configure-dynamic-privilege-access-settings). The [Prisma Access release notes](https://docs.paloaltonetworks.com/prisma-access/release-notes/5-1/prisma-access-about/prisma-access-known-issues) have
information on known issues for DPA.

Syncing new user groups for SAML applications in Azure may
require up to 3 hours for the Cloud Identity Engine to complete the sync. Wait until
the sync is complete before assigning projects to the new group.

1. Configure an authentication type in the Cloud Identity Engine.

   The authentication type you configure in the Cloud
   Identity Engine is only for use with DPA authentication; don't use the same
   authentication type you use for DPA for another authentication type.

   1. In the Cloud Identity Engine, select Authentication Types Add New Authentication Type.

      The Cloud Identity Engine supports Azure Active Directory (Azure AD)
      in this release. To use an existing Azure IdP configuration, select Authentication TypesActionsEdit.
   2. If you Set Up a new SAML
      2.0 authentication type, [configure](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine) Azure as the
      identity provider (IdP) in a new configuration.

      If you edit the configuration for an
      existing Azure IdP authentication type, [synchronize all attributes](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances)
      for the directory (also known as a full sync) after editing and
      submitting the configuration.
   3. Select Dynamic service provider metadata as the
      Metadata Type.

      ![]()
2. Copy and save the information from the Cloud Identity Engine that you must
   configure in your identity provider.

   Select one of the following methods to obtain the information you need to
   configure for the Cloud Identity Engine to communicate with your identity
   provider:

   - Copy the Entity ID and the Assertion
     Consumer Service URL, then save them in a secure
     location.

     Don't edit the Entity ID or
     use the Entity ID for other applications. You don't need to download
     the SP metadata if you use the Entity ID.
   - Click Download SP Metadata and save the metadata
     in a secure location. For more information, refer to the first step in
     the procedure for [configuring Azure as an IdP](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine) in
     the Cloud Identity Engine.

     This step is
     mandatory for successful DPA configuration using SP metadata, even
     if you edit an existing Azure IdP configuration. The SP metadata
     provides the Entity ID, the Reply URL (Assertion Customer Service
     URL) and the Logout URL; you must manually enter the Sign on URL.

     ![]()

   If you want to configure the authentication type so
   you can obtain the necessary information and you don't want to enter the
   metadata now, you can choose to Do It Later. This
   option allows you to generate the data you need to enter in the IdP for the
   next steps; however, you must enter the metadata before submitting the
   configuration to successfully use the authentication type with the Cloud
   Identity Engine.
3. In the IdP administrator portal, download the SAML application for the Cloud
   Identity Engine from the gallery.
   1. Log in to the Azure Portal and select Enterprise
      Applications.

      ![]()
   2. Search for the Palo Alto Networks Cloud Identity Engine -
      Cloud Authentication Service gallery application and
      select it.

      ![]()
   3. (Optional) Edit the application Name.
   4. Create the configuration.

      ![]()
   5. For Set up single sign-on, click Get
      started.

      ![]()
4. Depending on the method you used in step [2](#configure-dynamic-privilege-access-in-the-cloud-identity-engine), complete the necessary steps to
   configure the SAML application.

   - If you copied the Entity ID and Assertion Consumer Service URL:
     1. Edit the Basic SAML
        Configuration you created.

        ![]()
     2. Click Add identifier and paste the
        Entity ID you copied from the Cloud
        Identity Engine. 

        ![]()
     3. Click Add reply URL and paste the
        Assertion Consumer Service URL you
        copied from the Cloud Identity Engine. 

        ![]()
     4. Enter your regional endpoint as the Sign on
        URL using the following format:
        https://<RegionUrl>.paloaltonetworks.com/sp/acs
        (where <RegionUrl> is your regional
        endpoint). For more information on regional endpoints, see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html).
     5. Save your configuration.
     6. Close the window and
        Copy the App Federation
        Metadata URL.
   - If you downloaded the SP metadata:
     1. Click Upload metadata file to upload the
        SP metadata file from the Cloud Identity Engine. 

        ![]()
     2. Browse to the SP metadata file you
        downloaded from the Cloud Identity Engine.
     3. Add the file.
     4. Edit the Basic SAML
        Configuration you created.

        ![]()
     5. Enter your regional endpoint as the Sign on
        URL using the following format:
        https://<RegionUrl>.paloaltonetworks.com/sp/acs
        (where <RegionUrl> is your regional
        endpoint). For more information on regional endpoints, see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html).
     6. Save your configuration.
     7. Close the window and
        Copy the App Federation
        Metadata URL.
5. Assign your account to the application and save the configuration.
   1. Assign your account to ensure your access to the application and to any
      other users you want to authenticate using the SAML application. For
      more information, refer to step 3 in [configuring Azure as an
      IdP](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine).
   2. Save the configuration.
6. Continue the IdP configuration in the Cloud Identity Engine.
   1. Enter the remaining information to [configure your identity
      provider](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine) (refer to step 5).
   2. In the Cloud Identity Engine, enter the App Federation
      Metadata URL you copied as the Identity
      Provider Metadata URL .
   3. Click Get URL to confirm the Cloud Identity
      Engine can connect to the URL.

      This step is mandatory to confirm the
      configuration. If you don't click Get URL
      before clicking Test SAML Setup, the test
      isn't successful.
   4. Select whether Multi-factor Authentication is Enabled on the
      Identity Provider and whether you want to
      Force Authentication.

      Refer to steps 6-7 in [Configure Azure as an IdP in the
      Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine) for more information.
7. Configure the SAML attributes for the Cloud Identity Engine to use for
   authentication.
   1. Click Test SAML Setup to verify the
      configuration.
   2. Select the Username Attribute for the Cloud
      Identity Engine to use for authentication.

      Select the username attribute that uses the
      Name
      (/identity/claims/name:) format. If
      you do not select the correct username attribute, user
      authentication for projects is not successful. For more information,
      refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/the-role-of-claims).

      ![]()
   3. (Optional) Select other attributes to use for authentication, such as
      Usergroup Attribute, Access
      Domain, User Domain, and
      Admin Role.
8. If you have not already done so, Collect enterprise
   applications data from your [Azure directory](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type/configure-a-cloud-based-directory/set-up-azure). Sign
   in to confirm the changes and Submit the
   update to the configuration.

   The Cloud Identity Engine begins a complete synchronization of the attributes
   (also known as a [full sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances)) when you submit the
   configuration. Wait until the sync is complete before continuing.

   This step is mandatory to complete the configuration
   regardless of whether you're creating a new configuration or editing an
   existing configuration. You must complete this step before enabling Dynamic
   Privilege Access in the Cloud Identity Engine.
9. Enable Dynamic Privilege Access in the Cloud Identity Engine authentication
   profile.
   1. Select Enable Dynamic Privilege Access.
   2. Click Detect Directory and SAML  to allow the
      Cloud Identity Engine to detect available directories and SAML
      attributes.

      When the Cloud Identity Engine completes the collection of the
      attributes, the Directory and SAML
      2.0 Application information displays.

      If the Cloud Identity Engine can't detect the SAML application,
      complete a [full sync](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-instances/synchronize-cloud-identity-engine-instances) then reattempt
      this step.
   3. After confirming the information is correct,
      Submit the configuration.
10. Configure an [authentication profile](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile) in the Cloud
    Identity Engine to use the authentication type you configured.

---

<a id="configure-the-secrets-vault"></a>

##### Configure the Secrets Vault

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/configure-the-secrets-vault>*

Learn how to configure the password vault in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Early in computing history, sensitive information (such as passwords and
cryptographic keys) was usually stored in easily accessible locations, such as
plaintext files or in the code itself. In addition, passwords were often reused in
multiple locations and shared with colleagues using unencrypted methods. These
behaviors could expose organizations to significant security risks by leaving
sensitive data vulnerable to theft and misuse. When cyberattacks such as data
breaches and hacking became more advanced and frequent, organizations needed to
provide better security measures to protect their data.

One method of protecting this critical information is by using secrets vaults. A
secrets vault:

- Provides a centralized and secure storage method for sensitive information
  that can integrate with security and engineering processes.
- Encrypts data for security.
- Uses granular access to control who can view or change the information.
- Logs activity for auditing purposes.

Using secrets vaults helps organizations reduce their attack surface, ensure
compliance with regulations, and manage sensitive information more easily.

1. Configure user roles for the vault.

   A superuser has full privileges for the secrets
   vault, including initialization, adding secrets and collections, and vault
   deletion.

   1. Configure [roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) for users as needed.

      - Vault Administrator—Grants all secrets
        vault access privileges to the user, including initialization,
        adding secrets and collections, and vault deletion.
      - Vault View Only Administrator—Grants
        view-only secrets vault privileges to the user, enabling them to
        view all secrets vault data.

      Vault roles are add-on roles to the
      existing Common Services [roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions). You must configure
      them in combination with current roles. A standalone vault role
      can’t log in to the Cloud Identity Engine.
   2. As you add new users, configure roles as necessary.
2. Log in to the Cloud Identity Engine.
3. If you have not already done so, configure users and groups using the following
   methods:

   - [Configure an On-Premises Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory.html)
   - [Configure a Cloud-Based Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory.html)
   - [Configure a CIE Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html)
4. Select Secrets Vault.

   ![]()
5. If this is the first time using the secrets vault, complete the initial
   configuration.
   1. Click Activate the Secrets Vault.

      ![]()
   2. Click Create Secret.

      ![]()
6. Configure a secret.
   1. Enter the Secret Name.

      ![]()
   2. Enter the URLs that require this secret.

      Enter the URLs in standard [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) URI format (for
      example, https://www.example.com). You can
      configure up to 100 URLs for a single secret.
   3. Enter the Username.
   4. Enter the Password.

      Click the View Password (

      ![]()

      ) button to toggle visibility for
      the password. 

      ![]()
   5. Select the Collections if you have configured
      them.

      If you have not configured any collections, you can do so in the next
      step.
   6. (Optional) Enter a Note.

      You can enter up to 1,000 characters for the note.
   7. Grant Access to specific users or groups by
      specifying a user and access level.

      ![]()

      - View and Use—Users can view and use the
        secret.
      - Full Access—Users can add, edit, or
        delete the secret.
      - Use Only—Users can use the secret.If there are no options available, refer to step [3](#configure-the-secrets-vault).
   8. Click Save.
7. (Optional) Configure a collection.

   A collection lets you share secrets with specific users and groups.

   1. Select the Collections tab.

      ![]()
   2. If you have not created a collection before, click Create
      Collection. Otherwise, click Add
      Collection.
   3. Enter the Collection Name.

      ![]()
   4. Select the Secrets you want to include in the
      collection.

      You can configure up to 500 secrets for a collection.
   5. (Optional) Enter a Note with additional
      information.
   6. Grant Access by specifying users or groups and
      selecting the access type.
   7. Click Save.
8. Associate a secret with a collection.
   1. Select the secret.
   2. Click Edit.

      ![]()
   3. Select the Collections you want to associate
      with the secret.
   4. Click Save.
9. Find more information about secrets and collections.

   - Select a secret and click the Details tab to see
     associated collections, users and groups that can access the secret, and
     what type of access they have. 

     ![]()
   - Click the Look up for a user tab to enter a
     search query for a specific user who has access to the selected secret.

     ![]()
   - Click the Collections tab and select a collection
     to view Details for the collection, including the
     number and names of associated secrets and when the secrets were added.

     ![]()
   - View People with access to this collection by
     entering a search query and selecting a user. 

     ![]()
10. Manage the secrets vault.

    - Search the secrets vault by entering the search query. You can use
      filters to search by secret name, URL, or username. You can also specify
      which collections to search or search by creator name. 

      ![]()
    - Edit a secret by clicking the Edit (

      ![]()

      ) button. You
      can also select the secret then click Edit.
    - Delete a secret by clicking the Delete (

      ![]()

      ) button and confirming the
      deletion.
    - Change the password for a secret by selecting the secret, clicking
      Edit, and then, clicking Change
      Password. Enter the new password and click
      Save. 

      ![]()
    - Delete the secrets vault by clicking the Options button, selecting
      Delete Vault, and confirming the deletion.

      This action deletes the
      entire vault, including secrets and collections. To ensure
      continuation of services, verify that you have configured an
      alternate authentication method for any secrets vault users before
      completing this action.

      ![]()
11. Manage the collections.

    - Search the collections by entering the search query. You can use
      filters to search by collection name or search by creator name. 

      ![]()
    - Edit a collection by clicking the Edit (

      ![]()

      ) button. You
      can also select the collection then click
      Edit.
    - Delete a collection by clicking the Delete (

      ![]()

      ) button and confirming the
      deletion.

---

<a id="manage-the-cloud-identity-agent"></a>

#### Manage the Cloud Identity Agent

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent>*

Update your Cloud Identity agent, stop or restart the
connection between the agent and the Cloud Identity Engine, troubleshoot
issues, and manage certificates.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Agent serves as the critical bridge between your on-premises
infrastructure—such as Active Directory or OpenLDAP—and the Cloud Identity Engine. By
securely collecting and synchronizing user, group, and computer attributes, the agent
ensures that your Palo Alto Networks cloud-based applications possess the necessary
identity context to enforce granular security policies. Once you have installed and
authenticated the agent, ongoing management is required to maintain the health of this
connection, ensure data accuracy, and uphold security standards.

Effective agent management involves several key operational tasks. To monitor the health
of the synchronization process or troubleshoot connectivity errors, you can configure
the agent to generate detailed debug logs, which record events such as new connections
or authentication failures. Maintaining the security of the communication channel is
also paramount; this includes managing and rotating the certificates used for mutual
authentication between the agent and the cloud service.

Furthermore, you must ensure the agent software remains current. The Cloud Identity
Engine app notifies you when updates are available, allowing you to install the latest
version to benefit from new features and security patches. For operational maintenance,
you may need to temporarily stop the agent's connection to the cloud service without
uninstalling it, or completely remove the agent if a server is being decommissioned.

Start managing the Cloud Identity Agent by [configuring Cloud Identity Agent Logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs.html).

---

<a id="configure-cloud-identity-agent-logs"></a>

##### Configure Cloud Identity Agent Logs

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs>*

Learn how to set the Cloud Identity agent log level to
track events on the agent host for troubleshooting.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity agent logs Cloud Identity
Engine events that occur on the agent host. You can use these logs
to monitor informational events such as new connections (Information—New connection 192.0.2.0: 49161),
or for troubleshooting (Error—Verification of Server Cert failed, stopping Cloud Identity Agent).
For example, the agent automatically generates logs if you test
connectivity when you [Configure the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/configure-the-cloud-identity-agent.html#id17CFA0ZN0XI). You can also
use the Event Viewer on the agent host to review logs created if
the agent is unable to connect to the Cloud Identity Engine due
to an incorrect bind DN or password, server unavailability, or other
issue.

The agent displays logs in the order in which they
were generated. To provide a consistent timestamp across timezones,
logs include the timezone information in Coordinated Universal Time (UTC),
where the time offset is indicated by + or -. For the complete log
history, check the CloudIdAgentDebug log file on the agent host,
which permanently retains all logs.

1. Launch the agent.
2. Select FileDebug.
3. Select the type of event you want to log.

   The agent logs the events of the selected type and all
   subsequent types. For example, if you select Debug,
   the logs include error, warning, information, and debug events.

   - If you select None, the
     Cloud Identity agent does not log events at any level.
   - If you select Information, Warning,
     or Error, the agent deletes the data from
     the log after sending it to the debug log on the agent host.
   - If you select Debug or Verbose,
     the received data is stored permanently on the disk until you delete
     the files.

   To remove log files from the agent’s user interface, you
   can optionally [Clear Cloud Identity Agent Logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs/clear-cloud-identity-agent-logs.html#id183MF0V0L65).

---

<a id="search-cloud-identity-agent-logs"></a>

###### Search Cloud Identity Agent Logs

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs/search-cloud-identity-agent-logs>*

To troubleshoot issues with the Cloud Identity
Engine, use keywords to search the Cloud Identity agent logs. For
example, you could search for the IP address of a directory where
the agent wasn’t able to connect to learn more about why the error occurred.

Search
terms are case-sensitive.

1. From the Cloud Identity agent, select Monitoring.
2. Enter the search terms in the entry field to the left
   of Search.
3. Click Search. The results are
   highlighted in blue below the entry field.

   ![]()

---

<a id="clear-cloud-identity-agent-logs"></a>

###### Clear Cloud Identity Agent Logs

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs/clear-cloud-identity-agent-logs>*

Learn how to clear the logs on the user interface of
the Cloud Identity agent.

You can clear outdated logs on the agent’s
user interface. This does not delete the entries from the CloudIdAgentDebug
log file on the agent host.

1. From the Cloud Identity agent, select Monitoring.
2. Click Clear Log.

---

<a id="update-the-cloud-identity-agent"></a>

##### Update the Cloud Identity Agent

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/update-the-cloud-identity-agent>*

If you are not using the latest version of the Cloud
Identity agent, learn how to update to the latest available version.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Using the latest version of the agent is strongly
recommended. If your Cloud Identity agent is not the latest version
available, the Cloud Identity Engine app displays a notification.

Use
the following procedure to update your Cloud Identity agent to the
latest version.

When you upgrade the agent to version
1.7.0, it creates a backup of the existing agent configuration before
removing the deprecated version of the agent. During installation
of the new version of the agent, the existing configuration is automatically
restored.

1. [Stop](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service.html#id1818J060VBD) the connection
   to the Cloud Identity Engine service.

   You must stop the connection between the agent and the
   service before you can update the agent. Check Agents
   & Certificates in the Cloud Identity Engine app
   to confirm the agent’s status.
2. Uninstall the outdated agent from the host (StartControl PanelPrograms and FeaturesCloud Identity
   AgentUninstall).

   You must uninstall the outdated agent
   from the host before installing the latest version of the agent.
3. Log in to the [hub](https://apps.paloaltonetworks.com) and select the Cloud
   Identity Engine app.
4. Select your Cloud Identity Engine tenant (if you have
   more than one) then select Agents & Certificate.
5. Click Download New Agent, then [Install the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/install-the-cloud-identity-agent.html#id17CFA0U0B4X).

   ![]()

---

<a id="start-or-stop-the-connection-to-the-cloud-identity-engine"></a>

##### Start or Stop the Connection to the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service>*

To prevent the Cloud Identity agent from communicating
with the Cloud Identity Engine, you can stop and then restart the
communication later.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

When you start the Cloud Identity agent, it
automatically starts communicating with the Cloud Identity Engine
to synchronize the attributes. To prevent this communication (for
example, if a directory server is unavailable or if you want to [Remove the Cloud Identity Agent](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/remove-the-cloud-identity-agent.html#ide32f74ea-6dad-4d31-b5c0-651cdf2d2ae8)), you can
stop communication between the Cloud Identity agent and the Cloud
Identity Engine. You can then restart the connection later to allow
communication.

1. On the agent host, start the Cloud Identity agent
   if it is not already running, then select Cloud Identity
   Configuration.

   The current connection status of the agent displays at
   the lower-left corner of the window.

   ![]()
2. Stop or re-establish the connection between the agent
   and the service.
   - To connect the agent to the Cloud Identity Engine,
     click Start.

     ![]()
   - To prevent the agent from communicating with the Cloud Identity
     Engine, click Stop.

     ![]()

---

<a id="remove-the-cloud-identity-agent"></a>

##### Remove the Cloud Identity Agent

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/remove-the-cloud-identity-agent>*

If you no longer need a Cloud Identity agent, remove
it from your Cloud Identity Engine tenant.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you no longer need a Cloud Identity agent,
you can remove it from your Cloud Identity Engine tenant.

1. [Stop](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service.html#id1818J060VBD) the connection
   to the Cloud Identity Engine.

   You must stop the connection between the agent and the
   Cloud Identity Engine before you can remove the agent.
2. Uninstall the agent from the host server (StartControl PanelPrograms and FeaturesCloud Identity
   AgentUninstall).
3. Log in to the hub and select the Cloud Identity Engine
   tenant that contains the agent you want to remove.
4. Select Agents & Certificates.
5. Confirm that the agent’s Status is
   Offline and click Remove
   Agent.

   You can only remove an agent that is offline (the connection between the
   agent and the Cloud Identity Engine is not active). If the agent is not
   offline, the Remove Agent button is not
   available.

   ![]()

---

<a id="manage-cloud-identity-engine-certificates"></a>

##### Manage Cloud Identity Engine Certificates

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

After you generate the certificate to [Authenticate the Agent and the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html#id17CKFM00EIA), you can view
the certificate and its associated agent in the Cloud Identity Engine
app.

The Cloud Identity agent version 1.5.0 and later versions
automatically renews the certificate before it expires.

You can view the identification number and lifetime of the certificate
on the Agents & Certificates page in
the Cloud Identity Engine app.

If you need to [Remove Cloud Identity Agent Certificates](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates/revoke-cloud-identity-agent-certificates.html#id1818H0W70U7), you must [Delete Obsolete Cloud Identity Agent Certificates](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates/delete-obsolete-cloud-identity-agent-certificates.html#id188NK0604H4) before you
generate and install the new certificate.

To generate a new certificate for an agent, click Get
New Certificate, then follow the steps to [Authenticate the Agent and the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html#id17CKFM00EIA).

![]()

---

<a id="remove-cloud-identity-agent-certificates"></a>

###### Remove Cloud Identity Agent Certificates

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates/revoke-cloud-identity-agent-certificates>*

If the Cloud Identity agent’s certificate is compromised, remove the compromised
certificate and generate a new certificate.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If a Cloud Identity agent’s certificate is compromised, remove the
certificate.

1. Log in to the [hub](https://apps.paloaltonetworks.com) and select Cloud Identity Engine.
2. Select the tenant associated with the agent with the
   compromised certificate.
3. From the Cloud Identity Engine app, select Agents &
   Certificates.
4. Remove the certificate.

   ![]()
5. [Delete Obsolete Cloud Identity Agent Certificates](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates/delete-obsolete-cloud-identity-agent-certificates.html#id188NK0604H4) to remove
   the previous certificate.
6. Generate a new certificate to [Authenticate the Agent and the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html#id17CKFM00EIA) and install
   it on the agent host.

---

<a id="delete-obsolete-cloud-identity-agent-certificates"></a>

###### Delete Obsolete Cloud Identity Agent Certificates

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-agent/manage-cloud-identity-engine-certificates/delete-obsolete-cloud-identity-agent-certificates>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

You must delete the previous certificate for
the agent before installing the new certificate. If you do not delete
the previous certificate, the Cloud Identity Engine may reference
the previous certificate instead of the new certificate.

1. On the agent host, open Microsoft Management Control
   (MMC) by selecting StartRun,
   then entering MMC.
2. Select FileAdd/Remove
   Snap-In.

   ![]()
3. Select CertificatesAdd.

   ![]()
4. Select Computer AccountNext.

   ![]()
5. Select Local ComputerFinish.

   ![]()
6. Click OK, then navigate to Console RootCertificates (Local
   Computer)PersonalCertificates.

   ![]()
7. Select the previous certificate from the list.
8. Right-click the certificate, then Delete and
   click Yes to confirm the deletion.
9. Generate a new certificate to [Authenticate the Agent and the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-an-on-premises-directory/authenticate-cloud-identity-agent-and-the-cloud-identity-engine.html#id17CKFM00EIA) and install
   it on the agent host.

---

<a id="associate-the-cloud-identity-engine-with-palo-alto-networks-apps"></a>

#### Associate the Cloud Identity Engine with Palo Alto Networks Apps

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance>*

Associate your Cloud Identity Engine tenant with other Palo Alto Networks apps to
allow them to reference your directory data.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The following procedures describe the steps for the support account view in
the Hub. If you are using the tenant account view, association is not
necessary for a tenant service group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information, refer
to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

By associating your Cloud Identity Engine tenants with other Palo Alto Networks apps,
you can allow these apps and services to access your directory information for
reporting and policy enforcement. You can associate the Cloud Identity Engine tenant
with another app during activation or with an existing app at any time.

To share user attributes with multiple apps, associate the same Cloud Identity
Engine tenant with each app.

- [During Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-during-activation.html#id5ddfedb7-92e3-4202-ab1f-327bf0b62415)
- [Existing App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-with-an-existing-app.html#ida0515c5c-ad7f-474f-b028-b4cd164ce9c6)

#### Associate the Cloud Identity Engine During Activation

Learn how to associate the Cloud Identity Engine with
other Palo Alto Networks apps during tenant activation.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Using your Auth Code, [activate](https://docs.paloaltonetworks.com/cortex/cortex-hub/cortex-hub-getting-started/get-started/activate-applications.html) the Palo Alto
   Networks cloud app you want to associate with the Cloud Identity
   Engine tenant.

   ![]()
2. Enter the information required to activate the application, such
   as an Instance Name and a Region,
   which will vary depending on the app.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app.

   Only
   Cloud Identity Engine tenants that are compatible with the Palo
   Alto Networks cloud application are displayed in the drop-down list.
   For example, a Cloud Identity Engine tenant assigned to the US region
   would be compatible with another Palo Alto Networks cloud service
   app assigned to the US region. If the Cloud Identity Engine field
   is not available, the Palo Alto Networks cloud services app you
   selected does not support the Cloud Identity Engine.
4. Agree and Activate the app.

#### Associate the Cloud Identity Engine with an Existing App

Learn how to associate the Cloud Identity Engine with
an existing app on the hub.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Log in to the hub, click Settings (

   ![]()

   ) then Manage
   Apps.
2. Select the app you want to associate with the Cloud Identity Engine
   tenant.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app and click OK.

   ![]()

   Only Cloud
   Identity Engine tenants that are compatible with the Palo Alto Networks
   cloud application are displayed in the drop-down list. For example,
   a Cloud Identity Engine tenant assigned to the US region would be
   compatible with another Palo Alto Networks cloud service app assigned
   to the US region. If the Cloud Identity Engine field is not available,
   the Palo Alto Networks cloud services app you selected does not
   support the Cloud Identity Engine.

   After you associate the
   app, the Cloud Identity Engine tenant name displays in the Cloud
   Identity Engine column in the hub (SettingsManage Apps).

---

<a id="associate-the-cloud-identity-engine-with-palo-alto-networks-apps-1"></a>

##### Associate the Cloud Identity Engine with Palo Alto Networks Apps

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-during-activation>*

Associate your Cloud Identity Engine tenant with other Palo Alto Networks apps to
allow them to reference your directory data.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The following procedures describe the steps for the support account view in
the Hub. If you are using the tenant account view, association is not
necessary for a tenant service group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information, refer
to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

By associating your Cloud Identity Engine tenants with other Palo Alto Networks apps,
you can allow these apps and services to access your directory information for
reporting and policy enforcement. You can associate the Cloud Identity Engine tenant
with another app during activation or with an existing app at any time.

To share user attributes with multiple apps, associate the same Cloud Identity
Engine tenant with each app.

- [During Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-during-activation.html#id5ddfedb7-92e3-4202-ab1f-327bf0b62415)
- [Existing App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-with-an-existing-app.html#ida0515c5c-ad7f-474f-b028-b4cd164ce9c6)

##### Associate the Cloud Identity Engine During Activation

Learn how to associate the Cloud Identity Engine with
other Palo Alto Networks apps during tenant activation.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Using your Auth Code, [activate](https://docs.paloaltonetworks.com/cortex/cortex-hub/cortex-hub-getting-started/get-started/activate-applications.html) the Palo Alto
   Networks cloud app you want to associate with the Cloud Identity
   Engine tenant.

   ![]()
2. Enter the information required to activate the application, such
   as an Instance Name and a Region,
   which will vary depending on the app.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app.

   Only
   Cloud Identity Engine tenants that are compatible with the Palo
   Alto Networks cloud application are displayed in the drop-down list.
   For example, a Cloud Identity Engine tenant assigned to the US region
   would be compatible with another Palo Alto Networks cloud service
   app assigned to the US region. If the Cloud Identity Engine field
   is not available, the Palo Alto Networks cloud services app you
   selected does not support the Cloud Identity Engine.
4. Agree and Activate the app.

##### Associate the Cloud Identity Engine with an Existing App

Learn how to associate the Cloud Identity Engine with
an existing app on the hub.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Log in to the hub, click Settings (

   ![]()

   ) then Manage
   Apps.
2. Select the app you want to associate with the Cloud Identity Engine
   tenant.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app and click OK.

   ![]()

   Only Cloud
   Identity Engine tenants that are compatible with the Palo Alto Networks
   cloud application are displayed in the drop-down list. For example,
   a Cloud Identity Engine tenant assigned to the US region would be
   compatible with another Palo Alto Networks cloud service app assigned
   to the US region. If the Cloud Identity Engine field is not available,
   the Palo Alto Networks cloud services app you selected does not
   support the Cloud Identity Engine.

   After you associate the
   app, the Cloud Identity Engine tenant name displays in the Cloud
   Identity Engine column in the hub (SettingsManage Apps).

---

<a id="associate-the-cloud-identity-engine-with-palo-alto-networks-apps-2"></a>

##### Associate the Cloud Identity Engine with Palo Alto Networks Apps

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-with-an-existing-app>*

Associate your Cloud Identity Engine tenant with other Palo Alto Networks apps to
allow them to reference your directory data.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The following procedures describe the steps for the support account view in
the Hub. If you are using the tenant account view, association is not
necessary for a tenant service group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information, refer
to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

By associating your Cloud Identity Engine tenants with other Palo Alto Networks apps,
you can allow these apps and services to access your directory information for
reporting and policy enforcement. You can associate the Cloud Identity Engine tenant
with another app during activation or with an existing app at any time.

To share user attributes with multiple apps, associate the same Cloud Identity
Engine tenant with each app.

- [During Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-during-activation.html#id5ddfedb7-92e3-4202-ab1f-327bf0b62415)
- [Existing App](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance/associate-the-cloud-identity-engine-with-an-existing-app.html#ida0515c5c-ad7f-474f-b028-b4cd164ce9c6)

##### Associate the Cloud Identity Engine During Activation

Learn how to associate the Cloud Identity Engine with
other Palo Alto Networks apps during tenant activation.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Using your Auth Code, [activate](https://docs.paloaltonetworks.com/cortex/cortex-hub/cortex-hub-getting-started/get-started/activate-applications.html) the Palo Alto
   Networks cloud app you want to associate with the Cloud Identity
   Engine tenant.

   ![]()
2. Enter the information required to activate the application, such
   as an Instance Name and a Region,
   which will vary depending on the app.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app.

   Only
   Cloud Identity Engine tenants that are compatible with the Palo
   Alto Networks cloud application are displayed in the drop-down list.
   For example, a Cloud Identity Engine tenant assigned to the US region
   would be compatible with another Palo Alto Networks cloud service
   app assigned to the US region. If the Cloud Identity Engine field
   is not available, the Palo Alto Networks cloud services app you
   selected does not support the Cloud Identity Engine.
4. Agree and Activate the app.

##### Associate the Cloud Identity Engine with an Existing App

Learn how to associate the Cloud Identity Engine with
an existing app on the hub.

The following procedures describe the steps for
the support account view in the Hub. If you are using the tenant
account view, association is not necessary for a tenant service
group ([TSG](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)). For more information,
refer to the [Hub Getting Started](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) guide.

1. Log in to the hub, click Settings (

   ![]()

   ) then Manage
   Apps.
2. Select the app you want to associate with the Cloud Identity Engine
   tenant.
3. Select the Cloud Identity Engine tenant
   you want to associate with the app and click OK.

   ![]()

   Only Cloud
   Identity Engine tenants that are compatible with the Palo Alto Networks
   cloud application are displayed in the drop-down list. For example,
   a Cloud Identity Engine tenant assigned to the US region would be
   compatible with another Palo Alto Networks cloud service app assigned
   to the US region. If the Cloud Identity Engine field is not available,
   the Palo Alto Networks cloud services app you selected does not
   support the Cloud Identity Engine.

   After you associate the
   app, the Cloud Identity Engine tenant name displays in the Cloud
   Identity Engine column in the hub (SettingsManage Apps).

---

<a id="authenticate-users-with-the-cloud-identity-engine"></a>

#### Authenticate Users with the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Learn how to deploy the Cloud Identity Engine for user authentication by [configuring a SAML 2.0-based identity provider (IdP)](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type.html), a
client certificate and certificate authority (CA) chain, or both. Beyond these
standard methods, the service also supports OpenID Connect (OIDC) providers and
direct Password Authentication for users managed within a Cloud Identity Engine
directory. This flexibility allows you to integrate with major identity services
like Microsoft Entra ID (Azure AD), Okta, Google, PingOne, and PingFederate, or
generic SAML 2.0 compliant providers, ensuring a seamless login experience across
your organization.

After specifying how you want to authenticate your users, set up your authentication
profile to define your authentication security policy. This profile acts as the
logic layer, enabling you to implement multi-authentication strategies where you can
assign different authentication methods to specific user groups or directories
within a single configuration. For example, you might require certificates for
managed devices while prompting contractors for SAML credentials, all managed
through one central policy.

Once your profile is set up, the next step is to tell your firewall or management
tool (Panorama or Strata Cloud Manager) to use it. By linking your management
interface to this cloud-based profile, you separate your security settings from the
technical details of your login provider. This means you can update certificates or
change settings in the cloud without having to manually reconfigure every device in
your network.

Next, set the Cloud Identity Engine as the source for user and group information.
This allows your security rules to automatically adapt whenever users change roles
or departments, enforcing policies based on who the user is rather than their IP
address. This method shifts the heavy lifting of verifying identities from your
physical hardware to the cloud, making your network more efficient and easier to
manage.

---

<a id="set-up-password-authentication"></a>

##### Set Up Password Authentication

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/set-up-password-authentication>*

Find out how to configure password authentication as an authentication type for the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you configure a [CIE directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html) in the Cloud Identity Engine,
you also need to configure an authentication type for those users to enforce
security policy rules. Having to use a third-party identity provider (IdP) to manage
your CIE directory users can be tedious and time-consuming.

Configuring password authentication as an authentication type enables CIE directory
users to authenticate without requiring the use of an external IdP. After you
configure password authentication for your CIE directory, you can select password
authentication as an authentication type in an [authentication profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html). This enables CIE directory users to
authenticate using passwords, instead of having to configure an additional identity
provider.

Enabling password authentication for your CIE directory users simplifies the
authentication process for them by reducing the friction of having to use a separate
IdP to log in. It also simplifies the process for administrators, since they can add
or remove users from the CIE directory without having to configure or revoke
additional privileges.

**Before you begin:**

- [Configure a CIE Directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cie-directory.html).
- Add the password authentication users.

1. Set up password authentication as an authentication type in the Cloud Identity
   Engine.
   1. Select AuthenticationAuthentication Types.
   2. Click Add New Authentication Type.
   3. Set Up the Password
      Authentication type.

      ![]()
2. Create the password authentication configuration.
   1. Enter an Authentication Type Name.

      ![]()
   2. Select a CIE Directory.

      ![]()
   3. Submit the configuration.

**Next Steps:**

- You can now configure password authentication when you [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html).
- [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to combine the capabilities of the Cloud
  Identity Engine with the other Palo Alto Networks apps you use.

---

<a id="set-up-a-saml-20-authentication-type"></a>

##### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

##### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

##### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

##### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

##### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

##### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

##### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

##### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

##### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-1"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-azure-as-an-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-2"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-3"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-pingone-as-an-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-4"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-5"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-google-as-an-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-saml-20-authentication-type-6"></a>

###### Set Up a SAML 2.0 Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine/configure-a-saml-2-0-compliant-idp-in-the-cloud-identity-engine>*

Centralize user verification by configuring SAML 2.0 authentication profiles in the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The Cloud Identity Engine simplifies network security by acting as a central hub for
verifying user identities. Instead of configuring every firewall and security device
to connect directly to your login system—a process that can be complex and
time-consuming—you connect your devices to the Cloud Identity Engine once. When a
user attempts to access a protected resource, the engine acts as a "middleman,"
automatically redirecting the user to your organization's standard login page. Once
the user signs in successfully, the engine confirms their identity to the firewall,
allowing access based on your security rules.

This centralized approach offers significant flexibility, particularly for
organizations that use multiple login systems. For instance, you can configure the
system to have full-time employees log in using one service while contractors or
partners use another, all within a single configuration profile. This ensures a
consistent and secure login experience for all users without requiring you to manage
individual connections on every device in your network.

The Cloud Identity Engine supports the industry-standard SAML 2.0 protocol, allowing
you to easily integrate with major identity providers. Supported integrations
include **Entra ID** (formerly Azure AD), **Okta**, **PingOne**,
**PingFederate**, **Google**, and Idira.

- [Entra ID](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-azure-as-an-idp-in-the-cloud-identity-engine.html#id071d6534-8e31-423d-8d14-d591e2ff5edc)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine.html#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingone-as-an-idp-in-the-cloud-identity-engine.html#id082837d4-22ee-45ab-a9d0-f0b7259febf3)
- [PingFederate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-pingfederate-as-an-idp-in-the-cloud-identity-engine.html#idd35d048d-080a-4edb-a51f-bcb4a6aa5085)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-google-as-an-idp-in-the-cloud-identity-engine.html#id5bfd0401-7a7e-4951-bd1b-72b460ce9342)
- [Idira](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-cyberark-as-an-idp-in-the-cloud-identity-engine.html#configure-cyberark-as-an-idp-in-the-cloud-identity-engine)

<a id="id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c"></a>

###### Configure Azure as an IdP in the Cloud Identity Engine

Learn how to configure Azure as an identity provider
in the Cloud Identity Engine to use as an authentication type for
user authentication.

1. Download the Cloud Identity Engine integration
   in the Azure Portal.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. Log in to the [Azure Portal](https://portal.azure.com) and select Azure
      Active Directory.

      Make sure you complete all the necessary [steps](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/palo-alto-networks-cloud-identity-engine---cloud-authentication-service-tutorial) in the Azure portal.

      ![]()

      If you have more than one directory, Switch
      directory to select the directory you want to use with
      the Cloud Identity Engine.

      ![]()
   3. Select Enterprise applications and click New
      application.

      ![]()
   4. Add from the gallery then enter Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service and [download](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.paloaltonetworksidentityauthentication?tab=overview) the Azure AD single-sign
      on integration.
   5. After
      the application loads, select Users and groups,
      then Add user/group to Assign them
      to this application.

      Select the users and groups you want to use the Azure IdP in the Cloud Identity Engine for
      authentication.

      Be sure to assign the account you're using so you
      can test the configuration when it's complete. You may need to
      refresh the page after adding accounts to successfully complete the
      test.
   6. Select Single sign-on then
      select SAML.
   7. Upload Metadata File by browsing to
      the metadata file that you downloaded from the Cloud Identity Engine
      app and click Add.
   8. After the metadata uploads, Save your
      configuration.
   9. (Optional) Edit your User
      Attributes & Claims to Add a new claim or Edit an
      existing claim.

      If you attempt to test the configuration on the Azure
      Admin Console, a 404 error displays because the test is triggered
      by the IdP and the Cloud Identity Engine supports authentication
      requests initiated by the service provider.
2. Configure Azure AD for the Cloud Identity Engine.
   1. Select Single sign-on then select
      SAML.
   2. Edit the Basic SAML Configuration settings.
   3. Upload metadata file and select the
      metadata file you downloaded from the Cloud Identity Engine in the
      first step.
   4. Enter your regional endpoint as the Sign-on URL using
      the following format: https://<RegionUrl>.paloaltonetworks.com/sp/acs (where <RegionUrl> is your
      regional endpoint). For more information on regional endpoints,
      see [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).
   5. Copy the App Federation
      Metadata Url and save it to a secure location.

      At this point in the process, you may see the option to
      Test sign-in. If you try to test the single
      sign-on configuration now, the test won't be successful. You can test
      your configuration to verify it's correct in step [9](#id071d6534-8e31-423d-8d14-d591e2ff5edc_step-pzr_2zq_j1c).
3. Add and assign users who you want to require to use Azure AD for
   authentication.
   1. Select Azure Active Directory then select UsersAll users.
   2. Create a New user and enter a
      Name, User name.
   3. Select Show password, copy the password to a
      secure location, and Create the user.
   4. In the Palo Alto Networks Cloud Identity Engine - Cloud
      Authentication Service integration in the Azure Portal,
      select Users and groups.
   5. Add user then select Users and
      groups.
4. Add Azure as an authentication type in the Cloud Identity Engine
   app.
   1. In the Cloud Identity Engine app, select AuthenticationAuthentication Types then click Add New Authentication
      Type.

      ![]()
   2. Set Up a SAML 2.0
      authentication type.

      ![]()
   3. Select the Metadata Type you want to use.

      - To use the client credential flow, the auth code flow, or SCIM,
        select Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   4. Copy the Entity ID and Assertion
      Consumer Service URL and save them in a secure
      location.

      ![]()
   5. Download SP Certificate and Download
      SP Metadata and save them in a secure location.

      ![]()
   6. Enter a unique and descriptive Profile
      Name.

      ![]()
   7. Select Azure as your Identity
      Provider Vendor.

      ![]()
5. Select the method you want to use to Add Metadata.

   ![]()

   - If you want to enter the information manually, copy the identity
     provider ID and SSO URL, download the certificate, then enter the
     information in the Cloud Identity Engine IdP profile.
     1. Copy the necessary information from the Azure Portal and enter
        it in the IdP profile on the Cloud Identity Engine app as
        indicated in the following table:

        |

        Copy or Download from Azure Portal | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Azure AD Identifier. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate (Base64). | Click Browse files to select the Identity Provider Certificate you downloaded from the Azure Portal. |

        |

        Copy the Login URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     2. (Optional) Select the HTTP Binding for SSO Request to
        Identity Provider (Optional) method you want to
        use for the SAML binding that allows the firewall and IdP to
        exchange request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.

        ![]()
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Azure Portal, Download the
        Federation Metadata XML and
        Save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     App Federation Metadata Url, then paste it in
     the profile as the Identity Provider Metadata URL
     and click Get URL to obtain the
     metadata.

     Palo Alto Networks recommends using this method to
     configure Azure as an IdP.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.

   ![]()
7. Select Multi-factor Authentication is Enabled on
   the Identity Provider if your Azure configuration uses multi-factor
   authentication (MFA).

   ![]()
8. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
9. Click Test SAML setup to verify the profile
   configuration.

   This step is necessary to confirm that your firewall and IdP can communicate.

   If you do not provide the vendor information,
   the SAML test passes so that you can still submit the configuration.

   ![]()
10. Select the SAML attributes you want the firewall to use
    for authentication and Submit the IdP profile.

    1. In the Azure Portal, Edit the User
       Attributes & Claims.
    2. (Optional) In the Cloud Identity Engine app, enter the Username
       Attribute, Usergroup Attribute,
       Access Domain, User
       Domain, and Admin Role.
    3. Submitthe profile.

    ![]()
11. If you want to Enable Dynamic Privilege Access, ensure
    completion of the prerequisites before enabling this option, then
    Submit your changes to confirm the configuration.

    For more information, refer to [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html).

    ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc"></a>

###### Configure Okta as an IdP in the Cloud Identity Engine

If
you want to use Okta to authenticate users with the Cloud Identity Engine, there are two
ways to configure Okta authentication with the Cloud Identity Engine:

- (Recommended)[Integrate Okta as a Gallery Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
- [Integrate
  Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)

1. Select the method you want to use to integrate the Okta authentication in the
   Cloud Identity Engine and complete the steps in the Okta management console.

   - (Recommended)[Integrate Okta as a Gallery
     Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
   - [Integrate Okta as a Custom Application](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c)
2. Set up the Okta authentication in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationAuthentication Type.
3. Add Okta as an authentication type in the Cloud Identity Engine app.
   1. Set Up a SAML 2.0
      authentication type.

      ![]()
   2. Select the Metadata Type.

      - To use the gallery app, the custom app, or SCIM, select
        Single service provider
        metadata.
      - To [Configure Dynamic Privilege Access in the Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-dynamic-privilege-access-in-the-cloud-identity-engine.html), select
        Dynamic service provider
        metadata.

      ![]()
   3. Copy the Entity ID and store it in a secure
      location.
   4. Copy the Assertion Consumer Service URL and
      store it in a secure location.
   5. Click Download SP Certificate and store it in a
      secure location.
   6. Click Download SP Metadata and store it in a
      secure location.
4. Configure the Okta IDP profile.
   1. Enter a unique and descriptive Profile
      Name.

      ![]()
   2. Select Okta as the Identity Provider
      Vendor.
5. Select the method you want to use to Add Metadata.

   - If you want to enter the information manually, copy the client ID and
     domain, download the SP metadata certificate, then enter the information
     in the Cloud Identity Engine IdP profile.
     1. In the Okta Admin Console, select ApplicationsAPI Service Integrations and select the Palo Alto Networks
        Cloud Identity Engine integration.
     2. Copy the necessary information from the Okta
        Admin Console and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Client ID. | Enter it as the Identity Provider ID. |

        |

        N/A | Click to Upload the SP metadata certificate you downloaded in step [3.e](#tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_substep-hpy_kr4_3hc). |

        |

        Copy the Okta Domain. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from
     your IdP management system.
     1. In the Okta Admin Console, click View Setup
        Info and copy the IDP
        metadata and save it to a secure location.
     2. In the Cloud Identity Engine app, click Browse
        Files to select the metadata file then
        Open the metadata file.

     ![]()
   - If you want to use a URL to retrieve the metadata, copy the
     IDP metadata from step 4.2. Paste it in the
     profile and click Get URL to obtain the metadata.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()
6. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
7. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.
8. Test SAML setup to verify the profile configuration.

   The Test SAML setup option
   is not available until the Cloud Identity Engine validates the identity
   provider profile data.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use for authentication and
   Submit the IdP profile.

   You must select the username attribute in the Okta Admin Console for the
   attribute to display in the Cloud Identity Engine.

   1. In the Okta Admin Console, Edit the
      User Attributes & Claims.
   2. In the Cloud Identity Engine app, select the Username
      Attribute and optionally, the Usergroup
      Attribute, Access Domain,
      User Domain, and Admin
      Role.

      If you're using the Cloud Identity Engine
      for SAML authentication with GlobalProtect Clientless VPN, you must
      configure the User Domain attribute to the
      same value as the userdomain field in the
      Okta Admin Console (ApplicationsApplicationsSAML 2.0General).

   ![]()

<a id="tabs-id4126bb2e-0974-45b8-81da-c13f5db29908_task-qns_qpr_c3c"></a>

###### Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

###### Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

Learn about configruing Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta in the Cloud Identity
Engine as a gallery application. Complete the following steps to add and configure
the Okta gallery application in the Cloud Identity Engine. Be sure to complete all
the steps here and in the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

The Cloud Identity Engine supports [FedRAMP High](https://www.paloaltonetworks.com/security-for/government/fedramp) for the gallery app only.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Browse App Catalog.

   ![]()
3. Search for Palo Alto Networks Cloud Identity Engine and
   select Show all results.

   ![]()
4. Select the Single sign-on version of the Cloud Identity
   Engine app.

   ![]()
5. Click Add Integration.

   ![]()
6. Optionally edit the Application label then click
   Next.

   ![]()
7. Verify that SAML 2.0 is the sign-on option type.

   ![]()
8. If you enabled Force Authentication in step 7, uncheck
   Disable Force Authentication.

   ![]()
9. Edit and paste the SAML Region.

   The SAML Region is based on the Entity ID in the SP Metadata. To obtain the
   SAML Region, enter only the text between the backslash in the Entity ID and
   the paloaltonetworks.com domain. For example,
   if the Entity ID is
   https://cloud-auth.us.apps.paloaltonetworks.com/sp,
   the SAML Region is cloud-auth.us.apps.

   ![]()
10. Select the Application username format that you want to
    use to authenticate the user. For example, Email
    represents the UserPrincipalName (UPN) format.

    ![]()
11. Click Done.
12. (Optional) If you want to configure other attributes in addition to the
    username, refer to the [Okta documentation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Palo-Alto-Networks-Cloud-Identity-Engine.html).

###### Configure Okta as an IdP in the Cloud Identity Engine (Custom)

Learn about configuring Okta as an IdP in CIE.

Palo Alto Networks strongly recommends that you integrate Okta as a gallery
application. However, if you want to configure the Okta integration as a custom
application, complete the following steps.

1. Log in to the Okta Admin Console and select ApplicationsApplications.

   ![]()
2. Click Create App Integration.

   ![]()
3. Select SAML 2.0 as the sign-on method then click
   Next.

   ![]()
4. Enter an App name then click
   Next.

   ![]()
5. Copy the SP Metadata information from the Cloud Identity
   Engine and enter it in the Okta Admin Console as described in the following
   table:

   |

   Copy from Cloud Identity Engine | Enter in Okta Admin Console |

   | --- | --- |

   |  |  |
   | --- | --- |
   |

   Copy the Assertion Consumer Service URL in step 3. | Enter the URL as the Single sign on URL. |

   |

   Copy the Entity ID in step 3. | Enter it as the Audience URI (SP Entity ID). |

   ![]()
6. Specify the Name ID format and optionally the
   Application username.

   You must configure at least one SAML attribute that contains identification
   information for the user (usually the username attribute) for the attributes
   to display in the Cloud Identity Engine. To configure administrator access,
   you must also enter values for the accessdomain
   attribute and for the adminrole attribute that match
   the values on the firewall.

   ![]()
7. Click Finish to save the configuration.

**Next Steps:**

- Learn how to [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to take advantage of more
  capabilities for the Cloud Identity Engine.
- If you have a PAN-OS firewall, find out how to [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html) so you can use the Cloud
  Identity Engine in conjunction with the firewall to strengthen your security
  posture.

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb"></a>

<a id="id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc"></a>

###### Configure PingOne as an IdP in the Cloud Identity Engine

Learn how to configure PingOne as an identity provider
in the Cloud Identity Engine for user authentication.

Configure a profile to configure PingOne as an
identity provider (IdP) in the Cloud Identity Engine. After you
configure the IdP profile, [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8).

1. Enable the Cloud Identity Engine app in PingOne.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingOne and select ApplicationsMy ApplicationsAdd ApplicationNew SAML Application.

      ![]()
   4. Enter an Application Name,
      an Application Description, and select the Category then Continue
      to Next Step.
   5. Select I have the SAML configuration and
      ensure the Protocol Version is SAML
      v 2.0.

      ![]()
   6. Click Select File to Upload
      Metadata

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in PingOne as described in the following table:

      |

      Copy from Cloud Identity Engine | Enter in PingOne |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the Assertion Consumer Service (ACS). |

      ![]()
   8. Select either RSA\_SHA384 or RSA\_SHA256 as
      the Signing Algorithm.

      ![]()
   9. If you want to require users to log in with their credentials to
      reconnect to GlobalProtect, select Force
      Re-authentication.

      ![]()
   10. (Required for MFA) If you want to require multi-factor authentication
       for your users, select Force MFA.
   11. Click Continue to Next Step to specify
       the attributes for the users you want to authenticate using PingOne.
   12. Specify the Application Attribute and
       the associated Identity Bridge Attribute or Literal Value for
       your user then select Required.

       Be sure to assign the account you're using so you can test the configuration when it's
       complete. You may need to refresh the page after adding accounts to
       successfully complete the test.

       ![]()
   13. Click Add new attribute as
       needed to include additional attributes then Continue
       to next step to specify the group attributes.
   14. Add the groups you want to
       authenticate using PingOne or Search for
       the groups you want to add then Continue to next step to
       review your configuration.

       ![]()
2. Add PingOne as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingOne as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingOne, select ApplicationsMy Applications then select
        the Cloud Identity Engine app.
     2. Copy the necessary information from PingOne and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Okta Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Issuer ID. | Enter it as the Identity Provider ID. |

        |

        Download the Signing Certificate. | Click to Upload the certificate from the Okta Admin Console. |

        |

        Copy the Initiate Single Sign-On (SSO) URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. In PingOne, select ApplicationsMy Applications then select the Cloud Identity Engine app.
     2. Download the SAML
        Metadata.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - To use the Get URL method, copy the URL from your
     IdP and enter it in Cloud Identity Engine.
     1. Log in to Ping One using your administrator credentials.
     2. Select Applications then select the
        application you created in step [1.c](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep-xrt_3zy_tbc). 

        ![]()
     3. Copy the SAML Metadata
        URL and save it in a secure location. 

        ![]()
     4. In the Cloud Identity Engine, select Get
        URL and the Add Metadata
        method and paste the URL you copied in the previous step as the
        Identity Provider Metadata URL. 

        ![]()
     5. Click Get URL to confirm the URL and
        populate the Identity Provider ID and
        Identity Provider SSO URL. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile.
4. Select the HTTP Binding for SSO Request to IdP method
   you want to use for the SAML binding that allows the firewall and IdP to
   exchange request and response messages:

   - HTTP Redirect—Transmit SAML messages through URL
     parameters.
   - HTTP Post—Transmit SAML messages using
     base64-encoded HTML.
5. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
6. If your IdP requires users to log in using multi-factor authentication (MFA),
   select Multi-factor Authentication is Enabled on the Identity
   Provider.

   ![]()
7. If you enabled the Force Re-authentication option in
   step [1.9](#id082837d4-22ee-45ab-a9d0-f0b7259febf3_substep_tfl_qff_fxb), enable the
   Force Authentication option to require users to log
   in with their credentials to reconnect to GlobalProtect.

   ![]()
8. Test SAML setup to verify the profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
9. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Okta Admin Console, Edit the User
      Attributes & Claims.
   2. In the Cloud Identity Engine, select the Username Attribute and
      optionally, the Usergroup Attribute,
      Access Domain, User
      Domain, and Admin Role, then
      Submit your changes.

      You must select
      the username attribute in the Okta Admin Console for the attribute
      to display in the Cloud Identity Engine.

   ![]()

###### Configure PingFederate as an IdP in the Cloud Identity Engine

1. Prepare the metadata for the Cloud Identity
   Engine app in PingFederate.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to PingFederate and select SystemSP AffiliationsProtocol MetadataMetadata Export.
   4. Select I am the Identity Provider (IdP) then
      click Next.

      ![]()
   5. Select information to include in metadata manually then
      click Next.

      ![]()
   6. Select the Signing key you
      want to use then click Next.
   7. Ensure that SAML 2.0 is the
      protocol then click Next.
   8. Click Next as you don't need to define an
      attribute contract.
   9. Select the Signing Certificate and that
      you want to Include this certificate’s public key certificate
      in the <key info> element.

      ![]()
   10. Select the Signing Algorithm you want
       to use then click Next.
   11. Select the same certificate as the Encryption certificate then
       click Next.
   12. Review the metadata to verify the settings are correct
       then Export the metadata.

       ![]()
2. Add PingFederate as an authentication type in the Cloud
   Identity Engine app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select PingFederate as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   IdP profile.

   - If you want to enter the information manually, copy
     the identity provider ID and SSO URL, download the certificate,
     then enter the information in the Cloud Identity Engine IdP profile.
     1. In PingFederate, select SystemOAuth SettingsProtocol Settings to
        copy the Base URL and SAML 2.0
        Entity.
     2. Copy the necessary information from PingFederate and enter it in the IdP profile on the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from PingFederate | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the SAML 2.0 Entity ID. | Enter it as the Identity Provider ID. |

        |

        Copy the Base URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. In PingFederate, select SecuritySigning & Decryption Keys & Certificates to Export the certificate
        you want to use.
     4. In the Cloud Identity Engine app, click Browse files to select the
        PingFederate certificate.
     5. Select the HTTP Binding for SSO Request to IdP method you want to use for
        the SAML binding that allows the firewall and IdP to exchange
        request and response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.
     1. Locate the metadata file from the first step.
     2. In the Cloud Identity Engine app, click Browse
        files to select the metadata file, then
        Open the metadata file.

     ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for PingFederate.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   1. In the Cloud Identity Engine, select the Username Attribute.
   2. (Optional) Select the Usergroup Attribute, Access
      Domain, User Domain, and Admin
      Role.

   ![]()

###### Configure Google as an IdP in the Cloud Identity Engine

1. Prepare to configure Google as an IdP
   in the Cloud Identity Engine.
   1. If you have not already done so, [activate](https://docs.paloaltonetworks.com/cortex/directory-sync/directory-sync-getting-started/get-started-with-directory-sync/activate-directory-sync.html) the Cloud Identity
      Engine app.
   2. In the Cloud Identity Engine app, select AuthenticationSP MetadataDownload SP Metadata and Save the
      metadata in a secure location.

      ![]()
   3. Log in to the Google Admin Console and select AppsSAML Apps.

      ![]()
   4. Select Add AppAdd custom SAML app.

      ![]()
   5. Enter an App name then Continue to
      the next step.
   6. Click Download Metadata to Download
      IdP metadata then Continue to
      the next step.

      ![]()
   7. Copy the metadata information from the Cloud Identity Engine
      and enter it in the Google Admin Console as described in the following table
      then Continue to the next step:

      |

      Copy from Cloud Identity Engine | Enter in Google Admin Console |

      | --- | --- |

      |  |  |
      | --- | --- |
      |

      Copy the Entity ID from the SP Metadata page. | Enter it as the Entity ID. |

      |

      Copy the Assertion Consumer Service URL. | Enter the URL as the ACS URL. |
   8. Add mapping to select the Google
      Directory attributes then specify the corresponding App
      attributes. Repeat for each attribute you want to use
      then click Finish when the changes are complete.

      ![]()
   9. View details to specify the
      users and groups you want to authenticate with Google and enable
      the app to turn it ON for everyone then Save your
      changes.

      ![]()
   10. Select DirectoryUsers to specify the users
       you want to authenticate using Google.

       ![]()
2. Add Google as an authentication type in the Cloud Identity Engine
   app.
   1. Select Authentication Types and
      click Add New Authentication Type.

      ![]()
   2. Set Up a SAML 2.0 authentication
      type.

      ![]()
   3. Enter a Profile Name.

      ![]()
   4. Select Google as your Identity
      Provider Vendor.
3. Select the method you want to use to Add Metadata and Submit the
   profile.

   - If you want to enter the information manually, copy the identity provider ID and SSO URL,
     download the certificate, then enter the information in the Cloud
     Identity Engine.
     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata. 

        ![]()
     2. Click Download Metadata then copy the
        necessary information from Google and enter it in the Cloud
        Identity Engine app as indicated in the following table:

        |

        Copy or Download from Google Admin Console | Enter in Cloud Identity Engine IdP Profile |

        | --- | --- |

        |  |  |
        | --- | --- |
        |

        Copy the Entity ID. | Enter it as the Identity Provider ID. |

        |

        Download the Certificate. | Click to Upload the certificate from Google. |

        |

        Copy the SSO URL. | Enter the URL as the Identity Provider SSO URL. |

        ![]()
     3. Select the HTTP Binding for SSO Request to
        IdP method you want to use for the SAML binding
        that allows the firewall and IdP to exchange request and
        response messages:
        - HTTP Redirect—Transmit SAML
          messages through URL parameters.
        - HTTP Post—Transmit SAML messages
          using base64-encoded HTML.
   - If you want to upload a metadata file, download the metadata file from your IdP management
     system.

     The Cloud Identity Engine supports
     metadata file sizes of up to 16 MB.

     1. In the Google Admin Console, select the Cloud Identity Engine
        app and Download Metadata.
     2. Click Download Metadata and
        Save the file to a secure location.
     3. In the Cloud Identity Engine app, click Browse
        files to select the metadata file then
        Open the metadata file. 

        ![]()
   - If you don't want to
     enter the configuration information now, you can Do it
     later. This option allows you to submit the profile
     without including configuration information. However, you must edit the
     profile to include the configuration information to use the
     authentication type in an authentication profile. 

     ![]()

   The
   Cloud Identity Engine does not currently support the Get
   URL method for Google.
4. Specify the Maximum Clock Skew (seconds), which is the
   allowed difference in seconds between the system times of the IdP and the
   firewall at the moment when the firewall validates IdP messages (default is 60;
   range is 1–900). If the difference exceeds this value, authentication
   fails.
5. To require users to log in using their credentials to reconnect to
   GlobalProtect, enable Force Authentication.

   ![]()
6. Test SAML setup to verify the
   profile configuration.

   ![]()

   This step is necessary to confirm that your firewall and IdP can
   communicate.
7. Select the SAML attributes you want the firewall to use
   for authentication and Submit the IdP profile.

   Select the Username Attribute and optionally,
   the Usergroup Attribute, Access Domain, User
   Domain, and Admin Role. 

   ![]()

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile"></a>

###### Configure Idira as an IdP in the Cloud Identity Engine

Set up the Cloud Identity Engine integration with Idira.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- GlobalProtect - NGFW and Panorama - Prisma Access | - Active [Cloud Identity   Engine](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cie-activation) account with required administrator   rights - Cloud Identity Engine users who will access the Idira   Identity User Portal through SSO have been added to   Idira - PAN-OS 11.2 and later |

Configure Idira Identity (formerly CyberArk Identity) as a SAML 2.0 IdP (identity
provider) in the Cloud Identity Engine.

Keep the Cloud Identity Engine and Idira Identity
Admin portal windows open simultaneously to copy and paste settings between the two
browser windows.

1. Log in to the Cloud Identity Engine app.
2. Add Idira as an authentication type.
   1. Select AuthenticationAuthentication Types, and then click Add New Authentication
      Type.
   2. Set Up a SAML 2.0
      authentication type.
   3. For Metadata Type, select Single
      service provider metadata.
   4. Copy the EntityID and Assertion
      Consumer Service URL, and then click Download
      SP Certificate to save a copy of the service provider
      certificate.

      Alternatively, you can Download SP
      Metadata.

      Save this information in a secure place. You will need it to complete
      the service provider configuration in Idira Identity Administration
      portal.
3. Configure an Identity Provider Profile.
   1. For Profile Name, enter
      Idira.
   2. For Identity Provider Vendor, select
      Idira.
   3. Add Metadata manually or using the IdP metadata
      file from Idira.

      To acquire the metadata, complete up to step [3.b](#cie-sso-cyberark_cyberark-sso-url) in [Configure the Cloud Identity Engine Template for SSO in Idira](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark).

      - To enter the metadata, select Enter
        Manually, and then provide the
        following:

        - Identity Provider ID—The
          IdP Entity ID / Issuer from
          Idira
        - Identity Provider
          Certificate—Upload the Signing
          Certificate from Idira
        - Identity Provider SSO URL—The
          Single Sign On URL from
          Idira
      - To upload the IdP metadata file, select Upload
        Metadata, and then drag and drop the file or
        Browse files.
   4. (Optional) Select an HTTP Binding for SSO Request
      to Identity Provider method to use for the SAML
      binding.

      This allows the firewall and IdP to exchange request and response
      messages.
      - HTTP Redirect—Transmit SAML messages
        through URL parameters
      - HTTP Post—Transmit SAML messages
        using base64-encoded HTML
   5. Specify the Maximum Clock Skew (seconds)
      (default is 60; range is 1–900).

      Maximum Clock Skew is the allowed difference in seconds between the
      system times of the IdP and the firewall at the moment when the firewall
      validates IdP messages. If the difference exceeds this value,
      authentication fails.
   6. (Optional) Force Authentication.

      When you enable this option, Idira prompts users for credentials for
      every authentication attempt, even if they have an active single
      sign-on (SSO) session.
4. Verify your Identity Provider profile configuration.

   This step confirms that your NGFW and Idira can communicate.

   If you do not provide the vendor information, the SAML test passes so you
   can still submit the configuration.

   1. In the Test SAML and Attributes section, click Test SAML
      Setup.

      This redirects you to the Idira Identity Provider settings and
      initiates testing. After successful authentication, the configured
      username and any other IdP attributes populate in the Test SAML and
      Attributes window. Only the UserName attribute is mandatory.
   2. Submit your changes.
5. [Set up an Authentication profile to define
   how the Cloud Identity Engine authenticates users](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile).

<a id="cie-sso-cyberark_cyberark-sso-url"></a>

<a id="configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cie-sso-cyberark"></a>

###### Configure the Cloud Identity Engine Template for SSO in Idira

Configure the Cloud Identity Engine application template in the Idira Identity
Administration portal to enable service provider-initiated and identity
provider-initiated single sign-on (SSO) to the Idira Identity User Portal.

1. Log in to the Idira Identity Administration portal.
2. Add the Cloud Identity Engine web app template.
   1. Select Apps & WidgetsWeb Apps, and then click Add Web
      Apps.
   2. Search for Palo Alto Networks
      CIE, and then click
      Add.
   3. Add the Palo Alto Networks
      CIE web app, and then click
      Yes to confirm.
   4. Close the app catalog.

      The Palo Alto Networks CIE template opens to its prepopulated
      Settings page.
3. Configure Trust settings.
   1. On the sidebar, select Trust.
   2. In the Identity Provider Configuration section, collect the Idira
      Identity metadata.

      Save the metadata in a secure location. You will need this
      information to [configure the
      Identity Provider Profile](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_identity-provider-profile) in the Cloud Identity
      Engine app.

      - To populate the profile using an IdP metadata file,
        select Metadata, and then
        click Download Metadata
        File.
      - To enter the metadata, select Manual
        Configuration.
        Copy the IdP
        Entity ID / Issuer and
        Single Sign On URL, and
        then Download the
        Signing Certificate.
   3. In the Service Provider Configuration section, provide the [Cloud Identity Engine
      metadata](#configure-cyberark-as-an-idp-in-the-cloud-identity-engine_cyberark-metadata).

      - To use the SP metadata file, select
        Metadata, and then upload
        the File you downloaded from
        the Cloud Identity Engine.

        The metadata auto-populates.
      - To enter the SP metadata, select Manual
        Configuration, and then provide the
        following:

        - SP Entity ID / SP Issuer /
          Audience—The Entity
          ID from the Cloud Identity Engine
        - Assertion Consumer Service (ACS)
          URL—The Assertion Consumer
          Service URL from the Cloud Identity
          Engine
   4. Validate the metadata, and then Save the
      configuration.
4. Configure the SAML response.
   1. On the sidebar, select SAML Response.
   2. In the Attributes section, verify that the Attribute
      Name maps to the correct Attribute
      Value.

      Specifically, verify that the Login
      Attribute Name maps to the LoginUser.Email
      Attribute Value.

      Attributes are case-sensitive.
   3. (Optional) To map other attributes you want to pass in the
      SAML response, click Add.
   4. Save the configuration.
5. Define permissions for Cloud Identity Engine users, groups, or roles who
   will access the Idira Identity User Portal.

   Assigning permissions grants SSO access to the selected users, groups, or
   roles.

   One user must be an administrator who is mapped to the attribute. The
   user must already exist in CLICDATA.

   1. On the sidebar, select Permissions, and then
      click Add.
   2. Select the users, groups, or roles to grant SSO access, and then
      click Add.

      The added object appears on the Permissions page with
      View, Run, and Automatically Deploy
      permissions selected by default.
   3. Enable permissions for each user, group, or role, and then click
      Save.

      You can change the permissions to add additional control or if you
      prefer not to automatically deploy the application.
6. Review the settings, and then Save your
   configuration.
7. Test the Cloud Identity Engine SSO configuration.

   - To test IdP-initiated SSO:

     1. Sign in to the Idira Identity User Portal with a user
        account you just added.
     2. Click the Palo Alto Networks CIE
        application tile to launch the Cloud Identity Engine in a
        new tab and automatically sign in.
   - To test SP-initiated SSO:

     1. Visit your organization's Cloud Identity Engine SSO
        URL.
     2. Sign in with your Identity
        Provider.

        This redirects you to the Idira Identity User Portal.
        After successfully authenticating to the IdP, you are
        redirected back to the Cloud Identity Engine.

---

<a id="set-up-a-client-certificate"></a>

##### Set Up a Client Certificate

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-a-client-certificate>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Client certificate authentication leverages your organization’s Public Key
Infrastructure (PKI) to verify user identities using digital certificates installed
on their devices. Instead of, or in addition to, standard login credentials, the
Cloud Identity Engine validates the certificate presented by the client against a
configured Certificate Authority (CA) chain.

To implement this, you upload your root and intermediate CA certificates to the Cloud
Identity Engine to establish a chain of trust. You then define how the engine
identifies the user by specifying which field in the certificate—such as the Subject
Common Name (CN) or a Subject Alternative Name (SAN) like an email or User Principal
Name—maps to the username. This method provides a seamless, high-security
authentication option that can be deployed as a primary verification method or
combined with SAML 2.0 identity providers for robust multi-authentication
policies.

To use a client certificate to authenticate users, configure a certificate authority
(CA) and client certificate.

1. Configure a Certificate Authority (CA) chain to authenticate
   users.

   Upload the CA chain, including the root certificate and
   any intermediate certificates, that issues the client certificate.
   The Cloud Identity Engine supports multiple intermediate certificates
   but does not support sibling intermediate certificates in a single
   CA chain.

   1. In the Cloud Identity Engine app, select AuthenticationCA ChainsAdd CA Chain.

      ![]()
   2. Enter the necessary information for the CA chain profile.

      ![]()

      - **CA Name**—Enter a unique name to identify the
        CA chain in the Cloud Identity Engine tenant.
      - **Upload Certificate**—Drag and drop file(s) here or Browse
        files to your CA certificate then Open the
        certificate to select it.

        The file must end in the .crt or .pem file
        extension.
      - **Certificate Revocation List Endpoint (Optional)**—(Optional
        but recommended) Specify the URL for the certificate revocation
        list (CRL) list that you want the Cloud Identity Engine to use to
        validate the client certificate.
   3. Submit the changes to complete
      the configuration.
2. In the Cloud Identity Engine app, select AuthenticationAuthentication TypesAdd New Authentication Type.

   ![]()
3. Select Client CertificateSet Up.

   ![]()
4. Enter a unique Authentication Type Name for
   the client certificate.
5. Select the Username Field that
   you want the Cloud Identity Engine to use to authenticate users.

   Select the Username Field based on
   the attribute type of the client certificate that you want to use
   to authenticate the user; for example, if the username is defined
   in the client certificate using Subject,
   select Subject.

   ![]()
6. Configure the Username Attribute based
   on the previous step and the attribute that your client certificate
   uses to authenticate users.

   - If the Username Field is Subject, the
     Username Attribute is CN.
   - If the Username Field is Subject Alt Name,
     select Email or User Principal
     Name based on the attribute that your client certificate
     specifies.
7. Click Add CA Chain to add one
   or more CA chains to authenticate users.

   ![]()
8. Enter a search term in the Search CA Chain field
   or select a CA chain you previously configured and Add it
   to the configuration.

   The Cloud Identity Engine supports grouping multiple CA
   chains in a certificate type to authenticate client certificates
   issued by multiple CA chains.

   ![]()
9. Submit your changes to configure
   the authentication type.

---

<a id="configure-an-oidc-authentication-type"></a>

##### Configure an OIDC Authentication Type

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/set-up-oidc-authentication>*

Learn how to configure OpenID Connect (OIDC) as an authentication type for the Cloud
Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

OpenID Connect (OIDC) authentication provides a modern, flexible method for verifying
user identities within the Cloud Identity Engine. Built upon the OAuth 2.0
framework, OIDC enables Single Sign-On (SSO), allowing users to access supported
applications and resources after logging in just once. This approach streamlines the
user experience by reducing the frequency of re-authentication prompts while
ensuring that security policies are consistently enforced based on user attributes
collected from the provider.

The Cloud Identity Engine supports OIDC integration with major identity providers,
including **Microsoft Entra ID (Azure AD)**, **Okta**, **PingOne**, and
**Google**. By configuring an OIDC authentication type, you establish a
direct trust relationship that allows the engine to validate credentials and
retrieve identity data. It is important to note that currently, the OIDC
authentication type is supported specifically for the **Prisma Access Browser**
and is not available for use with GlobalProtect or the Authentication Portal.

The OIDC authentication type supports the Prisma® Access
Browser. It does not support GlobalProtect™ or Authentication Portal.

To configure an OpenID Connect (OIDC) provider as an authentication type in the Cloud
Identity Engine, complete the following steps for your identity provider (IdP) type.

When you configure OIDC as an authentication type, the
Cloud Identity Engine determines the username attribute using the following order
(where if the current attribute isn’t found, the Cloud Identity Engine attempts to
match using the next attribute in the list):

1. email
2. preferred\_username
3. username
4. sub

- [Azure](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-oidc-authentication/set-up-oidc-authentication-azure.html#set-up-oidc-authentication-azure)
- [Okta](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-oidc-authentication/set-up-oidc-authentication-okta.html#set-up-oidc-authentication-okta)
- [PingOne](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-oidc-authentication/set-up-oidc-authentication-pingone.html#set-up-oidc-authentication-pingone)
- [Google](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-oidc-authentication/set-up-oidc-authentication-google.html#set-up-oidc-authentication-google)

##### Set Up OIDC Authentication (Azure)

Learn about setting up OIDC authentication for Azure in CIE.

1. Set up OIDC as an authentication type in the Cloud Identity Engine.
   1. Select AuthenticationAuthentication TypesAdd New Authentication Type.
   2. Set Up the OIDC authentication type.

      ![]()
   3. Enter a unique and descriptive Authentication Type
      Name for your OIDC configuration.

      ![]()
   4. Copy the Callback URL/ Redirect URL.

      ![]()
   5. Select the JWT Encryption Algorithm that you
      want to use.

      The default value is RS256, default for most Identity
      Providers.

      ![]()
2. Configure Azure to use OIDC with the Cloud Identity Engine.
   1. Log in to the Azure account you want to use to connect to the Cloud
      Identity Engine.

      ![]()
   2. Click App registration.

      ![]()
   3. Click New registration.

      ![]()
   4. Enter a Name for the application.

      ![]()
   5. Select Accounts in this organizational directory
      only.

      ![]()
   6. For the Redirect URI, enter the domain for your
      Cloud Identity Engine instance and append
      oidc/callback

      ![]()
   7. Click Register to submit the
      configuration.

      ![]()
   8. Click Add user/group and add the users or groups
      you want to be able to configure OIDC as an authentication type (for
      example, service accounts).

      ![]()
3. Obtain the information you need to complete your OIDC Azure configuration.
   1. Select the application you just created then click
      Overview.
   2. Copy the Display name and Application
      (client) ID and save them in a secure location.

      ![]()
   3. Click Add a certificate or secret.

      Don’t allow the client
      secret to expire. If the client secret isn’t up to date, users can’t
      log in using OIDC.

      ![]()
   4. Select Client secrets then click New
      client secret.

      Don’t allow the client
      secret to expire. If the client secret isn’t up to date, users can’t
      log in using OIDC.

      ![]()
   5. Select when the secret Expires then click
      Add.

      Don’t allow the client
      secret to expire. If the client secret isn’t up to date, users can’t
      log in using OIDC.

      ![]()
   6. Copy the Value of the
      client secret and save them in a secure location.

      Because the secret displays only once, be
      sure to copy the information before closing or leaving the page.
      Otherwise, you must create a new secret.

      Don’t allow the client
      secret to expire. If the client secret isn’t up to date, users can’t
      log in using OIDC.

      ![]()
   7. (Optional) Select OverviewEndpoints and Copy the OpenID
      Connect metadata document up to
      /2.0 (the
      well-known/openid-configuration section
      of the URL isn't necessary).

      ![]()
4. Complete and submit the OIDC configuration.
   1. Enter the Display name you copied from Azure in
      step 3 as the Client Name.

      ![]()
   2. Enter the Client ID you copied from Azure in
      step 3.

      ![]()
   3. Enter the Value you copied from Azure in step 3
      as the Client Secret.

      ![]()
   4. Enter
      https://login.microsoftonline.com/organizations/2.0/
      as the Issuer URL.

      ![]()
   5. (Optional) Enter the Endpoint URL you copied in
      step 3.

      ![]()
   6. Click Test Connection and log in to confirm that
      the Cloud Identity Engine can reach your Azure IdP using OIDC.

      If you did not enter the OIDC Issuer URL in
      the previous step, the Cloud Identity Engine automatically populates
      the information.

      ![]()
   7. After confirming that the connection is successful,
      Submit the configuration.

      You can now use OIDC as an authentication type when you [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html).

##### Set Up OIDC Authentication (Okta)

Learn about setting up OIDC authentication for Okta in CIE.

1. Set up OIDC as an authentication type in the Cloud Identity Engine.
   1. Select AuthenticationAuthentication TypesAdd New Authentication Type.
   2. Set Up the OIDC authentication type.

      ![]()
   3. Enter a unique and descriptive Authentication Type
      Name for your OIDC configuration.

      ![]()
   4. Copy the Callback URL/ Redirect URL.

      ![]()
2. Configure Okta to use OIDC with the Cloud Identity Engine.
   1. Sign in to Okta.

      ![]()
   2. Select ApplicationsApplications.

      ![]()
   3. Click Create App Integration.

      ![]()
   4. Select OIDC - OpenID Connect as the
      Sign-in method and Web
      Application as the Application
      Type then click Next.

      ![]()
   5. Enter an App integration name.

      ![]()
   6. Click Add URI and enter the information you
      copied in step 1.

      ![]()
   7. Select the Controlled Access you want to allow
      then click Save.

      ![]()
3. Obtain the information you need to complete your OIDC Okta configuration.
   1. Copy the Client ID.

      ![]()
   2. Copy the Secret.

      The secret for Okta does not expire.

      ![]()
4. Complete and submit the OIDC configuration.
   1. Enter the App integration name you entered in
      Okta in step 2 as the Client Name.

      ![]()
   2. Enter the Client ID you copied from Okta in step
      3.

      ![]()
   3. Enter the Secret you copied from Okta in step 3
      as the Client Secret.

      ![]()
   4. Enter the domain name URL for your Okta IdP as the Issuer
      URL.

      ![]()
   5. (Optional) If you have your Endpoint URL, enter
      it here. If not, continue to the next step (the Cloud Identity Engine
      populates the Endpoint URL automatically after
      you successfully test the connection).

      ![]()
   6. Click Test Connection and log in to confirm that
      the Cloud Identity Engine can reach your Okta IdP using OIDC.

      If you did not enter the OIDC Issuer URL in
      the previous step, the Cloud Identity Engine automatically populates
      the information.

      ![]()
   7. After confirming that the connection is successful,
      Submit the configuration.

      You can now use OIDC as an authentication type when you [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html).

##### Set Up OIDC Authentication (PingOne)

Learn about setting up OIDC authentication for PingOne in CIE.

1. Set up OIDC as an authentication type in the Cloud Identity Engine.
   1. Select AuthenticationAuthentication TypesAdd New Authentication Type.
   2. Set Up the OIDC authentication type.

      ![]()
   3. Enter a unique and descriptive Authentication Type
      Name for your OIDC configuration.

      ![]()
   4. Copy the Callback URL/ Redirect URL.

      ![]()
2. Configure PingOne to use OIDC with the Cloud Identity Engine.
   1. Sign On to your PingOne account.

      ![]()
   2. Select Applications.

      ![]()
   3. Select OIDC then click Add
      Application.

      ![]()
   4. Select Web App then click
      Next.

      ![]()
   5. Enter an Application Name, a Short
      Description for the app, and select the app
      Category, then click
      Next.

      ![]()
3. Continue the OIDC Okta configuration.
   1. Click Add Secret then click
      Next.

      ![]()
   2. Enter the Start SSO URL and the
      Redirect URIs then click
      Next.

      ![]()
   3. Click Next.

      No configuration changes are necessary for this step.

      ![]()
   4. Add all the scopes in the List of Scopes to the
      Connected Scopes then click
      Next.

      ![]()
   5. Select Email (Work) as the
      sub attribute then click
      Next.

      ![]()
   6. Select all the Available Groups and add them to
      the Added Groups then click
      Done.

      ![]()
4. Obtain the information you need to complete your OIDC PingOne configuration and
   enter it in your Cloud Identity Engine configuration.
   1. Copy the following information from your configuration and save it in a
      secure location:

      - The Application Name you entered in step
        2.
      - The Client ID and Client
        Secrets you added in step 3.

        Don’t allow the client
        secret to expire. If the client secret isn’t up to date,
        users can’t log in using OIDC.
      - The Issuer URL (as shown below).

      ![]()
   2. Enter the Application Name you entered in
      PingOne in step 2 as the Client Name.

      ![]()
   3. Enter the Client ID you created in PingOne in
      step 3.

      ![]()
   4. Enter the Client Secrets you created in PingOne
      in step 3 as the Client Secret.

      ![]()
   5. Enter the Issuer URL for your PingOne IdP that
      you copied in step 4 as the Issuer URL.

      ![]()
   6. (Optional) If you have your Endpoint URL, enter
      it here. If not, continue to the next step (the Cloud Identity Engine
      populates the Endpoint URL automatically after
      you successfully test the connection).

      ![]()
   7. Click Test Connection and log in to confirm that
      the Cloud Identity Engine can reach your PingOne IdP using OIDC.

      If you did not enter the OIDC Issuer URL in
      the previous step, the Cloud Identity Engine automatically populates
      the information.

      ![]()
   8. After confirming that the connection is successful,
      Submit the configuration.

      You can now use OIDC as an authentication type when you [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html).

##### Set Up OIDC Authentication (Google)

Learn about setting up OIDC authentication for Google in CIE.

1. Set up OIDC as an authentication type in the Cloud Identity Engine.
   1. Select AuthenticationAuthentication TypesAdd New Authentication Type.
   2. Set Up the OIDC authentication type.

      ![]()
   3. Enter a unique and descriptive Authentication Type
      Name for your OIDC configuration.

      ![]()
   4. Copy the Callback URL/ Redirect URL.

      ![]()
2. Configure Google to use OIDC with the Cloud Identity Engine.
   1. Select your account and Enter your password then
      click Next.

      ![]()
   2. [Create](https://developers.google.com/workspace/guides/create-project) a new project or select
      an existing project.
   3. Enable the Identity and Access Management (IAM)
      API (if it's not already enabled).
   4. Select APIs & ServicesOAuth consent screen then [configure](https://developers.google.com/workspace/guides/configure-oauth-consent) the OAuth consent
      screen.
   5. [Create](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) your OAuth 2.0
      credentials, copy the Client ID and
      Client Secret, and store them in a secure
      location.

      Don’t allow the client
      secret to expire. If the client secret isn’t up to date, users can’t
      log in using OIDC.
3. Obtain the information you need to complete your OIDC Google configuration and
   enter it in your Cloud Identity Engine configuration.
   1. Copy the following information from your configuration and save it in a
      secure location:

      - The Name you entered in step 2.
      - The Client ID and Client
        secret you copied in step 2 (if you did not do
        so in the previous step).
      - The Authorized redirect URIs you copied
        in step 1.

      ![]()
   2. Enter the application name you entered in step 2 as the
      Client Name.

      ![]()
   3. Enter the Client ID you copied in step 2.

      ![]()
   4. Enter the Client Secret you copied in step 2.

      ![]()
   5. Enter the Authorized redirect URIs that you
      copied in step 1 as the Issuer URL.

      ![]()
   6. (Optional) If you have your Endpoint URL, enter
      it here. If not, continue to the next step (the Cloud Identity Engine
      populates the Endpoint URL automatically after
      you successfully test the connection).

      ![]()
   7. Click Test Connection and log in to confirm that
      the Cloud Identity Engine can reach your Google IdP using OIDC.

      If you did not enter the OIDC Issuer URL in
      the previous step, the Cloud Identity Engine automatically populates
      the information.

      ![]()
   8. After confirming that the connection is successful,
      Submit the configuration.

      You can now use OIDC as an authentication type when you [Set Up an Authentication Profile](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile.html).

---

<a id="set-up-an-authentication-profile"></a>

##### Set Up an Authentication Profile

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/set-up-an-authentication-profile>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

**Before you begin:**

- [Configure Directories for User Identification](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type.html) and add your users.
- [Set Up a SAML 2.0 Authentication Type](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type.html) or [Set Up a Client Certificate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-a-client-certificate.html#id559b4d92-459d-4d87-849c-30bcaf979fd6) to use as an authentication
  type.

After configuring your specific authentication sources—such as a **SAML 2.0** Identity
Provider, **OpenID Connect (OIDC)**, or **Client Certificates**—you must
create an **Authentication Profile** to define how these methods are applied to
your users. This profile functions as the policy layer of your identity
infrastructure, allowing you to specify exactly which verification method is used
for different segments of your organization. You can specify one or more
authentication types by group or by directory or for all directories.

To use more than one authentication type in your authentication profile, you must [configure a directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type.html#id0c385168-da26-44ec-bba8-149bbb64092f) in
the Cloud Identity Engine. For a single client certificate authentication type,
configuring a directory in the Cloud Identity Engine is optional. There is no
directory requirement for a single SAML 2.0-compliant authentication type.

1. Select AuthenticationAuthentication Profiles then Add
   Authentication Profile.

   ![]()
2. Enter a unique Profile Name.
3. Select the Authentication Mode.

   ![]()

   - If
     you select Single as the authentication mode,
     click Select authentication type and select
     the authentication type you want to use. 

     ![]()
   - If either of the following apply to your configuration, select the Directory Sync
     Username Attribute and Directory Sync Group
     Attribute.

     To successfully
     authenticate users using a client certificate, the value of the
     Directory Sync Username Attribute must
     match the value of the Username Attribute you
     select when you configure the Client Certificate Authentication
     Type.

     - You selected Multiple as the
       Authentication Mode and you have configured a client
       certificate.
     - You selected Single and the
       Authentication Type is Client Certificate.

     Palo Alto Networks strongly recommends
     using the User Principal Name (e.g.,
     bobsmith@corporation.com) format for the
     Directory Sync Username Attribute.

     ![]()
4. (Multiple Authentication Mode only) Define the Authentication
   mapping order by selecting the configured authentication
   types that you want to use to authenticate users.

   ![]()
5. (Multiple Authentication Mode only) During authentication, the Cloud Identity
   Engine uses the user identity information in the given Authentication
   mapping order to obtain the directory group information for the
   user to determine if the user’s group has an assigned authentication type. You
   can optionally Drag to reorder  authentication types. If
   the user belongs to multiple groups, the Cloud Identity Engine uses the first
   authentication type you assign to the group for user authentication.

   ![]()
6. Select the Default authentication type that
   you want the Cloud Identity Engine to use to authenticate users
   if the user is not in an assigned group.

   As a best practice, assign a default authentication type for each group you
   want to authenticate using the Cloud Identity Engine.

   ![]()
7. Choose directories and groups by selecting
   a directory or selecting All Directories.

   ![]()

   You can click the drop-down button to view or select individual users from a
   group. 

   ![]()

   You
   can also search by Directory Sync Group Attribute (such
   as Common-Name).

   ![]()
8. Select the group or groups from each directory that you
   want to authenticate using the authentication type you select in
   the next step.

   ![]()
9. Select an authentication type and Assign it
   to assign this authentication type to the group or groups you selected.

   ![]()
10. Review your selections by authentication type or select All
    Authentication Types to see all assigned groups.

    ![]()

    To remove access, make a selection from the Assigned
    Groups and click the Unassign button.

    ![]()
11. Submit your changes to configure
    the authentication profile.

**Next Steps:**

- [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html)
- [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html)
- [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to combine the capabilities of the Cloud
  Identity Engine with the other Palo Alto Networks apps you use.

---

<a id="set-up-an-authentication-profile-1"></a>

##### Set Up an Authentication Profile

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-the-cloud-identity-engine-in-an-authentication-profile>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

**Before you begin:**

- [Configure Directories for User Identification](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type.html) and add your users.
- [Set Up a SAML 2.0 Authentication Type](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type.html) or [Set Up a Client Certificate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-a-client-certificate.html#id559b4d92-459d-4d87-849c-30bcaf979fd6) to use as an authentication
  type.

After configuring your specific authentication sources—such as a **SAML 2.0** Identity
Provider, **OpenID Connect (OIDC)**, or **Client Certificates**—you must
create an **Authentication Profile** to define how these methods are applied to
your users. This profile functions as the policy layer of your identity
infrastructure, allowing you to specify exactly which verification method is used
for different segments of your organization. You can specify one or more
authentication types by group or by directory or for all directories.

To use more than one authentication type in your authentication profile, you must [configure a directory](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type.html#id0c385168-da26-44ec-bba8-149bbb64092f) in
the Cloud Identity Engine. For a single client certificate authentication type,
configuring a directory in the Cloud Identity Engine is optional. There is no
directory requirement for a single SAML 2.0-compliant authentication type.

1. Select AuthenticationAuthentication Profiles then Add
   Authentication Profile.

   ![]()
2. Enter a unique Profile Name.
3. Select the Authentication Mode.

   ![]()

   - If
     you select Single as the authentication mode,
     click Select authentication type and select
     the authentication type you want to use. 

     ![]()
   - If either of the following apply to your configuration, select the Directory Sync
     Username Attribute and Directory Sync Group
     Attribute.

     To successfully
     authenticate users using a client certificate, the value of the
     Directory Sync Username Attribute must
     match the value of the Username Attribute you
     select when you configure the Client Certificate Authentication
     Type.

     - You selected Multiple as the
       Authentication Mode and you have configured a client
       certificate.
     - You selected Single and the
       Authentication Type is Client Certificate.

     Palo Alto Networks strongly recommends
     using the User Principal Name (e.g.,
     bobsmith@corporation.com) format for the
     Directory Sync Username Attribute.

     ![]()
4. (Multiple Authentication Mode only) Define the Authentication
   mapping order by selecting the configured authentication
   types that you want to use to authenticate users.

   ![]()
5. (Multiple Authentication Mode only) During authentication, the Cloud Identity
   Engine uses the user identity information in the given Authentication
   mapping order to obtain the directory group information for the
   user to determine if the user’s group has an assigned authentication type. You
   can optionally Drag to reorder  authentication types. If
   the user belongs to multiple groups, the Cloud Identity Engine uses the first
   authentication type you assign to the group for user authentication.

   ![]()
6. Select the Default authentication type that
   you want the Cloud Identity Engine to use to authenticate users
   if the user is not in an assigned group.

   As a best practice, assign a default authentication type for each group you
   want to authenticate using the Cloud Identity Engine.

   ![]()
7. Choose directories and groups by selecting
   a directory or selecting All Directories.

   ![]()

   You can click the drop-down button to view or select individual users from a
   group. 

   ![]()

   You
   can also search by Directory Sync Group Attribute (such
   as Common-Name).

   ![]()
8. Select the group or groups from each directory that you
   want to authenticate using the authentication type you select in
   the next step.

   ![]()
9. Select an authentication type and Assign it
   to assign this authentication type to the group or groups you selected.

   ![]()
10. Review your selections by authentication type or select All
    Authentication Types to see all assigned groups.

    ![]()

    To remove access, make a selection from the Assigned
    Groups and click the Unassign button.

    ![]()
11. Submit your changes to configure
    the authentication profile.

**Next Steps:**

- [Configure the Cloud Identity Engine as a Mapping Source on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html)
- [Configure Cloud Identity Engine Authentication on the Firewall or Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-cloud-identity-engine-authentication/configure-the-cloud-identity-engine-in-an-authentication-profile.html)
- [Associate the Cloud Identity Engine with Palo Alto Networks Apps](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/enforce-security-policy-with-cloud-identity-engine/associate-a-cloud-identity-engine-instance.html) to combine the capabilities of the Cloud
  Identity Engine with the other Palo Alto Networks apps you use.

---

<a id="configure-the-cloud-identity-engine-as-a-mapping-source"></a>

##### Configure the Cloud Identity Engine as a Mapping Source

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall>*

Learn about how to configure CIE as a mapping source for User-ID.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

When you configure the Cloud Identity Engine as a User-ID source, the firewall or
Panorama retrieves the group mapping information from the Cloud Identity Engine. You
can then use the group information from the Cloud Identity Engine to create and
enforce group-based security policy rules.

If your tenant contains an Okta directory that uses
subdomains, enter the following CLI command on the firewall before configuring the
Cloud Identity Engine profile: debug user-id dscd subdomains on.
This command is disabled by default. To disable the subdomain capability, use the
debug user-id dscd subdomains off CLI command. These commands
are supported for PAN-OS version 10.2.9.

The Cloud Identity Engine retrieves the information for your tenant based on your
device certificate. It also uses the Palo Alto Networks Services [service route](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-networking-admin/service-routes/service-routes-overview.html), so make sure to allow
traffic for this service route or [configure a custom service route](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-networking-admin/service-routes/configure-service-routes.html).

To ensure that the Cloud Identity Engine can successfully
retrieve users and groups, all user or group names must meet the following
requirements: the name is case-sensitive and can have up to 63 characters on the
firewall or up to 31 characters on Panorama. It must be unique and use only letters,
numbers, hyphens, and underscores.

- [PAN-OS & Panorama](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-on-the-firewall.html#idd7321e4c-1e5f-4594-919a-6874fb04a50f)

---

<a id="troubleshoot-the-cloud-identity-engine"></a>

#### Troubleshoot the Cloud Identity Engine

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/troubleshoot-the-cloud-identity-engine>*

Learn more about how to troubleshoot issues with the
Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you are encountering issues with the Cloud Identity
Engine, refer the following topics for common issues and their solutions.

- [Cloud Identity Engine Troubleshooting Checklist](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/cloud-identity-engine-troubleshooting-checklist.html#id3b694492-00f5-4818-84ef-c13d4c725b2e)
- [Troubleshoot Cloud Identity Engine Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5)
- [Use the Authentication Logs for Troubleshooting](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/use-the-log-viewer-for-troubleshooting.html#id5f3615a5-eeca-428d-a512-77ddd1214eae)
- [Monitor Cloud Identity Engine Status](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/monitor-cloud-identity-engine-status.html#id5c9d8046-9a8c-4bf4-a525-52a253330c2d)

---

<a id="cloud-identity-engine-troubleshooting-checklist"></a>

##### Cloud Identity Engine Troubleshooting Checklist

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/troubleshoot-the-cloud-identity-engine/cloud-identity-engine-troubleshooting-checklist>*

Review the checklist to troubleshoot Cloud Identity Engine
configuration and connection issues.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

Use the checklist below to troubleshoot general
issues such as configuration or connection issues for the Cloud
Identity Engine. After each task, check if the issue still exists
before attempting the next task.

1. Confirm that your configuration meets the [system requirements](https://https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-release-notes/cloud-identity-engine-release-notes-welcome/cloud-identity-engine-release-notes-system-requirements/cortex/directory-sync/directory-sync-release-notes/directory-sync-release-notes-welcome/directory-sync-release-notes-system-requirements.html).
2. Use the Palo Alto Networks services status page ([status.paloaltonetworks.com](https://status.paloaltonetworks.com/)) to confirm that
   the Cloud Identity Engine service is active.
3. Use the system logs on the firewall associated with your
   Cloud Identity Engine tenant to check the [Cloud Identity Engine
   status](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/monitor-cloud-identity-engine-status.html#id5c9d8046-9a8c-4bf4-a525-52a253330c2d) for any issues.
4. (On-premises Active Directory only) Confirm that you have configured
   your network to allow Cloud Identity Engine traffic and [Search Cloud Identity Agent Logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs/search-cloud-identity-agent-logs.html) for any possible cuases of the issue.
5. (On-premises Active Directory only) Confirm
   your configuration is correct.

   - On the agent host:
     - Confirm you have administrator
       privileges for the agent host so that you can install and configure
       the agent.
     - Confirm that the Protocol you specify
       for the agent is supported and enabled on the agent host.
     - Close the agent and restart it.
     - Clear the DNS cache by entering the following command from an administrative
       command prompt: ipconfig /flushdns.
     - Confirm the server where you installed the agent meets the system requirements.
   - On the agent:
     - [Stop and restart](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/start-stop-cloud-identity-engine-service.html#id1818J060VBD) the
       connection to the Cloud Identity Engine service.
     - Confirm that the Bind DN and Bind
       Password are correct.
     - Confirm that the region for the Cloud Identity Engine in
       your Cloud Identity Configuration matches
       the region for your tenant.
     - Confirm that the Domain is a fully qualified domain
       name and the specified Port on the Active Directory
       server allows communication with the Cloud Identity agent.
     - Try increasing your Bind Timeout and Search
       Timeout to allow more time for the agent to connect
       and the search to complete.
   - In the app:
     - Check the Agents
       & Certificates page to verify you are using the
       latest version of the agent.
     - Check the Directories and Agents
       & Certificates pages to confirm the domains the
       agent is monitoring are correct.
     - Check the Directories page to confirm
       the NetBIOS Name is not empty. If the NetBIOS Name
       is empty, correct the domain name in the Cloud Identity agent and commit
       your changes. Wait at least five minutes before using the Directories page
       to verify the domain name and NetBIOS name are now correct, then
       remove the entry for the incorrect domain in the app.
6. (On-premises Active Directory only) Check the
   status of your certificates.

   - On the agent host:
     - If you are using LDAPS or LDAP
       with STARTTLS, confirm the root and intermediate CA certificates
       that were used to issue your domain controller certificates are
       valid and available in the Local Computer Trusted Root CA.
     - Confirm that you are not using a certificate that was generated
       for another tenant and that the certificate is not used for another
       agent or service.
     - Confirm you have generated a unique certificate in the Cloud
       Identity Engine app for each agent and that it is available in the
       Local Computer certificate store of the agent host.
   - In the app:
     - Check the Agents
       & Certificates page to verify that the agent has
       an associated Certificate.
     - Check the Agents & Certificates page
       to verify that the certificate status is not expired or revoked.
7. (On-premises Active Directory only) Confirm
   all connections are active.

   - On the agent:
     - Check the Cloud Identity
       Configuration to verify that the agent status is Running.
     - Check the LDAP Configuration is valid
       and Test Connectivity to AD to confirm the
       connection to your Active Directory is active.
     - View the Monitoring page to confirm the agent
       is Connected to the Cloud Identity
       Engine.
     - Check when the Last Update to Cloud Identity Engine was
       successful to determine the last time the agent was able to connect
       to the service.
     - Check when the Last LDAP Fetch was successful
       to determine the last time the agent was able to connect to your
       Active Directory.
   - In the app:
     - Check the Directories page
       for the Sync Status to determine if the last
       sync between the agent and the service was successful.
     - Check when the attributes were Last Updated by
       your Active Directory.
     - Check the Agents & Certificates page
       to confirm the agent’s Status is Online.
8. (Cloud-based directory only) If you are experiencing issues
   with your cloud-based directory:

   - [Reconnect](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories/manage-your-azure-directory/reconnect-directory.html#idb99373f7-aa27-449f-969a-0b2649b58666) your
     directory to your Cloud Identity Engine tenant.
   - Verify your directory credentials are correct.
   - Verify that you have granted the permissions that the Cloud
     Identity Engine requires.

If you are still encountering issues:

- (On-premises Active Directory only) Collect the [Cloud Identity agent logs](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/manage-the-cloud-identity-engine/manage-the-cloud-identity-agent/configure-cloud-identity-agent-logs.html#id1818I0S0N5S) to share
  with support.
- Collect the authentication logs so that support can [Use the Authentication Logs for Troubleshooting](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/use-the-log-viewer-for-troubleshooting.html)
- Learn more about how to [troubleshoot](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues.html#id183LG0B60R5) specific
  errors.
- Find out how to [Get Help](https://docs.paloaltonetworks.com/identity.html).

---

<a id="troubleshoot-cloud-identity-engine-issues"></a>

##### Troubleshoot Cloud Identity Engine Issues

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/troubleshoot-the-cloud-identity-engine/troubleshoot-cloud-identity-engine-issues>*

If you are encountering issues with the Cloud Identity
Engine, refer to the following table for common issues and solutions.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

If you are encountering specific issues when using the
Cloud Identity Engine, refer to the following table for common issues
and solutions. If you are still experiencing issues, be sure to
review how to [Monitor Cloud Identity Engine Status](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/monitor-cloud-identity-engine-status.html#id5c9d8046-9a8c-4bf4-a525-52a253330c2d) and the [Cloud Identity Engine Troubleshooting Checklist](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/troubleshoot-the-cloud-identity-engine/cloud-identity-engine-troubleshooting-checklist.html#id3b694492-00f5-4818-84ef-c13d4c725b2e).

|

What Do I Do If... | Resolution |

| --- | --- |

|  |  |
| --- | --- |
|

When I click Create to create the SCIM Connector application in the Azure AD Portal, a Not found error displays. | Refresh the page and recreate the SCIM Connector application. |

|

The Azure AD Portal displays that the sync is complete and there is a steady state for the SCIM Connector, but the user and group count does not display. | If the user and group count does not display, the sync is not fully complete. To resolve the issue, complete the following steps:  1. Verify the provisioning mappings, scope,    and other settings are correct. 2. Restart provisioning and wait for the    sync to complete. |

|

The sync for the SCIM Connector is unable to complete due to duplicate group names. | Group names must be unique; resolve the duplicate group names so that they are unique and Restart provisioning. If you are unable to resolve the duplicate group names and you don’t need data from the duplicate groups or to use them in security policy, you can continue the setup. |

|

I checked the status of the agent on the Directories page and the status is “In Progress” but no groups or OUs are listed. | While the domain is being synced, the In Progress status appears on the Directories page. If this is the first time the Cloud Identity Engine is syncing the domain, the groups and OUs may take some time to appear. If they do not display, delete then [re-create the Cloud Identity Engine tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/cloud-identity-engine-instances/create-cloud-identity-engine-instances.html#id17CLJB00HR1) and add the domain(s) again. |

|

The hub does not redirect to display my Cloud Identity Engine tenants or displays a blank page. | If this issue occurs, contact support (see [Get Help](https://docs.paloaltonetworks.com/identity.html)). |

---

<a id="cloud-identity-engine-getting-started"></a>

##### Cloud Identity Engine Getting Started

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/troubleshoot-the-cloud-identity-engine/use-the-log-viewer-for-troubleshooting>*

##### Use the Authentication Logs for Troubleshooting

Learn how to check the Authentication Logs for information that you can use to
troubleshoot authentication issues with the Cloud Identity Engine.

To troubleshoot authentication issues with [identity providers](https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-an-identity-provider-in-the-cloud-identity-engine.html#id5b7ef98d-9172-470a-a2b2-cd2b7c0d6d0a) or the
[firewall](https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/authenticate-users-with-the-cloud-identity-engine/configure-the-cloud-identity-engine-in-an-authentication-profile.html#id5988c4fb-d95c-4071-8d5c-2cbede9a8cc8), use the Authentication
Logs to review messages to the log.

Each authentication phase generates at least two log entries, with the exception
of SAML authentication using multiple CA chains in a certificate type, which
generates three log entries.

1. In the Cloud Identity Engine app, select AuthenticationAuthentication Logs.

   ![]()
2. To ensure the page displays the latest data, click Apply
   Search/Refresh.

   ![]()
3. Use the Date selector to search based on when the issue
   occurred.
4. Select the number of results you want to Show on each
   page.
5. Select whether you want to display the results in order
   of Newest first or Newest last.
6. Select a Profile to restrict the search results to a
   specific identity provider (IdP) profile.
7. Select the Status you want to display (All
   Status, Success, or
   Fail).
8. To Search by keyword, enter a
   search term and Apply Search.
9. To view the SAML request and response and the JSON web token (JWT), select the
   Details (

   ![]()

   ) for the row that contains the data you want to
   view.

   The log details display, allowing you to review the Data
   Received by the Cloud Identity Engine from your IdP and the
   Data Sent by the IdP to the Cloud Identity Engine.
   You can copy (

   ![]()

   ) the text to use for troubleshooting. 

   ![]()
10. Review the results to look for entries that indicate issues.
11. (Optional) Export the results
    as a .CSV file.

    ![]()

---

<a id="monitor-cloud-identity-engine-status"></a>

##### Monitor Cloud Identity Engine Status

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/troubleshoot-the-cloud-identity-engine/monitor-cloud-identity-engine-status>*

Learn how to view logs on your Palo Alto Networks firewall
for issues detected in the Cloud Identity Engine.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW - Prisma Access | The Cloud Identity Engine service is free; however, the enforcement points utilizing directory data may require specific licenses. Click [here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing) for more information. |

The firewall that you associate with your Cloud Identity Engine tenant checks the Cloud Identity
Engine daily for any errors or issues (for example, an expired [certificate](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/configure-a-client-certificate.html#id559b4d92-459d-4d87-849c-30bcaf979fd6) or a missing [identity provider](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type.html) profile).

The
firewall logs any errors that it detects in the system logs using
the event type cas-message. If you
encounter issues with your Cloud Identity Engine, be sure to review
the system logs on your firewall to help troubleshoot the issue.

![]()

---

<a id="cloud-identity-agent-help"></a>

#### Cloud Identity Agent Help

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/cloud-identity/cloud-identity-engine-getting-started/get-help-with-the-cloud-identity-engine>*

Learn how to use the on-premises Cloud Identity agent
to connect to the cloud-based Cloud Identity Engine.

The Cloud Identity agent collects user, organizational
unit (OU), container, computer, and group attributes from your on-premises
Active Directory or OpenLDAP-based directory server and stores them
in the Cloud Identity Engine, a secure, cloud-based infrastructure.
This allows your Palo Alto Networks cloud-based applications to
use the directory attributes to display more context about users and
devices and to help you configure user- or group-based policies.

---

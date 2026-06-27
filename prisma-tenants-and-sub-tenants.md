# Prisma Tenants & Sub-Tenants

> Compiled 2026-06-27. Tenant / multitenancy documentation across Common Services, Strata
> Cloud Manager, and Prisma Access — for building a **dedicated Prisma sub-tenant for
> Prisma Browser**.

## Building a Prisma Browser sub-tenant — where to look
1. **Understand the model** — *What Is a Tenant* and tenant/sub-tenant relationships → **Part 1 (Common Services)**.
2. **Create & manage the sub-tenant** — multitenant management, add/acquire tenants, sub-tenant
   administration in Strata Cloud Manager → **Part 2 (Strata Cloud Manager)**.
3. **Multitenancy on Prisma Access** — enable multitenancy / migrate, per-tenant scope → **Part 3 (Prisma Access)**.
4. **Associate devices/products to the sub-tenant** — device associations → **Part 1 (Common Services)**.
5. **License the sub-tenant** — allocate Prisma Access + Prisma Browser licenses to the new tenant →
   see `prisma-browser-licensing-onboarding.md` (allocate-licenses / activation).

**Contents:** Part 1 Common Services (80 pp) · Part 2 Strata Cloud Manager (35 pp) · Part 3 Prisma Access (11 pp).
> Each part keeps its own TOC and `*Source:` links; anchors namespaced (`cs-`/`scm-`/`pa-`).

---

# Common Services - Tenant Management and Device Associations

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services on 2026-06-27. 80 pages. Absolute URLs.

> Scoped to: /subscription-and-tenant-management, /device-associations

## Table of Contents

  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-1)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-2)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-3)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-4)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-5)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-6)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-7)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-8)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-9)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-10)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-11)
  - [Manage Subscriptions](#cs-manage-subscriptions)
    - [Manage Subscriptions](#cs-manage-subscriptions-1)
    - [Manage Subscriptions](#cs-manage-subscriptions-2)
    - [Convert a Trial to a Production License](#cs-convert-a-trial-to-a-production-license)
    - [Manage Subscriptions](#cs-manage-subscriptions-3)
    - [Manage Subscriptions](#cs-manage-subscriptions-4)
    - [Modify License Allocation](#cs-modify-license-allocation)
    - [Extend or Renew a Subscription](#cs-extend-or-renew-a-subscription)
    - [Expiring and Expired Subscription](#cs-expiring-and-expired-subscription)
    - [Deactivate a Product](#cs-deactivate-a-product)
  - [Tenant Management](#cs-tenant-management)
    - [What is a Tenant?](#cs-what-is-a-tenant)
    - [Add a Tenant](#cs-add-a-tenant)
    - [Edit a Tenant](#cs-edit-a-tenant)
    - [Manage Tenant Licenses](#cs-manage-tenant-licenses)
    - [Delete a Tenant](#cs-delete-a-tenant)
    - [Transition from Single Tenant FedRAMP to Multitenant FedRAMP](#cs-transition-from-single-tenant-fedramp-to-multitenant-fedramp)
    - [Move an Internal Tenant](#cs-move-an-internal-tenant)
    - [Acquire an External Tenant](#cs-acquire-an-external-tenant)
    - [Approve an External Tenant Acquisition](#cs-approve-an-external-tenant-acquisition)
    - [Limitations for Moving and Acquiring Tenants](#cs-limitations-for-moving-and-acquiring-tenants)
    - [Tenant Hierarchy Limits](#cs-tenant-hierarchy-limits)
    - [Edit Telemetry Settings](#cs-edit-telemetry-settings)
  - [Product Management](#cs-product-management)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-12)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-13)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-14)
  - [Device Associations in Strata Cloud Manager](#cs-device-associations-in-strata-cloud-manager)
    - [Device Associations in Strata Cloud Manager](#cs-device-associations-in-strata-cloud-manager-1)
    - [Device Associations in Strata Cloud Manager](#cs-device-associations-in-strata-cloud-manager-2)
    - [Device Associations in Strata Cloud Manager](#cs-device-associations-in-strata-cloud-manager-3)
  - [Device Model Compatibility](#cs-device-model-compatibility)
  - [Firewall and License Type Compatibility](#cs-firewall-and-license-type-compatibility)
  - [Platform Explorer](#cs-platform-explorer)
- [Device Associations in Strata Cloud Manager](#cs-device-associations-in-strata-cloud-manager-4)
- [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-15)
      - [Deactivate a Product](#cs-deactivate-a-product-1)
      - [Deactivate a Product](#cs-deactivate-a-product-2)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-16)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-17)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-18)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-19)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-20)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-21)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-22)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-23)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-24)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-25)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-26)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-27)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-28)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-29)
      - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-30)
      - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-31)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-32)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-33)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-34)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-35)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-36)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-37)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-38)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-39)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-40)
  - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-41)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-42)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-43)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-44)
    - [Common Services: License Activation, Subscription, & Tenant Management](#cs-common-services-license-activation-subscription-tenant-management-45)

---

<a id="cs-common-services-license-activation-subscription-tenant-management"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started>*

### Get Started with Common Services: License Activation, Subscription, Tenant Management, & Product Management

Get Started with Common Services: License Activation, Subscription, Tenant Management,
and Product Management.

Welcome to License Activation, Subscription, Tenant Management, and Product Management. Activate
and manage all your available licenses from one location. In multitenant
deployments, you can create multiple tenants, build a hierarchy, and share
and allocate license subscriptions for the desired tenants.

#### How to Access Subscription Management, Tenant Management, and Product Management

After you activate a license for your product, there are a few ways to
access Subscription Management, Tenant Management, and Product
Management.

|

Prisma SASE Multitenant Portal and FedRAMP | Single Tenant View of the Activation Console | Multienant View of the Activation Console | Single Tenant AIOps for NGFW and Strata Cloud Manager | Multitenant AIOps for NGFW and Strata Cloud Manager |

| --- | --- | --- | --- | --- |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

If you're a FedRAMP Moderate customer as of January 2024 or Prisma SASE FedRAMP High "In Process" customer as of December 2023, the following also applies to you.  If you have received information about the transition of your tenant to the Prisma SASE Multitenant Portal, you can access through the original support account view of the hubPrisma SASE Platform button Tenants and ServicesCommon ServicesSubscription or Tenant Management. | From the tenant view of the hubCommon Services  button, you will see Subscriptions & Add-ons Products in a single tenant environment. | From the tenant view of the hubCommon Services  button, you will see Subscriptions & Add-ons Tenant Management in a multitenant environment | If you have a single tenant, you can access through SettingsSubscriptions or Products . | If you have a multitenant environment, you can access through System SettingsSubscriptions or Tenants . |

Regardless of how you access Subscriptions or Tenants,
you’ll use approximately the following flow to manage your
deployment.

1. Activate licenses for your deployment type.
2. Manage your
   [product](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-products.html) or
   [tenants](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants).
3. Manage users, roles, and service accounts with [identity and
   access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/get-started).
4. (Optional) Manage devices in your deployment
   with [Device
   Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
5. (Optional) View health, security, and telemetry
   metrics with [AIOps for
   NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw/get-started-with-aiops/about).
6. (Optional) Monitor and manage items such as
   multitenant status, alerts, alarms, virtual ION
   devices through the [Strata Multitenant Cloud Manager](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform).

See the [Common Services FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq)
for further information about tenants, the tenant transition, or the
tenant view of the hub.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-1"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started/which-activation-flow-to-use>*

#### How Product Activation Works

Contains generic instructions to activate a product in the Activation Console or the
hub.

When you purchase a Palo Alto Networks product or subscription, you’ll receive
an email with a link you can use to launch the activation workflow and get started.
Here’s what to expect.

Based on the product you are activating determine which activation steps to
follow:

- **Activate SD-WAN and Firewall Products** – Use the existing
  workflow in the Hub and Strata Cloud Manager to activate products, complete
  onboarding, and manage licenses for tenants that have not yet transitioned to
  the new activation experience.

  **Supported for:**Next-Generation Firewall and SD-WAN products.
- **Activate SASE Products** – Use the Activation Console to complete product
  activation and onboarding through the new unified activation workflow for
  tenants that have already migrated to the updated experience. This workflow
  applies only to the SASE products that have transitioned to the unified
  activation experience.

  **Supported for:** Prisma Access,Prisma Browser,Remote Browser Isolation,CASB-X,Data Security,AI Access Security,SaaS Security Posture Management,Enterprise DLP

- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started/which-activation-flow-to-use/activate-using-hub.html#topic-70032f49-4d69-468c-bbbe-5d3f1b6ca6f6)
- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started/which-activation-flow-to-use/activate-using-activation-console.html#topic-82a2a6d3-ca17-4660-823d-3f82ab1e4d38)

#### Firewall and SD-WAN

Contains instruction to activate a product through hub

Next-Generation Firewall, SD-WAN, and some SASE products that have not yet transitioned
to the new activation experience during the phased rollout will use the existing
activation workflow described in this section.

##### Activate a License or Subscription for Paid Products

First-time license activation for paid products is through an email that you receive
from Palo Alto Networks regarding. The email contains an activation link. Activating
a product from the activation link creates a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where the product is
deployed.

![]()

After you activate a product, you have access to [Common Services](https://docs.paloaltonetworks.com/common-services) to [manage your product](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-products.html) from the
Activation Console or Strata Cloud Manager. You get assigned the
[Superuser](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) role to manage your product.

##### Single Customer Support Portal Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, for a single Customer Support Portal account, certain fields
in the activation form are prepopulated for you. Depending on your product, you
might be asked to select a region where you want to deploy the product, to select or
create Strata Logging Service to store your logs, to select or create a Cloud
Identity Engine instance to identify and verify all users across your
infrastructure, or to associate devices or appliances. 

![]()

- In the activation workflow, the Customer Support Portal account
  associated with the user is prepopulated if there is only one Customer
  Support Portal account associated with the user.
- For the selected Customer Support Portal account, if there is
  no prior tenant associated, the tenant field is autopopulated with the
  same name as the Customer Support Portal account.
- After completing the activation, the user who is activating the first
  product is added as a superuser on the selected tenant, and can also add
  other users.
- The default tenant can't be deleted as long as there are
  products activated in the tenant.
- If the user's selected Customer Support Portal account has a
  previously mapped tenant, and the user activating a license does not
  have access to that tenant, the user is informed to contact the tenant
  account admin to request access.

##### Multiple Customer Support Portal Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, if you have multiple Customer Support Portal accounts, you
will select the Customer Support Portal account that you want to use for managing
your product. Depending on your product, you might be asked to select a region where
you want to deploy the product, to select or create Strata Logging Service to
store your logs, to select or create a Cloud Identity Engine instance to identify
and verify all users across your infrastructure, or to associate devices or
appliances. 

![]()

- If there are multiple Customer Support Portal accounts
  associated with the user activating a license, the user can select a
  specific Customer Support Portal account.
- For the selected Customer Support Portal account, if there is
  no prior tenant associated, the tenant field is autopopulated with a
  default tenant that has the same name as the Customer Support Portal
  account name.
- After completing the activation, the user who is activating the first
  product is added as a superuser on the selected tenant, and they should be
  able to add other users.
- If the selected Customer Support Portal account has a
  previously mapped tenant, and the user does not have access to that
  tenant, the user is informed to contact the account admin to request
  access.
- If users require a multitenant setup, they are provided with an option to
  create a new tenant or a child tenant. They can create the hierarchy with
  the first child in the tenant management page. They can select the child
  tenant or create a new child tenant from the activation workflow.
- If multiple tenants exist where products have been previously activated for
  the Customer Support Portal account, but the user does not have access to
  those tenants, the user is warned that the product will be activated in a
  different tenant from where the other services are currently active. The
  user gets the option to proceed anyway, but is warned that dependent
  products need to be activated in the same tenant.

##### Managed Security Service Provider (MSSP) Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, for a Managed Security Service Provider (MSSP), you will
select the Customer Support Portal account that you want to use for managing your
customers' products. You will create a tenant hierarchy to manage them. Depending on
the product, you might be asked to select a region where you want to deploy the
product, to select or create Strata Logging Service to store the logs, to
select or create a Cloud Identity Engine instance to identify and verify all users
across the infrastructure, or to associate devices or appliances. 

![]()

After you activate a tenant heirarchy, you have access to [Common Services](https://docs.paloaltonetworks.com/common-services) to [manage your tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants.html) from the
Activation Console or Strata Cloud Manager. You can also use Strata Multitenant Cloud Manager aggregated views for monitoring information across all of your
tenants.

- In the case of managed security service providers (MSSP), the
  end customers are managed by the MSSP that owns the Customer Support
  Portal account.
- The default tenant is associated with the MSSP Customer Support
  Portal account. The user activating the product must be granted access
  to that tenant, and then user can create child tenants and activate
  products in the child tenant.

#### SASE

contains procedure to activate a product using the activation console.

The new unified activation and onboarding experience is available only for
following SASE products that have transitioned to the Activation Console.

Firewall and SD-WAN products (Next-Generation Firewall and SD-WAN), as well as
SASE products that have not yet transitioned, will continue to follow the existing
workflow described in Activation Using Hub.

**Supported for:** Prisma Access,Prisma Browser,Remote Browser Isolation,CASB-X,Data Security,AI Access Security,SaaS Security Posture Management,Enterprise DLP

##### Activate a Product on a Single Tenant

**Before You Begin**

If the product needs to be activated in a non-default tenant, create
the [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants) before you begin the activation
process

To activate a product, perform the following:

The following steps outline the common activation procedure for products. The
screenshots shown are based on Prisma Access, but the same workflow applies to all
supported products. Detailed, product-specific steps are provided in the respective
SASE product documentation.

1. Click **Login to Activate** in the welcome email.

   ![]()
2. This will take you to the Activation ConsoleSubscription and Add-ons, where you can view the list of all your product
   entitlements. Click **Activate** to activate a specific product.
3. You will be taken to the Product activation form.

   ![]()
4. Select a **Tenant** if you have multiple tenants. For a single
   tenant environment, it is autopopulated with the primary tenant.
5. Select a **Region** where you want to deploy your product.
6. Select the product-specific details.
7. **Agree to the terms and conditions**, and then click
   **Activate Now**.
8. You will be redirected to the Subscription page, where you can see
   the activation status. The status column would show **Activation in
   Progress** for the products where activation is in progress.
9. Once the activation is complete, click **Launch** to launch and access the
   product.When you launch the product, you will be redirected to the Strata Cloud
   Manager from where you can access the product and all its activated add-ons.

   ![]()

##### Activate a Product on Multiple Tenants

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click ⋮Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   Note: If you are modifying the allocation for the default tenant, ensure
   that you reduce the assigned license quantity. The reduced quantity
   becomes available for reallocation to other tenants in the
   hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat from the Step 3 to allocate licenses to additional tenants.

   Validate
   the license allocation by switching to the corresponding tenant in the
   tenant browser and reviewing the allocation details.

   ![]()

After activating your products, you can continue to [manage your subscriptions](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/about-subscription-management) from the
**Subscriptions & Add-ons** page in the **Activation Console**. This
page provides options to perform common subscription management tasks, including
activating free add-ons, enabling purchased add-ons, reallocating licenses to other
tenants, and renewing existing licenses.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-2"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-a-license-for-remote-browser-isolation>*

### Activate a License for Remote Browser Isolation Through Common Services

Learn how to activate a remote browser isolation (RBI) license through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial deployments | - Prisma Access license with optional add-ons - Activation link for Remote Browser Isolation license - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser with access to the   [Customer Support   Portal](https://support.paloaltonetworks.com/Support/Index) |

Verify if this activation process [applies to you](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started).

[Remote Browser Isolation](https://docs.paloaltonetworks.com/remote-browser-isolation) (RBI) creates a no-code
execution isolation environment for a user's local browser, so that no website code
and files are executed on the local browser.

The following steps assume that you have [already activated](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license)
Prisma Access and [added tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html#add-tenants) to create a multitenant
hierarchy.

![]()

After you receive an email from Palo Alto Networks identifying the RBI license you
are activating, click the email link to begin the activation process.

1. Select
   Login to Activate in your
   email.
2. You are automatically directed to Common ServicesSubscription & Add-ons, where you activate the subscription for your product.
3. Allocate the subscription to the recipient Tenant of
   your choice.

   ![]()
4. The Region is populated with a storage location for the
   data logs, known as Strata Logging Service.
5. Agree to the terms and conditions, and
   Activate.
6. Common ServicesTenant Management displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you can launch RBI
   from Common ServicesTenant Management or from System SettingsTenants, where you can then [configure RBI](https://docs.paloaltonetworks.com/remote-browser-isolation/administration/configure-rbi).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-3"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation>*

### Prisma SD-WAN and Add-Ons License Activation

Learn how to activate Prisma SD-WAN licenses in Common Services.

Welcome to Prisma SD-WAN license activation.

- [Activate a License for](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-sd-wan.html)
  Prisma SD-WAN and Add-ons

---

<a id="cs-common-services-license-activation-subscription-tenant-management-4"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-sd-wan>*

#### Activate a License for Prisma SD-WAN Through Common Services

Learn how to activate your cloud managed Prisma SD-WAN tenants through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial or   FedRAMP Moderate deployments. Not FedRAMP High "In Process"   deployments, which follow a [different   procedure](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation). | - Prisma SD-WAN license - Activation link - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser |

After you receive an email from Palo Alto Networks identifying the license you are
activating, including all your add-ons and capacities, use the activation link to
begin the activation process. The service will help you with the process of
allocating your license, creating your tenant, and managing your users.

As of December 2023,
all stand-alone Prisma SD-WAN sales orders come with an
activation email regardless if the subscription is brand new or for an existing
tenant. You will notice the new behavior, for example, if you have an existing
Prisma SD-WAN tenant with existing ION hardware devices and
you order more hardware devices for that tenant.

Select Activate Subscription in your email, then use one of
the following options:

- [New purchase license activation -
  one CSP account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-first-time-one-csp.html#sd-wan-first-one-csp)
- [New purchase license activation -
  multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-first-time.html#sd-wan-first)
- [Return visit license
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-repeat-visits.html#sd-wan-return)

#### New Purchase Cloud Managed Prisma SD-WAN Activation

Learn how to activate your newly purchased Cloud Managed Prisma SD-WAN license through Common Services.

Follow these steps for newly purchased Cloud Managed Prisma SD-WAN and add-ons license activation and ION device registration. All stand-alone
Prisma SD-WAN sales orders come with an activation email
regardless if the subscription is brand new or for an existing tenant.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the Multitenant
   Superuser role.
2. Because you have only one Customer Support Portal account associated with your
   user name, the Customer Support Account is
   pre-populated.

   ![]()
3. Allocate the subscription to the recipients of your choice. If your order
   includes ION devices, the device is also registered to this recipient.

   If you need just one tenant, use or rename the tenant provided. The name
   provided matches your Customer Support Portal account for convenience.

   ![]()

   For Managed Security Service Providers (MSSPs) and distributed enterprises,
   you can allocate the subscription directly on any tenant in the hierarchy.
   [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) For a Prisma SD-WAN tenant, allocating the license at the
   child-level automatically provisions it at the top-most, root-level, parent
   Prisma SD-WAN tenant as well. If the order includes
   ION devices, it is recommended that you allocate to the top-most,
   root-level, parent tenant. This enables the parent tenant to do ION device
   management for the child tenants.

   ![]()

   After activation, you can build out your tenant hierarchy as needed. You can
   create your tenant hierarchy to reflect your existing organizational
   structure. You can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access)
   when creating the hierarchy, in addition to [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

   However, any tenants that you create between the child tenant and the
   top-most, root-level, parent tenant do not get automatically provisioned
   with the license. That is a one-time process that happens only at
   activation.
4. Select the Region where you want to deploy your product.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or
   Strata Logging Service) are now provisioned. As the
   subscriptions are activating, the progress status will display. When the process
   is complete, the tenant status displays as Up. You
   now have a tenant provisioned with instances of the products that you purchased.
   The tenant has one user — the account that you used when you began this
   process.
7. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - Prisma SD-WAN
     [Administrator’s Guide](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan)
   - [Open APIs](https://pan.dev/sdwan/docs/)
   - Strata Logging Service
     [Getting Started
     Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
8. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

#### New Purchase Cloud Managed Prisma SD-WAN Activation

Learn how to activate your newly purchased Cloud Managed Prisma SD-WAN license through Common Services.

Follow these steps for newly purchased Cloud Managed Prisma SD-WAN and add-ons license activation and ION device registration. All stand-alone
Prisma SD-WAN sales orders come with an activation email
regardless if the subscription is brand new or for an existing tenant.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the Multitenant
   Superuser role.
2. Choose the Customer Support Account number that you want
   to use to activate the license.

   ![]()
3. Allocate the subscription to the recipients of your choice. If your order
   includes ION devices, the device is also registered to this recipient.

   For Managed Security Service Providers (MSSPs) and distributed enterprises,
   you can allocate the subscription directly on any tenant in the hierarchy.
   [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) For a Prisma SD-WAN tenant, allocating the license at the
   child-level automatically provisions it at the top-most, root-level, parent
   Prisma SD-WAN tenant as well. If the order includes
   ION devices, it is recommended that you allocate to the top-most,
   root-level, parent tenant. This enables the parent tenant to do ION device
   management for the child tenants.

   After activation, you can build out your tenant hierarchy as needed. You can
   create your tenant hierarchy to reflect your existing organizational
   structure. You can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access)
   when creating the hierarchy, in addition to [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

   However, any tenants that you create between the child tenant and the
   top-most, root-level, parent tenant do not get automatically provisioned
   with the license. That is a one-time process that happens only at
   activation.

   1. Create a new tenant from All Tenants +.

      ![]()
   2. Name the tenant and select Done.

      ![]()
   3. (Optional) For Managed Security Service Providers (MSSPs) and
      distributed enterprises, create a new child tenant by selecting
      + from the parent tenant that you previously
      created.

      ![]()
   4. (Optional) Name the child tenant and select
      Done.

      ![]()
4. Select the Region where you want to deploy your product.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or Strata Logging Service) are
   now provisioned. As the subscriptions are activating, the progress status will
   display. When the process is complete, the tenant status displays as
   Up. You now have a tenant provisioned with
   instances of the products that you purchased. The tenant has one user — the
   account that you used when you began this process.
7. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - Prisma SD-WAN
     [Administrator’s Guide](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan)
   - [Open APIs](https://pan.dev/sdwan/docs/)
   - Strata Logging Service
     [Getting Started
     Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
8. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

#### Return Visit Cloud Managed Prisma SD-WAN Activation

Learn how to activate your Cloud Managed Prisma SD-WAN tenants through Common Services for repeat visits.

Follow these steps if you have already completed [new purchase](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-sd-wan.html)
Prisma SD-WAN license activation, you have already created your
tenant hierarchy through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate a
Prisma SD-WAN subscription in additional child tenants in
your existing hierarchy..

1. Log in with your email address.
2. Choose the Customer Support Account number that you want
   to use to claim the license.

   As of December 2023, you can choose a different Customer Support Account than
   you chose during first-time activation. This is important in various
   scenarios such as, if you have different teams providing support for
   different instances of Prisma SD-WAN within the same
   tenant service group (TSG).

   ![]()
3. Allocate the subscription to the recipient tenant of your choice.

   ![]()
4. Select the Region nearest to the storage location of the
   data logs.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or Strata Logging Service) are
   now provisioned. As the subscriptions are activating, the progress status will
   display. When the process is complete, the tenant status displays as
   Up. You now have a tenant provisioned with
   instances of the products that you purchased. The tenant has one user — the
   account that you used when you began this process.
7. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

1. (Optional) In a multitenant hierarchy, monitor your tenants with the
   Prisma SD-WAN
   [Summary Dashboard](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-sd-wan-summary-dashboard.html).
2. (Optional) [add user access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-users) and [assign roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles).
3. For Managed Security Service Provider (MSSP) and distributed enterprise admins
   who build out the tenant hierarchy after activation, make sure to activate the
   Prisma SD-WAN licenses on all the child tenants. This allows you to allocate
   Prisma SD-WAN devices from the root tenant to any child tenant in the
   hierarchy.
   1. Use one of the [various ways to
      access](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html)
      Subscriptions & Add-ons.
   2. Search or scroll to find the subscription that you want to modify, and
      select ActionsActivate Cloud Tenant.

      ![]()
   3. You are automatically directed to the activation web interface to
      activate the license on the child tenant.

      1. Select the child tenant as the
         recipient.
      2. Select a region where you want to deploy
         your product.
      3. Agree to the Terms and Conditions, and
         Activate.
      4. You are automatically directed to Tenant
         Management. As the subscriptions are activating,
         the progress status will display. When the process is complete,
         the tenant status displays as Up. You now have a child tenant
         provisioned with instances of the products that you
         purchased.
   4. Repeat for all child tenants in the hierarchy.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-5"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation>*

### Activate AIOps Premium

Learn about AIOps Premium activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- From email activation link - Commercial deployments | - Customer Support Portal account |

[Strata Cloud Manager](https://docs.paloaltonetworks.com/cloud-management)  provides unified management and
operations only for NGFWs using the AIOps for NGFW Premium license.

- Continue to use the AIOps for NGFW Free app for the NGFWs onboarded
  to AIOps for NGFW Free. For more information, see [Activate AIOps for NGFW Free](https://docs.paloaltonetworks.com/ngfw/getting-started/activate-aiops-for-ngfw).
- To activate AIOps for NGFW with the add-on Enterprise License
  Agreement (ELA), see [activate an add-on enterprise license
  agreement](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation.html).
- To activate AIOps for NGFW with a Software NGFW Credits License
  Agreement, see [activate a software NGFW credits license
  agreement](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/vm-flex-license-activation/activate-vm-flex-license#task-vm-flex-aiops.html).

The AIOps for NGFW Premium (use the Strata Cloud Manager app) license is
supported only in a single tenant environment with paid Strata Logging Service. For information about support for firewalls and AIOps
for NGFW license type combinations, see [Firewall and License Type Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/firewall-and-license-type-compatibility#aiops-for-ngfw-firewall-and-license-type-compatibility).

Strata Cloud Manager is now available, featuring two licensing tiers: Strata
Cloud Manager Essentials and Strata Cloud Manager Pro. This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service. See [Strata Cloud Manager License](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html).

- [First time activation - one CSP
  account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-one-csp.html#aiops-premium-one-csp)
- [First time activation - multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-multiple-csp.html#aiops-premium-multiple-csp)
- [Return visit
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-repeat-visits.html#aiops-premium-return)

### First time AIOps for NGFW Premium Activation - One Customer Support Portal Account

Learn how to activate your AIOps for NGFW Premium application for the
first time if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time CASB-X activation.

1. After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
   begin the activation process.
2. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
3. Allocate the product to the Recipient.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
4. Select a Region where you want to deploy your product.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
5. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
6. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
7. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply AIOps for NGFW Premium.
8. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
9. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
10. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
    appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

    If the status isn't
    Complete, you can't add your devices
    yet.
11. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
    of the following options.

    - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
    - Launch from Common ServicesProducts or from SettingsProducts.
12. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
13. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
14. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### First time AIOps for NGFW Premium Activation - Multiple Customer Support Portal Account

Learn how to activate your AIOps for NGFW Premium application for the
first time if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time AIOps for NGFW Premium activation.

1. After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
   begin the activation process.
2. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
3. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
4. Select a Region where you want to deploy your product.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
5. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
6. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
7. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
8. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
9. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
   appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

   If the status isn't
   Complete, you can't add your devices
   yet.
10. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
    of the following options.

    - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
    - Launch from Common ServicesProducts or from SettingsProducts.
11. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
12. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
13. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Return Visit AIOPs Premium Activation

Learn how to activate your AIOPs Premium for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region for the physical location to process
   your data.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
4. Add Strata Logging Service.

   ![]()

   1. Select an Strata Logging Service instance.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
   appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

   If the status isn't
   Complete, you can't add your devices
   yet.
9. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
   of the following options.

   - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
   - Launch from Common ServicesProducts or from SettingsProducts.
10. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-6"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation>*

### Activate Next-Generation CASB on Cross Platforms CASB-X

Learn about CASB-X activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- From email activation link - Commercial deployments - Prisma Access   - Prisma Access (Managed by Strata Cloud Manager): 3.2 Innovation Release     (Future: Prisma Access 4.0 Preferred Release)   - Prisma Access (Managed by Panorama): 10.2 or newer - Next-Generation Firewall (Hardware Only and not available on   VMs)   - PAN-OS or Panorama management   - PAN-OS 10.2.3 or newer | - Customer Support Portal account - Strata Logging Service is required for SaaS   Security Inline. CASB-X can be   activated without it. - SSL decryption must be enabled on NGFW and Access (this   requires a separate professional services quickstart if not   already enabled). - The App-ID Cloud Engine (ACE) is disabled by default on   Panorama and enabled by default on firewalls when the SaaS   Security Inline license is installed as part of CASB   activation. As a best practice, the majority of policies   are app based and since the app classification changes   due to CASB activation, you would need to disable ACE on   all firewalls including Prisma and CNGFW by making   changes to appropriate templates.  Usually you   would not push changes during production hours and   therefore CASB activation should only be carried out   during maintenance period. |

The Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license contains all the cloud access security broker
components such as SaaS Security Inline, SaaS Security API, SaaS Security Posture
Management (SSPM), and Enterprise DLP. It can be applied on Cloud Managed Prisma Access, Panorama Managed Prisma Access, and Panorama managed
Next-Generation Firewall (NGFW) devices in a single tenant environment.

If you are trying to activate the CASB-X on Prisma Access add-on bundle, [activate a license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons instead. CASB-X is only
supported in a single tenant environment, but the CASB add-on bundle is supported in
single and multitenant environments.

If you have Prisma Access or NGFW in your tenant, you can apply CASB-X to the Prisma Access or NGFW devices in that
same tenant.

You cannot activate CASB-X if you already have the CASB
add-on bundle, or the add-ons associated with the bundle, activated on your
tenant. You cannot activate CASB-X if you do not have
Strata Logging Service activated on your tenant.

To convert a trial SaaS Security license to a production license, see
[convert trial license to production](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/convert-trial-license-to-production.html)

Welcome to CASB-X activation. Select
Activate Subscription in your email, then use one of the
following options:

- [First time activation - one CSP
  account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-first-time-one-csp.html#casb-x-one-csp)
- [First
  time activation - multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-first-time-multiple-csp.html#casb-x-multiple-csp)
- [Return visit activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-repeat-visits.html#caxb-x-return)

### First time CASB-X Activation - One Customer Support Portal Account

Learn how to activate your CASB-X application for the first time
if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time CASB-X activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X on NGFW, you must go to the Device
   Association tab to select the devices and apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### First time CASB-X Activation - Multiple Customer Support Portal Account

Learn how to activate your CASB-X application for the first time
if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time CASB-X activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.

   ![]()
5. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X on NGFW, you must go to the Device
   Association tab to select the devices and apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Return Visit CASB-X Activation

Learn how to activate your CASB-X for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.

   ![]()
5. **Agree to the terms and conditions**, and **Activate**.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X
   on NGFW, you must go to the Device Association tab to select the devices and
   apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-7"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation>*

### Cloud Identity Engine Activation

Learn about Cloud Identity Engine (CIE) activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- The Activation Console - Commercial deployments | - Customer Support Portal account |

Welcome to Common Services
Cloud Identity Engine (CIE) activation. Use one of the following options:

- [First time activation - one CSP
  account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/activate-cie-first-time-one-csp.html#cie-one-csp)
- [First time activation - multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-cie-first-time-multiple-csp.html#cie-multiple-csp)
- [Return visit
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/activate-cie-repeat-visits.html#return)
- [Share Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/share-cie-subscriptions.html#share-cie)

### First time Cloud Identity Engine Activation

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have only one Customer Support Portal account.

Follow these steps for first time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select
   Activate.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.

   ![]()
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

### First time Cloud Identity Engine Activation - Multiple Customer Support Portal Account

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select Activate.
2. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
3. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

      After you create a tenant hierarchy, you can [share a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/share-cie-subscriptions.html).
   3. Select Done.
4. Select a Region where you want to deploy your product.
5. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
7. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
8. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

### Return Visit Cloud Identity Engine Activation

Learn how to activate your Cloud Identity Engine for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. From the Activation Console, select Activate.
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

### Share Cloud Identity Engine

Learn how to share Cloud Identity Engine (CIE) on tenants through Common Services.

After you activate Cloud Identity Engine on a tenant and [add child tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you can share
(CIE) with the child tenants in your hierarchy.

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

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html)
   Tenant Management.
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

<a id="cs-common-services-license-activation-subscription-tenant-management-8"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation>*

### Activate SaaS Security Inline

Learn about SaaS Security Inline activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- From email activation link - Commercial deployments | - Customer Support Portal account |

Welcome to SaaS Security Inline activation. [SaaS Security Inline](https://docs.paloaltonetworks.com/content/techdocs/en_US/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/whats-saas-security-inline.html#idf9f840a9-055f-4320-9c1f-b0e46e5f4eed) is a security service
that offers advanced risk scoring, analytics, reporting, and security policy rule
authoring so that your organization has the SaaS visibility and security controls to
prevent data security risks of unsanctioned SaaS app usage on your network. Select
Activate Subscription in your email, then use one of the
following options:

- [First time activation - one CSP
  account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-first-time-one-csp.html#saas-inline-one-csp)
- [First time activation - multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-first-time-multiple-csp.html#saas-inline-multiple-csp)
- [Return visit activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-repeat-visits.html#saas-inline-return)

### First time SaaS Security Inline Activation - One Customer Support Portal Account

Learn how to activate your SaaS Security Inline application for the first time
if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time SaaS Security Inline activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### First time SaaS Security Inline Activation - Multiple Customer Support Portal Account

Learn how to activate your SaaS Security Inline application for the first time
if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time SaaS Security Inline activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Return Visit SaaS Security Inline Activation

Learn how to activate your SaaS Security Inline for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-9"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation>*

### Activate SaaS Security Posture Management

Learn about SaaS Security Posture Management activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- From email activation link - Commercial deployments | - Customer Support Portal account |

Welcome to SaaS Security Posture Management activation. [SaaS Security Posture Management](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm) helps detect and
remediate misconfigured settings in sanctioned SaaS applications through continuous
monitoring. Select Activate Subscription in your email, then
use one of the following options:

- [First time activation - one CSP
  account](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-first-time-one-csp.html#sspm-one-csp)
- [First time activation - multiple CSP accounts](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-first-time-multiple-csp.html#sspm-multiple-csp)
- [Return visit
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-repeat-visits.html#sspm-return)
- Convert SaaS Security Posture Management
  [from evaluation to production](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/convert-sspm-evaluation-to-production.html#sspm-convert)

The SaaS Security Posture Management license is a standalone license that is available only on
tenants. It does not require any other app or prerequisite.

If you are looking for an app bundle that includes SSPM, see the [Next
Generation Cloud Access Security Broker (CASB-X) for cross platform](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation.html)
license or the CASB on Prisma Access add-on bundle when [activating a license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons.

### First time Activation - One Customer Support Portal Account

Learn how to activate your SaaS Security Posture Management application for the first time if you
have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time SaaS Security Posture Management activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access or NGFW available in
   this tenant where you can associate firewalls or devices.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
8. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from email:

     ![]()
   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesProducts:

     ![]()
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### First time SaaS Security Posture Management Activation - Multiple Customer Support Portal Account

Learn how to activate your SaaS Security Posture Management application for the first time if you
have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time SaaS Security Posture Management activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
8. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from email:

     ![]()
   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesProducts:

     ![]()
9. [Get Started with SSPM](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/whats-sspm)
   documentation.
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Return Visit SaaS Security Posture Management Activation

Learn how to activate your SaaS Security Posture Management for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

### Convert SSPM Evaluation to Production Through Common Services

Learn how to convert a standalone SaaS Security Posture Management (SSPM) evaluation
license to a production license on a single tenant through Common Services.

If you have an evaluation license for standalone SaaS Security Posture Management
(SSPM), you can convert it to a production license. After you receive an email from
Palo Alto Networks identifying the SSPM license you are converting, click the email
link to begin the activation process.

1. Select Get Started with SaaS Security Posture Management
   (SSPM) in your email.
2. You are automatically directed to Common ServicesSubscription & Add-ons, where you activate the subscription for your product.
3. Use one of the following activation methods.

   - Select your existing Tenant to convert your
     evaluation license to a production license on the existing tenant:

   ![]()

   - Select Create New to convert your evaluation
     license to a production license on a new tenant:

   ![]()
4. The Customer Support Account is auto-populated with the
   same CSP that you used for the evaluation.
5. The Region is auto-populated with the same region that
   you used for the evaluation.
6. Agree to the terms and conditions, and
   Activate.
7. .
8. Common ServicesTenant Management displays the status of the activation, such as
   initializing or
   complete.
9. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesTenant Management. You’ll notice that you have a new
     Contract serial number:

     ![]()
10. [Get Started with SSPM](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/whats-sspm)
    documentation.
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-10"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation>*

### Software NGFW Credits Activation

Learn about VM-Series, funded with Software NGFW Credits activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Activation Console - Commercial deployments - Strata Cloud Manager for NGFW - IoT Security | - Customer Support Portal (CSP) account with a Software   NGFW Credits deployment profile enabled - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Multitenant   Superuser, Superuser, Business Administrator, or   View Only Administrator |

The Software NGFW Credits is a [VM-Series](https://docs.paloaltonetworks.com/vm-series/9-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-firewall-licensing) flexible consumption model based
on tokens, compatible with the following licenses that are supported for a [tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html):

- [IoT](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/activate-vm-flex-iot.html#task-vm-flex-iot)
- [Strata Cloud Manager to Manage
  VM-Series](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/activate-vm-flex-ngfw.html#task-vm-flex-aiops)
- [Strata Cloud Manager for
  Panorama Managed VM-Series](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/aiops-panorama-credits.html#task-aiops-panorama-credits)

### Activate a Software NGFW Credits License for IoT Through Common Services

Learn how to activate a Software NGFW Credits License for IoT on a tenant through
Common Services.

1. After you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal (CSP) of VM-Series for
   IOT, then you can activate your subscription.
2. After the profile is complete in the CSP, select Finish
   Setup. This redirects you to the hub Subscription
   & Add-ons, where you select Activate
   Now to activate the subscription for your product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you just created and enter a unique
   subdomain to complete the
   <subdomain>.iot.paloaltonetworks.com URL for
   your IoT Security app (this will be the URL where you log in to the IoT Security
   portal).
7. Agree to the terms and conditions, and
   Activate.
8. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
9. After the status is complete, which can take up to
   five minutes, you can do one of the following:

   - Go to the CSP to [register the firewall](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/register-the-vm-series-firewall-software-ngfw-credits).
   - Go to the hub Common ServicesDevice Associations tab to see the firewall devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
10. After the status is complete, you can launch
    Software NGFW for IoT from one of the following options.

    - Launch from email.
    - Launch from the hub tile.
    - Launch from Common ServicesTenant Management.
11. Get started with [IoT Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin/get-started-with-enterprise-iot-security).
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Activate a Software NGFW Credits License of Strata Cloud Manager for NGFW Through Common Services

Learn how to activate a Software NGFW Credits license of Strata Cloud Manager
for NGFW on a tenant through Common Services.

Use Strata Cloud Manager to manage VM-Series.

1. After you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal (CSP) for VM-Series for
   SCM, then you can activate your subscription.

   If you have enrolled to a cloud service subscription (consisting of IoT,
   SaaS Inline, Strata Cloud Manager, Strata Cloud Manager Pro, and Strata
   Logging Service), you will need to activate additional licenses on your
   tenants after you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on
   the Customer Support Portal. For more information, see [activate the deployment
   profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile-vm-series).
2. After the profile is complete in the CSP, select Finish
   Setup. This redirects you to the hub Subscription
   & Add-ons, where you select Activate
   Now to activate the subscription for your product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you created, Agree to
   the terms and conditions, and Activate.
7. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing,
     associating, or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
8. After the status of the license activation is
   complete, which can take up to five minutes,

   - Go to the CSP to [register the firewall](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/register-the-vm-series-firewall-software-ngfw-credits).
   - Use the auth code while bringing up a VM. The auth code is associated
     with this consumption model. When the license database sees the auth
     code request come in from the VM, it will automatically call hub with
     this information. At this point, the new VM serial number will be added
     to the TSG associated with the deployment profiles for Software NGFW.
   - Go to the hub Common ServicesDevice Associations tab to see the firewall devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. After the status is complete, you can launch
   Strata Cloud Manager for NGFW from the hub Common ServicesTenant Management.
10. Get started with Strata Cloud Manager
    [for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

### Activate a Software NGFW Credits License for AIOps for NGFW Premium on Panorama Through Common Services

Learn how to activate a Software NGFW Credits License using AIOps for NGFW Premium (Strata Cloud Manager) for Panorama Managed VM-Series on
a tenant through Common Services.

Use Strata Cloud Manager for Panorama Managed VM-Series.

1. [Create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal for VM-Series for
   Strata Cloud Manager including the following options,
   then you can activate your subscription:

   If you have enrolled to a cloud service subscription (consisting of IoT,
   SaaS Inline, Strata Cloud Manager, Strata Cloud Manager Pro, and Strata
   Logging Service), you will need to activate additional licenses on your
   tenants after you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on
   the Customer Support Portal. For more information, see [activate the deployment
   profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile-vm-series).

   - Panorama for Management
   - Panorama as Dedicated Log Collector
   - Strata Cloud Manager

   ![]()
2. After the profile is complete in the Customer Support Portal, select
   Finish Setup. This redirects you to the hub
   Subscription & Add-ons, where you select
   Activate Now to activate the subscription for your
   product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you just created,
   Agree to the terms and conditions, and
   Activate.
7. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing,
     associating, or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
8. After the status is complete, which can take up to
   five minutes,

   - Go to the Customer Support Portal to [provision Panorama](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/provision-panorama) or [migrate Panorama](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/migrate-panorama-to-a-flexible-license).
   - Go to the hub Common ServicesDevice Associations tab to see the Panorama devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. After the status is complete, you can launch
   Strata Cloud Manager for NGFW from the hub Common ServicesTenant Management.
10. Get started with Strata Cloud Manager
    [for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-11"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation>*

### Enterprise License Agreement Add-on Activation

Learn about Enterprise License Agreement Add-on activation.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Activation Console - Commercial deployments - AIOps for NGFW - Device Security | - Customer Support Portal (CSP) account with Enterprise   License Agreement (ELA) enabled - Strata Logging Service - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Multitenant   Superuser, Superuser, or Business   Administrator |

The add-on for ELA is a consumption model for large enterprises to assign
subscriptions in bulk to assets purchased from Palo Alto Networks.

ELA offers the flexibility to enable any of the following licenses that are supported
for a tenant or TSG:

- [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation/activate-ela-aiops-for-ngfw-premium.html#idb22044ba-c033-439c-9a80-e58818b072d9)
- [Device Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation/activate-ela-for-iot-security.html#activate-ela-for-iot-security)

You can start the ELA activation process in either the hub or Customer Support Portal
as described in the following sections.

### Activate ELA AIOps for NGFW Premium Through Common Services

Learn how to activate a premium add-on Enterprise License Agreement (ELA) of AIOps for NGFW Premium on a tenant through Common Services.

This task shows how to activate Enterprise License Agreement (ELA) for AIOps for NGFW
Premium license.

Strata Cloud Manager is now available, featuring two licensing tiers: Strata
Cloud Manager Essentials and Strata Cloud Manager Pro. This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service. See [Strata Cloud Manager License](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html).

1. Use one of the following activation methods.

   - Log into the [hub](https://apps.paloaltonetworks.com/apps) and
     activate from tenant view of the hubELA ActivationAIOps for NGFW:

   ![]()

   - Log into the Customer Support Portal and activate
     from Customer Support PortalDevicesELA AIOps Activation:

   ![]()
2. You are automatically directed to Common
   ServicesSubscription & Add-ons,
   where you activate the subscription for your product.
3. Select the same Tenant that you
   used for Strata Logging Service, so that you can associate ELA for AIOps on the same
   tenant where you want AIOps to be applied.
4. The Customer Support Account is
   grayed out, but is auto-populated with the same CSP that you used
   for Strata Logging Service.
5. The Region is grayed out, but
   is auto-populated with the same region that you used for Strata Logging Service.
6. The UI shows if you have Strata Logging Service available in this tenant
   where you can apply ELA for AIOps.

   ![]()
7. Agree to the terms and conditions,
   and Activate.
8. Common ServicesTenant Management displays
   the status of the activation, such as initializing or complete.
9. After the
   status is complete, you must go to
   the Common ServicesDevice
   Associations tab to select the devices
   and apply ELA for AIOps on them: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).

   If the status is not complete,
   you cannot apply ELA for AIOps on the devices yet.
10. After the status is complete,
    you can launch AIOps from one of the following options.

    - Launch from email.
    - Launch from the hub tile.
    - Launch from Common ServicesTenant Management.
11. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access). Assign
    role of [Superuser](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)
     or [Business Administrator](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions). The CSP-level access is not
    sufficient.

### Activate ELA for IoT Security Through Common Services

Learn how to activate an add-on Enterprise License Agreement (ELA) for IoT Security
on a tenant through Common Services.

1. Start the ELA activation process from either the hub or Customer Support
   Portal.

   **Hub**: Log in to the [hub](https://apps.paloaltonetworks.com/apps) and, from the tenant view, click ELA ActivationIoT Security at the top of the page.

   ![]()

   or

   **Customer Support Portal**: Log in to your [customer support portal](https://support.paloaltonetworks.com/Support/Index) account, select Products Enterprise AgreementsLicenses, and then click ELA-IoT
   Activation.

   ![]()

   Whether you start in the hub or Customer Support Portal, both actions load a
   magic link that opens the Activate IoT Security page on the hub.
2. Activate the IoT Security ELA for a tenant service group.
   1. Choose an existing [tenant service group (TSG) tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)
      or create a new one. A TSG essentially associates firewalls with
      applications such as IoT Security.
   2. Choose the firewall deployment region.
   3. Create a new IoT Security tenant URL by entering a unique subdomain to
      complete <subdomain>.iot.paloaltonetworks.com.

      This is the URL where you'll log in to your IoT Security portal.

      If you want to convert an existing IoT
      Security tenant from using one or more IoT Security licenses to an
      IoT Security Enterprise License Agreement, contact your Palo Alto
      Networks sales representative.
   4. Agree to the terms and conditions and then
      Activate.

      ![]()
3. Go to the Common ServicesDevice Associations tab to add firewalls to the TSG tenant, associate them with the
   IoT Security app, and then apply the Enterprise IoT Security ELA to them: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
4. In the Customer Support Portal, select ProductsDevices and view the entries in the License column for your firewalls to
   confirm that IoT Security is now applied to them.
5. Continue setting up IoT Security to work with your firewalls.

   To log in to your IoT Security portal, return to Common Services on the hub
   and select the IoT Security link on either the Tenant
   Management page or the Device Associations page.

   For IoT Security (Enterprise IoT Security Plus, Industrial IoT Security, or
   Medical IoT Security), see [Onboard IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/onboard-iot-security).

   For Enterprise IoT Security, see [Onboard Enterprise IoT
   Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin).
6. (Optional) Manage identity and access to IoT Security.

   To create an IoT Security user with owner privileges plus the ability to
   generate one-time passwords (OTPs) and pre-shared keys (PSKs), add a user
   account in the Customer Support Portal and assign a Superuser role in the
   relevant tenant service group (TSG) in Identity & Access (this is
   described in the following steps.) To create an IoT Security user with all
   owner privileges except the ability to generate OTPs and PSKs, add the new
   user account in Identity & Access and assign a Superuser role in
   Identity & Access. To create an IoT Security user with read-only
   privileges, add a user account in Identity & Access and assign a View
   Only user role in Identity & Access.

   1. (Optional) Add a user account in the Customer Support Portal.
      New users only need to be added to the Customer Support Portal accounts
      if they need access to operate onboarding or offboarding tasks, such as
      generating OTPs and PSKs. To create a new user in the Customer Support
      Portal:

      1. Log in to the [Customer Support
         Portal](https://support.paloaltonetworks.com/) with superuser permissions, which allow you to
         create new user accounts.
      2. Select Members Create New User, enter the required information, and then
         Submit.

      A new user account is created and added to the account as a member.
      An email notification is sent to the new user with login
      credentials.
   2. Log in to the [hub](https://apps.paloaltonetworks.com/), navigate to Common ServicesIdentity & Access/Access Management.
   3. [Add Identity](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-users).

      Users added in the Customer Support Portal are separate from users
      added in Identity & Access.
   4. To assign a [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) to the user you created,
      select the user, Assign Roles, choose
      IoT Security in Apps & Services, choose
      one of the options in Role, and then Assign
      Role.

---

<a id="cs-manage-subscriptions"></a>

### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

#### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

#### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

#### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

#### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

#### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

#### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

#### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="cs-manage-subscriptions-1"></a>

#### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/licensing-models>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

##### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

##### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

##### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

##### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

##### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

##### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

##### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="cs-manage-subscriptions-2"></a>

#### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/license-activation-diagnostics>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

##### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

##### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

##### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

##### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

##### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

##### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

##### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="cs-convert-a-trial-to-a-production-license"></a>

#### Convert a Trial to a Production License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/convert-trial-license-to-production>*

This section contains instructions to convert a trial to production
license.

When a trial subscription is converted to a production subscription, you will receive
a welcome email with an activation link. Proceed to activate using one of the
following procedures:

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/sase-trial-to-prod.html#topic-65d32790-d974-4843-bcd9-f8c21eabb497)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/firewall-trial-to-prod.html#topic-fcf7f43c-ca76-4aa3-9957-a59732cf3989)

#### SASE

This section contains instructions to convert a trial license of SASE Products to
Production license

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

When a trial entitlement is converted to a Production entitlement, you’ll
receive a welcome email that includes a direct link to the Activation Console. Use
this link to access the Activation Console and begin the activation process.

To convert the trial to a production license, perform the following:

1. In the Activation Console, navigate to the Subscriptions
   tab. The new production entitlement appears with a Needs
   Activation status.

   ![]()
2. Select Activate next to the production
   entitlement.
3. Select the desired Tenant. You can choose the existing
   trial tenant or a new tenant for deployment flexibility.
4. Select a Region nearest to the storage location of the data logs if you are
   changing the tenant.
5. Select the existing trial license you wish to replace in the
   Replaceable License section.

   ![]()
6. Agree to the terms and conditions, and select Activate
   Now.

#### Firewall and SD-WAN

This section contains instructions to convert firewall and SD-WAN trials to
production license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

Use the activation link provided by Palo Alto Networks to convert your existing
trial subscription license to a production license. Additionally, you can use this
opportunity to convert both the active trial licenses and to activate the production
license for your subscription for unlicensed tenants or devices at the same time.

1. Purchase the production license or subscription for your product.

   You need to contact your Palo Alto Networks sales representative to purchase
   the production license.
2. Click the activation link to begin the license conversion.

   The activation link is provided to you in an email from Palo Alto Networks.

   (Next-Gen Firewalls) Subscriptions are activated using an
   activation link only. Contact Palo Alto Networks
   [Customer Support](https://support.paloaltonetworks.com/) to continue the license
   conversion if you receive an email that does not include an activation
   link for your license conversion, and instead only includes auth codes.

   Do not activate the auth codes on your Next-Gen firewalls. Activating
   these auth codes may require Palo Alto Networks Customer Support to
   delete the trial license you want to convert. In some cases, this may
   cause your Next-Gen firewall to be restored to factory defaults and
   delete all existing configurations associated with the subscription.
3. Follow the activation procedure for your subscription.

   You must select the same tenant where the trial license is active to convert
   it to a production license. Additionally, you can use the same activation
   flow to convert trial licenses to production licenses and to activate the
   production license on tenants or devices with no active license at the same
   time.

---

<a id="cs-manage-subscriptions-3"></a>

#### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/request-eval-to-prod>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

##### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

##### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

##### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

##### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

##### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

##### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

##### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="cs-manage-subscriptions-4"></a>

#### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/modify-subscription>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

##### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

##### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

##### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

##### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

##### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

##### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

##### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="cs-modify-license-allocation"></a>

#### Modify License Allocation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/modify-license-allocation>*

This section contains instructions to modify your license allocation to other
tenants.

You can increase or decrease license allocations for a tenant after
activation. When you reduce a tenant’s allocation, the reduced quantity returns to
your license pool, and you can reallocate it to another tenant to maximize license
utilization across your organization. If you reduce license capacity for a Tenant
Service Group (TSG), a fully allocated license automatically converts to a shared
allocation.

When you purchase additional license capacity, it is no longer allocated to
existing TSGs by default. Instead, you decide whether to assign the new capacity to
the same TSG or distribute it across multiple TSGs, depending on your organization’s
needs. For example, if you purchase additional licenses for a new tenant, you can
directly allocate the new capacity to that tenant, or adjust allocations across
existing tenants as needed.

When you reduce the license capacity:

- You cannot reduce allocations below 200 users, the minimum required
  for service continuity.
- You can only reduce licenses in multiples of 10.
- When you reduce base license quantities, associated add-ons such as
  ADEM-AIOps, ZTNA Connector, or Remote Browser Isolation automatically adjust
  to maintain alignment.
- The mobile users and remote networks quantity can be reduced to
  either minimum quantity or it can also be made zero by deselecting those
  options.
- You cannot reduce the license capacity for Panorama Managed
  tenants.

All superusers, multitenant superusers, and business administrators of the
TSG will receive notification when you reduce license capacity. If the reduction
requires configuration changes (for example, adjusting bandwidth for sites), you
must make these changes before committing the configuration. Until then, commits are
blocked with a license quantity mismatch message.

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/sase-modify-lic-allocation.html#topic-35ba94d8-7ae0-4936-9a31-8sdwd520698bff1e)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/firewall-modify-lic-allocation.html#topic-a277402e-0556-4ab9-af0e-7d48c08c617d)

#### SASE

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click ⋮Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   Note: If you are modifying the allocation for the default tenant, ensure
   that you reduce the assigned license quantity. The reduced quantity
   becomes available for reallocation to other tenants in the
   hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat from the [Step 3](#cs-modify-license-allocation) to allocate licenses
   to additional tenants.

   Validate the license allocation by switching to the corresponding tenant in
   the tenant browser and reviewing the allocation details.

   ![]()

#### Firewall and SD-WAN

This section contains instruction to modify license allocation in firewall
products.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html) the
   Subscription.
2. [Search the subscriptions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions.html) table with
   your Tenant Service Group ID (tsg\_id).

   For the filtered TSG, you can verify the status of the assigned quantity
   compared to the total quantity. You also see the associated tenants where
   the subscription is currently allocated.

   ![]()
3. From Actions, select Activate Cloud
   Tenant.

   You will be directed to the Activate Subscription
   page.
4. Select an existing tenant or create a new tenant.
5. Modify the license allocation and select Done.

   ![]()
6. Agree to the Terms and Conditions and Activate.
7. In both Subscription and Tenant
   Management, you can verify the change in license
   allocation.

   ![]()

---

<a id="cs-extend-or-renew-a-subscription"></a>

#### Extend or Renew a Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/extend-subscription>*

Learn how to extend or renew a subscription through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can extend or renew your expiring license through Common Services. After
you request an extension from IT, and your updates are ready for use, you will
receive an activation link in your email.

- The following steps apply if you allocated part of your production license
  during the initial activation and you [share the license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) between multiple
  tenants.
- The following steps also apply if you allocated part of your evaluation
  license during the initial activation, you [share the license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) between multiple
  tenants, and you are converting to a production license.
- This does not apply to a full allocation or to a single tenant environment,
  regardless of production license extension or evaluation license to
  production conversion. In a full allocation or single tenant environment,
  there are no additional steps after clicking the activation link.

1. Click the activation link in your email.
2. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Common ServicesTenant Management.
3. Select Tenant Management. Only one way is shown
   here.

   ![]()
4. In Tenant Management, you see blue dots indicating that you need to take
   further steps.
5. Use the blue dots to find the tenant with the subscription that you need to
   extend, select the Tenant Name  and
   Edit the licensed products.

   ![]()
6. Agree to the terms and conditions and
   Activate Now.

---

<a id="cs-expiring-and-expired-subscription"></a>

#### Expiring and Expired Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-subscription>*

Learn how to track and manage about to expire and expired subscriptions to avoid
service interruptions.

This section explains how to monitor expiring and expired subscriptions and take
timely action to maintain uninterrupted service. It describes how subscription
statuses are visually indicated, where expired subscriptions are listed.

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/sase-expiring-subscription.html)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/firewall-expiring-subscription.html)

#### SASE

Details about where to find the expiration details and the visual indicators to
identify them.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama or Strata Cloud Manager) - Prisma Browser - Remote Browser Isolation - Next-Generation   CASB for Prisma Access and NGFW - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.

  ![]()
- Expired licenses will have 

  ![]()

  icon next to their expiration date to identify
  expired licenses.

  ![]()

#### Firewall and SD-WAN

Learn how to track and manage about to expire and expired subscriptions to avoid
service interruptions.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.
- Expired subscriptions are listed separately under the
  Expired tab for easy access.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html)
   Common ServicesSubscriptions & Add-ons.
2. Select Subscriptions & Add-ons. (This example
   demonstrates one method.)

   ![]()
3. In the Active tab, view all active subscriptions,
   including those expiring within 30 days

   - Expiring subscriptions have the

     ![]()

     icon next to their expiration date.
   - If you have renewed a subscription but it has not yet become active,
     those subscriptions have the 

     ![]()

     icon next to its start date.

   ![]()
4. To view expired subscriptions, go to the Expired
   tab.

   ![]()

---

<a id="cs-deactivate-a-product"></a>

#### Deactivate a Product

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/deactivate-product>*

This section contains instructions to deactivate a product and then reuse the tenant
or the license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can deactivate either an individual product or all products associated
with a Tenant Service Group (TSG). Deactivation helps you manage tenant resources
efficiently by allowing you to reuse existing tenants and make optimal use of
available licenses.

When you deactivate a product, it is removed from the tenant, and the
associated license can be reallocated to another tenant

You can deactivate:

- **All the products in a tenant:** Deactivate every product
  linked to the tenant.
- **Individual product:** Deactivate a single product from the
  tenant. This is supported only for Cloud Identity Engine and Security
  Lifecycle Review (SLR)

When you deactivate or remove all the products in a tenant, all its add-ons will also
be deactivated and removed from the tenant. After you initiate deactivation, you
have a 24-hour grace period to cancel the deactivation.

When you initiate deactivation, all the superusers will receive an email notification
during all the states of the activation process, such as scheduled deactivation,
deactivation successful, and deactivation failure.

- [Deactivate All Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all.html#topic-87d9ebf3-db73-4a08-80c4-2b1af9718476)
- [Deactivate Individual
  Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products.html#topic-9aef1da4-09af-471f-81b5-c3d6103fe68c)

#### Deactivate all Products

This topic contains procedure to deactivate all the products in the
tenant.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you
   have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate all the products in the tenant, click the Deactivate
   Products icon.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

#### Deactivate an Individual Product

This topic contains to deactivate specific products from the tenant.

1. Use one of the[various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you have a single
   tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate individual products, go to Actions  Deactivate Product.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="cs-tenant-management"></a>

### Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants>*

Learn how to add, delete, move, and acquire tenants.

You can create and manage a hierarchy of business organizations and units, each of which is a
[tenant](#). For each tenant, you specify a name that helps
you and others to easily identify it, such as the company name, a division,
or a geographic location (along with a business vertical designation, such
as retail or wholesale). You will allocate licenses to your tenants so that
you can manage and monitor the instances of all your products. For more
information about tenants, see [What is a Tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html#id6444f457-9deb-4cc5-8bf1-3c7eb0ab2ba4)
or the Common Services
[FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq).

Depending on your environment, you will see one of the following menus for
managing your tenants: Tenant Management or
Tenants.

You won't see this menu if you have a single tenant. You will see
Products instead. In a single tenant
environment, you can manage your products through [product management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-products.html).

|

Prisma SASE Multitenant Portal and FedRAMP | Multienant View of the Activation Console | Multitenant Strata Cloud Manager |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

From the original support account view of the Activation ConsolePrisma SASE Platform button Tenants and ServicesCommon Services, you will see Tenant Management. | From the tenant view of the Activation ConsoleCommon Services  button, you will see Tenant Management in a multitenant environment. | From the Strata Cloud Manager System Settings, you will see Tenants  in a multitenant environment. |

In a multitenant environment, you can switch between your tenants and also
between the apps or products in the tenant.

![]()

---

<a id="cs-what-is-a-tenant"></a>

#### What is a Tenant?

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant>*

Learn about tenants, Tenant Service Groups, and TSGs. A tenant is a logical container for
managing and monitoring licensed products. Tenant Service Groups enable the management of
multiple customers or business units in a tenant hierarchy that reflects your existing
organizational structure. Each tenant is isolated and can have its own set of policies and
resources, while still being managed from a single location.

Common Services enables you to manage a hierarchy of business units and organizations that
is referred to as a [tenant service group](#). A tenant service group (TSG) is
used to provide a logical container that contains [tenants](#) and other TSGs.
It is the building block for a multitenant hierarchy. Generally, this multitenant
hierarchy is described as a series of nested tenants, where a tenant is used to manage,
monitor, and license products. But mechanically, a tenant is just a TSG. The terms are
often used interchangeably.

After you have received information about the transition of your app instance to a tenant, your
instance is now a single tenant. You have access to Common Services for
subscription management, tenant management, and identity and access management. You do
not have access to the multitenant summary dashboards, as those are not applicable and
not available for single tenants. See the [FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq) if you have more questions about the migration.

Each tenant is automatically assigned a TSG ID, which is primarily for use with [service accounts](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts). However, the TSG ID is also
used for default login purposes. If you clear your cache, or if you log out of the
Strata Multitenant Cloud Manager and log back in, you are logged into the top-level parent
tenant with the lowest TSG ID by default. The top-level parent tenant with the lowest
TSG ID is likely the first one you created.

The [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants) explain the number of
used and unused tenants you can create.

---

<a id="cs-add-a-tenant"></a>

#### Add a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants>*

Learn about adding a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

After you create a tenant, you can allocate a supported product license to it or you can create a
child tenant and allocate the license to it. Licenses are allocated per each child
tenant that you need to manage.

If you are adding a tenant for the first time, you are automatically directed to
Tenants when you follow the license activation flow flow,
in which case you can skip to the [select a tenant](#cs-add-a-tenant) step.

If you are not adding a tenant for the first time or you are otherwise not following the general
flow, you can add a tenant from Tenants.

You can create your tenant
hierarchy to reflect your existing organizational structure. You
can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when
creating the hierarchy, in addition to [tenant hierarchy
limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are basically the same.
2. Select a tenant to be the
   parent of the child tenant you want to add.
3. Select New Tenant.

   ![]()
4. Specify a Name for the child that
   is representative of its function and select a Business Vertical.

   ![]()

   The
   Business Vertical is used for summarizing tenant network traffic
   information.
5. Select the **Telemetry Tier**, which defines the type of telemetry data
   transferred to the **Data Region** for monitoring and analysis.

   - Full (Recommended)- collects comprehensive data
     to support in-depth monitoring and analysis. This is the default
     setting.
   - Diagnostic- collects only essential data required
     for diagnostics and troubleshooting.

   To learn more about the data collected in each tier, see [Device Telemetry Metrics
   Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

   Telemetry Tier must be set to Full if the tenant
   includes Strata Cloud Manager.
6. Select the Data Region  where the telemetry data will be
   stored.

   - You cannot edit the region if Strata Logging Service, Strata Cloud
     Manager, or IOT Security is already enabled in the tenant.
   - If you add Strata Logging Service, Strata Cloud Manager, or IOT
     Security to the tenant later, the data region automatically switches
     to the region used by that product.
7. Specify a Support
   Contact, such as an email address or a phone number
   of a person to contact for support purposes. The maximum character
   limit for the contact is 255.

   - Select Inherit from parent if
     the contact person is the same as the parent.
   - Select Use custom if the contact person
     is different from the parent.
8. Set the User Inactivity Timeout to automatically log out
   idle users after a specific period. The default timeout is 30 minutes, but you
   can customize this value between 10 and 60 minutes. Choose a shorter or longer
   duration based on your organization's security policy and operational needs.
   This flexibility allows you to balance security requirements with user
   convenience.

   When no timeout value is set, new tenants automatically adopt the default
   timeout value from their parent tenant. Once you customize the timeout
   value, it becomes independent and is maintained separately for that
   tenant.
9. Add Tenant as a child of the current
   parent tenant in the tenant hierarchy.

   ![]()
10. (Optional) Specify license and activation details
    for your product.

---

<a id="cs-edit-a-tenant"></a>

#### Edit a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/edit-tenants>*

Learn about editing a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

When you create a tenant, you define attributes such as name and support contact to
describe its purpose and management. You can edit these tenant details at any time,
for example, when a support contact changes. This topic outlines the process for
editing tenant details.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are the same.
2. Select the tenant that you
   want to edit.
3. Select Edit Tenant.

   ![]()
4. Change any of the details about the tenant, as needed.

   - Name—Descriptive name that identifies the
     tenant.
   - Business Vertical—Primary industry or sector in
     which the tenant operates. This helps categorize and understand the
     tenant's main focus and potential needs. (For example,
     Wholesale & Retail.)

     Support
     Contact—Information of a person to contact for
     support purposes. (For example, John Smith, IT Manager -
     jsmith@globaltech.com, +1 555-123-4567)
   - User Inactivity Timeout—Number of minutes after
     which Strata Cloud Manager will log idle users out of the tenant.
     Choose a value between 10 and 60 minutes (30 minutes is default).

     New tenants automatically inherit the default
     timeout value from the parent tenant. After you modify the timeout
     value for a child tenant, the value is maintained independently.
   - Telemetry
     Tier—the type of telemetry data transferred to the **Data
     Region**.
     - Full (Recommended)- collects
       comprehensive data to support in-depth monitoring and analysis.
     - Diagnostic- collects only essential data
       required for diagnostics and troubleshooting.

     To learn more about the data collected in each tier, see [Device Telemetry Metrics
     Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

     - Downgrading from **Full** to **Diagnostic** may
       result in the loss of critical telemetry data needed for
       advanced analysis and support.
     - Only the super user can edit the Telemetry
       Tier.
     - Telemetry Tier must be set to Full if
       the tenant includes Strata Cloud Manager.
   - Data Region—the
     region where the telemetry data is stored.

     If
     Strata Logging Service, Strata Cloud Manager, or IOT Security is
     already enabled in the tenant, you cannot edit the region. It
     defaults to the product region.
5. Save.

---

<a id="cs-manage-tenant-licenses"></a>

#### Manage Tenant Licenses

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/manage-tenant-licenses>*

If you are activating a license for the first time, you will use a license activation flow.

If you are not activating a license for the first time or you are otherwise not following a
general flow, you can claim a license from Subscription &
Add-ons. Then you can activate it from Tenant
Management.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Common ServicesTenant Management.
2. Select Tenant Management. Only one way is shown
   here.

   ![]()
3. Edit the licensed products.

   ![]()
4. The rest is similar to [activating a license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons.
5. (Optional) [Monitor tenant licenses](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-tenant-licenses).

---

<a id="cs-delete-a-tenant"></a>

#### Delete a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/delete-tenants>*

Learn about deleting a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

After you create a tenant, you can delete it only if the tenant meets the following criteria:

- No activated products, which can be seen from Tenants.
- No child tenants, which can be seen from Tenants.
- No licenses allocated or claimed, which can be seen from Subscriptions &
  Add-ons.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are the same.
2. Select the tenant you want to delete and Delete
   Tenant.

   ![]()
3. Select Yes, Delete this Tenant to
   confirm deletion.

   ![]()

   Tenant
   deletion is successful only if the tenant does not have any child
   tenants and only if the tenant does not have any instances provisioned
   for it. If the tenant does have child tenants, delete those children
   first before you delete this tenant. If the tenant has an instance
   provisioned for it, remove the licenses before you delete the tenant.

---

<a id="cs-transition-from-single-tenant-fedramp-to-multitenant-fedramp"></a>

#### Transition from Single Tenant FedRAMP to Multitenant FedRAMP

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/transition-from-single-tenant-to-multitenant>*

Learn how to transition your single tenant Prisma Access FedRAMP to multitenant
FedRAMP.

If you are a new cloud-managed Prisma Access FedRAMP High "In Process" customer as of
December 2023, you can use the following information to transition
from a single tenant deployment to a multitenant deployment.

After you receive an email from Palo Alto Networks identifying the license you are activating,
including all your add-ons and capacities, Get Started
with Prisma Access to begin the
activation process.

1. To transition from a single tenant Panorama-managed Prisma Access to multitenant, select Get
   Started with Prisma Access in
   your email.
2. Follow the steps to [Activate a License
   for Single Tenant Cloud-Managed](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation)
   Prisma Access FedRAMP, but do not
   Launch the products
   yet.
3. Instead, select Tenant Management.
4. Select +Add
   tenant.

   ![]()
5. Adding a subtenant converts your single tenant to a multitenant
   hierarchy. Select Yes to continue.
6. [Manage your tenants
   through the](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started) Multitenant Cloud Manager.

---

<a id="cs-move-an-internal-tenant"></a>

#### Move an Internal Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/move-internal-tenants>*

Learn how to move an internal tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

If you're a managed security service provider (MSSP) or distributed enterprise and
you [create a
multitenant hierarchy](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you might need to move a tenant that is part of
your tenant hierarchy to a different location. You can do this by moving an internal
tenant.

Any tenant is considered an internal tenant if it's within your tenant hierarchy, and
you have Superuser access to the source and target tenants. It's possible to move
tenants within the same top-most, root-level, parent tenant or intermediate tenants
of your hierarchy. See [additional limitations](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition.html). You
would move an internal tenant primarily in the case of testing, demonstrations,
reorgs, correcting mistakes, and more.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Settings.
2. Select Tenants.
3. From the tenant that you want to move, select Move
   Tenant.

   In the following example, the source tenant is Child Tenant East. You must
   have the Superuser role for Child Tenant East to move this tenant to a new
   location in the hierarchy.

   ![]()
4. You’re prompted with a view of the current tenant hierarchy, so that you can
   select where to move the tenant. Select a new parent tenant for managing the
   subtenant and **Continue**.

   In the following example, the target tenant is Child Tenant West. You must
   also have the Superuser role for Child Tenant West to move Child Tenant East
   to become its subtenant.

   ![]()
5. Inherited roles that would be lost after the move are displayed before the
   final confirmation. Select Confirm.

   Inherited custom roles that would be lost after the
   move are also displayed before the final confirmation. Custom roles that
   were defined in a parent tenant and assigned in a child tenant would be lost
   because the role doesn't exist in the new hierarchy.

---

<a id="cs-acquire-an-external-tenant"></a>

#### Acquire an External Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants>*

Learn how to acquire an external tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

If you are a Managed Security Service Provider (MSSP) or distributed enterprise and
you [create a
multitenant hierarchy](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you might need to acquire and manage tenants that
are not part of your current tenant hierarchy. You can do this by acquiring an
external tenant.

Any tenant is considered an external tenant if it isn’t within your current tenant
hierarchy. You can only acquire a top-most, root-level, parent tenant through an
external tenant acquisition. You would acquire an external tenant primarily in the
case of corporate acquisitions or mergers or reorgs. A tenant can have only one
outstanding acquisition request open at a time. See [additional limitations](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition.html).

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Settings.
2. Select Tenants.
3. From the parent tenant where you will manage your newly acquired target tenant,
   select Acquire New Tenant.

   ![]()
4. At the prompt, provide the TSG ID and superuser email addresses of the
   administrators who need to accept the pairing request.
5. Select Acquire Tenant.
6. The administrator of the target tenant needs to approve the request.

---

<a id="cs-approve-an-external-tenant-acquisition"></a>

#### Approve an External Tenant Acquisition

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/approve-external-tenant-acquisition>*

Learn how to approve an external tenant acquisition through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

After a Managed Security Service Provider (MSSP) or distributed enterprise submits a
request to [acquire an external tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html), the administrators of the newly
acquired target tenant receive an email notification and an acquisition key. Only
one administrator has to approve the request for the tenant acquisition.

If you’re an administrator of the target tenant, you have two choices for approving
the request.

1. (Optional) If you have the email, select View
   Request from the message.
   1. The acquisition key is prepopulated, so you can **Accept** the
      request. 

      ![]()
   2. Confirmation is displayed. Select Close.
2. (Optional) If you are one of the administrators contacted in the [request to acquire an external tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html), and you’re already logged
   into the Strata Cloud Manager, but you don’t have the email:
   1. Select View Request from the banner.
   2. At the prompt, you can select to resend the acquisition key.
   3. Enter the acquisition key from your email.
   4. Accept.
   5. Confirmation is displayed. Close.

---

<a id="cs-limitations-for-moving-and-acquiring-tenants"></a>

#### Limitations for Moving and Acquiring Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition>*

Learn about the limitations and caveats for moving internal tenants and acquiring
external tenants through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

The following limitations exist for managed security service providers (MSSP) or
distributed enterprises [moving internal tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/move-internal-tenants.html) and [acquiring external tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html).

- You can acquire only the top-most, root-level, parent tenant hierarchies. You cannot
  acquire intermediate tenants within a hierarchy.
- You can't acquire tenant hierarchies with [Service Provider Backbone](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/manage-service-provider-backbones) enabled in the
  hierarchy.
- It's not recommended that a tenant hierarchy without a Service Provider Backbone
  enabled be acquired into a tenant with a Service Provider Backbone enabled. The
  action isn't blocked, but can have inconsistent results.
- You can't acquire a tenant hierarchy with Prisma SD-WAN licenses in the hierarchy at this time.
- Users with access to a tenant that acquires a new target tenant will
  gain access to the target tenant through inheritance.
- Tenant support contacts won't be changed during a move.
- A tenant with no support contact will inherit the new owner's
  contact.
- If a tenant is using a shared Cloud Identity Engine instance, you can't
  acquire it until the shared instance is removed.
- A tenant will keep all custom role definitions created on it.
- All service accounts created on a given tenant will stay with that
  tenant after being moved.
- If some but not all contact email addresses provided are valid tenant
  users, they will still receive the approval request email. Invalid emails will
  be ignored.
- Invalid acquisition requests will fail silently, they will look like
  successful requests to keep tenant information secret from the user.

---

<a id="cs-tenant-hierarchy-limits"></a>

#### Tenant Hierarchy Limits

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants>*

Understand limits in the Common Services hierarchy.

Your multitenant hierarchy has limits for its size and
depth. These limits exist for performance and security purposes.

The tenant hierarchy is comprised of one or more trees of tenant service groups (TSGs). Each tree
has a root TSG. A TSG is a logical container that can contain child TSGs, as well as
licensed tenants.

|

Name | Limit | Description |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Hierarchy depth | 10 | Identifies the maximum depth for any given hierarchy tree, starting at depth 1 for the root TSG. |

|

Child TSGs | 100 | Identifies the total number of immediate children permitted for any TSG in the hierarchy. This limit applies only to immediate children of the TSG. It does *not* apply to all descendents (grandchildren, great-grandchildren, and so on) of the TSG. |

|

Unused root TSGs | 10 | Identifies how many unused root TSGs can exist in your Strata Multitenant Cloud Manager. A TSG is unused if it has no child TSGs or tenants. |

---

<a id="cs-edit-telemetry-settings"></a>

#### Edit Telemetry Settings

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/edit-telemetry>*

What is telemetry and how to edit the telemetry settings from the tenant management
page

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of Superuser,   Multitenant Superuser, Multitenant IAM Admin |

Telemetry refers to the [device data](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview) collected from your
Next-Generation Firewall (NGFW) or Panorama and sent to Palo Alto Networks. This data
enables cloud-based applications to monitor and manage your devices efficiently.

Telemetry data improves visibility into device health and performance, supports capacity
planning and configuration management, and helps share threat intelligence across
platforms. It also enhances intrusion prevention capabilities and allows for the
evaluation and continuous improvement of threat signatures.

Telemetry settings are configured only at the tenant level. This means that all devices
associated with a specific tenant automatically inherit the telemetry configuration
defined for that tenant.

**What is the default telemetry configuration?**

By default, when you activate a product, telemetry is auto-enabled and the telemetry tier
is set to full. This default setting ensures that the most comprehensive set of
telemetry data is collected from the start, enabling robust monitoring, diagnostics, and
threat analysis.

You can modify the telemetry tier at any time through the **Tenant Management** page
to suit your data collection preferences.

**What are the available telemetry tiers?**

There are two telemetry tiers available, depending on the level of data you want to
transmit:

- **Full**-This tier sends a complete set of telemetry data, including extensive
  device health metrics, configuration summaries, threat activity, and performance
  data for in-depth monitoring and analysis.
- **Diagnostic**-This tier limits the scope of data collected and focuses on
  basic diagnostic information required for troubleshooting and analysis.

To learn more about what each telemetry tier includes, see [Device Telemetry Metrics Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

**Where is the Telemetry Data Stored?**

Telemetry data is stored in a specific data residency region, which you can configure
during product activation or tenant creation.

If the tenant already includes Strata Logging Service, Strata Cloud Manager, or IoT
Security, the data region defaults to the region assigned to that product. In such
cases, you can’t manually select or change the data region.

The telemetry data from the PAN-OS and Panorama devices are transmitted to the data
residency region at fixed [transmission intervals](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-collection).

##### Edit Telemetry Tier and Region

You can modify the telemetry configuration, such as the telemetry tier and data
residency region, at any time from the [Tenant Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/edit-tenants.html) page.

Changes made at the tenant level automatically apply to all devices associated
with that tenant, ensuring consistent telemetry behavior across your deployment.
If the data residency region is configurable, you have the flexibility to update
it to meet your organization’s data governance requirements.

---

<a id="cs-product-management"></a>

### Product Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-products>*

Learn how to add, delete, and rename products .

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Single tenant environment | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

Activating a free product from the Activation Console creates a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where the product is
deployed.

If you have a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), you can view, launch,
and manage your products from Products.

|

Single Tenant View of the Activation Console | Single Tenant Strata Cloud Manager |

| --- | --- |

|  |  |
| --- | --- |
|

From the tenant view of the Activation Console Common Services  button, you will see Products in a single tenant environment. | From the Strata Cloud Manager Settings, you will see Products  in a single tenant environment.  Strata Cloud Manager is for commercial deployments only and not yet available for Prisma SASE FedRAMP Moderate or High "In Process." |

You won't see this menu if you're a managed security service provider
(MSSP) or distributed enterprise with a multitenant hierarchy. You
will see Tenants instead. In a multitenant
environment, you can manage and monitor your tenants through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants) and
the [Strata Multitenant Cloud Manager](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform).

From Products, you can launch a product by selecting it
from the product list. 

![]()

#### Get Product Information

From ActionsProduct Information, you can view the information about your product. You
can also copy the information to clipboard for pasting into any
support case you open for the product. 

![]()

#### Rename Instance

From ActionsRename Instance, you can rename the instance of the product. This isn't available for
every product.

#### Delete

From ActionsDelete, you can delete the instance of the product. This
isn't available for every product.

#### Manage Sharing

From ActionsManage Sharing, you can manage sharing of the product. Sharing of some instances are
not automatically inherited by child tenants and must be assigned individually. This
isn't available for every product.

#### Add Tenant

From Add Tenant, you can add a tenant to
transition from a single tenant environment to a multitenant
environment. In a multitenant environment, you can manage and
monitor your tenants through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants) and
the [Strata Multitenant Cloud Manager](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform).

#### Switch Between Products

In a single tenant environment, you can switch between the apps or
products in your tenant. 

![]()

Strata Cloud Manager is for commercial deployments only and not
yet available for Prisma SASE FedRAMP Moderate or High "In Process."
See [Fedramp Moderat and High
Support](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/fedramp-moderate-and-high-support).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-12"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/release-updates>*

### Common Services: Subscription and Tenant Management Release Updates

Learn about the latest features and known issues related
to Common Services: Subscription and Tenant Management.

Here’s where you can learn about the
latest features related to Common Services: Subscription
and Tenant Management and the known issues the team is working on
to improve your experience:

- [Known Issues](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/release-updates/known-issues.html#id21a2a697-7e64-45a9-97fd-de67d479b74b)
- [What’s New](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/release-updates/whats-new.html#idf6bb425a-c7f5-4d49-9309-65d0e6809606)

---

<a id="cs-common-services-license-activation-subscription-tenant-management-13"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/release-updates/known-issues>*

#### Known Issues in Common Services: Subscription and Tenant Management

Learn about the known issues related to Common Services: Subscription and Tenant Management.

These are the issues we’re currently working on. If no issues are listed, then there are no
outstanding known issues. You can also check known issues for [Prisma SASE Multitenant Portal](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/release-updates/known-issues-msp), [Identity and Access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/release-updates/known-issues), and [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/release-updates).

|

ID | Description |

| --- | --- |

|  |  |
| --- | --- |
|

**APPORTAL-6501** | If you receive an activation email to amend your Prisma Access license, you need to select the same single tenant or multitenant option that you chose for the original net-new Cloud-managed or Panorama-managed license activation. |

|

**APPORTAL-6445** | The functionality does not change automatically when you switch from a single tenant to a multitenant (or from multitenant to single tenant), then you go to the subscriptions tab in the UI. You have to close the browser and reopen a new session or you have to log out and log in again to see the new view in the subscriptions tab. |

|

**BAN-12889** | When converting firewalls that are licensed for IoT Security from an IoT Security subscription that doesn't require a data lake to one that does, Strata Logging Service log storage will not automatically be enabled for them.  **Workaround**: To enable log storage for firewalls after the license conversion, you must move firewalls to the appropriate data lake instance within the Strata Logging Service application. For instructions, see [Start Sending Logs to a New](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/move-firewalls-to-a-new-region). |

|

**APPORTAL-8673** | When integrating IoT Security in a hybrid environment with Prisma Access and next-generation firewalls, it’s not possible to activate IoT Security as a Prisma Access add-on after you onboard firewalls with an IoT Security, Doesn’t Require Data Lake subscription.  **Workaround**: Activate the IoT Security add-on license on Prisma Access first and then onboard firewalls with an IoT Security, Doesn't Require Data Lake subscription. |

---

<a id="cs-common-services-license-activation-subscription-tenant-management-14"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/release-updates/whats-new>*

#### What’s New in Common Services: Subscription and Tenant Management

Learn about the latest features related to Common Services: Subscription and Tenant Management.

Here’s what’s new in Common Services: Subscription and Tenant Management. You
can also check what’s new for the [NetSec Platform](https://docs.paloaltonetworks.com/whats-new), [Identity and Access Management](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/release-updates/whats-new), [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/release-updates), and [Multitenant Portal](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/release-updates/whats-new).

- [What's new in June 2024](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-zmv_pgz_vbc)
- [What's new in May 2024](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-wmd_lqt_mbc)
- [What's new in February 2024](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-zs4_wkm_n1c)
- [What's new in December 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubdec23)
- [What's new in November 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubnov23)
- [What's new in October 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsuboct23)
- [What's new
  in August 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubaug23)
- [What's new in July 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubjul23)
- [What's new in June 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubjun23)
- [What's new in May 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubmay23)
- [What's new in April 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubapr23)
- [What’s New in March 2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id71385d21-38ea-444e-9046-6d7cf5fe17e4)
- [What’s new in February
  2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id2c815ec2-9155-4107-9960-bb41ac995b58)
- [What’s new in January
  2023](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id13f10934-351c-4c88-a06a-679238e36351)
- [What’s New in December
  2022](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_idc3a5d79b-b26c-41e7-be26-823639ddeaa2)
- [What’s New in November
  2022](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id44ece196-b7a2-484c-abce-eb6759f13fe9)
- [What’s New in October
  2022](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id3ec81fbc-6ba0-4525-84e7-a974a456eac6)
- [What’s New in September
  2022](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id6aded366-e3e7-4c12-b10c-ba4b16348fb1)
- [What’s New in August
  2022](#cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id706af526-3ee0-47b6-b291-dd585da044e1)

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-zmv_pgz_vbc"></a>

##### What's new in June 2024

###### License Simplification and Default Tenant Creation

Products offered for free, such as AIOps Free and CIE, don't need an activation link
or auth code for activation. The Activation Console serves as the entry point
for you to activate these products. Activating a product from the tenant view of the
Activation Console creates a single default tenant where the product is
deployed. If you have a single Customer Support Portal account, certain fields in
the activation form are prepopulated on your behalf for a simplified license
activation experience.

First-time license activation for paid products is still through an email that you
receive from Palo Alto Networks. The email still contains an activation link.
Activating a product from the activation link creates a single default tenant where
the product is deployed. If you have a single Customer Support Portal account,
certain fields in the activation form are prepopulated on your behalf for a
simplified license activation experience.

If you have multiple Customer Support Portal accounts, during activation you will
select the Customer Support Portal account that you want to use for managing your
product. If you're a managed security service provider (MSSP), during activation you
will select the Customer Support Portal account that you want to use for managing
your customers' products.

Get started with [License Activation, Subscription Management,
Tenant Management, and Product Management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started).

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-wmd_lqt_mbc"></a>

##### What's new in May 2024

###### FedRAMP High "In Process" Enhancement

[FedRAMP High “In Process”](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/fedramp-moderate-and-high-support) adds
additional support for Prisma SD-WAN standalone and add-on

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_concept-zs4_wkm_n1c"></a>

##### What's new in February 2024

The following new items were released in February 2024.

###### Tenant Moves and Acquisitions

You now have more flexibility in managing your multitenant hierarchy if you're a
Managed Security Service Provider (MSSP) or a distributed enterprise. You can [moving an internal tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants) within your
existing hierarchy to a different location. An internal tenant is any tenant that is
already part of your hierarchy, and to perform the move, you need superuser access
to both the source and the target tenants. This move is possible between
intermediate tenants or even within the same top-most, root-level parent tenant.
You'll typically use this function for tasks like testing, demonstrations,
reorganizations, or simply correcting configuration mistakes.

Additionally, you can now acquire and manage tenants that are currently outside your
existing tenant hierarchy. You do this by[acquiring an external tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants). An external
tenant is defined as one that isn't yet part of your current structure. Keep in mind
that you can only acquire a top-most, root-level, parent tenant when performing an
external tenant acquisition. You'll find this capability most useful in scenarios
such as corporate mergers, acquisitions, or large-scale reorganizations.

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubdec23"></a>

##### What's new in December 2023

The following new items were released in December 2023.

###### FedRAMP High "In Process" Support

Government agencies and highly regulated organizations require the highest level of
security assurance to protect sensitive, high-impact data in the cloud. Prisma® SASE
has reached a major milestone by initiating support for the most demanding security
framework: [FedRAMP High](https://docs.paloaltonetworks.com/fedramp) "In Process" status. This crucial
designation signifies that the platform is engineered to protect the U.S.
government's most sensitive unclassified data, including information vital to life
and financial stability.

This initial launch introduces High support for a substantial set of Prisma SASE
applications, add-ons, and key features. By advancing to this status, Palo Alto
Networks commits to providing Federal customers with the highest level of security
available for cloud services. This expansion ensures government agencies can deploy
and operate critical network security functions, including elements of the SASE
platform, with increased confidence in the security, reliability, and consistency
required for high-impact systems. The supported feature set meets the stringent
requirements for organizations handling the government's most sensitive data.

To ensure FedRAMP High "In Process" compliance, [Prisma SASE FedRAMP High In Process](https://docs.paloaltonetworks.com/fedramp) introduces support
for additional Prisma SASE apps, add-ons, and certain features.

###### License Activation Changes

- **Prisma SD-WAN:** Now all stand-alone Prisma SD-WAN sales orders come with an activation email
  regardless if the subscription is brand new or for an existing tenant.
  You'll see this when you [activate a license for](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-sd-wan.html) 
  Prisma SD-WAN.
- **Prisma SD-WAN:** Now you can choose a different
  Customer Support Account than you chose during first-time activation. You'll
  see this during [return visit license
  activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-repeat-visits.html) for Prisma SD-WAN.
- **Software NGFW Credits:** Now
  you can [activate a Software NGFW Credits
  License](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation.html) using Strata Cloud Manager (AIOps for NGFW Premium) for Panorama Managed VM-Series.

After you receive an email from Palo Alto Networks identifying the new product
license you're activating, including all your add-ons and capacities, use the
activation link to begin the activation process. You can activate and manage all
your available licenses, device associations, tenants, and identity and access from
[Common Services](https://docs.paloaltonetworks.com/common-services). As existing app instances transition to
[tenants and tenant service groups](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) you can
also use Common Services to manage those as well. After activation or transition,
you can find Common Services in the [tenant view of the hub](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) or in a [variety of ways](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started/supertask).

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubnov23"></a>

##### What's new in November 2023

The following new items were released in December 2023.

###### App Tile Name Change

You'll notice the following change in various license activation scenarios. For
example, if you [activate](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation.html) a license for the app formerly
known as AIOps for NGFW Premium, after the activation status is
complete, you can launch the app from a variety of places including the Activation Console
Strata Cloud Manager app tile.

The application tile names on the hub for Prisma Access, Prisma SD-WAN, and
AIOps for NGFW (the premium app only) are now changed to **Strata Cloud
Manager**. With this update, the application URL has also changed to [stratacloudmanager.paloaltonetworks.com](https://stratacloudmanager.paloaltonetworks.com), and
you’ll also now see the **Strata Cloud Manager** logo on the left navigation
pane.

![]()

Moving forward, continue using the Strata Cloud Manager app to manage and
monitor your deployments.

- → [Get started with Strata Cloud
  Manager](https://docs.paloaltonetworks.com/cloud-management)
- → [More on these changes](https://docs.paloaltonetworks.com/cloud-management/administration/overview/moving-to-cloud-management)

###### License Activation Changes

- **IOT add-on for Prisma Access:**
  Now you can use Common Services to activate the [IoT Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin/get-started-with-enterprise-iot-security) add-on when you [enable available add-ons](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-access-and-add-ons/enable-available-add-ons-for-prisma-access)
  Prisma Access (Managed by Strata Cloud Manager)
- **SaaS Security Inline:** Now you can use
  Common Services to [activate Saas Security Inline
  licenses](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation.html) and then get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).

After you receive an email from Palo Alto Networks identifying the new product
license you're activating, including all your add-ons and capacities, use the
activation link to begin the activation process. You can activate and manage all
your available licenses, device associations, tenants, and identity and access from
[Common Services](https://docs.paloaltonetworks.com/common-services). As existing app instances transition to
[tenants and tenant service groups](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) you can
also use Common Services to manage those as well. After activation or transition,
you can find Common Services in the [tenant view of the hub](https://docs.paloaltonetworks.com/hub/hub-getting-started/get-started/tenant-view) or in a [variety of ways](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started/supertask).

###### Remote Browser Isolation

Now you can use Common Services to [activate a license for Remote Browser Isolation
(RBI)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-a-license-for-remote-browser-isolation.html).

Browser and web-based attacks are continuously evolving, resulting in security
challenges for many enterprises. Web browsers, being a major entry point for malware
to penetrate networks, pose a significant security risk to enterprises, prompting
the increasing need to protect networks and devices from zero day attacks. Highly
regulated industries, such as government and financial institutions, also require
browser traffic isolation as a mandatory compliance requirement.

While most enterprises want to block 100% of attacks by using network security and
endpoint security methods, such a goal might not be realistic. Most attacks start
with the compromise of an endpoint that connects to malicious or compromised sites
or by opening malicious content from those sites. An attacker only needs one miss to
take over an endpoint and compromise the network. When this happens, the
consequences of that compromise and the impact to your organization can be
damaging.

[Remote Browser Isolation (RBI)](https://docs.paloaltonetworks.com/remote-browser-isolation)  creates a safe isolation
environment for your users' local browsers, preventing website code and files from
executing on their local browser. Unlike other isolation solutions, RBI uses
next-generation isolation technologies to deliver near-native experiences for users
accessing websites without compromising on security.

![]()

RBI is a service that transfers all browsing activity away from your users' managed
devices and corporate networks to an outside entity, such as Prisma® Access, which
securely isolates potentially malicious code and content within its platform.
Natively integrated with Prisma Access, RBI allows you to apply isolation profiles
easily to existing security policies. Isolation profiles can restrict many user
controls such as copy and paste actions, keyboard inputs, and sharing options like
file uploading, downloading, and printing files to keep sensitive data and
information secure. All traffic in isolation undergoes analysis and threat
prevention provided by Cloud-Delivered Security Services (CDSS), ensuring robust
security before content reaches the user.

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsuboct23"></a>

##### What's new in October 2023

The following new items were released in October 2023.

|

New Features in October 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Prisma Access China Cloud Managed License Activation** | You can now activate a license through Common Services for Cloud Managed Prisma Access China, an offering that allows you to onboard Prisma Access locations in mainland China. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubaug23"></a>

##### What's new in August 2023

The following new items were released in August 2023.

|

New Features in August 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**CIE Sharing** | Now you can use Common Services to [activate and share Cloud Identity Engine](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/share-cie-subscriptions.html). |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubjul23"></a>

##### What's new in July 2023

The following new items were released in July 2023.

|

New Features in July 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Unified License Activation** | The separate single tenant license activation flow and multitenant license activation flow have been unified into one. The following pages are updated to reflect the changes:  - Prisma Access (Managed by Strata Cloud Manager)   [and Add-ons license   activation](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) - Prisma Access (Managed by Panorama) [and Add-ons license   activation](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation) - [Prisma   SD-WAN and Add-ons License Activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation.html) - Prisma Access (Managed by Strata Cloud Manager)[and Prisma SD-WAN   Bundle License Activation](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/activate-a-license-for-cloud-managed-prisma-access-and-prisma-sd-wan) |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubjun23"></a>

##### What's new in June 2023

The following new items were released in June 2023.

|

New Features in June 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Strata Cloud Manager** | Depending on your licensed products, and if you have received information about the migration of your tenant, you might begin to manage and monitor your network and security infrastructure through [Strata Cloud Manager](https://docs.paloaltonetworks.com/cloud-management). You still use the same [Common Services](https://docs.paloaltonetworks.com/common-services) for license activation and tenant management, but you access them through Settings. |

|

**VM Flex License Agreement** | Now you can use Common Services to [Activate a VM Flex License Agreement](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation.html) for IoT Security and AIOps for NGFW. |

|

**Service Provider Backbone License Activation** | Now you can use Common Services to activate a license for [Service Provider Backbone](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sp-backbone-license.html#id497d7c6e-bc0e-4023-bbe8-266201ccc7bf), an offering that allows you more control of your Prisma Access egress traffic. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubmay23"></a>

##### What's new in May 2023

The following new items were released in May 2023.

|

New Features in May 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**IoT Security subscriptions** | Now that [IoT Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin/get-started-with-enterprise-iot-security) is compatible with tenants and tenant service groups (TSGs), you can use Common Services to [activate IoT Security subscriptions](https://docs.paloaltonetworks.com/iot/activation-and-onboarding/licenses-and-activation-for-iot-security/activate-iot-security). |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_conceptsubapr23"></a>

##### What's new in April 2023

The following new items were released in April 2023.

|

New Features in April 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Enterprise License Agreement add-on** | Now that [IoT Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin/get-started-with-enterprise-iot-security) is compatible with tenants and tenant service groups (TSGs), you can use Common Services to [activate an Enterprise License Agreement](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation.html) for IoT Security. |

|

**Extend or renew subscriptions** | [Extend or Renew a Subscription](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/extend-subscription.html) is updated to show additional steps to follow in shared license scenarios. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id71385d21-38ea-444e-9046-6d7cf5fe17e4"></a>

##### What’s New in March 2023

The following new items were released in March 2023.

|

New Features in March 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Prisma Access China License Activation** | You can now activate a license through Common Services for Prisma Access (Managed by Panorama) [China](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation/activate-a-license-for-single-tenant-panorama-managed-prisma-access-china), an offering that allows you to onboard Prisma Access locations in mainland China. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id2c815ec2-9155-4107-9960-bb41ac995b58"></a>

##### What’s New in February 2023

The following new items were released in February 2023.

|

New Features in February 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Enterprise License Agreement add-on** | Now that [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw) is compatible with tenants and tenant service groups (TSGs), you can use Common Services to [activate an Enterprise License Agreement](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation.html) of AIOps for NGFW Premium or AIOps for NGFW Free. |

|

**AIOps for NGFW** | Now that [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw) is compatible with tenants and tenant service groups (TSGs), you can use Common Services to [activate AIOps for NGFW](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation.html). |

|

**Saas Security Posture Management** | Now that [Saas Security Posture Management (SSPM)](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/whats-sspm) is compatible with tenants and tenant service groups (TSGs), you can use Common Services to [activate a SSPM license](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation.html). |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id13f10934-351c-4c88-a06a-679238e36351"></a>

##### What’s New in January 2023

The following new items were released in January 2023.

|

New Features in January 2023 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Singapore and Australia region changes** | When you [Activate a License for](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation.html)  in a single tenant or multitenant hierarchy using the Singapore or Australia region, all tenant data (such as configuration, telemetry logs, system logs, and stats) is now stored in the selected location. The new behavior is available only for new licenses and new tenant activations. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_idc3a5d79b-b26c-41e7-be26-823639ddeaa2"></a>

##### What’s New in December 2022

The following new items were released in December 2022.

|

New Features in November 2022 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Location add-on changes** | If you have a local edition license, the Location add-on is now available for enabling more than 5 regions, and for sharing additional locations with your tenants during Activate a License for Prisma Access (Managed by Strata Cloud Manager) [and Add-ons](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation). |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id44ece196-b7a2-484c-abce-eb6759f13fe9"></a>

##### What’s New in November 2022

The following new items were released in November 2022.

|

New Features in November 2022 | |

| --- | --- |

|  |  |
| --- | --- |
|

**CASB-X license activation** | [Next Generation CASB License on Cross Platforms (CASB-X)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation.html) can be applied on both Prisma Access and Next Generation Firewall (NGFW) devices in a single tenant environment. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id3ec81fbc-6ba0-4525-84e7-a974a456eac6"></a>

##### What’s New in October 2022

The following new items were released in October 2022.

|

New Features in October 2022 | |

| --- | --- |

|  |  |
| --- | --- |
|

**CASB license sharing** | When you [share a license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) for Prisma Access MSP or Distributed Enterprise that includes the Cloud Access Security Broker (CASB) add-on, you can enable CASB on the root tenants or child tenants where the Prisma Access license is shared. |

|

**Deselect add-ons** | When you [share](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) a Prisma Access license, you can now deselect add-ons such as Autonomous Digital Experience Management (ADEM) and Service Connection. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id6aded366-e3e7-4c12-b10c-ba4b16348fb1"></a>

##### What’s New in September 2022

The following new items were released in September 2022.

|

New Features in September 2022 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Multi-DLP Additional Workflows** | Data Loss Prevention (DLP) is now also available in single tenant [Activate a License](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons. In a single tenant Prisma Access Enterprise environment, you have the option to activate multiple individual DLPs against different single tenants or to consolidate multiple DLP instances (such as CASB, NGFW, and Prisma Cloud) under one Customer Support Portal (CSP) ID and one single tenant. |

|

**Prisma Access (Managed by Panorama) License Activation** | When you [Activate a License](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/panorama-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Panorama), the button label is now updated to Single Tenant / Panorama to indicate that the button is for both single tenant Prisma Access license activation and also for Panorama-managed Prisma Access license activation, regardless of single or multitenant status in Panorama. |

<a id="cs-idf6bb425a-c7f5-4d49-9309-65d0e6809606_id706af526-3ee0-47b6-b291-dd585da044e1"></a>

##### What’s New in August 2022

The following new items were released in August 2022.

|

New Features in August 2022 | |

| --- | --- |

|  |  |
| --- | --- |
|

**Prisma Access License Activation Enhancements** | Activate and manage [all your](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started/who-can-use-this-guide)  in one place. |

|

**Subscription Modification** | Request to [modify a subscription](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/modify-subscription.html#idae086a65-b3d1-42b2-8967-a62ae586881e) for your production tenant. |

|

**Evaluation to Production Conversion** | Request [evaluation license to production conversion](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/request-eval-to-prod.html#ide637199d-53b1-43c3-8a71-d67c34c17b5d), specifying the licenses you would like on your production tenant. |

|

**License Diagnostics** | You can now [diagnose license activation](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/license-activation-diagnostics.html#ideab56b26-c532-4af6-834f-d1fe0898a51e) issues and open support cases in one location. |

|

**CASB Bundle** | CASB add-on bundle allows you to activate the following capabilities all at once during [Activate a License](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons: SaaS Security Inline and API, Enterprise DLP, SaaS Security Posture Management (SSPM). |

|

**Multi-DLP Support** | Data Loss Prevention (DLP) is no longer restricted to one DLP instance per CSP ID. Depending on your license, you can now activate multiple DLPs per CSP ID. This makes it possible to activate the DLP add-on against multiple tenants, including child tenants, in your multitenant hierarchy during [Activate a License](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons. |

---

<a id="cs-device-associations-in-strata-cloud-manager"></a>

### Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/get-started>*

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

<a id="cs-device-associations-in-strata-cloud-manager-1"></a>

#### Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/get-started/associate-devices-with-a-tenant>*

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

#### Device Associations (Associate Devices with a Tenant)

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

#### Device Associations (Associate Devices with a Product)

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

#### Device Associations (Remove Device Associations)

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

<a id="cs-device-associations-in-strata-cloud-manager-2"></a>

#### Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/get-started/associate-apps-with-devices>*

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

#### Device Associations (Associate Devices with a Tenant)

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

#### Device Associations (Associate Devices with a Product)

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

#### Device Associations (Remove Device Associations)

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

<a id="cs-device-associations-in-strata-cloud-manager-3"></a>

#### Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/get-started/remove-device-associations>*

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

#### Device Associations (Associate Devices with a Tenant)

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

#### Device Associations (Associate Devices with a Product)

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

#### Device Associations (Remove Device Associations)

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

<a id="cs-device-model-compatibility"></a>

### Device Model Compatibility

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/hardware-model-compatibility>*

Check here for the device models that your applications support.

These are the device models that you can associate with different applications.

- [AIOps for NGFW or Strata Cloud Manager](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/aiops-for-ngfw-hardware-model-compatibility.html#concept_gqx_52q_hwb)
- [CASB-X](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/casb-x-hardware-model-compatibility.html#id1d78102d-b0fc-46c7-929f-9dbccbb7be02)
- [Device Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-iot.html#concept_k3s_npj_wwb)
- [SaaS Security](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/hardware-model-compatibility/hardware-model-compatibility-saas.html#concept_f3r_1jm_p1c)

### AIOps for NGFW or Strata Cloud Manager

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

### CASB-X

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

### Device Security

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

### SaaS Security

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

<a id="cs-firewall-and-license-type-compatibility"></a>

### Firewall and License Type Compatibility

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/firewall-and-license-type-compatibility>*

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

### Strata Cloud Manager

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

### AIOps for NGFW

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

### Device Security

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

### SaaS Security Inline

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

<a id="cs-platform-explorer"></a>

### Platform Explorer

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations/release-updates>*

---

<a id="cs-device-associations-in-strata-cloud-manager-4"></a>

## Device Associations in Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/device-associations>*

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

## Device Associations (Associate Devices with a Tenant)

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

## Device Associations (Associate Devices with a Product)

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

## Device Associations (Remove Device Associations)

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

<a id="cs-common-services-license-activation-subscription-tenant-management-15"></a>

## Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management>*

---

<a id="cs-deactivate-a-product-1"></a>

##### Deactivate a Product

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all>*

This section contains instructions to deactivate a product and then reuse the tenant
or the license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can deactivate either an individual product or all products associated
with a Tenant Service Group (TSG). Deactivation helps you manage tenant resources
efficiently by allowing you to reuse existing tenants and make optimal use of
available licenses.

When you deactivate a product, it is removed from the tenant, and the
associated license can be reallocated to another tenant

You can deactivate:

- **All the products in a tenant:** Deactivate every product
  linked to the tenant.
- **Individual product:** Deactivate a single product from the
  tenant. This is supported only for Cloud Identity Engine and Security
  Lifecycle Review (SLR)

When you deactivate or remove all the products in a tenant, all its add-ons will also
be deactivated and removed from the tenant. After you initiate deactivation, you
have a 24-hour grace period to cancel the deactivation.

When you initiate deactivation, all the superusers will receive an email notification
during all the states of the activation process, such as scheduled deactivation,
deactivation successful, and deactivation failure.

- [Deactivate All Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all.html#topic-87d9ebf3-db73-4a08-80c4-2b1af9718476)
- [Deactivate Individual
  Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products.html#topic-9aef1da4-09af-471f-81b5-c3d6103fe68c)

##### Deactivate all Products

This topic contains procedure to deactivate all the products in the
tenant.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you
   have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate all the products in the tenant, click the Deactivate
   Products icon.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

##### Deactivate an Individual Product

This topic contains to deactivate specific products from the tenant.

1. Use one of the[various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you have a single
   tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate individual products, go to Actions  Deactivate Product.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="cs-deactivate-a-product-2"></a>

##### Deactivate a Product

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products>*

This section contains instructions to deactivate a product and then reuse the tenant
or the license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can deactivate either an individual product or all products associated
with a Tenant Service Group (TSG). Deactivation helps you manage tenant resources
efficiently by allowing you to reuse existing tenants and make optimal use of
available licenses.

When you deactivate a product, it is removed from the tenant, and the
associated license can be reallocated to another tenant

You can deactivate:

- **All the products in a tenant:** Deactivate every product
  linked to the tenant.
- **Individual product:** Deactivate a single product from the
  tenant. This is supported only for Cloud Identity Engine and Security
  Lifecycle Review (SLR)

When you deactivate or remove all the products in a tenant, all its add-ons will also
be deactivated and removed from the tenant. After you initiate deactivation, you
have a 24-hour grace period to cancel the deactivation.

When you initiate deactivation, all the superusers will receive an email notification
during all the states of the activation process, such as scheduled deactivation,
deactivation successful, and deactivation failure.

- [Deactivate All Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all.html#topic-87d9ebf3-db73-4a08-80c4-2b1af9718476)
- [Deactivate Individual
  Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products.html#topic-9aef1da4-09af-471f-81b5-c3d6103fe68c)

##### Deactivate all Products

This topic contains procedure to deactivate all the products in the
tenant.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you
   have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate all the products in the tenant, click the Deactivate
   Products icon.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

##### Deactivate an Individual Product

This topic contains to deactivate specific products from the tenant.

1. Use one of the[various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you have a single
   tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate individual products, go to Actions  Deactivate Product.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="cs-common-services-license-activation-subscription-tenant-management-16"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-a-license-for-multitenant-service-provider-backbone>*

### Activate a License for Multitenant Service Provider Backbone Through Common Services

Learn how to activate a multitenant service provider (sp) backbone through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial deployments | - Prisma Access license - Service Provider (SP) Backbone license - Email activation link - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser |

Service Provider (SP) Backbones enable service providers to offer granular
Prisma Access egress traffic routes to their customers. Verify if this
activation process [applies to you](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/get-started).

SP Backbone
activation can be done only at the top-most, root-level, parent tenant. Only one
backbone license can be claimed per root tenant. The first step is to [create a backbone configuration](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/manage-service-provider-backbones). After
creating the backbone configuration, you can activate the license at the root level
of your tenant hierarchy. After that is done, subtenants can be activated to use the
backbone that is set up.

The following steps assume that
you have already [added tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html#add-tenants) to create a multitenant hierarchy and [created a backbone configuration](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/manage-service-provider-backbones).

![]()

After you receive an email from Palo Alto Networks identifying the Service
Provider (SP) Backbone license you are activating, click the email link to begin the
activation process.

1. Select Get Started with Service Provider Backbone in
   your email.
2. You are automatically directed to Common ServicesSubscription & Add-ons, where you activate the subscription for your product.
3. Select an existing top-most, root-level, parent
   Tenant:

   ![]()
4. Select the Customer Support Account for the tenant.
5. Agree to the terms and conditions, and
   Activate.
6. Common ServicesTenant Management displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you can [activate a](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation)
   Prisma Access (Managed by Strata Cloud Manager) license for any tenant in the multitenant hierarchy and
   assign the SP Backbone to it.
8. For Add SP Interconnect to Tenant, select one of the following:

   - Use Prisma Access backbone to use Prisma Access
     for egress traffic. This uses public cloud providers for network
     backbone, such as: GCP, AWS, Azure.
   - Use Service Provider backbone to use internet
     service provider backbones for Prisma Access egress traffic, such as:
     BT, Orange, AT&T. Choose one of the backbones that you configured.

   ![]()
9. If you selected to use a Service Provider backbone, you can Set
   Region Exceptions to exclude internet service provider backbones
   in these regions. The excluded regions use Prisma Access for network backbone
   instead.
10. Save and done.
11. Agree to the Terms and Conditions and
    Activate.
12. (Optional) [Manage](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/manage-service-provider-backbones) and [monitor](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-sp-backbones) your service provider
    backbones and connections.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-17"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-cie-first-time-multiple-csp>*

### First time Cloud Identity Engine Activation - Multiple Customer Support Portal Account

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select Activate.
2. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
3. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

      After you create a tenant hierarchy, you can [share a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/share-cie-subscriptions.html).
   3. Select Done.
4. Select a Region where you want to deploy your product.
5. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
7. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
8. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-18"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-multiple-csp>*

#### First time AIOps for NGFW Premium Activation - Multiple Customer Support Portal Account

Learn how to activate your AIOps for NGFW Premium application for the
first time if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time AIOps for NGFW Premium activation.

1. After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
   begin the activation process.
2. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
3. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
4. Select a Region where you want to deploy your product.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
5. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
6. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
7. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
8. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
9. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
   appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

   If the status isn't
   Complete, you can't add your devices
   yet.
10. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
    of the following options.

    - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
    - Launch from Common ServicesProducts or from SettingsProducts.
11. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
12. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
13. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-19"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-one-csp>*

#### First time AIOps for NGFW Premium Activation - One Customer Support Portal Account

Learn how to activate your AIOps for NGFW Premium application for the
first time if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time CASB-X activation.

1. After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
   begin the activation process.
2. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
3. Allocate the product to the Recipient.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
4. Select a Region where you want to deploy your product.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
5. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
6. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
7. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply AIOps for NGFW Premium.
8. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
9. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
10. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
    appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

    If the status isn't
    Complete, you can't add your devices
    yet.
11. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
    of the following options.

    - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
    - Launch from Common ServicesProducts or from SettingsProducts.
12. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
13. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
14. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-20"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-repeat-visits>*

#### Return Visit AIOPs Premium Activation

Learn how to activate your AIOPs Premium for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region for the physical location to process
   your data.

   The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
   activate AIOps for NGFW Premium for Strata Cloud Manager in
   a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
   Prisma Access, it's allowed because there are no dependencies
   with Prisma Access.

   However, if you later want to activate Prisma Access in the same
   region as the original AIOps for NGFW Premium region, it's not an
   available option. For hybrid customers, you will have to wait until the same
   region is supported by both AIOps for NGFW Premium and Prisma Access.

   Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
   following AIOps for NGFW Premium region will map to a different
   region when using Strata Cloud Manager to manage the firewall.

   Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

   - singapore
   - taiwan
   - korea
   - indonesia

   Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

   - Germany
   - Europe
   - Switzerland
   - Israel
   - France
   - Spain
   - Italy
   - Poland
   - Qatar

   Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

   - Americas
   - Canada
4. Add Strata Logging Service.

   ![]()

   1. Select an Strata Logging Service instance.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
   appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant).

   If the status isn't
   Complete, you can't add your devices
   yet.
9. Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
   of the following options.

   - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
   - Launch from Common ServicesProducts or from SettingsProducts.
10. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-21"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-first-time-multiple-csp>*

#### First time CASB-X Activation - Multiple Customer Support Portal Account

Learn how to activate your CASB-X application for the first time
if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time CASB-X activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.

   ![]()
5. **Agree to the terms and conditions**, and **Activate**.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X on NGFW, you must go to the Device
   Association tab to select the devices and apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-22"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-first-time-one-csp>*

#### First time CASB-X Activation - One Customer Support Portal Account

Learn how to activate your CASB-X application for the first time
if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time CASB-X activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X on NGFW, you must go to the Device
   Association tab to select the devices and apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-23"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/casb-x-activation/activate-casb-x-repeat-visits>*

#### Return Visit CASB-X Activation

Learn how to activate your CASB-X for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.

   ![]()
5. **Agree to the terms and conditions**, and **Activate**.
6. CASB-X activation is now complete for Prisma Access. To apply CASB-X
   on NGFW, you must go to the Device Association tab to select the devices and
   apply Next-Generation CASB on them:

   - [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started)
   - [Next Generation CASB-X](https://docs.paloaltonetworks.com/next-gen-casb)
7. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
8. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-24"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/activate-cie-first-time-one-csp>*

#### First time Cloud Identity Engine Activation

Learn how to activate your Cloud Identity Engine(CIE) application for the first time if
you have only one Customer Support Portal account.

Follow these steps for first time Cloud Identity Engine (CIE) activation.

1. From the Activation Console, select
   Activate.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.

   ![]()
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-25"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/activate-cie-repeat-visits>*

#### Return Visit Cloud Identity Engine Activation

Learn how to activate your Cloud Identity Engine for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. From the Activation Console, select Activate.
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-26"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/cie-activation/share-cie-subscriptions>*

#### Share Cloud Identity Engine

Learn how to share Cloud Identity Engine (CIE) on tenants through Common Services.

After you activate Cloud Identity Engine on a tenant and [add child tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you can share
(CIE) with the child tenants in your hierarchy.

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

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html)
   Tenant Management.
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

<a id="cs-common-services-license-activation-subscription-tenant-management-27"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/edit-a-license-for-service-provider-backbone>*

### Edit a License for Service Provider Backbone Through Common Services

Learn how to edit a license for a service provider (SP) backbone through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- [Tenant or Tenant   Service Group (TSG)](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) - Commercial deployments | - Prisma Access license - Service Provider (SP) Backbone license - [Role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions):   Multitenant Superuser or Superuser |

After you [activate a license](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sp-backbone-license.html) for your
service provider (SP) backbone, you can edit it from Tenant Management.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html)
   Common ServicesTenant Management.
2. Search or scroll to the tenant where you activated the SP backbone license.
3. Edit the licensed product for the SP backbone or Prisma
   Access.

   ![]()
4. Choose a Prisma Access Contract and
   Region to proceed.

   ![]()
5. For SP Interconnect, use one of the following options:

   - If you're deleting a backbone, deselect SP
     Backbone before you delete your SP backbone.
   - If you're adding a backbone, select SP Backbone
     to use internet service provider backbones for Prisma Access egress
     traffic, such as: BT, Orange, AT&T.

   ![]()
6. Select Exclude Region to exclude internet service
   provider backbones in these regions. Prisma Access egress traffic uses public
   cloud providers for network backbone instead, such as: GCP, AWS, Azure.
7. (Optional) Manage and monitor your service provider backbones and
   connections.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-28"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation/activate-ela-aiops-for-ngfw-premium>*

#### Activate ELA AIOps for NGFW Premium Through Common Services

Learn how to activate a premium add-on Enterprise License Agreement (ELA) of AIOps for NGFW Premium on a tenant through Common Services.

This task shows how to activate Enterprise License Agreement (ELA) for AIOps for NGFW
Premium license.

Strata Cloud Manager is now available, featuring two licensing tiers: Strata
Cloud Manager Essentials and Strata Cloud Manager Pro. This unified structure
streamlines the deployment of network security offerings, including AIOps for
NGFW, Autonomous Digital Experience Management (ADEM), cloud management
functionality, and Strata Logging Service. See [Strata Cloud Manager License](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html).

1. Use one of the following activation methods.

   - Log into the [hub](https://apps.paloaltonetworks.com/apps) and
     activate from tenant view of the hubELA ActivationAIOps for NGFW:

   ![]()

   - Log into the Customer Support Portal and activate
     from Customer Support PortalDevicesELA AIOps Activation:

   ![]()
2. You are automatically directed to Common
   ServicesSubscription & Add-ons,
   where you activate the subscription for your product.
3. Select the same Tenant that you
   used for Strata Logging Service, so that you can associate ELA for AIOps on the same
   tenant where you want AIOps to be applied.
4. The Customer Support Account is
   grayed out, but is auto-populated with the same CSP that you used
   for Strata Logging Service.
5. The Region is grayed out, but
   is auto-populated with the same region that you used for Strata Logging Service.
6. The UI shows if you have Strata Logging Service available in this tenant
   where you can apply ELA for AIOps.

   ![]()
7. Agree to the terms and conditions,
   and Activate.
8. Common ServicesTenant Management displays
   the status of the activation, such as initializing or complete.
9. After the
   status is complete, you must go to
   the Common ServicesDevice
   Associations tab to select the devices
   and apply ELA for AIOps on them: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).

   If the status is not complete,
   you cannot apply ELA for AIOps on the devices yet.
10. After the status is complete,
    you can launch AIOps from one of the following options.

    - Launch from email.
    - Launch from the hub tile.
    - Launch from Common ServicesTenant Management.
11. Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access). Assign
    role of [Superuser](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)
     or [Business Administrator](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions). The CSP-level access is not
    sufficient.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-29"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation/activate-ela-for-iot-security>*

#### Activate ELA for IoT Security Through Common Services

Learn how to activate an add-on Enterprise License Agreement (ELA) for IoT Security
on a tenant through Common Services.

1. Start the ELA activation process from either the hub or Customer Support
   Portal.

   **Hub**: Log in to the [hub](https://apps.paloaltonetworks.com/apps) and, from the tenant view, click ELA ActivationIoT Security at the top of the page.

   ![]()

   or

   **Customer Support Portal**: Log in to your [customer support portal](https://support.paloaltonetworks.com/Support/Index) account, select Products Enterprise AgreementsLicenses, and then click ELA-IoT
   Activation.

   ![]()

   Whether you start in the hub or Customer Support Portal, both actions load a
   magic link that opens the Activate IoT Security page on the hub.
2. Activate the IoT Security ELA for a tenant service group.
   1. Choose an existing [tenant service group (TSG) tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)
      or create a new one. A TSG essentially associates firewalls with
      applications such as IoT Security.
   2. Choose the firewall deployment region.
   3. Create a new IoT Security tenant URL by entering a unique subdomain to
      complete <subdomain>.iot.paloaltonetworks.com.

      This is the URL where you'll log in to your IoT Security portal.

      If you want to convert an existing IoT
      Security tenant from using one or more IoT Security licenses to an
      IoT Security Enterprise License Agreement, contact your Palo Alto
      Networks sales representative.
   4. Agree to the terms and conditions and then
      Activate.

      ![]()
3. Go to the Common ServicesDevice Associations tab to add firewalls to the TSG tenant, associate them with the
   IoT Security app, and then apply the Enterprise IoT Security ELA to them: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
4. In the Customer Support Portal, select ProductsDevices and view the entries in the License column for your firewalls to
   confirm that IoT Security is now applied to them.
5. Continue setting up IoT Security to work with your firewalls.

   To log in to your IoT Security portal, return to Common Services on the hub
   and select the IoT Security link on either the Tenant
   Management page or the Device Associations page.

   For IoT Security (Enterprise IoT Security Plus, Industrial IoT Security, or
   Medical IoT Security), see [Onboard IoT Security](https://docs.paloaltonetworks.com/iot/iot-security-admin/get-started-with-iot-security/onboard-iot-security).

   For Enterprise IoT Security, see [Onboard Enterprise IoT
   Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin).
6. (Optional) Manage identity and access to IoT Security.

   To create an IoT Security user with owner privileges plus the ability to
   generate one-time passwords (OTPs) and pre-shared keys (PSKs), add a user
   account in the Customer Support Portal and assign a Superuser role in the
   relevant tenant service group (TSG) in Identity & Access (this is
   described in the following steps.) To create an IoT Security user with all
   owner privileges except the ability to generate OTPs and PSKs, add the new
   user account in Identity & Access and assign a Superuser role in
   Identity & Access. To create an IoT Security user with read-only
   privileges, add a user account in Identity & Access and assign a View
   Only user role in Identity & Access.

   1. (Optional) Add a user account in the Customer Support Portal.
      New users only need to be added to the Customer Support Portal accounts
      if they need access to operate onboarding or offboarding tasks, such as
      generating OTPs and PSKs. To create a new user in the Customer Support
      Portal:

      1. Log in to the [Customer Support
         Portal](https://support.paloaltonetworks.com/) with superuser permissions, which allow you to
         create new user accounts.
      2. Select Members Create New User, enter the required information, and then
         Submit.

      A new user account is created and added to the account as a member.
      An email notification is sent to the new user with login
      credentials.
   2. Log in to the [hub](https://apps.paloaltonetworks.com/), navigate to Common ServicesIdentity & Access/Access Management.
   3. [Add Identity](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-users).

      Users added in the Customer Support Portal are separate from users
      added in Identity & Access.
   4. To assign a [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) to the user you created,
      select the user, Assign Roles, choose
      IoT Security in Apps & Services, choose
      one of the options in Role, and then Assign
      Role.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-30"></a>

##### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started/which-activation-flow-to-use/activate-using-activation-console>*

##### SASE

contains procedure to activate a product using the activation console.

The new unified activation and onboarding experience is available only for
following SASE products that have transitioned to the Activation Console.

Firewall and SD-WAN products (Next-Generation Firewall and SD-WAN), as well as
SASE products that have not yet transitioned, will continue to follow the existing
workflow described in Activation Using Hub.

**Supported for:** Prisma Access,Prisma Browser,Remote Browser Isolation,CASB-X,Data Security,AI Access Security,SaaS Security Posture Management,Enterprise DLP

###### Activate a Product on a Single Tenant

**Before You Begin**

If the product needs to be activated in a non-default tenant, create
the [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants) before you begin the activation
process

To activate a product, perform the following:

The following steps outline the common activation procedure for products. The
screenshots shown are based on Prisma Access, but the same workflow applies to all
supported products. Detailed, product-specific steps are provided in the respective
SASE product documentation.

1. Click **Login to Activate** in the welcome email.

   ![]()
2. This will take you to the Activation ConsoleSubscription and Add-ons, where you can view the list of all your product
   entitlements. Click **Activate** to activate a specific product.
3. You will be taken to the Product activation form.

   ![]()
4. Select a **Tenant** if you have multiple tenants. For a single
   tenant environment, it is autopopulated with the primary tenant.
5. Select a **Region** where you want to deploy your product.
6. Select the product-specific details.
7. **Agree to the terms and conditions**, and then click
   **Activate Now**.
8. You will be redirected to the Subscription page, where you can see
   the activation status. The status column would show **Activation in
   Progress** for the products where activation is in progress.
9. Once the activation is complete, click **Launch** to launch and access the
   product.When you launch the product, you will be redirected to the Strata Cloud
   Manager from where you can access the product and all its activated add-ons.

   ![]()

###### Activate a Product on Multiple Tenants

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click ⋮Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   Note: If you are modifying the allocation for the default tenant, ensure
   that you reduce the assigned license quantity. The reduced quantity
   becomes available for reallocation to other tenants in the
   hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat from the Step 3 to allocate licenses to additional tenants.

   Validate
   the license allocation by switching to the corresponding tenant in the
   tenant browser and reviewing the allocation details.

   ![]()

After activating your products, you can continue to [manage your subscriptions](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/about-subscription-management) from the
**Subscriptions & Add-ons** page in the **Activation Console**. This
page provides options to perform common subscription management tasks, including
activating free add-ons, enabling purchased add-ons, reallocating licenses to other
tenants, and renewing existing licenses.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-31"></a>

##### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started/which-activation-flow-to-use/activate-using-hub>*

##### Firewall and SD-WAN

Contains instruction to activate a product through hub

Next-Generation Firewall, SD-WAN, and some SASE products that have not yet transitioned
to the new activation experience during the phased rollout will use the existing
activation workflow described in this section.

###### Activate a License or Subscription for Paid Products

First-time license activation for paid products is through an email that you receive
from Palo Alto Networks regarding. The email contains an activation link. Activating
a product from the activation link creates a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where the product is
deployed.

![]()

After you activate a product, you have access to [Common Services](https://docs.paloaltonetworks.com/common-services) to [manage your product](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-products.html) from the
Activation Console or Strata Cloud Manager. You get assigned the
[Superuser](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) role to manage your product.

###### Single Customer Support Portal Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, for a single Customer Support Portal account, certain fields
in the activation form are prepopulated for you. Depending on your product, you
might be asked to select a region where you want to deploy the product, to select or
create Strata Logging Service to store your logs, to select or create a Cloud
Identity Engine instance to identify and verify all users across your
infrastructure, or to associate devices or appliances. 

![]()

- In the activation workflow, the Customer Support Portal account
  associated with the user is prepopulated if there is only one Customer
  Support Portal account associated with the user.
- For the selected Customer Support Portal account, if there is
  no prior tenant associated, the tenant field is autopopulated with the
  same name as the Customer Support Portal account.
- After completing the activation, the user who is activating the first
  product is added as a superuser on the selected tenant, and can also add
  other users.
- The default tenant can't be deleted as long as there are
  products activated in the tenant.
- If the user's selected Customer Support Portal account has a
  previously mapped tenant, and the user activating a license does not
  have access to that tenant, the user is informed to contact the tenant
  account admin to request access.

###### Multiple Customer Support Portal Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, if you have multiple Customer Support Portal accounts, you
will select the Customer Support Portal account that you want to use for managing
your product. Depending on your product, you might be asked to select a region where
you want to deploy the product, to select or create Strata Logging Service to
store your logs, to select or create a Cloud Identity Engine instance to identify
and verify all users across your infrastructure, or to associate devices or
appliances. 

![]()

- If there are multiple Customer Support Portal accounts
  associated with the user activating a license, the user can select a
  specific Customer Support Portal account.
- For the selected Customer Support Portal account, if there is
  no prior tenant associated, the tenant field is autopopulated with a
  default tenant that has the same name as the Customer Support Portal
  account name.
- After completing the activation, the user who is activating the first
  product is added as a superuser on the selected tenant, and they should be
  able to add other users.
- If the selected Customer Support Portal account has a
  previously mapped tenant, and the user does not have access to that
  tenant, the user is informed to contact the account admin to request
  access.
- If users require a multitenant setup, they are provided with an option to
  create a new tenant or a child tenant. They can create the hierarchy with
  the first child in the tenant management page. They can select the child
  tenant or create a new child tenant from the activation workflow.
- If multiple tenants exist where products have been previously activated for
  the Customer Support Portal account, but the user does not have access to
  those tenants, the user is warned that the product will be activated in a
  different tenant from where the other services are currently active. The
  user gets the option to proceed anyway, but is warned that dependent
  products need to be activated in the same tenant.

###### Managed Security Service Provider (MSSP) Activation Behavior

See the license activation topics in this guide for details about activating specific
products. In general, for a Managed Security Service Provider (MSSP), you will
select the Customer Support Portal account that you want to use for managing your
customers' products. You will create a tenant hierarchy to manage them. Depending on
the product, you might be asked to select a region where you want to deploy the
product, to select or create Strata Logging Service to store the logs, to
select or create a Cloud Identity Engine instance to identify and verify all users
across the infrastructure, or to associate devices or appliances. 

![]()

After you activate a tenant heirarchy, you have access to [Common Services](https://docs.paloaltonetworks.com/common-services) to [manage your tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants.html) from the
Activation Console or Strata Cloud Manager. You can also use Strata Multitenant Cloud Manager aggregated views for monitoring information across all of your
tenants.

- In the case of managed security service providers (MSSP), the
  end customers are managed by the MSSP that owns the Customer Support
  Portal account.
- The default tenant is associated with the MSSP Customer Support
  Portal account. The user activating the product must be granted access
  to that tenant, and then user can create child tenants and activate
  products in the child tenant.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-32"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-first-time>*

#### New Purchase Cloud Managed Prisma SD-WAN Activation

Learn how to activate your newly purchased Cloud Managed Prisma SD-WAN license through Common Services.

Follow these steps for newly purchased Cloud Managed Prisma SD-WAN and add-ons license activation and ION device registration. All stand-alone
Prisma SD-WAN sales orders come with an activation email
regardless if the subscription is brand new or for an existing tenant.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the Multitenant
   Superuser role.
2. Choose the Customer Support Account number that you want
   to use to activate the license.

   ![]()
3. Allocate the subscription to the recipients of your choice. If your order
   includes ION devices, the device is also registered to this recipient.

   For Managed Security Service Providers (MSSPs) and distributed enterprises,
   you can allocate the subscription directly on any tenant in the hierarchy.
   [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) For a Prisma SD-WAN tenant, allocating the license at the
   child-level automatically provisions it at the top-most, root-level, parent
   Prisma SD-WAN tenant as well. If the order includes
   ION devices, it is recommended that you allocate to the top-most,
   root-level, parent tenant. This enables the parent tenant to do ION device
   management for the child tenants.

   After activation, you can build out your tenant hierarchy as needed. You can
   create your tenant hierarchy to reflect your existing organizational
   structure. You can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access)
   when creating the hierarchy, in addition to [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

   However, any tenants that you create between the child tenant and the
   top-most, root-level, parent tenant do not get automatically provisioned
   with the license. That is a one-time process that happens only at
   activation.

   1. Create a new tenant from All Tenants +.

      ![]()
   2. Name the tenant and select Done.

      ![]()
   3. (Optional) For Managed Security Service Providers (MSSPs) and
      distributed enterprises, create a new child tenant by selecting
      + from the parent tenant that you previously
      created.

      ![]()
   4. (Optional) Name the child tenant and select
      Done.

      ![]()
4. Select the Region where you want to deploy your product.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or Strata Logging Service) are
   now provisioned. As the subscriptions are activating, the progress status will
   display. When the process is complete, the tenant status displays as
   Up. You now have a tenant provisioned with
   instances of the products that you purchased. The tenant has one user — the
   account that you used when you began this process.
7. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - Prisma SD-WAN
     [Administrator’s Guide](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan)
   - [Open APIs](https://pan.dev/sdwan/docs/)
   - Strata Logging Service
     [Getting Started
     Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
8. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-33"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-first-time-one-csp>*

#### New Purchase Cloud Managed Prisma SD-WAN Activation

Learn how to activate your newly purchased Cloud Managed Prisma SD-WAN license through Common Services.

Follow these steps for newly purchased Cloud Managed Prisma SD-WAN and add-ons license activation and ION device registration. All stand-alone
Prisma SD-WAN sales orders come with an activation email
regardless if the subscription is brand new or for an existing tenant.

1. Log in with your email address.

   - If you have a Palo Alto Networks Customer Support account, then enter
     the email address you used when you registered for that account and
     select Next.
   - If you do not have a Palo Alto Networks Customer Support account, then Create a New AccountPasswordNext.

   The service uses this email address for the user account assigned to the
   tenant that you use for this license. This tenant, and any others
   created by this email address, will have the Multitenant
   Superuser role.
2. Because you have only one Customer Support Portal account associated with your
   user name, the Customer Support Account is
   pre-populated.

   ![]()
3. Allocate the subscription to the recipients of your choice. If your order
   includes ION devices, the device is also registered to this recipient.

   If you need just one tenant, use or rename the tenant provided. The name
   provided matches your Customer Support Portal account for convenience.

   ![]()

   For Managed Security Service Providers (MSSPs) and distributed enterprises,
   you can allocate the subscription directly on any tenant in the hierarchy.
   [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) For a Prisma SD-WAN tenant, allocating the license at the
   child-level automatically provisions it at the top-most, root-level, parent
   Prisma SD-WAN tenant as well. If the order includes
   ION devices, it is recommended that you allocate to the top-most,
   root-level, parent tenant. This enables the parent tenant to do ION device
   management for the child tenants.

   ![]()

   After activation, you can build out your tenant hierarchy as needed. You can
   create your tenant hierarchy to reflect your existing organizational
   structure. You can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access)
   when creating the hierarchy, in addition to [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

   However, any tenants that you create between the child tenant and the
   top-most, root-level, parent tenant do not get automatically provisioned
   with the license. That is a one-time process that happens only at
   activation.
4. Select the Region where you want to deploy your product.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or
   Strata Logging Service) are now provisioned. As the
   subscriptions are activating, the progress status will display. When the process
   is complete, the tenant status displays as Up. You
   now have a tenant provisioned with instances of the products that you purchased.
   The tenant has one user — the account that you used when you began this
   process.
7. To complete the product setup, you must [access the products you purchased](https://docs.paloaltonetworks.com/content/techdocs/en_US/sase/prisma-sase-multitenant-platform/access-multitenant-platform/access-products.html) and
   perform any required postinstallation configuration. For information about your
   products, see:

   - Prisma SD-WAN
     [Administrator’s Guide](https://docs.paloaltonetworks.com/prisma/prisma-sd-wan)
   - [Open APIs](https://pan.dev/sdwan/docs/)
   - Strata Logging Service
     [Getting Started
     Guide](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started.html)
8. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-34"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-cloud-managed-prisma-sd-wan-repeat-visits>*

#### Return Visit Cloud Managed Prisma SD-WAN Activation

Learn how to activate your Cloud Managed Prisma SD-WAN tenants through Common Services for repeat visits.

Follow these steps if you have already completed [new purchase](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/prisma-sd-wan-and-add-ons-license-activation/activate-a-license-for-cloud-managed-prisma-sd-wan.html)
Prisma SD-WAN license activation, you have already created your
tenant hierarchy through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate a
Prisma SD-WAN subscription in additional child tenants in
your existing hierarchy..

1. Log in with your email address.
2. Choose the Customer Support Account number that you want
   to use to claim the license.

   As of December 2023, you can choose a different Customer Support Account than
   you chose during first-time activation. This is important in various
   scenarios such as, if you have different teams providing support for
   different instances of Prisma SD-WAN within the same
   tenant service group (TSG).

   ![]()
3. Allocate the subscription to the recipient tenant of your choice.

   ![]()
4. Select the Region nearest to the storage location of the
   data logs.

   There is no cross-region aggregation. Make sure that
   all your tenants are in the same region for monitoring purposes.
5. Agree to the Terms and Conditions.
6. Activate Now. The products and
   add-ons that you are activating (such as Prisma SD-WAN or Strata Logging Service) are
   now provisioned. As the subscriptions are activating, the progress status will
   display. When the process is complete, the tenant status displays as
   Up. You now have a tenant provisioned with
   instances of the products that you purchased. The tenant has one user — the
   account that you used when you began this process.
7. From here, the steps are the same for first time activation or return visit
   activation. Continue on to complete the activation with the steps that
   follow.

---

<a id="cs-common-services-license-activation-subscription-tenant-management-35"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-first-time-multiple-csp>*

#### First time SaaS Security Inline Activation - Multiple Customer Support Portal Account

Learn how to activate your SaaS Security Inline application for the first time
if you have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time SaaS Security Inline activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-36"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-first-time-one-csp>*

#### First time SaaS Security Inline Activation - One Customer Support Portal Account

Learn how to activate your SaaS Security Inline application for the first time
if you have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time SaaS Security Inline activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. Add Strata Logging Service.

   ![]()

   1. Select a Strata Logging Service instance for storing your
      logs.
   2. Enter the amount of data log storage.
   3. The region is grayed out, but is autopopulated with the same region
      that you used for Strata Logging Service.
5. Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
   CIE instance to identify and verify all users across your infrastructure.

   ![]()
6. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
7. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
8. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-37"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/saas-security-activation/activate-saas-inline-repeat-visits>*

#### Return Visit SaaS Security Inline Activation

Learn how to activate your SaaS Security Inline for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-38"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/activate-vm-flex-iot>*

#### Activate a Software NGFW Credits License for IoT Through Common Services

Learn how to activate a Software NGFW Credits License for IoT on a tenant through
Common Services.

1. After you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal (CSP) of VM-Series for
   IOT, then you can activate your subscription.
2. After the profile is complete in the CSP, select Finish
   Setup. This redirects you to the hub Subscription
   & Add-ons, where you select Activate
   Now to activate the subscription for your product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you just created and enter a unique
   subdomain to complete the
   <subdomain>.iot.paloaltonetworks.com URL for
   your IoT Security app (this will be the URL where you log in to the IoT Security
   portal).
7. Agree to the terms and conditions, and
   Activate.
8. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
9. After the status is complete, which can take up to
   five minutes, you can do one of the following:

   - Go to the CSP to [register the firewall](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/register-the-vm-series-firewall-software-ngfw-credits).
   - Go to the hub Common ServicesDevice Associations tab to see the firewall devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
10. After the status is complete, you can launch
    Software NGFW for IoT from one of the following options.

    - Launch from email.
    - Launch from the hub tile.
    - Launch from Common ServicesTenant Management.
11. Get started with [IoT Security](https://docs.paloaltonetworks.com/iot/enterprise-iot-security-admin/get-started-with-enterprise-iot-security).
12. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-39"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/activate-vm-flex-ngfw>*

#### Activate a Software NGFW Credits License of Strata Cloud Manager for NGFW Through Common Services

Learn how to activate a Software NGFW Credits license of Strata Cloud Manager
for NGFW on a tenant through Common Services.

Use Strata Cloud Manager to manage VM-Series.

1. After you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal (CSP) for VM-Series for
   SCM, then you can activate your subscription.

   If you have enrolled to a cloud service subscription (consisting of IoT,
   SaaS Inline, Strata Cloud Manager, Strata Cloud Manager Pro, and Strata
   Logging Service), you will need to activate additional licenses on your
   tenants after you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on
   the Customer Support Portal. For more information, see [activate the deployment
   profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile-vm-series).
2. After the profile is complete in the CSP, select Finish
   Setup. This redirects you to the hub Subscription
   & Add-ons, where you select Activate
   Now to activate the subscription for your product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you created, Agree to
   the terms and conditions, and Activate.
7. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing,
     associating, or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
8. After the status of the license activation is
   complete, which can take up to five minutes,

   - Go to the CSP to [register the firewall](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/register-the-vm-series-firewall-software-ngfw-credits).
   - Use the auth code while bringing up a VM. The auth code is associated
     with this consumption model. When the license database sees the auth
     code request come in from the VM, it will automatically call hub with
     this information. At this point, the new VM serial number will be added
     to the TSG associated with the deployment profiles for Software NGFW.
   - Go to the hub Common ServicesDevice Associations tab to see the firewall devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. After the status is complete, you can launch
   Strata Cloud Manager for NGFW from the hub Common ServicesTenant Management.
10. Get started with Strata Cloud Manager
    [for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-40"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/software-ngfw-credits-activation/aiops-panorama-credits>*

#### Activate a Software NGFW Credits License for AIOps for NGFW Premium on Panorama Through Common Services

Learn how to activate a Software NGFW Credits License using AIOps for NGFW Premium (Strata Cloud Manager) for Panorama Managed VM-Series on
a tenant through Common Services.

Use Strata Cloud Manager for Panorama Managed VM-Series.

1. [Create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
   Customer Support Portal for VM-Series for
   Strata Cloud Manager including the following options,
   then you can activate your subscription:

   If you have enrolled to a cloud service subscription (consisting of IoT,
   SaaS Inline, Strata Cloud Manager, Strata Cloud Manager Pro, and Strata
   Logging Service), you will need to activate additional licenses on your
   tenants after you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on
   the Customer Support Portal. For more information, see [activate the deployment
   profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile-vm-series).

   - Panorama for Management
   - Panorama as Dedicated Log Collector
   - Strata Cloud Manager

   ![]()
2. After the profile is complete in the Customer Support Portal, select
   Finish Setup. This redirects you to the hub
   Subscription & Add-ons, where you select
   Activate Now to activate the subscription for your
   product.

   ![]()
3. Select the Customer Support Account number that you want
   to use to manage the subscription.
4. Select a Tenant or create a tenant where you want to
   apply this subscription.
5. Select a Region storage location for the data logs,
   known as Strata Logging Service.
6. Select the deployment profile that you just created,
   Agree to the terms and conditions, and
   Activate.
7. Tenant Management displays the following:

   - Licensed Products displays the products
     associated with the tenant, including the status of the license
     activation, such as initializing,
     associating, or
     complete.
   - Deployment Profiles displays the deployment
     profiles associated with the tenant, including the status of the
     association, such as pending or
     complete.
8. After the status is complete, which can take up to
   five minutes,

   - Go to the Customer Support Portal to [provision Panorama](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/provision-panorama) or [migrate Panorama](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/migrate-panorama-to-a-flexible-license).
   - Go to the hub Common ServicesDevice Associations tab to see the Panorama devices: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
9. After the status is complete, you can launch
   Strata Cloud Manager for NGFW from the hub Common ServicesTenant Management.
10. Get started with Strata Cloud Manager
    [for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-41"></a>

### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sp-backbone-license>*

### Service Provider Backbone License Activation Through Common Services

Learn about service provider (SP) backbone multitenant license
activation.

Welcome to Common Services Service Provider Backbone multitenant and single tenant
license activation. Verify if this activation process [applies to you](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html).

- [Activate a License for Service
  Provider Backbone](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/activate-a-license-for-multitenant-service-provider-backbone.html#id21051be5-43da-4fef-939f-72e846d67270)
- [Edit a License for Service Provider
  Backbone](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/edit-a-license-for-service-provider-backbone.html)

---

<a id="cs-common-services-license-activation-subscription-tenant-management-42"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-first-time-multiple-csp>*

#### First time SaaS Security Posture Management Activation - Multiple Customer Support Portal Account

Learn how to activate your SaaS Security Posture Management application for the first time if you
have multiple Customer Support Portal accounts.

If you have multiple Customer Support Portal accounts, follow these steps for first
time SaaS Security Posture Management activation.

1. If you have multiple Customer Support Portal accounts, choose the
   Customer Support Account number that you want to use.

   ![]()
2. Allocate the product to the Recipient of your choice.

   You can allocate your entire license to one recipient or you can share it
   with multiple recipients in a tenant hierarchy. [What is a tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

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
      through [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
      tenant hierarchy to reflect your existing organizational structure.
      You can also consider [identity and access
      inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
      [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).
   3. Select Done.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access and NGFW available
   in this tenant where you can apply CASB-X.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
8. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from email:

     ![]()
   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesProducts:

     ![]()
9. [Get Started with SSPM](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/whats-sspm)
   documentation.
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-43"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-first-time-one-csp>*

#### First time Activation - One Customer Support Portal Account

Learn how to activate your SaaS Security Posture Management application for the first time if you
have only one Customer Support Portal account.

If you have only one Customer Support Portal account, follow these steps for first
time SaaS Security Posture Management activation.

1. Because you have only one Customer Support Portal account associated with your
   username, the Customer Support Account is
   prepopulated.
2. Allocate the product to the Recipient of your choice.
   1. The name provided matches your Customer Support Portal account for
      convenience. You can use the name provided or change it.
3. Select a Region where you want to deploy your product.
4. The web interface shows if you have Prisma Access or NGFW available in
   this tenant where you can associate firewalls or devices.
5. **Agree to the terms and conditions**, and **Activate**.

   A single default tenant is autocreated behind the scenes, and the product is
   activated in the tenant.

   This tenant, and any others created by this Customer Support Portal
   account, will have the  Superuser role.
6. Common ServicesProducts displays the status of the activation, such as
   initializing or
   complete.
7. After the status is complete, you must go to the Common ServicesDevice Associations tab to add firewalls to the tenant: [Device Associations](https://docs.paloaltonetworks.com/common-services/device-associations/get-started).
8. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from email:

     ![]()
   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesProducts:

     ![]()
9. Get started with [SaaS Security Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline).
10. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-44"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/activate-sspm-repeat-visits>*

#### Return Visit SaaS Security Posture Management Activation

Learn how to activate your SaaS Security Posture Management for repeat visits.

Follow these steps if you have already completed first time activation, you have
already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
another product in your existing hierarchy.

1. Choose the Customer Support Account number that you want
   to use to activate.

   ![]()
2. Allocate the subscription to the Recipient tenant of
   your choice.

   You can hover over each tenant to see which apps you already activated.

   ![]()
3. Select a Region where you want to deploy your product.
4. **Agree to the terms and conditions**, and **Activate**.
5. (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
6. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).
7. [Get started with CIE](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started).

---

<a id="cs-common-services-license-activation-subscription-tenant-management-45"></a>

#### Common Services: License Activation, Subscription, & Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/sspm-activation/convert-sspm-evaluation-to-production>*

#### Convert SSPM Evaluation to Production Through Common Services

Learn how to convert a standalone SaaS Security Posture Management (SSPM) evaluation
license to a production license on a single tenant through Common Services.

If you have an evaluation license for standalone SaaS Security Posture Management
(SSPM), you can convert it to a production license. After you receive an email from
Palo Alto Networks identifying the SSPM license you are converting, click the email
link to begin the activation process.

1. Select Get Started with SaaS Security Posture Management
   (SSPM) in your email.
2. You are automatically directed to Common ServicesSubscription & Add-ons, where you activate the subscription for your product.
3. Use one of the following activation methods.

   - Select your existing Tenant to convert your
     evaluation license to a production license on the existing tenant:

   ![]()

   - Select Create New to convert your evaluation
     license to a production license on a new tenant:

   ![]()
4. The Customer Support Account is auto-populated with the
   same CSP that you used for the evaluation.
5. The Region is auto-populated with the same region that
   you used for the evaluation.
6. Agree to the terms and conditions, and
   Activate.
7. .
8. Common ServicesTenant Management displays the status of the activation, such as
   initializing or
   complete.
9. After the status is complete, you can launch SSPM
   from one of the following options.

   - Launch from the hub tile:

     ![]()
   - Launch from Common ServicesTenant Management. You’ll notice that you have a new
     Contract serial number:

     ![]()
10. [Get Started with SSPM](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-sspm/get-started-with-sspm/whats-sspm)
    documentation.
11. (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).

---

---

# Strata Cloud Manager - Subscription and Tenant Management

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager on 2026-06-27. 35 pages. Absolute URLs.

> Scoped to: /subscription-and-tenant-management

## Table of Contents

  - [Manage Subscriptions](#scm-manage-subscriptions)
    - [How to Access Subscriptions?](#scm-how-to-access-subscriptions)
    - [Request a Trial Add-On](#scm-request-a-trial-add-on)
    - [Activate Add-Ons](#scm-activate-add-ons)
    - [Convert a Trial to a Production License](#scm-convert-a-trial-to-a-production-license)
    - [Modify License Allocation](#scm-modify-license-allocation)
    - [Future-Dated Subscription](#scm-future-dated-subscription)
    - [Extend or Renew a Subscription](#scm-extend-or-renew-a-subscription)
    - [Amend a Subscription](#scm-amend-a-subscription)
    - [Expiring and Expired Subscription](#scm-expiring-and-expired-subscription)
    - [Deactivate a Product](#scm-deactivate-a-product)
  - [Tenant Management](#scm-tenant-management)
    - [What is a Tenant?](#scm-what-is-a-tenant)
    - [Add a Tenant](#scm-add-a-tenant)
    - [Edit a Tenant](#scm-edit-a-tenant)
    - [Manage Tenant Licenses](#scm-manage-tenant-licenses)
    - [Delete a Tenant](#scm-delete-a-tenant)
    - [Transition from Single Tenant FedRAMP to Multitenant FedRAMP](#scm-transition-from-single-tenant-fedramp-to-multitenant-fedramp)
    - [Move an Internal Tenant](#scm-move-an-internal-tenant)
    - [Acquire an External Tenant](#scm-acquire-an-external-tenant)
    - [Approve an External Tenant Acquisition](#scm-approve-an-external-tenant-acquisition)
    - [Limitations for Moving and Acquiring Tenants](#scm-limitations-for-moving-and-acquiring-tenants)
    - [Tenant Hierarchy Limits](#scm-tenant-hierarchy-limits)
    - [Edit Telemetry Settings](#scm-edit-telemetry-settings)
  - [Product Management](#scm-product-management)
- [Subscription and Tenant Management](#scm-subscription-and-tenant-management)
      - [Deactivate all Products](#scm-deactivate-all-products)
      - [Deactivate an Individual Product](#scm-deactivate-an-individual-product)
      - [Firewall and SD-WAN](#scm-firewall-and-sd-wan)
      - [SASE](#scm-sase)
      - [Firewall and SD-WAN](#scm-firewall-and-sd-wan-1)
      - [SASE](#scm-sase-1)
      - [Firewall and SD-WAN](#scm-firewall-and-sd-wan-2)
      - [SASE](#scm-sase-2)
  - [Request Evaluation to Production Conversion](#scm-request-evaluation-to-production-conversion)

---

<a id="scm-manage-subscriptions"></a>

### Manage Subscriptions

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management>*

Learn how to manage subscriptions through .

**Important**: We are rolling out this new, unified activation experience in
stages. For supported SASE products, you may see the new activation console now,
or you maybe directed to use the Hub for activation until the update reaches
your tenant.

The Subscription and Add-ons page in the
Activation Console serves as your singular destination for
all product activation and entitlement management. This unified portal is designed to
streamline the entire process from product acquisition to deployment. Users may now log
in to the Activation Console at any time to view, activate, and
manage all the product entitlements.

![]()

#### Subscriptions and Trials Tab

The Subscriptions and Trial tabs
provide a centralized view of all product entitlements associated with the selected
tenant, enabling customers to monitor, manage, and activate both purchased and trial
products efficiently.

**Subscriptions Tab**

The Subscriptions tab lists all purchased product
entitlements, displaying critical details such as activation status, tenant
allocation, allocated versus total license quantity, expiration dates, and add-on
availability. These details allow customers to quickly assess whether licenses are
fully activated, partially allocated, or pending activation, and understand how
entitlements are being utilized across tenants.

In the Subscriptions page, you will see the following:

- **SASE**

  The SASE tab displays all SASE products associated with the
  tenant, including both activated products and those pending activation.
  You can activate these products directly from the Activation Console.
  Currently, the Activation Console supports activation only for SASE
  products.
- **Firewall and SD-WAN**

  The Firewall and SD-WAN tab lists all Next-Generation Firewall(NGFW) and SD-WAN products
  that are activated on this tenant. For activating Next-Generation Firewall (NGFW) and SD-WAN products,
  you must follow the activation procedure using Magic links, as
  activation through the Activation Console is not supported for these
  products.

![]()

**Trials Tab**

The Trials shows all trials that are ready to activate or have
already been activated. Key details include activation status, tenant allocation,
allocated versus total trial license quantity, expiration dates, and associated
add-ons. This ensures customers can track trial usage and manage trial product
activations effectively.

Both tabs include robust search and filtering capabilities, allowing users to locate
specific product entitlements using product name, entitlement group ID, activation
status, or other displayed attributes. This functionality makes it easy to navigate
large volumes of product entitlements and ensures quick access to the information
needed for decision-making and license management.

![]()

#### Subscriptions List

In both the Subscriptions and Trials
tabs, you can view a list of your product entitlements along with high-level
subscription details for each product:

- **Product**  – Displays the product name and the product
  Entitlement group ID (previously called Serial no). If the product
  supports trial add-on activation, a Request Add-On
  Trial button is available to request it.
- **Description** – Displays the base product license
  associated with the product entitlement.
- **Allocated/Total** – Lists the quantity of allocated
  licenses on your tenant compared to the total available.
- **Add-Ons** – Displays the number of available trial and
  purchased add-ons. Hover over this field to view details, such as
  whether an add-on is already activated or ready to activate.
- **Allocated Tenants** – Shows the number of tenants for
  which licenses are allocated.
- **Status** – Indicates the activation status of the product,
  such as:

  - Needs Activation
  - Needs Activation, Contains Future Dated
  - Activation in Progress
  - Active Fully Allocated
  - Active Partially Allocated
  - Future Dated
  - Activation Failed
- **Expiration Date** – Shows the license expiration date.
- **Actions** – Provides options to activate a product, launch the
  product UI, or view details.

![]()

#### View Subscription Details

You can access detailed information for a specific product entitlement by clicking
View Details from the Activation
Console. This opens a dedicated page where you can examine the
activation status, license information, and entitlement identifiers for the selected
product. Key details such as the start date, expiry date, and
entitlement group ID are clearly displayed to provide
complete visibility into the product entitlement.

#### Subscription Details

The Details tab presents comprehensive information about the
selected product entitlement, organized into several sections:

- **Tenants** – Displays all tenants associated with the
  product, including the tenant name and license allocation quantity for
  each tenant.
- **Description** – Shows details of the base product,
  including the product name, total allocated licenses, and remaining
  available quantity.
- **Purchased Add-Ons** – Lists all purchased add-ons along
  with their activation status and license allocation.
- **Trial Add-Ons** – Displays all active trial add-ons and
  their respective allocation.
- **Future Entitlements** – If the product license has a future start date,
  this section shows the future start and expiry dates for the
  entitlement.

![]()

#### Activate and Manage License

From the View Details page, you can also perform key actions to manage your
licenses:

- **Activate** – Activate a license for the selected product, whether it is
  a purchased license or a trial license. To activate, click Activate and
  provide the required product information.

  ![]()
- **Manage** – For products that are already activated, you can manage
  licenses by performing actions such as reallocating licenses to different
  tenants or activating add-ons.

  ![]()

#### Help and Support

The Help and Support tab provides all the essential product
details needed when creating a support ticket. This ensures support engineers have
the necessary context to address issues quickly and efficiently.

![]()

#### Tenants Browser

In the left pane, you will see a tenant browser. If your environment has only one
tenant, the browser displays the primary tenant, and all related subscription and
trial details automatically appear in the Subscriptions and
Trials tabs. If your environment includes multiple
tenants, the tenant browser presents a hierarchical view, starting with the root
tenant at the top level, followed by the child tenants you have access to. You can
search for and select a tenant to view its corresponding product entitlements,
subscription details, and license allocations. This structure allows you to easily
navigate between tenants and ensures that you always view and manage information in
the correct context.

![]()

---

<a id="scm-how-to-access-subscriptions"></a>

#### How to Access Subscriptions?

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription>*

Contains details about the various ways in which the subscriptions can be
accessed.

After you activate a license for your product, there are a few ways to access
Subscription Management.

|

Prisma SASE Multitenant Portal and FedRAMP | Single Tenant View of the Activation Console | Multienant View of the Activation Console | Single Tenant AIOps for NGFW and Strata Cloud Manager | Multitenant AIOps for NGFW and Strata Cloud Manager |

| --- | --- | --- | --- | --- |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|

If you're a FedRAMP Moderate customer as of January 2024 or Prisma SASE FedRAMP High "In Process" customer as of December 2023, the following also applies to you.  If you have received information about the transition of your tenant to the Prisma SASE Multitenant Portal, you can access through the original support account view of the Activation ConsolePrisma SASE Platform button Tenants and ServicesCommon ServicesSubscription Management. | From the tenant view of the Activation ConsoleCommon Services  button, you will see Subscriptions & Add-ons in a single tenant environment. | From the tenant view of the Activation ConsoleCommon Services  button, you will see Subscriptions & Add-ons in a multitenant environment | If you have a single tenant, you can access through SettingsSubscriptions . | If you have a multitenant environment, you can access through System SettingsSubscriptions List . |

---

<a id="scm-request-a-trial-add-on"></a>

#### Request a Trial Add-On

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/request-trial-add-on>*

This section contains instructions to request a trial add on.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access - Prisma Browser - Strata Cloud Manager Pro | - Superuser Role |

You can request a trial for only the following Prisma Access
add-ons from within the Activation ConsoleActivation Console.

- Prisma Browser
- Strata Cloud Manager Pro

To request a trial add-on:

1. Log in to the Activation Console.
2. In the Activation Console, select Subscriptions &
   Add-ons.
3. Locate your base Prisma Access product and select Request
   Add-On Trial next to the product.

   ![]()

   ![]()
4. From the available add-on products, select the products for which you want
   trial access.

   ![]()
5. Click Activate Free Trial.
6. Once it is approved, you will see a notification in the Activation ConsoleSubscriptions.
7. After approval, the add-ons will be automatically activated and will be
   accessible in the Strata Cloud Manager.
8. You can also View Details of the product to see the
   add-on status.

---

<a id="scm-activate-add-ons"></a>

#### Activate Add-Ons

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/activate-add-ons>*

This section contains instructions to activate add-ons.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access | - Superuser Role |

Some Prisma Access add-ons are activated automatically, while others
require manual activation from the Activation Console.

After you purchase an add-on product, you’ll receive a welcome email that
includes a direct link to the Activation Console. Use this link to access the
Activation Console and begin the activation process.

To activate the Add-on, perform the following:

1. Log in to the Activation Console.
2. In the Activation Console, select Subscriptions &
   Add-ons.
3. From the list of products, locate the product associated with your
   add-on.
4. Click **⋮ → Manage** next to the base product.

   ![]()
5. Follow the on-screen prompts to complete the add-on activation.

---

<a id="scm-convert-a-trial-to-a-production-license"></a>

#### Convert a Trial to a Production License

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod>*

This section contains instructions to convert a trial to production
license.

When a trial subscription is converted to a production subscription, you will receive
a welcome email with an activation link. Proceed to activate using one of the
following procedures:

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/sase-trial-to-prod.html#topic-65d32790-d974-4843-bcd9-f8c21eabb497)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/firewall-trial-to-prod.html#topic-fcf7f43c-ca76-4aa3-9957-a59732cf3989)

#### SASE

This section contains instructions to convert a trial license of SASE Products to
Production license

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

When a trial entitlement is converted to a Production entitlement, you’ll
receive a welcome email that includes a direct link to the Activation Console. Use
this link to access the Activation Console and begin the activation process.

To convert the trial to a production license, perform the following:

1. In the Activation Console, navigate to the Subscriptions
   tab. The new production entitlement appears with a Needs
   Activation status.

   ![]()
2. Select Activate next to the production
   entitlement.
3. Select the desired Tenant. You can choose the existing
   trial tenant or a new tenant for deployment flexibility.
4. Select a Region nearest to the storage location of the data logs if you are
   changing the tenant.
5. Select the existing trial license you wish to replace in the
   Replaceable License section.

   ![]()
6. Agree to the terms and conditions, and select Activate
   Now.

#### Firewall and SD-WAN

This section contains instructions to convert firewall and SD-WAN trials to
production license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

Use the activation link provided by Palo Alto Networks to convert your existing
trial subscription license to a production license. Additionally, you can use this
opportunity to convert both the active trial licenses and to activate the production
license for your subscription for unlicensed tenants or devices at the same time.

1. Purchase the production license or subscription for your product.

   You need to contact your Palo Alto Networks sales representative to purchase
   the production license.
2. Click the activation link to begin the license conversion.

   The activation link is provided to you in an email from Palo Alto Networks.

   (Next-Gen Firewalls) Subscriptions are activated using an
   activation link only. Contact Palo Alto Networks
   [Customer Support](https://support.paloaltonetworks.com/) to continue the license
   conversion if you receive an email that does not include an activation
   link for your license conversion, and instead only includes auth codes.

   Do not activate the auth codes on your Next-Gen firewalls. Activating
   these auth codes may require Palo Alto Networks Customer Support to
   delete the trial license you want to convert. In some cases, this may
   cause your Next-Gen firewall to be restored to factory defaults and
   delete all existing configurations associated with the subscription.
3. Follow the activation procedure for your subscription.

   You must select the same tenant where the trial license is active to convert
   it to a production license. Additionally, you can use the same activation
   flow to convert trial licenses to production licenses and to activate the
   production license on tenants or devices with no active license at the same
   time.

---

<a id="scm-modify-license-allocation"></a>

#### Modify License Allocation

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations>*

This section contains instructions to modify your license allocation to other
tenants.

You can increase or decrease license allocations for a tenant after
activation. When you reduce a tenant’s allocation, the reduced quantity returns to
your license pool, and you can reallocate it to another tenant to maximize license
utilization across your organization. If you reduce license capacity for a Tenant
Service Group (TSG), a fully allocated license automatically converts to a shared
allocation.

When you purchase additional license capacity, it is no longer allocated to
existing TSGs by default. Instead, you decide whether to assign the new capacity to
the same TSG or distribute it across multiple TSGs, depending on your organization’s
needs. For example, if you purchase additional licenses for a new tenant, you can
directly allocate the new capacity to that tenant, or adjust allocations across
existing tenants as needed.

When you reduce the license capacity:

- You cannot reduce allocations below 200 users, the minimum required
  for service continuity.
- You can only reduce licenses in multiples of 10.
- When you reduce base license quantities, associated add-ons such as
  ADEM-AIOps, ZTNA Connector, or Remote Browser Isolation automatically adjust
  to maintain alignment.
- The mobile users and remote networks quantity can be reduced to
  either minimum quantity or it can also be made zero by deselecting those
  options.
- You cannot reduce the license capacity for Panorama Managed
  tenants.

All superusers, multitenant superusers, and business administrators of the
TSG will receive notification when you reduce license capacity. If the reduction
requires configuration changes (for example, adjusting bandwidth for sites), you
must make these changes before committing the configuration. Until then, commits are
blocked with a license quantity mismatch message.

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/sase-modify-lic-allocation.html#topic-35ba94d8-7ae0-4936-9a31-8sdwd520698bff1e)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/firewall-modify-lic-allocation.html#topic-a277402e-0556-4ab9-af0e-7d48c08c617d)

#### SASE

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click ⋮Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   Note: If you are modifying the allocation for the default tenant, ensure
   that you reduce the assigned license quantity. The reduced quantity
   becomes available for reallocation to other tenants in the
   hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat from the [Step 3](#scm-modify-license-allocation) to allocate licenses
   to additional tenants.

   Validate the license allocation by switching to the corresponding tenant in
   the tenant browser and reviewing the allocation details.

   ![]()

#### Firewall and SD-WAN

This section contains instruction to modify license allocation in firewall
products.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html) the
   Subscription.
2. [Search the subscriptions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions.html) table with
   your Tenant Service Group ID (tsg\_id).

   For the filtered TSG, you can verify the status of the assigned quantity
   compared to the total quantity. You also see the associated tenants where
   the subscription is currently allocated.

   ![]()
3. From Actions, select Activate Cloud
   Tenant.

   You will be directed to the Activate Subscription
   page.
4. Select an existing tenant or create a new tenant.
5. Modify the license allocation and select Done.

   ![]()
6. Agree to the Terms and Conditions and Activate.
7. In both Subscription and Tenant
   Management, you can verify the change in license
   allocation.

   ![]()

---

<a id="scm-future-dated-subscription"></a>

#### Future-Dated Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/future-dated-subscriptions>*

This contains details about where and how you can find the future dated license
details.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Activation Console | - Superuser Role |

This section describes how to manage licenses and subscription renewals that are
purchased in advance of their effective date. It explains how future-dated licenses
appear in the Activation Console, how renewals are reflected, and where to view upcoming
start dates and subscription details.

##### Future-Dated Licenses

To support flexible procurement and advanced planning, subscriptions or licenses can
be purchased ahead of their intended start date. These subscriptions are displayed
in the Activation Console with a Contains
Future Dated status, indicating that they have been secured
but are not yet available for activation or use.

![]()

##### Future-Dated Renewal

To ensure uninterrupted service, renew your subscriptions before their
expiration date. Submitting a renewal request in advance helps prevent service
disruption and enables seamless continuation of your subscription.

After your renewal request is successfully processed, you will receive a confirmation
email with the updated subscription details. In addition to the email notification,
you can view the updated status and renewal details directly in the Activation
Console. Renewed subscriptions display a Contains Future
Dated status, indicating that the upcoming term has been secured.
The new subscription term and its effective start date are listed under the
Future Subscriptions section on the subscription
Details page, providing clear visibility into the
upcoming renewal period.

To view details of a renewed subscription:

1. Click View Details for the respective
   product.
2. In the Future Entitlement section, review
   the start date, expiry
   date, and complete license details.

   ![]()

---

<a id="scm-extend-or-renew-a-subscription"></a>

#### Extend or Renew a Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/extend-subscription>*

Learn how to extend or renew a subscription through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can extend or renew your expiring license through Common Services. After
you request an extension from IT, and your updates are ready for use, you will
receive an activation link in your email.

- The following steps apply if you allocated part of your production license
  during the initial activation and you [share the license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) between multiple
  tenants.
- The following steps also apply if you allocated part of your evaluation
  license during the initial activation, you [share the license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/share-license-allocation-for-cloud-managed-prisma-access) between multiple
  tenants, and you are converting to a production license.
- This does not apply to a full allocation or to a single tenant environment,
  regardless of production license extension or evaluation license to
  production conversion. In a full allocation or single tenant environment,
  there are no additional steps after clicking the activation link.

1. Click the activation link in your email.
2. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Common ServicesTenant Management.
3. Select Tenant Management. Only one way is shown
   here.

   ![]()
4. In Tenant Management, you see blue dots indicating that you need to take
   further steps.
5. Use the blue dots to find the tenant with the subscription that you need to
   extend, select the Tenant Name  and
   Edit the licensed products.

   ![]()
6. Agree to the terms and conditions and
   Activate Now.

---

<a id="scm-amend-a-subscription"></a>

#### Amend a Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/amend-subscription>*

Learn how to amend a subscription.

You can amend your production license subscription through Common Services. Reasons for
amending include, but are not limited to, the following:

- new add-ons
- subscription modification
- [evaluation to production
  conversion](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/request-eval-to-prod.html#ide637199d-53b1-43c3-8a71-d67c34c17b5d)

After your subscription updates are ready for use, you will receive an activation
link in your email. You can click the link or you can go directly to manage your
tenant.

The following steps apply to a full license allocation or to
a single tenant environment. Use [extend or renew](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/extend-subscription.html) for shared license scenarios.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html)
   Common ServicesTenant Management.
2. Select Tenant Management. Only one way is shown
   here.

   ![]()
3. Use the blue dots to find the tenant
   with the subscription that you need to amend, select the Tenant
   Name  and Edit the licensed products.

   ![]()
4. Make any necessary changes and select Activate Now.

---

<a id="scm-expiring-and-expired-subscription"></a>

#### Expiring and Expired Subscription

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub>*

Learn how to track and manage about to expire and expired subscriptions to avoid
service interruptions.

This section explains how to monitor expiring and expired subscriptions and take
timely action to maintain uninterrupted service. It describes how subscription
statuses are visually indicated, where expired subscriptions are listed.

- [SASE](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/sase-expiring-subscription.html)
- [Firewall and SD-WAN](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/firewall-expiring-subscription.html)

#### SASE

Details about where to find the expiration details and the visual indicators to
identify them.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama or Strata Cloud Manager) - Prisma Browser - Remote Browser Isolation - Next-Generation   CASB for Prisma Access and NGFW - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.

  ![]()
- Expired licenses will have 

  ![]()

  icon next to their expiration date to identify
  expired licenses.

  ![]()

#### Firewall and SD-WAN

Learn how to track and manage about to expire and expired subscriptions to avoid
service interruptions.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.
- Expired subscriptions are listed separately under the
  Expired tab for easy access.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html)
   Common ServicesSubscriptions & Add-ons.
2. Select Subscriptions & Add-ons. (This example
   demonstrates one method.)

   ![]()
3. In the Active tab, view all active subscriptions,
   including those expiring within 30 days

   - Expiring subscriptions have the

     ![]()

     icon next to their expiration date.
   - If you have renewed a subscription but it has not yet become active,
     those subscriptions have the 

     ![]()

     icon next to its start date.

   ![]()
4. To view expired subscriptions, go to the Expired
   tab.

   ![]()

---

<a id="scm-deactivate-a-product"></a>

#### Deactivate a Product

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product>*

This section contains instructions to deactivate a product and then reuse the tenant
or the license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can deactivate either an individual product or all products associated
with a Tenant Service Group (TSG). Deactivation helps you manage tenant resources
efficiently by allowing you to reuse existing tenants and make optimal use of
available licenses.

When you deactivate a product, it is removed from the tenant, and the
associated license can be reallocated to another tenant

You can deactivate:

- **All the products in a tenant:** Deactivate every product
  linked to the tenant.
- **Individual product:** Deactivate a single product from the
  tenant. This is supported only for Cloud Identity Engine and Security
  Lifecycle Review (SLR)

When you deactivate or remove all the products in a tenant, all its add-ons will also
be deactivated and removed from the tenant. After you initiate deactivation, you
have a 24-hour grace period to cancel the deactivation.

When you initiate deactivation, all the superusers will receive an email notification
during all the states of the activation process, such as scheduled deactivation,
deactivation successful, and deactivation failure.

- [Deactivate All Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all.html#topic-87d9ebf3-db73-4a08-80c4-2b1af9718476)
- [Deactivate Individual
  Products](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products.html#topic-9aef1da4-09af-471f-81b5-c3d6103fe68c)

#### Deactivate all Products

This topic contains procedure to deactivate all the products in the
tenant.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you
   have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate all the products in the tenant, click the Deactivate
   Products icon.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

#### Deactivate an Individual Product

This topic contains to deactivate specific products from the tenant.

1. Use one of the[various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you have a single
   tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate individual products, go to Actions  Deactivate Product.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="scm-tenant-management"></a>

### Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants>*

Learn how to add, delete, move, and acquire tenants.

You can create and manage a hierarchy of business organizations and units, each of which is a
[tenant](#). For each tenant, you specify a name that helps
you and others to easily identify it, such as the company name, a division,
or a geographic location (along with a business vertical designation, such
as retail or wholesale). You will allocate licenses to your tenants so that
you can manage and monitor the instances of all your products. For more
information about tenants, see [What is a Tenant?](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html#id6444f457-9deb-4cc5-8bf1-3c7eb0ab2ba4)
or the Common Services
[FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq).

Depending on your environment, you will see one of the following menus for
managing your tenants: Tenant Management or
Tenants.

You won't see this menu if you have a single tenant. You will see
Products instead. In a single tenant
environment, you can manage your products through [product management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-products.html).

|

Prisma SASE Multitenant Portal and FedRAMP | Multienant View of the Activation Console | Multitenant Strata Cloud Manager |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

From the original support account view of the Activation ConsolePrisma SASE Platform button Tenants and ServicesCommon Services, you will see Tenant Management. | From the tenant view of the Activation ConsoleCommon Services  button, you will see Tenant Management in a multitenant environment. | From the Strata Cloud Manager System Settings, you will see Tenants  in a multitenant environment. |

In a multitenant environment, you can switch between your tenants and also
between the apps or products in the tenant.

![]()

---

<a id="scm-what-is-a-tenant"></a>

#### What is a Tenant?

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant>*

Learn about tenants, Tenant Service Groups, and TSGs. A tenant is a logical container for
managing and monitoring licensed products. Tenant Service Groups enable the management of
multiple customers or business units in a tenant hierarchy that reflects your existing
organizational structure. Each tenant is isolated and can have its own set of policies and
resources, while still being managed from a single location.

Common Services enables you to manage a hierarchy of business units and organizations that
is referred to as a [tenant service group](#). A tenant service group (TSG) is
used to provide a logical container that contains [tenants](#) and other TSGs.
It is the building block for a multitenant hierarchy. Generally, this multitenant
hierarchy is described as a series of nested tenants, where a tenant is used to manage,
monitor, and license products. But mechanically, a tenant is just a TSG. The terms are
often used interchangeably.

After you have received information about the transition of your app instance to a tenant, your
instance is now a single tenant. You have access to Common Services for
subscription management, tenant management, and identity and access management. You do
not have access to the multitenant summary dashboards, as those are not applicable and
not available for single tenants. See the [FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq) if you have more questions about the migration.

Each tenant is automatically assigned a TSG ID, which is primarily for use with [service accounts](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts). However, the TSG ID is also
used for default login purposes. If you clear your cache, or if you log out of the
Strata Multitenant Cloud Manager and log back in, you are logged into the top-level parent
tenant with the lowest TSG ID by default. The top-level parent tenant with the lowest
TSG ID is likely the first one you created.

The [tenant hierarchy limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants) explain the number of
used and unused tenants you can create.

---

<a id="scm-add-a-tenant"></a>

#### Add a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/add-tenants>*

Learn about adding a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

After you create a tenant, you can allocate a supported product license to it or you can create a
child tenant and allocate the license to it. Licenses are allocated per each child
tenant that you need to manage.

If you are adding a tenant for the first time, you are automatically directed to
Tenants when you follow the license activation flow flow,
in which case you can skip to the [select a tenant](#scm-add-a-tenant) step.

If you are not adding a tenant for the first time or you are otherwise not following the general
flow, you can add a tenant from Tenants.

You can create your tenant
hierarchy to reflect your existing organizational structure. You
can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when
creating the hierarchy, in addition to [tenant hierarchy
limits](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are basically the same.
2. Select a tenant to be the
   parent of the child tenant you want to add.
3. Select New Tenant.

   ![]()
4. Specify a Name for the child that
   is representative of its function and select a Business Vertical.

   ![]()

   The
   Business Vertical is used for summarizing tenant network traffic
   information.
5. Select the **Telemetry Tier**, which defines the type of telemetry data
   transferred to the **Data Region** for monitoring and analysis.

   - Full (Recommended)- collects comprehensive data
     to support in-depth monitoring and analysis. This is the default
     setting.
   - Diagnostic- collects only essential data required
     for diagnostics and troubleshooting.

   To learn more about the data collected in each tier, see [Device Telemetry Metrics
   Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

   Telemetry Tier must be set to Full if the tenant
   includes Strata Cloud Manager.
6. Select the Data Region  where the telemetry data will be
   stored.

   - You cannot edit the region if Strata Logging Service, Strata Cloud
     Manager, or IOT Security is already enabled in the tenant.
   - If you add Strata Logging Service, Strata Cloud Manager, or IOT
     Security to the tenant later, the data region automatically switches
     to the region used by that product.
7. Specify a Support
   Contact, such as an email address or a phone number
   of a person to contact for support purposes. The maximum character
   limit for the contact is 255.

   - Select Inherit from parent if
     the contact person is the same as the parent.
   - Select Use custom if the contact person
     is different from the parent.
8. Set the User Inactivity Timeout to automatically log out
   idle users after a specific period. The default timeout is 30 minutes, but you
   can customize this value between 10 and 60 minutes. Choose a shorter or longer
   duration based on your organization's security policy and operational needs.
   This flexibility allows you to balance security requirements with user
   convenience.

   When no timeout value is set, new tenants automatically adopt the default
   timeout value from their parent tenant. Once you customize the timeout
   value, it becomes independent and is maintained separately for that
   tenant.
9. Add Tenant as a child of the current
   parent tenant in the tenant hierarchy.

   ![]()
10. (Optional) Specify license and activation details
    for your product.

---

<a id="scm-edit-a-tenant"></a>

#### Edit a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/edit-tenants>*

Learn about editing a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

When you create a tenant, you define attributes such as name and support contact to
describe its purpose and management. You can edit these tenant details at any time,
for example, when a support contact changes. This topic outlines the process for
editing tenant details.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are the same.
2. Select the tenant that you
   want to edit.
3. Select Edit Tenant.

   ![]()
4. Change any of the details about the tenant, as needed.

   - Name—Descriptive name that identifies the
     tenant.
   - Business Vertical—Primary industry or sector in
     which the tenant operates. This helps categorize and understand the
     tenant's main focus and potential needs. (For example,
     Wholesale & Retail.)

     Support
     Contact—Information of a person to contact for
     support purposes. (For example, John Smith, IT Manager -
     jsmith@globaltech.com, +1 555-123-4567)
   - User Inactivity Timeout—Number of minutes after
     which Strata Cloud Manager will log idle users out of the tenant.
     Choose a value between 10 and 60 minutes (30 minutes is default).

     New tenants automatically inherit the default
     timeout value from the parent tenant. After you modify the timeout
     value for a child tenant, the value is maintained independently.
   - Telemetry
     Tier—the type of telemetry data transferred to the **Data
     Region**.
     - Full (Recommended)- collects
       comprehensive data to support in-depth monitoring and analysis.
     - Diagnostic- collects only essential data
       required for diagnostics and troubleshooting.

     To learn more about the data collected in each tier, see [Device Telemetry Metrics
     Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

     - Downgrading from **Full** to **Diagnostic** may
       result in the loss of critical telemetry data needed for
       advanced analysis and support.
     - Only the super user can edit the Telemetry
       Tier.
     - Telemetry Tier must be set to Full if
       the tenant includes Strata Cloud Manager.
   - Data Region—the
     region where the telemetry data is stored.

     If
     Strata Logging Service, Strata Cloud Manager, or IOT Security is
     already enabled in the tenant, you cannot edit the region. It
     defaults to the product region.
5. Save.

---

<a id="scm-manage-tenant-licenses"></a>

#### Manage Tenant Licenses

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/manage-tenant-licenses>*

If you are activating a license for the first time, you will use a license activation flow.

If you are not activating a license for the first time or you are otherwise not following a
general flow, you can claim a license from Subscription &
Add-ons. Then you can activate it from Tenant
Management.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Common ServicesTenant Management.
2. Select Tenant Management. Only one way is shown
   here.

   ![]()
3. Edit the licensed products.

   ![]()
4. The rest is similar to [activating a license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation) for Prisma Access (Managed by Strata Cloud Manager) and Add-ons.
5. (Optional) [Monitor tenant licenses](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/monitor-tenants/monitor-tenant-licenses).

---

<a id="scm-delete-a-tenant"></a>

#### Delete a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/delete-tenants>*

Learn about deleting a tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Prisma SASE Multitenant Portal - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

After you create a tenant, you can delete it only if the tenant meets the following criteria:

- No activated products, which can be seen from Tenants.
- No child tenants, which can be seen from Tenants.
- No licenses allocated or claimed, which can be seen from Subscriptions &
  Add-ons.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Tenants.

   If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
   instead. The steps are the same.
2. Select the tenant you want to delete and Delete
   Tenant.

   ![]()
3. Select Yes, Delete this Tenant to
   confirm deletion.

   ![]()

   Tenant
   deletion is successful only if the tenant does not have any child
   tenants and only if the tenant does not have any instances provisioned
   for it. If the tenant does have child tenants, delete those children
   first before you delete this tenant. If the tenant has an instance
   provisioned for it, remove the licenses before you delete the tenant.

---

<a id="scm-transition-from-single-tenant-fedramp-to-multitenant-fedramp"></a>

#### Transition from Single Tenant FedRAMP to Multitenant FedRAMP

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/transition-from-single-tenant-to-multitenant>*

Learn how to transition your single tenant Prisma Access FedRAMP to multitenant
FedRAMP.

If you are a new cloud-managed Prisma Access FedRAMP High "In Process" customer as of
December 2023, you can use the following information to transition
from a single tenant deployment to a multitenant deployment.

After you receive an email from Palo Alto Networks identifying the license you are activating,
including all your add-ons and capacities, Get Started
with Prisma Access to begin the
activation process.

1. To transition from a single tenant Panorama-managed Prisma Access to multitenant, select Get
   Started with Prisma Access in
   your email.
2. Follow the steps to [Activate a License
   for Single Tenant Cloud-Managed](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-activation)
   Prisma Access FedRAMP, but do not
   Launch the products
   yet.
3. Instead, select Tenant Management.
4. Select +Add
   tenant.

   ![]()
5. Adding a subtenant converts your single tenant to a multitenant
   hierarchy. Select Yes to continue.
6. [Manage your tenants
   through the](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started) Multitenant Cloud Manager.

---

<a id="scm-move-an-internal-tenant"></a>

#### Move an Internal Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/move-internal-tenants>*

Learn how to move an internal tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

If you're a managed security service provider (MSSP) or distributed enterprise and
you [create a
multitenant hierarchy](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you might need to move a tenant that is part of
your tenant hierarchy to a different location. You can do this by moving an internal
tenant.

Any tenant is considered an internal tenant if it's within your tenant hierarchy, and
you have Superuser access to the source and target tenants. It's possible to move
tenants within the same top-most, root-level, parent tenant or intermediate tenants
of your hierarchy. See [additional limitations](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition.html). You
would move an internal tenant primarily in the case of testing, demonstrations,
reorgs, correcting mistakes, and more.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Settings.
2. Select Tenants.
3. From the tenant that you want to move, select Move
   Tenant.

   In the following example, the source tenant is Child Tenant East. You must
   have the Superuser role for Child Tenant East to move this tenant to a new
   location in the hierarchy.

   ![]()
4. You’re prompted with a view of the current tenant hierarchy, so that you can
   select where to move the tenant. Select a new parent tenant for managing the
   subtenant and **Continue**.

   In the following example, the target tenant is Child Tenant West. You must
   also have the Superuser role for Child Tenant West to move Child Tenant East
   to become its subtenant.

   ![]()
5. Inherited roles that would be lost after the move are displayed before the
   final confirmation. Select Confirm.

   Inherited custom roles that would be lost after the
   move are also displayed before the final confirmation. Custom roles that
   were defined in a parent tenant and assigned in a child tenant would be lost
   because the role doesn't exist in the new hierarchy.

---

<a id="scm-acquire-an-external-tenant"></a>

#### Acquire an External Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants>*

Learn how to acquire an external tenant through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

If you are a Managed Security Service Provider (MSSP) or distributed enterprise and
you [create a
multitenant hierarchy](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/add-tenants.html), you might need to acquire and manage tenants that
are not part of your current tenant hierarchy. You can do this by acquiring an
external tenant.

Any tenant is considered an external tenant if it isn’t within your current tenant
hierarchy. You can only acquire a top-most, root-level, parent tenant through an
external tenant acquisition. You would acquire an external tenant primarily in the
case of corporate acquisitions or mergers or reorgs. A tenant can have only one
outstanding acquisition request open at a time. See [additional limitations](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition.html).

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html)
   Settings.
2. Select Tenants.
3. From the parent tenant where you will manage your newly acquired target tenant,
   select Acquire New Tenant.

   ![]()
4. At the prompt, provide the TSG ID and superuser email addresses of the
   administrators who need to accept the pairing request.
5. Select Acquire Tenant.
6. The administrator of the target tenant needs to approve the request.

---

<a id="scm-approve-an-external-tenant-acquisition"></a>

#### Approve an External Tenant Acquisition

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/approve-external-tenant-acquisition>*

Learn how to approve an external tenant acquisition through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

After a Managed Security Service Provider (MSSP) or distributed enterprise submits a
request to [acquire an external tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html), the administrators of the newly
acquired target tenant receive an email notification and an acquisition key. Only
one administrator has to approve the request for the tenant acquisition.

If you’re an administrator of the target tenant, you have two choices for approving
the request.

1. (Optional) If you have the email, select View
   Request from the message.
   1. The acquisition key is prepopulated, so you can **Accept** the
      request. 

      ![]()
   2. Confirmation is displayed. Select Close.
2. (Optional) If you are one of the administrators contacted in the [request to acquire an external tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html), and you’re already logged
   into the Strata Cloud Manager, but you don’t have the email:
   1. Select View Request from the banner.
   2. At the prompt, you can select to resend the acquisition key.
   3. Enter the acquisition key from your email.
   4. Accept.
   5. Confirmation is displayed. Close.

---

<a id="scm-limitations-for-moving-and-acquiring-tenants"></a>

#### Limitations for Moving and Acquiring Tenants

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limitations-tenant-move-acquisition>*

Learn about the limitations and caveats for moving internal tenants and acquiring
external tenants through Common Services.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Tenant or tenant service group (TSG) - Strata Cloud Manager - Strata Multitenant Cloud Manager - The Activation Console | - Prisma Access license - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) on the source   and target tenants |

The following limitations exist for managed security service providers (MSSP) or
distributed enterprises [moving internal tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/move-internal-tenants.html) and [acquiring external tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/acquire-external-tenants.html).

- You can acquire only the top-most, root-level, parent tenant hierarchies. You cannot
  acquire intermediate tenants within a hierarchy.
- You can't acquire tenant hierarchies with [Service Provider Backbone](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/manage-service-provider-backbones) enabled in the
  hierarchy.
- It's not recommended that a tenant hierarchy without a Service Provider Backbone
  enabled be acquired into a tenant with a Service Provider Backbone enabled. The
  action isn't blocked, but can have inconsistent results.
- You can't acquire a tenant hierarchy with Prisma SD-WAN licenses in the hierarchy at this time.
- Users with access to a tenant that acquires a new target tenant will
  gain access to the target tenant through inheritance.
- Tenant support contacts won't be changed during a move.
- A tenant with no support contact will inherit the new owner's
  contact.
- If a tenant is using a shared Cloud Identity Engine instance, you can't
  acquire it until the shared instance is removed.
- A tenant will keep all custom role definitions created on it.
- All service accounts created on a given tenant will stay with that
  tenant after being moved.
- If some but not all contact email addresses provided are valid tenant
  users, they will still receive the approval request email. Invalid emails will
  be ignored.
- Invalid acquisition requests will fail silently, they will look like
  successful requests to keep tenant information secret from the user.

---

<a id="scm-tenant-hierarchy-limits"></a>

#### Tenant Hierarchy Limits

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/limits-tenants>*

Understand limits in the Common Services hierarchy.

Your multitenant hierarchy has limits for its size and
depth. These limits exist for performance and security purposes.

The tenant hierarchy is comprised of one or more trees of tenant service groups (TSGs). Each tree
has a root TSG. A TSG is a logical container that can contain child TSGs, as well as
licensed tenants.

|

Name | Limit | Description |

| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
|

Hierarchy depth | 10 | Identifies the maximum depth for any given hierarchy tree, starting at depth 1 for the root TSG. |

|

Child TSGs | 100 | Identifies the total number of immediate children permitted for any TSG in the hierarchy. This limit applies only to immediate children of the TSG. It does *not* apply to all descendents (grandchildren, great-grandchildren, and so on) of the TSG. |

|

Unused root TSGs | 10 | Identifies how many unused root TSGs can exist in your Strata Multitenant Cloud Manager. A TSG is unused if it has no child TSGs or tenants. |

---

<a id="scm-edit-telemetry-settings"></a>

#### Edit Telemetry Settings

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/edit-telemetry>*

What is telemetry and how to edit the telemetry settings from the tenant management
page

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Strata Multitenant Cloud Manager - Commercial or FedRAMP deployments | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of Superuser,   Multitenant Superuser, Multitenant IAM Admin |

Telemetry refers to the [device data](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview) collected from your
Next-Generation Firewall (NGFW) or Panorama and sent to Palo Alto Networks. This data
enables cloud-based applications to monitor and manage your devices efficiently.

Telemetry data improves visibility into device health and performance, supports capacity
planning and configuration management, and helps share threat intelligence across
platforms. It also enhances intrusion prevention capabilities and allows for the
evaluation and continuous improvement of threat signatures.

Telemetry settings are configured only at the tenant level. This means that all devices
associated with a specific tenant automatically inherit the telemetry configuration
defined for that tenant.

**What is the default telemetry configuration?**

By default, when you activate a product, telemetry is auto-enabled and the telemetry tier
is set to full. This default setting ensures that the most comprehensive set of
telemetry data is collected from the start, enabling robust monitoring, diagnostics, and
threat analysis.

You can modify the telemetry tier at any time through the **Tenant Management** page
to suit your data collection preferences.

**What are the available telemetry tiers?**

There are two telemetry tiers available, depending on the level of data you want to
transmit:

- **Full**-This tier sends a complete set of telemetry data, including extensive
  device health metrics, configuration summaries, threat activity, and performance
  data for in-depth monitoring and analysis.
- **Diagnostic**-This tier limits the scope of data collected and focuses on
  basic diagnostic information required for troubleshooting and analysis.

To learn more about what each telemetry tier includes, see [Device Telemetry Metrics Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

**Where is the Telemetry Data Stored?**

Telemetry data is stored in a specific data residency region, which you can configure
during product activation or tenant creation.

If the tenant already includes Strata Logging Service, Strata Cloud Manager, or IoT
Security, the data region defaults to the region assigned to that product. In such
cases, you can’t manually select or change the data region.

The telemetry data from the PAN-OS and Panorama devices are transmitted to the data
residency region at fixed [transmission intervals](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-collection).

##### Edit Telemetry Tier and Region

You can modify the telemetry configuration, such as the telemetry tier and data
residency region, at any time from the [Tenant Management](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants/edit-tenants.html) page.

Changes made at the tenant level automatically apply to all devices associated
with that tenant, ensuring consistent telemetry behavior across your deployment.
If the data residency region is configurable, you have the flexibility to update
it to meet your organization’s data governance requirements.

---

<a id="scm-product-management"></a>

### Product Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-products>*

Learn how to add, delete, and rename products .

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Cloud Manager - The Activation Console - Single tenant environment | - IAM [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) of   Superuser, Multitenant Superuser, Multitenant IAM   Admin |

Activating a free product from the Activation Console creates a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where the product is
deployed.

If you have a single [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), you can view, launch,
and manage your products from Products.

|

Single Tenant View of the Activation Console | Single Tenant Strata Cloud Manager |

| --- | --- |

|  |  |
| --- | --- |
|

From the tenant view of the Activation Console Common Services  button, you will see Products in a single tenant environment. | From the Strata Cloud Manager Settings, you will see Products  in a single tenant environment.  Strata Cloud Manager is for commercial deployments only and not yet available for Prisma SASE FedRAMP Moderate or High "In Process." |

You won't see this menu if you're a managed security service provider
(MSSP) or distributed enterprise with a multitenant hierarchy. You
will see Tenants instead. In a multitenant
environment, you can manage and monitor your tenants through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants) and
the [Strata Multitenant Cloud Manager](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform).

From Products, you can launch a product by selecting it
from the product list. 

![]()

#### Get Product Information

From ActionsProduct Information, you can view the information about your product. You
can also copy the information to clipboard for pasting into any
support case you open for the product. 

![]()

#### Rename Instance

From ActionsRename Instance, you can rename the instance of the product. This isn't available for
every product.

#### Delete

From ActionsDelete, you can delete the instance of the product. This
isn't available for every product.

#### Manage Sharing

From ActionsManage Sharing, you can manage sharing of the product. Sharing of some instances are
not automatically inherited by child tenants and must be assigned individually. This
isn't available for every product.

#### Add Tenant

From Add Tenant, you can add a tenant to
transition from a single tenant environment to a multitenant
environment. In a multitenant environment, you can manage and
monitor your tenants through [tenant management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants) and
the [Strata Multitenant Cloud Manager](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform).

#### Switch Between Products

In a single tenant environment, you can switch between the apps or
products in your tenant. 

![]()

Strata Cloud Manager is for commercial deployments only and not
yet available for Prisma SASE FedRAMP Moderate or High "In Process."
See [Fedramp Moderat and High
Support](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements/fedramp-moderate-and-high-support).

---

<a id="scm-subscription-and-tenant-management"></a>

## Subscription and Tenant Management

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management>*

---

<a id="scm-deactivate-all-products"></a>

##### Deactivate all Products

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-all>*

This topic contains procedure to deactivate all the products in the
tenant.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you
   have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate all the products in the tenant, click the Deactivate
   Products icon.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="scm-deactivate-an-individual-product"></a>

##### Deactivate an Individual Product

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/deactivate-product/deactivate-individual-products>*

This topic contains to deactivate specific products from the tenant.

1. Use one of the[various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/manage-multitenants.html) Tenants. If you have a single
   tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) instead. The steps are the
   same.
2. Select the tenant that is linked to the product.
3. To deactivate individual products, go to Actions  Deactivate Product.

   ![]()
4. Specify the reason for deactivation and Schedule
   Deactivation.

   All the superusers will receive an email notification when you initiate
   product deactivation.

   ![]()
5. Cancel Deactivation Request to cancel deactivation
   during the 24 hour grace period.

   ![]()

   ![]()

---

<a id="scm-firewall-and-sd-wan"></a>

##### Firewall and SD-WAN

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/firewall-expiring-subscription>*

Learn how to track and manage about to expire and expired subscriptions to avoid
service interruptions.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.
- Expired subscriptions are listed separately under the
  Expired tab for easy access.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html)
   Common ServicesSubscriptions & Add-ons.
2. Select Subscriptions & Add-ons. (This example
   demonstrates one method.)

   ![]()
3. In the Active tab, view all active subscriptions,
   including those expiring within 30 days

   - Expiring subscriptions have the

     ![]()

     icon next to their expiration date.
   - If you have renewed a subscription but it has not yet become active,
     those subscriptions have the 

     ![]()

     icon next to its start date.

   ![]()
4. To view expired subscriptions, go to the Expired
   tab.

   ![]()

---

<a id="scm-sase"></a>

##### SASE

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/expiring-and-expired-sub/sase-expiring-subscription>*

Details about where to find the expiration details and the visual indicators to
identify them.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama or Strata Cloud Manager) - Prisma Browser - Remote Browser Isolation - Next-Generation   CASB for Prisma Access and NGFW - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

To ensure uninterrupted services, it’s important to renew subscriptions before they
expire or immediately after expiration. To make subscription statuses easily
identifiable, expiring and expired subscriptions are visually marked:

- Subscriptions set to expire within 30 days have the 

  ![]()

  icon next to their expiration date, helping you
  track them in advance.

  ![]()
- Expired licenses will have 

  ![]()

  icon next to their expiration date to identify
  expired licenses.

  ![]()

---

<a id="scm-firewall-and-sd-wan-1"></a>

##### Firewall and SD-WAN

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/firewall-modify-lic-allocation>*

This section contains instruction to modify license allocation in firewall
products.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html) the
   Subscription.
2. [Search the subscriptions](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/activation-and-onboarding/activate-your-prisma-access-license/cloud-managed-prisma-access-and-add-ons-license-activation/search-subscriptions.html) table with
   your Tenant Service Group ID (tsg\_id).

   For the filtered TSG, you can verify the status of the assigned quantity
   compared to the total quantity. You also see the associated tenants where
   the subscription is currently allocated.

   ![]()
3. From Actions, select Activate Cloud
   Tenant.

   You will be directed to the Activate Subscription
   page.
4. Select an existing tenant or create a new tenant.
5. Modify the license allocation and select Done.

   ![]()
6. Agree to the Terms and Conditions and Activate.
7. In both Subscription and Tenant
   Management, you can verify the change in license
   allocation.

   ![]()

---

<a id="scm-sase-1"></a>

##### SASE

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/modify-license-allocations/sase-modify-lic-allocation>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

1. On the Subscriptions page, locate the activated product
   you wish to manage.
2. Click ⋮Manage for the required product.

   ![]()
3. Select the target tenant.

   ![]()
4. Select a Region nearest to the storage location of the data logs.
5. Modify the license allocation as needed.

   Note: If you are modifying the allocation for the default tenant, ensure
   that you reduce the assigned license quantity. The reduced quantity
   becomes available for reallocation to other tenants in the
   hierarchy.
6. Agree to the terms and conditions, and select Activate
   Now to activate the license on the selected tenant.
7. Validate the allocation by clicking View Details and
   hovering over the Tenants to view the license quantity
   for each tenant.
8. Repeat from the [Step 3](#scm-sase-1) to allocate licenses
   to additional tenants.

   Validate the license allocation by switching to the corresponding tenant in
   the tenant browser and reviewing the allocation details.

   ![]()

---

<a id="scm-firewall-and-sd-wan-2"></a>

##### Firewall and SD-WAN

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/firewall-trial-to-prod>*

This section contains instructions to convert firewall and SD-WAN trials to
production license.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) - Prisma Access - SD-WAN | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

Use the activation link provided by Palo Alto Networks to convert your existing
trial subscription license to a production license. Additionally, you can use this
opportunity to convert both the active trial licenses and to activate the production
license for your subscription for unlicensed tenants or devices at the same time.

1. Purchase the production license or subscription for your product.

   You need to contact your Palo Alto Networks sales representative to purchase
   the production license.
2. Click the activation link to begin the license conversion.

   The activation link is provided to you in an email from Palo Alto Networks.

   (Next-Gen Firewalls) Subscriptions are activated using an
   activation link only. Contact Palo Alto Networks
   [Customer Support](https://support.paloaltonetworks.com/) to continue the license
   conversion if you receive an email that does not include an activation
   link for your license conversion, and instead only includes auth codes.

   Do not activate the auth codes on your Next-Gen firewalls. Activating
   these auth codes may require Palo Alto Networks Customer Support to
   delete the trial license you want to convert. In some cases, this may
   cause your Next-Gen firewall to be restored to factory defaults and
   delete all existing configurations associated with the subscription.
3. Follow the activation procedure for your subscription.

   You must select the same tenant where the trial license is active to convert
   it to a production license. Additionally, you can use the same activation
   flow to convert trial licenses to production licenses and to activate the
   production license on tenants or devices with no active license at the same
   time.

---

<a id="scm-sase-2"></a>

##### SASE

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/trial-to-prod/sase-trial-to-prod>*

This section contains instructions to convert a trial license of SASE Products to
Production license

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console - Prisma Access - Prisma Browser - Remote Browser Isolation - CASB-X - Data Security - AI Access Security - SaaS Security Posture Management - Enterprise DLP | - Superuser or Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

When a trial entitlement is converted to a Production entitlement, you’ll
receive a welcome email that includes a direct link to the Activation Console. Use
this link to access the Activation Console and begin the activation process.

To convert the trial to a production license, perform the following:

1. In the Activation Console, navigate to the Subscriptions
   tab. The new production entitlement appears with a Needs
   Activation status.

   ![]()
2. Select Activate next to the production
   entitlement.
3. Select the desired Tenant. You can choose the existing
   trial tenant or a new tenant for deployment flexibility.
4. Select a Region nearest to the storage location of the data logs if you are
   changing the tenant.
5. Select the existing trial license you wish to replace in the
   Replaceable License section.

   ![]()
6. Agree to the terms and conditions, and select Activate
   Now.

---

<a id="scm-request-evaluation-to-production-conversion"></a>

### Request Evaluation to Production Conversion

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/request-eval-to-prod>*

Learn how to request an evaluation license to production license conversion
through.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Strata Multitenant Cloud Manager - Activation Console | - Any [Tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)  that   contains FedRAMP High Prisma Access - Multitenant Superuser [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) |

You can initiate a request to convert your
evaluation license to a production license. This request does not instantly
result in a modification from evaluation to production. After the
request is made, you still work with your Palo Alto Networks account
representative to complete the process.

1. Use one of the [various ways to access](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/subscription-and-tenant-management/about-subscription-management/how-to-access-subscription.html)
   Common ServicesSubscriptions & Add-ons.
2. Select Subscriptions & Add-ons. Only one way is
   shown here.

   ![]()
3. Find the subscription that you want
   to modify, and select ActionsEval to Prod Request.

   ![]()
4. Specify the licenses you would like on your production
   tenant and Send Request. The request is looked
   at your Palo Alto Networks account representative to create a quote.
   Some examples include the following:

   - Sku: Prisma Access
   - LicenseUnits: 100
   - Addon: Service Connection,
     ADEM, SaaS Inline, DLP, IoT
   - Terms: 12 months

   ![]()

---

---

# Prisma Access - Manage Multiple Tenants (Multitenancy)

> Extracted from https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access on 2026-06-27. 11 pages. Absolute URLs.

> Scoped to: /administration/manage-multiple-tenants-in-prisma-access

## Table of Contents

- [Prisma Access Multi-Tenancy](#pa-prisma-access-multi-tenancy)
  - [Multitenancy Configuration Overview](#pa-multitenancy-configuration-overview)
  - [Plan Your Multitenant Deployment](#pa-plan-your-multitenant-deployment)
  - [Create an All-New Multitenant Deployment](#pa-create-an-all-new-multitenant-deployment)
  - [Enable Multitenancy and Migrate the First Tenant](#pa-enable-multitenancy-and-migrate-the-first-tenant)
  - [Add Tenants to Prisma Access](#pa-add-tenants-to-prisma-access)
  - [Delete a Tenant](#pa-delete-a-tenant)
  - [Create a Tenant-Level Administrative User](#pa-create-a-tenant-level-administrative-user)
  - [Control Role-Based Access for Tenant-Level Administrative Users](#pa-control-role-based-access-for-tenant-level-administrative-users)
    - [Remove Plugin Access for a Tenant-Level Administrative User](#pa-remove-plugin-access-for-a-tenant-level-administrative-user)
  - [Sort Logs by Device Group ID in a Multitenant Deployment](#pa-sort-logs-by-device-group-id-in-a-multitenant-deployment)

---

<a id="pa-prisma-access-multi-tenancy"></a>

## Prisma Access Multi-Tenancy

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in   Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

This section only provides information for managing multiple tenants in Prisma Access (Panorama).
For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see
[Prisma SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started).

To
allow you to create and manage multiple Prisma Access instances,
Prisma Access offers multitenancy, which enables you to create up
to 200 instances (tenants) on a single Panorama appliance (or 2
appliances in high availability (HA) mode), with each tenant having
their own separate [templates](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks/add-a-template) and [template stacks](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks/configure-a-template-stack), [device groups](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management/device-groups), and [access domains](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/access-domains).

Existing
or future non-multitenant deployments are not affected by multitenancy
and will continue to function normally. We recommend that you enable
multitenancy only if your organization has a need to manage multiple
tenants in Prisma Access.

This section only provides the tasks
you perform to configure tenants for remote networks, mobile users,
or a combination of remote network and mobile user deployments.
To configure the Clean Pipe service, see [Prisma Access for Clean Pipe](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/clean-pipe.html#id7bd96d66-212b-49e0-861b-628d676d88d3).

---

<a id="pa-multitenancy-configuration-overview"></a>

### Multitenancy Configuration Overview

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/multitenancy-configuration-overview>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

Enabling multitenancy allows you to host multiple instances of Prisma Access on a
single Panorama appliance. Each instance is known as a [Tenant](#).

Prisma Access tenants get their own dedicated Prisma Access instances and they are
not shared between tenants.

![]()

Use the following workflow to configure the ability to manage multiple tenants in a
single Panorama appliance:

1. Enable multitenancy. If you have an existing Prisma Access
   instance, enabling multitenancy automatically migrates your existing Prisma
   Access configuration to the first tenant.

   You give the first (migrated) tenant a name and specify
   an access domain. Prisma Access migrates the templates, template
   stacks, and device groups associated with the existing configuration
   and associates them with the access domain you create.

   After
   you migrate your initial configuration, the administrative user
   in Panorama becomes a superuser with the ability to create and manage
   all Prisma Access tenants.

   ![]()
2. Then, [add tenants to Prisma
   Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access.html#id34997992-9769-4fc2-9304-93f7d0352394).

   To deploy multiple tenants, make sure that you have the
   following license minimums:

   To determine the type of Prisma Access license you have from Panorama, select PanoramaLicenses.

   - If you have a **Business**, **Business Premium**, **Zero
     Trust Network Access (ZTNA) Secure Internet Gateway (SIG)**, or **Enterprise** license,
     use the following minimums as a guideline:

     **Prisma Access
     for Networks** and **Prisma Access for Users**:

     The minimum quantity for all tenants is 200.

     *Units* correspond
     to bandwidth in Mbps for Prisma Access for Remote Networks and the
     number of mobile users for Prisma Access for Users.
   - If your license type starts with GlobalProtect
     Cloud Service, use the following minimums as a guideline:

     **Prisma
     Access for Networks**—You must have a minimum of 200 Mbps available
     in your license for each tenant.

     **Prisma Access for Users**—You
     must have a minimum of 200 mobile users available in your license
     for each tenant.

     In both types of Prisma Access configurations,
     you can add additional licensing (above these minimums) of either
     type. You can increase or decrease the bandwidth or mobile user
     allocation for any tenants after onboarding, as long as you keep
     the minimum required allocation per tenant, and the overall licensed capacity
     is not exceeded.

   You can set up a multitenant configuration
   for only remote networks, only mobile users, or both. You allocate
   licenses accordingly to each tenant when you enable multitenancy.

   If you have a license for remote networks and mobile users, you can set up an individual tenant
   with only mobile users or only remote networks.

   For each tenant you create
   after the first, Prisma Access automatically creates templates,
   template stacks, and device groups for each tenant and associates
   them to the access domain you create. Prisma Access creates this
   environment to allow you to [create a tenant-level
   administrative user](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant.html#id22568b02-14b3-4c80-9dcd-192f224c1d09)using an administrative role based on
   the tenant’s device groups and templates, then creating an administrative user
   based on that role. In this way, you create an administrative user
   that has access to a single tenant without allowing that user access
   to the other tenants that are managed by the Panorama appliance.

   Prisma
   Access creates template stacks, templates, and device group using
   the following naming convention:

   - A service connection
     template stack with the name of sc-stk-tenant,
     where tenant is the tenant’s name.
   - A service connection template with the name of sc-tpl-tenant.
   - A service connection device group with the name of sc-dg-tenant.
   - A mobile user template stack with the name of mu-stk-tenant.
   - A mobile user template with the name of mu-tpl-tenant.
   - A mobile user device group with the name of mu-dg-tenant.
   - A remote network template stack with the name of rn-stk-tenant.
   - A remote network template with the name of rn-tpl-tenant.
   - A remote network device group with the name of rn-dg-tenant.
   - An Explicit Proxy template stack with the name of ep-stk-tenant.
   - An Explicit Proxy template with the name of ep-tpl-tenant.
   - An Explicit Proxy device group with the name of ep-dg-tenant.
   - A Clean Pipe template stack with the name of cp-stk-tenant.
   - A Clean Pipe template with the name of cp-tpl-tenant.
   - A Clean Pipe device group with the name of cp-dg-tenant.

   Template
   stacks, templates, and device groups are created for all Prisma
   Access types, even those for which you might not be licensed. For
   example, if you purchase a license for remote networks, Prisma Access
   automatically creates template stacks, templates, and device groups
   for remote networks, mobile users, and Clean Pipe.

   If you
   add custom templates, they cannot take precedence over the Prisma Access-created
   templates.

   You allocate remote network and mobile user license
   resources for each tenant based on the license that is associated
   with the Cloud Services plugin in Panorama.

   The following
   figure shows a sample Prisma Access deployment using a license with
   a 20,000 Mbps remote network bandwidth pool and 20,000 mobile users.
   The administrator allocated 5,000 Mbps in remote network bandwidth
   and 5,000 mobile users for the existing configuration. After the
   administrator enabled multitenancy, the license allocation migrated
   along with all other configuration to the first tenant. The administrator
   then created additional tenants, each with a 5,000 Mbps bandwidth
   pool for remote networks and 5,000 mobile users for each tenant.
   Prisma Access allocates the license resources from the overall license
   allocation. After you complete this configuration, there is 5,000
   Mbps of remote network bandwidth and 5,000 mobile users available
   in the license.

   ![]()

---

<a id="pa-plan-your-multitenant-deployment"></a>

### Plan Your Multitenant Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/plan-your-multitenant-deployment>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

Before you enable multitenancy, migrate the first tenant, and
create additional tenants, make sure that you have all required
information and resources to do so by completing the following tasks:

- If you are migrating an existing
  single-tenant deployment [to a multitenant deployment](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/enable-multitenancy-and-migrate-the-first-tenant.html#id66bc0a6a-4f45-4954-b771-0280c192cac7),
  make a note of the following Prisma Access features that are not
  supported. See the [Palo Alto Networks Compatibility
  Matrix](https://docs.paloaltonetworks.com/compatibility-matrix/reference/prisma-access?otp=id31c499de-881a-4e34-ba50-458e1d1f0ff9) for the list of unsupported features.
- If don’t have an existing Prisma Access configuration, you Enable
  Multitenancy and add your tenants; then, then configure
  the tenants after you create them. See [Create an All-New Multitenant Deployment](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-an-all-new-multitenant-deployment.html#id91d84f7f-fc85-4553-a0cc-b784efcfefd6) for more
  information.
- Make a note of your license allocation for remote networks
  and mobile users.

  Open your license (PanoramaLicenses) and find the Prisma
  Access Total Mbps (remote networks bandwidth
  pool) for remote networks and User Limit (total
  number of licensed users) for mobile users.

  When you create
  tenants, you assign resources for remote networks and mobile users
  from this license allocation. If you run out of the minimum required licensed
  Mbps for remote networks or mobile users, you cannot create additional
  tenants.

  You should also make a note of the bandwidth
  and mobile users allocation for your existing configuration. After
  you migrate your configuration to the first tenant, check these
  values to verify that the first tenant migrated correctly.
- Make a list of the names you will use to identify each tenant.

  When you create tenant names, avoid using names
  like [Tenant-1](#), [Tenant-2](#), [Tenant-3](#), and
  so on. The system logs reserve a small number of characters for
  the tenant name in the log output and, if tenants have similar names,
  it can be difficult to associate the tenant with the logs. We recommend
  using a unique and short name for tenants (for example, [Acme](#) or [Hooli](#)).
- Make a list of the administrative users you will create and
  assign for each tenant, and note the maximum number of administrative
  users that can be logged in concurrently.

  When administrative
  users are performing normal multitenant operations such as configuration
  changes and commit operations, we recommend having a maximum of
  12 administrative users logged in to Panorama concurrently.

  An
  administrative user who can manage multiple tenants can provision
  up to 200 tenants at the same time with a single commit operation.
- Be sure that you have sufficient license resources to enable
  multiple tenants.

  The minimum license allocation for each
  tenant is 200 Mbps for each remote network or 200 mobile users.
  You can also create a tenant with only remote networks or mobile
  users, and can configure tenants in differing configurations on
  the same Panorama. For example, you could create a tenant with remote
  networks only, a tenant with mobile users only, or a tenant with
  both mobile users and remote networks, as long as each tenant meets
  the minimum license allocation and the relevant licenses are activated
  and associated with the Panorama where you configure the tenants.
- When configuring a tenant in multitenancy mode, create a
  unique name for each IPSec tunnel and IKE gateway for service connections
  and remote network connections, and try to use a name that will
  not be duplicated by another tenant. While there is no effect to
  functionality, you cannot delete an IPSec tunnel or IKE gateway
  if another tenant is using a tunnel or gateway with the same name.

  This caveat applies to all objects, including QoS profiles (you cannot delete
  objects with duplicate names in a multi-tenant deployment if one of the objects
  is being referenced by another tenant).
- Single-tenant users cannot view system logs; only superusers
  can. You can, however, [sort logs by tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/sort-logs-by-device-group-id-for-external-logging.html#id92db6d70-62b1-4bc3-b394-769bee1aa2c9).
- When a mobile user logs into a single Prisma Access tenant, the user consumes one
  license unit. If a user logs into additional tenants under a single multitenant
  deployment, the user consumes one license unit for each tenant they are logged
  in. For example, if a single user is logged into five tenants, the user consumes
  five mobile user license units in total.
- When using the multitenancy feature and logged in as a tenant-level administrative
  user, opening the Panorama Task Manager (clicking Tasks at
  the bottom of the Panorama web interface) shows all tasks for all
  tenants, including any tasks done at the superuser (Admin) level.
- Some Prisma Access features are not supported for use with
  multitenancy. See [Multitenancy Unsupported Features](https://docs.paloaltonetworks.com/compatibility-matrix/reference/prisma-access?otp=id31c499de-881a-4e34-ba50-458e1d1f0ff9) in
  the [Palo Alto Networks Compatibility
  Matrix](https://docs.paloaltonetworks.com/compatibility-matrix/reference/prisma-access) for details.
- If you [back up](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations.html) a Panorama configuration,
  then [revert](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/revert-panorama-configuration-changes.html) it to an earlier
  saved configuration, Panorama cannot revert to the configuration
  you saved if you perform the following actions in the following
  order:

  1. Backup a Panorama configuration.
  2. Delete a tenant.
  3. Restore the configuration.

  If you delete
  a tenant, you cannot use any of the previous backups you saved before
  you deleted the tenant. However, you can use any backups you make
  after you delete the tenant.

---

<a id="pa-create-an-all-new-multitenant-deployment"></a>

### Create an All-New Multitenant Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-an-all-new-multitenant-deployment>*

How to create a multitenant and don’t have an existing
Prisma Access configuration, follow these rules.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

If you want to create a multitenant deployment
and don’t have an existing Prisma Access configuration, you can Enable
Multitenancy and add your tenants; then configure the
tenants after you create them.

If you have an existing single-tenant deployment and want
to migrate to a multitenant deployment, use the workflow to [enable multitenancy
and migrate the first tenant](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/enable-multitenancy-and-migrate-the-first-tenant.html#id66bc0a6a-4f45-4954-b771-0280c192cac7).

When you create the first tenant with no existing configuration,
make sure of the following differences and guidelines to follow:

- Since there is no configuration to move over, Prisma Access creates templates, template stacks,
  and device groups for each tenant and associates them to the access domain you
  create during tenant creation. See [Multitenancy Configuration Overview](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/multitenancy-configuration-overview.html) for the naming convention that Prisma Access uses.
- Optionally, after you create the tenant-level access domain,
  you could [create an administrative
  user](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant.html#id22568b02-14b3-4c80-9dcd-192f224c1d09) that allows administration for a single tenant by associating
  an administrator with the access domain.
- If you have any existing templates or device groups (for
  example, templates from an on-premises device that is managed by
  Panorama that should also be used by Prisma Access), be sure to
  add those device groups and templates domains to the Access
  Domain when you create and configure it. If you do not
  add device groups and templates to the access domain, you cannot
  view or select them when you configure the Prisma Access components
  in the Cloud Services plugin.

---

<a id="pa-enable-multitenancy-and-migrate-the-first-tenant"></a>

### Enable Multitenancy and Migrate the First Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/enable-multitenancy-and-migrate-the-first-tenant>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

Use the following workflow to enable multitenancy and migrate your existing configuration to the
first tenant you create. If you don’t have any existing configuration, you can
enable multitenancy and add your tenants; then configure them.

When you enable multitenancy,
Prisma Access migrates the following components of your configuration:

- All service connection and remote network tunnel onboarding information,
  including tunnel configuration.
- Existing mobile users onboarding information.
- Strata Logging Service information.
- Existing [Autonomous DEM (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem.html) configuration
- The templates, template stacks, and device groups for service connections,
  remote networks, and mobile users.

You need to specify the number of users (for a mobile user deployment), bandwidth (for a remote
networks deployment), and [Autonomous DEM (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem/get-started-with-adem) to allocate for each
deployment (if you have purchased an ADEM license).

Because
of these device group changes, you create an [access domain](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/access-domains) and add
the migrated device groups, templates, and template stacks, as shown
in the following workflow.

If you don’t have an existing
Prisma Access configuration, and you are creating an all-new multitenant
deployment, do not use this workflow; instead, complete the steps
in [Add Tenants to Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access.html#id34997992-9769-4fc2-9304-93f7d0352394) to create the
first tenant.

1. Determine the number of licensed units you want to allocate to this
   deployment.

   While Prisma Access migrates your configuration to the first tenant, you need
   to specify:

   - The Bandwidth to allocate for the tenant’s
     remote users deployment (if applicable).
   - The Users to allocate for the tenant’s mobile
     users deployment (if applicable).
   - The number of ADEM units to allocate for mobile uses and remote
     networks (if applicable).
2. Select PanoramaCloud ServicesConfiguration.
3. Select Enable Multitenancy (located
   on the upper right of the page).

   ![]()

   After you enable multitenancy, Panorama displays a notification informing you that the existing
   Prisma Access configuration move to the first tenant.

   After you enable
   multitenancy, your deployment permanently changes to a multitenant
   deployment, and you cannot revert to single tenant mode.
4. Click OK to migrate the existing
   configuration to the first tenant.

   The Tenants page displays, and pie
   charts in the center of the window display.

   - If you
     have a remote networks or mobile users license, the available amount
     of licensed remote network bandwidth and mobile users display.
   - (Remote Networks and Mobile User Deployments Only)
     If you have purchased an Autonomous DEM license, the available number
     of units for ADEM uses displays.
   - If you have a Clean Pipe deployment, the amount of bandwidth
     for the tenant displays.
5. Choose the type of deployment you want to use for the tenant.

   - For a remote network, mobile user deployment, or
     to configure both deployment types for a tenant, select Remote Networks/Mobile
     Users.
   - For a clean pipe deployment, select Clean Pipe.

     This
     section only describes how to configure tenants for remote network, mobile
     user, or both remote network and mobile user deployment types. To configure
     the clean pipe service, see [Prisma Access for Clean Pipe](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/clean-pipe.html#id7bd96d66-212b-49e0-861b-628d676d88d3).
6. Migrate the existing configuration to the first tenant.

   The first migrated sub-tenant's name is auto-populated from the tenant you
   are migrating and cannot be edited.

   1. Create a new Access Domain by clicking
      the down arrow selecting New Access Domain.
   2. Enter a Name for the access
      domain and click OK.

      Prisma Access adds the Mobile\_User\_Device\_Group, Remote\_Network\_Device\_Group,
      and Service\_Conn\_Device\_Group Device Groups to
      the new access domain.

      Do not associate the default Device Groups and Templates to other
      sub-tenants other than the first migrated sub-tenant.

      ![]()
   3. (Optional) Click Templates to
      verify that Prisma Access added the following templates and template stacks:

      - Explicit\_Proxy\_Template
      - Explicit\_Proxy\_Template\_Stack
      - Mobile\_User\_Template
      - Mobile\_User\_Template\_Stack
      - Remote\_Network\_Template
      - Remote\_Network\_Template\_Stack
      - Service\_Conn\_Template
      - Service\_Conn\_Template\_Stack

        These
        are the default template stacks and templates for a standard Prisma
        Access deployment; if you added other templates, be sure that Prisma Access
        added them.

      ![]()
   4. (Optional) If you have other templates associated with
      this configuration, select them.
   5. Click OK to close the Access
      Domain page and return to the Tenants page.
7. Enter the values in Bandwidth (Mbps) for remote
   networks, Users for mobile users, and the number of
   Autonomous DEM Users you want to allocate for each
   deployment type.

   Use the following guidelines when allocating ADEM units for a tenant:

   - The number of ADEM units you can allocate for mobile users and remote
     networks can be only equal to or less than base license.
   - The minimum number of units you can allocate is 200.
   - After you allocate the ADEM units for a tenant, you can edit or
     remove those units.
   - If you did not purchase an ADEM license for your deployment type
     (Mobile Users or Remote Networks), that choice is grayed out.

   ![]()
8. Click OK.

   The PanoramaCloud
   ServicesConfiguration page
   shows the first tenant successfully migrated, and a Tenants drop-down
   is added above the Tenants area.

   ![]()
9. Make sure that all the templates and device groups were populated to the
   tenant.
   1. Select the tenant from the drop-down list.
   2. Go to PanoramaCloud ServicesConfiguration.
   3. Select Service Setup.
   4. Click the gear to edit the Settings.
   5. Make sure that the correct template stack, template, and device group
      (Service\_Conn\_Template\_Stack, Service\_Conn\_Template, and
      Service\_Conn\_Device\_Group, respectively) were populated to the
      settings.
   6. Go to oither tabs for which you have existing configuration (for
      example, Mobile Users—GlobalProtect,
      Mobile Users—Explicit Proxy,
      Remote Networks, or Service
      Connection), click the gear to edit the
      Settings, and make sure that the correct
      template stack, template, and device group were populated to the
      settings.
10. Commit your changes locally to Panorama (CommitCommit to Panorama.
11. Select CommitCommit to Panoramato save your changes locally on the Panorama that manages Prisma
    Access.

    If you do not perform a local commit, Prisma Access components do not display
    in the Push Scope when you Commit and Push your changes.
12. Commit and push your changes to make them active in Prisma Access.
    1. Select CommitCommit and Push and Edit
       Selections in the Push Scope.
    2. Select Prisma Access, then
       select the tenant you created, Service Setup, Remote Networks,
       and Mobile Users.

       ![]()
    3. Click OK to save your changes
       to the Push Scope.
    4. Commit and Push your
       changes.
13. Select PanoramaCloud ServicesStatus.

    The status page shows the status of all tenants. Because you have created only one tenant, that
    tenant is the only one that displays. If you select that tenant from the
    drop-down, you show a detailed status of that tenant.

    ![]()

    Selecting a tenant from the drop-down returns you to the Status page for that tenant.
14. Continue to [add more tenants](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access.html#id34997992-9769-4fc2-9304-93f7d0352394) to
    Prisma Access.

---

<a id="pa-add-tenants-to-prisma-access"></a>

### Add Tenants to Prisma Access

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

After you migrate the existing information as
a first tenant, you can create and configure additional tenants.
For each tenant you create after the first, Prisma Access creates
a separate access domain with its own set of template stacks and templates
and its own domain groups.

Use this workflow to add more tenants
to Prisma Access.

If you are creating an all-new multitenant
deployment, use this workflow to add the first tenant, as well as
additional tenants. See [Create an All-New Multitenant Deployment](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-an-all-new-multitenant-deployment.html#id91d84f7f-fc85-4553-a0cc-b784efcfefd6) for more
information.

1. Log in to Panorama as a superuser.
2. Add and configure the tenant.
   1. Select PanoramaCloud ServicesConfiguration, then Add a new tenant.

      Be sure that you select Remote Networks/Mobile
      Users; to create and configure a Clean Pipe
      deployment, see [Prisma Access for Clean Pipe](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/clean-pipe.html#id7bd96d66-212b-49e0-861b-628d676d88d3).
   2. Specify a descriptive Name for the tenant.
   3. Add a new Access Domain,
      give it a descriptive Name, and click
      OK to return to the
      Tenants window.

      After you click OK, Prisma Access
      automatically creates templates, template stacks, and device groups
      and associates them to the access domain you create.
3. Specify the amount of Bandwidth (Mbps) to allocate for
   the Remote Networks and the number of
   Users to allocate for the Mobile
   Users.
4. (Deployments with Autonomous DEM Only) If you have purchased an [Autonomous DEM (ADEM)](https://docs.paloaltonetworks.com/autonomous-dem/get-started-with-adem) license, select
   the number of units to allocate for ADEM.

   Use the following guidelines when allocating ADEM units for a tenant:

   - The number of ADEM units you can allocate for mobile users and remote
     networks can be only equal to or less than base license.
   - The minimum number of units you can allocate is 200.
   - After you allocate the ADEM units for a tenant, you can edit or
     remove those units.
   - If you did not purchase an ADEM license for your deployment type
     (Mobile Users or Remote Networks), that choice is grayed out.

   ![]()
5. Click OK to create the first tenant.
6. Make sure that Prisma Access applied the template stack, template, and device
   group service settings to the service connection settings of the tenant you just
   created.
   1. Select the tenant you created from the Tenant
      drop-down.

      ![]()
   2. Select PanoramaCloud ServicesConfigurationService Setup.
   3. Click the gear icon to the right of the Settings
      area to edit the settings.
   4. Make sure that Prisma Access has associated the template stack
      (sc-stk-tenant), template
      (sc-tpl-tenant), and
      device group (sc-dg-tenant) to
      your service connection settings.
   5. Make sure that the Parent Device Group is set to
      Shared and click OK.

      ![]()
7. Make sure that Prisma Access applied the template stack, template, and device
   group to the remote network settings.
   1. Select PanoramaCloud ServicesConfigurationRemote Networks and click the gear icon to the right of the
      Settings area to edit the settings.
   2. Make sure that the Prisma Access has associated the template stack
      (rn-stk-tenant), template
      (rn-tpl-tenant), and
      device group (rn-dg-tenant) to
      your remote network settings.
   3. Make sure that the Parent Device Group is set to
      Shared and click
      OK.

      ![]()
8. Make sure that Prisma Access applied the template stack, template, and device
   group to the mobile user settings.
   1. Select PanoramaCloud ServicesConfigurationMobile Users and click the gear icon to the right of the
      Settings area to edit the settings.
   2. Make sure that the Prisma Access has associated the template stack
      (mu-stk-tenant), template
      (mu-tpl-tenant), and
      device group (mu-dg-tenant) to
      your remote network settings.
   3. Make sure that the Parent Device Group is set to
      Shared and click
      OK.

      ![]()
9. Commit your changes locally to Panorama (CommitCommit to Panorama.
10. (Mobile User deployments only)—Add an infrastructure subnet, then
    commit and push your changes to make them active in Prisma Access.

    These steps are required for the mobile user changes to take effect.

    1. Select PanoramaCloud ServicesConfigurationService Setup, click the gear icon to edit the Settings, and configure
       an [infrastructure
       subnet](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-setup/configure-the-prisma-access-service-infrastructure/prisma-access-service-infrastructure-panorama.html#id174DBE00YY4).
    2. Select CommitCommit and Push, Edit Selections in the Push
       Scope, and make sure that Mobile Users is
       selected.
    3. Click OK to save your changes to the Push
       Scope.
    4. Commit and Push your
       changes.
11. Select the new tenant you created by selecting PanoramaCloud ServicesConfigurationtenant-name and continue the configuration of your tenant.
    1. [Configure the Service Infrastructure](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-setup.html).
    2. [Create a Service
       Connection to Allow Access to Private Apps.](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-service-connections.html#id796b2831-1122-4932-9a3d-5211142321d5).
    3. [Onboard and Configure
       Remote Networks](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-remote-networks.html#id4f074dec-9248-4ea6-b9da-3bb815151aee) if you are licensed for remote
       networks.
    4. [Set Up Global Protect for](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/set-up-globalprotect-mobile-users/set-up-globalprotect-mobile-users-panorama.html#id3f9ae0c3-ba79-4001-9ddf-c72e3d03092f) if you are licensed for remote
       users.

       ![]()

---

<a id="pa-delete-a-tenant"></a>

### Delete a Tenant

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/delete-a-tenant>*

Delete a tenant in a Prisma Access (Managed by Panorama) deployment.

Delete a tenant in a Prisma Access (Managed by Panorama) deployment by completing the following
steps.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in   Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

- While you can delete all tenants in a multitenant deployment, you cannot
  delete the admin-level Prisma Access configuration where you add or
  delete tenants.
- When you delete a tenant, Prisma Access deletes the template and device
  group set for which you are licensed, but does not delete the unlicensed
  set. For example, if you have a Prisma Access for Users license and
  delete a tenant, Prisma Access deletes the mobile user-related template
  stacks, templates, and device groups but does not delete the set it
  created for the unlicensed Prisma Access for Networks. You can manually
  delete these unused template and device group sets after you delete the
  tenant.

1. From the Panorama that manages Prisma Access, select PanoramaCloud ServicesConfiguration.
2. Select the tenant, and delete all configuration
   associated with it.

   Perform this step as a best practice to make sure that all configuration is deleted from the
   tenant, including any Service Connection, Mobile User, Remote Network, or
   Clean Pipe configuration.
3. Commit and Push your changes to Prisma Access.
   1. Select CommitPush to Devices.
   2. Edit Selections, and make sure
      that all the components you deleted (including Remote Networks,
      Mobile Users, Service Setup, Explicit Proxy, and Clean Pipe, depending
      on your deployment) are selected.

      ![]()
   3. Click Push.
4. Select one or more tenants and then Delete them.

   Deleting a tenant removes the tenant from Panorama but does not remove the
   tenant from the Prisma Access infrastructure. To delete a tenant and remove
   it from the infrastructure, you delete it, perform a local commit, and then
   deprovision it as shown in the following steps.

   If you delete the tenant but do not deprovision it, you can still retrieve
   it by contacting Palo Alto Networks support.

   If you have your Panoramas set up in an HA configuration, only perform
   the delete and deprovision operations from the Active Panorama in an HA
   pair.

   ![]()

   A pop-up window displays, confirming the tenant deletion process. Click
   Yes to continue, or click
   No to cancel the deletion.

   ![]()
5. Commit your changes locally to Panorama by selecting CommitCommit to Panorama and Commit your changes.

   After the local commit, the tenants are marked for deletion and are removed
   from the list of tenants, but are not deleted from the Prisma Access
   infrastructure. A pop-up displays showing the tenants that are deleted. 

   ![]()
6. (Optional) To completely remove the tenants from the Prisma Access
   infrastructure, Deprovision Deleted Tenants.

   Deprovisioning a tenant:

   - Removes it from your configuration and the Prisma Access infrastructure,
     and you cannot retrieve it.
   - Regains the license that was allocated to the tenant.

   ![]()

   A confirmation message displays with the names of the tenants that would be
   deprovisioned; click OK to continue the
   deprovisioning of the tenant, or Cancel the
   operation.

   When you deprovision a tenant, you completely delete the tenant and all
   resources that are allocated with it, and you regain the licenses that were
   allocated to these tenants. The tenant cannot be retrieved.

   ![]()

   If no tenants need to be deprovisioned, the following message displays.

   ![]()
7. (Optional) Check the status of the deprovisioning operation by going
   to MonitorLogsSystem. The deprovisioning operation and the name of the tenant is
   displayed in the logs.

   ![]()

---

<a id="pa-create-a-tenant-level-administrative-user"></a>

### Create a Tenant-Level Administrative User

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

You should create an administrative user for
each tenant. In that way, a tenant-level administrator can view
and make changes to their tenant configuration but doesn’t have
access to other tenants. To create an administrative user for a specific
tenant, complete the following task. For more information about
role-based access control (RBAC) for tenant-level administrative
users, see [Control Role-Based Access for Tenant-Level Administrative Users](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/control-role-based-access-for-tenant-level-administrative-users.html#id4f2ddb30-2222-4df3-9d65-9de4c6ac3050).

Users
who manage single tenants cannot see the system logs because the MonitorLogsSystem choice
is not available. This limitation applies to all Administrators
who have an administrative role of Device Group and Template.
Only superusers can view system logs in multitenancy mode.

1. Create
   an [administrative role](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) with
   a type of Device Group and Template.
   1. Select PanoramaAdmin Roles.
   2. Add an Admin Role Profile with
      a Role of Device Group and Template.
   3. Click OK.

      You can create a single Admin Role Profile and share it
      across multiple tenants; however, you must create a separate administrator
      for each tenant.

      While you tailor the administrative
      role for the needs of your organization, we recommend deselecting Commit
      for Other Admins. Deselecting this choice allows a tenant-level
      user to commit only the changes they have made, and prevents them
      from unintentionally committing other changes that other tenant-level
      administrative users have made that are not yet committed.

      ![]()
2. Create
   and configure an [Administrator](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) for the tenant.
   1. Select PanoramaAdministrators.
   2. Add an Administrator.
   3. Enter and confirm a Password for
      the new Administrator.
   4. Specify an Administrator Type of Device
      Group and Template Admin.
   5. Specify the Access Domain that
      is associated with the device groups for that tenant.
   6. Specify the Admin Role that
      you created in Step [1](#pa-create-a-tenant-level-administrative-user) for the tenant.

      ![]()
3. Click OK.
4. Repeat Steps [2](#pa-create-a-tenant-level-administrative-user) and [3](#pa-create-a-tenant-level-administrative-user) to add additional
   users to manage your tenants as required.
5. Select CommitCommit to Panorama and Commit your changes.

---

<a id="pa-control-role-based-access-for-tenant-level-administrative-users"></a>

### Control Role-Based Access for Tenant-Level Administrative Users

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/control-role-based-access-for-tenant-level-administrative-users>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

If you manage a multitenant deployment, you
can use role-based access control (RBAC) to [create tenant-level
administrative users](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant.html#id22568b02-14b3-4c80-9dcd-192f224c1d09).

To modify RBAC-level access for
tenant-level administrative users in Panorama, you [create a tenant-level
administrative user](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant.html#id22568b02-14b3-4c80-9dcd-192f224c1d09), use an [Admin Role Profile](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/set-up-panorama/set-up-administrative-access-to-panorama/configure-an-admin-role-profile) with
a Role of Device Group and Template,
and Enable, Disable,
or give Read Only access to areas of the
Panorama Web UI. Use this method to manage
access to all Panorama components for tenant-level users, with the
exception of access to the Cloud Services plugin where you manage
Prisma Access.

If you want to restrict a tenant-level user
from configuring the Prisma Access components in Panorama, you cannot
use Admin Roles. To disallow users from configuring Prisma Access-specific
configuration tasks, you must prevent the user from accessing the
Cloud Services plugin, which also prevents them from viewing it. Using
this method, you can create an administrative user for a security
professional who has permissions to make changes to security policies
and push those changes to Panorama, but cannot view or make any
changes to Prisma Access configuration.

You can either
enable or disable access to the Cloud Services plugin for a user,
but you cannot give a user read-only access; if a user has access to
view the Cloud Services plugin, the user can also make configuration
changes to its components, including Prisma Access.

The
following table shows sample tenant-level administrative roles and
the steps you perform to create those roles.

|

Sample Tenant-Level Configuration | Configuration Task |

| --- | --- |

|  |  |
| --- | --- |
|

Create a networking-focused user who:  - Can   edit plugin configurations - Can commit to Panorama - Can push configuration to Prisma Access | [Create a tenant-level administrative user](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/create-administrative-users-for-a-single-tenant.html#id22568b02-14b3-4c80-9dcd-192f224c1d09), enabling Save and Commit permissions in the Admin Role Profile, and disabling or making Read Only any permissions that you don’t want the tenant-level administrative user to have. |

|

Create a security-focused user who:  - Can   view and make changes to security policies  - Can   commit to Panorama - Cannot view, or make changes to, the Cloud Services plugin - Cannot push configuration to Prisma Access (requires the superuser   to push the configuration) | To prevent a tenant-level administrative user from viewing or accessing the plugin, remove plugin access for a tenant-level administrator. For all other Panorama-related permissions, change the Admin Role permissions for the user. |

|

Create a hybrid user who:  - Has read-only access   to the Cloud Services plugin - Has read-write access to the security policy - Cannot push the configuration to Prisma Access (requires the   superuser to push the configuration) | This configuration is not possible. You cannot make the Cloud Services plugin read-only. You can only provide access to admin users to view it and use it to make configuration changes, or disallow them from viewing it. |

---

<a id="pa-remove-plugin-access-for-a-tenant-level-administrative-user"></a>

#### Remove Plugin Access for a Tenant-Level Administrative User

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/control-role-based-access-for-tenant-level-administrative-users/remove-plugin-access-for-a-tenant-level-administrative-user>*

Learn how to remove plugin access for a tenant-level administrative user.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma   SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)   license |

In normal multitenant configurations, you use
access domains [Add Tenants to Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access.html#id34997992-9769-4fc2-9304-93f7d0352394) and associate
each access domain with a tenant. To prevent a tenant-level administrative
user from viewing or making configuration changes to Prisma Access,
you create an access domain, but you do not associate it with a
tenant.

Because you associated the access domain to the device
groups and template stacks for the tenant, the tenant-level administrative
user has RBAC access at the tenant level and is able to perform
configuration for that tenant only. Because you did not associate
the access domain with a tenant in Prisma Access, the access domain
is unable to view the Cloud Services plugin, which provides access
to Prisma Access. In this way, you create a user who can perform
tenant-level configuration tasks without being able to access, view,
or make configuration changes to Prisma Access.

To remove
Prisma Access for an administrative-level user, complete
the following task.

This task assumes that you have [Add Tenants to Prisma Access](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/add-tenants-to-prisma-access.html#id34997992-9769-4fc2-9304-93f7d0352394) templates,
template stacks, and device groups for the tenant; you’ll be associating
them to the tenant-level administrative user.

1. Create
   an [administrative role](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) with
   a type of Device Group and Template.
   1. Select PanoramaAdmin Roles.
   2. Add an Admin Role Profile with
      a Role of Device Group and Template.
   3. Click OK.

      You can create a single Admin Role Profile and share it
      across multiple tenants.

      ![]()
2. Select PanoramaAccess Domain and Add an [Access Domain](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/access-domains).
3. Specify the Device Groups and Templates associated
   with the tenant.

   If you created any device groups that are children
   or grandchildren of other device groups under the Shared parent
   device group, select only the device group at the lowest hierarchical
   level (child or grandchild); do not select the parent or you will
   have errors on commit.

   ![]()

   ![]()
4. Create
   and configure an [Administrator](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) for the tenant-level
   administrative user, specifying the Access Domain you just created.
   1. Select PanoramaAdministrators.
   2. Add an Administrator.
   3. Enter and confirm a Password for
      the new Administrator.
   4. Specify an Administrator Type of Device
      Group and Template Admin.
   5. Specify the Access Domain that
      is associated with the device groups for that tenant.
   6. Specify the Admin Role that
      you created in Step [1](#pa-remove-plugin-access-for-a-tenant-level-administrative-user) for the tenant.

      When you complete this example, the abcd-tenant-no-plugin-access Administrative
      user will have permissions based on what you defined in the Admin
      Role profile, but will not be able to view or configure the Cloud
      Services plugin (including Prisma Access). Note, however, that they
      will not be able to push any changes that they make to the cloud.

      ![]()
5. Select CommitCommit to Panorama and Commit your changes.

---

<a id="pa-sort-logs-by-device-group-id-in-a-multitenant-deployment"></a>

### Sort Logs by Device Group ID in a Multitenant Deployment

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access/sort-logs-by-device-group-id-for-external-logging>*

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access (Managed by Panorama) - For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager), see [Prisma SASE](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/get-started). | - [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license) license |

To sort the logs manually by tenant in Panorama,
select MonitorLogs and
choose the Device Group associated with that
tenant to display the logs for that device group. However, if you are
forwarding your logs to an external device, you might have a need
to sort those logs at the tenant level. To do so, find the device
group ID in the logs that is associated with the device group and
use that group ID-to-device group mapping to associate the logs
with a tenant.

There are four fields associated with the device
group in the logs: DG Hierarchy Level 1, DG
Hierarchy Level 2, DG Hierarchy Level 3,
and DG Hierarchy Level 4. These fields show
the device group IDs in its hierarchy. The shared device group (level
0) is not included in this structure.

DG Hierarchy
Level 1 refers to the first device group level in the
hierarchy. If you added children or grandchildren device groups,
the DG Hierarchy Level 2 through DG
Hierarchy Level 4 fields show the hierarchy from the
child group to the great-grandchild group, respectively.

To find
logs by tenant, complete the following task.

1. Find
   the device group IDs associated with the device group.

   - To find this information using a CLI command, log
     into Panorama as a superuser (admin-level user), enter the show readonly command
     in configuration mode, and view the values in the device-group heading.
     The IDs for the device groups display under the device group name.
     The following example shows that the device ID for the acme-sc device
     group is 20.

     Note that these device
     groups are at the first level in the hierarchy (DG Hierarchy
     Level 1); you use that information in the query in the
     next step.

     ```
     admin# show readonly
     ...
       device-group {
             acme-sc {
               id 20;
             }
             acme-rn {
               id 39;
             }
             acme-mu {
               id 40;
             }
             hooli-rn {
               id 56;
             }
             hooli-sc {
               id 57;
             }
             hooli-mu {
     ```
   - To use an API query, enter the following API command:

     ```
     /api/?type=op&cmd=<show><dg-hierarchy></dg-hierarchy></show>
     ```

   For
   more information about using APIs with logs, see [Retrieve Logs (API)](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-panorama-api/pan-os-xml-api-request-types/retrieve-logs-api.html).
2. Use the device group ID-to-device group name mapping
   to associate the logs with a tenant.
3. Add the Forwarding parameters
   that select the logs you want to forward.

---

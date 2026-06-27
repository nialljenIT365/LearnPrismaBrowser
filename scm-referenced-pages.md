# Strata Cloud Manager — Referenced Pages

> Pulled from https://docs.paloaltonetworks.com on 2026-06-27. Images/links are absolute URLs.

---

## Log Viewer: Strata Cloud Manager

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/incidents-and-alerts/log-viewer>*

View the log records that your devices have collected and stored in Strata Logging Service.

|

Where Can I Use This? | What Do I Need? |

| --- | --- |

|  |  |
| --- | --- |
|

- Prisma Access  *(with Strata Cloud Manager or Panorama   configuration management)* - NGFW, including those funded by [Software NGFW   Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw) | - Each of these licenses include access to Strata Cloud Manager:    - Prisma Access   - AIOps for NGFW Premium license (use the Strata Cloud Manager app) or AIOps for NGFW Free (use the AIOps for NGFW Free app)   - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)   - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support) - A [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) that has   permission to view the dashboard |

Log Viewer provides the capabilities of [Explore](https://docs.paloaltonetworks.com/strata-logging-service/administration/view-logs/retrieve-logs) — where you can view and interact
with your logs stored in Strata Logging Service.

Log Viewer provides an audit trail for system, configuration, and network
events. Jump from a dashboard to your logs to get details and investigate findings.
A query field and time range preferences help you narrow down the specific logs that
are of interest to you.

- [Learn more about how to build your
  queries](https://docs.paloaltonetworks.com/strata-logging-service/administration/view-logs/retrieve-logs/about-queries)
- Discover new Log Viewer features in the  [Strata Logging Servicerelease
  notes](https://docs.paloaltonetworks.com/strata-logging-service/release-notes/new-features).

Log Viewer highlights actions and severity of the logs to help you
understand how sessions are enforced. You can also view the details of the security
artifacts of the logs in [Search](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/insights-scm/search.html) page.

![]()

Select the log type you want to view. For details on the log types and definition of each of
their log fields, see the [Log Reference](https://docs.paloaltonetworks.com/strata-logging-service/log-reference/log-forwarding-schema-overview) guide.

---

## Configuration: ZTNA Connectors

*Source: <https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-cloud-manager/getting-started/insights-scm/monitor-data-centers/monitor-data-centers-ztna-connectors>*

View and monitor ZTNA Connectors to see the status and performance of your ZTNA
connectors and connector groups.

Zero Trust Network Access (ZTNA) Connector simplifies private application access for all
your applications. The ZTNA Connector VM in your environment automatically forms tunnels
between your private applications and Prisma Access. View a summary of all
configured ZTNA connectors, including the Application Targets
associated with the connector, its average and median bandwidth, and the
Status (Up, Partially Up, or Down). Select in Strata Cloud Manager to see how your ZTNA connectors and connector
groups are performing.

![]()

## Total Connector Groups

Select the Total Connector Groups to get the details about the
Connector Groups and the associated Connectors. You can filter the information
using:

- **Time Range**: Select and available range or use a custom range.
- **PA Location**: Select the location as per your requirement.
- **Connector Group**: List of available Connector Groups.
- **Status**: Select either **Up**, **Down** or **Partially
  Up**.

  ![]()

- If all Connectors in a Connector
  Group are up, the Status is
  Up (green).
- If all the Connectors are down, the status is
  Down (red).
- If some Connectors are up and some are down, the
  Status is Partially Up
  (orange).
- Disabled Connectors appear as gray.

On the right-side of the screen, you get the details such as **Group Name**,
**Connector Status**, **Targets** for the Connector Group.

![]()

Select Connector Status and then
Action, to get the Device Metrics
(Memory, CPU, Bandwidth, and Connector Availability).

![]()

Select Target to get the following details such as
**Target**, **Status**, **FQDN/IP Subnet**, and **Enabled**.

## Total Wildcards

**Wildcards**—For wildcard-based apps, create an FQDN-based Connector Group, and
then, specify the wildcard to use (for example, \*.example.com) for the app target.
When users access sites that match the wildcard, those apps are automatically
onboarded for access from ZTNA Connector for your mobile users and remote network
users.

Total Wildcards summarizes how many Wildcard rules you have onboarded. [This is the number of wildcard rules that you
created](https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/configure-a-ztna-connector), which is a different total than the number of apps discovered as
a result of creating these rules. Select the number next to Total
Wildcards to get the following details such as **Wildcard**,
**Connector Group**, **Targets**, and **Enabled**. 

![]()

Select Action to
get the bandwidth.

![]()

## Target

**FQDNs**—Prisma Access resolves the FQDNs of the applications you onboard to
ZTNA Connector to the IP addresses in the Application IP address block.

**IP Subnets**—Create an IP subnet-based Connector Group, and then enter the IP
subnet to use for the app target.

Select the number to view the total number of FQDNs and get
the details such as **Target**, **Status**, **FQDN**, **Connector
Group**, and **Enabled**.

![]()

Select Action to get the bandwidth.

![]()

Select the number to view the total number of IP Subnet and
get the details such as **Target**, **Status**, **IP Subnet**,
**Connector Group**, and **Enabled**.

![]()

---

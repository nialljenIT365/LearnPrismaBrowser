**DEPLOYMENT**
**GUIDE**

# Securing Internet and Private Applications by Using Prisma Browser and Prisma Access

#### **JUNE 2026**


_Table of Contents_

## Table of Contents


Preface......................................................................................................................................................................................................... 3

Purpose of This Guide................................................................................................................................................................................5

Objectives............................................................................................................................................................................................ 5

Audience..............................................................................................................................................................................................5

Related Documentation........................................................................................................................................................................6

Design Model...............................................................................................................................................................................................8

Assumptions and Prerequisites................................................................................................................................................................11

Validation Environment.......................................................................................................................................................................11

Deployment Details................................................................................................................................................................................... 13

Activating Prisma Browser and Managing Group Membership..........................................................................................................13

Creating Prisma Browser Policies......................................................................................................................................................17

Restricting the Usage of Other Browsers.......................................................................................................................................... 30

Forcing Redirect to Prisma Browser by using the Prisma Browser Extension....................................................................................34

Completing Additional Configuration Tasks for Private Application Access........................................................................................ 39

Verifying Prisma Browser Operation.................................................................................................................................................. 52

Feedback....................................................................................................................................................................................................60


_Palo Alto Networks_ _2_


_Preface_

## Preface

### GUIDE TYPES


_Overview guides_ provide high-level introductions to technologies or concepts.


_Design guides_ provide an architectural overview for using Palo Alto Networks® technologies to provide visibility, control, and

protection to applications built in a specific environment. These guides are required reading prior to using their companion

deployment guides.


_Deployment guides_ provide decision criteria for deployment scenarios, as well as procedures for combining Palo Alto

Networks technologies with third-party technologies in an integrated design.


_Solution guides_ provide add-on solutions for post-deployment use cases.

### DOCUMENT CONVENTIONS


Blue text indicates a configuration variable for which you need to substitute the correct value for your environment.


In the IP box, enter 10.5.0.4/24, and then click OK.


Bold text denotes:


       - Command-line commands.


# show device-group branch-offices


       - User-interface elements.


In the Interface Type list, choose Layer 3.


       - Navigational paths.


Navigate to Network > Virtual Routers.


       - A value to be entered.


Enter the password admin.


_Palo Alto Networks_ _3_


_Preface_


_Italic text_ denotes the introduction of important terminology.


An _external dynamic_ list is a file hosted on an external web server so that the firewall can import objects.


Highlighted text denotes emphasis.


Total valid entries: 755

### ABOUT PROCEDURES

These guides sometimes describe other companies’ products. Although steps and screen-shots were up-to-date at the time

of publication, those companies might have since changed their user interface, processes, or requirements.

### GETTING THE LATEST VERSIONS OF GUIDES

We continually update reference architecture guides. You can access the latest version of this and all guides at this location:


[https://www.paloaltonetworks.com/referencearchitectures](https://www.paloaltonetworks.com/referencearchitectures)

### WHAT'S NEW IN THIS RELEASE

This is a new guide.


_Palo Alto Networks_ _4_


_Purpose of This Guide_

## Purpose of This Guide


This guide provides deployment details for using Palo Alto Networks [®] Prisma [®] Browser and Prisma Access in order to

achieve an integrated design. This deployment guide provides you with a framework for securing access to internet and

private applications and providing security and visibility for your workforce.

### OBJECTIVES

Completing the procedures in this guide, you are able to successfully integrate multiple Palo Alto Networks products and

third-party capabilities for securing web access, including the use of SaaS applications. You also enable the following

functionality:


   - Secure access to both internet and private applications


   - Zero Trust access controls


   - Browser-based data loss prevention (DLP) controls


   - Deep, browser-based visibility into end-user actions

### AUDIENCE

This guide is for technical readers, including system architects and security engineers, who want to secure access to internet
based and private applications. It assumes the reader is familiar with the basic concepts of applications, networking, routing,

and security. To be successful, the reader should also have a basic understanding of internet architectures.


_Palo Alto Networks_ _5_


_Purpose of This Guide_

### RELATED DOCUMENTATION

The following is a prerequisite for using this guide:


   - [Securing Internet and Private Applications by Using Prisma Browser and Prisma Access: Design Guide—](https://architectures.link/2075p-prime)

Provides design guidance for securely accessing internet and private applications by integrating Prisma Browser with

Prisma Access. Details browser-native protections, including last-mile controls, Enterprise DLP, and cloud-delivered

security services across managed and unmanaged devices. Covers design decisions for traffic routing using VPN

agents and explicit proxies, along with browser-enforcement strategies such as conditional access and mobile-device

management.


The following are prerequisites for using this guide:


   - [Securing Internet for Mobile Users by Using Tunnel Mode: Deployment Guide—Provides implementation](https://architectures.link/2024p-prime2)

details for using Prisma Access to secure internet access for mobile users. Includes decision criteria for tunnel-mode

deployment scenarios, as well as step-by-step procedures that achieve an integrated design.


   - [Securing Internet for Mobile Users by Using Explicit Proxy: Deployment Guide—Provides implementation](https://architectures.link/2020p-prime2)

details for using Prisma Access to secure internet access for mobile users. Includes decision criteria for explicit proxy

deployment scenarios, as well as step-by-step procedures that achieve an integrated design.


   - [Secure Internet Policy Design: Solution Guide—Provides policy design and deployment guidance for securing](https://architectures.link/2150p-prime)

internet services by using the Prisma Access cloud-delivered security platform and Palo Alto Networks next
generation firewalls.


Before using this guide, you should have completed at least one of the following deployments:


   - [Securing Private Application Access by Using Service Connections: Deployment Guide—Provides](https://architectures.link/2040p-prime)

implementation details for connecting enterprise network resources to Prisma Access by using service connections,

which provide secure private-application access to mobile users and remote sites. Includes decision criteria for

deployment scenarios, as well as step-by-step procedures that achieve an integrated design.


   - [Securing Private Application Access with ZTNA Connector in AWS: Deployment Guide—Provides](https://architectures.link/2042p-prime)

implementation details for deploying ZTNA Connector virtual appliances in AWS in order to provide secure private
application access to mobile users and remote sites. Includes decision criteria for deployment scenarios, as well as

step-by-step procedures that achieve an integrated design.


   - [Securing Private Application Access with ZTNA Connector in Azure: Deployment Guide—Provides](https://architectures.link/2044p-prime)

implementation details for deploying ZTNA Connector virtual appliances in Azure in order to provide secure private
application access to mobile users and remote sites. Includes decision criteria for deployment scenarios, as well as

step-by-step procedures that achieve an integrated design.


   - [Securing Private Application Access with ZTNA Connector in VMware vSphere: Deployment Guide—Provides](https://architectures.link/2047p-prime)

implementation details for deploying ZTNA Connector virtual appliances in VMware vSphere in order to provide secure

private-application access to Prisma Access mobile users and remote sites. Includes decision criteria for deployment

scenarios, as well as step-by-step procedures that achieve an integrated design.


_Palo Alto Networks_ _6_


_Purpose of This Guide_


The following solution guides build upon this deployment:


   - [AI-Powered Autonomous Digital Experience Management: Solution Guide—Provides design, deployment, and](https://architectures.link/107p-prime)

operational guidance for integrating AI-Powered ADEM with the Palo Alto Networks Prisma SASE solution.


   - [Securing Access to GenAI Applications: Solution Guide—Provides design and deployment guidance for securing](https://architectures.link/2148p-prime)

access to AI applications by using the Prisma Access cloud-delivered security platform and Palo Alto Networks next
generation firewalls.


   - [Mitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide—Provides design and deployment](https://architectures.link/2147p-prime)

guidance for delivering comprehensive data security by using Enterprise DLP.


_Palo Alto Networks_ _7_


_Design Model_

## Design Model


[There are many ways to build a secure architecture by using the concepts discussed in the Securing Internet and Private](https://architectures.link/2075p-prime)

[Applications by Using Prisma Browser and Prisma Access: Design Guide. The design model provides secure access to](https://architectures.link/2075p-prime)

the internet and SaaS applications using Prisma Browser and also provides secure access to private applications by using

Prisma Browser integrated with Prisma Access. This design model assumes you have an existing Prisma Access deployment

that uses either Prisma Agent or GlobalProtect [®] for managed devices. Introducing Prisma Browser to this infrastructure

strengthens security for managed devices and establishes a safe, frictionless pathway for BYOD and contractor access.


On managed devices running Prisma Access agent or GlobalProtect app, Prisma Browser acts as a powerful addition. It

defends against browser-native threats and extends your existing mobile user policies with granular, last-mile controls such

as copy/paste restrictions, download governance, and visibility into user activity within SaaS sessions. Because these devices

maintain a VPN tunnel to Prisma Access, all traffic (both private and SaaS application traffic) flows through Prisma Access.

For optimal routing, you enable agent and internal host detection exclusively for managed devices. For unmanaged devices,

you keep these features disabled because the devices might have agents that connect to different infrastructures.


_Figure 1_ _Managed device flow_


Prisma Browser turns unmanaged and personal endpoints into secure workspaces, allowing employees and contractors

to safely reach your organization’s internal and SaaS applications without installing a local agent. Because there is no

VPN agent on unmanaged devices, you enable the Prisma Access Explicit Proxy in order to provide connectivity to private

applications.


_Palo Alto Networks_ _8_


_Design Model_


_Figure 2_ _Unmanaged Device Flow_


[The Secure Internet Policy Design: Solution Guide](https://architectures.link/2150p-prime) organizes applications in Prisma Access into three tiers: Sanctioned,

Tolerated, and Unsanctioned.


To extend this model to Prisma Browser, you create matching application groups in Prisma Browser so the same

classification can be used for browser policies:


   - Sanctioned applications are formally approved to meet a business need. They are business-critical and typically

permitted without functional restrictions.


   - Tolerated applications are apps and websites not explicitly classified as sanctioned or unsanctioned. Users can still

access them, but under stricter security controls.


   - Unsanctioned applications are known to pose risk to the organization and are blocked without exception.


Permissions within each category vary based on whether the user is on a managed or unmanaged device. Because traffic on

unmanaged devices is much harder to decrypt, these endpoints cannot piggyback off your existing Prisma Access policies

the way managed devices do, so you define a separate, broader policy for them. Beyond that, the last-mile controls that only

Prisma Browser can enforce should also differ by trust level. For example, a sanctioned SaaS app might allow full download

access from a managed laptop while restricting downloads and clipboard activity on a personal device.


To enforce this distinction, you define a managed device group that checks for the presence of a certificate on the endpoint.

Devices with the certificate are classified as managed and receive broader access. Devices without the certificate are treated

as unmanaged and subject to tighter restrictions.


You apply the pre-configured Restricted Browser control set on both device groups to reduce the browser’s attack surface

by disabling vulnerable APIs and protocols. You pair this with a browser customization policy that enforces timely updates,

ensuring users always run a version with the latest security patches.


_Palo Alto Networks_ _9_


_Design Model_


You enforce the use of Prisma Browser using two layers of protection. The first uses Entra ID's conditional access policy to

block unauthorized browsers from reaching sensitive applications. The second layer applies endpoint controls, such as the

Prisma Browser extension or a mobile device management (MDM) solution, to prevent unauthorized browsers from running

on user devices. Together, these layers provide comprehensive coverage against unauthorized access.


Finally, in order to access private applications, you use an existing configuration that includes either Prisma Access service

connections or ZTNA Connectors. This setup provides seamless, secure access to your private applications and gives you

the ability to configure non-web-based connections.


_Palo Alto Networks_ _10_


_Assumptions and Prerequisites_

## Assumptions and Prerequisites


This deployment assumes the following:


   - Your organization has a Palo Alto Networks customer support account. If you do not have a support account, you can

[create one at the Customer Support Portal.](https://support.paloaltonetworks.com/Support/Index)


   - You have Prisma Access with the Prisma Browser add-on license.


   - You have a Prisma Access mobile user license with sufficient quantity for your organization.


   - You have Microsoft Entra ID as your IdP and have a directory with users and groups.


   - Your Entra ID has the licenses required for deploying conditional access policies.


Additionally, for organizations with IT-managed endpoints:


   - You have already deployed Prisma Access with an agent-based access using tunnel-mode configuration as described

[in the Securing Internet for Mobile Users by Using Tunnel Mode: Deployment Guide. This guide also includes](https://architectures.link/2024p-prime2)

the configuration steps to configure the CIE authentication profile and CIE directory sync service that Prisma Browser

uses.


   - This guide also assumes that you have previously activated and configured Enterprise DLP as described in the

[Mitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide.](https://architectures.link/2147p-prime)


Additionally, for organizations with unmanaged endpoints:


   - You have already deployed Prisma Access with an agent-based access that uses proxy-mode configuration as

[described in the Securing Internet for Mobile Users by Using Explicit Proxy: Deployment Guide. If you have not,](https://architectures.link/2020p-prime2)

you should complete the configuration in this guide before continuing.


   - This guide also assumes that you have completed post-onboarding tasks to enable private-application access for

explicit proxy.

### VALIDATION ENVIRONMENT

At the time of writing, we used the following environment to validate this design:


   - Prisma Browser version 148.12.1.68


   - SCM version 2026.r1.3


   - Prisma Access version 6.1.0 Preferred


   - Prisma Access agent version: 26.1.2.4


   - GlobalProtect app version: 6.3.3


   - Microsoft Windows 11 clients


_Palo Alto Networks_ _11_


_Assumptions and Prerequisites_




   - Prisma Browser Extension with Windows 11 Chrome and Edge browsers


   - MacOS Sequoia 15.7.5 clients


_Palo Alto Networks_ _12_


_Deployment Details_


## Deployment Details





This section guides you through the activation workflow and then the initial setup of the Cloud Identity Engine (CIE) and

Prisma Browser. You must complete these tasks to support Prisma Browser for IT-managed endpoints and unmanaged

endpoints.


1.1 Activate Prisma Browser

For this procedure, you need the activation email that you received after you purchased Prisma Browser. To activate Prisma

Browser and any additional add-on licenses you have purchased, you use the Palo Alto Networks activation console.


Step 1: In your Prisma Access license activation email, click the highlighted link. Guided activation begins.


Step 2: After you log in to the activation console with your customer support account, in the row for Prisma Browser, in the

Action column, click Activate.


This procedure assumes that you will use the default tenant that was assigned to your Customer Support Portal account. If

necessary, you can rename the tenant after you complete the activation. You can also create a sub-tenant and then activate

Prisma Browser in the sub-tenant, but that is beyond the scope of this guide.


Step 3: In the Specify the Tenant list, accept the choice or your default tenant.


Step 4: In the Select Region list, choose your region (example: United States).


Step 5: After you review the terms and conditions, select Agree to the Terms and Conditions, and then click Activate

Now. The provisioning process begins.


Step 6: After the provisioning process completes, verify that the status of the licensed product for the tenant is Active.


_Palo Alto Networks_ _13_


_Deployment Details_


1.2 Access Strata Cloud Manager

Strata [™] Cloud Manager (SCM) provides a single management pane that combines Prisma Access, NGFW, and Prisma SD
WAN tasks.


Step 1: [Log in to SCM.](https://stratacloudmanager.paloaltonetworks.com/)

To navigate to specific functions, you use the left panel. If the left panel is collapsed, to see the text labels that describe each

function, you can expand it by clicking the chevron at the bottom of the left panel.


Step 2: For effective navigation within SCM, familiarize yourself with the icons. You access initial setup, configuration, and

operations tasks by using _Configuration_ commands.


1.3 Assign Group Membership for Authorized Users

Later in this guide, you create group-based policy rules that use information from Microsoft Entra ID. In this procedure, you

create the Microsoft Entra ID group and assign example users to the group.


This procedure assumes that your Microsoft Entra ID configuration already includes groups for Employees and Contractors,

if not, then create them now.


Step 1: [Log in to the Azure Resource Manager at https://portal.azure.com.](https://portal.azure.com/)


Step 2: Navigate to Home > Microsoft Entra ID.

First, you create the group.


Step 3: On the left, select Manage > Groups, and then click New Group.


Step 4: In the Group Name box, enter AI-access-permitted, and then click Create.

Next, you add members to the group.


Step 5: In the list of groups, click AI-access-permitted, and then on the left, select Manage > Members.


Step 6: Click Add Members.


_Palo Alto Networks_ _14_


_Deployment Details_


Step 7: In the Add members pane, for each user that you want to assign to the group, select the row (example: amy or

chris), and then click Select.


Step 8: Review group membership to ensure it includes your example users.


1.4 Enable Prisma Browser

Now that you have configured CIE for both Directory Sync and authentication, you deploy Prisma Browser.


Step 1: In SCM, navigate to Configuration > Prisma Browser, and then click Enable Prisma Browser.


Step 2: On the Prisma Browser page, navigate to Administration > Onboarding.


Step 3: On the Users Page, under Authentication profile, select example.com-entra_id.


Step 4: Under User groups, in the Directory list, choose your Entra ID directory.


_Palo Alto Networks_ _15_


_Deployment Details_


Step 5: In the User groups list, choose the user groups that will use Prisma Browser (example: Employees, Contractors).


Step 6: At the bottom of the page, click Next: Prisma Access integration.


Step 7: At the bottom of the page, click Next: Routing.


Step 8: In the Traffic flow section, select Only route private application traffic through Prisma Access.


Step 9: Click Next: Enforce SSO applications.


Step 10: Expand the Configure your SSO enforcement section.


Step 11: Ensure Dedicated IP addresses is selected and in the Dedicated IP addresses box, click the copy icon, and then

paste the IP addresses in a safe place. You must have these IP addresses when you create a conditional access policy in

Procedure 3.1.


Step 12: In the Identity Providers section, select Microsoft Azure Active Directory.

|Col1|Col2|Note|
|---|---|---|
|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|



Step 13: Under Authentication traffic, enable the slider to Traffic is routed, and then click Save changes.


Step 14: Click Next: Download and distribute. On this page, you download the latest version of Prisma Browser or copy a

download link for the browser, depending on the browser distribution method for your organization.

|Col1|Col2|Note|
|---|---|---|
|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.|



_Palo Alto Networks_ _16_


_Deployment Details_



Step 15: Click Next: Browser policy.


Step 16: Click Browser Policy. Setup is complete.





After the initial setup of Prisma Browser is complete, you create policies that customize the browser for your organization.

There are many ways to construct your policies to meet the needs of your organization. The following procedures serve as

a flexible starting point for how you can create policies. You can adopt the policies that align with your goals, mix and match

specific elements, or modify them entirely to fit your unique requirements.


In this deployment, you create access and data policies around managed and unmanaged devices and sanctioned, tolerated,

and unsanctioned applications. Because managed users in this deployment use a full-tunnel connection to Prisma Access,

it is assumed that Prisma Access handles their primary DLP and security policies. For these managed users, the browser

policies focus on layering specific browser-based protections that Prisma Access cannot enforce. Conversely, because

unmanaged users do not use a full-tunnel connection, you apply more comprehensive DLP policies directly within Prisma

Browser. You also create specific AI policies that restrict access to AI applications to only users who are in the AI-access
permitted group.


To protect data, these policies make use of _nested DLP profiles_, which are containers that can hold other data profiles. For

example, you can use nested data profiles to build a Global PII Protection policy by nesting the profiles for US PII, EU PII

General Data Protection Regulation, and APAC PII within it.


_Palo Alto Networks_ _17_


_Deployment Details_


[For more information about DLP profiles and how to create them, see the Mitigating Data-Exfiltration Risk by Using](https://architectures.link/2147p-prime)

[Enterprise DLP: Solution Guide.](https://architectures.link/2147p-prime)


2.1 Create Device Group

To apply policies to managed and unmanaged devices, you must first create device groups that define the criteria for each

category. In this example, managed devices are identified by their certificates. By uploading the issuer certificate, you enable

Prisma Browser to recognize managed devices. Any device lacking this certificate is automatically classified as unmanaged.


This procedure assumes that your organization has a root certificate authority (CA) or an intermediate CA that issues and

signs device certificates for your managed devices. You must have a copy of the certificate for issuing CA in one of the

supported formats: PEM, CER, CRT or CER.

|Col1|Col2|Caution|Col4|
|---|---|---|---|
|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.||



Step 1: In SCM, navigate to Configuration > Prisma Browser > Directory > Devices.


Step 2: On the Device Groups tab, click Add device group.


Step 3: Under Group name, enter Managed Devices.


Step 4: Under Platform, select Desktop Browser, and then click Next: Device group attributes.


Step 5: Select Issuer Certificate, and then click Add issuer certificate.


_Palo Alto Networks_ _18_


_Deployment Details_


Step 6: Upload the issuer certificate that you use for your managed devices, click Set, and then click Create.


2.2 Create a Sign-in Rule to Enable Posture Status View

When you configure a sign-in rule that includes a device group, Prisma Browser performs a posture check on the attributes

that you assigned in the device group. As an example, because the Managed Devices group includes the Issuer Certificate

attribute, Prisma Browser checks for the presence of a valid device certificate when a user signs in to Prisma Browser.


You should assign this sign-in rule a priority higher than the default rule.


In this example, the default action for the sign-in rule is Allow, so the policy provides visibility only and does not restrict

access. The information that Prisma Browser collects might be useful for troubleshooting. If you want to restrict access

based on the sign-in rule, you change the action to Block.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Sign-in Rules.


Step 2: Click Create, and then in the Create list, choose New rule.


Step 3: In the Name box, enter Enable Posture Status View for Managed Device Certificate.


Step 4: Click Next: Scope.


_Palo Alto Networks_ _19_


_Deployment Details_


Step 5: In the Device groups list, choose Managed Devices, and then click Save.


2.3 Create Application Groups

In order to define which applications are sanctioned or unsanctioned, you create application groups. You then use these

groups when creating policies. You should adjust sanctioned and unsanctioned applications according to your specific

business needs.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.||



First, you create the sanctioned application group and you add specific example applications to the group.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Directory > Applications.


Step 2: On the Application Groups tab, click Add application group.


Step 3: In the Name box, enter Sanctioned Applications.


_Palo Alto Networks_ _20_


_Deployment Details_


Step 4: In the Applications list, search for and choose Workday HCM and Salesforce Desk, and then click Save.


Next, you create the unsanctioned application group. In this example, you use Dropbox and WeTransfer as unsanctioned

applications.


Step 5: On the Application Groups tab, click Add application group.


Step 6: In the Name box, enter Unsanctioned Applications.


Step 7: In the Applications list, search for and choose Dropbox and WeTransfer, and then click Save.


2.4 Create Block Unsanctioned and High-Risk Policy

First, you create the Block Unsanctioned and High-Risk Applications rule. This policy blocks all users from accessing any

unsanctioned application or website classified as high risk by Palo Alto Networks. This gives baseline protection from users

accessing malicious or poor security web sites. This policy applies to every device.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Block Unsanctioned and High-Risk Applications.


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: Click Next: Applications.


Step 7: Select Internet and SaaS applications.


Step 8: Select Custom.


_Palo Alto Networks_ _21_


_Deployment Details_


Step 9: In the Website Classification list, search for and choose Risk level: High and Risk Level: Medium.


Step 10: Select Application groups.


Step 11: In the Select Application groups list, select Unsanctioned Applications.


Step 12: Click Next: Access.


Step 13: Select Block.


Step 14: Click Next: Tracking.


Step 15: Select On, click Save, and then click Save anyway.


2.5 Create the Managed Device Sanctioned Applications Policy

Next, you create the Sanctioned Applications (Managed) policy. This policy gives full access to trusted sanctioned

applications.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Sanctioned Applications (Managed).


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: In the Device groups list, choose Managed Devices.


Step 6: Click Next: Applications.


Step 7: Select Application groups.


Step 8: In the Select Application groups box, select Sanctioned Applications.


Step 9: Click Next: Access.


Step 10: Select Allow.


_Palo Alto Networks_ _22_


_Deployment Details_


Step 11: Click Next: Login controls.


Step 12: Click Next: Controls and data profiles.


Step 13: At the top of the screen, click Control set: None.


Step 14: In the control set list, choose Allow full access, and then click Save.


2.6 Create the Managed Device Tolerated Applications Policy

Next, you create the Tolerated Applications (Managed) policy. This policy applies to all other sites accessed by managed

devices. Since the policy assumes that users on IT-managed devices tunnel all traffic through Prisma Access, Prisma Access

handles the enterprise DLP. Using the PII DLP profile, this policy layers on baseline browser protections that only the browser

can perform.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Tolerated Applications (Managed).


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: In the Device groups list, choose Managed Devices.


Step 6: Click Next: Applications.


Step 7: Select Internet & SaaS applications and keep the default of Any internet & SaaS application.


Step 8: Select Private applications and keep the default of Any private application.


Step 9: Click Next: Access.


Step 10: Select Allow.


Step 11: Click Next: Login controls.


Step 12: Click Next: Controls and data profiles.


Step 13: On the Controls and data profiles page, click + Set data profile.


Step 14: On the Data profile side drawer pane, select Specific data profile.


Step 15: For Select data profile, choose PII, and then click Save.


Step 16: Select Clipboard.


Step 17: In the Clipboard window, Select Copy & paste data out, select Block, and then click Set.


Step 18: Select Screenshot.


Step 19: In the Screenshot window, choose Block, and then click Set.


Step 20: Select Print.


_Palo Alto Networks_ _23_


_Deployment Details_


Step 21: In the Print window, choose Block, click Set, and then click Save.


2.7 Create the Unmanaged Device Sanctioned Applications Policy

Next, you create the Sanctioned Applications (Unmanaged) policy. This policy gives access to trusted sanctioned

applications, provides baseline protections through Advanced WildFire [®], and uses a nested DLP profile to protect sensitive

data.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Sanctioned Applications (Unmanaged).


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: Click Next: Applications.


Step 6: Select Application groups.


Step 7: In the Select Application groups box, select Sanctioned Applications.


Step 8: Click Next: Access.


Step 9: Select Allow.


Step 10: Click Next: Login controls.


Step 11: Click Next: Controls and data profiles.


Step 12: On the Controls and data profiles page, click + Set data profile.


Step 13: On the Data profile side drawer pane, choose Specific data profile.


Step 14: For Select data profile, choose Nested-network-dlp-profile, and then click Save.


Step 15: On the Controls and data profiles page, select File Download.


Step 16: In the File Download window, choose Block, and then click Set.


Step 17: Select File Upload.


Step 18: In the File Upload window, choose Block, and then click Set.


Step 19: On the Controls and data profiles page, select Malicious File Protection.


Step 20: Select Enable.


Step 21: Under Action, select Prevent.


Step 22: In the Engine list, choose Advanced WildFire.


Step 23: Under Upon, select File Upload.


_Palo Alto Networks_ _24_


_Deployment Details_


Step 24: Click Set, and then click Save.


2.8 Create the Unmanaged Device Tolerated Applications Policy

Next, you create the Tolerated Applications (Unmanaged) policy. This policy applies to any other applications that are not

explicitly listed in either the Sanctioned application group or the Unsanctioned application group and that are accessed by

unmanaged devices and blocks all files uploaded and downloaded through Prisma Browser.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Tolerated Applications (Unmanaged).


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: Click Next: Applications.


Step 6: Select Internet & SaaS applications and keep the default of Any internet & SaaS application.


Step 7: Select Private applications and keep the default of Any private application.


Step 8: Click Next: Access.


Step 9: Select Allow.


Step 10: Click Next: Controls and data profiles.


_Palo Alto Networks_ _25_


_Deployment Details_


Step 11: On the Controls and data profiles page, select File Download.


Step 12: In the File Download window, choose Block, and then click Set.


Step 13: Select File Upload.


Step 14: In the File Upload window, choose Block, and then click Set.


Step 15: Click Save, and then click Save anyway.


2.9 Create AI policy

In this procedure, you configure a set of policy rules that you use to control access to sanctioned, tolerated, and

unsanctioned AI applications for authorized users. This procedure references the Microsoft Entra ID group that you created in

Procedure 1.3.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter AI Access Permitted.


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: In the Users/User groups list, choose AI-access-permitted.


Step 6: In the Device groups list, choose Managed Devices.


Step 7: Click Next: Applications.


Step 8: Select Internet & SaaS applications, and then select Custom.


Step 9: In the Website Classification list, search for and choose Artificial Intelligence.


Step 10: Click Next: Access.


Step 11: Select Allow.


Step 12: Click Next: Login controls.


Step 13: Click Next: Controls and data profiles.


Step 14: On the Controls and data profiles page, click + Set data profile.


Step 15: On the Data profile side drawer pane, choose Specific data profile.


Step 16: For Select data profile, choose Nested-network-dlp-profile, and then click Save.


Step 17: On the Controls and data profiles page, Select File Upload.


Step 18: In the File Upload window, choose Block, and then click Set.


Step 19: Click Next: Tracking, and then click Save.

Next you create an AI policy to block any user who is not in the AI-access-permitted group and on a managed device.


_Palo Alto Networks_ _26_


_Deployment Details_


Step 20: In the Create list, choose New rule.


Step 21: In the Name box, enter AI Access Denied.


Step 22: Under Rule Type, select Access & Data Control.


Step 23: Click Next: Scope.


Step 24: Click Next: Applications.


Step 25: Select Internet & SaaS applications, and then select Custom.


Step 26: In the Website Classification list, search for and choose Artificial Intelligence.


Step 27: Click Next: Access.


Step 28: Select Block, and then click Save.


2.10 Organize and Adjust Policy Rules

In this procedure, you create sections in order to organize your policies and arrange them in the correct evaluation sequence.

Proper ordering is critical: if a rule is placed incorrectly, it might trigger prematurely and prevent subsequent policies from

being processed.


The following image details the correct order of the policies.


_Palo Alto Networks_ _27_


_Deployment Details_


_Figure 3_ _Policy priority_


Step 1: Continuing on the Policy Rules page, in the Create list, choose New section.


Step 2: For Section name, enter AI Policy, and then click the blue checkmark.


Step 3: To create Managed Devices and Unmanaged sections, repeat Procedure 2.10, Step 1 and Procedure 2.10, Step

2 for each section.


Step 4: Click Change priorities.


Step 5: Drag and drop policies into their corresponding sections and reorder them as shown in Figure 3. When you're done,

click Save changes.


_Palo Alto Networks_ _28_


_Deployment Details_


2.11 Create Browser Security Policy to Enforce Best Practices

Next, you create a Browser Security policy. This policy uses the pre-configured control set Restricted Browser in order to

reduce the browser attack surface, perform browser hardening, enable network protection to block web pages with SSL

errors or with insecure content, and enforce strict control of password saving and autofill data.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Secure Browser.


Step 3: Under Rule Type, select Browser Security, and then click Next: Scope.


Step 4: Click Next: Browser Security controls.


Step 5: At the top of the page, click Controls set: None, and then select Restricted browser.


Step 6: Click Save, and then click Save anyway.


2.12 Create Browser Customization Policy to Ensure Latest Version

In this procedure, you create a policy that mandates scheduled Prisma Browser updates. This policy ensures the prompt

application of the most recent security patches and updates to the browser's security engines.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Enforce Upgrades.


Step 3: Under Rule Type, select Browser Customization, and then click Next: Scope.


Step 4: Click Next: Browser Customization controls.


Step 5: Scroll down to the Upgrade Management pane, and then click Deployment Upgrade.


Step 6: Select Default channel.


Step 7: In the Update grace period pane, choose the grace period, and then click Set.


_Palo Alto Networks_ _29_


_Deployment Details_



Step 8: Click Save, and then click Save anyway.


Step 9: At the top right of the screen, click Review changes, click Next, and then click Publish.





This section includes example configurations for two browser-enforcement options. You can use these options on their own

or in combination with one another.


As a baseline, Palo Alto Networks recommends that you use a conditional access policy in order to ensure that you access

sanctioned SaaS applications using Prisma Browser.


3.1 Create an Entra ID Conditional Access Policy

In this procedure, you create a conditional access policy within Microsoft Entra ID in order to permit access to certain

applications through Prisma Browser only. This policy makes use of the Prisma Browser proxy’s known IP addresses in order

to create a policy that allows access only when trying to authenticate on these known IP addresses.


Before creating the policy, you must define the Prisma Browser proxy IP range.


Step 1: Log in to your Azure portal.


Step 2: Click Microsoft Entra ID.


_Palo Alto Networks_ _30_


_Deployment Details_


Step 3: On the Entra ID Overview page, in the left menu, navigate to Manage > Security.


Step 4: On the Security page, navigate to Manage > Named Locations, and then click IP ranges location.


Step 5: In the New Location (IP Ranges) pane, in the Name box, enter Prisma Browser Range.


Step 6: Above the Name box, click Download. An example text document downloads.


Step 7: Open the downloaded text document.


Step 8: Replace the example IP ranges with the IPs copied in Procedure 1.4, Step 11.


Step 9: Save this file in a safe place.


Step 10: In the New location (IP ranges) pane, click Upload.


Step 11: Select the file saved in Step 9, and then click Create.


Next, you create the conditional access policy that enforces users to access applications through Prisma Browser.


Step 12: Continuing in the Azure portal, on the Microsoft Entra ID Security page, navigate to Protect > Conditional Access,

and then click Create new policy.


Step 13: In the Name box, enter Force Prisma Browser.


Step 14: Under Users or agents, click 0 users and agents selected.


Step 15: On the Include tab, select All users.


_Palo Alto Networks_ _31_


_Deployment Details_


Step 16: Under Target Resources, click No target resources selected.

When defining your target resources, you can choose specific applications or select all of them. Choosing "All resources"

mandates that every enterprise application in your Entra ID be accessed exclusively through Prisma Browser. In this example,

you select specific enterprise applications to require Prisma Browser access.


Step 17: On the Include tab, select Select resources, and then under Select specific resources, click None.


Step 18: In the Resources pane, select the enterprise applications (example: Office 365) that users must access through

Prisma Browser, and then click Select.


Step 19: Under Network, click Not configured.


Step 20: For Configure, select Yes.


Step 21: On the Exclude tab, under Select, click None.


Step 22: In the Select Networks pane, select Prisma Browser Range.


_Palo Alto Networks_ _32_


_Deployment Details_


Step 23: Under Grant, click 0 controls selected.


Step 24: Select Block Access, and then click Select.


Step 25: Under Enable Policy, select On, and then click Create.


Now for users to access the selected applications, they must use Prisma Browser.


3.2 Create a Microsoft Intune Policy to Enforce the Use of Prisma Browser

In this procedure, you create use the Microsoft Intune MDM solution to create a policy to block other browsers from being

able to run on Windows computers. This procedure assumes you have an Intune deployment that the endpoints are

connected to.


Step 1: Log in to your Microsoft Intune Portal.


Step 2: Navigate to Devices > Manage Devices > Configuration.


Step 3: On the Policies tab, click Create > New Policy.


Step 4: In the Platform list, choose Windows 10 and later.


Step 5: In the Profile Type list, choose Settings catalog.


Step 6: Click Create


Step 7: On the Basics tab, under Name, enter Block non-PB browsers.


Step 8: In the description box, enter Block Chrome, Edge, Firefox, and Opera, and then click Next.


_Palo Alto Networks_ _33_


_Deployment Details_


Step 9: Click Add settings.


Step 10: In the search box, enter List of disallowed applications and click Search.


Step 11: Under Browse by category, click Administrative Templates\System.


Step 12: Under Setting name, click the List of disallowed applications (User) check box.


Step 13: At the top-right corner of the Settings picker menu, click the X.


Step 14: To restrict running specified Windows applications, enable the Don't run specified Windows applications slider.


Step 15: In the resulting box, enter chrome.exe.


Step 16: In the subsequent boxes, enter firefox.exe, opera.exe, and msedge.exe, and then click Next.


Step 17: On the Scope Tags page, click Next.


Step 18: On the Assignments page, under Included groups, click Add Groups.


Step 19: Search for and select the user group Employees, and then click Select.


Step 20: Click Next, and on the Review + Create page, click Create.





A unique capability of the Prisma Browser Extension is that you can use it to enforce the usage of Prisma Browser. You can

configure a policy rule so that when users running consumer browsers with the Prisma Browser Extension try to access

specified web sites, they are automatically redirected to use Prisma Browser instead.


_Palo Alto Networks_ _34_


_Deployment Details_


4.1 Create policy to redirect Prisma Browser Extension to Prisma Browser

To create a policy rule that applies only to users with the Prisma Browser Extension, you must first create a device group

to match the browser extension for all OS versions. You then use this device group in a policy rule to force the redirect to

Prisma Browser.


Step 1: In SCM, navigate to Configuration > Prisma Browser > Directory > Devices.


Step 2: On the Device Groups tab, click Add device group.


Step 3: In the Group name box, enter Prisma Browser Extension.


Step 4: In the Platform section, click Browser Extension, and then click Next: Device group attributes.


Step 5: Clear OS version, and then click Create.


Step 6: On the Prisma Browser page, navigate to Policy > Rules, and then in the Create list, choose New rule.


Step 7: In the Name box, enter Redirect All Consumer Browsers to Prisma Browser.


Step 8: Under Rule Type, select Access & Data Control.


Step 9: Click Next: Scope.


Step 10: In the Device groups list, choose Prisma Browser Extension.


Step 11: Click Next: Applications.


Step 12: Select Internet & SaaS applications and Private applications.


Step 13: Click Next: Access.


Step 14: Select Enforce Prisma Browser Extension traffic redirection to Prisma Browser.


Step 15: Select Redirection will automatically open Prisma Browser, and then click Save.


Step 16: At the top right of the screen click Review changes, click Next, then click Publish.


_Palo Alto Networks_ _35_


_Deployment Details_


4.2 Download the Prisma Browser Extension Installer from SCM

To deploy the Prisma Browser Extension, you must use SCM to generate a configuration that specifies the identity provider

that you use, the device management method, and the browser type.


The Prisma Browser Extension supports the following methods listed in Table 1.


_Table 1 Prisma Browser Extension deployment options for Chromium-based browsers_










|Identity provider|Device management method|Browser types|
|---|---|---|
|Okta<br>Microsoft Entra ID<br>Google|Jamf<br>Manual deployment|Arc<br>ChatGPT Atlas<br>Brave<br>Chrome<br>Comet<br>DIA<br>Edge|
|Okta<br>Microsoft Entra ID<br>Google|Google Workspace|Chrome|
|Okta<br>Microsoft Entra ID<br>Google|Windows MDM|Arc<br>Brave<br>Chrome<br>Comet<br>Edge|



You can deploy the extension to the Safari browser with either Jamf or by using manual deployment.


For Windows systems, to install the extension, SCM provides both a PowerShell script and registry modification file. For

MacOS systems, to install the extension, SCM provides a package file.


In this example, you use Chrome browser with Microsoft Entra ID and deploy it manually on a Windows system by using a

registry modification file.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser.


Step 2: On the Prisma Browser page, navigate to Administration > Onboarding.


_Palo Alto Networks_ _36_


_Deployment Details_


Step 3: On Step 5 Download and distribute, click the Deploy Prisma Browser Extension pane. The pane expands.


Step 4: In the Identity provider (IdP) list, choose Azure.


Step 5: In the Device management list, choose Manual Deployment (Locally).


Step 6: In the Browser list, select Chrome, and then click Generate.


Step 7: Verify that the Login domain(s) settings include your FQDN (example: test-example.com).


Step 8: Click the Windows pane. The pane expands.


Step 9: If you are testing on an unmanaged device, select Apply testing mode adaptations.


Step 10: To download the extension configuration, click Download .reg file.


Step 11: When prompted, save the file to your local system and note the file name and location.


4.3 Install the Prisma Browser Extension

In this procedure, you use a registry modification file to install the Prisma Browser Extension for Chrome on a Windows

system.


This procedure assumes that the Prisma Browser is already installed.


Step 1: On the Windows system where you intend to install the Prisma Browser Extension, copy the file you downloaded

previously in Procedure 4.2 Step 11.


Step 2: To make registry changes, double-click the copied .reg file.


Step 3: Launch Chrome and navigate to chrome://policy, and then click Reload policies.


Step 4: On the Chrome toolbar, click the extensions symbol and in the row for Prisma Browser Extension, click the

thumbtack icon to pin the extension.


_Palo Alto Networks_ _37_


_Deployment Details_


Step 5: Click the Prisma Browser Extension. The extension pane appears.


Step 6: Click Log in.


Step 7: [In the Enter your work or school account box, enter your user ID (example: brian@test-example.com), and then](mailto:brian@test-example.com)

click Continue.


Step 8: If your user ID is associated to multiple Prisma Browser tenants, click the preferred tenant.


_Palo Alto Networks_ _38_


_Deployment Details_



Step 9: When prompted, enter the password.


Step 10: Click Continue browsing.





_Palo Alto Networks_ _39_


_Deployment Details_


The procedures in this section are required only if you are routing traffic to private applications. In this design, managed

devices connect to Prisma Access via their existing VPN agent tunnels, while unmanaged devices connect using an explicit

proxy.


This architecture requires an existing Prisma Access tenant with either a service connection or a ZTNA Connector routing to

the data center or private cloud where your private applications are located.


[If you are using service connections, you have configured them as described in Securing Private Application Access by](https://architectures.link/2040p-prime)

[Using Service Connections: Deployment Guide.](https://architectures.link/2040p-prime)


Otherwise, if you are using ZTNA Connector, you have configured them as described in any of the following guides:


   - [Securing Private Application Access with ZTNA Connector in AWS: Deployment Guide](https://architectures.link/2042p-prime)


   - [Securing Private Application Access with ZTNA Connector in Azure: Deployment Guide](https://architectures.link/2044p-prime)


   - [Securing Private Application Access with ZTNA Connector in VMware vSphere: Deployment Guide](https://architectures.link/2047p-prime)


Additionally, Prisma Access must already be configured for VPN agents and explicit proxy to support your mobile users as

[described in Securing Internet for Mobile Users by Using Tunnel Mode: Deployment Guide](https://architectures.link/2024p-prime2) [and/or Securing Internet](https://architectures.link/2020p-prime2)

[for Mobile Users by Using Explicit Proxy: Deployment Guide.](https://architectures.link/2020p-prime2)


_Figure 4_ _Private application access_


In this setup, you first configure a browser customization policy with agent and internal host detection. This ensures traffic is

routed efficiently and guarantees that managed devices use the VPN tunnel to access private applications. For unmanaged

devices, you must enable the Prisma Access explicit proxy to accept Prisma Browser traffic and route it to private apps.


After these configurations are complete, you define your applications in Prisma Browser. This example walks you through

creating two applications for users to access: a standard web application and a non-standard (SSH) application.


_Palo Alto Networks_ _40_


_Deployment Details_


5.1 Create Browser Customization Policy for Managed Devices

In this procedure, you create a policy that Prisma Browser uses to determine if an IT-managed endpoint can reach internal

networks and a VPN agent (either the Prisma Access agent or GlobalProtect app) is installed. For access to private apps, this

policy requires that the VPN agent must be connected to Prisma Access. Prisma Browser then connects to the private apps

by using the VPN agent tunnel.


In this example, the internal host detection check uses the host dc01-web.example.com with IP address 10.5.0.10. This

private app must be reachable from Prisma Access by using a service connection or ZTNA Connector. If the VPN agent is

not connected to Prisma Access, the internal host detection check fails.


You should assign this policy rule a priority higher than the Browser Customization - baseline rule. As a result of this policy,

unmanaged endpoints use explicit proxy to access private applications.


Step 1: In SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: On the Browser Customization tab, click Create, and then click New rule.


Step 3: In the Name box, enter Internal Host Detection and Agent Detection (Managed Devices).


Step 4: Click Next: Scope.


Step 5: In the Device groups list, select Managed Devices.


Step 6: Click Next: Browser Customization controls.


Step 7: Scroll down to the Routing pane, and then click Internal network detection.


Step 8: Select Enable.


Step 9: Select Internal host detection.


Step 10: In the FQDN to resolve box, enter dc01-web.example.com.


Step 11: In the Expected IP address box, enter 10.5.0.10.


_Palo Alto Networks_ _41_


_Deployment Details_


Step 12: Select Agent detection, and click Set, and then click Save.


Step 13: At the top right of the screen, click Review changes, click Next, and then click Publish.


5.2 Enable Prisma Access Explicit Proxy (Optional)

If you have not already deployed Prisma Access with an agent-based access by using proxy mode configuration as

[described in the Securing Internet for Mobile Users by Using Explicit Proxy: Deployment Guide, you configure it now.](https://architectures.link/2020p-prime2)

This procedure is not required for IT-managed endpoints, because they use a VPN agent to connect to Prisma Access and

do not require an explicit proxy configuration.


Step 1: Continuing in SCM, navigate to Configure > NGFW and Prisma Access.


Step 2: In the Configuration Scope pane, on the Folders tab, choose Explicit Proxy.


Step 3: On the Setup tab, in the Infrastructure Settings pane, click the edit cog.


Step 4: In the Explicit Proxy URL box, enter the hostname (such as example) that you want to use for explicit proxy, and

then click Save.

Next, you set up explicit proxy to use Entra ID for authentication.


Step 5: On the Setup tab, in the User Authentication pane, click the edit cog.


Step 6: Under Authentication Method 1, select SAML/Cloud Identity Engine.


Step 7: In the Profile list, choose example.com-entra_id, and then click Save.

Next, you choose the Prisma Access locations to deploy explicit proxy.


Step 8: On the Setup tab, in the Prisma Access Locations pane, click the edit cog.


_Palo Alto Networks_ _42_


_Deployment Details_


Step 9: Click the plus (+) sign at two locations geographically close to the proxy users, and then click Save.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|It is a best practice to add at least two locations for resiliency.|It is a best practice to add at least two locations for resiliency.|It is a best practice to add at least two locations for resiliency.||



Next, you push the explicit proxy configuration to Prisma Access.


Step 10: On the Setup tab, in the Push Config list, choose Push.


Step 11: In the Push Config dialog box, in the Description box, enter a description.


Step 12: Ensure that Explicit Proxy is selected, and then click Push.


Step 13: In the Jobs dialog box, when the result for your ValidateAndPush job is OK, click Done.

SCM should complete the Prisma Access explicit-proxy deployment in approximately 15 to 30 minutes.


5.3 Enable Private Application Access for Prisma Browser

When using Prisma Browser for unmanaged endpoints, for traffic to access private applications through Prisma Access,

you route the traffic via the Prisma Access explicit proxy. In this procedure, you enable private application access for Prisma

Browser and private app access for explicit proxy.


This procedure is not required for IT-managed endpoints, because they use a VPN agent to connect to Prisma Access and

do not require an explicit proxy configuration.


Step 1: Continuing in SCM, navigate to Configure > NGFW and Prisma Access.


Step 2: In the Configuration Scope pane, on the Folders tab, choose Explicit Proxy.


Step 3: On the Setup tab, in the Infrastructure Settings pane, click the edit cog.


_Palo Alto Networks_ _43_


_Deployment Details_


Step 4: In the Prisma Browser pane, enable Prisma Browser.


Step 5: In the Proxy URL Settings pane, select Enable Private App Access for Explicit Proxy, and then click Save.


5.4 Configure Private Applications for Prisma Browser

In order to assign policies to the applications, you must define them as private applications in Prisma Browser.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Directory > Applications > Private

Applications.


Step 2: Click Add private app.


Step 3: In the Name box, enter Example app01.


Step 4: In the FQDN or IP Address box, enter app01.example.com, and then click Add.


Step 5: At the bottom of the pane, click Add.


_Palo Alto Networks_ _44_


_Deployment Details_



Step 6: Repeat this procedure as necessary for any additional private applications.


5.5 Configure Application Group

To simplify the policy management for access to private applications, you create an application group.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Directory > Applications.


Step 2: On the Application Groups tab, click Add application group.


Step 3: In the Name box, enter Private Applications.


_Palo Alto Networks_ _45_


_Deployment Details_


Step 4: In the Applications list, click the filter for Private, search for and choose your private applications (example: dc01
web and dc02-web), and then click Save.


5.6 Create the Managed Device Private Applications Policy

Using the application group for private applications, you create the Private Applications (Managed) policy. This policy gives full

access to private applications.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.||



Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Private Applications (Managed).


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: In the Device groups list, choose Managed Devices.


Step 7: Click Next: Applications.


Step 8: Select Application groups.


Step 9: In the Select Application groups box, select Private Applications.


Step 10: Click Next: Access.


_Palo Alto Networks_ _46_


_Deployment Details_


Step 11: Select Allow.


Step 12: Click Next: Login controls.


Step 13: Click Next: Controls and data profiles.


Step 14: At the top of the screen, click Control set: None.


Step 15: In the control set list, choose Allow full access, and then click Save.


5.7 Create the Unmanaged Device Private Applications Policy

Next, you create the Private Applications (Unmanaged) policy. This policy gives access to private applications, provides

baseline protections through Advanced WildFire, and uses a nested DLP profile to protect sensitive data.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.|Ensure your Prisma Access policies are configured to allow traffic to your private<br> applications; otherwise, access will be blocked.||



Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Private Applications (Unmanaged).


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: Click Next: Applications.


Step 7: Select Application groups.


Step 8: In the Select Application groups box, select Private Applications.


Step 9: Click Next: Access.


Step 10: Select Allow.


Step 11: Click Next: Login controls.


Step 12: Click Next: Controls and data profiles.


Step 13: On the Controls and data profiles page, click + Set data profile.


Step 14: On the Data profile side drawer pane, choose Specific data profile.


Step 15: For Select data profile, choose Nested-network-dlp-profile, and then click Save.


Step 16: On the Controls and data profiles page, select File Download.


Step 17: In the File Download window, choose Block, and then click Set.


_Palo Alto Networks_ _47_


_Deployment Details_


Step 18: Select File Upload.


Step 19: In the File Upload window, choose Block, and then click Set.


Step 20: On the Controls and data profiles page, select Malicious File Protection.


Step 21: Select Enable.


Step 22: Under Action, select Prevent.


Step 23: In the Engine list, choose Advanced WildFire.


Step 24: Under Upon, select File Upload.


Step 25: Click Set, and then click Save.


5.8 Organize and Adjust Private Application Policy Rules

In this procedure, you move the newly created rules into existing sections in order to organize your policies and arrange them

in the correct evaluation sequence. Proper ordering is critical: if a rule is placed incorrectly, it might trigger prematurely and

prevent subsequent policies from being processed.


The following image details the correct order of the policies.


_Palo Alto Networks_ _48_


_Deployment Details_


_Figure 5_ _Policy priority for private applications_


Step 1: Continuing on the Policy Rules page, click Change Priorities.


Step 2: Drag and drop policies into their corresponding sections and reorder them as shown in Figure 5. When you're done,

click Save changes.


_Palo Alto Networks_ _49_


_Deployment Details_


5.9 Configure Remote Connections for Non-Web Apps

To define a non-web application that Prisma Browser includes in the Remote connections list, you must first define it on

SCM. In this example, you use app01 as an SSH remote connection. Unless you configure a policy to disable this capability,

Prisma Browser users can also add connections on their local device even if you don't define them in SCM.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Directory > Applications > Remote

Connections.


Step 2: Click Add remote connection.


Step 3: In the Name box, enter app01 SSH.


Step 4: In the FQDN/IP Address box, enter app01.example.com.


Step 5: In the Protocol list, choose SSH.


Step 6: In the Port box, enter 22, and then click Add.


Step 7: Repeat this procedure as necessary for any other remote connections.


5.10 Create the Policy for Admin-defined Remote Connections

This policy allows access for all managed and unmanaged devices to connect to any admin-defined remote connections

such as the one you created in the previous procedure.


If you also want to allow user-defined remote connections, you should configure that here. Otherwise, you must block user
defined remote connections with an additional policy rule with a block action.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Permit Admin-defined Remote Connections.


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: Click Next: Applications.


Step 7: Select Remote connections.


_Palo Alto Networks_ _50_


_Deployment Details_


Step 8: Select Admin defined remote connections, and then click Save.


5.11 Create the Policy to Disable User-Defined Remote Connections

This policy blocks access for all managed and unmanaged devices to connect to any user-defined remote connections. If

you block access, the Prisma Browser option to add a new (user-defined) connection is disabled for all users and does not

appear on the Remote connections pane.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Block User-defined Remote Connections.


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: Click Next: Applications.


Step 7: Select Remote connections.


Step 8: Select Any remote connection using manual connect.


Step 9: Click Next: Access.


Step 10: Select Block, and then click Save.


Step 11: At the top right of the screen click Review changes, click Next, and then click Publish.


5.12 Organize and Adjust Remote Connection Policy Rules

In this procedure, you move the newly created rules into existing sections in order to organize your policies and arrange them

in the correct evaluation sequence. Proper ordering is critical: if a rule is placed incorrectly, it might trigger prematurely and

prevent subsequent policies from being processed.


The following image details the correct order of the policies.


_Palo Alto Networks_ _51_


_Deployment Details_


_Figure 6_ _Policy priority for remote connections_


Step 1: Continuing on the Policy Rules page. In the Create list, choose New section.


Step 2: For Section name, enter Remote Connections, and then click the blue checkmark.


Step 3: Click Change Priorities.


Step 4: Drag and drop policies into their corresponding sections and reorder them as shown in Figure 6. When you're done,

click Save changes.





After you install Prisma Brower, create your initial profile, and log in, you can access the internet, SaaS applications,

and private applications. Prisma Browser includes several tools you can use to verify operational status and perform

troubleshooting.


_Palo Alto Networks_ _52_


_Deployment Details_


6.1 Access the Prisma Browser Control Pane

Step 1: To access the Prisma Browser control pane, on the top right of the browser window, click the Prisma Browser icon.


The control pane appears.


Step 2: To determine the last time the Prisma Browser policy was updated, hover over the shield icon.


_Palo Alto Networks_ _53_


_Deployment Details_


Step 3: To access the Troubleshooting page, click the shield. You can also access the Troubleshooting page by navigating

directly to prisma://troubleshoot.


You can view more tools by scrolling further in the Troubleshooting page.


_Palo Alto Networks_ _54_


_Deployment Details_


6.2 Perform Prisma Browser Quick Actions

When testing or troubleshooting, if you want to reload or reset the Prisma Browser engine, or to make sure you are running

the latest policy, you use the Quick Actions pane.


Step 1: Continuing from the Prisma Browser Troubleshooting page, to expand the options, click Quick Actions.


Step 2: For the task you want, click the action.


_Palo Alto Networks_ _55_


_Deployment Details_


6.3 Launch Remote Connections for Non-Web Apps

To use Prisma Browser remote connections, you access the remote connections list through the Prisma Browser control

pane and then choose the connection you want to access.


Step 1: To access the Prisma Browser control pane, click the Prisma Browser icon at the top-right of the browser window,

and then on the control pane, click Remote connections.


Step 2: To launch a remote connection, hover over the row for the connection, and then click Connect.


Step 3: Enter your credentials, choose your authentication method, and then click Connect now.


_Palo Alto Networks_ _56_


_Deployment Details_


Step 4: The remote connection opens in a new Prisma Browser tab.


6.4 Verify Prisma Access Integration

If you are using Prisma Access to access private apps, you can verify whether an IT-managed endpoint properly detected

access to the internal network or if an unmanaged endpoint has a valid proxy configuration.


Step 1: Continuing in the Prisma Browser Troubleshooting page, to expand the details, click Prisma Access Integration.

On a managed device, Prisma Browser should indicate Proxy configuration status is Internal network detected.


On an unmanaged device, Prisma Browser should indicate Proxy configuration status is OK.


_Palo Alto Networks_ _57_


_Deployment Details_


Step 2: To test the proxy connectivity for an unmanaged device, click Test.


You can also verify that Prisma Browser is providing access to a private app through a proxy configuration by inspecting the

location bar.


Step 3: To verify the configuration, in the location bar, click the Prisma Access icon.


6.5 Verify Device Posture

If you created a sign-in rule and assigned it a scope that included device attributes, the Prisma Browser control pane includes

the Posture status option.


Step 1: Continuing in the Prisma Browser control pane, to view the specified attributes, click Posture status.

If the device includes a specified attribute, Prisma Browser displays a green check.


If the device is missing a specified attribute, Prisma Browser displays a red warning.


_Palo Alto Networks_ _58_


_Deployment Details_



Step 2: To see additional details, click the attribute (example: Device certificate).


_Palo Alto Networks_ _59_


_Deployment Details_


## Feedback

[You can use the feedback form](https://www.paloaltonetworks.com/resources/reference-architectures/feedback-ra?guid=2076p-16062026) to send comments about this guide.


_Palo Alto Networks_ _60_


#### **HEADQUARTERS**

Palo Alto Networks

3000 Tannery Way

Santa Clara, CA 95054, USA

[https://www.paloaltonetworks.com](https://www.paloaltonetworks.com)



Phone: +1 (408) 753-4000

Sales: +1 (866) 320-4788

Fax: +1 (408) 753-4001

[info@paloaltonetworks.com](mailto:info@paloaltonetworks.com)



©2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks. A list of our trademarks can be

[found at https://www.paloaltonetworks.com/company/trademarks.html. All other marks mentioned herein may be trademarks of their](https://www.paloaltonetworks.com/company/trademarks.html)

respective companies. Palo Alto Networks reserves the right to change, modify, transfer, or otherwise revise this publication without notice.


P-2076P-16062026



**DEPLOYMENT**
**GUIDE**

# Securing Internet and Private Applications by Using Prisma Browser

#### **JUNE 2026**


_Table of Contents_

## Table of Contents


Preface......................................................................................................................................................................................................... 3

Purpose of This Guide................................................................................................................................................................................5

Objectives............................................................................................................................................................................................ 5

Audience..............................................................................................................................................................................................5

Related Documentation........................................................................................................................................................................6

Design Model...............................................................................................................................................................................................7

Assumptions and Prerequisites..................................................................................................................................................................9

Validation Environment.........................................................................................................................................................................9

Deployment Details................................................................................................................................................................................... 10

Activating Prisma Browser and Integrating It with Cloud Identity Engine............................................................................................10

Creating Prisma Browser Policies......................................................................................................................................................19

Restricting the Usage of Other Browsers.......................................................................................................................................... 30

Forcing a Redirect to Prisma Browser by Using the Prisma Browser Extension................................................................................ 34

Configuring Prisma Browser Connector.............................................................................................................................................39

Feedback....................................................................................................................................................................................................45


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


This guide provides deployment details for using Palo Alto Networks [®] Prisma [®] Browser in order to achieve an integrated

design. This deployment guide provides you with a framework for securing access to internet and private applications and

providing security and visibility for your workforce.

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


   - [Securing Internet and Private Applications by Using Prisma Browser: Design Guide—Provides design guidance](https://architectures.link/2070p-prime)

for securely accessing internet and private applications by using Prisma Browser. Details browser-native protections,

including last-mile controls, Enterprise DLP, and cloud-delivered security services across managed and unmanaged

devices. Covers design and deployment considerations for using Prisma Browser Connector to access private and

non-web-based applications, such as SSH and RDP.


The following build upon this deployment:


   - [AI-Powered Autonomous Digital Experience Management: Solution Guide—Provides design, deployment, and](https://architectures.link/107p-prime)

operational guidance for integrating AI-Powered ADEM with the Palo Alto Networks Prisma SASE solution.


   - [Securing Access to GenAI Applications: Solution Guide—Provides design and deployment guidance for securing](https://architectures.link/2148p-prime)

access to AI applications by using the Prisma Access cloud-delivered security platform and Palo Alto Networks next
generation firewalls.


   - [Mitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide—Provides design and deployment](https://architectures.link/2147p-prime)

guidance for delivering comprehensive data security by using Enterprise DLP.


_Palo Alto Networks_ _6_


_Design Model_

## Design Model


To build a secure architecture, you can apply the concepts in this guide in multiple ways. In this model, Microsoft Entra

ID serves as the IdP. It handles SAML authentication for both Prisma Browser and the applications your users access.

Prisma Browser connects with Entra ID by using the CIE, which brokers authentication between users and Entra ID. CIE also

provides group information for use in your Prisma Browser policies by synchronizing user and group identities from Entra ID.


_Figure 1_ _Prisma Browser design model_


After you enable Prisma Browser, you configure browser policies to govern how users interact with applications.


In this example, you organize policies around three application categories:


   - Sanctioned—You formally approve these applications to meet a business need. They are business-critical and

typically permitted without restrictions on functionality.


   - Tolerated—These include any apps or websites that you have not explicitly classified as sanctioned or unsanctioned.

Users can still access them, but with stricter security controls applied.


   - Unsanctioned—These applications are known to pose a risk to the organization and are blocked without exception.


Permissions within each category vary based on whether the user is on a managed or unmanaged device. To make this

distinction, you define a managed device group that checks for the presence of a certificate on the endpoint. Devices with the

certificate are classified as managed and receive broader access. Devices without the certificate are classified as unmanaged

and subject to tighter restrictions such as disabling file downloads and printing.


To protect against evasion and malware, you enforce Palo Alto Networks CDSS, such as Advanced URL Filtering and

Advanced WildFire [®], across all web traffic. These policies use Enterprise DLP profiles to identify and protect sensitive data in

real time. For example, if a user accesses a Tolerated GenAI application from an unmanaged device, the browser's AI prompt


_Palo Alto Networks_ _7_


_Design Model_


collection controls actively prevent the user from pasting proprietary source code into the chat. For baseline browser security,

you apply a restricted browser control set, which reduces the browser's attack surface by disabling vulnerable APIs and

protocols.


For all users, regardless of their device type, you apply a browser enforcement policy that uses the conditional access

capabilities in Entra-ID. This permits access to sensitive applications only for users on devices running Prisma Browser. For

users with managed devices, to prevent unauthorized browsers from running, you also apply endpoint controls, such as the

Prisma Browser extension or an MDM solution. By combining these methods, you provide comprehensive protection against

access from unauthorized browsers.


Finally, in order to access private applications, you use the Prisma Browser Connector. By deploying two redundant ZTNA

Connectors in your data center or cloud environment, you establish a resilient secure link to the Prisma Browser Connector

service. This setup provides seamless, secure access to your private applications and gives you the ability to configure non
web-based connections.


_Palo Alto Networks_ _8_


_Assumptions and Prerequisites_

## Assumptions and Prerequisites


This deployment assumes the following:


   - You have Microsoft Entra ID as your IdP and have a directory with users and groups.


   - Your Entra ID has the licenses required for deploying conditional access policies.


   - You have the Prisma Browser Pro license.


   - Your organization has a Palo Alto Networks customer support account. If you do not have a support account, you can

[create one at the Customer Support Portal.](https://support.paloaltonetworks.com/Support/Index)


   - This guide also assumes that you have previously activated and configured Enterprise DLP as described in the

[Mitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide.](https://architectures.link/2147p-prime)

### VALIDATION ENVIRONMENT

At the time of writing, we used the following environment to validate this design:


   - Prisma Browser version 148.6.3.96


   - Microsoft Windows 11 clients


   - Prisma Browser Extension with Windows 11 Chrome and Edge browsers


   - MacOS Sequoia 15.7.5 clients


_Palo Alto Networks_ _9_


_Deployment Details_


## Deployment Details





This section guides you through the activation workflow and then the initial setup of the Cloud Identity Engine (CIE) and

Prisma Browser.


1.1 Activate Prisma Browser and CIE

For this procedure, you need the activation email that you received after you purchased Prisma Browser. To activate Prisma

Browser and any additional add-on licenses you have purchased, you use the Palo Alto Networks activation console.


Step 1: In your Prisma Access license activation email, click the highlighted link. Guided activation begins.


Step 2: After you log in to the activation console with your customer support account, in the row for Prisma Browser

Standalone, in the Action column, click Activate.


This procedure assumes that you will use the default tenant that was assigned to your Customer Support Portal account. If

necessary, you can rename the tenant after you complete the activation. You can also create a sub-tenant and then activate

Prisma Browser in the sub-tenant, but that is beyond the scope of this guide.


Step 3: In the Specify the Tenant list, accept the choice or your default tenant.


Step 4: In the Select Region list, choose your region (example: United States).


Step 5: After you review the terms and conditions, select Agree to the Terms and Conditions, and then click Activate

Now. The provisioning process begins.


_Palo Alto Networks_ _10_


_Deployment Details_


Step 6: After the provisioning process completes, verify that the status of the licensed product for the tenant is Active.

Next, you activate CIE.


Step 7: Continuing in the activation console, in the row for Cloud Identity Engine, in the Action column, click Activate.


Step 8: In the Specify the Tenant list, accept the choice or your default tenant.


Step 9: In the Select Region list, choose your region (example: United States - Americas).


Step 10: After the provisioning process completes, verify that the status of the licensed product for the tenant is Active.


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


_Palo Alto Networks_ _11_


_Deployment Details_


Step 2: Navigate to Home > Microsoft Entra ID.

First, you create the group.


Step 3: On the left, select Manage > Groups, and then click New Group.


Step 4: In the Group Name box, enter AI-access-permitted, and then click Create.

Next, you add members to the group.


Step 5: In the list of groups, click AI-access-permitted, and then on the left, select Manage > Members.


Step 6: Click Add Members.


Step 7: In the Add members pane, for each user that you want to assign to the group, select the row (example: amy or

chris), and then click Select.


Step 8: Review group membership to ensure it includes your example users.


1.4 Configure the CIE Authentication Profile to Microsoft Entra ID

In this procedure, you configure a Microsoft Entra ID SAML enterprise application, and then you configure CIE to use

Microsoft Entra ID for SAML authentication.


This procedure requires access to SCM, CIE, and the Azure portal.


First, you configure CIE.


Step 1: In SCM, at the bottom of the left navigation pane, click the user icon. The tenant navigation pane opens.


_Palo Alto Networks_ _12_


_Deployment Details_


Step 2: Under Available Apps, click Cloud Identity Engine.


Step 3: In Authentication > Authentication Types, click Add New Authentication Type.


Step 4: Under SAML 2.0, click Set Up.


Step 5: On the Set Up SAML Authentication page, in the Configure Cloud Authentication Service (CAS) as your SAML

Service Provider section, click Download SP Metadata.


_Palo Alto Networks_ _13_


_Deployment Details_


Step 6: Save the file for use later in this procedure (example: CAS-Metadata.xml).

Next, you configure Microsoft Entra ID.


Step 7: [In a new browser tab, log in to the Azure portal.](https://portal.azure.com/)


Step 8: In the search bar, enter and select Microsoft Entra ID.


Step 9: Navigate to Manage > Enterprise Applications.


Step 10: At the top of the page, click New Application.


Step 11: In the search box, enter Palo Alto Networks Cloud Identity Engine.


Step 12: Click Palo Alto Networks Cloud Identity Engine - Cloud Authentication Service.


Step 13: In the Name box, enter CIE - Cloud Authentication Service, and then click Create. Microsoft Entra ID adds the

application.


Step 14: In Microsoft Entra ID > Enterprise Applications > CIE - Cloud Authentication Service, under Manage, click

Single sign-on.


Step 15: In the single sign-on method pane, click SAML.


Step 16: At the top of the page, click Upload metadata file.


Step 17: In the Upload meta file window, click the browse icon.


Step 18: Navigate to the metadata file that you previously downloaded (example: CAS-Metadata.xml), and then click Add.


Step 19: In the Sign on URL box, enter https://cloud-auth.us.apps.paloaltonetworks.com/sp/acs


Step 20: Click Save, and then, to close the box, click X.


Step 21: In the Test Single Sign-On dialog box, click No, I'll test later.


Step 22: In the SAML Certificates pane, in the Federation Metadata XML row, click Download. It might take a few minutes

to create and download the XML file.


_Palo Alto Networks_ _14_


_Deployment Details_


Step 23: Save the file for use later in this procedure (example: CIE - Cloud Authentication Service.xml).


Next, you return to CIE to complete the configuration of the authentication type.


Step 24: Continuing in CIE, in the Configure your Identity Provider Profile section, in the Profile Name box, enter

example.com-entra_id-SAML.


Step 25: In the Identity Provider Vendor list, choose Entra Id.


Step 26: In the Add Metadata section, select Upload Metadata.


Step 27: Click Browse Files.


Step 28: Select the file you downloaded previously (example: CIE - Cloud Authentication Service.xml), and then click

Open.


Step 29: If your IdP has multi-factor authentication enabled, then enable Multi-factor Authentication is Enabled on the

Identity Provider.


Step 30: In the Test SAML and Attributes Section, click Test SAML Setup.

CIE performs a SAML authentication test. A window appears with the test results.


Step 31: If the test is successful, click Submit.

With Entra ID configured as an authentication type, you now create an authentication profile in CIE.

|Col1|Col2|Note|
|---|---|---|
|A deployment without client certificates uses the single authentication mode.|A deployment without client certificates uses the single authentication mode.|A deployment without client certificates uses the single authentication mode.|



Step 32: In CIE, under Authentication > Authentication Profiles, click Add Authentication Profile.


Step 33: In the Profile Name box, enter example.com-entra_id.


Step 34: In the Authentication Mode list, choose Single.


_Palo Alto Networks_ _15_


_Deployment Details_


Step 35: In the Authentication Type list, choose example.com-entra_id-SAML, and then click Submit.


1.5 Configure the CIE Connection to Entra ID Directory as a Read-Only Service

Using the directory sync service in CIE, you link SCM to your CIE in order to pull group mapping from Entra ID.


First, you retrieve the Microsoft Entra ID tenant ID.


Step 1: [Log in to the Azure portal.](https://portal.azure.com/)


Step 2: Click Microsoft Entra ID.


Step 3: On the Overview page, in the Basic Information section, copy the Tenant ID and record the value.

Next, you connect CIE to Microsoft Entra ID.


Step 4: In SCM, at the bottom of the left navigation pane, click the person icon. The tenant navigation pane opens.


Step 5: Under Available Apps, click Cloud Identity Engine.


Cloud Identity Engine opens in a new browser tab.


Step 6: On the Directories page, click Add New Directory. The Set Up Directory page appears.


Step 7: On the Set Up Directory page, under Cloud Directory, in the Set Up list, choose Entra ID.


Step 8: On the Configure Directory Sync for Entra ID page, in the Select Connection Flow section, expand the Advanced

Settings for Data Collection Permissions list and select Collect Roles and Administrators.


Step 9: In the Directory ID box, enter the Azure Entra ID Tenant ID that you recorded in Step 3.


Step 10: In the Check Connection Status pane, click Test Connection.


_Palo Alto Networks_ _16_


_Deployment Details_


Step 11: When the test completes successfully, under Customize Directory Name, in the Directory Name box, enter a

directory name, and then click Submit. This completes the connection.


Step 12: After the directory connects and synchronization completes, Sync Status displays Success.


1.6 Enable Prisma Browser

Now that you have configured CIE for both Directory Sync and authentication, you deploy Prisma Browser.


Step 1: In SCM, navigate to Configuration > Prisma Browser, and then click Enable Prisma Browser.


Step 2: On the Prisma Browser page, navigate to Administration > Onboarding.


Step 3: On the Users Page, under Authentication profile, select example.com-entra_id.


Step 4: Under User groups, in the Directory list, choose your Entra ID directory.


Step 5: In the User groups list, choose the user groups that will use Prisma Browser (example: Employees, Contractors).


_Palo Alto Networks_ _17_


_Deployment Details_


Step 6: At the bottom of the page, click Next: Private applications.

If necessary, you configure private application access later in this guide.


Step 7: Click Next: Enforce SSO applications.


Step 8: Expand the Configure your SSO enforcement section, and then click Shared IP addresses.


Step 9: In the Shared IP addresses box, click the copy icon, and then paste the IP addresses in a safe place. You must

have these IP addresses when you create a conditional access policy in Procedure 3.1.


Step 10: In the Identity Providers section, select Microsoft Azure Active Directory.

|Col1|Col2|Note|
|---|---|---|
|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|Ensure that you select your IdP provider in this step. If you do not, the authentication<br> traffic is not sent to the Prisma Browser proxy for use in conditional access policies.|



Step 11: Under Authentication traffic, enable the slider to Traffic is routed.


Step 12: Click Next: Download and distribute. On this page, you download the latest version of Prisma Browser or copy a

download link for the browser, depending on the browser distribution method for your organization.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.|You can also download Prisma Browser from thePrisma Browser self-service <br> installation page.||



Step 13: Click Next: Browser Policy.


Step 14: Click Browser Policy. Setup is complete.


_Palo Alto Networks_ _18_


_Deployment Details_





After the initial setup of Prisma Browser is complete, you create policies that customize the browser for your organization.

There are many ways to construct your policies to meet the needs of your organization. The following procedures serve as

a flexible starting point for how you can create policies. You can adopt the policies that align with your goals, mix and match

specific elements, or modify them entirely to fit your unique requirements.


In this deployment, you create access and data policies around managed and unmanaged devices and sanctioned, tolerated,

and unsanctioned applications. You also create specific AI policies that restrict access to AI applications to only users who

are in the AI-access-permitted group.


To protect data, these policies make use of _nested DLP profiles_, which are containers that can hold other data profiles. For

example, you can use nested data profiles to build a Global PII Protection policy by nesting the profiles for US PII, EU PII

General Data Protection Regulation, and APAC PII within it.


[For more information about DLP profiles and how to create them, see the Mitigating Data-Exfiltration Risk by Using](https://architectures.link/2147p-prime)

[Enterprise DLP: Solution Guide.](https://architectures.link/2147p-prime)


2.1 Create Device Groups

To apply policies to managed and unmanaged devices, you must first create device groups that define the criteria for each

category. In this example, managed devices are identified by their certificates. By uploading the issuer certificate, you enable

Prisma Browser to recognize managed devices. Any device lacking this certificate is automatically classified as unmanaged.


_Palo Alto Networks_ _19_


_Deployment Details_


This procedure assumes that your organization has a root certificate authority (CA) or an intermediate CA that issues and

signs device certificates for your managed devices. You must have a copy of the certificate for issuing CA in one of the

supported formats: PEM, CER, CRT or CER.


Step 1: In SCM, navigate to Configuration > Prisma Browser > Directory > Devices.


Step 2: On the Device Groups tab, click Add device group.


Step 3: Under Group name, enter Managed Devices.


Step 4: Under Platform, select Desktop Browser, and then click Next: Device group attributes.


Step 5: Select Issuer Certificate, and then click Add issuer certificate.


Step 6: Upload the issuer certificate that you use for your managed devices, click Set, and then click Create.


2.2 Create Application Groups

In order to define which applications are sanctioned or unsanctioned, you create application groups. You then use these

groups when creating policies. You should adjust sanctioned and unsanctioned applications according to your specific

business needs.


_Palo Alto Networks_ _20_


_Deployment Details_

|Col1|Col2|Note|Col4|
|---|---|---|---|
|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.|This guide assumes that your InfoSec admins have determined which applications<br> are sanctioned and unsanctioned for your organization. Using this information, you<br> explicitly map these applications into Prisma Browser application groups.<br>Any application that is not explicitly sanctioned or unsanctioned is assumed to be<br> tolerated and is not a member of the sanctioned or unsanctioned application groups.||



First, you create the sanctioned application group and you add specific example applications to the group.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Directory > Applications.


Step 2: On the Application Groups tab, click Add application group.


Step 3: In the Name box, enter Sanctioned Applications.


Step 4: In the Applications list, search for and choose Workday HCM and Salesforce Desk, and then click Save.


Next, you create the unsanctioned application group. In this example, you use Dropbox and WeTransfer as unsanctioned

applications.


Step 5: On the Application Groups tab, click Add application group.


Step 6: In the Name box, enter Unsanctioned Applications.


Step 7: In the Applications list, search for and choose Dropbox and WeTransfer, then click Save.


2.3 Create Block Unsanctioned and High-Risk Policy

First, you create the Block Unsanctioned and High-Risk Applications rule. This policy blocks all users from accessing any

unsanctioned application or website classified as high risk by Palo Alto Networks. This gives baseline protection from users

accessing malicious or poor security web sites. This policy applies to every device.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Policy > Rules.


_Palo Alto Networks_ _21_


_Deployment Details_


Step 2: In the Create list, choose New rule.


Step 3: In the Name box, enter Block Unsanctioned and High-Risk Applications.


Step 4: Under Rule Type, select Access & Data Control.


Step 5: Click Next: Scope.


Step 6: Click Next: Applications.


Step 7: Select Internet and SaaS applications.


Step 8: Select Custom.


Step 9: In the Website Classification list, search for and choose Risk level: High and Risk Level: Medium.


Step 10: Select Application groups.


Step 11: In the Select Application groups list, select Unsanctioned Applications.


Step 12: Click Next: Access.


Step 13: Select Block.


Step 14: Click Next: Tracking.


Step 15: Select On, click Save, and then click Save anyway.


2.4 Create the Managed Device Sanctioned Applications Policy

Next, you create the Sanctioned Applications (Managed) policy. This policy gives full access to trusted sanctioned

applications.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Sanctioned Applications (Managed).


Step 3: Under Rule Type, select Access & Data Control.


_Palo Alto Networks_ _22_


_Deployment Details_


Step 4: Click Next: Scope.


Step 5: In the Device groups list, choose Managed Devices.


Step 6: Click Next: Applications.


Step 7: Select Application groups.


Step 8: In the Select Application groups box, select Sanctioned Applications.


Step 9: Click Next: Access.


Step 10: Select Allow.


Step 11: Click Next: Login controls.


Step 12: Click Next: Controls and data profiles.


Step 13: At the top of the screen, click Control set: None.


Step 14: In the control set list, choose Allow full access, and then click Save.


2.5 Create the Managed Device Tolerated Applications Policy

Next, you create the Tolerated Applications (Managed) policy. This policy applies to all other sites accessed by managed

devices, it provides baseline protections and uses a nested DLP profile to protect sensitive data.


This policy uses a preconfigured nested Enterprise DLP profile in order to identify and protect sensitive data. For more

[information about Enterprise DLP and how to create profiles, see the Mitigating Data-Exfiltration Risk by Using Enterprise](https://architectures.link/2147p-prime)

[DLP: Solution Guide.](https://architectures.link/2147p-prime)


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Tolerated Applications (Managed).


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: In the Device groups list, choose Managed Devices.


Step 6: Click Next: Applications.


Step 7: Click Next: Access.


Step 8: Select Allow.


Step 9: Click Next: Login controls.


Step 10: Click Next: Controls and data profiles.


Step 11: On the Controls and data profiles page, click + Set data profile.


Step 12: On the Data profile side drawer pane, select Specific data profile.


_Palo Alto Networks_ _23_


_Deployment Details_


Step 13: For Select data profile, choose Nested-network-dlp-profile, and then click Save.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|For more information about Enterprise DLP and how to create nested policies, see<br> theMitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide.<br>On the Controls and data profiles page, selectFile Download.|For more information about Enterprise DLP and how to create nested policies, see<br> theMitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide.<br>On the Controls and data profiles page, selectFile Download.|For more information about Enterprise DLP and how to create nested policies, see<br> theMitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide.<br>On the Controls and data profiles page, selectFile Download.||



Step 14: In the File Download window, choose Block, and then click Set.


Step 15: Select File Upload.


Step 16: In the File Upload window, choose Block, and then click Set.


Step 17: Click Save.


2.6 Create the Unmanaged Device Sanctioned Applications Policy

Next, you create the Sanctioned Applications (Unmanaged) policy. This policy gives access to trusted sanctioned

applications, provides baseline protections through Advanced WildFire, and uses a nested DLP profile to protect sensitive

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


_Palo Alto Networks_ _24_


_Deployment Details_


Step 16: In the File Download window, choose Block, and then click Set.


Step 17: Select File Upload.


Step 18: In the File Upload window, choose Block, and then click Set.


Step 19: On the Controls and data profiles page, select Malicious File Protection.


Step 20: Select Enable.


Step 21: Under Action, select Prevent.


Step 22: In the Engine list, choose Advanced WildFire.


Step 23: Under Upon, select File Upload.


Step 24: Click Set, and then click Save.


2.7 Create the Unmanaged Device Tolerated Applications Policy

Next, you create the Tolerated Applications (Unmanaged) policy. This policy applies to any other applications that are not

explicitly listed in either the Sanctioned application group or the Unsanctioned application group and that are accessed by

unmanaged devices and blocks all files uploaded and downloaded through Prisma Browser.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Sanctioned Applications (Unmanaged).


_Palo Alto Networks_ _25_


_Deployment Details_


Step 3: Under Rule Type, select Access & Data Control.


Step 4: Click Next: Scope.


Step 5: Click Next: Applications.


Step 6: Click Next: Access.


Step 7: Select Allow.


Step 8: Click Next: Controls and data profiles.


Step 9: On the Controls and data profiles page, select File Download.


Step 10: In the File Download window, choose Block, and then click Set.


Step 11: Select File Upload.


Step 12: In the File Upload window, choose Block, and then click Set.


Step 13: Click Save, and then click Save anyway.


2.8 Create AI Policy

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


_Palo Alto Networks_ _26_


_Deployment Details_


Step 14: On the Controls and data profiles page, click + Set data profile.


Step 15: On the Data profile side drawer pane, choose Specific data profile.


Step 16: For Select data profile, choose Nested-network-dlp-profile, and then click Save.


Step 17: On the Controls and data profiles page, Select File Upload.


Step 18: In the File Upload window, choose Block, and then click Set.


Step 19: Select GenAI Prompt.


Step 20: Select Allow.


Step 21: Click Next: Tracking.


Step 22: Under GenAI Prompt, enable Prompt content, and then click Save.

Next you create an AI policy to block any user who is not in the AI-access-permitted group and on a managed device.


Step 23: In the Create list, choose New rule.


Step 24: In the Name box, enter AI Access Denied.


Step 25: Under Rule Type, select Access & Data Control.


Step 26: Click Next: Scope.


Step 27: Click Next: Applications.


Step 28: Select Internet & SaaS applications, and then select Custom.


Step 29: In the Website Classification list, search for and choose Artificial Intelligence.


Step 30: Click Next: Access.


Step 31: Select Block, and then click Save.


2.9 Organize and Adjust Policy Rules

In this procedure, you create sections in order to organize your policies and arrange them in the correct evaluation sequence.

Proper ordering is critical: if a rule is placed incorrectly, it might trigger prematurely and prevent subsequent policies from

being processed.


The following image details the correct order of the policies.


_Palo Alto Networks_ _27_


_Deployment Details_


_Figure 2_ _Policy priority_


Step 1: Continuing on the Policy Rules page. In the Create list, choose New section.


Step 2: For Section name, enter AI Policy, and then click the blue checkmark.


Step 3: To create Managed Devices and Unmanaged sections, repeat Step 1 and Step 2 for each section.


Step 4: Click Change Priority.


Step 5: Drag and drop policies into their corresponding sections and reorder them as shown in Figure 2. When you're done,

click Save changes.


_Palo Alto Networks_ _28_


_Deployment Details_


2.10 Create Browser Security Policy to Enforce Best Practices

Next, you create a Browser Security policy. This policy uses the pre-configured control set Restricted Browser in order to

reduce the browser attack surface, perform browser hardening, enable network protection to block web pages with SSL

errors or with insecure content, and enforce strict control of password saving and autofill data.


Step 1: Continuing on the Policy Rules page, in the Create list, choose New rule.


Step 2: In the Name box, enter Secure Browser.


Step 3: Under Rule Type, select Browser Security, and then click Next: Scope.


Step 4: Click Next: Browser Security controls.


Step 5: At the top of the page, click Control set : None, and then select Restricted Browser.


Step 6: Click Save, and then click Save anyway.


2.11 Create Browser Customization Policy to Ensure Latest Version

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


Step 8: Replace the example IP ranges with the IPs copied in Procedure 1.6, Step 9.


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


4.1 Create a Policy to Redirect the Prisma Browser Extension to Prisma Browser

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


Step 3: On the Step 5 Download and distribute page, expand the Deploy Prisma Browser Extension pane.


Step 4: In the Identity provider (IdP) list, choose Azure.


Step 5: In the Device management list, choose Manual Deployment (Locally).


Step 6: In the Browser list, select Chrome, and then click Generate.


Step 7: Verify that the Login domain(s) settings include your FQDN (example: test-example.com).


Step 8: Expand the Windows pane.


Step 9: If you are testing on an unmanaged device, select Apply testing mode adaptations.


Step 10: To download the extension configuration, click Download .reg file.


Step 11: When prompted, save the file to your local system and note the file name and location.


4.3 Install the Prisma Browser Extension

In this procedure, you use a registry modification file to install the Prisma Browser Extension for Chrome on a Windows

system.


This procedure assumes that the Prisma Browser is already installed.


Step 1: On the Windows system where you intend to install the Prisma Browser Extension, copy the file you downloaded

previously in Procedure 4.2, Step 11.


Step 2: To make registry changes, double-click the copied .reg file.


Step 3: Launch Chrome and navigate to chrome://policy, and then click Reload policies.


Step 4: On the Chrome toolbar, click the extensions symbol and in the row for Prisma Browser Extension, click the

thumbtack icon to pin the extension.


_Palo Alto Networks_ _37_


_Deployment Details_


Step 5: Click the Prisma Browser Extension. The extension pane appears.


Step 6: Click Log in.


Step 7: In the Enter your work or school account box, enter your user ID (example: brian@test-example.com), and then

click Continue.


Step 8: If your user ID is associated to multiple Prisma Browser tenants, click the preferred tenant.


_Palo Alto Networks_ _38_


_Deployment Details_



Step 9: When prompted, enter the password.


Step 10: Click Continue browsing.





_Palo Alto Networks_ _39_


_Deployment Details_


The procedures in this section are optional unless you have private applications. To enable private application access, you

must configure Prisma Browser Connector to allow access to these applications.


In this setup you configure two ZTNA connectors that are assigned to the same connector group for redundancy. The

configuration includes two applications, one web-based and one non-web-based (SSH).


5.1 Create the ZTNA Connectors

First, you create the ZTNA Connectors in SCM and assign them to a group.


Step 1: In SCM, navigate to Configuration > ZTNA Connector.


Step 2: Click Enable ZTNA Connector.


Step 3: On the Connector Groups tab, click Create Connector Group.


Step 4: In the Name box, enter Example DC-01, and then click Create.


Step 5: On the Connectors tab, click Create Connector.


Step 6: In the Name box, enter DC01-Connector-1.


_Palo Alto Networks_ _40_


_Deployment Details_


Step 7: In the Connector Group list, choose Example DC-01, and then click Create.


Next, create a second connector for redundancy.


Step 8: On the Connectors tab, click Create Connector.


Step 9: In the Name box, enter DC01-Connector-2.


Step 10: In the Connector Group list, choose Example DC-01, and then click Create.


5.2 Create Application Targets

Next, create application targets for the applications you wish to reach through PB Connector. In this example you use FQDN

Targets to define the applications.


_Table 2 Example applications_

|Name|Connector group|FQDN|TCP port|Probing port|
|---|---|---|---|---|
|Example app01|Example DC-01|app01.example.com|80,443|80|
|Example app02|Example DC-01|app02.example.com|22|22|



Step 1: Continuing in SCM, navigate to Configuration > ZTNA Connector.


Step 2: On the FQDN Targets tab, click Create FQDN Target.


Step 3: In the Name box, enter Example app01.


Step 4: In the Connector Group list, select Example DC-01.


Step 5: In the FQDN box, enter app01.example.com.


Step 6: In the TCP Port box, enter 80,443.


_Palo Alto Networks_ _41_


_Deployment Details_


Step 7: In the Probing Port box, enter 80, and then click Create.


Step 8: Repeat this procedure for Example app02.


5.3 Deploy ZTNA Connectors

Depending on your datacenter or private cloud environment, you may deploy the ZTNA Connector VMs from a cloud provider

[marketplace or an image downloaded from the Customer Support Portal. The ZTNA Connector VM must have network](https://support.paloaltonetworks.com/)

reachability to the private applications it is protecting, as well as access to a DNS server capable of resolving application

hostnames to their local IP addresses. Additionally, the connector requires outbound internet connectivity to establish and

maintain its tunnel to Prisma Access.


The "Securing Private Applications for Mobile Users by Using ZTNA Connector" reference architecture includes full design

and deployment details for the ZTNA Connector in the most common datacenter and private cloud environments.


Step 1: Deploy your ZTNA Connector VMs as described in the "Deploy ZTNA Connectors" section in the relevant guide for

your environment:

   - [Securing Private Application Access with ZTNA Connector in AWS: Deployment Guide](https://architectures.link/2042p-prime)


   - [Securing Private Application Access with ZTNA Connector in Azure: Deployment Guide](https://architectures.link/2044p-prime)


   - [Securing Private Application Access with ZTNA Connector in VMware vSphere: Deployment Guide](https://architectures.link/2047p-prime)


_Palo Alto Networks_ _42_


_Deployment Details_


After the VM boots up and registers with SCM, it creates a secure tunnel to the Prisma Browser Connector. When

established, the Tunnel and Control Plane columns display a status of Up.


5.4 Configure Private Applications for Prisma Browser

In order to assign policies to the applications, you must define them as private applications in Prisma Browser.


Step 1: In SCM, navigate to Configuration > Prisma Browser > Applications > Private Applications.


Step 2: Click Add private app.


Step 3: In the Name box, enter Example app01.


Step 4: In the FQDN or IP Address box, enter app01.example.com, and then click Add.


Step 5: At the bottom of the pane, click Add.


_Palo Alto Networks_ _43_


_Deployment Details_


5.5 Configure Remote Connections for Non-Web Apps

Next, you define app02 as an SSH remote connection.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Applications > Remote Connections.


Step 2: Click Add remote connection.


Step 3: In the Name box, enter Example app02.


Step 4: In the FQDN/IP Address box, enter app02.example.com.


Step 5: In the Protocol list, choose SSH.


Step 6: In the Port box, enter 22, and then click Add.


5.6 Add Applications to Applications Group

Next you add the applications to the Sanctioned application group to inherit the security policies.


Step 1: Continuing in SCM, navigate to Configuration > Prisma Browser > Applications > Application Groups.


Step 2: Next to Sanctioned Applications, click the pencil icon.


Step 3: In the Applications list, search for and select Example app01 and Example app02, and then click Add.


Step 4: At the top right of the screen click Review changes, click Next, and then click Publish.


_Palo Alto Networks_ _44_


_Deployment Details_


## Feedback

[You can use the feedback form](https://www.paloaltonetworks.com/resources/reference-architectures/feedback-ra?guid=2071p-16062026) to send comments about this guide.


_Palo Alto Networks_ _45_


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


P-2071P-16062026



**DESIGN GUIDE**

# Securing Internet and Private Applications by Using Prisma Browser

#### **JUNE 2026**


_Table of Contents_

## Table of Contents


Preface......................................................................................................................................................................................................... 3

Purpose of This Guide................................................................................................................................................................................5

Audience..............................................................................................................................................................................................5

Related Documentation........................................................................................................................................................................6

Introduction..................................................................................................................................................................................................7

Security Challenges............................................................................................................................................................................. 7

Essential Capabilities............................................................................................................................................................................7

Design Overview.................................................................................................................................................................................. 8

Palo Alto Networks Design Details.......................................................................................................................................................... 10

Prisma Browser................................................................................................................................................................................. 10

Components...................................................................................................................................................................................... 11

Interacting with IDPs..........................................................................................................................................................................12

Security Functions............................................................................................................................................................................. 13

Browser Policy...................................................................................................................................................................................18

Private Application Access with Prisma Browser Connector..............................................................................................................20

Prisma Browser Mobile App and Browser Extension.........................................................................................................................21

Browser Enforcement........................................................................................................................................................................ 22

Browser Distribution...........................................................................................................................................................................24

Licensing............................................................................................................................................................................................24

System Requirements........................................................................................................................................................................25

Design Model.............................................................................................................................................................................................26

Summary.................................................................................................................................................................................................... 28

Feedback....................................................................................................................................................................................................29


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


This guide provides architectural guidance and discusses decision criteria for using Palo Alto Networks [®] Prisma [®] Browser in

order to achieve an integrated design. This reference architecture guide provides you with a framework for securely accessing

applications from end-user devices, providing security and visibility for your workforce.

### AUDIENCE

This guide is for technical readers, including system architects and security engineers, who want to secure access to their

internet and private applications. You should be familiar with the basic concepts of applications, networking, routing, and

security. To be successful, you should also have a basic understanding of internet architectures.


_Palo Alto Networks_ _5_


_Purpose of This Guide_

### RELATED DOCUMENTATION

This guide supports the following:


   - [Securing Internet and Private Applications by Using Prisma Browser: Deployment Guide—Provides](https://architectures.link/2071p-prime)

implementation details for securely accessing internet and private applications by using Prisma Browser and Prisma

Browser Connector. Includes high-level tasks and step-by-step configuration details for browser-native protections,

including last-mile controls, Enterprise DLP, and cloud-delivered security services across managed and unmanaged

devices.


   - [AI-Powered Autonomous Digital Experience Management: Solution Guide—Provides design, deployment, and](https://architectures.link/107p-prime)

operational guidance for integrating AI-Powered ADEM with the Palo Alto Networks Prisma SASE solution.


   - [Secure Internet Policy Design: Solution Guide—Provides policy design and deployment guidance for securing](https://architectures.link/2150p-prime)

internet services by using the Prisma Access cloud-delivered security platform and Palo Alto Networks next
generation firewalls.


   - [Mitigating Data-Exfiltration Risk by Using Enterprise DLP: Solution Guide—Provides design and deployment](https://architectures.link/2147p-prime)

guidance for delivering comprehensive data security by using Enterprise DLP.


_Palo Alto Networks_ _6_


_Introduction_

## Introduction


The browser is the main gateway for today's workforce. From cloud-based SaaS platforms to internal tools, it is how users

access applications and interact with sensitive data. However, as the browser's role in daily operations has grown, so has its

appeal as a primary target for cyberattacks. Because traditional network security tools were not designed to natively secure

the browser, they can leave your environment unintentionally exposed to advanced threats and data leakage.

### SECURITY CHALLENGES

To secure your modern workspace, you must overcome several critical challenges:


   - Browser-based threats—Adversaries increasingly use stolen session cookies to hijack authenticated web sessions,

bypassing your multi-factor authentication (MFA) controls entirely. Furthermore, AI-assisted phishing campaigns and

malicious extensions can silently compromise active web sessions.


   - The decryption dilemma—Gaining meaningful visibility at the network layer requires Secure Sockets Layer/Transport

Layer Security (SSL/TLS) decryption. Because SSL/TLS inspection can degrade performance and break applications,

system constraints often force you to bypass decryption for certain traffic. This unintentionally creates baseline

security blind spots.


   - Lack of application context—Even when traffic is decrypted, traditional network inspection often lacks deep, real
time presentation context. It can be difficult to differentiate between a user routinely viewing a single customer record

and maliciously exporting a highly sensitive database.


   - Data leakage and shadow IT—Without controls directly at the browser level, you lack visibility into unintentional data

leakage, such as users pasting proprietary data into unsanctioned generative AI (GenAI) applications.

### ESSENTIAL CAPABILITIES

Because legacy network tools cannot fully inspect or control web interactions, your secure-access solution must include the

following capabilities:


   - Provide real-time protection from browser-based threats and vulnerabilities


   - Deliver deep visibility into user actions without requiring network decryption


   - Prevent the exfiltration or leakage of sensitive data across any device


   - Secure unmanaged, bring-your-own-device (BYOD), and third-party access without requiring complex, system-level

device management agents


   - Operate transparently without compromising the user's efficiency or device performance


_Palo Alto Networks_ _7_


_Introduction_

### DESIGN OVERVIEW

When planning to secure web access and protect sensitive data across managed and unmanaged devices, an organization

must identify their critical web applications, data locations, and remote user footprint. With this information, they can use

security capabilities from Palo Alto Networks in order to secure web access and protect sensitive data across managed and

unmanaged devices.


Prisma Browser is a secure enterprise browser specifically designed to protect your environment from cyber threats while

providing your users with a familiar, seamless experience. By making Prisma Browser your security edge, you extend your

security stack directly to the primary user workspace.


Prisma Browser gives you unprecedented control by embedding security where the work actually happens. Because it serves

as the presentation layer, it natively inspects web sessions, file transfers, and extension behaviors in full context, without

the need for network interception or decryption. With this depth of visibility, your security team can easily audit application

access, control how data moves, and ensure sensitive information stays where it belongs. Prisma Browser, along with other

Palo Alto Networks applications and services, enables you to secure access from any device.


_Figure 1_ _Prisma Browser design overview_


_Palo Alto Networks_ _8_


_Introduction_



This design includes the following components:


   - Prisma Browser


   - Prisma Browser Connector


   - Strata [™] Cloud Manager (SCM)


   - Strata Logging Service (formerly known as _Cortex_ _[®]_ _Data Lake_ )


   - Enterprise DLP


   - Cloud Identity Engine (CIE)


The next section contains more detailed information about these components and their capabilities.


_Palo Alto Networks_ _9_


_Palo Alto Networks Design Details_

## Palo Alto Networks Design Details


Securing your modern workforce requires shifting the protective edge directly to where work happens: the browser. This

architecture integrates your identity management, cloud-delivered security services, and native browser controls to establish

a highly visible, zero-trust workspace. By adopting this design, you can seamlessly protect sensitive data and applications

across any device, all while maintaining the fast, native web experience your users expect.

### PRISMA BROWSER

The Palo Alto Networks Prisma Browser is a secure enterprise browser designed to protect against web threats, data loss,

and unauthorized access.

##### **Secure Workspace**

Prisma Browser transforms any endpoint into a secure enterprise workspace, regardless of location or device. Built

specifically for security, the browser significantly reduces your attack surface by disabling vulnerable engines and preventing

the installation of malicious extensions. This proactive approach tightly controls access and secures your data.


Users must authenticate before accessing the browser. This ensures the workspace and its underlying data remain securely

tied to a verified identity and your MFA policies. To enforce a strict boundary between local device activity and your sensitive

corporate data, the browser comprehensively encrypts all local assets. This isolates your information from malware, such

as infostealers and screen-scrapers, that target access tokens, cookies, and credentials. Even if an unmanaged device is

compromised, lost, or stolen, the sensitive data inside the browser remains inaccessible to the underlying operating system.


Built on Chromium, Prisma Browser offers your users a familiar experience with no learning curve. They can seamlessly

transfer settings from their personal browsers, customize their homepage with application shortcuts, and synchronize

their profiles across devices. To further streamline the user experience, a secure, built-in password manager safely stores

credentials and auto-fills logins, while single sign-on (SSO) integration ensures a fast and straightforward setup.

##### **Edge Benefits**

Shifting the security edge directly to the browser fundamentally transforms how you protect data and empower your

workforce. By positioning security exactly where users interact with applications, you unlock powerful capabilities that

traditional network security architectures simply cannot match. Because the browser serves as the presentation layer,

it natively renders content in clear text. This gives your security team instant, deep visibility into user activity without the

complexity and performance hit of decrypting network traffic.


This native visibility extends far beyond basic access logs. Unlike traditional perimeter security, which only recognizes that a

user navigated to an application, edge-level visibility captures specific in-app actions. This provides a transparent audit trail

that details exactly how your users handle sensitive data at any given moment.


As the final enforcement point between the user and your data, the browser enables highly precise, "last-mile" access

controls. You can dynamically restrict specific interactions by disabling functions such as copy and paste, printing, screen

sharing, or file downloads. This granular control naturally extends to real-time data-loss prevention (DLP). Instead of


_Palo Alto Networks_ _10_


_Palo Alto Networks Design Details_


discovering a leak during a post-incident review, you can instantly enforce policies to detect and block the transfer of

sensitive information, such as personally identifiable information (PII) or intellectual property. You can even instantly block

users from pasting proprietary data into external GenAI tools.


Beyond these robust security controls, placing the edge in the browser improves the user experience. Prisma Browser routes

traffic directly to the application, eliminating the need to backhaul traffic through VPNs or rely on the pixel-streaming of virtual

desktop infrastructure (VDI) environments. This direct routing gives your employees the lightning-fast, native web experience

they expect.

##### **Access Without Boundaries**

Prisma Browser gives you the ability to securely connect any device to any web application, whether public or private, entirely

through the browser. You can also use Prisma Browser to access non-web remote connections, such as SSH and remote

desktop protocol (RDP).


This flexibility makes Prisma Browser a natural fit for a wide range of scenarios beyond standard access controls and insights:


   - Employee BYOD—Securely enable your teams to use their own devices


   - Contractor onboarding—Grant fast, secure access to external workers without the need for VDI


   - Mergers and acquisitions—Quickly connect newly acquired users without overhauling infrastructure


   - VPN replacement—Eliminate the need for VPN infrastructure and upkeep


   - Asset-light deployments—Remove the logistical hassle of issuing corporate hardware for smaller teams


In every case, Prisma Browser makes it simple: just install the browser and get to work. There are no agents, no VPNs, and

no hardware to ship.

### COMPONENTS

##### **Strata Cloud Manager and Strata Logging Service**

Strata Cloud Manager (SCM) is a cloud-based, multi-region management solution that administrators use to configure and

manage Prisma Browser. SCM is responsible for pushing the appropriate policy to the browsers, based on user and device

posture. SCM keeps Prisma Browser installations up-to-date with the latest patches and policies. It also offers administrators

deep visibility into their Prisma Browser deployment, along with monitoring of user activity.


Prisma Browser sends log data to Strata Logging Service (SLS). Administrators can review log data in the SCM console.

These logs offer detailed insights into user actions, including the specific websites visited, login attempts, file downloads or

uploads, clipboard events, printing, and more. This detailed information equips IT personnel with a deep understanding of

user behavior and creates an audit trail that is invaluable for incident response.


_Palo Alto Networks_ _11_


_Palo Alto Networks Design Details_

##### **Identity Provider**

An _identity provider_ (IdP) is a service that stores and manages digital identities. To authenticate and authorize users access

to the browser, Prisma Browser authenticates against an IdP. Organizations also use the IdP to configure conditional access

policies that force users to access applications through Prisma Browser.

##### **Cloud Identity Engine**

Palo Alto Networks CIE is a cloud-based service designed to simplify and enhance identity and access management for

organizations. CIE consists of two core components: Directory Sync and Cloud Authentication Service. The Prisma Browser

solution leverages both.


Directory Sync is a secure, cloud-based infrastructure that provides Palo Alto Networks apps and services with read-only

access to directory information. This information allows you to define the directory and the users and groups who have

access to Prisma Browser.


Cloud Authentication Service acts as an authentication broker between the IdP and Palo Alto Networks apps and services. It

allows you to integrate CIE with your IdP, which Prisma Browser uses to authenticate users who are logging into the browser.

##### **Enterprise DLP**

Palo Alto Networks Enterprise DLP enables you to create a data protection framework. The solution separates cloud
based policy and analysis functions from local traffic inspection and enforcement. Prisma Browser actively executes these

enforcement functions directly at the edge of your enterprise network.


Enterprise DLP is a cloud-native platform where you define and manage the data protection strategy. You can create

data patterns, configure data profiles, and define policies on the console. Enterprise DLP includes multiple data detection

methods, such as machine learning-based classifiers, optical character recognition (OCR), exact data matching (EDM), and

indexed document matching (IDM).


Prisma Browser enforces data controls natively at the browser layer, where every user action is fully visible in context. This

comprehensive visibility enables granular last-mile controls. Organizations can define precise policy for file uploads and

downloads, copy and paste actions, printing, screenshots, and more, and apply that policy at the exact moment a user

interacts with data.

### INTERACTING WITH IDPS

Prisma Browser does not maintain its own user directory or authentication system. Instead, it integrates with your existing

IdP through Palo Alto Networks’ CIE, which acts as the broker between your IdP and the browser. This design means Prisma

Browser fits into your established identity governance model rather than creating a parallel one. Users authenticate with the

same credentials they already use, and group membership is inherited from systems your team already manages.


**Supported Identity Providers**

Prisma Browser supports most major identity providers, including Microsoft Entra ID, Okta, and Google. For proof-of-concept

evaluations or demo environments, you can use a local CIE directory to onboard a small set of test users.


_Palo Alto Networks_ _12_


_Palo Alto Networks Design Details_


**Authentication Methods**

CIE for Prisma Browser authentication supports three authentication methods you can use to sign users into the browser:

SAML 2.0, OpenID Connect (OIDC), and password authentication against a local CIE directory. For most organizations, the

practical choice is between SAML 2.0 and OIDC. SAML remains the most common option for established enterprises and

offers the broadest IdP coverage, while OIDC is a modern, token-based alternative often preferred for newer integrations.

Both deliver the same end-user experience, and the decision is largely a matter of organizational preference. Local CIE

password authentication supports proof-of-concept evaluations and demo environments.


**Group-Based Policy Enforcement**

User groups synchronized from your IdP into CIE become directly available for use in Prisma Browser policy rules. This allows

security teams to scope access control, data control, and browser hardening policies to specific populations. For example,

applying stricter download restrictions to finance teams, limiting AI tool usage for contractors, or enabling developer tooling

only for engineering. Because the IdP serves as your single source of truth for group membership, policy targeting stays

automatically aligned with role changes, terminations, and organizational restructuring without requiring manual updates

inside the browser console.

### SECURITY FUNCTIONS

Prisma Browser combines several powerful security functions to actively protect your corporate resources. Because the

browser inherently understands the applications your users access and the posture of their devices, it empowers your

security team to enforce highly precise, differentiated controls. This foundational visibility drives the following advanced

security capabilities, ensuring only compliant devices can access your sensitive data.


_Figure 2_ _Security functions in Prisma Browser_

##### **Visibility and Insights**

When a security incident occurs, traditional network logs often fall short. The logs might confirm that a user logged into a

SaaS application, but they cannot tell you what the user actually did in that application. Did the user simply view a sensitive

record, or did they copy its contents, print it, or upload it to an unsanctioned GenAI tool? Without visual evidence and

granular activity tracking, your security team is forced to make assumptions, which slows down incident response and leaves

dangerous compliance gaps.


_Palo Alto Networks_ _13_


_Palo Alto Networks Design Details_


Prisma Browser solves this by capturing rich, contextual data directly from the workspace, without requiring complex network

decryption. It logs deep analytics for every web action, tracking everything from basic web navigation and login attempts to

clipboard events, file downloads, and developer tool usage.


To manage these insights, you can specify activity logging levels for each policy rule. For highly sensitive applications, you

can enable enhanced logging to capture screenshot evidence, or even configure session recording to capture full browsing

activity, including clicks, scrolling, and typing.


_Figure 3_ _Prisma Browser logs_


SCM transforms raw logs into actionable intelligence. When investigating an incident, your team can use the SCM

investigation pane to view a time-indexed canvas of all accessed sites and their related visual evidence. You can quickly

filter events to construct a precise timeline of a user's in-app actions. Additionally, SCM automatically identifies and groups

application usage by type and risk, instantly highlighting the high-risk shadow IT and GenAI apps your users are accessing.


_Figure 4_ _GenAI application filters_


**ADEM**

When users experience slow load times or application errors, your IT and helpdesk teams often struggle to identify the root

cause. Traditional network monitoring tools lack visibility into the endpoint and the specific application transaction, making

it difficult to determine whether a performance issue stems from the user's local Wi-Fi, a device resource constraint, or the

application itself. This blind spot leads to prolonged troubleshooting and frustrated employees.


_Palo Alto Networks_ _14_


_Palo Alto Networks Design Details_


To solve this, Autonomous Digital Experience Management (ADEM) integrates directly into Prisma Browser as an

extension. This integration adds an essential layer of visibility by capturing browser-based real-user monitoring (RUM) data

based on actual user interactions in real time. Because the browser is the final rendering point, RUM data provides your team

with genuine insight into how your users experience internet-based and private applications.


[For more information about ADEM and RUM data, see the AI-Powered Autonomous Digital Experience Management:](https://architectures.link/107p-prime)

[Solution Guide.](https://architectures.link/107p-prime)

##### **Access Controls**

When you grant users static, permanent access to applications and data, it expands your organization's attack surface.

Security teams using traditional binary controls (simply allowing or blocking access entirely) must choose between enforcing

strict least-privilege policies and maintaining user productivity.


Because Prisma Browser provides comprehensive visibility of all browser activity, it enables a dynamic, end-to-end Zero Trust

security model. This gives your team full control over all activity, allowing you to enforce least-privilege access to applications

and their underlying data. You can create highly granular security policies based on contextual factors such as user identity,

device posture, location, time, and network.


To further balance security and productivity, Prisma Browser allows for just-in-time (JIT) controls. With these controls you

can grant users temporary access rights to resources for only a specified amount of time. When you use this approach, it

drastically reduces the risk associated with permanent privileges by actively shrinking your attack surface.


You can configure JIT controls by using one of the following three methods, each of which prompts the user before they can

continue:


   - Warn and allow—Informs the user about the risks and sensitivity and allows access.


   - Warn and allow to proceed with a reason—Informs the user about the risks and sensitivity and requires the user to

enter a business justification to continue.


   - Permission request—Requires the user to send a permission request to an admin in order to gain access. The

admin approves or denies the requested access, and then the user is notified of the outcome.

##### **Palo Alto Networks Cloud-Delivered Security Services**

Even within a secured workspace, your users constantly face evasive phishing campaigns, compromised websites, and zero
day malware that can bypass traditional, signature-based network defenses.


To actively protect your users from these dynamic web threats, Prisma Browser natively integrates with Palo Alto Networks

cloud-delivered security services (CDSS). Powered by AI and machine learning, this comprehensive suite of cloud-based

protections analyzes web interactions directly at the browser edge, enabling you to detect and stop evasive threats in real

time without degrading the user experience.


_Palo Alto Networks_ _15_


_Palo Alto Networks Design Details_


This cloud-delivered protection relies on two key services:


   - Advanced URL Filtering—Provides real-time safe browsing by combining machine learning with the PAN-DB

advanced URL database to analyze content as users navigate the web. This acts as a proactive, invisible shield. It

stops phishing and scams by instantly blocking malicious pages from loading if a user accidentally clicks a deceptive

link, and it prevents drive-by threats by restricting access to compromised websites.


   - Advanced WildFire—Offers seamless protection against malicious downloads. As a cloud-based threat analysis

service, it uses machine learning to discover unknown, zero-day malware. For your browser, it serves as an

automated quarantine zone. It secures downloads by analyzing files in a secure cloud environment before they are

allowed to save or execute locally. When WildFire [®] detects a new threat globally, it immediately updates its defenses,

ensuring your browser automatically learns to block that exact threat moving forward without requiring manual

updates.

##### **Last-Mile Controls and DLP**

When sensitive data renders on a user's screen, traditional network security tools lose visibility. They cannot prevent a user

from copying text, taking a screenshot, or printing a confidential document.


To close this gap, Prisma Browser enforces data controls natively at the presentation layer, "last mile." Because every user

action is fully visible in context, you can define precise policies governing file transfers, copy and paste actions, printing, and

screen sharing. These highly granular controls are applied at the exact moment your user interacts with the data, preventing

data leakage before it happens.


If your environment requires advanced data security, Prisma Browser integrates seamlessly with Palo Alto Networks

Enterprise DLP. This integration provides a unified data protection strategy in which your team can reuse the exact same data

profiles across the browser, NGFWs, and endpoint DLP.


This integration augments the browser's native capabilities with a detection engine that is significantly richer than the

standard regular expressions used by baseline data controls. It provides you with EDM, IDM, OCR, and ML-based classifiers

that extend far beyond standard regular expressions. Designed for complex compliance environments, this powerful

integration also equips your security team with an ability to conduct deep forensic investigations. Table 1 provides examples

of the DLP controls that are available to administrators.


_Table 1 DLP controls_






|Data protection|Description|
|---|---|
|Download, upload,<br>and print|Prevents users from saving sensitive documents to unmanaged local drives, exfiltrating data to personal<br>clouds, or printing to unauthorized physical locations.|
|File encryption for<br>downloaded files|Encrypts downloaded files and makes them viewable only from sanctioned devices.|
|Screenshot<br>prevention|Controls whether users can take screenshots, print the screens, and record or share the screen with video<br>conferencing tools.|



_(Table 1 continues on the following page)_


_Palo Alto Networks_ _16_


_Palo Alto Networks Design Details_


_Table 1 (continued)_







|Data protection|Description|
|---|---|
|Data masking|Allows for masking textual content within web pages. You can configure the masking with either predefined<br>information types, such as personally identifiable information and payment card industry, or a custom regular<br>expression. When you enable data masking, the browser inspects and masks data that a user types into any<br>field within the webpage.|
|Typing Guard|Analyzes what a user enters into a web form in real time. If Typing Guard detects sensitive information, it<br>secures that information from exposure by stripping it before allowing the webform submission to proceed.<br>You can customize this behavior and notify users based on your specific security requirements.|
|Webpage<br>watermarking|Overlays a dynamic, identifiable watermark on webpages. A watermark acts as a deterrent against physical<br>circumvention, such as a user attempting to photograph the screen with a mobile device.|
|Clipboard|Controls copy and paste functions. You can restrict the user's ability to copy and paste sensitive content to<br>and from a browser or other apps.|
|Read-only webpage|Configures read-only mode for webpages.|
|Camera|Controls access to the device's camera.|
|Microphone|Controls access to the device's microphone.|

##### **Live Page Scanning**

To bypass perimeter defenses, attackers frequently fragment their malicious code so that it assembles only at runtime,

directly inside the user's browser. They also hide threats behind CAPTCHAs or route them through encrypted channels to

steal data or compromise systems. To counter these highly evasive attacks, Prisma Browser provides live page scanning

capability to seamlessly analyze content live as it renders. It detects and blocks fragmented malicious scripts as they attempt

to assemble, neutralizes cloaked phishing attempts at the exact moment of user interaction, and inspects dynamic traffic

streams like WebSockets directly within the browser. This equips your users with real-time protection against stealthy in
browser threats before they can cause data loss or system disruption.

##### **Device Posture Check**

Even with strong user authentication, allowing access to corporate data from unpatched or unprotected devices introduces

significant risk. If an endpoint is compromised, valid credentials are not enough to protect your environment.


To solve this, Prisma Browser enables you to enforce continuous device-posture checks in order to ensure the device

running the browser is compliant . You can define what constitutes a healthy endpoint by creating device groups based on

attributes such as the operating system, serial numbers, and active endpoint protection status.


Rather than checking compliance only at the initial login, Prisma Browser periodically analyzes the device—typically every

90 seconds. If an endpoint falls out of compliance during a session, the browser immediately blocks further interaction,

preventing compromised devices from maintaining access to your applications and data.


_Palo Alto Networks_ _17_


_Palo Alto Networks Design Details_

### BROWSER POLICY

You enable and configure Prisma Browser features through centralized policies. These policies allow you to control security

functions from basic browser customization to deep-data protection measures across your entire workforce.

##### **Policy Rule Types**

Prisma Browser policies fall into three separate categories: access and data control, browser security, and browser

customization.


**Access and Data Control**

Access and data control policies regulate how your users interact with web resources by managing access permissions and

security mechanisms. For each rule, you can configure settings for data leak prevention, threat protection, and webpage

element customization.


When configuring these rules, you have the option of selecting a specific log level for the policy:


   - Off—Does not log user actions.


   - Anonymized—Logs user actions without personal data.


   - On—Logs user actions including personal data.


   - Enhanced—Logs user actions including personal data and includes screenshot of the end-user's active tab at the

time of the activity.


In addition, you can configure screen recording in order to capture full browsing activity (including clicks and typing) within

specified applications. The browser automatically stops the recording after a period of user inactivity.


**Browser Security**

Browser security policies strengthen your defenses and reduce your attack surface by giving you comprehensive control over

the browser's behavior. For each security rule, you can configure settings for browser hardening, passwords and autofill,

network protection, extensions, and privacy. For example, you can manage allowed extensions, disable vulnerable APIs,

guard against keyloggers, and enforce network safeguards such as mandating HTTPS or blocking pages with SSL certificate

errors.


**Browser Customization**

Browser customization policies enable you to tailor the browser for your organization. For each customization rule, you

can dictate settings for corporate branding, interface customization, traffic routing, default home pages, and upgrade

management.


**Controls Sets**

Configuring complex security and management settings for every individual policy rule is repetitive and increases the risk of

configuration drift. To streamline management, SCM provides Controls Sets, which allow you to bundle configurations into

reusable templates.


_Palo Alto Networks_ _18_


_Palo Alto Networks Design Details_


SCM includes several pre-configured Controls Sets that you can immediately reference in your policies, or you can build

custom sets tailored to your specific needs. These sets align directly with the three policy categories: data control, browser

security, and browser customization.


When you assign a Controls Set to a policy rule, the rule automatically applies the bundled settings. Crucially, the settings

defined in the Controls Set override any rule-specific settings configured locally on that policy. This ensures consistent

enforcement across your deployment and provides a single source of truth for your configurations.

##### **Policy Priority**

Prisma Browser evaluates policy rules in a top-down sequence, meaning the rules at the top of your list hold the highest

priority. Because a user's session might match multiple rules simultaneously, this priority determines which specific controls

take effect.


To ensure predictable enforcement, you must place your most specific, granular rules at the top of the list, and your broader,

baseline rules at the bottom. For example, if a high-priority rule explicitly blocks file downloads for a specific user, but a lower
priority baseline rule allows downloads globally, the system honors the high-priority rule and blocks the download.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|Unlike traditional firewall policies that stop processing on the first match, Prisma<br> Browser rules can aggregate. Each rule contains several controls. If a control from a<br> higher-priority rule does not explicitly override a control from a matching lower-priority<br> rule, the control from the lower-priority rule still applies.|Unlike traditional firewall policies that stop processing on the first match, Prisma<br> Browser rules can aggregate. Each rule contains several controls. If a control from a<br> higher-priority rule does not explicitly override a control from a matching lower-priority<br> rule, the control from the lower-priority rule still applies.|Unlike traditional firewall policies that stop processing on the first match, Prisma<br> Browser rules can aggregate. Each rule contains several controls. If a control from a<br> higher-priority rule does not explicitly override a control from a matching lower-priority<br> rule, the control from the lower-priority rule still applies.||



To illustrate this aggregation, consider a scenario where you have a highly specific rule for your Finance team placed above a

global baseline rule, as shown in Table 2.


_Table 2 Policy priority_

|Priority|Rule name|Target|File downloads|Copy and paste|
|---|---|---|---|---|
|1(High)|Finance-Strict|Finance Group|Block|Not configured|
|2 (Low)|Global-Baseline|All Users|Allow|Allow|



If a user in the Finance group logs in, their session matches both rules. Prisma Browser evaluates Priority 1 first and

explicitly blocks file downloads. However, because the Priority 1 rule does not specify a copy and paste control, the browser

aggregates the configuration and inherits the "Allow" action from the Priority 2 baseline rule.


The resulting effective policy for the Finance user is Downloads: Blocked and Copy/Paste: Allowed.

##### **Scope**

When creating policies, you must always define a scope. The scope dictates exactly to whom, what, or where the policy

applies.


_Palo Alto Networks_ _19_


_Palo Alto Networks Design Details_


To build highly targeted policies, you can use the following options individually or combine them:


   - Users/User groups—Leveraging the directory connected to your CIE, you can target specific individuals or defined

user groups.


   - Device groups—You can scope policies to specific endpoints. You define these groups by evaluating device types or

posture attributes, such as installed certificates, operating system version, or the status of active endpoint protection.

[For more information about device group attributes, see Configure Prisma Browser Device Posture Attributes.](https://architectures.link/2075p-link1)

|Col1|Col2|Note|Col4|
|---|---|---|---|
|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.|On a Windows system, Prisma Browser checks for a client certificate in the personal<br> certificate store. This client certificate must include a private key and its issuer must<br> match the certificate that you use when configuring the device group attribute.||



   - Network—You can specify public or local IP addresses to enforce controls based on the network the user is

connecting from.


   - Location—You can enforce geographic policies. The browser can determine the user's country by using location

services. If those services are unavailable, the browser uses GeoIP data to determine location.

##### **Sign-In Rules**

Sign-in rules act as the primary gatekeeper for your workspace, controlling exactly who and what is allowed to log into

Prisma Browser. You use these rules to restrict initial access based on specific users, user groups, or network locations.


Sign-in rules serve as the enforcement point for the device posture checks discussed earlier. By tying your device groups to

these rules, you ensure that devices meet your strict compliance standards before they are allowed to authenticate and open

the browser workspace.

### PRIVATE APPLICATION ACCESS WITH PRISMA BROWSER CONNECTOR

If you need to provide secure access to privately hosted applications within your data center or private cloud, you can use the

Prisma Browser Connector. This cloud service integrates Prisma Browser with a local ZTNA Connector.


To securely link your internal applications, you deploy a virtual machine with a ZTNA Connector directly inside your private

network. This connector simplifies access by fully automating tunnel creation, management, and routing to your private

application endpoints. You specify the application's FQDN or IP address, and the local ZTNA Connector establishes a

persistent, outbound-only tunnel to the Prisma Browser Connector cloud service.


Because the connector initiates the connection from the inside out and never accepts incoming internet traffic, your private

network remains completely hidden. You do not need to expose any ports or reconfigure your inbound firewall rules.


_Palo Alto Networks_ _20_


_Palo Alto Networks Design Details_


_Figure 5_ _Prisma Browser Connector_


You can deploy the ZTNA Connector with ease because the virtual machine requires no inbound security configuration.

Instead, Prisma Browser natively enforces all security policies, which minimizes your operational overhead. For your users,

the experience is seamless: accessing a private, internal application looks and feels exactly like visiting a public website.

Furthermore, if your private applications are not web-based, the Prisma Browser Connector allows users to securely access

remote devices using SSH and RDP directly within the browser.


[For more information about ZTNA Connector, see Securing Private Application Access with ZTNA Connector: Design](https://architectures.link/2032p-prime)

[Guide.](https://architectures.link/2032p-prime)

### PRISMA BROWSER MOBILE APP AND BROWSER EXTENSION

In addition to the traditional desktop browser version, Prisma Browser is also available as a mobile app and a browser

extension.

##### **Mobile App**

User productivity requires access on the go. Available for iOS, iPadOS, and Android devices, the Prisma Browser mobile app

extends your secure workspace to mobile endpoints.


Tailored for the mobile form factor, the app provides a secure, non-intrusive environment for employees to safely access

SaaS platforms, browse the web, and securely reach your private applications without requiring a legacy mobile VPN. Just

like the desktop experience, the mobile app leverages Palo Alto Networks CDSS to prevent phishing attempts and enforces

DLP controls to protect sensitive interactions.


The Prisma Browser mobile app also performs continuous device posture checks natively. These checks enable you to verify

critical health signals—such as the OS version, screen lock status, root/jailbreak status, and app store integrity—before

granting access. It also extends your visibility by providing comprehensive logging and audit trails for all mobile browser

activity.

##### **Prisma Browser Extension**

If your environment requires you to continue supporting consumer browsers, such as for external contractors or specific

unmanaged devices, you can add Prisma Browser extension as part of your managed browser strategy. Although the

extension operates within a consumer browser framework, it successfully delivers essential baseline protections, enforces

your access policies, and provides your team with the deep visibility required to secure everyday browsing.


_Palo Alto Networks_ _21_


_Palo Alto Networks Design Details_


The extension supports Safari and standard Chromium-based browsers such as Chrome and Edge, as well as specialized

enterprise and AI-centric platforms such as ChatGPT Atlas and DiaAI.

### BROWSER ENFORCEMENT

Even with the most robust security policies in place, your environment remains vulnerable if users can simply open a standard

consumer browser to access corporate applications. To prevent users from bypassing your security controls, you must

ensure that corporate data is exclusively accessed through Prisma Browser.

##### **Conditional Access**

When employees work remotely or on personal devices, they often log in to corporate SaaS platforms with their preferred

consumer browsers. Standard authentication typically verifies the user's identity but ignores the origin of the request. As a

result, access is granted regardless of the browser that is being used. This creates a critical security gap that allows sensitive

corporate data to flow into an unmanaged environment, bypassing your native data controls, live page scanning, and visibility

policies.


In order to enforce compliance and eliminate this workaround, Prisma Browser integrates directly with your IdP. A conditional

access policy precisely controls the circumstances under which users can authenticate and access data. By using these

native IdP policies, you can evaluate the origin of every login attempt, ensuring that users are operating within the secure

workspace.


_Figure 6_ _Prisma Browser authentication_


Application authentication traffic routes through the Prisma Browser proxy, providing you with a set of known IP addresses.

You can configure your IdP's conditional access policy to require these specific proxy IP addresses. If an authentication

attempt originates from an IP address outside of this known set, the user is likely trying to log in by using a standard

consumer browser. When this occurs, the IdP automatically denies the request. This guarantees that your users can only

access specified SaaS applications when they use Prisma Browser.


_Palo Alto Networks_ _22_


_Palo Alto Networks Design Details_


_Figure 7_ _Conditional access policy_


Conditional access is highly effective for protecting your corporate applications. However, it does not prevent users from

opening consumer browsers for general, non-corporate web browsing. You should use conditional access as your baseline

security layer. You can then combine it with the other enforcement strategies detailed below in order to completely restrict the

use of unmanaged browsers on corporate devices.

##### **Mobile Device Management**

To extend browser enforcement down to the endpoint layer, you can leverage a mobile-device management (MDM) service.

An MDM is a centralized security solution that allows you to monitor, manage, and secure your corporate devices. One of its

most crucial functions is regulating exactly what software can be installed or run on a managed endpoint.


As an enforcement mechanism, you can configure your MDM to block alternative consumer browsers by targeting the

software's specific file name or file path. This effectively prevents users from launching unmanaged browsers, ensuring they

use Prisma Browser for their daily tasks.


While using an MDM to block unauthorized software is highly effective for most everyday users, it is not foolproof. Legacy

or basic software restriction policies sometimes rely on static indicators. In those specific scenarios, a savvy user could

potentially circumvent MDM restrictions by changing the file name or moving the executable's file path. For this reason, MDM

software restrictions are best deployed as a supplementary layer alongside more robust controls like conditional access.

##### **Prisma Browser Extension**

If your users continue to use standard consumer browsers for general web activity, the Prisma Browser extension provides a

unique enforcement capability to bridge the security gap.


You can configure a policy rule that transforms the extension into an active traffic director. When a user running a consumer

browser, equipped with the Prisma Browser extension, attempts to access specified corporate websites or critical

applications, the extension automatically intercepts the request and redirects them to open the link in Prisma Browser

instead.


This seamless transition, known as a _browser bump_, ensures that you can mandate Prisma Browser's comprehensive

security features for your most sensitive applications without disrupting a user's standard workflow.


_Palo Alto Networks_ _23_


_Palo Alto Networks Design Details_

### BROWSER DISTRIBUTION

To transform an endpoint into a secure workspace, you must have a reliable method to deliver Prisma Browser to your users.

Choosing the right distribution strategy allows you to balance the need for centralized administrative control on managed

devices with the flexibility required to quickly onboard contractors or BYOD users.


You can distribute Prisma Browser in one of the following ways:


   - Distribution tools—Remotely and automatically deploy Prisma Browser on devices by using third-party software

distribution tools, such as Microsoft System Center Configuration Manager, Microsoft Group Policy Objects, and

unified endpoint management or MDM solutions.

|Col1|Col2|Note|Col4|
|---|---|---|---|
|Using a distribution tool such as an MDM solution allows you to set Prisma Browser<br> as the default browser for endpoints. This simplifies the process for users and<br> reduces potential administrative overhead.|Using a distribution tool such as an MDM solution allows you to set Prisma Browser<br> as the default browser for endpoints. This simplifies the process for users and<br> reduces potential administrative overhead.|Using a distribution tool such as an MDM solution allows you to set Prisma Browser<br> as the default browser for endpoints. This simplifies the process for users and<br> reduces potential administrative overhead.||



   - SSO integration—Add a link to download Prisma Browser directly from your SSO login page. Users can then install it

in self-service mode with no administrative privileges required.


   - Deployment emails—Send invitation emails directly to the users of your choice. They can start using Prisma Browser

right after completing a simple, standard installation with no admin permissions required.

### LICENSING

Prisma Browser Standalone licensing is available in two distinct tiers. Choosing the right bundle depends on your

organization's specific security and management requirements.


Prisma Browser tiers:


   - Prisma Browser Core— If you need a strong foundation for secure enterprise browsing, choose Prisma Browser

Core. This tier provides essential protections for web, SaaS, and GenAI applications. It equips you with standard web

and data protection, such as Advanced URL Filtering, Advanced WildFire, and Enterprise DLP. Core also includes

fundamental browser management, basic ZTNA through third-party integrations, and identity protections such as

a built-in password manager and MFA controls. It is ideal for organizations looking to secure standard web access

without requiring deep, custom integrations.


   - Prisma Browser Pro—If you need private application access and advanced threat defense, choose Prisma Browser

Pro. Pro includes everything in the Core tier, plus advanced capabilities such as private application access by using

the Prisma Browser Connector. With the Pro tier, you gain the ability to secure legacy and non-web protocols, such

as RDP, SSH, and server message block. Furthermore, it delivers advanced web, extension, and browser protections,

along with comprehensive identity features such as shared passwords and non-SSO enforcement. Finally, the Pro tier

provides you with ADEM capabilities, capturing RUM data in order to streamline helpdesk troubleshooting.


_Palo Alto Networks_ _24_


_Palo Alto Networks Design Details_

### SYSTEM REQUIREMENTS

Prisma Browser provides a secure workspace across a wide range of operating systems and hardware architecture.


Prisma Browser supports the following:


   - Windows—Windows 11 64-bit on both standard 64-bit and ARM (A64) processor architectures.


   - macOS—macOS 12 Monterey or later, with native support for both Intel x86 and Apple M1 or newer silicon.


   - Linux—Several major distributions, including Ubuntu 22.04.5 LTS or later, Fedora 41 or later, and IGEL OS 12 or

later.


Prisma Browser mobile app supports the following:


   - Mobile devices—Android devices running version 12 and later, and iOS devices running version 18 and later.


_Palo Alto Networks_ _25_


_Design Model_

## Design Model


To build a secure architecture, you can apply the concepts in this guide in multiple ways. In this model, Microsoft Entra

ID serves as the IdP. It handles SAML authentication for both Prisma Browser and the applications your users access.

Prisma Browser connects with Entra ID by using the CIE, which brokers authentication between users and Entra ID. CIE also

provides group information for use in your Prisma Browser policies by synchronizing user and group identities from Entra ID.


_Figure 8_ _Prisma Browser design model_


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

Advanced WildFire, across all web traffic. These policies use Enterprise DLP profiles to identify and protect sensitive data in

real time. For example, if a user accesses a Tolerated GenAI application from an unmanaged device, the browser's AI prompt


_Palo Alto Networks_ _26_


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


_Palo Alto Networks_ _27_


_Summary_

## Summary


In this guide, you learned about a design that protects against the variety of cyber threats that organizations face and

safeguards corporate resources while maintaining efficiency and effectiveness. The design turns the browser into a secure

workspace by integrating advanced security features such as encrypting browser assets and locking down vulnerable

browser components. It also includes DLP controls, Zero Trust access controls, and comprehensive web security. These

capabilities provide deep visibility into user actions and ensure that only authorized users can access sensitive information.


To extend this secure workspace to your internal resources, you use the Prisma Browser Connector. This approach grants

your users seamless, high-performance access to private web applications and legacy protocols without exposing your

infrastructure to the public internet.


This design includes the following components:


   - Prisma Browser


   - Prisma Browser Connector


   - Strata Cloud Manager


   - Strata Logging Service


   - Enterprise DLP


   - Cloud Identity Engine


The following guide builds upon what you've learned here, walking you step-by-step through deployment of this design and

its components:


   - [Securing Internet and Private Applications by Using Prisma Browser: Deployment Guide—Provides](https://architectures.link/2071p-prime)

implementation details for securely accessing internet and private applications by using Prisma Browser and Prisma

Browser Connector. Includes high-level tasks and step-by-step configuration details for browser-native protections,

including last-mile controls, Enterprise DLP, and cloud-delivered security services across managed and unmanaged

devices.


_Palo Alto Networks_ _28_


_Summary_


## Feedback

[You can use the feedback form](https://www.paloaltonetworks.com/resources/reference-architectures/feedback-ra?guid=2070p-16062026) to send comments about this guide.


_Palo Alto Networks_ _29_


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


P-2070P-16062026



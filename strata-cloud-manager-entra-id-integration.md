# Strata Cloud Manager — Entra ID Integration (Cloud Identity Engine)

> Pulled from https://docs.paloaltonetworks.com on 2026-06-27. Images/links are absolute URLs.

---

## Set Up a SAML 2.0 Authentication Type

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

# Configure Azure as an IdP in the Cloud Identity Engine

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

# Configure Okta as an IdP in the Cloud Identity Engine

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

## Integrate Okta as a Custom or Gallery Application

- [Gallery Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-gallery)
- [Custom Application](https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/authenticate-users-with-the-cloud-identity-engine/set-up-a-saml-2-0-authentication-type/configure-okta-as-an-idp-in-the-cloud-identity-engine/configure-okta-as-an-idp-in-the-cloud-identity-engine-custom.html#configure-okta-as-an-idp-in-the-cloud-identity-engine-custom)

# Configure Okta as an IdP in the Cloud Identity Engine (Gallery)

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

# Configure Okta as an IdP in the Cloud Identity Engine (Custom)

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

# Configure PingOne as an IdP in the Cloud Identity Engine

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

# Configure PingFederate as an IdP in the Cloud Identity Engine

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

# Configure Google as an IdP in the Cloud Identity Engine

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

# Configure Idira as an IdP in the Cloud Identity Engine

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

## Configure the Cloud Identity Engine Template for SSO in Idira

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

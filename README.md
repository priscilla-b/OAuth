# OAuth


## What is OAuth?
> An open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications
\- from [docs](https://oauth.net/)
- The main reason why OAuth was initially set up was to allow an application access user's data without having to give it the user's password. Case in point: remember when all those third party apps would ask for you email + password in order to access your gmail contact, etc? Obvious security violation as apps could hold on to and be able to change your password. Some applications would store users' password in plaint text(obvious security risk). Only way users could revoke access was to change passwords
- The main distinguishing feature of OAuth is that instead of letting users enter passwords in the third-party app, users are redirected to the OAuth server(the primary application I guess) to enter their password and then redirected back to the third party app that is seeking access.
- Other use cases of OAuth after its initial use case was around organizations that were building first-party apps on their own APIs. Case in point: when logging into any google service(YouTube, Gmail, etc.) you don't sign into the service directly. You're redirected to Google's OAuth server(accounts.google.com) where you sign in and then redirected to the google service after authentication.
- Benefit is to centralize password management for security reasons.
- Another benefit of centralization is that it makes it easy to upgrade authentication for all users/services


## OAuth 2
- There were some use cases such as in mobile applications, where the initial implementation of OAuth could not be used securely.
-  The goal of OAuth 2 was to build on OAuth 1 for mobile applications and simplify aspects that were confusing to API consumers.
- Issue with OAuth 2 was that there were conflicts between the web and enterprise contributors of the protocol. A lot of the areas of contention were put in different documents, leaving a lot of gaps in the protocol(now being called a framework in the core document as a result).
- Result is that web implementation for OAuth 2 can be complex and confusing as you'll need to synthetize information from different drafts
- Implementation Issues:
    - standard does not require a token type
    - does not require specific grant types
    - does not give guidance on token string size


### Creating an OAuth 2 Application
- Create a developer account on the service's website and enter basic info about the app(name, website, logo, etc.)
- You'll be given a `client_id` and `client_secret` (sometimes) that your app will use to interact with the service.
- Critical to register one or more redirect urls (where the OAuth 2 service will return the user after they have authorized the application) to avoid creating malicious apps that can steal user data.
- Redirect URL must be an https endpoint to provide an attacker from intercepting authorization code and hijack a session
- Instead of registering multiple redirect urls for different application states, OAuth 2 provides a "**state**" parameter that can be used to encode an app state. 
- The parameter is a string that will be returned after user is authorized to bring them to the right location in the app. State string should be encrypted with a method like JWT.


## Concepts I've Learnt
### **cURL**
- stands for **client URL** is a command line tool that developers use to transfer data to and from a server. Let's you communicate with a server by specifying url(location) and data you want to send. 
- Supports different protocols(http, https) and runs on almost every platform, making it ideal for testing communication on almost any device
- Benefits: 
    - highly portable and comparable with almost OS and device
    - useful for testing endpoints
    - can be verbose, hence helpful for debugging
    - good error logging


## Resources
- [OAuth Documentation](https://oauth.net/)
- [What is OAuth and why does it matter?](https://www.youtube.com/watch?v=KT8ybowdyr0) - OktaDev on Youtube
- [OAuth 2 Servers](https://www.oauth.com/oauth2-servers/)
- [IBM: What is cURL?](https://developer.ibm.com/articles/what-is-curl-command/)
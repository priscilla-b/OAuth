# OAuth


## What is OAuth?
> An open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications
\- from [docs](https://oauth.net/)
- The main reason why OAuth was initially set up was to allow an application access user's data without having to give it the user's password. Case in point: remember when all those third party apps would ask for you email + password in order to access your gmail contact, etc? Obvious security violation as apps could hold on to and be able to change your password. Some applications would store users' password in plaint text(obvious security risk). Only way users could revoke access was to change passwords
- The main distinguishing feature of OAuth is that instead of letting users enter passwords in the third-party app, users are redirected to the OAuth server(the primary application I guess) to enter their password and then redirected back to the third party app that is seeking access.
- Other use cases of OAuth after its initial use case was around organizations that were building first-party apps on their own APIs. Case in point: when logging into any google service(YouTube, Gmail, etc.) you don't sign into the service directly. You're redirected to Google's OAuth server(accounts.google.com) where you sign in and then redirected to the google service after authentication.
- Benefit is to centralize password management for security reasons.
- Another benefit of centralization is that it makes it easy to upgrade authentication for all users/services




## Resources
- [OAuth Documentation](https://oauth.net/)
- [What is OAuth and why does it matter?](https://www.youtube.com/watch?v=KT8ybowdyr0) - OktaDev on Youtube

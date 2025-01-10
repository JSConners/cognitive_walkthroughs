# Paypal

| Step - Action | What happened | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 0. Manage Passkeys | Displays iOS passkey... gives a notification that a passkey can't be created on this device or browser... then has FAQ link. | A similar thing happened with apple, could not use macOS Sonoma... but could use Ventura, Monterrey or Big Sur. This information is just REALLY out of date. See Notes 1.  | 
| Step 1. FAQ | VERY OUT OF DATE information | See (BAD FAQ Info)[BAD FAQ Info] (PayPal FAQ)[https://www.paypal.com/us/cshelp/article/what-is-a-passkey-and-how-do-i-use-it-to-log-in-to-my-paypal-account-help997]  <br> Doesn't work on Windows, must activate passkeys in browser, Safari is required... etc <br> It is a little misleading about what actually happens when they say: "They let you log in the same way you unlock your device -using your face, fingerprint, or PIN." <br> Still more incorrect information about cloud storing passkeys. <br> REALLY BAD INFO about only being able to recover from a lost/broken device... says only 30 days.. Apple docs state that is for deleted passkeys (Apple)[https://support.apple.com/guide/mac-help/recover-a-deleted-password-or-passkey-mchlee73013a/mac]  | 


## Notes 
1. We were able to bypass the Apple limitations by creating a passkey on a mobile device, then logging in on a Mac Mini running Sonoma. We could not create a passkey on Sonoma.
2. 


## BAD FAQ Info
A passkey allows you to securely log in to PayPal without entering a password. With a passkey, you can log in to PayPal using the same biometrics, PIN, or password for your device, resistant to phishing and hacking attempts.

Who can create a passkey? 
Passkeys are currently available for eligible personal accounts. An eligible Apple or Android device is required to create a passkey.

Eligible Apple devices:

iOS 16+
MacOS Ventura, Monterrey, or Big Sur
For web use, a Safari browser is required.
For Chrome, passkeys cannot be enabled unless they are turned on in the browser's settings.

Eligible Android devices:

Android 9+
For web use, a Chrome browser is required.
How are passkeys different from passwords?  
Passkeys are a simple and secure alternative to passwords. They let you log in the same way you unlock your device -using your face, fingerprint, or PIN.

Once created, passkeys are synced with your iCloud Keychain or Google Password Manager, ensuring a robust and private relationship between you and your device. Unlike passwords, which require you to create, remember, and enter your information to log in, you never have to type or enter your passkey. Passkeys are backed up and protected from loss; if you get a new device, it can quickly be restored for up to 30 days.

How do I create a Passkey? 
Here’s how to create for the first time on your mobile device:

Log in to your PayPal account from your mobile device.
In your Profile under Login and Security, you’ll see the option to “Create a Passkey.” Once you’ve reviewed the info, choose Next.
Review the details and to give permission, choose Continue.
You'll be prompted to unlock your device to create a passkey.
On iPhones, you can use Face ID, Touch ID, or passcode to unlock your device. On Android devices, you can use the face or fingerprint scan, PIN, or Pattern to unlock your device (depending on what device lock is set up on your device). You should be automatically directed to your PayPal home screen when completed.

You can also follow this link to Setup your passkey.

What happens if my device is lost or stolen? 
If your device is lost or stolen, you can still log in to PayPal with your password or a one-time passcode. Your account with PayPal cannot be accessed without first unlocking your lost or stolen device. As an extra precaution, you can also log in to PayPal and remove the passkey from your account.

As another precaution, passkeys are privately stored and synced with your iCloud Keychain or Google Password Manager - this means that you should be able to (and should) delete a passkey on a lost or stolen device by logging into your cloud account.

How do I delete my passkey from my account? 
You can remove your passkey in the Security settings within your account through the PayPal app or on PayPal.com. However, this action will not remove the passkey from your device.

On an Apple device, please follow these steps to remove the passkey from your device:

Choose System Settings, then click Passwords in the sidebar. (You may
need to scroll down.)
Click the Info button for PayPal.com.
Click Edit. 
Click Delete Passkey.
Click Delete Passkey (again).
On an Android device, follow these steps to remove a passkey from your device:

Choose Settings, then click Passwords Manager in the sidebar. (You
may need to scroll down.)
Click the entry for PayPal.com. (You may need to scroll down to find the entry for PayPal.).
Unlock your device if you're prompted to do so.
Click Delete for the passkey listed for PayPal.
Click Delete (again) on the pop-up dialog.
How do I use my existing passkey across all my devices? 
Log in to PayPal on your Apple (iPhones, Macs, and iPads) or Google (Android only) device with a passkey stored on that device.

If your email is not remembered on the PayPal login page, type in your email and choose Next to log in with a passkey. If your email is remembered, choose the Log In button to start a passkey. 
Follow the onscreen instructions to confirm your identity by unlocking your device.
Log in to PayPal on a device with a passkey stored on your phone (iPhone or Android phone).

iPhones store your passkeys on an iCloud keychain, so they are automatically used whenever you are logged in with the same Apple ID on another device (iOS 16, iPadOS 16, macOS Ventura, or tvOS 16 required). Similarly, Android phones store your passkeys in Google Password Manager, so they are automatically used whenever you are logged in with the same Google account across all your Android devices (Android 9+).

To log in with a passkey on a device not associated with the same Apple ID or Google Account, follow these steps:

If your email is not remembered on the PayPal login page, type in your email and choose Next to initiate the login with a passkey. If your email is remembered, then choose Log In to start the login with a passkey.
Choose Other options, Passkey from a nearby device, or similar on the pop-up screen, and then follow the instructions to display a QR code.
Follow the instructions to scan the QR code with a phone with the passkey for PayPal.
Finish the onscreen instructions on your phone to approve the login on the nearby device.
Which devices and browsers support passkeys? 
Today passkeys for PayPal accounts are supported by eligible Apple or Android devices:

Eligible Apple devices:

iOS 16+
MacOS Ventura, Monterrey, or Big Sur
For web use, a Safari browser is required.

Eligible Android devices:

Android 9+
For web use, a Chrome browser is required.
Passkeys are not supported on WebView browsers and Windows devices. On a Windows device, the user must use a password or SMS OTP to log in. 

Can I use a passkey on an unsupported device? 
No, passkeys can’t be used on unsupported devices or web browsers. 

Once I create a passkey, do I have to enter a password with PayPal again? 
Once you create a passkey, you can use it as your primary login method. You may see other login options if your operating system, device, or browser does not meet eligibility requirements or if you are in a country where passkeys are unavailable. 

What if my passkey fails? 
You’ll receive an error message and be prompted to log in using another login method.

What if I want to use my password instead? How do I do that?
During login, click Try Another Way to see all, including the password. You can turn off your passkey in the Security settings within your account through PayPal.com.  

With passkeys, does PayPal now have my biometric data? 
No. Your biometric data is not shared with PayPal and never leaves your device. 

# Screenshots

These screenshots are from macOS Sinoma, using Google Chrome, and viewing https://gmail.com

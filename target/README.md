# Cognitive Walkthrough

No options for smartphone/tablet/hardware token? 

## Apple Notes
### Setting up a Passkey with Existing Account

| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
Signing in with password, it showed an option for password or passkeys. When using the password (because no passkey yet), it showed a screen introducing Passkeys. Two buttons: “Create a passkey” and “Maybe later”, with Create a passkey in red, clearly the default button. | Success: Prompts users to switch to a more secure and convenient system. <br><br> Failure: Not teaching them about recovery. Nothing about where credentials are stored. Equates to biometrics. | Selling based on “simplify”. Sign in with fingerprint, face, or PIN. More convenient, more secure. You can use both passkeys and passwords. 
Pressed the button to create, it popped up the OS dialog, which says it will save a passkey in iCloud Keychain. | Failure: Passkey for “jconners@0988@gmail.com” instead of for “Target”. Says it will be available on all yoru devices (all Apple devices).
Click Continue. Prompted for Apple Password. | Failure: biometrics not available on this device, so we couldn’t use them. False advertising? <br><br> Failure: But it doesn’t explain which password. OS password, iCloud, or Target password. All for the same email.
Entered OS password. It was created and named “Chrome 123 on Macintosh” | Failure: No option to name the Passkey. It says next time you can use your fingerprint to sign in, but it will actually be OS password on this device and could be FaceID elsewhere.
Done goes to Target Home Page
When clicking cancel when creating a passkey, you now have the option of using either iCloud keychain or Chrome profile | Failure: Can’t scan a QR code and use your phone <br><br>
When clicking cancel when creating a passkey, you now have the option of using either iCloud keychain or Chrome profile | Failure: Can’t scan a QR code and use your phone <br><br> Failure: A Chrome profile Passkey is given the same default name. There is no option to rename keys. <br><br> Failure: Chrome profile Passkeys are stored only on that device, can’t use them elsewhere.

### Register for a new account Account
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
Signed up for an account using name, email, phone, and password. | Took to home page.
Signed out, signed back in with password, now it prompts for a Passkey

### Adding a Passkey
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
Find it in Settings, Sign in and Security | Uses the OS prompt as before. No other teaching material besides what is shown below “Add passkey”.<br><br> Failure: “Once you add one, it’s saved to your password manager” – if you use one!<br><br> Will not let you use a hardware security pay. | Sells passkeys based on “Strengthen account security”, “skip typing your password”, “save time and peace of mind”






# Screenshots
## [Windows Screenshots](windows_SS) 
These screenshots are from Windows 11, using Google Chrome, and viewing https://target.com... Taken on 4/25/2024

## [macOS Screenshots](macOS_SS)
These screenshots are from macOS Sonoma, using Google Chrome, and viewing https://target.com... Taken on ---
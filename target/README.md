# Cognitive Walkthrough

No options for smartphone/tablet/hardware token? 
## Notes
Target gives a 1 time prompt asking the user if they want to use Passkeys. 

## Apple Notes
### Setting up a Passkey with Existing Account

| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 0. Sign in and security page | Info -- "Passkeys protect your account iwth a key unique to you, like your face or fingerprint. Once you add one, it's saved to your password manager, so you can use it to sign in from other devices. You can shoose to sign in with your passkey or password any time." <br> Has good bullet points at the bottom of the passkeys box: "Strengthen account security, skip typing your password, save time and peace of mind."  | Good mental model analogies that will help users understand what is happening. <br> Could be a little clearer in the distinction between unique key and biometrics. <br> Reassures the user they can still use their password if they want. | 
| Step 1. click "Add passkey"| See (Win11 OS)[win11OSdialoges.md] | I could only register a passkey on the local device... clicking cancel ended the passkey registration process. <br> This is a decision by Target to not allow roaming devices in the FIDO2 settings. | 
| Step 2. Click "Ok" after passkey creation in OS Dialogue. | Passkey is named "Chrome 124" and gives a date/time. | A little weird... could let the user name the passkey... but also has a separate field below to show where the user is currently logged in, so that might be why. |


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

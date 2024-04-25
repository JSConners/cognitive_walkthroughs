# Cognitive Walkthrough

## Apple Notes
### Setting up a Passkey with Existing Account on Chrome
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Setup: Using Chrome on a Mac | The button to do this is on the same page as adding 2FA to the account
| Passkeys and Security Key page | | Two buttons for creating a key, do they do the same thing? No!<br><br>(1) Top right blue button assumes that I want to create a passkey on my device (iCloud keychain). <br><br>(2) Bottom, white button gives me the option of using another device. But even then “Create a passkey” assumes this device, whereas “Use another device” defaults to hardware key if I have one plugged in or to phone QR code if not. <br><br> “To add security to your account, create a passkey on this device or use another device, like a hardware security key.” – may not know what a hardware security key is, doesn’t mention I can use my phone. <br><br> “Only set up passkeys on devices you own” – Very easy to create a passkey on a computer that is not my own – warning is buried in the text
| Clicked on Create a Passkey, I get the OS box that asks for my fingerprint – Use Touch ID to sign in? Fingerprint continues. Cancel brings up to ask about either iCloud keychain or Chrome Profile. No option to go to hardware or iPhone. | Mental Model – reinforces biometrics for user understanding – you are signing in with fingerprint (in my case) and they mention face, screen lock (what is screen lock?) – possibly a mobile device | Leads user to think of Passkeys as Touch ID. Does say that a Passkey will be created and saved on the iCloud Keychain – requires users to know what this is. 
| If I use TouchID, it gives me a box that says “Password Created” with one button, DONE. Once dismissed, the screen shows me my Passkey stored in the iCloud keychain. | Success story – user is led to create a Passkey using the iCloud keychain. <br><br> Potential failure story – what if I am on a different device later on? <br><br> Different OS account / Microsoft account at home vs work 
Or if I want to use a different setup (Phone / hardware token) it is not obvious how to get there. | Chrome is the only browser that allows me to use the Chrome keychain (obviously). <br><br> Chrome on Mac bypasses the OS dialogs, whereas Safari and Firefox use the Mac dialogs.<br><br>Canceling causes an “error”
| If I click Use another Device, I get a QR code to scan. I can choose to insert a hardware security key at this point (and it has some instruction for this at the bottom of the screen. | Failure – user fails to read instruction or doesn’t see instruction for hardware security key. | If I have configured iCloud to save keys and/or have configured 1Password to save keys, these will be shown as options. If only one is configured, it will go straight to that option.
| If I have a hardware security key plugged in and click Use another Device, I get a QR code dialog that then disappears and is replaced with a PIN dialog | Failure – If I have a security key plugged in, I will never see the QR code (it disappears quickly) and I don’t have the option to use my phone. | 

### Differences between Chrome and Safari
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| When clicking Use Another Device, we get an OS dialog instead of a Chrome or Safari dialog. It says “Save a passkey on a device with a camera” It mentions iphone, ipad, or android device. The other choice is “Use an External Security Key” | Failure: Try it Out doesn’t work with keys saved to Passkeys (regardless of browser) on a phone (not the laptop). Note, the browser extension will try to jump in and do everything. | Note wording is different for OS dialog box than Chrome dialog boxes.

### Differences between Chrome and Firefox
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Firefox uses the OS dialogs | | |

### Using 1Password
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| 1Password will intercept the request to create a Passkey and “go first” | Failure: If I want to use a hardware security key, then even if I choose “Use another Device”, 1 Password intercepts the request, and I have to click the device icon to then get a dialog that comes from the OS to let me use my hardware security key. | 1Password is opinionated and feels like it should always go first (on a laptop). On a phone if you configure both, user gets a choice of which to use.










# Screenshots
## [Windows Screenshots](windows_SS) 
These screenshots are from Windows 11, using Google Chrome, and viewing https://gmail.com ... Taken on 2/27/2024

## [macOS Screenshots](macOS_SS)
These screenshots are from macOS Sonoma, using Google Chrome, and viewing https://gmail.com ... Taken on ---
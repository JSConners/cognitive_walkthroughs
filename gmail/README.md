# Cognitive Walkthrough
<button href="www.gmail.com"> <img src="./mac_SS/blueButton.png" </button>
## Apple Notes
### Setting up a Passkey with Existing Account on Chrome
| Step | Design Comments | Researcher Suggestions or Comments |
| ---- | ----------- | ---------- |
Setup: Using Chrome on a Mac | The button to do this is on the same page as adding 2FA to the account
| ---- | ----------- | ---------- |
**Step 1.** Passkeys and Security Key page  |  1. Two buttons for creating a key, do they do the same thing? No! <br><br> From the screen recording <br>1.1 Top right blue button labeled "Create a Passkey" ![Create a Passkey](./mac_SS/blueButton.png)   <br> This assumes that I want to create a passkey on my device (iCloud keychain). <br> <br>1.2 Bottom, white button labeled "+ Create a Passkey" ![+ Create a Passkey](./mac_SS/+create.png) <br> gives me the option of using another device. But even then “Create a passkey” assumes this device, whereas “Use another device” defaults to hardware key if I have one plugged in or to phone QR code if not. <br><br>  | 1. It's unclear from the UI if the 2 buttons do the same thing. User's may not know what a hardware security key is, doesn’t mention I can use my phone.
| ---- | ----------- | ---------- |
**Step 2.** Click on create a passkey. <br><br> ![+ Create a Passkey](./mac_SS/+create.png) | A browser popup with 3 buttons, an identical button to ![Create a Passkey](./mac_SS/blueButton.png),<br> a button that says "use another device", and "cancel" <br><br> Dialogue: "Create a passkey to start signing in with just your fingerprint, face, or screen lock. You can create a passkey on this device or use another device, like a hardware security key." | Mental Model – reinforces biometrics or device pin, for user understanding – you are signing in with F ingerprint / FaceID / Device pin / Device Password (in my case) and they mention face, screen lock <br><br> A user may not know what the websites means by "screen lock", and it could possibly be refering to a mobile device?
| ---- | ----------- | ---------- |
**Step 3.** Clicked on the blue button: "Create a Passkey" | I get an OS dialogue box that asks for my fingerprint – Use Touch ID to sign in?<br><br> Using my fingerprint continues the process.  | This option, regardless of OS and authentication mechanism, only lets the user use that devices default method (e.g., if I have winHello w/ pin, I can only use the pin, same for FaceID/Fingerprint/Password(mac mini keychain). Leads user to think of Passkeys as TouchID or FaceID. It does say that a Passkey will be created and saved on the iCloud Keychain – requires users to know what a Passkey is.
| ---- | ----------- | ---------- |
**Step 4.** Clicked on cancel | This brought up a new OS dialogue box with iCloud keychain or Chrome Profile as selectable options. No option to go to hardware or iPhone. | If someone wanted to use their iPhone, then they couldn't. Also applies to hardware tokens. What if someone is using a public computer, or using a friends laptop, and the device is logged into a different icloud account? I could accidentally create a passkey on a device that I don't own/control, instead of being able to use my own device, such as a phone or tablet. <br><br>If a website can recognize unique devices (highly probable), they could potentially give a user a warning like: "This is a new device, do you REALLY want to save a passkey on this device?"
| ---- | ----------- | ---------- |
**Step 5.** Going back to **Step 3**, then proceeding to use TouchID | Website gives me a box that says “Passkey Created” with one button, "DONE". Once dismissed, the screen shows me that my Passkey is stored in the iCloud keychain. | Success – If a user is on their own device, and the device has a built in biometric, they are led to create a Passkey using the iCloud keychain. The process was really fast and simple, works very well for a user in a single OS-ecosystem. <br><br> Potential failure – what if I am on a different device later on, or using a different OS account / Microsoft account at home vs work 
| ---- | ----------- | ---------- |
**Step 6.** I want to use a different authenticator |  Clicking cancel in **Step 4**, gives 2 options: "iCloud Keychain" and "Chrome Profile" <br><br> Clicking cancel on the new window gives an error: "Something went wrong, we weren't able to save your account changes. Try again." | Chrome is the only browser that allowed me to use the Chrome keychain <br><br> Chrome bypasses some macOS dialogs, whereas Safari and Firefox use macOS dialogs. <br><br> The UI does not make it obvious how to use a different device, but this is an OS notification. <br><br> If I click choose another authenticator, and then change my mind, instead of going backwards 1 step, it errors out.  
| ---- | ----------- | ---------- |
**Step 7.** Click "Use another Device" on the screen in **Step 2** | I get a QR code to scan. Small text at bottom that says I can use a USB Security key. | Failure – user fails to read instruction or doesn’t see instruction for hardware security key. <br><br>On an iPhone, and I scan the QR code... if I have configured iCloud to save keys and/or have configured 1Password to save keys, these will be shown as options. If only one is configured, it will go straight to that option.
| ---- | ----------- | ---------- |
**Step 8.** I have a HSK conneccted and click "Use another Device" from **Step 2** | I get a QR code dialog that then disappears automatically. New dialogue box asking for the HSK pin. | Failure – If I have a security key plugged in, I will never see the QR code (it disappears quickly) and I don’t have the option to use my phone.

### Differences between Chrome and Safari
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
When clicking Use Another Device in **Step 2** | **DOUBLE CHECK THIS!!!!!!**<br>We get an OS dialog instead of a Chrome or Safari dialog. It says “Save a passkey on a device with a camera” It mentions iphone, ipad, or android device. The other choice is “Use an External Security Key” | Failure: Try it Out doesn’t work with keys saved to Passkeys (regardless of browser) on a phone (not the laptop). Note, the browser extension will try to jump in and do everything. <br><br> Note wording is different for OS dialog box than Chrome dialog boxes.

### Differences between Chrome and Firefox
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Firefox uses the OS dialogs | | |

### Using 1Password
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
At **Step 3**| 1Password will intercept the request to create a Passkey and “go first”, interupting the macOS dialog. | Failure: If I want to use a hardware security key, then even if I choose “Use another Device”, 1 Password intercepts the request, and I have to click the device icon to then get a dialog that comes from the OS to let me use my hardware security key. <br><br> 1Password is opinionated and feels like it should always go first (on a laptop). On a phone if you configure both, user gets a choice of which to use.


## Windows Differences
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
**Step 1** Click the blue button (top right). | When clicking cancel inside the Windows Security OS dialog box, Gmail responds with an error message "Something went wrong." | This is different than on macOS Sonoma, where Chrome gives additional options after defaulting to the device the user is currently using. This might be based on the Chrome profile syncing--- but seems to be more of a Mac thing. 
| ---- | ----------- | ---------- |
**Step 7** Click on "Use another device" | Windows Security Dialog Box <br><br> Has options for: 1. Chrome Profile registered Android device<br><br> 2. iPhone, iPad, or Android Device<br><br> 3. Security Key. | Design Comments: Option (1) is listed on this OS notification twice, and the "more choices" are smaller. Just remove the big Option (1), and make "more choices" larger. 
| ---- | ----------- | ---------- |
**Step 8** Clicked on "iPhone, iPad, or Android Device. | Displayed a QR code, with information on what website the request came from, and which application sent the request. 


## Notes
We need to  verify what the priority is for Windows Hello, if I have a pin/FaceID/Fingerprint all setup. 
James -- go through the Browser Differences... 


# Screenshots
## [Windows Screenshots](windows_SS) 
These screenshots are from Windows 11, using Google Chrome, and viewing https://gmail.com ... Taken on 2/27/2024

## [macOS Screenshots](macOS_SS)
These screenshots are from macOS Sonoma, using Google Chrome, and viewing https://gmail.com ... Taken on ---

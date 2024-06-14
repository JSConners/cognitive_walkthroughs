# Cognitive Walkthrough

Registration using Windows Hello was fine. When trying to register a smartphone, it did NOT use the browser popup, and used it's own instead. I scanned it, got redirected to the Sony Website, where I clicked use passkeys, and then my phone displayed a QR code that a device which I had a passkey on needed to scan. 

When I registered my iPhone first, it was straightforward. 


## Windows Notes
### Setting up a Passkey with Existing Account

| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 1. Go into account settings, click add a passkey. | Success: Stripped down process, quick and easy. <br><br> Failure: No information about what a passkey is, how it works, etc.. | Add some information about passkeys being a password replacement. | 
| Step 2. Click "Create on This Device"  | Success: Allows user to choose any device. (OS Notification) | |
| Step 3. Scan a QR code, process completed on mobile device. | | | 
| Step 4. Passkey registration completed | **Success: Password is deactivated. The only way to log into my account is using my passkey!!** <br><br> Failure: The notification that the password will be deactivated is small and at the end of a notification. | When the user clicks the add a passkey button, notify them that their password will be removed. 

## Bad design for some of it... 
| Step | Design Comments | Researcher Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 1. Click "Create a Passkey" button in the account security screen | Get 2 options, On this device or on Another device. | This is a browser popup from the website. | 
| Step 2. Click "Create on another device" | Browser popup that says scan QR code and gives a QR code. | Scanning the QR code does NOT create a passkey on the device. It is a URL QR Code, that sends the user to the Sony webpage, askiong them to login... where they can then use the "Create a passkey on this device" option.. to create a passkey on their mobile device. This completely bypasses the CTAP2 protocol on desktops... which is used to make sure the auth information is transfered securely. Seems like an attacker could leverage this. |


### Managing my Passkeys
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Managing Passkeys | Failure: Sends Payload browser information from the host Browser, instead of where the passkey is saved (e.g., iCloud, 1Password, etc). | | 


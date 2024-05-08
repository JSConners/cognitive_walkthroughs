# Cognitive Walkthrough

## Windows Notes
### Setting up a Passkey with Existing Account

| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Go into account settings, click add a passkey. | Success: Stripped down process, quick and easy. <br><br> Failure: No information about what a passkey is, how it works, etc.. | Add some information about passkeys being a password replacement. | 
| Choose the device I want to save a passkey with. | Success: Allows user to choose any device. (OS Notification) | |
| Scan a QR code, process completed on mobile device. | | | 
| Passkey registration completed | **Success: Password is deactivated. The only way to log into my account is using my passkey!!** <br><br> Failure: The notification that the password will be deactivated is small and at the end of a notification. | When the user clicks the add a passkey button, notify them that their password will be removed. 


### Managing my Passkeys
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Managing Passkeys | Failure: Sends Payload browser information from the host Browser, instead of where the passkey is saved (e.g., iCloud, 1Password, etc). | | 


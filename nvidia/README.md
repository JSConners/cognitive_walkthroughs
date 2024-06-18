# Cognitive Walkthrough

## Windows Notes
### Setting up a Passkey with Existing Account

| Step - Action | What happened | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 0. Hardware Security Device page. | Displays <Not set> and has a button "+Add New Security Device" | It's weird that this is the phrasing used for Passkey setup.. non-standard terminology |
| Step 1. Click "+Add New Security Device" | Displays a new page "Secure My Account"... immediately hidden by OS dialog box | The OS dialog blocks any information on this page. All the language is based on using a hardware security device. |
| Step 1.2. Windows OS Dialog into "Secure My Account" page| Has a dialog box to allow the user to name their security key, and has a check box for additional security.  | Pretty good design.. except it still uses hardware token phrasing after I just registered using an iPhone. |
| Step 2. Success Popup | Tells the user that the key has been registered, and can now be used to login or as a security factor. | Reasonable... Changes phrasing to "security key" instead of "hardware security device
" ... just inconsistent phrasing |
| Step 3. Hardware Security Device page | Displays the given name, last used and added on dates. | The information is reasonable enough... could let a user know just by Last Used if their cloud account has been compromised. (though that date might get overridden when they login). |


| Go into account settings, click "Hardware Security Device." | Failure: This is under multi-factor security and does not tell the user until later in the process they can use it to login. <br><br> Failure: the phrase "Passkey" does not appear until the OS level notification. | Use common phrasing such as the word "Passkey". Notify the user BEFORE creation that it can be used to login to the account. | 



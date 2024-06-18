# Kayak

- stripped down -- no instructions / text about what Passkeys are
- goes straight from "Add Passkey" to ask you where you want to store it:
  - iCloud Keychain
  - Phone, tablet, or security key
  - Chrome Profile
- Can use a security key


| Step | Design Comments | Researcher Suggestions or Comments |
| ---- | ----------- | ---------- |
| Step 1. Account Settings Screen |  Text: "Passkeys are easy to setup and let you securely sign into your KAYAK account using your fingerprint, face or screen lock." <br> Click the black button that says "Add passkey" | This is misleading if you are doing this on a desktop without biometrics available.. maybe screen covers using Windows Hello pin/ user password... still unclear... <br> Emphasis on "Easy" and "Secure" <br> Conflates Passkeys and Biometrics.  |
| Step 2. Clicked "Add Passkey" -> Windows Security dialog box | See ** 1 ** in [Windows OS Dialogues](Windows OS Dialogues) | This is confusing as the website talked about biometrics/screenlock... but the OS presented a window that asked me for my pin. The website could instead say something like "You can use your compatible smartphone, Windows Hello, iCloud Keychain"... | 
| Step 3. Clicked "Use Another Device" | See ** 2 ** in [Windows OS Dialogues](Windows OS Dialogues) | | 
| Step 4. Clicked "Use iPhone, iPad, or Android device" | See ** 3** in [Windows OS Dialogues](Windows OS Dialogues) | | 
| Step 5. Device Connected! Screen | See ** 4 ** in [Windows OS Dialogues](Windows OS Dialogues) | | 
| Step 6.  Passkey Saved Screen | See ** 5 ** in [Windows OS Dialogues](Windows OS Dialogues) | | 
| Step 7. Click "Continue" in OS dialog from Step 6. | Kayak shows a passkey registered to Google Chrome | Not super helpful... should show either from iCloud or Windows Hello... But this might also be a privacy preservation? So the website doesn't learn anything extra from WebAuthn/CTAP2 about the devices being used??? <br> Google's implementaion has created date, last used, browser used, and location info... Kayak's website only has last used... maybe enough for most users? If they know for sure how many passkeys are currently linked to an account, and the devices that can use them. Could still give more info. <br> Tradeoff -- Privacy vs Enough information to know if (an extra passkey has been added/compromised),... websites likely already know all of the mentioned info... it's the appearance of privacy preservation.. not actual privacy preservation...  



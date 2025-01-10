# Cognitive Walkthrough

## Adding a Passkey on Windows
| Step - Action | What happened | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
|Step 0. Passkey Registration Page | "It works with the same face, fingerprint or PIN you already use to unlock your device. We don't store your face, fingerprint or PIN data."  | Useful information that gives good context (your method on your device). <br> First website to mention they don't store the biometric data! <br> People may conflate passkeys with biometrics. |
|Step 1. Click "Set up"  | Same Win11OSdialog.md  |  |
--skipping Windows Dialog -- 
|Step 2. Passkeys Page | Labeled the Passkey "iCloud Keychain", and included the setup date. <br> Tells the user that if they are sharing their account, the other person will need to setup their own passkey! <br> Also suggests using a different cloud service account. | When telling the user to setup a passkey with a different cloud provider, they use the phrasing "Apple ID"... but when displaying info about the passkey it says "iCloud Keychain"... need to be consistent with terminology (users may not even know the difference between them and it might add confusion).   |
|Step 3. Displaying additional Passkey information (drop downs) | Use passkey on different devices, including computer  | SUPER BAD PHRASING -- "You can also sign in with the passkey on devices that aren't assoicated with your cloud servbice account, but the steps are different." -- Links to a general help page... This is trying to say something like "You can use your smartphone to sign in on your desktop, even if your desktop doesn't have a passkey." but it gets REALLY lost... |
|Step 4. Sharing passkeys with friends and family | Paragraph 2 -- confusing text  | SUPER BAD PHRASING -- "If they don’t want to set up their own passkey, they can choose to sign in with a passkey from another device. As long as your phone is near their devices, the two devices will be connected through bluetooth and you will be prompted to approve the sign-in on your phone." -- If User1 has a passkey on Device1, and User2 doesn't want to use Passkeys on Device2... User2's device2 can connect via bluetooth (e.g., airdrop) to device1 if it is nearby, and User1 can approve the passkey login. |
|Step 5. Use passkeys with 2-step verification | Leaves 2FA on for the user  | Maybe bad design as Passkeys inherently use 2FA... |
|Step 6. Privacy Considerations |   | Good information. <br> Nit picky --- the biometric unlocks the credential, and isn't the credential itself... making this distinction could help prevent users from conflating the 2.   |

## Notes
1. The intial description says "easier and safer".


## Signing in with a Passkey on Windows
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Passwords are default, Passkey is a white button. If you click Use a Passkey and you don’t have one, then Windows OS assumes you must have a passkey on a different device. <br><br> **This must have only showed up because we were playing with passkeys – on a new account (turk@internet) this didn’t happen.**   | Put in email first – need this to know which account.  <br><br> Sign in with a Passkey is a white button and is non-default. 


# Screenshots
## [Windows Screenshots](windows_SS) 
These screenshots are from Windows 11, using Google Chrome, and viewing https://target.com... Taken on 4/25/2024

## [macOS Screenshots](macOS_SS)
These screenshots are from macOS Sonoma, using Google Chrome, and viewing https://target.com... Taken on ---

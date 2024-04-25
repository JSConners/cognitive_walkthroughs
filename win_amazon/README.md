# Cognitive Walkthrough

## Adding a Passkey on Windows
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Navigate to Passkey page | Has useful information about what a Passkey is, how to share them, privacy considerations. Amazon doesn’t see your biometrics.<br><br> Selling it with “easier and safer than passwords”. Uses the same face, fingerprint or PIN you already use to unlock your device. We don’t store your face, fingerprint, or PIN data.” <br><br> Failure – could use some of the info from Privacy considerations up in the main area. Bunch of good information here, we could potentially build this into a mental model in a new UI. <br> 
| Account → Login and Security → sign in with password → Passkey → Add a passkey – Windows OS Making sure it’s you – Let’s save a passkey on this device … defaults to PIN, or use another device | Success – who you are logging in as, and to what service. Labeled as Windows Security – so you are reasonably sure it is Windows OS. Communicates it’s coming from Chrome. Says where the passkey is saved.<br><br>Failure –  no context about what a passkey is, build a mental model.
| Put in PIN – You can now use Windows Hello to sign in with your face, fingerprint, or PIN. Gives email address and site. All in the OS | Success – OS dialog. <br><br> **Note – once you type four digits, the Windows dialog goes away. No enter key. Feels fast.* 
|Choosing another device – Chrome detects your Android phone is registered as a Passkey device, so that is the default option. Can also use Iphone, Ipad, Android device, Security key, or this windows device | Success – Choose where to save this passkey. Giving users control and info that passkeys are stored on devices.
|When choosing iPhone, or Android, it brings up a dialog to turn on Bluetooth. It says you need to turn it on temporarily and they’ll turn it off | Failure: Doesn’t say why Bluetooth is needed. <br><br> Success: They turn it back off for you when done.
| Now has a QR Code screen | Success: Tells you directly what to do – scan code, where saving code, saving it for amazon.com. <br><br> Failure – leaves you the email address for the account. | Then walk through the iphone process, save the key, success on the desktop in Amazon.





## Signing in with a Passkey on Windows
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
| Passwords are default, Passkey is a white button. If you click Use a Passkey and you don’t have one, then Windows OS assumes you must have a passkey on a different device. <br><br> **This must have only showed up because we were playing with passkeys – on a new account (turk@internet) this didn’t happen.**   | Put in email first – need this to know which account.  <br><br> Sign in with a Passkey is a white button and is non-default. 


## Registering for a new Account on Windows
| Step | Success and Failure | Design Suggestions or Comments |
| ---- | ----------- | ---------- |
|Signed up for an account using name, email, phone, and password. | Failure: Forces you to use a phone number 

# Screenshots

These screenshots are from Windows 11, using Google Chrome, and viewing https://amazon.com... Taken on 4/25/2024
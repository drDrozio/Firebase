import pyrebase

config={
	"apiKey": "AIzaSyCJ_p-TCd7a16e5MiCSg0vcDPWGRjTAMbk",
    "authDomain": "fire-8a42b.firebaseapp.com",
    "databaseURL": "https://fire-8a42b.firebaseio.com",
    "projectId": "fire-8a42b",
    "storageBucket": "fire-8a42b.appspot.com",
    "messagingSenderId": "218150852345",
    "appId": "1:218150852345:web:d10d202f7961cc17917428",
    "measurementId": "G-QRVRRVYWJM"
}

firebase=pyrebase.initialize_app(config)

auth=firebase.auth()

email=input("Enter Email : ")
password=input("Enter Password : ")

## Creating User ID and Password
# user=auth.create_user_with_email_and_password(email,password)
# print("User Account Created")

## Sign In
signin=auth.sign_in_with_email_and_password(email,password)
print("Sign In Successful")

## Email verification
# auth.send_email_verification(signin['idToken'])
# print("Email Verification Sent")

## Reset Password
# auth.send_password_reset_email(email)
# print("Password Reset Mail Sent")


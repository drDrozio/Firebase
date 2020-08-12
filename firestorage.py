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

storage=firebase.storage()

## Uploading files (Image,Text,Audio)
# storage.child("Images/newimage.jpg").put("messi.jpg")
# print("Image Uploaded")

storage.child("Images/newimage.jpg").download("downloaded.jgp")
print("Image Downloaded")
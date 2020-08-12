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

db=firebase.database()

data={"name":"Whiskey"}

## Pushing to database
# db.child("users").push(data)
# print("Data added to realtime database")

## Pushing to db with own key
# db.child("users").child("MyKey").set(data)

## Updating
db.child("users").child("MyKey").update({"name":"Agent Whiskey"})
db.child("users").child("-MEWO3IeNBXC-QnpHsh0").update({"name":"Drozio"})
print("Database Updated")

## Retreive
users=db.child("users").get()
print(users.val())
print()

all_users=db.child("users").get()
for user in all_users.each():
	print(user.val())
	print(user.key())


## Delete
db.child("users").child("MyKey").remove()
print("User removed")
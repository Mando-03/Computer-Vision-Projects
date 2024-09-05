import firebase_admin
from firebase_admin import credentials , db


cred = credentials.Certificate("serviceAccountKey.json") # get it from firebase
firebase_admin.initialize_app(cred, {'databaseURL': "get your own buddy"})



ref = db.reference('Students')  
data = {
    "182002" : {
        "name" : "Mohamed Mandor",
        "Major": "Software Engineering",
        "total Attendance" : 6,
        "last_Attendance_Time" : "2024-9-4 18:40:00"
    },
    "852741": {
        "name": "Andrej Karpathy",
        "Major": "openai",
        "total Attendance": 6,
        "last_Attendance_Time": "2024-9-4 18:40:00"
    },
    "963852": {
        "name": "Elon Musk",
        "Major": "Mad Ideas Production",
        "total Attendance": 0,
        "last_Attendance_Time": "2024-9-4 18:40:00"
    }
}

for key,value in data.items():
    ref.child(key).set(value)  
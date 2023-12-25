import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-68370-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "559039":
        {
            "name": "Yekaditya",
            "major": "Meachine Learning",
            "starting_year": 2019,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:34:14"
        }
}

for key, value in data.items():
    ref.child(key).set(value)

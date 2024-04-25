import datetime
from google.cloud import firestore

db = firestore.Client()
brasilia_tz = datetime.timezone(datetime.timedelta(hours=-3))

def addUser():
    doc_ref = db.collection("users").document("pmoreira")
    doc_ref.set({"first": "Pedro", "last": "Moreira", "born": 2001})

def listUsers():
    users_ref = db.collection("users")
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def listWithBasicFilter():
    pass

def putUser():
    data = {"first": "Pedro", "last": "Moreira", "born": 2001, "update_at": datetime.datetime.now(tz=brasilia_tz)}
    db.collection("users").document("pmoreira").set(data)
    
def putFieldUser():
    doc_ref = db.collection("users").document("pmoreira")
    doc_ref.update({ "active": True })

listUsers()
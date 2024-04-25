from google.cloud import firestore

db = firestore.Client()

def addUser():
    doc_ref = db.collection("users").document("pmoreira")
    doc_ref.set({"first": "Pedro", "last": "Moreira", "born": 2001})

def listUsers():
    users_ref = db.collection("users")
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

listUsers()
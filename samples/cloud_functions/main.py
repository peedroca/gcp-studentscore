import functions_framework
from google.cloud import firestore

@functions_framework.http
def hello(request):
    db = firestore.Client()
    
    users_ref = db.collection("users")
    docs = users_ref.stream()

    users = []
    for doc in docs:
        users.append(f"{doc.id} => {doc.to_dict()}")
        
    return users

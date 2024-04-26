import functions_framework
import datetime
from google.cloud import firestore

brasilia_tz = datetime.timezone(datetime.timedelta(hours=-3))

@functions_framework.http
def hello(request):
    db = firestore.Client()
    
    users_ref = db.collection("users")
    docs = users_ref.stream()

    users = []
    for doc in docs:
        users.append(f"{doc.id} => {doc.to_dict()}")
        
    return users

@functions_framework.http
def save_message(request):
    db = firestore.Client()

    code = request.args.get("code")
    author = request.args.get("author")
    response = request.args.get("response")

    message = {
        "author": author, 
        "code": code, 
        "response": response, 
        "update_at": datetime.datetime.now(tz=brasilia_tz)
    }

    doc_ref = db.collection("discord").document('{}_{}'.format(code, author))
    doc_ref.set(message)

    return "Ok!"
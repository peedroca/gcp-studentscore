import functions_framework
import datetime
from google.cloud import firestore

brasilia_tz = datetime.timezone(datetime.timedelta(hours=-3))

@functions_framework.http
def hello():
    return "Working"

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


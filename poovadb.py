from google.cloud import firestore
from google.oauth2 import service_account
from google.cloud.firestore import FieldFilter
from google.cloud.firestore_v1.field_path import FieldPath

# Path to your service account key file
SERVICE_ACCOUNT_KEY_PATH = "poovakey.json"

# Load credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_PATH)

# Initialize Firestore client with explicit credentials
db = firestore.Client(credentials=credentials)


def update_document():

    imeis = [866228071946701,
    866228071945026,
    866228071903389,
    866228071941926,
    866228071946701,
    866228071945026,
    866228071903389,
    866228071942148,
    866228071902209,
    866228071941926,
    866228071942148,
    866228071902209,
    866228071942148,
    866228071902209]

    for imei in imeis:
        # Using FieldFilter with properly formatted field name
        users_ref = db.collection('productsMeizu').where(
            filter=FieldFilter("`IMEI 1 `", "==", imei)
        )
        docs = users_ref.stream()

        for doc in docs:
            doc_ref = db.collection('productsMeizu').document(doc.id)
            doc_ref.update({"state": "1",
                            "buyer2": "",
                            "delidate2": ""})
            
            print(f'{doc.id} => {doc.to_dict().get("state")} => {doc.to_dict().get("buyer2")} => {doc.to_dict().get("delidate2")}')
        print("--------------------------------------------------")

def delete_document():

    deliveryIDs = ["1234567890","0987654321"]

    for dID in deliveryIDs:
        # Using FieldFilter with properly formatted field name
        users_ref = db.collection('deliveryordersRetailer').where(
            filter=FieldFilter("`deliveryID`", "==", dID)
        )
        docs = users_ref.stream()

        for doc in docs:
            doc_ref = db.collection('deliveryordersRetailer').document(doc.id)
            print(f'{doc.id} => {doc.to_dict().get("deliveryID")} ')

            doc_ref.delete()
            print("------------ DELETED -----------------")

print("Poova DB")
update_document()
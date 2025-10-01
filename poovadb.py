from google.cloud import firestore
from google.oauth2 import service_account
from google.cloud.firestore import FieldFilter
from google.cloud.firestore_v1.field_path import FieldPath
import csv

# Path to your service account key file
SERVICE_ACCOUNT_KEY_PATH = "poovakey.json"

# Load credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_PATH)


# Initialize Firestore client with explicit credentials
db = firestore.Client(credentials=credentials,project="poovaservice")


def update_document():

    imeis = [353104320127114,
353104320100087,
353104320234126,
353104320128658,
353104320232815,
353104320172276,
353104320126850,
353104320173027,
353104320126702,
353104320126959]

    for imei in imeis:
        # Using FieldFilter with properly formatted field name
        users_ref = db.collection('productsAlcatel').where(
            filter=FieldFilter("`IMEI 1 `", "==", imei)
        )
        docs = users_ref.stream()

        for doc in docs:
            doc_ref = db.collection('productsAlcatel').document(doc.id)
            doc_ref.update({"state": "1",
                            "buyer2": "",
                            "delidate2": ""})
            
            print(f'{doc.id} => {doc.to_dict().get("state")} => {doc.to_dict().get("buyer2")} => {doc.to_dict().get("delidate2")}')
        print("--------------------------------------------------")


def job_setstate():

    countme=0

    # Using FieldFilter with properly formatted field name
    imei_ref = db.collection('productsTCL').where(filter=FieldFilter("`buyer2`", "==", "")).where(filter=FieldFilter("`state`", "==", "2"))
    docs = imei_ref.stream()

    for doc in docs:
        doc_ref = db.collection('productsTCL').document(doc.id)
        doc_ref.update({"state": "1","delidate2": ""})
        countme=countme+1      
        print(f'{doc.id} => {doc.to_dict().get("state")} => {doc.to_dict().get("buyer2")} => {doc.to_dict().get("delidate2")}')
        print("------------ ",countme," --------------")


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

def clean_number(value, is_int=False):
    """Remove commas and convert to float or int safely."""
    if not value:
        return 0 if is_int else 0.0
    value = value.replace(",", "")
    return int(value) if is_int else float(value)


## ------------------ Feed CSV data ------------------------------------------------------
def upload_csv_to_firestore(csv_file_path):
    collection_ref = db.collection("warehouse")
    
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Skip header row if exists
        next(reader, None)
        
        for row in reader:
            
            doc_data = {
                "matID": row[0],
                "name": row[1],
                "model": row[2],
                "description": row[3],
                "receivedDate": row[4],
                "cost": clean_number(row[5]),
                "sellprice": clean_number(row[6]),
                "note": row[7],
                "qty": clean_number(row[8], is_int=True)
            }
            
            # Use matID as document ID (optional), otherwise Firestore auto-generates
            collection_ref.document(doc_data["matID"]).set(doc_data)

    print("CSV upload completed successfully")
## ----------------------------------------------------------------------------------------


print("Poova Service DB - Job #3")

print("Done")
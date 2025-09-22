sudo apt install python3.12-venv
python3 -m venv poova
source poova/bin/activate
pip install google-cloud-firestore

==============================================

from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Reference a specific document
doc_ref = db.collection("users").document("alovelace")

# Get the document snapshot
doc_snap = doc_ref.get()

# Check if the document exists and convert its data to a dictionary
if doc_snap.exists:
    user_data = doc_snap.to_dict()
    print(f"Document data: {user_data}")
    print(f"User's first name: {user_data.get('first_name')}")
else:
    print("No such document!")


============================================================================

from google.cloud.firestore import FieldFilter

# Filter for documents where 'age' is greater than 30
query = db.collection(u'users').where(filter=FieldFilter(u'age', u'>', 30))
filtered_docs = query.stream()

for doc in filtered_docs:
    print(f'{doc.id} => {doc.to_dict()}')

# Filter for documents where 'city' is 'London'
query = db.collection(u'users').where(filter=FieldFilter(u'city', u'==', u'London'))
city_docs = query.stream()

for doc in city_docs:
    print(f'{doc.id} => {doc.to_dict()}')

===================================================

doc_ref = db.collection(u'users').document(u'alovelace')
doc = doc_ref.get()

if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'Document does not exist!')

======================================================

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

print("Poova DB")

imeis = [350801970499171,
350801970494636,
350801970483837,
350475480246990,
350475480234392]

# Using FieldFilter with properly formatted field name
users_ref = db.collection('products').where(
    filter=FieldFilter("`IMEI 1 `", "==", 350338990006215)
)
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict().get("IMEI 1 ")}')

=============================================================


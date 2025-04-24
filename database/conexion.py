import firebase_admin
from firebase_admin import credentials

def iniciar_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("database/firebase_config.json")
        firebase_admin.initialize_app(cred)

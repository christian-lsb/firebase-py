from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("configs/firebase_config.json")
firebase_admin.initialize_app(cred)

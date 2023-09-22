from typing import Union
from fastapi import FastAPI
from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("configs/firebase_config.json")
firebase_admin.initialize_app(cred)


app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/login')
def login(email: str, password: str):
    try:
        user = firebase_admin.auth.get_user_by_email(email)
    except:
        None
        return {"message": "Login successful"}
    return

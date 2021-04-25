from fastapi import FastAPI, Depends, HTTPException, status
from layers import caesar, crypto
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os


app = FastAPI()
security = HTTPBasic()


username = os.environ.get('USERNAME')
passsword = os.environ.get('PASSWORD')


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, username)
    correct_password = secrets.compare_digest(credentials.password, passsword)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post('/encode_crypto')
def encode_crypto(text, username: str = Depends(get_current_username)):
    value = crypto(text)
    return value


@app.post('/decode_crypto')
def decode_crypto(text, username: str = Depends(get_current_username)):
    value = crypto(text, method="decrypt")
    return value


@app.post('/encode_caesar')
def encode_caesar(text, username: str = Depends(get_current_username)):
    value = caesar(text)
    return value


@app.post('/decode_caesar')
def decode_caesar(text, username: str = Depends(get_current_username)):
    value = caesar(text, method="decrypt")
    return value
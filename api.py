from fastapi import FastAPI
from layers import caesar, crypto


app = FastAPI()


@app.get('/')
def index():
    return 'Ok'


@app.post('/encode_crypto')
def encode_crypto(text):
    value = crypto(text)
    return value


@app.post('/decode_crypto')
def decode_crypto(text):
    value = crypto(text, method="decrypt")
    return value
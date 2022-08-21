from typing import Union
from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Optional
import json
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'roleUsers.log',
    filemode='w'
)

app = FastAPI()

@app.get("/")
def getRoleUsers():
    data=''
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/roleUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    if data != '' and data != 'Not found':
            logging.info('GET method executed successfully')
            return {"roleUsers": response.json()}
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: No Content"}

@app.get("/roleUsers/encryptedToken={encryptedToken}")
def read_roleUsers(encryptedToken: str):
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/roleUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    wRole = ''
    for usr in data:
        if usr['encryptedToken'] == encryptedToken:
            wRole = usr['role']
            wExpirationDate = usr['expirationDate']
    if wRole != '' and wRole != 'Not found':
        logging.info('GET method executed successfully')
        return {"encryptedToken": encryptedToken, "role": wRole, "expirationDate": wExpirationDate, }
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: NoContent"}
    
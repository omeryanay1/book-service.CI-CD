# connectionController.py
import requests
import json

URL = "http://0.0.0.0:5001"  # Base URL for the book service

def http_get(resource: str):
    response = requests.get(url=f"{URL}/{resource}", headers={"Content-Type": "application/json"})
    return response

def http_delete(resource: str):
    response = requests.delete(url=f"{URL}/{resource}", headers={"Content-Type": "application/json"})
    return response

def http_post(resource: str, data: {}):
    response = requests.post(url=f'{URL}/{resource}', headers={"Content-Type": "application/json"}, data=json.dumps(data))
    return response

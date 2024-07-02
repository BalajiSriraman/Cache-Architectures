from typing import Union
from fastapi import FastAPI, HTTPException
from pyignite import Client
import json

app = FastAPI()


# Initialize Ignite client
ignite_client = Client()
ignite_client.connect('localhost', 10800)  

@app.get("/")
async def read_root():
    return {"Ping": "Pong"}

@app.post("/create/{key}")
async def create_item(key: str, value: dict):
    cache = ignite_client.get_or_create_cache("my_cache")
    
    if cache.contains_key(key):
        raise HTTPException(status_code=400, detail="Key already exists")
    
    cache.put(key, json.dumps(value))
    return {"message": f"Item created with key: {key}"}

@app.get("/read/{key}")
async def read_item(key: str):
    cache = ignite_client.get_or_create_cache("my_cache")
    
    value = cache.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return json.loads(value)
    
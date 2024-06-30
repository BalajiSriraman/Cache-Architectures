from typing import Union
from fastapi import FastAPI, HTTPException
import json
from pymemcache.client.base import Client

app = FastAPI()

memcached_client = Client(('memcached', 11211))

@app.get("/")
async def read_root():
    return {"Ping": "Pong"}

@app.post("/create/{key}")
async def create_item(key: str, value: dict):
    if memcached_client.get(key) is not None:
        raise HTTPException(status_code=400, detail="Key already exists")
    
    memcached_client.set(key, json.dumps(value))
    return {"message": f"Item created with key: {key}"}

@app.get("/read/{key}")
async def read_item(key: str):
    value = memcached_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return json.loads(value.decode('utf-8'))
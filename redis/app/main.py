from typing import Union

from fastapi import FastAPI, HTTPException

app = FastAPI()

from redis import Redis
import json

redis = Redis(host='localhost', port=6379, db=0)  # Adjust these settings as needed

@app.get("/")
async def read_root():
    return {"Ping": "Pong"}

@app.post("/create/{key}")
async def create_item(key: str, value: dict):
    if redis.exists(key):
        raise HTTPException(status_code=400, detail="Key already exists")
    
    redis.set(key, json.dumps(value))
    return {"message": f"Item created with key: {key}"}

@app.get("/read/{key}")
async def read_item(key: str):
    value = redis.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return json.loads(value)
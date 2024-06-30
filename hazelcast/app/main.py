from typing import Union
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

import hazelcast



# Get a distributed map

@app.get("/")
async def read_root():
    client = hazelcast.HazelcastClient()


    distributed_map = client.get_map("distributed-map")

    print("Map Size:", distributed_map.size().result())

    return {"Ping": "Pong"}

# @app.post("/create/{key}")
# async def create_item(key: str, value: dict):
#     if hz_map.contains_key(key):
#         raise HTTPException(status_code=400, detail="Key already exists")
    
#     hz_map.put(key, json.dumps(value))
#     return {"message": f"Item created with key: {key}"}

# @app.get("/read/{key}")
# async def read_item(key: str):
#     value = hz_map.get(key)
#     if value is None:
#         raise HTTPException(status_code=404, detail="Item not found")
    
#     return json.loads(value)

# @app.on_event("shutdown")
# async def shutdown_event():
#     client.shutdown()
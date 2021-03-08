from fastapi import FastAPI
import uuid

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/health")
def read_health():
    return {"health": "is alive"}


@app.get("/uuid")
def generate_id():
    return {"uuid": uuid.uuid4()}

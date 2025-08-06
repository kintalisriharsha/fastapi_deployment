from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_root():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path, media_type="text/html")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
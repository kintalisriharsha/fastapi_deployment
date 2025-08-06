from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_root():
    index_path = os.path.join(os.path.dirname(__file__), "static/index.html")
    return FileResponse(index_path, media_type="text/html")

@app.get("/db_url")
def get_db_url():
    return {"DATABASE_URL": DATABASE_URL}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
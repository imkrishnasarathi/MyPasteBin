from fastapi import FastAPI, HTTPException
from uuid import uuid4
import os

app = FastAPI()
PASTE_DIR = "pastes"
os.makedirs(PASTE_DIR, exist_ok=True)

@app.post("/paste")
def create_paste(text: str):
    paste_id = str(uuid4())[:8]
    paste_path = os.path.join(PASTE_DIR, f"{paste_id}.txt")

    with open(paste_path, "w") as f:
        f.write(text)

    return {"id": paste_id, "url": f"http://localhost:8000/paste/{paste_id}"}

@app.get("/paste/{paste_id}")
def get_paste(paste_id: str):
    paste_path = os.path.join(PASTE_DIR, f"{paste_id}.txt")

    if not os.path.exists(paste_path):
        raise HTTPException(status_code=404, detail="Paste not found")

    with open(paste_path, "r") as f:
        return {"id": paste_id, "text": f.read()}

@app.delete("/paste/{paste_id}")
def delete_paste(paste_id: str):
    paste_path = os.path.join(PASTE_DIR, f"{paste_id}.txt")

    if os.path.exists(paste_path):
        os.remove(paste_path)
        return {"message": "Paste deleted"}
    else:
        raise HTTPException(status_code=404, detail="Paste not found")

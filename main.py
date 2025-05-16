from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai_api import generate_ad_copy
import json
import os

app = FastAPI()

# ✅ פונקציה ראשית לעמוד הבית
@app.get("/")
def read_root():
    return {"message": "NextGenAds backend is running 🚀"}

# ✅ מחלקת בריף לפרויקט חדש
class InitProjectRequest(BaseModel):
    client_id: str
    brand_story: str
    images: list
    default_target: str

# ✅ יצירת פרויקט לקוח
@app.post("/client/init-project")
def init_project(data: InitProjectRequest):
    client_data = {
        "client_id": data.client_id,
        "brand_story": data.brand_story,
        "images": data.images,
        "default_target": data.default_target,
        "campaigns": []
    }
    os.makedirs("clients", exist_ok=True)
    with open(f"clients/{data.client_id}.json", "w") as f:
        json.dump(client_data, f, indent=4)
    return {"status": "created", "client_id": data.client_id}

# ✅ קבלת קופי מה-AI
class CopyRequest(BaseModel):
    prompt: str

@app.post("/generate-copy")
def generate_copy(data: CopyRequest):
    copy = generate_ad_copy(data.prompt)
    return {"generated_copy": copy}

# ✅ מאפשר CORS מה-Frontend שלך
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

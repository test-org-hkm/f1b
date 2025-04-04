from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Get frontend URL from environment variable
frontend_url = os.getenv('FRONTEND_URL')

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BirthdayRequest(BaseModel):
    birth_date: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Birthday Calculator API"}

@app.post("/calculate-age")
def calculate_age(request: BirthdayRequest):
    try:
        birth_date = datetime.strptime(request.birth_date, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return {"age": age}
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD"} 
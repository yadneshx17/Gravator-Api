import subprocess
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import re

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY", "default-api-key")
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

@app.get("/gravatar/{email}")
def gravatar_lookup(email: str, api_key: str = Depends(get_api_key)):
    try:
        command = ["python3", "gmailtogravatar.py", email]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Error: {result.stderr.strip()}")

        raw_output = result.stdout.strip()
        cleaned_output = strip_ansi(raw_output)

        # Extract Data only
        info = {}
        patterns = {
            "display_name": r"Display Name\s*:\s*(.+)",
            "preferred_username": r"Preferred Username\s*:\s*(.+)",
            "profile_url": r"Profile URL\s*:\s*(.+)",
            "thumbnail_url": r"Thumbnail URL\s*:\s*(.+)",
            "about_me": r"About Me\s*:\s*(.+)",
            "location": r"Current Location\s*:\s*(.+)"
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, cleaned_output)
            info[key] = match.group(1).strip() if match else None

        return info

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

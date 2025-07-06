from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter()

@router.post("/upload")
async def upload_log(file: UploadFile = File(...)):
    contents = await file.read()
    lines = contents.decode().splitlines()
    
    suspicious = []
    for i, line in enumerate(lines):
        if any(keyword in line.lower() for keyword in ["failed password", "sudo", "chmod 777"]):
            suspicious.append(f"Line {i+1}: {line.strip()}")
    
    return {
        "message": "Suspicious Log Entries",
        "parsed_logs": suspicious
    }

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/logs/upload")
async def upload_log(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    lines = text.splitlines()
    suspicious = []

    for line in lines:
        if "failed password" in line.lower() or "chmod 777" in line.lower() or "sudo" in line.lower():
            suspicious.append(line)

    return {
        "message": "Suspicious logs found",
        "parsed_logs": suspicious
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

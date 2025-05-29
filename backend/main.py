from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Job Shop Quote App is running!"}

@app.post("/generate-quote")
async def generate_quote(file: UploadFile = File(...), quantity: int = Form(...)):
    return {"message": f"Received {file.filename} x{quantity}"}

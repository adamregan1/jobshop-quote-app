from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import math

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
async def generate_quote(
    file: UploadFile = File(...),
    quantity: int = Form(...),
    labor_hours: float = Form(...),
    commercial_parts_cost: float = Form(...),
    material_length_required: float = Form(...),  # in inches
    material_cost_per_nominal_bar: float = Form(...),
    nominal_bar_length: float = Form(...)
):
    # Calculate total cost based on formula
    labor_cost = labor_hours * 150
    commercial_cost = commercial_parts_cost * 1.25
    bars_needed = math.ceil(material_length_required / nominal_bar_length)
    material_cost = bars_needed * material_cost_per_nominal_bar * 1.25

    total = (labor_cost + commercial_cost + material_cost) * quantity

    # Example routing steps
    routing_steps = [
        {"step": "Saw Cut", "time_minutes": 10},
        {"step": "Lathe Op", "time_minutes": 15},
        {"step": "Mill Op", "time_minutes": 20},
        {"step": "Deburr", "time_minutes": 5},
        {"step": "Inspect", "time_minutes": 10},
    ]

    return {
        "file_received": file.filename,
        "quantity": quantity,
        "quote": round(total, 2),
        "routing": routing_steps
    }
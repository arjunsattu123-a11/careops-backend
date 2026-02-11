from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from datetime import datetime

# 1️⃣ Create app FIRST
app = FastAPI()

# 2️⃣ MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["careops_db"]

bookings = db["bookings"]
inventory = db["inventory"]


# 3️⃣ Health check
@app.get("/")
def root():
    return {"message": "CareOps backend running"}


# 4️⃣ Booking API (FINAL ROUND READY)
@app.post("/bookings")
def create_booking(name: str, service: str):

    service = service.strip().title()

    # Reduce inventory first (atomic)
    result = inventory.update_one(
        {
            "service": service,
            "available_slots": {"$gt": 0}
        },
        {
            "$inc": {"available_slots": -1}
        }
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=400,
            detail="No slots available"
        )

    booking = {
        "name": name,
        "service": service,
        "status": "created",
        "created_at": datetime.utcnow()
    }

    bookings.insert_one(booking)

    return {"message": "Booking confirmed"}
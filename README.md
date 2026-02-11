# CareOps Backend API

Production-ready FastAPI backend for managing service bookings and real-time inventory tracking using MongoDB.

---

# Features

- Create service bookings
- Real-time inventory slot reduction
- Prevent overbooking using atomic MongoDB updates
- Proper HTTP error handling
- Clean REST API structure

---

# Tech Stack

- Python 3
- FastAPI
- MongoDB
- Uvicorn
- PyMongo

---

# Project Structure

careops-backend/
│── main.py
│── .gitignore
│── requirements.txt


---

# How to Run Locally

1. Clone the repository

```
git clone https://github.com/arjunsattu123-a11/careops-backend.git
cd careops-backend
```

2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Start server

```
uvicorn main:app --reload
```

Server runs at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

---

# API Endpoints

# Health Check
GET /

Returns server status.

# Create Booking
POST /bookings

Query Params:
- name (string)
- service (string)

Prevents booking if no slots available.

---

#Logic Explanation

Before creating a booking, the system:

1. Checks if service has available slots (> 0)
2. Atomically reduces slot count using `$inc`
3. Creates booking record
4. Returns proper HTTP error if no slots available

This prevents race conditions and overbooking.

---

# Author

Arjun  
Backend Developer | Python | FastAPI | MongoDB

# DeepFleet-AI 🚚📦  
**AI-Powered Logistics Fleet Optimization System**

DeepFleet-AI is an end-to-end, production-grade fleet management and route optimization platform built using **Machine Learning**, **AWS Cloud**, and **React**. It enables intelligent delivery routing, ETA prediction, and real-time fleet visibility using historical delivery data and live tracking.

---

## 🌐 Tech Stack

### 🧠 Backend & ML
- **Python**, **Flask**
- **Scikit-learn**, **Pandas**, **NumPy**, **XGBoost**
- **Geopy**, **Haversine**, **Folium**

### 🌍 Frontend (optional)
- **React.js**, **Tailwind CSS**, **Recharts**

### ☁ Cloud/DevOps
- **AWS EC2**, **S3**, **CloudWatch**, **Lambda**
- **Docker**, **GitHub Actions**

---

## 📁 Project Structure

```bash
DeepFleet-AI/
├── backend/
│   ├── main.py                # FastAPI entrypoint
│   ├── routes/
│   │   ├── fleet.py
│   │   └── auth.py
│   ├── services/
│   │   └── optimizer.py       # Route optimization logic
│   ├── models/
│   │   └── delivery_model.py  # SQLAlchemy models
│   └── utils/
│       └── geo_utils.py       # Geolocation, Haversine formula
│
├── ml/
│   ├── model.py               # Fleet routing ML model
│   ├── train.py               # Training script
│   ├── predict.py             # Inference logic
│   └── data/
│       └── delivery_logs.csv  # Sample training data
│
├── frontend/                  # Optional React Dashboard
│   └── src/
│       └── components/
│       └── pages/
│
├── docker/
│   └── Dockerfile
│   └── docker-compose.yml
│
├── scripts/
│   └── seed_db.py             # Populate DB
│   └── scheduler.py           # Fleet update scheduler (Lambda)
│
├── infrastructure/
│   └── terraform/             # AWS setup
│   └── sagemaker-deploy.tf                                                                                                                                 
├── api/                    # Flask backend APIs
│   ├── app.py              # API entrypoint
│   ├── routes/
│   │   └── delivery_routes.py
│   └── utils/
│       └── helpers.py 
├── README.md
└── requirements.txt  
````

---

## 🚀 Features

* ✅ Predict ETA (Estimated Time of Arrival) using ML
* ✅ Route Optimization using Haversine/Mapbox APIs
* ✅ Vehicle Type Classification
* ✅ Data ingestion from CSV or REST
* ✅ Scalable deployment with Docker

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/hq969/DeepFleet-AI.git
cd DeepFleet-AI
```

### 2. Backend Setup

```bash
cd api/
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
python app.py
```

### 3. Frontend Setup (Optional)

```bash
cd frontend/
npm install
npm run dev
```

### 4. Run Docker (Alternative)

```bash
docker build -t deepfleet-backend .
docker run -p 5000:5000 deepfleet-backend
```

---

## 📊 Sample API

**Endpoint:** `/predict_eta`

**POST Body:**

```json
{
  "origin": [28.6139, 77.2090],
  "destination": [28.5355, 77.3910],
  "vehicle_type": "van"
}
```

**Response:**

```json
{
  "eta_minutes": 42.5
}
```

---

## 📂 Dataset

Sample delivery logs can be found in:

```
ml/data/delivery_logs.csv
```

You can expand this with more real-world logs.

---

## 📌 To-Do

* [ ] Integrate Mapbox/Google Directions API
* [ ] Add MongoDB or PostgreSQL for delivery log storage
* [ ] Real-time GPS data streaming via AWS Kinesis

---

## 👨‍💻 Contributors

* **Harsh Sonkar** — [LinkedIn](www.linkedin.com/in/harsh-sonkar-232573250)

---

## 📄 License

MIT License. Free to use and modify with attribution.

---



from fastapi import FastAPI
from routes import fleet, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(fleet.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to DeepFleet-AI"}

from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(user: dict):
    return {"token": "fake-token"}

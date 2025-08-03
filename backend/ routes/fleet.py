from fastapi import APIRouter
from services.optimizer import optimize_route

router = APIRouter(prefix="/fleet")

@router.post("/optimize")
def optimize(data: dict):
    return optimize_route(data)

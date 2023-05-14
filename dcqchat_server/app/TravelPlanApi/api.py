from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
def index():
    return "index"

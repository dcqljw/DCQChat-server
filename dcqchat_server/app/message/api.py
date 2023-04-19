import loguru
from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy.orm import Session

from app import socket_manager, get_db
from cruds import usercrud
from schemas import userschemas

logger.add("test.log")
loguru
router = APIRouter()


@socket_manager.on("join", namespace="/ws")
async def handle_join(sid, data, **kwargs):
    print(sid)
    print(data)
    print(**kwargs)
    await socket_manager.emit('join', 'user', namespace='/ws')


@router.get("/")
def test(user_id: int):
    pass


@router.post('/create')
def create(user: userschemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("msg")
    return usercrud.create_user(db=db, user=user)

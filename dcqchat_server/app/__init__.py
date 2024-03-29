from fastapi import FastAPI
from fastapi_socketio import SocketManager

from models import usermodel
from sql.database import SessionLocal, engine

usermodel.Base.metadata.create_all(bind=engine)
app = FastAPI()
socket_manager = SocketManager(app, mount_location="/ws")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_app():
    from app.message import api as mes_api
    from app.TravelPlanApi import api as tp_api
    app.include_router(mes_api.router, prefix="/message")
    app.include_router(tp_api.router, prefix="/tp")
    return app

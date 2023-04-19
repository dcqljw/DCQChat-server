from sqlalchemy.orm import Session

from models import usermodel
from schemas import userschemas


def create_user(db: Session, user: userschemas.UserCreate):
    fake_password = user.password + "dcqchat"
    db_user = usermodel.User(email=user.email, password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(usermodel.User).filter(usermodel.User.id == user_id).first()



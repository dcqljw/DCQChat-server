from sqlalchemy import Column, Integer, String

from sql.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), unique=True, index=True)
    password = Column(String(256))

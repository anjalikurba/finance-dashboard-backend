from sqlalchemy.engine import default
from sqlalchemy import column,Integer,String,Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = column(Integer,primary_key=True)
    name = column(String)
    email = column(String,unique=True)
    password = column(String)
    role = column(String)
    is_active = column(Boolean,default=True)
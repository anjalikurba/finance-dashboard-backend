from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    description = Column(String)
    
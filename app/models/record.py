from sqlalchemy import column,Integer,Float,String,Date
from app.database import Base

class Record(Base):
    __tablename__ = "records"
    id = column(Integer,primary_key=True)
    amount = column(float)
    type = column(String)
    category = column(String)
    Date = column(Date)
    description = column(String)
    
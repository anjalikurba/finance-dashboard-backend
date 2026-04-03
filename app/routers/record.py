from sys import prefix
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate

router = APIRouter(
    prefix="/records",
    tags=["records"]
)

@router.post("/")
def create_record(record:RecordCreate,db:Session=Depends(get_db)):
    new_record = Record(
        amount=record.amount,
        type=record.type,
        category=record.category,
        date=record.date,
        description=record.description
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/")
def get_records(db:Session=Depends(get_db)):
    return db.query(Record).all()
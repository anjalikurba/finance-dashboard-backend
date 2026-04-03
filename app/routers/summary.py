from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.record import Record
from app.services.summary_services import calculate_summary

router = APIRouter(
    prefix="/summary",
    tags=["summary"]
)

@router.get("/")
def get_summary(db:Session=Depends(get_db)):
    records = db.query(Record).all()
    return calculate_summary(records)
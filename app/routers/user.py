from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.database import get_db
from app.schemas.user import UserCreate


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/")
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_user = user(email=user.email,hashed_password=user.hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

@router.get("/")
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()
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
    new_user = User(
        name=user.name, 
        email=user.email, 
        password=user.password, 
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()
from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, record  # Import models so SQLAlchemy knows about them
from app.routers.user import router as user_router
from app.routers.record import router as record_router
from app.routers.summary import router as summary_router

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(record_router)
app.include_router(summary_router)

@app.get("/")
def read():
    return {"message":"Welcome to Finance Dashboard"}
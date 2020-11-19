from typing import List

from src.config import SYSTEM_NAME
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from src import controller
from src.database import schemas
from src.database.scripts import get_db

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    return f"<body><h1>API of {SYSTEM_NAME}</h1></body>"


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return controller.create_user(user, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controller.read_users(skip=skip, limit=limit, db=db)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id, db: Session = Depends(get_db)):
    try:
        return controller.read_user(user_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

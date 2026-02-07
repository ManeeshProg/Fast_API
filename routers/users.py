from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.users import User
from schemas.users import UserCreate, UserResponse

router=APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user=User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
from fastapi import APIRouter,Depends,HTTPException
from models import Car
from database.database import get_db
from sqlalchemy.orm import Session
from schemas.cars import CarCreate, CarResponse

router = APIRouter()
@router.post("/", response_model=CarResponse)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/{car_id}", response_model=CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    db_car=db.query(Car).filter(Car.id==car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
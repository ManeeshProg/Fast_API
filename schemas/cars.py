from pydantic import BaseModel

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    owner_id: int
    price: int


class CarResponse(BaseModel):
    id: int
    make: str
    model: str
    year: int
    owner_id: int
    price: int
    class Config:
        from_attributes = True
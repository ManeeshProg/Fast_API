from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="Users"
    id=Column(Integer, primary_key=True, index=True)
    user_name=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    password=Column(String,nullable=False)
    
    
    cars = relationship("Car", back_populates="owner")
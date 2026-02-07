from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Car(Base):
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey("Users.id"))
    owner = relationship("User", back_populates="cars")
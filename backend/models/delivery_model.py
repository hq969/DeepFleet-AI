from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Delivery(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True)
    location = Column(String)
    lat = Column(Float)
    lon = Column(Float)

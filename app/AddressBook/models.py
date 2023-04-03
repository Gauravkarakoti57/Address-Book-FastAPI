from sqlalchemy import Column, String, Integer, Float
from .database import Base


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postcode = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)
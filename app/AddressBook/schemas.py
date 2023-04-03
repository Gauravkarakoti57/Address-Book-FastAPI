from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    name : str
    contact : str
    address : str
    city : str
    state : str
    country : str
    postcode : str
    latitude : float
    longitude : float

class ShowAddress(Address):
    
    class Config:
        orm_mode = True


class User(BaseModel):
    name : str
    password : str
    email : str
    

class ShowUser(BaseModel):
    name : str
    email : str
    class Config:
        orm_mode = True


class Login(BaseModel):
    username : str
    password : str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
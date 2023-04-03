from fastapi import APIRouter, Depends, status, Response
from typing import List
from .. import schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import address
from databases import Database
from .. import models
import math, string

router = APIRouter(
    prefix='/address',
    tags=['Addresses']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowAddress)
def create(request: schemas.Address, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return address.create(request, db)

@router.get("/all",status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAddress])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return address.get_all(db)

@router.get("/{id}",status_code=status.HTTP_200_OK, response_model=schemas.ShowAddress)
def show(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return address.show(id,db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return address.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Address, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return address.update(id, request, db)

@router.get("/{lat}/{long}/{distance}",status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAddress])
def get_address_in_distance(lat: float,long : float, distance: float, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    addresses_list = []
    addresses = db.query(models.Address).all()
    for temp_address in addresses:
        distance = address.haversine(float(temp_address.latitude), float(temp_address.longitude), lat, long, distance)
        if distance:
            addresses_list.append(temp_address)
    return addresses_list
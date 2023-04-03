from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
import math

def get_all(db: Session):
    addresses = db.query(models.Address).all()
    return addresses

def create(request: schemas.Address,db: Session):
    new_address = models.Address(name = request.name, contact = request.contact, address = request.address,
                city = request.city, state = request.state, country = request.country, postcode = request.postcode,
                latitude = request.latitude, longitude = request.longitude)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def destroy(id:int,db: Session):
    address = db.query(models.Address).filter(models.Address.id == id)

    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")

    address.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Address, db:Session):
    address = db.query(models.Address).filter(models.Address.id == id)

    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")

    address.update(request.dict())
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    address = db.query(models.Address).filter(models.Address.id == id).first()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with the id {id} is not available")
    return address

def haversine(latitude, longitude, lat, lon, distance):
     
    # distance between latitudes
    # and longitudes
    dLat = (lat - latitude) * math.pi / 180.0
    dLon = (lon - lon) * math.pi / 180.0
 
    # convert to radians
    latitude = (latitude) * math.pi / 180.0
    lat = (lat) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(latitude) * math.cos(longitude))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    if distance < rad * c:
        return True
    else:
        return False
#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel,Base
from  sqlalchemy import *
from sqlalchemy.orm import relationship
 
place_amenity = Table('place_amenity',Base.metadata,
                        Column('place_id',String(60),ForeignKey("places.id"),primary_key=True,nullable=False),
                        Column('amenity_id',String(60),ForeignKey("amenities.id",primarykey=True,nullable=False)),
                       )
class Place(BaseModel):
    """ A place to stay """

    amenities = relationship('Amenity',secondary='place_amenity',
                                backref="place_amenities",viewonly=False)

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import from Base


class Amenity(BaseModel):
    """
    class attributes
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullbase=False)
    place_amenities
    

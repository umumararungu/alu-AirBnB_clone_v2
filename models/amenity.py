#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlarchemy import *
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    class attributes
    """
    if models.storage_t == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullbase=False)
    else:
        name = ""
    

    

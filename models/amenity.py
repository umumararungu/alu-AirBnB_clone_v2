#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlarchemy import *
=======
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

<<<<<<< HEAD
class Amenity(BaseModel):
    """
    class attributes
    """
    if models.storage_t == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullbase=False)
    else:
        name = ""
    

    
=======

class Amenity(BaseModel, Base):
    """Represents an amenity data set."""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

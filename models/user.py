#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
=======
from sqlalchemy import Column, String, ForeignKey
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD

    __tablename__ = "users"
=======
    __tablename__ = 'users'
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    places = relationship("Place", backref="user", cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
=======

    places = relationship(
        'Place',
        cascade='all, delete-orphan',
        backref='user')
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from .city import City
=======
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

Base = declarative_base()

<<<<<<< HEAD

class State(BaseModel, Base):
    """State class"""

    engine = create_engine("mysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db")

    session = sessionmaker(bind=engine)()

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Getter for list of all `City` objects when in file storage
            mode.
            """
            from . import storage

            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
=======
class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace(".", " ")
            city = shlex.split(city)
            if city[0] == "City":
                lista.append(var[key])
        for elem in lista:
            if elem.state_id == self.id:
                result.append(elem)
        return result
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
